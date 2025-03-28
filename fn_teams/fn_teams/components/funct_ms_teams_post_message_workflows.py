# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
# Generated with resilient-sdk v51.0.2.2.1096

"""AppFunction implementation"""

import json

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

from fn_teams.lib.microsoft_messages import MessageClient
from fn_teams.lib.microsoft_commons import get_principal_user

PACKAGE_NAME = "fn_teams"
FN_NAME = "ms_teams_post_message_workflows"

SCHEMA_CONTENT_TYPE = "contentType"
SCHEMA_CONTENT = "content"

SOAR_USER_NAME = "soar_user_name"
SOAR_USER_EMAIL = "soar_user_email"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'ms_teams_post_message_workflow'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Post a message to a Microsoft Teams channel
        Inputs:
            -   fn_inputs.teams_payload
            -   fn_inputs.incident_id
            -   fn_inputs.teams_channel
            -   fn_inputs.task_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields([
            "incident_id",
            "teams_channel",
            "teams_payload"], fn_inputs)

        # confirm that the message payload follows the ActiveCard format
        adaptive_card = json.loads(fn_inputs.teams_payload)

        if not (adaptive_card.get(SCHEMA_CONTENT_TYPE) and adaptive_card.get(SCHEMA_CONTENT)):
            yield FunctionResult({}, success=False, reason="AdaptiveCard format is not specified")
            return

        inputs = fn_inputs._asdict()
        message_client = MessageClient(self.rc)

        # get components of the webhook we'll be using
        webhook = self.options.get(fn_inputs.teams_channel.lower())
        if not webhook:
            yield FunctionResult({}, success=False, reason=f"app.config webhook not found: {fn_inputs.teams_channel}")
            return

        teams_payload = message_client.build_workflow_adaptive_card(
            self.opts["resilient"],
            inputs,
            adaptive_card,
            self.rest_client().org_id
        )
        # fill in requesting user if that information is specified
        teams_payload = get_soar_submission_user(teams_payload, self.get_fn_msg())

        proxies = self.rc.get_proxies()

        results = message_client.post_message_workflow(
            webhook,
            teams_payload,
            proxies
        )

        yield FunctionResult(results)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

def get_soar_submission_user(teams_payload, message):
    """ make substitutions for SOAR user_name or user_email if present in the top level
         adaptiveCard content

    :param teams_payload: adaptiveCard
    :type teams_payload: dict
    :param message: original message consumed from the message queue
    :type message: dict
    :return: updated adaptiveCard
    :rtype: dict
    """
    for content in teams_payload.get("content").get("body", []):
        if content.get("type") == "TextBlock" and content.get("text") and \
            (SOAR_USER_NAME in content.get("text") or SOAR_USER_EMAIL in content.get("text", "")):
            user_name, user_email = get_principal_user(message)
            content["text"] = content["text"].format(soar_user_name=user_name,
                                                     soar_user_email=user_email)

    return teams_payload
