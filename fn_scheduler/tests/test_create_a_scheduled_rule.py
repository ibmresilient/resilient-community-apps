# -*- coding: utf-8 -*-
"""
Tests using pytest_resilient_circuits
use the environment variable TEST_RESILIENT_APP_CONFIG to refer to the app.config file for testing
"""

from __future__ import print_function
import datetime
import logging
import pytest
import sys
if sys.version_info.major == 3:
    from unittest.mock import Mock, patch
else:
    from mock import Mock, patch

from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from fn_scheduler.lib.scheduler_helper import ResilientScheduler
from common import setup_mock_incident, setup_mock_actions, setup_evt

PACKAGE_NAME = "fn_scheduler"
FUNCTION_NAME = "create_a_scheduled_rule"

log = logging.getLogger(__name__)

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

now = datetime.datetime.now()
yyyymmdd = now.strftime('%s')


def call_create_a_scheduled_rule_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("create_a_scheduled_rule", function_params)
    setup_evt(evt)

    circuits.manager.fire(evt)
    event = circuits.watcher.wait("create_a_scheduled_rule_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestCreateAScheduledRule:
    """ Tests for the create_a_scheduled_rule function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None


    #@pytest.mark.skip
    @pytest.mark.parametrize("scheduler_type, scheduler_type_value, scheduler_rule_name, scheduler_rule_parameters, scheduler_label, incident_id, object_id, row_id, expected_results", [
        ('cron',     "* 2 * *", "Test Rule", "text=text", "bad cron", 123, 0, None, {"value": "xyz"}),
        ('interval', "2",       "Test Rule", "text=text", "bad interval", 123, 0, None, {"value": "xyz"}),
        ('date',     "10/31/2019", "Test Rule", "text=text", "bad date", 123, 0, None, {"value": "xyz"}),
        ('delta',    "2x",       "Test Rule", "text=text", "bad delta", 123, 0, None, {"value": "xyz"}),
        ('deltax',    "2x",       "Test Rule", "text=text", "bad scheduler name", 123, 0, None, {"value": "xyz"})
    ])
    @patch('fn_scheduler.lib.resilient_helper.get_rules')
    @patch('fn_scheduler.components.create_a_scheduled_rule.get_incident')
    def test_failure_scheduler_type(self, mock_incident, mock_rules,
                                    circuits_app, scheduler_type, scheduler_type_value,
                                    scheduler_rule_name, scheduler_rule_parameters, scheduler_label,
                                    incident_id, object_id, row_id, expected_results):
        """ Test calling with sample values for the parameters """
        setup_mock_incident(mock_incident)
        setup_mock_actions(mock_rules)

        function_params = {
            "scheduler_type": scheduler_type,
            "scheduler_type_value": scheduler_type_value,
            "scheduler_rule_name": scheduler_rule_name,
            "scheduler_rule_parameters": scheduler_rule_parameters,
            "scheduler_label": scheduler_label,
            "incident_id": incident_id,
            "object_id": object_id,
            "row_id": row_id
        }

        with pytest.raises(Exception):
            results = call_create_a_scheduled_rule_function(circuits_app, function_params)


    #@pytest.mark.skip
    @pytest.mark.parametrize("scheduler_type, scheduler_type_value, scheduler_rule_name, scheduler_rule_parameters, scheduler_label, incident_id, object_id, row_id, expected_results", [
        ('cron',     "* 2 * * *", "Rule not found", "text=text", "Rule not found", 123, 0, None, {"value": "xyz"}),
        ('interval', "2m",       "Test Rule", "text=text", "Rule disabled", 123, 0, None, {"value": "xyz"})
    ])
    @patch('fn_scheduler.lib.resilient_helper.get_rules')
    @patch('fn_scheduler.components.create_a_scheduled_rule.get_incident')
    def test_failure_scheduler_rule(self, mock_incident, mock_rules,
                                    circuits_app, scheduler_type, scheduler_type_value,
                                    scheduler_rule_name, scheduler_rule_parameters, scheduler_label,
                                    incident_id, object_id, row_id, expected_results):
        """ Test calling with sample values for the parameters """
        setup_mock_incident(mock_incident)
        setup_mock_actions(mock_rules, enabled=False)

        function_params = {
            "scheduler_type": scheduler_type,
            "scheduler_type_value": scheduler_type_value,
            "scheduler_rule_name": scheduler_rule_name,
            "scheduler_rule_parameters": scheduler_rule_parameters,
            "scheduler_label": scheduler_label,
            "incident_id": incident_id,
            "object_id": object_id,
            "row_id": row_id
        }

        with pytest.raises(Exception):
            results = call_create_a_scheduled_rule_function(circuits_app, function_params)


    #@pytest.mark.skip
    @pytest.mark.parametrize("scheduler_type, scheduler_type_value, scheduler_rule_name, scheduler_rule_parameters, scheduler_label, incident_id, object_id, row_id, expected_results", [
        ('cron',     "* 2 * * *", "Test Rule", "text=text", "incident closed", 123, 0, None, {"value": "xyz"})
    ])
    @patch('fn_scheduler.lib.resilient_helper.get_rules')
    @patch('fn_scheduler.components.create_a_scheduled_rule.get_incident')
    def test_failure_incident_closed(self, mock_incident, mock_rules,
                                     circuits_app, scheduler_type, scheduler_type_value,
                                     scheduler_rule_name, scheduler_rule_parameters, scheduler_label,
                                     incident_id, object_id, row_id, expected_results):
        """ Test calling with sample values for the parameters """
        setup_mock_incident(mock_incident, end_date=1546719640000)
        setup_mock_actions(mock_rules)

        function_params = {
            "scheduler_type": scheduler_type,
            "scheduler_type_value": scheduler_type_value,
            "scheduler_rule_name": scheduler_rule_name,
            "scheduler_rule_parameters": scheduler_rule_parameters,
            "scheduler_label": scheduler_label,
            "incident_id": incident_id,
            "object_id": object_id,
            "row_id": row_id
        }

        with pytest.raises(Exception):
            results = call_create_a_scheduled_rule_function(circuits_app, function_params)


    #@pytest.mark.skip
    @pytest.mark.parametrize("scheduler_type, scheduler_type_value, scheduler_rule_name, scheduler_rule_parameters, scheduler_label, incident_id, object_id, row_id, expected_results", [
        ('cron',     "* 2 * * *", "Test Rule", "text=text", "incident not found", 1234, 0, None, {"value": "xyz"})
    ])
    @patch('fn_scheduler.lib.resilient_helper.get_rules')
    @patch('fn_scheduler.components.create_a_scheduled_rule.get_incident')
    def test_failure_incident_not_found(self, mock_incident, mock_rules,
                                        circuits_app, scheduler_type, scheduler_type_value,
                                        scheduler_rule_name, scheduler_rule_parameters, scheduler_label,
                                        incident_id, object_id, row_id, expected_results):
        """ Test calling with sample values for the parameters """
        setup_mock_incident(mock_incident, success=False)
        setup_mock_actions(mock_rules)

        function_params = {
            "scheduler_type": scheduler_type,
            "scheduler_type_value": scheduler_type_value,
            "scheduler_rule_name": scheduler_rule_name,
            "scheduler_rule_parameters": scheduler_rule_parameters,
            "scheduler_label": scheduler_label,
            "incident_id": incident_id,
            "object_id": object_id,
            "row_id": row_id
        }

        with pytest.raises(Exception):
            results = call_create_a_scheduled_rule_function(circuits_app, function_params)


    #@pytest.mark.skip
    @pytest.mark.parametrize("scheduler_type, scheduler_type_value, scheduler_rule_name, scheduler_rule_parameters, scheduler_label, incident_id, object_id, row_id, expected_results", [
        ('cron',     "* 2 * * *", "Test Rule", "text=text", "object id mismatch", 123, 4, None, {"value": "xyz"})
    ])
    @patch('fn_scheduler.lib.resilient_helper.get_rules')
    @patch('fn_scheduler.components.create_a_scheduled_rule.get_incident')
    def test_failure_object_id_mismatch(self, mock_incident, mock_rules,
                                        circuits_app, scheduler_type, scheduler_type_value,
                                        scheduler_rule_name, scheduler_rule_parameters, scheduler_label,
                                        incident_id, object_id, row_id, expected_results):
        """ Test calling with sample values for the parameters """
        setup_mock_incident(mock_incident)
        setup_mock_actions(mock_rules, object_type=4)

        function_params = {
            "scheduler_type": scheduler_type,
            "scheduler_type_value": scheduler_type_value,
            "scheduler_rule_name": scheduler_rule_name,
            "scheduler_rule_parameters": scheduler_rule_parameters,
            "scheduler_label": scheduler_label,
            "incident_id": incident_id,
            "object_id": object_id,
            "row_id": row_id
        }

        with pytest.raises(Exception):
            results = call_create_a_scheduled_rule_function(circuits_app, function_params)


    #@pytest.mark.skip
    @pytest.mark.parametrize("scheduler_type, scheduler_type_value, scheduler_rule_name, scheduler_rule_parameters, "
                             "scheduler_label, incident_id, object_id, row_id, expected_results", [
                                 ('cron', "* 2 * * *", "Test Rule", None, "cron", 123, None, None, {"value": "xyz"}),
                                 ('interval', "2h", "Test Rule", None, "interval", 123, None, None, {"value": "xyz"}),
                                 ('date', "", "Test Rule", None, "date", 123, None, None, {"value": "xyz"}),
                                 ('delta', "2h", "Test Rule", None, "delta", 123, None, None, {"value": "xyz"}),
                                 ('delta', "2h", "unicode ΞΟΠΡ", None, "unicode ΞΟΠΡ", 123, None, None, {"value": "xyz"})
                             ])
    @patch('fn_scheduler.lib.resilient_helper.get_rules')
    @patch('fn_scheduler.components.create_a_scheduled_rule.get_incident')
    def test_success(self, mock_get_incident, mock_get_rules,
                     circuits_app, scheduler_type, scheduler_type_value,
                     scheduler_rule_name, scheduler_rule_parameters,
                     scheduler_label, incident_id, object_id, row_id, expected_results):
        """ Test calling with sample values for the parameters """
        setup_mock_incident(mock_get_incident)
        setup_mock_actions(mock_get_rules)

        rule_label = "{}_{}".format(scheduler_label, yyyymmdd)

        if scheduler_type == "date":
            dt = ResilientScheduler.get_interval("2h", date=True)
            scheduler_type_value = dt.strftime('%Y-%m-%d %H:%M:%S')

        function_params = {
            "scheduler_type": scheduler_type,
            "scheduler_type_value": scheduler_type_value,
            "scheduler_rule_name": scheduler_rule_name,
            "scheduler_rule_parameters": scheduler_rule_parameters,
            "scheduler_label": rule_label,
            "incident_id": incident_id,
            "object_id": object_id,
            "row_id": row_id
        }
        results = call_create_a_scheduled_rule_function(circuits_app, function_params)
        assert results['success']
