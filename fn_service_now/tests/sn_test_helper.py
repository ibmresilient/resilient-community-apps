try:
    from unittest.mock import patch, Mock, MagicMock
except:
    from mock import patch, Mock, MagicMock
from fn_service_now.util.resilient_helper import ResilientHelper
from fn_service_now.util.external_ticket_status_datatable import ExternalTicketStatusDatatable
from pytest_resilient_circuits import BasicResilientMock, resilient_endpoint
import requests_mock
from mock_data import task
import json
import six

# Handle basestring in 2.x and 3.x
try:
  basestring
except NameError:
  basestring = str

# Handle unicode in 2.x and 3.x
try:
    unicode
except NameError:
    unicode = str

def get_mock_config_data():
  return u"""[fn_service_now]
sn_host=https://test.service-now.com
sn_api_uri=/api/x_261673_resilient/api
sn_table_name=incident
sn_username=ibmresilient
sn_password="$testpassword"
"""

def mock_pre_scrip_dict_to_json_str(d):
  """Function that converts a dictionary into a JSON string.
     Supports types: basestring, bool and int. 
     Supports nested directories.
     If the value is None, it sets it to False"""

  json_entry = '"{0}":{1}'
  json_entry_str = '"{0}":"{1}"'
  entries = [] 

  for entry in d:
    key = entry
    value = d[entry]

    if value is None:
      value = False

    if isinstance(value, list):
      raise ValueError('dict_to_json_str does not support Python Lists')

    if isinstance(value, basestring):
      value = value.replace(u'"', u'\\"')
      entries.append(json_entry_str.format(key, value))
    
    elif isinstance(value, bool):
      value = 'true' if value == True else 'false'
      entries.append(json_entry.format(key, value))

    elif isinstance(value, dict):
      entries.append(json_entry.format(key, mock_pre_scrip_dict_to_json_str(value)))

    else:
      entries.append(json_entry.format(key, value))

  return '{0} {1} {2}'.format('{', ','.join(entries), '}')

# Convert unicode dict to str dict
def mock_byteify(data):
    """Function that converts unicode dict to str dict"""

    data_as_utf8_str_dict = None

    if isinstance(data, unicode):
        data_as_utf8_str_dict = data.encode("utf-8")
        
        # if Python 3.x data_as_utf8_str_dict will be bytes, so we convert back to str
        if isinstance(data_as_utf8_str_dict, bytes):
            data_as_utf8_str_dict = data_as_utf8_str_dict.decode(("utf-8"))

    elif isinstance(data, dict):
        data_as_utf8_str_dict = {mock_byteify(key): mock_byteify(value) for key, value in data.items()}

    return data_as_utf8_str_dict

class MockedResponse:
  def __init__(self, status_code, text):
    self.status_code = status_code
    self.text = text

class SNResilientMock(BasicResilientMock):

    attachments = {
        "1": {
            "name": "Mock Attachment Name",
            "created": 1519264285530,
            "content_type": "text/plain",
            "size": 984,
            "id": 1,
        },
        "2": {
            "name": "spreadsheet_sample_1.xlsx",
            "created": 1519264285530,
            "content_type": "text/xlsx",
            "size": 24136,
            "id": 2,
        }
    }

    datatable_rows = [
      {
        "sn_records_dt_time": 1543333316605,
        "sn_records_dt_name": "Mock Task Name",
        "sn_records_dt_type": "Task",
        "sn_records_dt_res_id": "RES-1001-2002",
        "sn_records_dt_sn_ref_id": "INC123456",
        "sn_records_dt_res_status": """<div style="color: rgb(0,179,60);">Active</div>""",
        "sn_records_dt_snow_status": """<div style="color: rgb(230,0,0);">Resolved</div>""",
        "sn_records_dt_links": """<a href="https://0.0.0.0/#incidents/2105?task_id=2251401">RES</a> <a href="https://test.service-now.com/nav_to.do?uri=incident.do?sysparm_query=number=INC0010459">SN</a>"""
      },
      {
        "sn_records_dt_time": 1543333316605,
        "sn_records_dt_res_id": "RES-1001",
        "sn_records_dt_name": "Mock Incident Name",
        "sn_records_dt_type": "Incident",
        "sn_records_dt_sn_ref_id": "INC123457",
        "sn_records_dt_res_status": """<div style="color: rgb(0,179,60);">Active</div>""",
        "sn_records_dt_snow_status": """<div style="color: rgb(230,0,0);">Resolved</div>""",
        "sn_records_dt_links": """<a href="https://0.0.0.0/#incidents/2105?task_id=2251401">RES</a> <a href="https://test.service-now.com/nav_to.do?uri=incident.do?sysparm_query=number=INC0010459">SN</a>"""
      }
    ]

    updated_datatable_rows = [
        {
            "sn_records_dt_time": 1543333316605,
            "sn_records_dt_res_id": "RES-1001-2002",
            "sn_records_dt_sn_ref_id": "INC123456",
            "sn_records_dt_name": "Mock Task Name",
            "sn_records_dt_type": "Task",
            "sn_records_dt_res_status": """<div style="color: rgb(0,179,60);">Active</div>""",
            "sn_records_dt_snow_status": """<div style="color: rgb(230,0,0);">Resolved</div>""",
            "sn_records_dt_links": """<a href="https://0.0.0.0/#incidents/2105?task_id=2251401">RES</a> <a href="https://test.service-now.com/nav_to.do?uri=incident.do?sysparm_query=number=INC0010459">SN</a>"""
        },
        {
            "sn_records_dt_time": 1543333316605,
            "sn_records_dt_res_id": "RES-1001",
            "sn_records_dt_name": "Mock Incident Name",
            "sn_records_dt_type": "Incident",
            "sn_records_dt_sn_ref_id": "INC123457",
            "sn_records_dt_res_status": """<div style="color: rgb(0,179,60);">Closed</div>""",
            "sn_records_dt_snow_status": """<div style="color: rgb(230,0,0);">Resolved</div>""",
            "sn_records_dt_links": """<a href="https://0.0.0.0/#incidents/2105?task_id=2251401">RES</a> <a href="https://test.service-now.com/nav_to.do?uri=incident.do?sysparm_query=number=INC0010459">SN</a>"""
      }
    ]

    @staticmethod
    def format_datatable_row(row, row_id):
      formatted_row = {}

      for key, value in row.items():
        formatted_row[key] = {
          "row_id": row_id,
          "id": key,
          "value": value
        }
  
      return {"id": row_id, "cells": formatted_row}
    
    @staticmethod
    def get_datatable_rows(rows):
      row_id = 0
      return_rows = []
      for row in rows:
        row_id += 1
        return_rows.append(SNResilientMock.format_datatable_row(row, row_id))
      return return_rows

    @resilient_endpoint("GET", "/incidents/[0-9]+/attachments/[0-9]+$")
    def attachments_one_incident_get(self, request):
        """ GET an attachment """
        attachment_id = request.url.split("/")[-1]
        data = self.attachments[attachment_id]
        return requests_mock.create_response(request,
                                             status_code=200,
                                             json=data)

    @resilient_endpoint("GET", "/tasks/[0-9]+/attachments/[0-9]+$")
    def attachments_one_task_get(self, request):
        """ GET an attachment """
        attachment_id = request.url.split("/")[-1]
        data = self.attachments[attachment_id]
        return requests_mock.create_response(request,
                                             status_code=200,
                                             json=data)

    @resilient_endpoint("GET", "/incidents/[0-9]+/attachments/[0-9]+/contents$")
    def attachments_contents_incident_get(self, request):
        """ GET the file contents of an attachment """
        attachment_id = request.url.split("/")[-2]
        data = {"data": "test data"}
        return requests_mock.create_response(request,
                                             status_code=200,
                                             content=six.b(json.dumps(data)))

    @resilient_endpoint("GET", "/tasks/[0-9]+/attachments/[0-9]+/contents$")
    def attachments_contents_task_get(self, request):
        """ GET the file contents of an attachment """
        attachment_id = request.url.split("/")[-2]
        data = {"data": "test data"}
        return requests_mock.create_response(request,
                                             status_code=200,
                                             content=six.b(json.dumps(data)))

    @resilient_endpoint("GET", "/incidents/[0-9]+/table_data/sn_records_dt\?handle_format=names")
    def datatable_incident_get(self, request):
        """ GET sn_records_dt datatable """

        data = {"rows": SNResilientMock.get_datatable_rows(self.datatable_rows)}

        return requests_mock.create_response(request,
                                             status_code=200,
                                             content=six.b(json.dumps(data)))

    @resilient_endpoint("PUT", "/incidents/[0-9]+/table_data/sn_records_dt/row_data/[0-9]+\?handle_format=names")
    def datatable_incident_put(self, request):
        """ PUT sn_records_dt datatable """

        data = SNResilientMock.get_datatable_rows(self.updated_datatable_rows)[0]

        return requests_mock.create_response(request,
                                             status_code=200,
                                             content=six.b(json.dumps(data)))

    @resilient_endpoint("GET", "/tasks/[0-9]+\?text_content_output_format\=always_text\&handle_format\=names$")
    def tasks_get_with_parameters(self, request):
        """ GET tasks with parameters text_content_output_format and handle_format """

        return requests_mock.create_response(request,
                                             status_code=200,
                                             content=six.b(json.dumps(task.get_mocked_task())))

    @resilient_endpoint("GET", "/tasks/[0-9]+/instructions")
    def tasks_get_instructions(self, request):
        """ GET tasks instructions """

        data = b"""Test task instructions <br> Test task instructions<br><br>"""

        return requests_mock.create_response(request,
                                             status_code=200,
                                             content=data)