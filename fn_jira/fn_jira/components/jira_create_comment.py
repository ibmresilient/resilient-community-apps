# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

"""Function implementation
Preprocessor script:
inputs.jira_url = incident.properties.jiraurl
inputs.jira_comment = note.text.content
"""

import logging
import fn_jira.lib.constants as constants
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from .jira_common import JiraCommon
from resilient_lib import validate_fields, MarkdownParser, str_to_bool
from fn_jira.util.helper import CONFIG_DATA_SECTION

PACKAGE_NAME = CONFIG_DATA_SECTION


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'jira_create_comment"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("jira_create_comment")
    def _jira_create_comment_function(self, event, *args, **kwargs):
        """Function: create a jira comment"""
        try:
            log = logging.getLogger(__name__)

            # Get the function parameters:
            appDict = self._build_comment_appDict(kwargs)

            yield StatusMessage("starting...")

            jira_common = JiraCommon(self.opts, self.options)
            resp = jira_common.create_comment(log, appDict)

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
        validate_fields(['jira_url', 'jira_comment'], kwargs)

        html2markdwn = MarkdownParser(strikeout=constants.STRIKEOUT_CHAR, bold=constants.BOLD_CHAR,
                                      underline=constants.UNDERLINE_CHAR, italic=constants.ITALIC_CHAR)
        jira_comment = html2markdwn.convert(self.get_textarea_param(kwargs['jira_comment']))
        if jira_comment is None or not jira_comment.strip():
            raise FunctionError("comment is empty after rich text is removed")

        appDict = {
            'user': self.options['user'],
            'password': self.options['password'],
            'url': kwargs['jira_url'],
            'verifyFlag': str_to_bool(self.options.get('verify_cert', 'True')),
            'comment': jira_comment
        }

        return appDict
