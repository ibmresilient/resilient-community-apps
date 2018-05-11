# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation
Preprocessor script:
inputs.jira_url = incident.properties.jiraurl
inputs.jira_comment = note.text.content
"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from .jira_common import create_comment
from fn_jira.lib.resilient_common import validateFields, clean_html


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'jira_create_comment"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("jira", {})
        self.log = logging.getLogger(__name__)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("jira", {})

    @function("jira_create_comment")
    def _jira_create_comment_function(self, event, *args, **kwargs):
        """Function: create a jira comment"""
        try:
            # Get the function parameters:
            appDict = self._build_comment_appDict(kwargs)

            yield StatusMessage("starting...")
            resp = create_comment(self.log, appDict)

            # Produce a FunctionResult with the return value
            yield FunctionResult(resp)
        except Exception as err:
            yield FunctionError(err)


    def _build_comment_appDict(self, kwargs):
        """
        build the dictionary used to create a comment
        :param kwargs:
        :return: dictionary of values to use
        """

        # test for required fields
        validateFields(['jira_url', 'jira_comment'], kwargs)

        jira_comment = clean_html(self.get_textarea_param(kwargs['jira_comment']))
        if len(jira_comment.strip()) == 0:
            raise FunctionError("comment is empty after rich text is removed")

        appDict = {
            'user': self.options['user'],
            'password': self.options['password'],
            'url': kwargs['jira_url'],
            'verifyFlag': True if self.options.get('verifyflag', 'True') == 'True' else False,
            'comment': jira_comment
        }

        return appDict