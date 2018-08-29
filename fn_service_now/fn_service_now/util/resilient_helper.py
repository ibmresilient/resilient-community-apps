# (c) Copyright IBM Corp. 2018. All Rights Reserved.
import requests
import os
import base64
from bs4 import BeautifulSoup
import json
class ResilientHelper:

  # Define a Task that gets sent to ServiceNow
  class Task:
    def __init__(self, incident_id, task_id, task_date_initiated, task_instructions,
                task_creator, task_owner, optional_fields=None):
      self.type = "res_task"
      self.incident_id = incident_id
      self.task_id = task_id
      self.task_date_initiated = task_date_initiated
      self.task_instructions = task_instructions
      self.task_creator = task_creator
      self.task_owner = task_owner
      self.optional_fields = optional_fields
    
    def toJSON(self):
      return json.dumps(self.__dict__)

  def get_task(self, client, task_id, incident_id, optional_fields_wanted=None):
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

    # Get the task creator and owner
    task_creator = {
      "name": "{0} {1}".format(task["creator"]["fname"], task["creator"]["lname"]),
      "email": task["creator"]["email"]
    }
    task_owner = {
      "name": "{0} {1}".format(task["owner_fname"], task["owner_lname"]),
      "email": task["owner_id"]
    }

    # Setup optional fields dict
    optional_fields = None
    
    if optional_fields_wanted is not None:
      optional_fields = {}
      
      # Add all optional fields
      for field_name in optional_fields_wanted:
        
        # if it is a known SYSTEM_FIELD
        if field_name in self.SYSTEM_FIELDS:
          if field_name == "task_due_date":
            optional_fields["task_due_date"] = task["due_date"]
        
        # Else it must be a CUSTOM_INCIDENT_FIELD or the field does not exist
        # TODO

    return self.Task(incident_id, task_id, task["init_date"], task_instructions, task_creator, task_owner, optional_fields)

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

  def get_res_incident(self, client, incident_id, want_notes=False, want_attachments=False,):
    entity = {
      "id": incident_id,
      "data": None
    }

    try:
      entity["data"] = client.get("/incidents/{0}?text_content_output_format=always_text".format(entity["id"]))

    except:
      raise ValueError("incident_id {0} not found".format(incident_id))

    if want_notes:
      incident = entity["data"]
      notes = self.get_res_incident_notes(client, incident_id)
      if notes is not None:
        incident["notes"] = notes["data"]

    if want_attachments:
      incident = entity["data"]
      attachments = self.get_res_incident_attachments(client, entity["id"])
      if attachments is not None:
        incident["attachments_meta_data"] = attachments["meta_data"]
        incident["attachments_data"] = attachments["data"]

    return entity["data"]

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

  # def get_res_incident_tasks(self, client, incident_id, want_layouts=False, want_notes=False, want_attachments=False):
  #   entity = {
  #     "id": incident_id,
  #     "data": None
  #   }

  #   entity["data"] = client.get("/incidents/{0}/tasks?want_layouts={1}&want_notes={2}".format(entity["id"], want_layouts, want_notes))

  #   if entity["data"] is not None and len(entity["data"]) > 0:
  #     tasks = entity["data"]
  #     for task in tasks:
  #       if task["notes_count"] > 0:
  #         task_notes = task["notes"]

  #         for note in task_notes:
  #           print note["text"]
        
  #       if want_attachments and task["attachments_count"] > 0:
  #         attachments = self.get_res_task_attachments(client, task["id"])

  #         task["attachments_meta_data"] = attachments["meta_data"]
  #         task["attachments_data"] = attachments["data"]

  #   return entity["data"]

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
      print 'Timeout error'
    except requests.exceptions.TooManyRedirects:
      print 'Bad URL'
    except requests.exceptions.HTTPError as err:
      if(err.response.content):
        custom_error_content = json.loads(err.response.content)
        print custom_error_content['error']['message']
      else:
        print err
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print e

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
    self.SN_API_URL = "{0}{1}".format(self.SN_HOST, "/api/x_261673_test_res/res_test_api")
    self.SN_USERNAME = str(self.get_config_option("sn_username"))
    
    # Handle password surrounded by '
    pwd = str(self.get_config_option("sn_password"))
    if (pwd.startswith("'") and pwd.endswith("'")) or (pwd.startswith('"') and pwd.endswith('"')):
      self.SN_PASSWORD = pwd[1:-1]
    else:
      self.SN_PASSWORD = pwd
    
    self.SN_AUTH = (self.SN_USERNAME, self.SN_PASSWORD)

    self.headers = {"Content-Type":"application/json","Accept":"application/json"}

    # List of both required and optional fields that are know to Resilient that we handle getting
    self.SYSTEM_FIELDS = [
      "incident_id",
      "task_id",
      "task_date_initiated",
      "task_instructions",
      "task_creator",
      "task_owner",
      "task_due_date"
      ]
