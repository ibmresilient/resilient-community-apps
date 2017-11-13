# -*- coding: utf-8 -*-
"""System Integration Tests for FileSearch component."""

from __future__ import print_function
import os.path
import pytest
import logging

logging.getLogger().setLevel(logging.DEBUG)

data_dir = os.path.join(os.path.dirname(__file__), "sample_data")
config_data = """
[query_csv]
queue=query_csv
query_definitions_dir = %s
""" % (data_dir)

print(config_data)


@pytest.mark.usefixtures("configure_resilient")
class TestQueryCSV:
    """System tests for the QueryCSV component"""
    # Appliance Configuration Requirements
    destinations = ("query_csv",)
    custom_fields = {"field1": ("text", "Field 1", None),
                     "field2": ("number", "Field 2", None)}
    automatic_actions = {"CSV Test": ("query_csv", "Artifact",
                                      ({u"value": u"Test 1",
                                        u"field_name": u"artifact.value",
                                        u"method": u"equals"},)),
                         "CSV Test 2": ("query_csv", "Artifact",
                                        ({u"value": u"Test 2",
                                          u"field_name": u"artifact.value",
                                          u"method": u"equals"},)),
                         "CSV Test 3": ("query_csv", "Artifact",
                                        ({u"value": u"無選用ばル職",
                                          u"field_name": u"artifact.value",
                                          u"method": u"equals"},))}

    def test_query_csv_no_fieldlist(self, circuits_app, new_incident):
        """Query CSV File with specified fieldlist"""
        # Runs a CSV search and sets 2 custom fields
        inc = circuits_app.app.action_component.rest_client().post("/incidents",
                                                                   new_incident)
        artifact_data = {
            "type": {
                "name": "String"
            },
            "value": "Test 1",
            "description": {
                "format": "html",
                "content": "<div>A value to search for</div>"
            },
            "inc_id": inc['id']
        }
        artifact = circuits_app.app.action_component.rest_client().post("/incidents/%d/artifacts" % inc['id'],
                                                                        artifact_data)
        event = circuits_app.watcher.wait("csv_test_success",
                                          timeout=10,
                                          channel='actions.query_csv')
        assert event
        pytest.wait_for(event, "complete", True)
        event = circuits_app.watcher.wait("csv_test",
                                          timeout=10,
                                          channel='actions.query_csv')
        assert event
        pytest.wait_for(event, "complete", True)
        updated_inc = circuits_app.app.action_component.rest_client().get("/incidents/%d" % inc['id'])
        assert updated_inc["properties"]["field1"] == u"無選用ばル職"
        assert updated_inc["properties"]["field2"] == 7

    def test_query_csv_with_fieldlist(self, circuits_app, new_incident):
        """Query CSV File with fieldlist in file"""
        # Runs a CSV search and sets 2 custom fields
        inc = circuits_app.app.action_component.rest_client().post("/incidents",
                                                                   new_incident)
        artifact_data = {
            "type": {
                "name": "String"
            },
            "value": "Test 2",
            "description": {
                "format": "html",
                "content": "<div>A value to search for</div>"
            },
            "inc_id": inc['id']
        }
        artifact = circuits_app.app.action_component.rest_client().post("/incidents/%d/artifacts" % inc['id'],
                                                                        artifact_data)
        event = circuits_app.watcher.wait("csv_test_2_success",
                                          timeout=10,
                                          channel='actions.query_csv')
        assert event
        pytest.wait_for(event, "complete", True)
        event = circuits_app.watcher.wait("csv_test_2",
                                          timeout=10,
                                          channel='actions.query_csv')
        assert event
        pytest.wait_for(event, "complete", True)
        updated_inc = circuits_app.app.action_component.rest_client().get("/incidents/%d" % inc['id'])
        assert updated_inc["properties"]["field1"] == u"無選用ばル職"
        assert updated_inc["properties"]["field2"] == 7

    def test_csv_value_lookup(self, circuits_app, new_incident):
        """Query CSV File for value in column"""
        # Runs a CSV search and sets 2 custom fields
        inc = circuits_app.app.action_component.rest_client().post("/incidents",
                                                                   new_incident)
        artifact_data = {
            "type": {
                "name": "String"
            },
            "value": u"無選用ばル職",
            "description": {
                "format": "html",
                "content": "<div>A value to search for</div>"
            },
            "inc_id": inc['id']
        }
        artifact = circuits_app.app.action_component.rest_client().post("/incidents/%d/artifacts" % inc['id'],
                                                                        artifact_data)
        event = circuits_app.watcher.wait("csv_test_3_success",
                                          timeout=10,
                                          channel='actions.query_csv')
        assert event
        pytest.wait_for(event, "complete", True)
        event = circuits_app.watcher.wait("csv_test_3",
                                          timeout=10,
                                          channel='actions.query_csv')
        assert event
        pytest.wait_for(event, "complete", True)
        updated_inc = circuits_app.app.action_component.rest_client().get("/incidents/%d" % inc['id'])
        assert updated_inc["properties"]["field1"] == u"無選用ばル職"
        assert updated_inc["properties"]["field2"] == 7
