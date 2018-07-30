# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import os
import io
import base64
import requests_mock
from pytest_resilient_circuits import BasicResilientMock, resilient_endpoint


class AttachmentMock(BasicResilientMock):

    @staticmethod
    def test_data(filename):
        """Read a test data file"""
        template_file_path = os.path.join(os.path.dirname(__file__), "data", filename)
        with io.open(template_file_path, 'rb') as template_file:
            return template_file.read()

    @staticmethod
    def test_data_b64(filename):
        """Read a test data file, return its contents as base64"""
        return base64.b64encode(AttachmentMock.test_data(filename))

    attachments = {
        "1": {
            "name": "email_sample_1.eml",
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
        },
        "42": {
            "name": "excel_query/budget.xlsx",
            "created": 1519264285530,
            "content_type": "text/xlsx",
            "size": 60061,
            "id": 42,
        },
        "101": {
            "name": "sample1.pdf",
            "created": 1519264285530,
            "content_type": "application/pdf",
            "size": 9871,
            "id": 101,
        },
        "201": {
            "name": "sample1.zip",
            "created": 1519264285530,
            "content_type": "application/zip",
            "size": 207,
            "id": 201,
        },
        "2021": {
            "name": "test attachment name.txt",
            "created": 1519264285530,
            "content_type": "text/plain",
            "size": 984,
            "id": 2021,
        }
    }

    @resilient_endpoint("GET", "/tasks/[0-9]+/attachments$")
    @resilient_endpoint("GET", "/incidents/[0-9]+/attachments$")
    def attachments_get(self, request):
        """ GET the list of attachments """
        data = [value for id, value in self.attachments.items()]
        return requests_mock.create_response(request,
                                             status_code=200,
                                             json=data)

    @resilient_endpoint("POST", "/tasks/[0-9]+/attachments$")
    @resilient_endpoint("POST", "/incidents/[0-9]+/attachments$")
    def attachments_post(self, request):
        """ POST an attachment """

        data = {}
        incident_id = request.url.split("/")[-2]

        if incident_id == "202":
          data = self.attachments["2021"]

        return requests_mock.create_response(request,
                                             status_code=200,
                                             json=data)

    @resilient_endpoint("GET", "/tasks/[0-9]+/attachments/[0-9]+$")
    @resilient_endpoint("GET", "/incidents/[0-9]+/attachments/[0-9]+$")
    def attachments_one_get(self, request):
        """ GET an attachment """
        attachment_id = request.url.split("/")[-1]
        data = self.attachments[attachment_id]
        return requests_mock.create_response(request,
                                             status_code=200,
                                             json=data)

    @resilient_endpoint("GET", "/tasks/[0-9]+/attachments/[0-9]+/contents$")
    @resilient_endpoint("GET", "/incidents/[0-9]+/attachments/[0-9]+/contents$")
    def attachments_contents_get(self, request):
        """ GET the file contents of an attachment """
        attachment_id = request.url.split("/")[-2]
        data = self.test_data(self.attachments[attachment_id]["name"])
        return requests_mock.create_response(request,
                                             status_code=200,
                                             content=data)

