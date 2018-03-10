# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import io
import os
import base64
import requests_mock
from pytest_resilient_circuits import BasicResilientMock, resilient_endpoint


class ArtifactMock(BasicResilientMock):

    @staticmethod
    def test_data(filename):
        """Read a test data file"""
        template_file_path = os.path.join(os.path.dirname(__file__), "data", filename)
        with io.open(template_file_path, 'rb') as template_file:
            return template_file.read()

    @staticmethod
    def test_data_b64(filename):
        """Read a test data file, return its contents as base64"""
        return base64.b64decode(ArtifactMock.test_data(filename))

    email_artifacts = {
        "1": {
            "description": "mail",
            "value": "email_sample_1.eml",
            "type": "RFC 822 Email Message File",
            "id": 1
        },
        "2": {
            "description": "mail",
            "value": "email_sample_2.eml",
            "type": "RFC 822 Email Message File",
            "id": 2
        },
        "3": {
            "description": "mail",
            "value": "email_sample_3.eml",
            "type": "RFC 822 Email Message File",
            "id": 3
        }
    }

    @resilient_endpoint("GET", "/incidents/[0-9]+/artifacts$")
    def artifacts_get(self, request):
        """ GET the list of artifacts """
        data = [value for id, value in self.artifacts.items()]
        return requests_mock.create_response(request,
                                             status_code=200,
                                             json=data)

    @resilient_endpoint("GET", "/incidents/[0-9]+/artifacts/[0-9]+$")
    def artifacts_one_get(self, request):
        """ GET an artifact """
        artifact_id = request.url.split("/")[-1]
        data = self.email_artifacts[artifact_id]
        return requests_mock.create_response(request,
                                             status_code=200,
                                             json=data)

    @resilient_endpoint("GET", "/incidents/[0-9]+/artifacts/[0-9]+/contents$")
    def artifacts_contents_get(self, request):
        """ GET the file contents of an artifact """
        artifact_id = request.url.split("/")[-2]
        data = self.test_data(self.email_artifacts[artifact_id]["value"])
        return requests_mock.create_response(request,
                                             status_code=200,
                                             content=data)

