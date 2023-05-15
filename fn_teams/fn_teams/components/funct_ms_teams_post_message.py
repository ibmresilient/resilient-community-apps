# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

"""AppFunction implementation"""
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

from fn_teams.lib import constants
from fn_teams.lib.microsoft_messages import MessageClient

PACKAGE_NAME = constants.PACKAGE_NAME
FN_NAME = "ms_teams_post_message"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'ms_teams_post_message'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        This application allows for posting Incident/Task details to a MS Teams channel.
        The application can be triggered from either incident or task level where,
        information about the incident or task is formulated and posted in a convenient
        manner. This information is posted to a channel specified by the teams_channel
        input. This channel name (specified by teams_channel) is used to lookup
        app.config to retrieve the appropriate channel webhook url.

        Inputs:
        -------
            task_id       <str> : If called from task then Task ID
            incident_id   <str> : Incident ID
            teams_channel <str> : Name of the channel
            teams_payload <str> : The payload generated with incident/task details
            teams_mrkdown <bol> : Enables/Disables markdown formatting

        Returns:
        --------
            Response <dict> : A response with the room/team options and details
                              or the error message if the meeting creation
         """

        yield self.status_message(constants.STATUS_STARTING_APP.format(FN_NAME))

        validate_fields([
            'incident_id',
            'teams_channel',
            'teams_payload'], fn_inputs)
        
        teams_channel = fn_inputs.teams_channel
        try:
            message_client = MessageClient(self.rc)
            status = message_client.post_message(
                self.opts,
                teams_channel = teams_channel,
                webhook_url = self.options.get(teams_channel.lower()),
                teams_payload = fn_inputs.teams_payload,
                org_id = self.rest_client().org_id,
                incident_id = fn_inputs.incident_id,
                task_id = fn_inputs.task_id if hasattr(fn_inputs,
                    'task_id') else False,
                teams_mrkdown = fn_inputs.teams_mrkdown if hasattr(fn_inputs,
                    'teams_mrkdown') else False)

            yield FunctionResult({
                "message" : (constants
                    .SUCCESSFULLY_POSTED_MESSAGE
                    .format(teams_channel))}, success=status)

        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
