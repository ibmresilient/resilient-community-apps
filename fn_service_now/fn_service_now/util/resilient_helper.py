# (c) Copyright IBM Corp. 2019. All Rights Reserved.
"""ResilientHelper Module"""
import logging
import base64
import json
from bs4 import BeautifulSoup
import requests
import six
from resilient_circuits import StatusMessage
from resilient import SimpleHTTPException

# Handle unicode in 2.x and 3.x
try:
    unicode
except NameError:
    unicode = str

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


class ResilientHelper(object):
    """A helper class for sn_utilities"""
    def __init__(self, app_configs):

        log = logging.getLogger(__name__)
        log.debug("Initializing ResilientHelper")

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

        log.debug("ResilientHelper initialized")
        log.debug("App Configs: sn_host: %s sn_api_uri: %s sn_api_url: %s sn_table_name: %s sn_username: %s",
            self.SN_HOST, self.SN_API_URI, self.SN_API_URL, self.SN_TABLE_NAME, self.SN_USERNAME)

    @classmethod
    def _byteify(cls, data):
        """Function to handle json.dumps and json.loads object_hook for supporting Python 2 and 3"""

        if six.PY2:
            if isinstance(data, unicode):
                return data.encode("utf-8")

            elif isinstance(data, dict):
                return {cls._byteify(key): cls._byteify(value) for key, value in data.items()}

            return None

        elif six.PY3:
            data_as_utf8_str = None

            if isinstance(data, unicode):
                data_as_utf8_str = data.encode("utf-8")

                # if Python 3.x data_as_utf8_str will be bytes, so we convert back to str
                if isinstance(data_as_utf8_str, bytes):
                    data_as_utf8_str = data_as_utf8_str.decode(("utf-8"))

            elif isinstance(data, dict):
                data_as_utf8_str = {cls._byteify(key): cls._byteify(value) for key, value in data.items()}

            return data_as_utf8_str
        else:
            raise ValueError("We do not support this version of Python")

    @staticmethod
    def _encodeBase64(str_to_encode):
        """A helper function to encode a base64 string for Python 3 and 3 support"""
        if six.PY2:
            return base64.b64encode(str_to_encode)

        elif six.PY3:
            str_to_encode = base64.b64encode(str_to_encode)
            return str_to_encode.decode("utf-8")

        else:
            raise ValueError("We do not support this version of Python")

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

        log = logging.getLogger(__name__)
        log.debug("Trying to get function input: %s from %s. optional = %s", input_name, inputs, optional)

        the_input = inputs.get(input_name)

        if the_input is None and optional is False:
            err = "'{0}' is a mandatory function input".format(input_name)
            raise ValueError(err)
        else:
            log.debug("Got function input: %s", input_name)
            return the_input

    @staticmethod
    def generate_res_id(incident_id, task_id=None, sn_res_id=None):
        """If incident_id and task_id are valid, returns "RES-1001-2002"
        Else if task_id is None, returns "RES-1001". If sn_res_id if defined
        just return it. """

        # If sn_res_id is defined, just return it. This helps us with closing from Data Table
        if sn_res_id is not None:
            return sn_res_id

        res_id = ["RES", str(incident_id)]
        if task_id is not None:
            res_id.append(str(task_id))
        return "-".join(res_id)

    @staticmethod
    def parse_res_id(res_id):
        """Parse res_id (RES-1001-2002) and return a dict with incident_id and task_id"""
        incident_id, task_id = None, None
        ids = res_id.split("-")

        incident_id = ids[1]
        if len(ids) == 3:
            task_id = ids[2]

        return {"incident_id": incident_id, "task_id": task_id}

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

    @staticmethod
    def state_to_text(state):
        """Converts O/A to Active and C to Closed"""
        if state == "O" or state == "A":
            return "Active"
        elif state == "C":
            return "Closed"
        else:
            raise ValueError("{0} is not a valid Resilient State. O=Open Task, A=Active Incident, C=Closed Incident/Task".format(state))

    @staticmethod
    def get_incident(client, incident_id):
        """Function that gets the incident from Resilient"""

        log = logging.getLogger(__name__)
        err_msg = None
        get_url = "/incidents/{0}?text_content_output_format=always_text&handle_format=names".format(incident_id)

        # Get the incident from resilient api
        try:
            log.debug("GET Incident from Resilient: ID %s URL: %s", incident_id, get_url)
            incident = client.get(get_url)
            log.debug("Incident got successfully: %s", incident)
        except Exception as err:
            err_msg = "Error trying to get Incident {0}.".format(incident_id)

            if err.message and "not found" in err.message.lower():
                err_msg = "{0} Could not find Incident with ID {1}".format(err_msg, incident_id)
            elif isinstance(err, SimpleHTTPException):
                err_msg = "{0}\nServer Error.\nStatus Code: {1}\nURL: {2}\n{3}".format(err_msg, err.response.status_code, err.response.url, err.message)
            else:
                err_msg = "{0} {1}".format(err_msg, err)

            raise ValueError(err_msg)

        return Incident(incident_id, incident["name"], incident["description"])

    @staticmethod
    def get_task(client, task_id, incident_id):
        """Function that gets the task from Resilient. Gets the task's instructions too"""

        log = logging.getLogger(__name__)
        err_msg = None

        # Get the task from resilient api
        try:
            get_url = "/tasks/{0}?text_content_output_format=always_text&handle_format=names".format(task_id)
            log.debug("GET Task from Resilient: ID %s URL: %s", task_id, get_url)
            task = client.get(get_url)
            log.debug("Task got successfully: %s", task)
        except Exception as err:
            err_msg = "Error trying to get Task {0}.".format(task_id)

            if err.message and "not found" in err.message.lower():
                err_msg = "{0} Could not find Task with ID {1}".format(err_msg, task_id)
            elif isinstance(err, SimpleHTTPException):
                err_msg = "{0}\nServer Error.\nStatus Code: {1}\nURL: {2}\n{3}".format(err_msg, err.response.status_code, err.response.url, err.message)
            else:
                err_msg = "{0} {1}".format(err_msg, err)

            raise ValueError(err_msg)


        # Get the task_instructions in plaintext
        try:
            get_url = "/tasks/{0}/instructions".format(task_id)
            log.debug("GET task_instructions for: ID %s URL: %s", task_id, get_url)
            task_instructions = client.get_content(get_url)
            soup = BeautifulSoup(unicode(task_instructions, "utf-8"), 'html.parser')
            soup = soup.get_text()
            task_instructions = soup.replace(u'\xa0', u' ')
            log.debug("task_instructions got successfully")
        except Exception as err:
            err_msg = "Error trying to get task_instructions for Task {0}.".format(task_id)

            if isinstance(err, SimpleHTTPException):
                err_msg = "{0}\nServer Error.\nStatus Code: {1}\nURL: {2}\n{3}".format(err_msg, err.response.status_code, err.response.url, err.message)
            else:
                err_msg = "{0} {1}".format(err_msg, err)

            raise ValueError(err_msg)


        return Task(incident_id, task_id, task["name"], task_instructions)

    @classmethod
    def get_attachment(cls, res_client, attachment_id, incident_id=None, task_id=None):
        """Function that gets incident/task attachment"""

        log = logging.getLogger(__name__)
        attachment = {"id": None, "name": None, "content_type": None, "contents": None}
        err_msg, get_url = None, None

        # Get attachment metadata url
        if task_id:
            get_url = "/tasks/{0}/attachments/{1}".format(task_id, attachment_id)
        elif incident_id:
            get_url = "/incidents/{0}/attachments/{1}".format(incident_id, attachment_id)
        else:
            raise ValueError("Failed to get_attachment. task_id or incident_id must be specified with attachment_id")

        # Get attachment metadata
        try:
            log.debug("GET Attachment metadata: ID %s URL: %s", attachment_id, get_url)
            meta_data = res_client.get(get_url)
            log.debug("Attachment metadata got successfully")
        except Exception as err:
            err_msg = "Error trying to get Attachment {0}.".format(attachment_id)

            if err.message and "not found" in err.message.lower():
                err_msg = "{0} Could not find Attachment with ID {1}. incident_id: {2} task_id: {3}".format(err_msg, attachment_id, incident_id, task_id)
            elif isinstance(err, SimpleHTTPException):
                err_msg = "{0}\nServer Error.\nStatus Code: {1}\nURL: {2}\n{3}".format(err_msg, err.response.status_code, err.response.url, err.message)
            else:
                err_msg = "{0} {1}".format(err_msg, err)

            raise ValueError(err_msg)

        attachment["content_type"] = meta_data["content_type"]
        attachment["id"] = attachment_id
        attachment["name"] = meta_data["name"]

        # Get attachment contencts url
        get_contents_url = "{0}/contents".format(get_url)

        # Get attachment contents
        try:
            log.debug("GET Attachment contents: ID %s URL: %s", attachment_id, get_url)
            attachment["contents"] = cls._encodeBase64(res_client.get_content(get_contents_url))
            log.debug("Attachment contents got successfully")
        except Exception as err:
            err_msg = "Error trying to get Attachment contents for ID: {0}.".format(attachment_id)

            if err.message and "not found" in err.message.lower():
                err_msg = "{0} Could not find Attachment with ID {1}. incident_id: {2} task_id: {3}".format(err_msg, attachment_id, incident_id, task_id)
            elif isinstance(err, SimpleHTTPException):
                err_msg = "{0}\nServer Error.\nStatus Code: {1}\nURL: {2}\n{3}".format(err_msg, err.response.status_code, err.response.url, err.message)
            else:
                err_msg = "{0} {1}".format(err_msg, err)

        return attachment

    @classmethod
    def generate_sn_request_data(cls, res_client, res_datatable, incident_id, sn_table_name, res_link, task_id=None, init_note=None, sn_optional_fields=None):
        """Function that generates the data that is sent in the request to the /create endpoint in ServiceNow"""

        log = logging.getLogger(__name__)
        err_msg, request_data = None, None

        log.debug("Generating request for ServiceNow. incident_id: %s task_id: %s sn_table_name: %s res_link: %s init_note: %s sn_optional_fields: %s res_datatable: %s",
            incident_id, task_id, sn_table_name, res_link, init_note, sn_optional_fields, res_datatable)

        # Generate the res_id
        res_id = cls.generate_res_id(incident_id, task_id)

        log.debug("res_id: {0}".format(res_id))

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
            task = cls.get_task(res_client, task_id, incident_id)

            # Add task to the request_data
            request_data = task.as_dict()

        else:
            incident = cls.get_incident(res_client, incident_id)

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

        log.debug("sn_request_data %s", request_data)

        return request_data

    def sn_GET(self, url, params=None, auth=None, headers=None):
        """Method to handle a ServiceNow GET request"""

        log = logging.getLogger(__name__)
        err_msg, response_content = None, None

        if headers is None:
            headers = self.headers

        if auth is None:
            auth = self.SN_AUTH

        url = "{0}{1}".format(self.SN_API_URL, url)

        try:
            log.debug("GET Request to ServiceNow. url: %s headers: %s params: %s", url, headers, params)
            response = requests.get(url, auth=auth, headers=headers, params=params)
            response.raise_for_status()
            log.debug("GET Request successful")

        except requests.exceptions.Timeout:
            err_msg = "GET request to ServiceNow timedout"
            raise ValueError(err_msg)

        except requests.exceptions.TooManyRedirects:
            err_msg = "Too Many Redirects for: {0}".format(url)
            raise ValueError(err_msg)

        except requests.exceptions.HTTPError as err:
            if err.response.content:
                response_content = json.loads(err.response.content)
                err_msg = response_content["error"]["message"]
                raise ValueError(err_msg)
            else:
                raise ValueError(err)

        except requests.exceptions.RequestException as err:
            raise ValueError(err)

        return response

    def sn_POST(self, url, data, auth=None, headers=None):
        """Method to handle ServiceNow POST request. If successful, returns the response as a Dictionary"""
        
        log = logging.getLogger(__name__)
        return_json, err_msg, response_content = None, None, None

        if headers is None:
            headers = self.headers

        if auth is None:
            auth = self.SN_AUTH

        url = "{0}{1}".format(self.SN_API_URL, url)

        try:
            log.debug("POST Request to ServiceNow. url: %s headers: %s data: %s", url, headers, data)
            response = requests.post(url, auth=auth, headers=headers, data=data)
            response.raise_for_status()
            log.debug("POST Request successful")

            return_json = response.json()['result']

        except requests.exceptions.Timeout:
            err_msg = "GET request to ServiceNow timedout"
            raise ValueError(err_msg)

        except requests.exceptions.TooManyRedirects:
            err_msg = "Too Many Redirects for: {0}".format(url)
            raise ValueError(err_msg)

        except requests.exceptions.HTTPError as err:
            if err.response.content:
                response_content = json.loads(err.response.content)
                err_msg = response_content["error"]["message"]
                raise ValueError(err_msg)
            else:
                raise ValueError(err)

        except requests.exceptions.RequestException as err:
            raise ValueError(err)

        except requests.exceptions.RequestException as err:
            raise ValueError(err)

        return return_json
