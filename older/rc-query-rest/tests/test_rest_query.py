"""System Integration Tests for REST Query component"""
from __future__ import print_function

import os.path
import pytest
from circuits.core.handlers import handler

data_dir = os.path.join(os.path.dirname(__file__), "rest_sample_data")
config_data = """[rest]
queue = rest
query_definitions_dir = %s
test_endpoint = http://httpbin.org/post
""" % (data_dir)

@pytest.mark.usefixtures("configure_resilient")
class TestRESTIntegrationTests:
    """ System tests for the REST Query component """
    # Appliance Configuration Requirements
    destinations = ("rest",)
    automatic_actions = {"Payload String Test": ("rest", "Incident",
                                                 ({u"value": u"Payload Is String",
                                                   u"field_name": u"incident.name",
                                                   u"method": u"equals"},)),
                         "Payload Dict Test": ("rest", "Incident",
                                               ({u"value": u"Payload Is Dict",
                                                 u"field_name": u"incident.name",
                                                 u"method": u"equals"},))}

    payload_testdata = [pytest.param("Payload Is String", "payload_string_test",
                                     id="string_payload"),
                        pytest.param("Payload Is Dict", "payload_dict_test",
                                     id="dict_payload")]

    @pytest.mark.parametrize("inc_name,rule_name", payload_testdata)
    def test_payload_string_or_dict(self, inc_name, rule_name, circuits_app, new_incident):
        """ http-body is a string to render or a dict"""

        # Incident data will be posted to HTTP Bin and then the incident name will be
        # changed to the incident ID that was posted.

        new_incident["name"] = inc_name
        inc = circuits_app.app.action_component.rest_client().post("/incidents", new_incident)

        event = circuits_app.watcher.wait(rule_name + "_success", timeout=10, channel='actions.rest')
        assert event
        pytest.wait_for(event, "complete", True)
        event = circuits_app.watcher.wait("QueryEvent", timeout=10, channel='actions.rest')
        assert event
        pytest.wait_for(event, "complete", True)

        updated_inc = circuits_app.app.action_component.rest_client().get("/incidents/%d" % inc["id"])
        assert updated_inc["name"] == str(inc["id"])
