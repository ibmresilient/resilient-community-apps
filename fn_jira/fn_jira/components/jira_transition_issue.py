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
from resilient_lib import validate_fields, MarkdownParser, str_to_bool

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'jira_transition_issue"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get("jira", {})
        self.log = logging.getLogger(__name__)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get("jira", {})

    @function("jira_transition_issue")
    def _jira_transition_issue_function(self, event, *args, **kwargs):
        """Function: transition a jira issue. This requires app.config configuration information for jira
           It uses fields passed from resilient:
            jira_url - complete url for the issue to transition
            jira_transition_id - jira id to transition the issue. This is found in jira via the url:
               https://<jira host>/rest/api/2/status/
        """
        try:
            appDict = self._build_transitionIssue_appDict(kwargs)

            yield StatusMessage("starting...")
            jira_common = JiraCommon(self.opts, self.options)
            r = jira_common.transition_issue(self.log, appDict)

            # Produce a FunctionResult with the return value
            yield FunctionResult({"issue": r})      # json object needed, not a string representation
        except Exception as err:
            yield FunctionError(err)

    def _build_transitionIssue_appDict(self, kwargs):
        '''
        build the dictionary used for the transition api request
        :param kwargs:
        :return: dictionary of values to use
        '''

        # test for required fields
        validate_fields(['jira_url', 'jira_transition_id'], kwargs)

        appDict = {
            'user': self.options['user'],
            'password': self.options['password'],
            'url': kwargs['jira_url'],
            'verifyFlag': str_to_bool(self.options.get('verify_cert', 'True')),
            'transitionId': kwargs['jira_transition_id'],
        }

        if kwargs.get('jira_resolution'):
            appDict['resolution'] = kwargs['jira_resolution']

        # optional
        if kwargs.get('jira_comment', None):
            html2markdwn = MarkdownParser(strikeout=constants.STRIKEOUT_CHAR, bold=constants.BOLD_CHAR,
                                          underline=constants.UNDERLINE_CHAR, italic=constants.ITALIC_CHAR)
            appDict['comment'] = html2markdwn.convert(kwargs['jira_comment'])

        return appDict

