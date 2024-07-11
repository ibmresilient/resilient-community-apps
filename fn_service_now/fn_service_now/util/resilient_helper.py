# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

"""ResilientHelper Module"""

import base64
import json
from logging import getLogger
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from resilient import SimpleHTTPException
from resilient_lib import RequestsCommon, IntegrationError

unicode = str

CONFIG_DATA_SECTION = "fn_service_now"
CP4S_CASES_REST_PREFIX = "cases-rest"

SN_STATE_COLOR_MAP = {
    "New": "green",
    "Active": "green",
    "In Progress": "orange",
    "On Hold": "yellow",
    "Resolved": "red",
    "Closed": "red",
    "Canceled": "red",
    "Cancelled": "red",

    # colors for security incidents states
    "Draft": "green",
    "Assigned": "blue",
    "Analysis": "orange",
    "Contain": "yellow",
    "Eradicate": "yellow",
    "Recover": "yellow",
    "Work In Progress": "yellow",
    "Review": "red",
    "Closed Complete": "red"
}

COLORS_HEX_MAP = {
    "green": "#00b33c",
    "blue": "#89CFF0",
    "orange": "#ff9900",
    "yellow": "#e6e600",
    "red": "#e60000"
}

LOG = getLogger(__name__)

# Define an Incident that gets sent to ServiceNow
class Incident(object):
    """Class that represents a SOAR Incident. See API notes for more"""
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
    """Class that represents a SOAR Task. See API notes for more"""
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
    def __init__(self, opts, app_configs):

        LOG.debug("Initializing ResilientHelper")

        self.app_configs = app_configs

        self.rc = RequestsCommon(opts, app_configs)

        self._sn_host = self._get_config_option("sn_host", placeholder="https://instance.service-now.com")

        self._sn_table_name = str(self._get_config_option("sn_table_name", optional=True, placeholder="incident"))
        self._sn_username = str(self._get_config_option("sn_username", placeholder="<ServiceNow Username>"))
        # Handle password surrounded by ' or "
        pwd = str(self._get_config_option("sn_password", placeholder="<ServiceNow Password>"))
        if (pwd.startswith("'") and pwd.endswith("'")) or (pwd.startswith('"') and pwd.endswith('"')):
            self._sn_password = pwd[1:-1]
        else:
            self._sn_password = pwd

        # https://instance.service-now.com/api/x_ibmrt_resilient/api
        self._sn_api_uri = self._get_config_option("sn_api_uri")
        self._base_api_url = urljoin(self.host, self.api_uri)

        self._sn_api_auth = (self.username, self._sn_password)

        self._cp4s_prefix = self._get_config_option("cp4s_cases_prefix", placeholder=CP4S_CASES_REST_PREFIX, optional=True)

        # Default headers
        self.headers = {"Content-Type": "application/json", "Accept": "application/json"}

        LOG.debug("ResilientHelper initialized")
        LOG.debug("App Configs: sn_host: %s sn_api_uri: %s sn_api_url: %s sn_table_name: %s sn_username: %s cp4s_cases_prefix: %s", self.host, self.api_uri, self._base_api_url, self.table_name, self.username, self._cp4s_prefix)

    @property
    def host(self):
        return self._sn_host

    @property
    def api_uri(self):
        return self._sn_api_uri

    @property
    def username(self):
        return self._sn_username

    @property
    def table_name(self):
        return self._sn_table_name

    @classmethod
    def _byteify(cls, data):
        """Function to handle json.loads object_hook for supporting Python 3"""
        data_as_utf8_str = data

        if isinstance(data, unicode):
            data_as_utf8_str = data.encode("utf-8")

            # if Python 3.x data_as_utf8_str will be bytes, so we convert back to str
            if isinstance(data_as_utf8_str, bytes):
                data_as_utf8_str = data_as_utf8_str.decode(("utf-8"))

        elif isinstance(data, dict):
            data_as_utf8_str = {cls._byteify(key): cls._byteify(value) for key, value in data.items()}

        return data_as_utf8_str

    @staticmethod
    def _encodeBase64(str_to_encode):
        """A helper function to encode a base64 string for Python 3 support"""
        str_to_encode = base64.b64encode(str_to_encode)
        return str_to_encode.decode("utf-8")

    def _get_config_option(self, option_name, optional=False, placeholder=None):
        """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
        option = self.app_configs.get(option_name, placeholder)
        err = f"'{option_name}' is mandatory and is not set in app.config file. You must set this value to run this function"

        if not option and optional is False:
            raise ValueError(err)
        elif optional is False and placeholder and option == placeholder:
            raise ValueError(err)
        else:
            return option

    @staticmethod
    def get_function_input(inputs, input_name, optional=False):
        """Given input_name, checks if it defined. Raises ValueError if a mandatory input is None"""
        LOG.debug("Trying to get function input: %s from %s. optional = %s", input_name, inputs, optional)

        the_input = inputs.get(input_name)

        if the_input is None and optional is False:
            err = f"'{input_name}' is a mandatory function input"
            raise ValueError(err)
        else:
            LOG.debug("Got function input: %s", input_name)
            return the_input

    @staticmethod
    def generate_res_id(incident_id, task_id=None, sn_res_id=None):
        """If incident_id and task_id are valid, returns "RES-1001-2002"
        Else if task_id is None, returns "RES-1001". If sn_res_id if defined
        just return it. """

        # If sn_res_id is defined, just return it. This helps us with closing from Data Table
        if sn_res_id:
            return sn_res_id

        res_id = ["RES", str(incident_id)]
        if task_id:
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

    def generate_res_link(self, incident_id, host, org_id, task_id=None):
        """Function that generates a https URL to the incident or task"""

        # for CP4S cases endpoint, remove the cases-rest prefix (CP4S_CASES_REST_PREFIX)
        if self._cp4s_prefix in host:
            base_host = host.replace(self._cp4s_prefix + ".", "")
            link = f"https://{base_host}/app/respond/#cases/{incident_id}"
        else:
            link = f"https://{host}/#incidents/{incident_id}"

        if task_id:
            link += f"?taskId={task_id}&tabName=details&orgId={org_id}"

        return link

    def generate_sn_link(self, sn_query, sn_table_name=None):
        """Function that generates a URL to the record in ServiceNow"""
        if not sn_table_name:
            sn_table_name = self.table_name

        # https://xxxx.service-now.com/nav_to.do?uri=incident.do?sysparm_query=number=INC0000009
        uri = f"{self.host}/nav_to.do?uri={sn_table_name}.do?sysparm_query={sn_query}"
        return uri

    @staticmethod
    def convert_text_to_richtext(text, color_name="green"):
        """Converts text to richtext and adds a color"""

        # default to green if not given or not found in the colors dict
        if color_name not in COLORS_HEX_MAP:
            LOG.warning("Converting to richtext. Using default color 'green' because given color '%s' was not found in color dictionary", color_name)
            color_name = "green"

        # because of above check, we don't need a default here because that is handled above
        color_hex_code = COLORS_HEX_MAP.get(color_name)

        # wrap the text with the color in HTML and return
        return f"""<div style="color:{color_hex_code}">{text}</div>"""

    @staticmethod
    def state_to_text(state):
        """Converts O/A to Active and C to Closed"""
        if state == "O" or state == "A":
            return "Active"
        elif state == "C":
            return "Closed"
        else:
            raise ValueError(f"{state} is not a valid SOAR State. O=Open Task, A=Active Incident, C=Closed Incident/Task")

    @staticmethod
    def get_incident(client, incident_id):
        """Function that gets the incident from SOAR"""
        err_msg = None
        get_url = f"/incidents/{incident_id}?text_content_output_format=always_text&handle_format=names"

        # Get the incident from resilient api
        try:
            LOG.debug("GET Incident from SOAR: ID %s URL: %s", incident_id, get_url)
            incident = client.get(get_url)
            LOG.debug("Incident got successfully: %s", incident)
        except Exception as err:
            err_msg = f"Error trying to get Incident {incident_id}."
            if hasattr(err, "message") and "not found" in err.message.lower():
                err_msg = f"{err_msg} Could not find Incident with ID {incident_id}"
            elif isinstance(err, SimpleHTTPException):
                err_msg = f"{err_msg}\nServer Error.\nStatus Code: {err.response.status_code}\nURL: {err.response.url}\n{err.message}"
            else:
                err_msg = f"{err_msg} {err}"

            raise ValueError(err_msg) from err

        return Incident(incident_id, incident["name"], incident["description"])

    @staticmethod
    def rename_incident(client, incident_id, new_incident_name):
        """
        Static function to update the name of a incident.
        Primarily used for prepending sn_ref_id to the incident's name
        for easy filtering when viewing incident list
        """

        def change_func(data):
            data["name"] = new_incident_name

        url = f"/incidents/{incident_id}?handle_format=names"

        # Use the get_put option to GET the data, apply the change, and PUT it back to the server
        try:
            LOG.debug("PUT Incident from SOAR: ID: %s URL: %s New Name: %s", incident_id, url, new_incident_name)
            client.get_put(url, change_func)
            LOG.info("Incident was successfully renamed to '%s'", new_incident_name)
        except Exception as err:
            raise ValueError(str(err)) from err

    @staticmethod
    def get_task(client, task_id, incident_id):
        """Function that gets the task from SOAR. Gets the task's instructions too"""
        err_msg = None

        # Get the task from resilient api
        try:
            get_url = f"/tasks/{task_id}?text_content_output_format=always_text&handle_format=names"
            LOG.debug("GET Task from SOAR: ID %s URL: %s", task_id, get_url)
            task = client.get(get_url)
            LOG.debug("Task got successfully: %s", task)
        except Exception as err:
            err_msg = f"Error trying to get Task {task_id}."

            if hasattr(err, "message") and "not found" in err.message.lower():
                err_msg = f"{err_msg} Could not find Task with ID {task_id}"
            elif isinstance(err, SimpleHTTPException):
                err_msg = f"{err_msg}\nServer Error.\nStatus Code: {err.response.status_code}\nURL: {err.response.url}\n{err.message}"
            else:
                err_msg = f"{err_msg} {err}"

            raise ValueError(err_msg) from err

        # Get the task_instructions in plaintext
        try:
            get_url = f"/tasks/{task_id}/instructions_ex"
            LOG.debug("GET task_instructions for: ID %s URL: %s", task_id, get_url)
            task_instructions = client.get_content(get_url)
            soup = BeautifulSoup(unicode(task_instructions, "utf-8"), "html.parser")
            soup = soup.get_text()
            # BeautifulSoup decoding of the HTML includes quotation marks and non-breaking spaces
            # so we need to remove those for the instructions text that will go to SNOW
            task_instructions = soup.replace("\xa0", " ").replace('"','').replace("\\n", "\n")
            LOG.debug("task_instructions got successfully")
        except Exception as err:
            err_msg = f"Error trying to get task_instructions for Task {task_id}."

            if isinstance(err, SimpleHTTPException):
                err_msg = f"{err_msg}\nServer Error.\nStatus Code: {err.response.status_code}\nURL: {err.response.url}\n{err.message}"
            else:
                err_msg = f"{err_msg} {err}"

            raise ValueError(err_msg) from err

        return Task(incident_id, task_id, task["name"], task_instructions)

    @staticmethod
    def rename_task(client, task_id, new_task_name):
        """
        Static function to update the name of a task.
        Primarily used for prepending sn_ref_id to the task's name
        for easy filtering when viewing task list
        """

        def change_func(data):
            data["name"] = new_task_name

        url = f"/tasks/{task_id}?handle_format=names"

        # Use the get_put option to GET the data, apply the change, and PUT it back to the server
        try:
            LOG.debug(f"PUT Task from SOAR: ID: {task_id} URL: {url} New Name: {new_task_name}")
            client.get_put(url, change_func)
            LOG.info(f"Task was successfully renamed to '{new_task_name}'", )
        except Exception as err:
            raise ValueError(str(err))


    @classmethod
    def get_attachment(cls, res_client, attachment_id, incident_id=None, task_id=None):
        """Function that gets incident/task attachment"""
        attachment = {"id": None, "name": None, "content_type": None, "contents": None}
        err_msg, get_url = None, None

        # Get attachment metadata url
        if task_id:
            get_url = f"/tasks/{task_id}/attachments/{attachment_id}"
        elif incident_id:
            get_url = f"/incidents/{incident_id}/attachments/{attachment_id}"
        else:
            raise ValueError("Failed to get_attachment. task_id or incident_id must be specified with attachment_id")

        # Get attachment metadata
        try:
            LOG.debug(f"GET Attachment metadata: ID {attachment_id} URL: {get_url}")
            meta_data = res_client.get(get_url)
            LOG.debug("Attachment metadata got successfully")
        except Exception as err:
            err_msg = f"Error trying to get Attachment {attachment_id}."

            if hasattr(err, "message") and "not found" in err.message.lower():
                err_msg = f"{err_msg} Could not find Attachment with ID {attachment_id}. incident_id: {incident_id} task_id: {task_id}"
            elif isinstance(err, SimpleHTTPException):
                err_msg = f"{err_msg}\nServer Error.\nStatus Code: {err.response.status_code}\nURL: {err.response.url}\n{err.message}"
            else:
                err_msg = f"{err_msg} {err}"

            raise ValueError(err_msg) from err

        attachment["content_type"] = meta_data["content_type"]
        attachment["id"] = attachment_id
        attachment["name"] = meta_data["name"]

        # Get attachment contents url
        get_contents_url = f"{get_url}/contents"

        # Get attachment contents
        try:
            LOG.debug(f"GET Attachment contents: ID {attachment_id} URL: {get_url}")
            attachment["contents"] = cls._encodeBase64(res_client.get_content(get_contents_url))
            LOG.debug("Attachment contents got successfully")
        except Exception as err:
            err_msg = f"Error trying to get Attachment contents for ID: {attachment_id}."

            if hasattr(err, "message") and "not found" in err.message.lower():
                err_msg = f"{err_msg} Could not find Attachment with ID {attachment_id}. incident_id: {incident_id} task_id: {task_id}"
            elif isinstance(err, SimpleHTTPException):
                err_msg = f"{err_msg}\nServer Error.\nStatus Code: {err.response.status_code}\nURL: {err.response.url}\n{err.message}"
            else:
                err_msg = f"{err_msg} {err}"

            raise ValueError(err_msg) from err

        return attachment

    def generate_sn_request_data(self, res_client, res_datatable, incident_id, res_link, sn_table_name=None, task_id=None, init_note=None, sn_optional_fields=None):
        """Function that generates the data that is sent in the request to the /create endpoint in ServiceNow"""
        err_msg, request_data = None, None

        if not sn_table_name:
            sn_table_name = self.table_name

        if res_link:
            init_note += "\nSOAR link: " + res_link

        LOG.debug("Generating request for ServiceNow. incident_id: %s task_id: %s sn_table_name: %s res_link: %s init_note: %s sn_optional_fields: %s res_datatable: %s", incident_id, task_id, sn_table_name, res_link, init_note, sn_optional_fields, res_datatable)

        # Generate the res_id
        res_id = self.generate_res_id(incident_id, task_id)

        LOG.debug("res_id: %s", res_id)

        # Check if already exists in data table
        sn_ref_id = res_datatable.get_sn_ref_id(res_id)

        if sn_ref_id:
            err_msg = "Failed to create a ServiceNow Record. This {0} already exists in ServiceNow. {0} ID: {1}. sn_ref_id: {2}"

            if task_id:
                err_msg = err_msg.format("Task", task_id, sn_ref_id)

            else:
                err_msg = err_msg.format("Incident", incident_id, sn_ref_id)

            return {
                "success": False,
                "data": err_msg
            }

        if task_id:
            # Get the task
            task = self.get_task(res_client, task_id, incident_id)

            # Add task to the request_data
            request_data = task.as_dict()

        else:
            incident = self.get_incident(res_client, incident_id)

            # Add incident to the request_data
            request_data = incident.as_dict()

        # Add sn_table_name, resilient_id, link and init_note to the request_data
        request_data["sn_table_name"] = sn_table_name
        request_data["id"] = res_id
        request_data["link"] = res_link
        request_data["sn_init_work_note"] = init_note

        # Extend request_data if there is data in 'sn_optional_fields'
        if sn_optional_fields and len(sn_optional_fields) > 0:
            fields = []
            for field in sn_optional_fields:
                fields.append({"name": field, "value": sn_optional_fields[field]})
            request_data["sn_optional_fields"] = fields
        else:
            request_data["sn_optional_fields"] = None

        LOG.debug(f"sn_request_data {request_data}")

        return {
            "success": True,
            "data": request_data
        }

    def get_table_name(self, fn_table_name_input=None):
        if fn_table_name_input:
            return fn_table_name_input

        return self.table_name

    def sn_api_request(self, method, endpoint, params=None, data=None, headers=None, return_whole_response_obj=False, callback=None):
        """Method to handle requests to our custom APIs in ServiceNow"""
        res, return_value = None, None

        SUPPORTED_METHODS = ["GET", "POST", "PATCH"]

        if method not in SUPPORTED_METHODS:
            raise ValueError(f"{method} is not a supported ServiceNow API Request. Supported methods are: {SUPPORTED_METHODS}")

        headers = self.headers if headers is None else headers
        url = f"{self._base_api_url}{endpoint}"

        if callback is None:
            callback = default_callback_for_sn_request

        res = self.rc.execute(
            method=method,
            url=url,
            auth=self._sn_api_auth,
            headers=headers,
            params=params,
            data=json.dumps(data),
            callback=callback
        )

        LOG.info("SN REQUEST:\nmethod: %s\nurl: %s\nbody: %s",
                 res.request.method,
                 res.request.url,
                 res.request.body)

        if method == "GET" or return_whole_response_obj:
            LOG.info("SN RESPONSE: %s", res)
            return_value = res

        elif method in ("POST", "PATCH"):
            LOG.info("SN RESPONSE: %s", res.json())
            return_value = res.json()["result"]

        return return_value

    def test_connection(self):
        """
        Test connection to ServiceNow with given configs.

        Selftest function implements the specific handling of the response.

        :return: response object
        :rtype: request.Response
        """
        return self.sn_api_request(
            "POST",
            "/test_connection",
            data={"sn_table_name": self.table_name},
            return_whole_response_obj=True,
            callback=lambda x:x # noop callback so that we can handle error messages ourselves rather than raise_for_status
        )


def default_callback_for_sn_request(response):
    """
    Because ServiceNow returns custom error objects with non-200 codes,
    we have to handle the requests differently than requests.raise_for_status()
    does.

    For a 404 response, the response body will be something like:

        {
            "error": {
                "detail": "...",
                "message": "..."
            },
            "status": "failure"
        }

    Read https://developer.servicenow.com/dev.do#!/learn/learning-plans/washingtondc/servicenow_application_developer/app_store_learnv2_rest_washingtondc_scripted_rest_api_error_objects
    for details

    :param response: response object from call; remember that it could be success, in which case, we just return it
    :type response: requests.Response
    :raises IntegrationError: when >= 300 codes are returned, with error message parsed into IntegrationError object
    :return: response object if < 300 code returned
    :rtype: requests.Response
    """
    status_code = response.status_code

    if status_code < 300:
        return response

    if response is not None and hasattr(response, "content"):
        response_result = json.loads(response.content)
        err_msg = response_result["error"]["message"]
        err_detail = response_result["error"]["detail"]
    else:
        err_msg = "Could not connect to ServiceNow"
        err_detail = "Unknown"

    err_msg = f"{status_code} Client Error: {err_msg}"
    if err_detail:
        err_msg += f" Detail: {err_detail}"

    raise IntegrationError(err_msg)
