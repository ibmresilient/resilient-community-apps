# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
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
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from .jira_common import transition_issue
from fn_jira.lib.resilient_common import validateFields, clean_html

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'jira_transition_issue"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("jira", {})
        self.log = logging.getLogger(__name__)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
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
            r = transition_issue(self.log, appDict)

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
        validateFields(['jira_url', 'jira_transition_id'], kwargs)

        appDict = {
            'user': self.options['user'],
            'password': self.options['password'],
            'url': kwargs['jira_url'],
            'verifyFlag': True if self.options['verifyflag'] == 'True' else False,
            'transitionId': kwargs['jira_transition_id']
        }

        # optional
        if kwargs.get('jira_comment', None):
            appDict['comment'] = clean_html(kwargs['jira_comment'])

        return appDict
