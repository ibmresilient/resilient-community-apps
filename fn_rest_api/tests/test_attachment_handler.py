# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
import json, os, copy, logging
import pytest, unittest

from requests.exceptions import InvalidURL
from unittest.mock import patch, MagicMock
from fn_rest_api.lib.attachment_handler import *


def test_constants():
    assert ID == "id"
    assert NAME == "name"
    assert CONTENT_TYPE == "content_type"
    assert FILE_CONTENTS == "file_contents"
    assert ARTIFACTS == "artifacts"
    assert ATTACHMENTS == "attachments"
    assert INCIDENT_ID == "incident_id"
    assert ARTIFACT_ID == "artifact_id"
    assert ATTACHMENT_ID == "attachment_id"
    assert ATTACHMENT_FORM_FIELD == "attachment_form_field_name"

ATH_METADATA = json.loads(open(os.path.join(os.path.dirname(__file__), "data", "attachmentResponse.json"), "r").read())
ART_METADATA = json.loads(open(os.path.join(os.path.dirname(__file__), "data", "artifactResponse.json"), "r").read())
ART_WO_ATCH  = json.loads(open(os.path.join(os.path.dirname(__file__), "data", "artifactWithoutAttachmentResponse.json"), "r").read())
ATH_CONTENT  = open(os.path.join(os.path.dirname(__file__), "data", "attachment.svg"), "rb").read()
ART_CONTENT  = open(os.path.join(os.path.dirname(__file__), "data", "artifact.svg"), "rb").read()

class MockRestClient(MagicMock):
    def get(self, url):
        if url == '/incidents/2096/attachments/478':
            return copy.deepcopy(ATH_METADATA)
        elif url == '/incidents/2096/artifacts/26':
            return copy.deepcopy(ART_METADATA)
        elif url == '/incidents/2096/artifacts/36':
            return copy.deepcopy(ART_WO_ATCH)
        else:
            raise InvalidURL(f"unrecognized url : {url}")

    def get_content(self, url):
        if url == "/incidents/2096/attachments/478/contents":
            return ATH_CONTENT
        elif url == "/incidents/2096/artifacts/26/contents":
            return ART_CONTENT
        else:
            raise InvalidURL(f"unrecognized url : {url}")


def test_artifact():
    rest_client = MockRestClient()
    ath = AttachmentHandler(rest_client)
    output = ath.attach_files({}, incident_id=2096, artifact_id=26)
    output = output.get("files")
    assert len(output) == 1
    assert len(output[0]) == 2
    # test for default attachment_form_field_name
    assert output[0][0] == "file"

    _body = output[0][1]
    assert _body[0] == 'artifact.svg'
    assert _body[2] == 'image/svg+xml'
    assert _body[1] == open(os.path.join(os.path.dirname(__file__), "data", "artifact.svg"), "rb").read()

def test_attachment():
    field_name = "image/files"
    rest_client = MockRestClient()
    ath = AttachmentHandler(rest_client)
    output = ath.attach_files({}, incident_id=2096, attachment_id=478, attachment_form_field_name=field_name)
    output = output.get("files")
    assert len(output) == 1
    assert len(output[0]) == 2
    # test for custom attachment_form_field_name
    assert output[0][0] == field_name

    _body = output[0][1]
    assert _body[0] == 'attachment.svg'
    assert _body[2] == 'image/svg+xml'
    assert _body[1] == open(os.path.join(os.path.dirname(__file__), "data", "attachment.svg"), "rb").read()

def test_invalid_attachment():
    rest_client = MockRestClient()
    ath = AttachmentHandler(rest_client)
    with pytest.raises(InvalidURL) as err:
        ath.attach_files({}, incident_id=2096, attachment_id=500)

def test_invalid_artifact():
    rest_client = MockRestClient()
    ath = AttachmentHandler(rest_client)
    with pytest.raises(InvalidURL) as err:
        ath.attach_files({}, incident_id=2096, artifact_id=500)

def test_artifact_with_no_attachment():
    rest_client = MockRestClient()
    ath = AttachmentHandler(rest_client)
    with pytest.raises(ValueError):
        ath.attach_files({}, incident_id=2096, artifact_id=36)


def test_both():
    rest_client = MockRestClient()
    ath = AttachmentHandler(rest_client)
    output = ath.attach_files({}, incident_id=2096, artifact_id=26, attachment_id=478)
    output = output["files"]
    assert len(output) == 1
    assert len(output[0]) == 2
    # test for default attachment_form_field_name
    assert output[0][0] == "file"

    _body_artifact = output[0][1]
    assert _body_artifact[0] == 'attachment.svg'
    assert _body_artifact[2] == 'image/svg+xml'
    assert _body_artifact[1] == open(os.path.join(os.path.dirname(__file__), "data", "attachment.svg"), "rb").read()

def test_missing_incident_id():
    rest_client = MockRestClient()
    ath = AttachmentHandler(rest_client)
    assert ath.attach_files({}, artifact_id=10, attachment_id=10) == {}

def test_missing_artifact_attachment_id():
    rest_client = MockRestClient()
    ath = AttachmentHandler(rest_client)
    assert ath.attach_files({}, incident_id=10) == {}

def test_missing_arguments():
    rest_client = MockRestClient()
    ath = AttachmentHandler(rest_client)
    with pytest.raises(TypeError) as err:
        ath._get_file_contents()

def test_missing_incident_id():
    rest_client = MockRestClient()
    ath = AttachmentHandler(rest_client)
    with pytest.raises(AttributeError) as err:
        ath._get_file_contents(ATH_METADATA, object_type="attachments")

def test_get_artifact():
    rest_client = MockRestClient()
    ath = AttachmentHandler(rest_client)
    ath.incident_id = 2096
    ath.task_id = None
    ret = ath._get_file_contents(ATH_METADATA, object_type="attachments")
    assert ret
    assert FILE_CONTENTS in ret
    assert ret[FILE_CONTENTS]

def test_missing_artifact_id():
    rest_client = MockRestClient()
    ath = AttachmentHandler(rest_client)
    with pytest.raises(TypeError) as err:
        ath.find_artifact_by_id()

def test_working_artifact_id():
    rest_client = MockRestClient()
    ath = AttachmentHandler(rest_client)
    ath.incident_id = 2096
    response = ath.find_artifact_by_id(artifact_id=26)
    assert response.get(ATTACHMENT_ID)
    assert response.get(ATTACHMENT_ID) == ART_METADATA.get("attachment").get("id")
    assert response.get(ID)
    assert response.get(ID) == ART_METADATA.get("id")

def test_artifact_without_attachment():
    rest_client = MockRestClient()
    ath = AttachmentHandler(rest_client)
    ath.incident_id = 2096
    with pytest.raises(ValueError) as err:
        ath.find_artifact_by_id(artifact_id=36)


@pytest.fixture(scope="function")
def fx_mock_rest_client():
    yield MockRestClient()

def test_without_file_asbody(caplog, fx_mock_rest_client):
    caplog.set_level(logging.INFO)
    ath = AttachmentHandler(fx_mock_rest_client)

    sample_file = ('Content-Header', ('file_name', b'<svg id="Layer_1" da...Z"/></svg>', 'Content-Type'))
    _out = ath._add_files_to_request(files=sample_file, send_file_as_body=False, rest_properties={})
    assert _out == {"files" : [sample_file]}
    assert len(caplog.records) == 1
    assert "Sending file as multipart/form-data" in caplog.records[0].message

def test_without_file_as_body_with_rest_properties(caplog, fx_mock_rest_client):
    sample_rest_properties = {
        "headers" : {
            "authorization" : "bearer 112233",
            "content-type"  : "application/json"},
        "body" : {
            "data"  : "value",
            "value" : "data"}}
    sample_file = ('Content-Header', ('file_name', b'<svg id="Layer_1" da...Z"/></svg>', 'Content-Type'))

    caplog.clear(), caplog.set_level(logging.INFO)
    ath = AttachmentHandler(fx_mock_rest_client)
    _out = ath._add_files_to_request(files=sample_file, send_file_as_body=False, rest_properties=sample_rest_properties)
    assert _out["files"] == [sample_file]
    assert _out["headers"] == sample_rest_properties["headers"]
    assert _out["body"] == sample_rest_properties["body"]
    assert len(caplog.records) == 1
    assert "Sending file as multipart/form-data" in caplog.records[0].message

def test_data_already_exists(caplog, fx_mock_rest_client):
    sample_file = ('Content-Header', ('file_name', b'<svg id="Layer_1" da...Z"/></svg>', 'Content-Type'))
    sample_rest_properties = {
        "headers" : {
            "authorization" : "bearer 112233",
            "content-type"  : "application/json"},
        "body" : {
            "data"  : "value",
            "value" : "data"}}

    caplog.clear(), caplog.set_level(logging.INFO)
    ath = AttachmentHandler(fx_mock_rest_client)
    with pytest.raises(IntegrationError):
        ath._add_files_to_request(
            sample_file,
            send_file_as_body=True,
            rest_properties=sample_rest_properties)

def test_data_already_exists(caplog, fx_mock_rest_client):
    sample_file = ('Content-Header', ('file_name', b'<svg id="Layer_1" da...Z"/></svg>', 'Content-Type'))
    sample_rest_properties = {
        "headers" : {
            "authorization" : "bearer 112233",
            "content-type"  : "application/json"},
        "body" : {
            "data"  : "value",
            "value" : "data"}}

    caplog.clear(), caplog.set_level(logging.INFO)
    ath = AttachmentHandler(fx_mock_rest_client)
    with pytest.raises(IntegrationError):
        ath._add_files_to_request(
            files=sample_file,
            send_file_as_body=True,
            rest_properties=sample_rest_properties)

def test_content_type_already_exists(caplog, fx_mock_rest_client):
    sample_file = ('Content-Header', ('file_name', b'<svg id="Layer_1" da...Z"/></svg>', 'image/jpeg'))
    sample_rest_properties = {
        "headers" : {
            "authorization" : "bearer 112233",
            "content-type"  : "application/json"}}

    caplog.clear(), caplog.set_level(logging.INFO)
    ath = AttachmentHandler(fx_mock_rest_client)
    _out = ath._add_files_to_request(rest_properties=sample_rest_properties,
        files=sample_file,
        send_file_as_body=True)
    assert _out["headers"] == sample_rest_properties["headers"]
    assert _out["body"] == sample_file[1][1]
    assert 'WARNING' == caplog.records[1].levelname
    assert 'File content-type image/jpeg does not match with user provided content-type application/json' in caplog.records[1].message
    assert _out["headers"] == sample_rest_properties["headers"]

def test_set_content_type(caplog, fx_mock_rest_client):
    sample_file = ('Content-Header', ('file_name', b'....', 'image/jpeg'))
    sample_rest_properties = {"headers" : {}}

    ath = AttachmentHandler(fx_mock_rest_client)
    _out = ath._add_files_to_request(
        rest_properties=sample_rest_properties,
        files=sample_file,
        send_file_as_body=True)
    assert _out["headers"] == {'content-type': 'image/jpeg'}

    # missing `headers` key in rest_properties
    sample_file = ('Content-Header', ('file_name', b'....', 'image/jpeg'))
    sample_rest_properties = {}

    ath = AttachmentHandler(fx_mock_rest_client)
    _out = ath._add_files_to_request(
        files=sample_file,
        send_file_as_body=True,
        rest_properties=sample_rest_properties)
    assert _out["headers"] == {'content-type': 'image/jpeg'}
