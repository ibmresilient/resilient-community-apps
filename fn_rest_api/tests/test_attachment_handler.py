# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
import json, os
import pytest, unittest

from requests.exceptions import InvalidURL
from unittest.mock import patch, MagicMock
from fn_rest_api.lib.attachment_handler import *

class TestAttachmentConstants(unittest.TestCase):
    def test_constants(self):
        self.assertEqual(ID, "id")
        self.assertEqual(NAME, "name")
        self.assertEqual(CONTENT_TYPE, "content_type")
        self.assertEqual(FILE_CONTENTS, "file_contents")
        self.assertEqual(ARTIFACTS, "artifacts")
        self.assertEqual(ATTACHMENTS, "attachments")
        self.assertEqual(INCIDENT_ID, "incident_id")
        self.assertEqual(ARTIFACT_ID, "artifact_id")
        self.assertEqual(ATTACHMENT_ID, "attachment_id")
        self.assertEqual(ATTACHMENT_FORM_FIELD, "attachment_form_field_name")

ATH_METADATA = json.loads(open(os.path.join(os.path.dirname(__file__), "data", "attachmentResponse.json"), "r").read())
ART_METADATA = json.loads(open(os.path.join(os.path.dirname(__file__), "data", "artifactResponse.json"), "r").read())
ATH_CONTENT  = open(os.path.join(os.path.dirname(__file__), "data", "attachment.svg"), "rb").read()
ART_CONTENT  = open(os.path.join(os.path.dirname(__file__), "data", "artifact.svg"), "rb").read()

class MockRestClient(MagicMock):
    def get(self, url):
        if url == '/incidents/2096/attachments/478':
            return ATH_METADATA
        elif url == '/incidents/2096/artifacts/26':
            return ART_METADATA
        else:
            raise InvalidURL(f"unrecognized url : {url}")

    def get_content(self, url):
        if url == "/incidents/2096/attachments/478/contents":
            return ATH_CONTENT
        elif url == "/incidents/2096/artifacts/26/contents":
            return ART_CONTENT
        else:
            raise InvalidURL(f"unrecognized url : {url}")


class TestAttachmentHandler(unittest.TestCase):

    def test_artifact(self):
        rest_client = MockRestClient()
        ath = AttachmentHandler(rest_client)
        output = ath.add_files(incident_id=2096, artifact_id=26)
        assert len(output) == 1
        assert len(output[0]) == 2
        # test for default attachment_form_field_name
        assert output[0][0] == "file"

        _body = output[0][1]
        assert _body[0] == 'artifact.svg'
        assert _body[2] == 'image/svg+xml'
        assert _body[1] == open(os.path.join(os.path.dirname(__file__), "data", "artifact.svg"), "rb").read()

    def test_attachment(self):
        field_name = "image/files"
        rest_client = MockRestClient()
        ath = AttachmentHandler(rest_client)
        output = ath.add_files(incident_id=2096, attachment_id=478, attachment_form_field_name=field_name)
        assert len(output) == 1
        assert len(output[0]) == 2
        # test for custom attachment_form_field_name
        assert output[0][0] == field_name

        _body = output[0][1]
        assert _body[0] == 'attachment.svg'
        assert _body[2] == 'image/svg+xml'
        assert _body[1] == open(os.path.join(os.path.dirname(__file__), "data", "attachment.svg"), "rb").read()

    def test_invalid_attachment(self):
        rest_client = MockRestClient()
        ath = AttachmentHandler(rest_client)
        with pytest.raises(InvalidURL) as err:
            ath.add_files(incident_id=2096, attachment_id=500)

    def test_invalid_artifact(self):
        rest_client = MockRestClient()
        ath = AttachmentHandler(rest_client)
        with pytest.raises(InvalidURL) as err:
            ath.add_files(incident_id=2096, artifact_id=500)

    def test_both(self):
        rest_client = MockRestClient()
        ath = AttachmentHandler(rest_client)
        output = ath.add_files(incident_id=2096, artifact_id=26, attachment_id=478)
        assert len(output) == 2
        assert len(output[0]) == 2
        # test for default attachment_form_field_name
        assert output[0][0] == "file"

        _body_artifact = output[0][1]
        assert _body_artifact[0] == 'artifact.svg'
        assert _body_artifact[2] == 'image/svg+xml'
        assert _body_artifact[1] == open(os.path.join(os.path.dirname(__file__), "data", "artifact.svg"), "rb").read()

        _body_artifact = output[1][1]
        assert _body_artifact[0] == 'attachment.svg'
        assert _body_artifact[2] == 'image/svg+xml'
        assert _body_artifact[1] == open(os.path.join(os.path.dirname(__file__), "data", "attachment.svg"), "rb").read()


class TestAddFiles(unittest.TestCase):

    def test_missing_incident_id(self):
        rest_client = MockRestClient()
        ath = AttachmentHandler(rest_client)
        self.assertIsNone(ath.add_files(artifact_id=10, attachment_id=10))

    def test_missing_artifact_attachment_id(self):
        rest_client = MockRestClient()
        ath = AttachmentHandler(rest_client)
        self.assertIsNone(ath.add_files(incident_id=10))


class TestGetFileContents(unittest.TestCase):

    def test_missing_arguments(self):
        rest_client = MockRestClient()
        ath = AttachmentHandler(rest_client)
        with pytest.raises(TypeError) as err:
            ath._get_file_contents()
    
    def test_missing_incident_id(self):
        rest_client = MockRestClient()
        ath = AttachmentHandler(rest_client)
        with pytest.raises(AttributeError) as err:
            ath._get_file_contents(ATH_METADATA, object_type="attachments")

    def test_get_artifact(self):
        rest_client = MockRestClient()
        ath = AttachmentHandler(rest_client)
        ath.incident_id = 2096
        ret = ath._get_file_contents(ATH_METADATA, object_type="attachments")
        assert ret
        assert FILE_CONTENTS in ret
        assert ret[FILE_CONTENTS]

    def test_write_file(self):
        rest_client = MockRestClient()
        ath = AttachmentHandler(rest_client)
        ath.incident_id = 2096
        ret = ath._get_file_contents(ATH_METADATA, object_type="attachments", write_to_phy_location=True)
        assert ret
        assert FILE_CONTENTS in ret
        assert ret[FILE_CONTENTS]
        assert ret["file_path_on_device"]
        assert os.path.isfile(ret["file_path_on_device"])
        assert open(ret["file_path_on_device"], "rb").read() == ATH_CONTENT