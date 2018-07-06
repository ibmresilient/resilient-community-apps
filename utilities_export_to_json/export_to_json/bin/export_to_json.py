# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#!/usr/bin/env python

"""Export data to JSON"""

import resilient
import collections
import json
import logging
import os
import collections
import re
import time
from datetime import datetime, timedelta
from calendar import timegm

LOG = logging.getLogger(__name__)

OBJECT_TYPES = {
    "incident": 0,
    "task": 1,
    "note": 2,
    "milestone": 3,
    "artifact": 4,
    "attachment": 5
}

LAST_RUN_FILE = ".resilient_export_to_json_lastrun"

class ExportArgumentParser(resilient.ArgumentParser):
    def __init__(self, config_file=None):
        super(ExportArgumentParser, self).__init__(config_file=config_file)

        self.add_argument('filename',
                          help="The JSON filename.")

        self.add_argument('last_modified_field_name',
                          help="Name of a custom field that holds the last-modified timestamp")

        self.add_argument("--since",
                          type=valid_date_or_days_ago,
                          help="Only report incidents created after this date (YYYY-MM-DD) or days ago")

        self.add_argument("--until",
                          type=valid_date_or_days_ago,
                          help="Only report incidents created on or before this date (YYYY-MM-DD) or days ago")

        self.add_argument('--incident',
                          type=int,
                          nargs="*",
                          help="The id(s) of specific incident(s) to export.")

        self.add_argument('--field',
                          nargs="*",
                          help="The field name(s) to export.")

        self.add_argument('--query',
                          help="Filename containing a query in JSON format.")


def valid_date_or_days_ago(s):
    """Validation function for date parameters, expects YYYY-MM-DD or just N"""
    # Try date format first
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        pass
    # Try just a plain number
    try:
        return int(s)
    except ValueError:
        msg = "Date must be YYYY-MM-DD, or a number of days in the past: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


def get_json_time_or_days_ago(dt):
    """Epoch timestamp from datetime"""
    if isinstance(dt, int):
        # means: a number of days ago
        td = timedelta(dt)
        dt = datetime.now() - td
    return timegm(dt.utctimetuple()) * 1000

def filter_htmltext(str):
    """Removes rich text from a string"""
    original_string = str
    try:
        return re.sub(re.compile('<.*?>'), '', str)
    except Exception as e:
        return original_string
    return str

def convert_epoch_to_datetimestr(epoch, milliseconds):
    """Converts epoch time into a datetime object"""
    if epoch is None:
        return None
    if type(epoch) is not int:
        try:
            epoch = int(epoch)
        except Exception:
            return epoch
    if milliseconds:
        epoch /= 1000

    return datetime.fromtimestamp(epoch).isoformat()

class ExportContext(object):
    """Responsible for exporting Resilient data into a JSON formatted file"""
    def __init__(self, opts):
        self.opts = opts

        # Create SimpleClient and connect
        self.client = resilient.get_client(opts)

        if not self.client:
            raise Exception("Resilient Client is not valid.")

        # Build a catalog of all the field definitions
        # If opts specifies a restricted list of fields, only include the ones specified.
        fieldlist = opts.field or []

        self.rows = {}
        self.fields = {}
        for objecttype in OBJECT_TYPES.keys():
            # Add the "id" field
            self.fields[objecttype] = {"name": "id", "input_type": "id", "text": "id"}
            # Then get the actual defined fields
            thefields = self.client.get("/types/{}/fields".format(objecttype))
            if not thefields:
                raise Exception("Unable to get fields from REST API")

            for thefield in thefields:
                if fieldlist == [] or thefield["name"] in fieldlist:
                    self.fields[objecttype][thefield["name"]] = thefield

        # Allows for ID to string conversion
        self.types = self.client.get("/types")
        if not self.types:
            raise Exception("Unable to get Resilient types")

        # The list of users and groups is available via the owner_id field
        # (or members, equivalently)
        # (the full list of users and groups is only available to admins)
        owner_field = self.get_field("incident", "owner_id")
        self.users_lookup = {value["value"]: value["label"] for value in owner_field["values"]}


    def get_field(self, objecttype, fieldname):
        """Find a field definition, by api-name"""
        try:
            return self.fields[objecttype][fieldname]
        except KeyError:
            return None

    def is_date(self, objecttype, fieldname):
        """Checks the type of field"""        
        field = self.get_field(objecttype, fieldname)
        if not field:
            return False

        if field.get("input_type") and field.get("input_type") == "datetimepicker":
            return True

        return False

    def clean_schema(self, object, typename):
        """Creates a new object referencing the fields of the type"""
        type_fields = self.types.get(typename)
        if type_fields is None:
            return {}

        type_fields = type_fields.get("fields")
        if type_fields is None:
            return {}

        new_object = {}

        for field_name in type_fields:
            field = type_fields.get(field_name)
            if not field:
                continue

            prefix = field.get("prefix")

            shouldConvertToDatetime = False
            if self.is_date(typename, field_name):
                shouldConvertToDatetime = True

            try:
                if prefix is None:
                    new_object[field_name] = object[field_name]
                    if shouldConvertToDatetime:
                        new_object[field_name] = convert_epoch_to_datetimestr(new_object[field_name], True)
                else:
                    new_object[prefix][field_name] = object[prefix][field_name]
                    if shouldConvertToDatetime:
                        new_object[prefix][field_name] = convert_epoch_to_datetimestr(new_object[prefix][field_name], True)
            except KeyError:
                continue

        return new_object

    def get_name_from_id(self, id):
        """Converts an ID provided by the REST API into the string it represents"""
        for type in self.types:
            if int(self.types[type].get("id")) == int(id):
                return type

        return ""

    def get_column_name_from_id(self, tablename, columnid):
        """Converts a field ID to the field name"""
        for column_name in self.types[tablename]["fields"]:
            column = self.types[tablename]["fields"][column_name]
            if int(column["id"]) == int(columnid):
                return column_name

        return ""

    def process_datatables(self, datatables, id):
        """Process datatable info from API"""
        new_data_table = {}
        for data_table_id in datatables:
            table_name = self.get_name_from_id(data_table_id)
            if table_name == "":
                continue

            new_data_table[table_name] = []
            data_table = datatables[data_table_id]

            for row in data_table.get("rows"):
                temp_items = []
                for cell_id in row.get("cells"):
                    cell = row["cells"][cell_id]
                    temp_items.append({"id": cell.get("id"), "value": cell.get("value")})

                temp_items.sort(key=lambda x: x.get("id"), reverse=False)

                temp_row = {}
                for cell in temp_items:
                    column_name = self.get_column_name_from_id(table_name, cell.get("id"))
                    if column_name == "":
                        continue

                    temp_row[column_name] = cell.get("value")

                new_data_table[table_name].append(temp_row)

        return new_data_table

    def get_partial_incident_data(self, last_run_time):
        specific_ids = self.opts.get("incident")
        created_since_date_or_days_ago = self.opts.get("since")
        created_until_date_or_days_ago = self.opts.get("until")

        # Query is more efficient than just reading the full description of every incident.
        # But caution: by default, it only returns the partial incident DTO.
        conditions = [{"field_name": "inc_training", "method": "equals", "value": False}]
        if self.opts.get("query"):
            with open(self.opts.get("query"), 'r') as template_file:
                conditions = json.loads(template_file.read())
        if created_since_date_or_days_ago:
            conditions.append({"field_name": "create_date", "method": "gt", "value": get_json_time_or_days_ago(created_since_date_or_days_ago)})
        if created_until_date_or_days_ago:
            conditions.append({"field_name": "create_date", "method": "lte", "value": get_json_time_or_days_ago(created_since_date_or_days_ago)})
        if last_run_time:
            conditions.append({"field_name":("properties." + self.opts.get("last_modified_field_name")), "method": "gt", "value": last_run_time})

        query = {"filters": [{"conditions": conditions}]}

        incidents = self.client.post("/incidents/query?return_level=partial", query)
        if specific_ids:
            incidents = [i for i in incidents if i["id"] in specific_ids]

        return incidents

    def get_basic_incident_data(self):
        if not os.path.isfile(LAST_RUN_FILE):
            return self.get_partial_incident_data(None)

        with open(LAST_RUN_FILE, "r") as lastrun_file:
            data = lastrun_file.read().replace("\n", "")

        try:
            last_run_time = int(data)
        except Exception:
            return self.get_partial_incident_data(None)

        return self.get_partial_incident_data(last_run_time)

    def get_incidents(self):
        """Yield all the incidents"""
        incidents = self.get_basic_incident_data()
        for incident in incidents:
            full_incident = self.client.get("/incidents/{}?handle_format=names&text_content_output_format=always_text".format(incident["id"]))
            if full_incident.get("id") is None:
                raise Exception("Incident data corrupted, \"id\" attribute is non-existent.")

            properties = full_incident.get("properties")
            last_modified_field = properties.get(self.opts.get("last_modified_field_name"))

            full_incident = self.clean_schema(full_incident, "incident")

            full_incident["last_modified_etj"] = last_modified_field
            yield full_incident


    def get_tasks(self, incident):
        """Yield all the tasks"""
        tasks = self.client.get("/incidents/{}/tasks?handle_format=names&text_content_output_format=always_text".format(incident["id"]))
        for task in tasks:
            task["instr_text"] = filter_htmltext(task.get("instr_text"))
            task["closed_date"] = convert_epoch_to_datetimestr(task.get("closed_date"), True)
            task["due_date"] = convert_epoch_to_datetimestr(task.get("due_date"), True)

            task = self.clean_schema(task, "task")
            yield task


    def get_notes(self, incident):
        """Yield all the notes"""
        notes = self.client.get("/incidents/{}/comments?handle_format=names&text_content_output_format=always_text".format(incident["id"]))
        for note in notes:
            note = self.clean_schema(note, "note")
            yield note


    def get_milestones(self, incident):
        """Yield all the milestones"""
        milestones = self.client.get("/incidents/{}/milestones?handle_format=names&text_content_output_format=always_text".format(incident["id"]))
        for milestone in milestones:
            milestone = self.clean_schema(milestone, "milestone")
            yield milestone


    def get_artifacts(self, incident):
        """Yield all the artifacts"""
        artifacts = self.client.get("/incidents/{}/artifacts?handle_format=names&text_content_output_format=always_text".format(incident["id"]))
        for artifact in artifacts:
            artifact = self.clean_schema(artifact, "artifact")
            yield artifact


    def get_attachments(self, incident):
        """Yield all the attachments"""
        attachments = self.client.get("/incidents/{}/attachments?handle_format=names&text_content_output_format=always_text".format(incident["id"]))
        for attachment in attachments:
            attachment = self.clean_schema(attachment, "attachment")
            yield attachment

    def get_datatables(self, incident):
        """Grabs datatables from REST API and processes them"""
        data_tables = self.client.get("/incidents/{}/table_data".format(incident["id"]))
        return self.process_datatables(data_tables, incident["id"])


    def export_data(self):
        """Formalize the export to JSON"""

        filename = self.opts.get("filename")
        if not filename:
            raise Exception("Filename is invalid.")

        # generators do not provide a length
        incident_count = 0
        existing_incidents = None
        if os.path.isfile(filename):
            with open(filename, "r") as export_file:
                try:
                    existing_incidents = json.loads(export_file.read().replace("\n", ""))
                except Exception:
                    existing_incidents = {}
            os.remove(filename)

        if os.path.isfile(LAST_RUN_FILE):
            with open(LAST_RUN_FILE, "r") as lastrun_file:
                file_last_time = lastrun_file.read().replace("\n", "")
        else:
            file_last_time = 0

        highest_last_modified = int(file_last_time)
        with open(filename, "w") as outfile:
            incidents = self.get_incidents()
            incidents_list = []
            datatable_list = []
            for incident in incidents:
                if incident.get("id") is None:
                    raise Exception("Incident data corrupted, \"id\" attribute is non-existent.")

                incident_count += 1
                incident["tasks"] = list(self.get_tasks(incident))
                incident["notes"] = list(self.get_notes(incident))
                incident["milestones"] = list(self.get_milestones(incident))
                incident["artifacts"] = list(self.get_artifacts(incident))
                incident["attachments"] = list(self.get_attachments(incident))
                
                data_tables = self.get_datatables(incident)
                for data_table_name in data_tables:
                    incident[data_table_name] = data_tables[data_table_name]

                if incident.get("last_modified_etj") is not None:
                    last_modified_time = incident.get("last_modified_etj")

                    if type(last_modified_time) is str:
                        try:
                            last_modified_time = int(last_modified_time)
                        except Exception:
                            incident.pop("last_modified_etj", None)
                            incidents_list.append(incident)  
                            continue

                    if last_modified_time > highest_last_modified:
                        highest_last_modified = last_modified_time

                    incident.pop("last_modified_etj", None)

                incidents_list.append(incident)

            if not existing_incidents:
                json.dump({"incidents":incidents_list}, outfile)
                outfile.write("\n")
            else:
                for i, existing_incident in enumerate(existing_incidents.get("incidents")):
                    for updated_incident in incidents_list:
                        if existing_incident.get("id") == updated_incident.get("id") and existing_incident.get("id") is not None:
                            existing_incidents["incidents"][i] = updated_incident
                            break

                for updated_incident in incidents_list:
                    if existing_incidents.get("incidents") is None:
                        break
                    if updated_incident.get("id") is None:
                        continue

                    incidents = existing_incidents.get("incidents")

                    found_incident = False
                    for incident in incidents:
                        if incident.get("id") == updated_incident.get("id"):
                            found_incident = True
                            break

                    if found_incident is False:
                        existing_incidents["incidents"].append(updated_incident)
 
                json.dump(existing_incidents, outfile)
                outfile.write("\n")

        with open(LAST_RUN_FILE, "w") as outfile:
            epoch_time = highest_last_modified
            outfile.write(str(epoch_time))

        print("{} incidents written to {}".format(incident_count, filename))
        return filename


    def export_json(self):
        """Export incidents to a file"""
        return self.export_data()


def main():
    """Main"""
    parser = ExportArgumentParser(config_file=resilient.get_config_file())
    opts = parser.parse_args()

    # Export the data
    export_context = ExportContext(opts)
    filename = export_context.export_json()

    print("Done.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
