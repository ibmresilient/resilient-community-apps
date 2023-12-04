# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
import json
import pytest, unittest

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


def mock_rest_client_get(url):
    if INCIDENT_ID in url and ATTACHMENT_ID in url:
        return json.loads(open("data/ibmLog.json", "r"))

    if INCIDENT_ID in url and ARTIFACTS_ID in url:
        return json.loads(open("data/ibmLog.json", "r"))