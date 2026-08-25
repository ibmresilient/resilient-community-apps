# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

"""AppFunction implementation"""
from resilient_lib import IntegrationError, validate_fields
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

from fn_teams.lib import constants
from fn_teams.lib.microsoft_messages import MessageClient
from fn_teams.lib.microsoft_authentication import  MicrosoftAuthentication

PACKAGE_NAME = constants.PACKAGE_NAME
FN_NAME = "ms_teams_read_message"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'ms_teams_enable_team'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        The Graph API's read message method is one of Microsoft's protected APIs since
        it has access to sensitive data. The user must grant this application permission
        to access their data in order for this application to function. This means that
        only the resources to which the user has access, such as channels and teams, will
        be available to this application. This feature allows read of all messages
        on the channel or the replies to a specific message. The function can retrieve all
        replies to a certain message if it is given the message id for that message. The
        function will dump all messages in that channel back into SOAR if the channel name
        attribute is given. This application will required both authentication headers for
        the application to function. Application permission is used for finding the group,
        teams and channels, whereas the Delegated permission is used for reading messaged
        from the channel.

        options:
        --------
            message_id             <str> : Id of the message who's replies are to be retrieved
            channel_id             <str> : Id of the channel, the message belongs
            group_id               <str> : Id of the group, the channel belongs
            channel_name           <str> : Name of the MS Channel to be deleted
            ms_description         <str> : Description for the Channel
            ms_group_mail_nickname <str> : Mail nickname for the group (Must be unique)
            ms_group_name          <str> : Name of the Microsoft Group

        Returns:
        --------
            Response <dict> : A response with all the messages of a channel or the replies
                              to a particular message and all information related to it,
                              or an error message from the MS Graph api if the operation
                              fails
         """

        yield self.status_message(constants.STATUS_STARTING_APP.format(FN_NAME))

        validate_fields(["refresh_token"], self.options)

        options = {}
        if getattr(fn_inputs, 'ms_message_id', ""):
            options["message_id"] = fn_inputs.ms_message_id

        if getattr(fn_inputs, 'ms_channel_name', ""):
            options["channel_name"] = fn_inputs.ms_channel_name
        elif getattr(fn_inputs, 'ms_channel_id', ""):
            options["channel_id"] = fn_inputs.ms_channel_id
        else:
            raise IntegrationError("One of: ms_channel_name or ms_channel_id is required")

        if getattr(fn_inputs, 'ms_groupteam_id', ""):
            options["group_id"] = fn_inputs.ms_groupteam_id
        elif getattr(fn_inputs, 'ms_group_mail_nickname', ""):
            options["group_mail_nickname"] = fn_inputs.ms_group_mail_nickname
        elif getattr(fn_inputs, 'ms_groupteam_name', ""):
            options["group_name"] = fn_inputs.ms_groupteam_name
        else:
            raise IntegrationError("One of: ms_groupteam_id, ms_groupteam_name or group_mail_nickname is required")

        try:
            yield self.status_message(constants.STATUS_GENERATE_HEADER)
            authenticator = MicrosoftAuthentication(self.rc, self.options)
            dual_headers = {}
            dual_headers["application"] = authenticator.authenticate_application_permissions()
            dual_headers["delegated"]   = authenticator.authenticate_delegated_permissions(self.options.get("refresh_token"))
            authenticated = True
            yield self.status_message(constants.STATUS_SUCCESSFULLY_AUTHENTICATED)

        except IntegrationError as err:
            yield self.status_message(constants.STATUS_AUTHENTICATION_FAILED)
            authenticated = False
            yield FunctionResult({}, success=False, reason=str(err))

        if authenticated:
            try:
                messenger = MessageClient(self.rc)
                response = messenger.read_messages(dual_headers, options)
                yield FunctionResult(response, success=True)

            except IntegrationError as err:
                yield FunctionResult({}, success=False, reason=str(err))
