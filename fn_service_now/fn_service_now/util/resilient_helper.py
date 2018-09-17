# (c) Copyright IBM Corp. 2018. All Rights Reserved.
import requests
import os
import base64
from bs4 import BeautifulSoup
import json
import csv
try:
    # for Python 2.x
    from StringIO import StringIO
except ImportError:
    # for Python 3.x
    from io import StringIO

class ResilientHelper:

  # Define a Task that gets sent to ServiceNow
  class Task:
    """Class that repersents a Resilient Task. See API notes for more"""
    def __init__(self, incident_id, task_id, task_name, task_instructions,
                task_creator, task_owner):
      self.type = "res_task"
      self.incident_id = incident_id
      self.task_id = task_id
      self.task_name = task_name
      self.task_instructions = task_instructions
      self.task_creator = task_creator
      self.task_owner = task_owner

    def asDict(self):
      return self.__dict__

  def get_task(self, client, task_id, incident_id):
    """Function that gets the task from Resilient. Gets the task's instructions too and any optional fields"""
    # Get the task from resilient api
    try:
      task = client.get("/tasks/{0}?text_content_output_format=always_text&handle_format=names".format(task_id))
    except:
      # TODO: Better error
      raise ValueError("task_id {0} not found".format(task_id))
    
    # Get the task_instructions in plaintext
    try:
      task_instructions = client.get_content("/tasks/{0}/instructions".format(task_id))
      soup = BeautifulSoup(unicode(task_instructions, "utf-8"), 'html.parser')
      soup = soup.get_text()
      task_instructions = soup.replace(u'\xa0', u' ')
    except:
      raise ValueError("Error getting task instructions")

    # Get the task creator and owner
    task_creator = {
      "name": "{0} {1}".format(task["creator"]["fname"], task["creator"]["lname"]),
      "email": task["creator"]["email"]
    }
    task_owner = {
      "name": "{0} {1}".format(task["owner_fname"], task["owner_lname"]),
      "email": task["owner_id"]
    }

    return self.Task(incident_id, task_id, task["name"], task_instructions,
                    task_creator, task_owner)

  # Define an Incident that gets sent to ServiceNow
  class Incident:
    """Class that repersents a Resilient Incident. See API notes for more"""
    def __init__(self, incident_id, incident_name, incident_description, incident_serverity,
                 incident_creator, incident_date_created):

      self.type = "res_incident"
      self.incident_id = incident_id
      self.incident_name = incident_name
      self.incident_description = incident_description
      self.incident_severity = incident_serverity
      self.incident_creator = incident_creator
      self.incident_date_created = incident_date_created

    def add_work_note(self, note):
      self.sn_init_work_note = note

    def asDict(self):
      return self.__dict__

  def get_incident(self, client, incident_id, optional_fields_wanted=None):
    """Function that gets the incident from Resilient and any optional fields"""
    # Get the incident from resilient api
    try:
      incident = client.get("/incidents/{0}?text_content_output_format=always_text&handle_format=names".format(incident_id))
    except:
      # TODO Better error
      raise ValueError("incident_id {0} not found".format(incident_id))

    incident_creator = {
      "name": "{0} {1}".format(incident["creator"]["fname"], incident["creator"]["lname"]),
      "email": incident["creator"]["email"]
    }

    incident_severity = str(incident["severity_code"]).lower()
    if incident_severity == "high":
      incident_severity = 1
    elif incident_severity == "medium":
      incident_severity = 2
    elif incident_severity == "low":
      incident_severity = 3

    return self.Incident(incident_id, incident["name"], incident["description"], incident_severity,
                         incident_creator, incident["create_date"])

  def generate_res_id(self, incident_id, task_id=None):
    """If incident_id and task_id are valid, returns "RES-1001-2002"
      Else if task_id is None, returns "RES-1001" """

    id = ["RES", str(incident_id)]
    if task_id is not None:
      id.append(str(task_id))
    return "-".join(id)

  def generate_res_link(self, incident_id, host, task_id=None):
    """Function that generates a https URL to the incident or task"""
    
    link = "https://{0}/#incidents/{1}".format(host, incident_id)

    if task_id is not None:
      link += "?task_id={0}".format(task_id)
    
    return link

  def write_file(self, filename, data):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)
    fo = open(path, "wb")
    fo.write(data)
    fo.close()
    return path

  def str_to_bool(self, str):
    """Convert unicode string to equivalent boolean value. Converts a "true" or "false" string to a boolean value , string is case insensitive."""
    if str.lower() == "true":
        return True
    elif str.lower() == "false":
        return False
    else:
        raise ValueError("{} is not a boolean".format(str))

  def csv_to_list(self, as_csv):
    """Function to convert a csv string to a Python List"""
    as_list = []
    f = StringIO(as_csv)
    reader = csv.reader(f, delimiter=',')
    for value in reader:
      as_list.append(value)
    return as_list[0]

  def get_config_option(self, option_name, optional=False):
    """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
    option = self.options.get(option_name)

    if option is None and optional is False:
      err = "'{0}' is mandatory and is not set in ~/.resilient/app.config file. You must set this value to run this function".format(option_name)
      raise ValueError(err)
    else:
      return option
  
  def get_function_input(self, inputs, input_name, optional=False):
    """Given input_name, checks if it defined. Raises ValueError if a mandatory input is None"""
    input = inputs.get(input_name)

    if input is None and optional is False:
      err = "'{0}' is a mandatory function input".format(input_name)
      raise ValueError(err)
    else:
      return input

  def get_res_incident_notes(self, client, incident_id):
    entity = {
      "id": incident_id,
      "data": None
    }

    entity["data"] = client.get("/incidents/{0}/comments?text_content_output_format=always_text".format(entity["id"]))
    
    if entity["data"] is not None and len(entity["data"]) == 0:
      entity = None
    
    return entity

  def get_res_incident_attachments(self, client, incident_id):
    entity = {
      "id": incident_id,
      "data": None,
      "meta_data": None
    }

    entity["meta_data"] = client.get("/incidents/{0}/attachments".format(entity["id"]))

    if entity["meta_data"] is not None and len(entity["meta_data"]) > 0:
      entity["data"] = []
      for attachment_info in entity["meta_data"]:
        attachment = client.get_content("/incidents/{0}/attachments/{1}/contents".format(entity["id"], attachment_info["id"]))

        if attachment is not None:
          entity["data"].append(base64.b64encode(attachment))

    else:
      entity = None

    return entity

  def get_res_task_attachments(self, client, task_id):
    entity = {
      "id": task_id,
      "data": None,
      "meta_data": None
    }

    entity["meta_data"] = client.get("/tasks/{0}/attachments".format(entity["id"]))

    if entity["meta_data"] is not None and len(entity["meta_data"]) > 0:
      entity["data"] = []
      for attachment_info in entity["meta_data"]:
        attachment = client.get_content("/tasks/{0}/attachments/{1}/contents".format(entity["id"], attachment_info["id"]))

        if attachment is not None:
          entity["data"].append(base64.b64encode(attachment))

    return entity

  def POST(self, url, data, auth=None, headers=None):
    """Function to handle POSTing to ServiceNow. If successful, returns the response as a Dictionary"""
    if(headers is None):
      headers = self.headers

    if auth is None:
      auth = self.SN_AUTH
    
    url = self.SN_API_URL + url

    returnJSON = None

    try:
      response = requests.post(url, auth=auth, headers=headers, data=data)
      response.raise_for_status()

      returnJSON = response.json()['result']

    except requests.exceptions.Timeout:
      raise ValueError('Request to ServiceNow timedout')

    except requests.exceptions.TooManyRedirects:
      raise ValueError('A bad url request', url)

    except requests.exceptions.HTTPError as err:
      if(err.response.content):
        custom_error_content = json.loads(err.response.content)
        raise ValueError(custom_error_content['error']['message'])
      else:
        raise ValueError(err)
    except requests.exceptions.RequestException as e:
        raise ValueError(e)

    return returnJSON

  def GET(self, url, params, auth=None, headers=None):

    if(headers is None):
      headers = self.headers

    if auth is None:
      auth = self.SN_AUTH
    
    url = self.SN_API_URL + url
    
    try:
      response = requests.get(url, auth=auth, headers=headers, params=params)
    except Exception:
      raise ValueError("ServiceNow GET failed. Check url, credentials and params")

    return response

  def __init__(self, options):
    self.options = options

    self.SN_HOST = self.get_config_option("sn_host")

    # https://service-now-host.com/api/<app-name>/<custom-api-name/
    self.SN_API_URL = "{0}{1}".format(self.SN_HOST, "/api/x_261673_resilient/api")
    self.SN_USERNAME = str(self.get_config_option("sn_username"))

    # Handle password surrounded by '
    pwd = str(self.get_config_option("sn_password"))
    if (pwd.startswith("'") and pwd.endswith("'")) or (pwd.startswith('"') and pwd.endswith('"')):
      self.SN_PASSWORD = pwd[1:-1]
    else:
      self.SN_PASSWORD = pwd

    self.SN_AUTH = (self.SN_USERNAME, self.SN_PASSWORD)

    # Default headers
    self.headers = {"Content-Type":"application/json","Accept":"application/json"}

    # Optional system fields that are know to Resilient that we handle getting
    self.SYSTEM_FIELDS = [
      "task_due_date",
      "incident_date_occurred",
      "incident_date_discovered",
      "incident_type"
      ]

class ExternalTicketStatusDatatable():
  """TODO"""
  def __init__(self, res_client, incident_id):
    self.res_client = res_client
    self.incident_id = incident_id
    self.api_name = "sn_external_ticket_status"
    self.data = None
    self.rows = None

  def get_data(self):
    uri = "/incidents/{0}/table_data/{1}?handle_format=names".format(self.incident_id, self.api_name)
    try:
      self.data = self.res_client.get(uri)
      self.rows = self.data["rows"]
    except Exception:
      raise ValueError("Failed to get sn_external_ticket_status Datatable")

  def get_sn_ref_ids(self, incident_id, task_id=None):
    """Returns list of each related sn_ref_id"""
    id = ["RES", str(incident_id)]
    
    if task_id is not None:
      id.append(str(task_id))

    res_id_to_search = "-".join(id)

    ids_found = []
    
    for row in self.rows:
      cells = row["cells"]
      res_id = str(cells["res_id"]["value"])
      
      if task_id is not None:
        if(res_id_to_search in res_id):
          ids_found.append(str(cells["sn_ref_id"]["value"]))

      else:
        if(res_id_to_search == res_id):
          ids_found.append(str(cells["sn_ref_id"]["value"]))
    
    return ids_found

  def asDict(self):
    return self.__dict__