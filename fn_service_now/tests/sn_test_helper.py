from mock import MagicMock
from fn_service_now.util.resilient_helper import ResilientHelper
import json
import requests_mock
from pytest_resilient_circuits import BasicResilientMock, resilient_endpoint

def get_mock_config_data():
  return u"""[fn_service_now]
sn_host=https://test.service-now.com
sn_api_uri=/api/x_261673_resilient/api
sn_table_name=incident
sn_username=ibmresilient
sn_password="$testpassword"
"""

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
        "time": 1543333316605,
        "res_id": "RES-1001-2002",
        "sn_ref_id": "INC123456",
        "resilient_status": """<div style="color: rgb(0,179,60);">Active</div>""",
        "servicenow_status": """<div style="color: rgb(230,0,0);">Resolved</div>""",
        "link": """<a href="https://0.0.0.0/#incidents/2105?task_id=2251401">RES</a> <a href="https://test.service-now.com/nav_to.do?uri=incident.do?sysparm_query=number=INC0010459">SN</a>"""
      },
      {
        "time": 1543333316605,
        "res_id": "RES-1001",
        "sn_ref_id": "INC123457",
        "resilient_status": """<div style="color: rgb(0,179,60);">Active</div>""",
        "servicenow_status": """<div style="color: rgb(230,0,0);">Resolved</div>""",
        "link": """<a href="https://0.0.0.0/#incidents/2105?task_id=2251401">RES</a> <a href="https://test.service-now.com/nav_to.do?uri=incident.do?sysparm_query=number=INC0010459">SN</a>"""
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
        data = "test data"
        return requests_mock.create_response(request,
                                             status_code=200,
                                             content=data)

    @resilient_endpoint("GET", "/tasks/[0-9]+/attachments/[0-9]+/contents$")
    def attachments_contents_task_get(self, request):
        """ GET the file contents of an attachment """
        attachment_id = request.url.split("/")[-2]
        data = "test data"
        return requests_mock.create_response(request,
                                             status_code=200,
                                             content=data)

    @resilient_endpoint("GET", "/incidents/[0-9]+/table_data/sn_external_ticket_status\?handle_format=names")
    def datatable_incident_get(self, request):
        """ GET sn_external_ticket_status datatable """

        data = {"rows": SNResilientMock.get_datatable_rows(self.datatable_rows)}

        return requests_mock.create_response(request,
                                             status_code=200,
                                             content=json.dumps(data))