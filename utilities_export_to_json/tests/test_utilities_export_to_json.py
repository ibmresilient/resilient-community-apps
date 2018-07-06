# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function

from resilient_circuits.action_message import FunctionException_, FunctionError_

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch
import pytest

from export_to_json.bin.export_to_json import main
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult, FunctionError
import resilient
import json
import os
import sys
import logging
import re

OBJECT_TYPE_DATA = {
	"task": "task_fields.json",
	"note": "note_fields.json",
	"milestone": "milestone_fields.json",
	"incident": "incident_fields.json",
	"attachment": "attachment_fields.json",
	"artifact": "artifact_fields.json"
}

TEST_TYPE = None

def get_types(url):
	data = ""
	with open(("tests/data/types.json"), "r") as json_file:
		data = json_file.read().replace("\n", "")

	return json.loads(data)

def check_str_for_regex(regex, str):
	pattern = re.compile(regex)
	return bool(pattern.match(str))

def get_fields(url):
	object_type = re.search('\/types\/(.*.)\/fields', url, re.IGNORECASE).group(1)
	object_filename = ""
	try:
		object_filename = OBJECT_TYPE_DATA[object_type]
	except KeyError:
		return {}

	data = ""
	with open(("tests/data/" + object_filename), "r") as json_file:
		data = json_file.read().replace("\n", "")

	return json.loads(data)

def get_basic_incident_data():
	data = ""
	with open(("tests/data/basic_incident_data.json"), "r") as json_file:
		data = json_file.read().replace("\n", "")

	return json.loads(data)

def get_incident_data(url):
	incident_id = re.search("\/incidents\/([0-9]+)\?.*$", url, re.IGNORECASE).group(1)
	print("Requested incident %s!" % incident_id)
	incidents = ""
	with open(("tests/data/incidents.json"), "r") as json_file:
		incidents = json.loads(json_file.read())

	return incidents[incident_id]

object_types = {}

def get_incident_object_data(url):
	global object_types

	if url.find("?") is not -1:
		regex = re.search("\/incidents\/([0-9]+)\/(.*)\?.*$", url, re.IGNORECASE)
	else:
		regex = re.search("\/incidents\/([0-9]+)\/(.*)", url, re.IGNORECASE)

	incident_id = regex.group(1)
	object_type = regex.group(2)

	if object_type and TEST_TYPE == "standard":
		object_types[object_type] = False

	if TEST_TYPE == "partial_response_object" and object_types[object_type] is False:
		return {}

	print("Getting %s of incident %i!" % (object_type, int(incident_id)))
	if object_type == "table_data":
		object_type = "datatables"
	elif object_type == "comments":
		object_type = "notes"

	object_data = ""
	with open(("tests/data/incident_data/" + str(incident_id) + "_" + str(object_type) + ".json"), "r") as json_file:
		object_data = json.loads(json_file.read())

	return object_data

partial_response_extent = {"types": True, "incident_query": True, "incident_full": True}

class FakeResilientClient:
	def get(self, url):
		if TEST_TYPE == "no_response":
			return {}
		elif TEST_TYPE == "no_response_none":
			return None

		print("URL: %s" % url)
		if check_str_for_regex("\/types\/.*.\/fields", url):
			return get_fields(url)
		elif check_str_for_regex("\/types$", url) and partial_response_extent["types"]:
			return get_types(url)
		elif check_str_for_regex("\/incidents\/[0-9]+\?.*$", url) and partial_response_extent["incident_full"]:
			return get_incident_data(url)
		elif check_str_for_regex("\/incidents\/[0-9]+/.*", url):
			return get_incident_object_data(url)

		return {}

	def post(self, url, query):
		if TEST_TYPE == "no_response":
			return {}
		elif TEST_TYPE == "no_response_none":
			return None

		if check_str_for_regex("\/incidents\/query.*", url) and partial_response_extent["incident_query"]:
			return get_basic_incident_data()

		return {}

def handle_resilient_get_client(opts):
	return FakeResilientClient()

json_dumps_called = False
def fake_json_dump(object, outfile):
	global json_dumps_called
	print("big yeet")
	json_dumps_called = True
	return None

def call_export_to_json():
	testargs = ["export_to_json.py", "export.json", "time_incident_modified"]
	with patch.object(sys, 'argv', testargs):
		main()

@patch("resilient.get_client", side_effect=handle_resilient_get_client)
@patch("json.dump", side_effect=fake_json_dump)
def test_standard(caplog, a):
	"""This just makes sure the program works when given expected data"""
	caplog.set_level(logging.INFO)
	global json_dumps_called
	
	TEST_TYPE = "standard"

	call_export_to_json()

	TEST_TYPE = ""

	if json_dumps_called:
		json_dumps_called = False
		assert True
	else:
		assert False


@patch("resilient.get_client", side_effect=handle_resilient_get_client)
@patch("json.dump", side_effect=fake_json_dump)
def test_no_response_empty_object(caplog, a):
	"""Simulate empty object response from API"""
	caplog.set_level(logging.INFO)
	TEST_TYPE = "no_response"

	call_export_to_json()

	TEST_TYPE = ""

	assert True

@patch("resilient.get_client", side_effect=handle_resilient_get_client)
@patch("json.dump", side_effect=fake_json_dump)
def test_no_response_none(caplog, a):
	"""Simulate None response from API"""
	caplog.set_level(logging.INFO)
	TEST_TYPE = "no_response_none"

	call_export_to_json()

	TEST_TYPE = ""

	assert True

@patch("resilient.get_client", side_effect=handle_resilient_get_client)
@patch("json.dump", side_effect=fake_json_dump)
def test_partial_response(caplog, a):
	"""Simulate partial responses from API"""
	global partial_response_extent
	global object_types
	caplog.set_level(logging.INFO)

	partial_response_extent["types"] = False
	partial_response_extent["incident_query"] = False
	partial_response_extent["incident_full"] = False

	TEST_TYPE = "partial_response"
	excepted = False
	try:
		call_export_to_json()
	except Exception:
		excepted = True

	for field_name in list(partial_response_extent.keys()):
		print("field_name: %s" % field_name)
		excepted = False
		try:
			call_export_to_json()
		except Exception:
			excepted = True

		partial_response_extent[field_name] = True

		if excepted is False:
			assert False

	TEST_TYPE = "partial_response_object"

	for field_name in list(object_types.keys()):
		object_types[field_name] = True
		call_export_to_json()

	if os.path.exists("export.json"):
		os.remove("export.json")

	if os.path.exists(".resilient_lastrun"):
		os.remove(".resilient_lastrun")

	assert True