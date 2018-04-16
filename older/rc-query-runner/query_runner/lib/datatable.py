"""Simple helper class to access a data table"""
import logging
from .misc import NONE_VALUES

LOG = logging.getLogger(__name__)


class DataTableRow(dict):
    # Get and set attributes like row.prop, but store them in cells for datatable

    def __init__(self, data=None):
        super(DataTableRow, self).__init__()
        if data is None:
            data = {}
        self["cells"] = data.get("cells", {})
        self["id"] = data.get("id")

    def __getattr__(self, name):
        if name == "id":
            return self["id"]
        elif name == "cells":
            return self["cells"]
        elif name in self["cells"]:
            return self["cells"][name]["value"]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        if name == "id":
            self["id"] = value
        elif name == "cells":
            self["cells"] = value
        else:
            self["cells"][name] = {"value": value}

    def __delattr__(self, name):
        if name in self["cells"]:
            del self["cells"][name]
        else:
            raise AttributeError("No such attribute: " + name)


class DataTable(object):

    def __init__(self, res_client, table_name=None):
        self.res_client = res_client
        self.table_name = table_name
        self.table_id = None
        self.tabledef = None

    def _get_tabledef(self):
        if self.tabledef is None:
            tabledef_url = "/types/{0}".format(self.table_name)
            self.tabledef = self.res_client.get(tabledef_url)
        return self.tabledef

    def get_field_types(self):
        return {field_def["name"]: field_def["input_type"] for field_def in self._get_tabledef()["fields"].values()}

    def get_columns(self):
        return self._get_tabledef()["fields"].keys()

    def get_required_columns(self):
        return [field["name"] for field in self._get_tabledef()["fields"].values() if field.get("required") == "always"]

    def rows(self, incident_id):
        # Get the row data.  Always get names, not select ids.
        table_url = "/incidents/{}/table_data/{}?handle_format=names".format(incident_id, self.table_name)
        table_data = {"rows": []}
        try:
            table_data = self.res_client.get(table_url)
        except:
            # The return doesn't distinguish between "no such datatable" and "no rows".
            # Validate by fetching metadata.  If that fails, throw it.  Otherwise, return an empty row set.
            self.get_columns()
        return table_data["rows"]

    def match(self, rows, key_dict, limit=1):
        """Find the rows that match all of the specified key fields"""
        matching_rows = []
        for row in rows:
            # All key fields must match
            match = True
            for (k, v) in key_dict.items():
                if row["cells"].get(k, {}).get("value", None) != v:
                    match = False
                    break
            if match:
                matching_rows.append(row)
            if limit and len(matching_rows) == limit:
                break
        return matching_rows

    def find_rows(self, incident_id,key_dict, limit=1):
        """Find the rows that match all of the specified conditions"""
        rows = self.rows(incident_id)
        matching_rows = self.match(rows, key_dict, limit=limit)
        return matching_rows

    def find_row(self, incident_id, row_id):
        """Find the row with a specific id"""
        rows = self.rows(incident_id)
        for row in rows:
            if row["id"] == row_id:
                return row
        return None

    def add_row(self, incident_id, datarow):
        table_url = "/incidents/{}/table_data/{}/row_data?handle_format=names".format(incident_id, self.table_name)
        row_data = self.res_client.post(table_url, datarow)
        return row_data

    def update(self, incident_id, row, updated_row, co3_context_token=None):
        row["cells"].update(updated_row["cells"])
        row_id = row["id"]
        table_url = "/incidents/{}/table_data/{}/row_data/{}?handle_format=names".format(incident_id, self.table_name, row_id)
        row_data = self.res_client.put(table_url, row, co3_context_token=co3_context_token)
        return row_data

    def update_row(self, incident_id, datarow, co3_context_token=None):
        row = self.find_row(incident_id, datarow["id"])
        if row is None:
            raise Exception("Cannot update, row {} not found".format(datarow["id"]))
        return self.update(row, incident_id, datarow, co3_context_token=co3_context_token)

    def delete_row(self, incident_id, datarow_id, co3_context_token=None):
        table_url = "/incidents/{}/table_data/{}/row_data/{}".format(incident_id, self.table_name, datarow_id)
        status = self.res_client.delete(table_url, co3_context_token=co3_context_token)
        return status

    def update_cell_value_types(self, dt_row):
        """ Fix the values in a dt row to be numeric or list where appropriate """
        dt_field_types = self.get_field_types()
        for key, value in dt_row["cells"].items():
            value = value["value"]
            if value in NONE_VALUES:
                value = None
            elif dt_field_types[key]  in ("datepicker", "datetimepicker", "number"):
                try:
                    value = int(value)
                except ValueError as e:
                    value = None
                    LOG.exception("Field %s should be numeric! %s", key, e)
                    LOG.error("Mapping for field %s skipped due to invalid integer value", key)
            elif dt_field_types[key]  in ("multiselect", "multiselect_members"):
                # Convert the value to a list
                if not isinstance(value, list):
                    value = [value]
            elif dt_field_types[key] == "boolean":
                # Convert the value to True or False
                if value == "True":
                    value = True
                elif value == "False":
                    value = False
                else:
                    raise ValueError("Datatable Field [%s] Value [%s] not valid boolean value", key, value)

            dt_row["cells"][key]["value"] = value

    @staticmethod
    def cell(row, name):
        return row["cells"][name]["value"]
