# -*- coding: utf-8 -*-

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
import test_emails

PACKAGE_NAME = "fn_email_header_validation"
FUNCTION_NAME = "email_header_validation_using_dkimarc"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_email_header_validation_using_dkimarc_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("email_header_validation_using_dkimarc", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("email_header_validation_using_dkimarc_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestEmailHeaderValidationUsingDkimarc:
    """ Tests for the email_header_validation_using_dkimarc function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("email_header_validation_target_email, expected_results", [
        (test_emails.arc_only(), {"dkim_verify": False,
                                  "arc_verify": True,
                                  "dkim_message": "Message is not DKIM signed",
                                  "arc_message": "success"}),
        (test_emails.arc_only_fail(), {"dkim_verify": False,
                                       "arc_verify": False,
                                       "dkim_message": "Message is not DKIM signed",
                                       "arc_message": "Most recent ARC-Message-Signature did not validate"}),
        (test_emails.dkim_arc_success(), {"dkim_verify": True,
                                          "arc_verify": True,
                                          "dkim_message": "success",
                                          "arc_message": "success"}),
        (test_emails.no_headers(), {"dkim_verify": False,
                                    "arc_verify": False,
                                    "dkim_message": "Message is not DKIM signed",
                                    "arc_message": "Message is not ARC signed"}),
        (test_emails.dkim_only(), {"dkim_verify": True,
                                   "arc_verify": False,
                                   "dkim_message": "success",
                                   "arc_message": "Message is not ARC signed"}),
        (test_emails.dkim_only_fail(), {"dkim_verify": False,
                                        "arc_verify": False,
                                        "dkim_message": "Most recent DKIM-Message-Signature did not validate",
                                        "arc_message": "Message is not ARC signed"})
    ])
    def test_success(self, circuits_app, email_header_validation_target_email, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "email_header_validation_target_email": email_header_validation_target_email
        }
        results = call_email_header_validation_using_dkimarc_function(circuits_app, function_params)
        assert(expected_results == results)