# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function

from resilient_circuits.action_message import FunctionException_, FunctionError_

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch
import pytest

from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult, FunctionError
import json
import os

PACKAGE_NAME = "fn_mitre_integration"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

def call_mitre_function(circuits, function_params, func_name, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction(func_name, function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait(func_name+"_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestMITRE:
    """ Tests for the utilities_excel_query function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """

        func = get_function_definition(PACKAGE_NAME, "mitre_technique_information")
        assert func is not None

        func = get_function_definition(PACKAGE_NAME, "mitre_tactic_information")
        assert func is not None

    # Technique information
    @pytest.mark.livetest
    @pytest.mark.parametrize("tech_name, tech_id",
                             [
                                 (None, "T1453"),
                                 (None, "T1155"),
                                 (None, "T1245"),
                                 ("Port Knocking", None),
                                 ("Port Knocking", "T1453")
                             ])
    def test_technique_information(self, tech_name, tech_id, circuits_app):
        function_params = {
            "mitre_technique_name": tech_name,
            "mitre_technique_id": tech_id,
            "mitre_technique_mitigation_only": False
        }
        # When Function Error Gets called in testing, the runner fails
        assert call_mitre_function(circuits_app, function_params, "mitre_technique_information")

    @pytest.mark.livetest
    @pytest.mark.parametrize("tech_name, tech_id",
                             [
                                 (None, None),
                                 ("Made up", None),
                                 (None, "Made up")
                             ])
    def test_technique_information_fails(self, tech_name, tech_id, circuits_app):
        function_params = {
            "mitre_technique_name": tech_name,
            "mitre_technique_id": tech_id,
            "mitre_technique_mitigation_only": False
        }
    
        with pytest.raises(AssertionError):
            assert call_mitre_function(circuits_app, function_params, "mitre_technique_information")


    # Tactic information
    @pytest.mark.livetest
    @pytest.mark.parametrize("tact_name, tact_id",
                             [
                                 (None, "TA0007"),
                                 ("Collection", None),
                                 ("Collection", "TA0007")
                             ])
    def test_tactic_information(self, tact_name, tact_id, circuits_app):
        function_params = {
            "mitre_tactic_name": tact_name,
            "mitre_tactic_id": tact_id
        }
        # When Function Error Gets called in testing, the runner fails
        assert call_mitre_function(circuits_app, function_params, "mitre_tactic_information")

    @pytest.mark.livetest
    @pytest.mark.parametrize("tact_name, tact_id",
                             [
                                 (None, None),
                                 ("Made up", None),
                                 (None, "Made up")
                             ])
    def test_tactic_information_fails(self, tact_name, tact_id, circuits_app):
        function_params = {
            "mitre_tactic_name": tact_name,
            "mitre_tactic_id": tact_id
        }
    
        with pytest.raises(AssertionError):
            assert call_mitre_function(circuits_app, function_params, "mitre_tactic_information")

    # Software Information
    @pytest.mark.livetest
    @pytest.mark.parametrize("tech_name, tech_id",
                             [
                                 (None, "T1156"), #enterprise
                                 (None, "T1437"), #Mobile
                             ])
    def test_software_information(self, tech_name, tech_id, circuits_app):
        function_params = {
            "mitre_technique_name": tech_name,
            "mitre_technique_id": tech_id
        }
        # When Function Error Gets called in testing, the runner fails
        results = call_mitre_function(circuits_app, function_params, "mitre_techniques_software")
        assert results
        assert len(results["content"]["mitre_software"])

    @pytest.mark.livetest
    @pytest.mark.parametrize("tech_name, tech_id",
                             [
                                 (None, "T1245"), # Pre-Attack
                                 (None, "T1526"), # Enterprise
                                 (None, "T1470") # Mobile
                             ])
    def test_software_empty(self, tech_name, tech_id, circuits_app):
        function_params = {
            "mitre_technique_name": tech_name,
            "mitre_technique_id": tech_id
        }
        # When Function Error Gets called in testing, the runner fails
        results = call_mitre_function(circuits_app, function_params, "mitre_techniques_software")
        assert results
        assert len(results["content"]["mitre_software"]) == 0

    @pytest.mark.livetest
    @pytest.mark.parametrize("tech_name, tech_id",
                             [
                                 (None, None),
                                 ("Made up", None),
                                 (None, "Made up")
                             ])
    def test_software_fails(self, tech_name, tech_id, circuits_app):
        function_params = {
            "mitre_technique_name": tech_name,
            "mitre_technique_id": tech_id
        }
    
        with pytest.raises(AssertionError):
            assert call_mitre_function(circuits_app, function_params, "mitre_techniques_software")

    # Groups using technique
    @pytest.mark.livetest
    @pytest.mark.parametrize("tech_name, tech_id",
                             [
                                 (None, "T1134"), #enterprise
                                 (None, "T1437"), #Mobile
                             ])
    def test_group_information(self, tech_name, tech_id, circuits_app):
        function_params = {
            "mitre_technique_name": tech_name,
            "mitre_technique_id": tech_id
        }
        # When Function Error Gets called in testing, the runner fails
        results = call_mitre_function(circuits_app, function_params, "mitre_groups_using_technique")
        assert results
        assert len(results["content"]["mitre_groups"])

    @pytest.mark.livetest
    @pytest.mark.parametrize("tech_name, tech_id",
                             [
                                 (None, "T1245"), # Pre-Attack
                                 (None, "T1155"), # Enterprise
                                 (None, "T1475") # Mobile
                             ])
    def test_groups_empty(self, tech_name, tech_id, circuits_app):
        function_params = {
            "mitre_technique_name": tech_name,
            "mitre_technique_id": tech_id
        }
    
        result = call_mitre_function(circuits_app, function_params, "mitre_groups_using_technique")
        assert len(result["content"]["mitre_groups"]) == 0

    @pytest.mark.livetest
    @pytest.mark.parametrize("tech_name, tech_id",
                             [
                                 (None, None),
                                 ("Made up", None),
                                 (None, "Made up")
                             ])
    def test_group_information_fails(self, tech_name, tech_id, circuits_app):
        function_params = {
            "mitre_technique_name": tech_name,
            "mitre_technique_id": tech_id
        }
    
        with pytest.raises(AssertionError):
            assert call_mitre_function(circuits_app, function_params, "mitre_groups_using_technique")

