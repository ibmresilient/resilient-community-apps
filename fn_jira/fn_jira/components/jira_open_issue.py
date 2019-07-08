# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

"""Integrations between Resilient and Jira
    It supports: creating a jira issue with a title (summary) and description

  Preprocessor script:
    desc = ''
    if incident.description is not None:
      desc = incident.description.content

    inputs.incidentID = incident.id
    inputs.jira_description = "Incident types: {}\nNist Attack Vectors: {}\n\nAdditional Information: {}".format(incident.incident_type_ids, incident.nist_attack_vectors, desc)
    inputs.jira_summary = "Resilient: {}".format(incident.name)
  Postprocessor script:
    incident.properties.jiraid = results.issue['key']
    incident.properties.jiraurl = results.issue['self']

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
from resilient_lib import MarkdownParser, validate_fields, str_to_bool, build_incident_url, build_resilient_url

BROWSE_FRAGMENT = 'browse'

class FunctionComponent(ResilientComponent):

    """Component that implements Resilient function 'jirs_open_issue"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get("jira", {})
        self.res_params = opts.get("resilient", {})
        self.log = logging.getLogger(__name__)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get("jira", {})
        self.res_params = opts.get("resilient", {})

    @function("jira_open_issue")
    def _jira_open_issue_function(self, event, *args, **kwargs):
        """Function: create a jira issue. This requires app.config configuration information for jira """
        try:
            appDict = self._build_createIssue_appDict(kwargs)

            yield StatusMessage("starting...")
            jira_common = JiraCommon(self.opts, self.options)
            r = jira_common.create_issue(self.log, appDict)

            if r.get('key'):
                url = '/'.join((appDict['url'], BROWSE_FRAGMENT, r.get('key')))
                r['url'] = url

            # Produce a FunctionResult with the return value
            yield FunctionResult({"issue": r})      # json object needed, not a string representation
        except Exception as err:
            yield FunctionError(err)


    def _build_createIssue_appDict(self, kwargs):
        '''
        build the dictionary used for the create api request
        :param kwargs:
        :return: dictionary of values to use
        '''

        validate_fields(['incident_id', 'jira_project', 'jira_issuetype', 'jira_summary'], kwargs)

        # build the URL back to Resilient
        url = build_incident_url(build_resilient_url(self.res_params.get('host'), self.res_params.get('port')), kwargs['incident_id'])
        if kwargs.get("task_id"):
            url = "{}?task_id={}".format(url, kwargs.get("task_id"))

        html2markdwn = MarkdownParser(strikeout=constants.STRIKEOUT_CHAR, bold=constants.BOLD_CHAR,
                                      underline=constants.UNDERLINE_CHAR, italic=constants.ITALIC_CHAR)

        data = {
            'url': self.options['url'],
            'user': self.options['user'],
            'password': self.options['password'],
            'verifyFlag': str_to_bool(self.options.get('verify_cert', 'True')),
            'project': self.get_textarea_param(kwargs['jira_project']),
            'issuetype': self.get_textarea_param(kwargs['jira_issuetype']),
            'fields': {
                'summary': self.get_textarea_param(kwargs['jira_summary']),
                'description': u"{}\n{}".format(url, html2markdwn.convert(kwargs.get('jira_description', '')))
            }
        }

        if kwargs.get('jira_priority'):
            data['fields']['priority'] = { 'id': kwargs['jira_priority'] }

        if kwargs.get('jira_assignee'):
            data['fields']['assignee'] = { "name": kwargs['jira_assignee'] }

        return data
