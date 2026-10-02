# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from mock import patch
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from .mock_incident import IncidentMock, PACKAGE_NAME

FUNCTION_NAME = "send_email2"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = IncidentMock


def call_send_email2_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("send_email2", function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("send_email2_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestSendEmail2:
    """ Tests for the send_email2 function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    fail_template_not_found = {
        "mail_inline_template": None,
        "mail_from": None,
        "mail_template_label": "not found",
        "mail_body": None,
        "mail_importance": "high",
        "mail_bcc": None,
        "mail_attachments": None,
        "mail_message_id": None,
        "mail_to": "a@example.com",
        "mail_subject": "sample text",
        "mail_in_reply_to": None,
        "mail_cc": None,
        "mail_incident_id": 123,
        "mail_encryption_recipients": None
    }

    fail_no_recipient_to = {
        "mail_inline_template": None,
        "mail_from": None,
        "mail_template_label": None,
        "mail_body": None,
        "mail_importance": "high",
        "mail_bcc": None,
        "mail_attachments": None,
        "mail_message_id": None,
        "mail_to": None,
        "mail_subject": "sample text",
        "mail_in_reply_to": None,
        "mail_cc": None,
        "mail_incident_id": 123,
        "mail_encryption_recipients": None
    }

    fail_no_body = {
        "mail_inline_template": None,
        "mail_from": None,
        "mail_template_label": None,
        "mail_body": None,
        "mail_importance": "high",
        "mail_bcc": None,
        "mail_attachments": None,
        "mail_message_id": None,
        "mail_to": "a@example.com",
        "mail_subject": "sample text",
        "mail_in_reply_to": None,
        "mail_cc": None,
        "mail_incident_id": 123,
        "mail_encryption_recipients": None
    }

    fail_both_templates = {
        "mail_inline_template": "something",
        "mail_from": None,
        "mail_template_label": "label",
        "mail_body": None,
        "mail_importance": "high",
        "mail_bcc": None,
        "mail_attachments": None,
        "mail_message_id": None,
        "mail_to": "a@example.com",
        "mail_subject": "sample text",
        "mail_in_reply_to": None,
        "mail_cc": None,
        "mail_incident_id": 123,
        "mail_encryption_recipients": None
    }

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (fail_template_not_found, None),
        (fail_no_body, None),
    ])
    def test_fails(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_send_email2_function(circuits_app, mock_inputs)
        assert(results['success'] == False)


    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (fail_no_recipient_to, None),
        (fail_both_templates, None)
    ])

    def test_exceptions(self, circuits_app, mock_inputs, expected_results):
        with pytest.raises(ValueError) as e_valueError:
            results = call_send_email2_function(circuits_app, mock_inputs)

    success_body = {
        "mail_inline_template": None,
        "mail_from": None,
        "mail_template_label": None,
        "mail_body": "success_body",
        "mail_importance": None,
        "mail_bcc": None,
        "mail_attachments": None,
        "mail_message_id": None,
        "mail_to": "a@example.com",
        "mail_subject": "sample text",
        "mail_in_reply_to": None,
        "mail_cc": None,
        "mail_incident_id": 123,
        "mail_encryption_recipients": None
    }

    success_inline_template = {
        "mail_inline_template": "{{ incident.id }}",
        "mail_from": None,
        "mail_template_label": None,
        "mail_body": "success_inline_template",
        "mail_importance": None,
        "mail_bcc": None,
        "mail_attachments": None,
        "mail_message_id": None,
        "mail_to": "a@example.com",
        "mail_subject": "sample text",
        "mail_in_reply_to": None,
        "mail_cc": None,
        "mail_incident_id": 123,
        "mail_encryption_recipients": None
    }

    success_inline_template_with_body = {
        "mail_inline_template": "{{ incident.id }}-{{ mail.mail_subject }}",
        "mail_from": None,
        "mail_template_label": None,
        "mail_body": "success_inline_template_with_body",
        "mail_importance": None,
        "mail_bcc": None,
        "mail_attachments": None,
        "mail_message_id": None,
        "mail_to": "a@example.com",
        "mail_subject": "sample text",
        "mail_in_reply_to": None,
        "mail_cc": None,
        "mail_incident_id": 123,
        "mail_merge_body": True,
        "mail_encryption_recipients": None
    }

    @patch('fn_outbound_email.components.funct_send_email2.send_msg')
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (success_body, success_body['mail_body']),
        (success_inline_template, str(success_inline_template['mail_incident_id'])),
        (success_inline_template_with_body, f"{str(success_inline_template_with_body['mail_incident_id'])}-{success_inline_template_with_body['mail_subject']}\n{success_inline_template_with_body['mail_body']}")
    ])
    def test_inline_template(self, mock_send_msg, circuits_app, mock_inputs, expected_results):
        mock_send_msg.return_value = None

        results = call_send_email2_function(circuits_app, mock_inputs)
        assert(results['success'] == True)
        assert(results['content']['mail_body']) == expected_results
