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
    self.headers = {"Content-Type":"application/json","Accept":"application/json"}

  def get_config_option(self, option_name, optional=False):
    """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
    option = self.app_configs.get(option_name)

    if not option and optional is False:
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

  def generate_sn_link(self, sn_query, sn_table_name=None):
    """Function that generates a URL to the record in ServiceNow"""
    if not sn_table_name:
      sn_table_name = self.SN_TABLE_NAME

    # https://dev59090.service-now.com/nav_to.do?uri=incident.do?sysparm_query=number=INC0010350
    uri = "{0}/nav_to.do?uri={1}.do?sysparm_query={2}".format(self.SN_HOST, sn_table_name, sn_query)
    return uri

  def convert_text_to_richtext(self, text, color="green"):
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

  def sn_GET(self, url, params, auth=None, headers=None):

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

  # Define a Task that gets sent to ServiceNow
  class Task:
    """Class that represents a Resilient Task. See API notes for more"""
    def __init__(self, incident_id, task_id, task_name, task_instructions):
      self.type = "res_task"
      self.incident_id = incident_id
      self.task_id = task_id
      self.task_name = task_name
      self.task_instructions = task_instructions

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

    return self.Task(incident_id, task_id, task["name"], task_instructions)

  # Define an Incident that gets sent to ServiceNow
  class Incident:
    """Class that represents a Resilient Incident. See API notes for more"""
    def __init__(self, incident_id, incident_name, incident_description):

      self.type = "res_incident"
      self.incident_id = incident_id
      self.incident_name = incident_name
      self.incident_description = incident_description

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
      raise ValueError("incident_id {0} not found".format(incident_id))

    return self.Incident(incident_id, incident["name"], incident["description"])

class ExternalTicketStatusDatatable():
  """Class that handles the sn_external_ticket_status datatable"""
  def __init__(self, res_client, incident_id):
    self.res_client = res_client
    self.incident_id = incident_id
    self.api_name = "sn_external_ticket_status"
    self.data = None
    self.rows = None

    self.get_data()

  def get_data(self):
    uri = "/incidents/{0}/table_data/{1}?handle_format=names".format(self.incident_id, self.api_name)
    try:
      self.data = self.res_client.get(uri)
      self.rows = self.data["rows"]
    except Exception:
      raise ValueError("Failed to get sn_external_ticket_status Datatable")

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

    else:
      return None

  def add_row(self, time, res_id, sn_ref_id, resilient_status, servicenow_status, link):
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
    # Generate uri to POST datatable row
    uri = "/incidents/{0}/table_data/{1}/row_data/{2}?handle_format=names".format(self.incident_id, self.api_name, row["id"])
    
    def get_value(cell_name):
      if cell_name in cells_to_update:
        return cells_to_update[cell_name]
      else:
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

  def asDict(self):
    return self.__dict__