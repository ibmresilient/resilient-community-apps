# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#!/usr/bin/env python

"""Export data to JSON"""

import co3 as resilient
import collections
import json
import logging
import os
import pytz
import re
import getpass
import html2text
import collections
from datetime import datetime, timedelta
from calendar import timegm

LOG = logging.getLogger(__name__)


# The config file location should usually be set in the environment
APP_CONFIG_FILE = os.environ.get("APP_CONFIG_FILE", "app.config")
# Resolve config values from keyring if specified
import resilient_circuits.keyring_arguments as keyring_arguments
from resilient_circuits.rest_helper import get_resilient_client


OBJECT_TYPES = {
    "incident": 0,
    "task": 1,
    "note": 2,
    "milestone": 3,
    "artifact": 4,
    "attachment": 5
}


class ExportArgumentParser(keyring_arguments.ArgumentParser):
    def __init__(self):
        super(ExportArgumentParser, self).__init__(config_file=APP_CONFIG_FILE)

        self.add_argument('filename',
                          help="The spreadsheet filename.")

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


def get_datetime(ts):
    """datetime from epoch timestamp"""
    if ts:
        return datetime.fromtimestamp(int(int(ts)/1000))


def get_field_value_label(field, value):
    for val in field["values"]:
        if val["value"] == value:
            return val["label"]
    return None

def filter_htmltext(str):
    original_string = str
    try:
        str = html2text.html2text(str)
        str = str.strip('\n')
    except Exception as e:
        return original_string
    return str

def convert_epoch_to_datetimestr(epoch, milliseconds):
    if epoch is None:
        return None
    if milliseconds:
        epoch /= 1000

    return datetime.fromtimestamp(epoch).isoformat()

class ExportContext(object):
    def __init__(self, opts):
        self.opts = opts

        # Create SimpleClient and connect
        self.client = get_resilient_client(self.opts)
        self.client.connect(opts.email, opts.password)

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
       
            for thefield in thefields:
                if fieldlist == [] or thefield["name"] in fieldlist:
                    self.fields[objecttype][thefield["name"]] = thefield

        # Allows for ID to string conversion
        self.types = self.client.get("/types")

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


    def clean_schema(self, object, typename):
        for field in list(object.keys()):
            if not self.get_field(typename, field):
                if field == "properties":
                    continue
                object.pop(field, None)

    def get_name_from_id(self, id):
        for type in self.types:
            if int(self.types[type]["id"]) == int(id):
                return type

        return ""

    def get_column_name_from_id(self, tablename, columnid):
        for column_name in self.types[tablename]["fields"]:
            column = self.types[tablename]["fields"][column_name]
            if int(column["id"]) == int(columnid):
                return column_name

        return ""

    def process_datatables(self, datatables, id):
        """Process datatable info from API"""
        new_data_table = []
        for data_table_id in datatables:
            table_name = self.get_name_from_id(data_table_id)

            data_table = datatables[data_table_id]

            for row in data_table["rows"]:
                temp_items = []
                for cell_id in row["cells"]:
                    cell = row["cells"][cell_id]
                    temp_items.append({"id": cell["id"], "value": cell["value"]})

                temp_items.sort(key=lambda x: x["id"], reverse=False)

                temp_row = {}
                for cell in temp_items:
                    column_name = self.get_column_name_from_id(table_name, cell["id"])
                    if column_name == "":
                        continue
                    temp_row["incident_id"] = id
                    temp_row[column_name] = cell["value"]


                new_data_table.append(temp_row)

        return new_data_table


    def get_incidents(self):
        """Yield all the incidents"""
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

        query = {"filters": [{"conditions": conditions}]}
        LOG.debug(json.dumps(query, indent=2))
        incidents = self.client.post("/incidents/query?return_level=partial", query)
        if specific_ids:
            incidents = [i for i in incidents if i["id"] in specific_ids]
        for incident in incidents:
            full_incident = self.client.get("/incidents/{}?handle_format=names&text_content_output_format=always_text".format(incident["id"]))
            self.clean_schema(full_incident, "incident")

            
            yield full_incident


    def get_tasks(self, incident):
        """Yield all the tasks"""
        tasks = self.client.get("/incidents/{}/tasks?handle_format=names&text_content_output_format=always_text".format(incident["id"]))
        for task in tasks:
            task["instr_text"] = filter_htmltext(task["instr_text"])

            task["closed_date"] = convert_epoch_to_datetimestr(task["closed_date"], True)
            task["due_date"] = convert_epoch_to_datetimestr(task["due_date"], True)

            self.clean_schema(task, "task")
            yield task


    def get_notes(self, incident):
        """Yield all the notes"""
        notes = self.client.get("/incidents/{}/comments?handle_format=names&text_content_output_format=always_text".format(incident["id"]))
        for note in notes:
            self.clean_schema(note, "note")
            yield note


    def get_milestones(self, incident):
        """Yield all the milestones"""
        milestones = self.client.get("/incidents/{}/milestones?handle_format=names&text_content_output_format=always_text".format(incident["id"]))
        for milestone in milestones:
            self.clean_schema(milestone, "milestone")
            yield milestone


    def get_artifacts(self, incident):
        """Yield all the artifacts"""
        artifacts = self.client.get("/incidents/{}/artifacts?handle_format=names&text_content_output_format=always_text".format(incident["id"]))
        for artifact in artifacts:
            self.clean_schema(artifact, "artifact")
            yield artifact


    def get_attachments(self, incident):
        """Yield all the attachments"""
        attachments = self.client.get("/incidents/{}/attachments?handle_format=names&text_content_output_format=always_text".format(incident["id"]))
        for attachment in attachments:
            self.clean_schema(attachment, "attachment")
            yield attachment

    def get_datatables(self, incident):
        data_tables = self.client.get("/incidents/{}/table_data".format(incident["id"]))
        return self.process_datatables(data_tables, incident["id"])


    def export_data(self):
        """Do the export"""

        filename = self.opts.get("filename")

        # generators do not provide a length
        incident_count = 0
        with open(filename, "w") as outfile:
            incidents = self.get_incidents()
            incidents_list = []
            datatable_list = []
            for incident in incidents:
                incident_count += 1
                incident["tasks"] = list(self.get_tasks(incident))
                incident["notes"] = list(self.get_notes(incident))
                incident["milestones"] = list(self.get_milestones(incident))
                incident["artifacts"] = list(self.get_artifacts(incident))
                incident["attachments"] = list(self.get_attachments(incident))

                incident["create_date"] = convert_epoch_to_datetimestr(incident["create_date"], True)
                incident["due_date"] = convert_epoch_to_datetimestr(incident["due_date"], True)
                incident["end_date"] = convert_epoch_to_datetimestr(incident["end_date"], True)
                incident["discovered_date"] = convert_epoch_to_datetimestr(incident["discovered_date"], True)
                incident["start_date"] = convert_epoch_to_datetimestr(incident["start_date"], True)

                datatable_list.append(self.get_datatables(incident))

                incidents_list.append(incident)

            json.dump({"incidents":incidents_list, "data_tables": datatable_list}, outfile)
            outfile.write("\n")

        print("{} incidents written to {}".format(incident_count, filename))
        return filename


    def export_json(self):
        """Export incidents to a file"""
        return self.export_data()


def main():
    """Main"""
    # Parse commandline arguments
    if not APP_CONFIG_FILE:
        print("Error, APP_CONFIG_FILE environment variable is not defined.")
        return None

    parser = ExportArgumentParser()
    opts = parser.parse_args()

    # Export the data
    export_context = ExportContext(opts)
    filename = export_context.export_json()

    print("Done.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
