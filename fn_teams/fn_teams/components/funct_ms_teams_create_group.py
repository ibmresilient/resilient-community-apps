# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#
# """AppFunction implementation"""
from urllib import parse

from resilient_lib import validate_fields, IntegrationError
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

from fn_teams.lib import constants
from fn_teams.lib.microsoft_groups import GroupsInterface
from fn_teams.lib.microsoft_authentication import  MicrosoftAuthentication

PACKAGE_NAME = "fn_teams"
FN_NAME = "ms_teams_create_group"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'webex_delete_teamsrooms'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.opts = opts
        self.required_parameters = {}
        self.config_options = opts.get(PACKAGE_NAME, {})


    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):

        yield self.status_message(constants.STATUS_STARTING_APP.format(FN_NAME))

        validate_fields([
            "incident_id",
            "ms_group_name",
            "add_members_from",
            "ms_group_description",
            "ms_group_mail_nickname"], fn_inputs)

        self.required_parameters["rc"] = self.rc
        self.required_parameters["logger"] = self.LOG
        self.required_parameters["resclient"] = self.rest_client()

        self.required_parameters["incident_id"] = fn_inputs.incident_id
        self.required_parameters["group_name"] = fn_inputs.ms_group_name
        self.required_parameters["add_members_from"] = fn_inputs.add_members_from
        self.required_parameters["group_description"] = fn_inputs.ms_group_description
        self.required_parameters["group_mail_nickname"] = fn_inputs.ms_group_mail_nickname

        self.required_parameters["task_id"] = fn_inputs.task_id if hasattr(fn_inputs, 'task_id') else None
        self.required_parameters["owners_list"] = fn_inputs.ms_owners_list if hasattr(fn_inputs, 'ms_owners_list') else None
        self.required_parameters["additional_mambers"] = fn_inputs.additional_members if hasattr(fn_inputs, 'additional_members') else None

        try:
            yield self.status_message(constants.STATUS_GENERATE_HEADER)
            authenticator = MicrosoftAuthentication(self.required_parameters, self.config_options)
            self.required_parameters["header"] = authenticator.authenticate()
            authenticated = True
            yield self.status_message(constants.STATUS_SUCCESSFULLY_AUTHENTICATED)

        except IntegrationError as err:
            self.LOG.error(constants.STATUS_SUCCESSFULLY_AUTHENTICATED)
            yield self.status_message(constants.STATUS_AUTHENTICATION_FAILED)
            authenticated = False
            yield FunctionResult(None, success=False, reason=str(err))

        if authenticated:
            try:
                group_manager = GroupsInterface(self.required_parameters)
                response = group_manager.create_group()
                yield FunctionResult(response, success=True)
            except IntegrationError as err:
                yield FunctionResult(rason=str(err), success=False)
