# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

"""Integrations between Resilient and Jira
    It supports: transitioning a jira issue with a comment

  Preprocessor script:
    inputs.jira_url = incident.properties.jiraurl
    inputs.jira_comment = "Resolution: {}\n{}".format(incident.resolution_id, incident.resolution_summary.content)

  method calls return json when an issue is created:
    "{"id":"19320","key":"DISCO-2","self":"https://jira1-01.internal.resilientsystems.com/rest/api/2/issue/19320"}"
  errors:
    {"errorMessages":[],"errors":{"project":"project is required"}}

See config.py for properties needed for jira access
"""

import logging
import fn_jira.lib.constants as constants
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from .jira_common import JiraCommon
from resilient_lib import validate_fields, MarkdownParser
from fn_jira.util.helper import CONFIG_DATA_SECTION, validate_app_configs

PACKAGE_NAME = CONFIG_DATA_SECTION


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'jira_transition_issue"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("jira_transition_issue")
    def _jira_transition_issue_function(self, event, *args, **kwargs):
        """Function: transition a jira issue. This requires app.config configuration information for jira
           It uses fields passed from resilient:
            jira_url - complete url for the issue to transition
            jira_transition_id - jira id to transition the issue. This is found in jira via the url:
               https://<jira host>/rest/api/2/status/
        """
        try:
            log = logging.getLogger(__name__)

            # Get + validate the app.config parameters:
            log.info("Validating app configs")
            app_configs = validate_app_configs(self.options)

            # Get + validate the function parameters:
            log.info("Validating function inputs")
            fn_inputs = validate_fields(["jira_url", "jira_transition_id"], kwargs)
            log.info("Validated function inputs: %s", fn_inputs)

            appDict = self._build_transitionIssue_appDict(app_configs, fn_inputs)

            yield StatusMessage("starting...")
            jira_common = JiraCommon(self.opts, self.options)
            r = jira_common.transition_issue(log, appDict)

            # Produce a FunctionResult with the return value
            yield FunctionResult({"issue": r})      # json object needed, not a string representation
        except Exception as err:
            yield FunctionError(err)

    def _build_transitionIssue_appDict(self, app_configs, fn_inputs):
        '''
        build the dictionary used for the transition api request
        :param kwargs:
        :return: dictionary of values to use
        '''

        appDict = {
            'user': app_configs.get("user"),
            'password': app_configs.get("password"),
            'url': fn_inputs.get('jira_url'),
            'verifyFlag': app_configs.get("verify_cert"),
            'transitionId': fn_inputs.get('jira_transition_id'),
        }

        if fn_inputs.get('jira_resolution'):
            appDict['resolution'] = fn_inputs.get('jira_resolution')

        # optional
        if fn_inputs.get('jira_comment'):
            html2markdwn = MarkdownParser(strikeout=constants.STRIKEOUT_CHAR, bold=constants.BOLD_CHAR,
                                          underline=constants.UNDERLINE_CHAR, italic=constants.ITALIC_CHAR)
            appDict['comment'] = html2markdwn.convert(fn_inputs.get('jira_comment'))

        return appDict

