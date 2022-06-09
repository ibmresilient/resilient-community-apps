# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
from os.path import dirname, join
from base64 import b64encode
from requests_mock import create_response
from pytest_resilient_circuits import BasicResilientMock, resilient_endpoint

class ArtifactMock(BasicResilientMock):

    @staticmethod
    def test_data(filename):
        """Read a test data file"""
        template_file_path = join(dirname(__file__), "data", filename)
        with open(template_file_path, 'rb') as template_file:
            return template_file.read()

    @staticmethod
    def test_data_b64(filename):
        """Read a test data file, return its contents as base64"""
        return b64encode(ArtifactMock.test_data(filename))

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
        },
        "6": {
            "description": "valid cert",
            "value": "ssl_certs/ssl_example.cert",
            "type": "X509 Certificate File",
            "id": 6
        },
        "7": {
            "description": "expired cert",
            "value": "ssl_certs/ssl_expired.cert",
            "type": "X509 Certificate File",
            "id": 7
        },
        "8": {
            "description": None,
            "value": "email_sample_1.eml",
            "type": "RFC 822 Email Message File",
            "id": 8,
            "attachment": {
                "type": "artifact",
                "id": 16,
                "name": "email_sample_1.eml",
                "created": 1519264285530,
                "content_type": "text/plain",
                "size": 984,
            }
        }
    }

    @resilient_endpoint("GET", "/incidents/[0-9]+/artifacts$")
    def artifacts_get(self, request):
        """ GET the list of artifacts """
        data = [value for id, value in self.artifacts.items()]
        return create_response(request, status_code=200, json=data)

    @resilient_endpoint("POST", "/incidents/[0-9]+/artifacts$")
    def artifacts_post(self, request):
        """ POST an attachment """
        data = [
            {
                "id": 50,
                "type": 29,
                "value": "test",
                "description": None
            }
        ]
        return create_response(request, status_code=200, json=data)

    @resilient_endpoint("POST", "/incidents/[0-9]+/artifacts/files$")
    def artifacts_files_post(self, request):
        """ POST an artifact file"""
        data = [
            {
                "id": 51,
                "type": 29,
                "value": "test",
                "description": None
            }
        ]
        return create_response(request, status_code=200, json=data)

    @resilient_endpoint("GET", "/types/artifact/fields/type$")
    def artifacts_type_get(self, request):
        """ GET artifact types """
        data = {
                "uuid": "25dd5ae3-549b-4114-a9b6-64ef7baef80c",
                "type_id": 4,
                "text": "Type",
                "prefix": None,
                "internal": None,
                "values": [
                    {
                        "value": 1,
                        "label": "IP Address",
                    },
                    {
                        "value": 2,
                        "label": "DNS Name",
                    }
            ]
        }
        return create_response(request, status_code=200, json=data)

    @resilient_endpoint("GET", "/incidents/[0-9]+/artifacts/[0-9]+$")
    def artifacts_one_get(self, request):
        """ GET an artifact """
        artifact_id = request.url.split("/")[-1]
        data = self.email_artifacts[artifact_id]
        return create_response(request, status_code=200, json=data)

    @resilient_endpoint("GET", "/incidents/[0-9]+/artifacts/[0-9]+/contents$")
    def artifacts_contents_get(self, request):
        """ GET the file contents of an artifact """
        artifact_id = request.url.split("/")[-2]
        data = self.test_data(self.email_artifacts[artifact_id]["value"])
        return create_response(request, status_code=200, content=data)
