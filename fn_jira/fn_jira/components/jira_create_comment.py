# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
Preprocessor script:
inputs.jira_url = incident.properties.jiraurl
inputs.jira_comment = note.text.content
"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from .jira_common import create_comment


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
            jira_url = kwargs.get("jira_url")  # text
            jira_comment = kwargs.get("jira_comment")  # text

            log = logging.getLogger(__name__)
            log.info("jira_url: %s", jira_url)
            log.info("jira_comment: %s", jira_comment)

            appDict = self._build_comment_appDict(kwargs)
            resp = create_comment(self.log, appDict)

            # Produce a FunctionResult with the return value
            yield FunctionResult(resp)
        except Exception as err:
            yield FunctionError(err)


    def _build_comment_appDict(self, kwargs):
        '''
        build the dictionary used to create a comment
        :param kwargs:
        :return: dictionary of values to use
        '''

        # test for required fields
        if not kwargs.get('jira_url', None):
            raise AttributeError("Missing required field: jira_url")

        if not kwargs.get('jira_comment', None):
            raise AttributeError("Missing required field: jira_comment")

        appDict = {
            'user': self.options['user'],
            'password': self.options['password'],
            'url': kwargs['jira_url'],
            'comment': self.get_textarea_param(kwargs['jira_comment'])
        }

        return appDict