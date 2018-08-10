# (c) Copyright IBM Corp. 2018. All Rights Reserved.
import requests
import os
import base64

class ServiceNowHelper:

  def write_file(self, filename, data):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)
    fo = open(path, 'wb')
    fo.write(data)
    fo.close()
    return path

  def str_to_bool(self, str):
    """Convert unicode string to equivalent boolean value. Converts a "true" or "false" string to a boolean value , string is case insensitive."""
    if str.lower() == 'true':
        return True
    elif str.lower() == 'false':
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
      raise ValueError('incident_id {0} not found'.format(incident_id))

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

  def get_res_incident_tasks(self, client, incident_id, want_layouts=False, want_notes=False, want_attachments=False):
    entity = {
      "id": incident_id,
      "data": None
    }

    entity["data"] = client.get("/incidents/{0}/tasks?want_layouts={1}&want_notes={2}".format(entity["id"], want_layouts, want_notes))

    if entity["data"] is not None and len(entity["data"]) > 0:
      tasks = entity["data"]
      for task in tasks:
        if task["notes_count"] > 0:
          task_notes = task["notes"]

          for note in task_notes:
            print note["text"]
        
        if want_attachments and task["attachments_count"] > 0:
          attachments = self.get_res_task_attachments(client, task["id"])

          task["attachments_meta_data"] = attachments["meta_data"]
          task["attachments_data"] = attachments["data"]

    return entity["data"]

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
    
    try:
      response = requests.post(url, auth=auth, headers=headers, data=data)
    except Exception:
      raise ValueError("ServiceNow POST failed. Check url and credentials")

    return response

  def __init__(self, options):
    self.options = options

    self.SN_API_URL = self.get_config_option("sn_api_url")
    self.SN_USERNAME = str(self.get_config_option("sn_username"))
    
    # Handle password surrounded by '
    pwd = str(self.get_config_option("sn_password"))
    if (pwd.startswith("'") and pwd.endswith("'")) or (pwd.startswith('"') and pwd.endswith('"')):
      self.SN_PASSWORD = pwd[1:-1]
    else:
      self.SN_PASSWORD = pwd
    
    self.SN_AUTH = (self.SN_USERNAME, self.SN_PASSWORD)

    self.headers = {"Content-Type":"application/json","Accept":"application/json"}

