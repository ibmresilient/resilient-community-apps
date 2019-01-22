# (c) Copyright IBM Corp. 2019. All Rights Reserved.
"""ResilientHelper Module"""
import base64
import json
from bs4 import BeautifulSoup
import requests


class ResilientHelper(object):
    """A helper class for sn_utilities"""
    def __init__(self, app_configs):
        self.app_configs = app_configs

        self.SN_HOST = self.get_config_option("sn_host")
        self.SN_API_URI = self.get_config_option("sn_api_uri")

        # https://service-now-host.com/api/<app-name>/<custom-api-name/
        self.SN_API_URL = "{0}{1}".format(self.SN_HOST, self.SN_API_URI)
        self.SN_TABLE_NAME = str(self.get_config_option("sn_table_name"))
        self.SN_USERNAME = str(self.get_config_option("sn_username"))

        # Handle password surrounded by ' or "
        pwd = str(self.get_config_option("sn_password"))
        if (pwd.startswith("'") and pwd.endswith("'")) or (pwd.startswith('"') and pwd.endswith('"')):
            self.SN_PASSWORD = pwd[1:-1]
        else:
            self.SN_PASSWORD = pwd

        self.SN_AUTH = (self.SN_USERNAME, self.SN_PASSWORD)

        # Default headers
        self.headers = {"Content-Type": "application/json", "Accept": "application/json"}

    def get_config_option(self, option_name, optional=False):
        """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
        option = self.app_configs.get(option_name)

        if not option and optional is False:
            err = "'{0}' is mandatory and is not set in app.config file. You must set this value to run this function".format(option_name)
            raise ValueError(err)
        else:
            return option

    @staticmethod
    def get_function_input(inputs, input_name, optional=False):
        """Given input_name, checks if it defined. Raises ValueError if a mandatory input is None"""
        the_input = inputs.get(input_name)

        if the_input is None and optional is False:
            err = "'{0}' is a mandatory function input".format(input_name)
            raise ValueError(err)
        else:
            return the_input

    @staticmethod
    def get_attachment(res_client, attachment_id, incident_id=None, task_id=None):
        """Function that gets incident/task attachment"""
        attachment = {"id": None, "name": None, "content_type": None, "contents": None}
        meta_data_uri, contents_uri = None, None

        if task_id:
            meta_data_uri = "/tasks/{0}/attachments/{1}".format(task_id, attachment_id)
            contents_uri = "/tasks/{0}/attachments/{1}/contents".format(task_id, attachment_id)
        elif incident_id:
            meta_data_uri = "/incidents/{0}/attachments/{1}".format(incident_id, attachment_id)
            contents_uri = "/incidents/{0}/attachments/{1}/contents".format(incident_id, attachment_id)
        else:
            raise ValueError("Failed to get_attachment. task_id or incident_id must be specified with attachment_id")

        meta_data = res_client.get(meta_data_uri)

        attachment["content_type"] = meta_data["content_type"]
        attachment["id"] = attachment_id
        attachment["name"] = meta_data["name"]
        attachment["contents"] = base64.b64encode(res_client.get_content(contents_uri))

        return attachment

    @staticmethod
    def generate_res_id(incident_id, task_id=None):
        """If incident_id and task_id are valid, returns "RES-1001-2002"
        Else if task_id is None, returns "RES-1001" """

        res_id = ["RES", str(incident_id)]
        if task_id is not None:
            res_id.append(str(task_id))
        return "-".join(res_id)

    @staticmethod
    def generate_res_link(incident_id, host, task_id=None):
        """Function that generates a https URL to the incident or task"""

        link = "https://{0}/#incidents/{1}".format(host, incident_id)

        if task_id is not None:
            link += "?task_id={0}".format(task_id)

        return link

    def generate_sn_link(self, sn_query, sn_table_name=None):
        """Function that generates a URL to the record in ServiceNow"""
        if not sn_table_name:
            sn_table_name = self.SN_TABLE_NAME

            # https://devxxxx.service-now.com/nav_to.do?uri=incident.do?sysparm_query=number=INC0000009
            uri = "{0}/nav_to.do?uri={1}.do?sysparm_query={2}".format(self.SN_HOST, sn_table_name, sn_query)
        return uri

    @staticmethod
    def generate_sn_request_data(res_client, res_helper, res_datatable, incident_id, sn_table_name, res_link, task_id=None, init_note=None, sn_optional_fields=None):
        """Function that generates the data that is sent in the request to the /create endpoint in ServiceNow"""
        request_data = None

        # Generate the res_id
        res_id = res_helper.generate_res_id(incident_id, task_id)

        # Check if already exists in data table
        sn_ref_id = res_datatable.get_sn_ref_id(res_id)

        if sn_ref_id:
            err_msg = "Failed to create in ServiceNow. This {0} already exists in ServiceNow. {0} ID: {1}. sn_ref_id: {2}"

            if task_id:
                err_msg = err_msg.format("Task", task_id, sn_ref_id)

            else:
                err_msg = err_msg.format("Incident", incident_id, sn_ref_id)

            raise ValueError(err_msg)

        if task_id is not None:
            # Get the task
            task = res_helper.get_task(res_client, task_id, incident_id)

            # Add task to the request_data
            request_data = task.as_dict()

        else:
            incident = res_helper.get_incident(res_client, incident_id)

            # Add incident to the request_data
            request_data = incident.as_dict()

        # Add sn_table_name, resilient_id, link and init_note to the request_data
        request_data["sn_table_name"] = sn_table_name
        request_data["id"] = res_id
        request_data["link"] = res_link
        request_data["sn_init_work_note"] = init_note

        # Extend request_data if there is data in 'sn_optional_fields'
        if sn_optional_fields is not None and len(sn_optional_fields) > 0:
            fields = []
            for field in sn_optional_fields:
                fields.append({"name": field, "value": sn_optional_fields[field]})
            request_data["sn_optional_fields"] = fields
        else:
            request_data["sn_optional_fields"] = None

        return request_data

    @staticmethod
    def convert_text_to_richtext(text, color="green"):
        """Converts text to richtext and adds a color"""

        colors = {
            "green": "#00b33c",
            "orange": "#ff9900",
            "yellow": "#e6e600",
            "red": "#e60000"
        }

        color = colors.get(color)

        return """<div style="color:{0}">{1}</div>""".format(color, text)

    def sn_POST(self, url, data, auth=None, headers=None):
        """Function to handle POSTing to ServiceNow. If successful, returns the response as a Dictionary"""
        if headers is None:
            headers = self.headers

        if auth is None:
            auth = self.SN_AUTH

        url = self.SN_API_URL + url

        return_json = None

        try:
            response = requests.post(url, auth=auth, headers=headers, data=data)
            response.raise_for_status()

            return_json = response.json()['result']

        except requests.exceptions.Timeout:
            raise ValueError('Request to ServiceNow timedout')

        except requests.exceptions.TooManyRedirects:
            raise ValueError('A bad url request', url)

        except requests.exceptions.HTTPError as err:
            if err.response.content:
                custom_error_content = json.loads(err.response.content)
                raise ValueError(custom_error_content['error']['message'])
            else:
                raise ValueError(err)
        except requests.exceptions.RequestException as err:
            raise ValueError(err)

        return return_json

    def sn_GET(self, url, params=None, auth=None, headers=None):
        """Method to handle a ServiceNow GET request"""
        if headers is None:
            headers = self.headers

        if auth is None:
            auth = self.SN_AUTH

        url = self.SN_API_URL + url

        try:
            response = requests.get(url, auth=auth, headers=headers, params=params)
        except Exception as err:
            raise ValueError("ServiceNow GET failed. Check url, credentials and params.", err)

        return response

    # Define a Task that gets sent to ServiceNow
    class Task(object):
        """Class that represents a Resilient Task. See API notes for more"""
        def __init__(self, incident_id, task_id, task_name, task_instructions):
            self.type = "res_task"
            self.incident_id = incident_id
            self.task_id = task_id
            self.task_name = task_name
            self.task_instructions = task_instructions

        def as_dict(self):
            """Returns this class as a Dictionary"""
            return self.__dict__

    def get_task(self, client, task_id, incident_id):
        """Function that gets the task from Resilient. Gets the task's instructions too"""
        # Get the task from resilient api
        try:
            task = client.get("/tasks/{0}?text_content_output_format=always_text&handle_format=names".format(task_id))
        except:
            raise ValueError("task_id {0} not found".format(task_id))

        # Get the task_instructions in plaintext
        try:
            task_instructions = client.get_content("/tasks/{0}/instructions".format(task_id))
            soup = BeautifulSoup(unicode(task_instructions, "utf-8"), 'html.parser')
            soup = soup.get_text()
            task_instructions = soup.replace(u'\xa0', u' ')
        except:
            raise ValueError("Error getting task instructions")

        return self.Task(incident_id, task_id, task["name"], task_instructions)

    # Define an Incident that gets sent to ServiceNow
    class Incident(object):
        """Class that represents a Resilient Incident. See API notes for more"""
        def __init__(self, incident_id, incident_name, incident_description):
            self.type = "res_incident"
            self.incident_id = incident_id
            self.incident_name = incident_name
            self.incident_description = incident_description

        def as_dict(self):
            """Returns this class object as a dictionary"""
            return self.__dict__

    def get_incident(self, client, incident_id):
        """Function that gets the incident from Resilient"""
        # Get the incident from resilient api
        try:
            incident = client.get("/incidents/{0}?text_content_output_format=always_text&handle_format=names".format(incident_id))
        except:
            raise ValueError("incident_id {0} not found".format(incident_id))

        return self.Incident(incident_id, incident["name"], incident["description"])


class ExternalTicketStatusDatatable(object):
    """Class that handles the sn_external_ticket_status datatable"""
    def __init__(self, res_client, incident_id):
        self.res_client = res_client
        self.incident_id = incident_id
        self.api_name = "sn_external_ticket_status"
        self.data = None
        self.rows = None

        self.get_data()

    def as_dict(self):
        """Returns this class object as a dictionary"""
        return self.__dict__

    def get_data(self):
        """Gets that data and rows of the data table"""
        uri = "/incidents/{0}/table_data/{1}?handle_format=names".format(self.incident_id, self.api_name)
        try:
            self.data = self.res_client.get(uri)
            self.rows = self.data["rows"]
        except Exception as err:
            raise ValueError("Failed to get sn_external_ticket_status Datatable", err)

    def get_row(self, cell_name, cell_value):
        """Returns the row if found. Returns None if no matching row found"""
        for row in self.rows:
            cells = row["cells"]
            if cells[cell_name] and cells[cell_name].get("value") and cells[cell_name].get("value") == cell_value:
                return row
        return None

    def get_sn_ref_id(self, res_id):
        """Returns the sn_ref_id that relates to the res_id"""
        row = self.get_row("res_id", res_id)

        if row is not None:
            cells = row["cells"]
            return str(cells["sn_ref_id"]["value"])

        return None

    def add_row(self, time, res_id, sn_ref_id, resilient_status, servicenow_status, link):
        """Adds a new row to the data table and returns that row"""
        # Generate uri to POST datatable row
        uri = "/incidents/{0}/table_data/{1}/row_data?handle_format=names".format(self.incident_id, self.api_name)

        cells = [
            ("time", time),
            ("res_id", res_id),
            ("sn_ref_id", sn_ref_id),
            ("resilient_status", resilient_status),
            ("servicenow_status", servicenow_status),
            ("link", link)
        ]

        formatted_cells = {}

        # Format the cells
        for cell in cells:
            formatted_cells[cell[0]] = {"value": cell[1]}

        formatted_cells = {
            "cells": formatted_cells
        }

        return self.res_client.post(uri, formatted_cells)

    def update_row(self, row, cells_to_update):
        """Updates the row with the given cells_to_update and returns the updated row"""
        # Generate uri to POST datatable row
        uri = "/incidents/{0}/table_data/{1}/row_data/{2}?handle_format=names".format(self.incident_id, self.api_name, row["id"])

        def get_value(cell_name):
            """Gets the new or old value of the cell"""
            if cell_name in cells_to_update:
                return cells_to_update[cell_name]

            return row["cells"][cell_name]["value"]

        cells = [
            ("time", get_value("time")),
            ("res_id", get_value("res_id")),
            ("sn_ref_id", get_value("sn_ref_id")),
            ("resilient_status", get_value("resilient_status")),
            ("servicenow_status", get_value("servicenow_status")),
            ("link", get_value("link"))
        ]

        formatted_cells = {}

        # Format the cells
        for cell in cells:
            formatted_cells[cell[0]] = {"value": cell[1]}

        formatted_cells = {
            "cells": formatted_cells
        }

        return self.res_client.put(uri, formatted_cells)
