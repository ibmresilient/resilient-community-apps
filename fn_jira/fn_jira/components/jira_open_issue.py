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
from resilient_lib import MarkdownParser, validate_fields, build_incident_url, build_resilient_url
from fn_jira.util.helper import CONFIG_DATA_SECTION, validate_app_configs

PACKAGE_NAME = CONFIG_DATA_SECTION
BROWSE_FRAGMENT = 'browse'

class FunctionComponent(ResilientComponent):

    """Component that implements Resilient function 'jirs_open_issue"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})
        self.res_params = opts.get("resilient", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})
        self.res_params = opts.get("resilient", {})

    @function("jira_open_issue")
    def _jira_open_issue_function(self, event, *args, **kwargs):
        """Function: create a jira issue. This requires app.config configuration information for jira """
        try:
            log = logging.getLogger(__name__)

            # Get + validate the app.config parameters:
            log.info("Validating app configs")
            app_configs = validate_app_configs(self.options)

            # Get + validate the function parameters:
            log.info("Validating function inputs")
            fn_inputs = validate_fields(["incident_id", "jira_project", "jira_issuetype", "jira_summary"], kwargs)
            log.info("Validated function inputs: %s", fn_inputs)

            appDict = self._build_createIssue_appDict(app_configs, fn_inputs)

            yield StatusMessage("starting...")
            jira_common = JiraCommon(self.opts, self.options)
            r = jira_common.create_issue(log, appDict)

            if r.get('key'):
                url = '/'.join((appDict['url'], BROWSE_FRAGMENT, r.get('key')))
                r['url'] = url

            # Produce a FunctionResult with the return value
            yield FunctionResult({"issue": r})      # json object needed, not a string representation
        except Exception as err:
            yield FunctionError(err)


    def _build_createIssue_appDict(self, app_configs, fn_inputs):
        '''
        build the dictionary used for the create api request
        :param kwargs:
        :return: dictionary of values to use
        '''

        # build the URL back to Resilient
        url = build_incident_url(build_resilient_url(self.res_params.get('host'), self.res_params.get('port')), fn_inputs.get("incident_id"))
        if fn_inputs.get("task_id"):
            url = "{}?task_id={}".format(url, fn_inputs.get("task_id"))

        html2markdwn = MarkdownParser(strikeout=constants.STRIKEOUT_CHAR, bold=constants.BOLD_CHAR,
                                      underline=constants.UNDERLINE_CHAR, italic=constants.ITALIC_CHAR)

        data = {
            'url': app_configs.get("url"),
            'user': app_configs.get("user"),
            'password': app_configs.get("password"),
            'verifyFlag': app_configs.get("verify_cert"),
            'project': fn_inputs.get("jira_project"),
            'issuetype': fn_inputs.get("jira_issuetype"),
            'fields': {
                'summary': fn_inputs.get("jira_summary"),
                'description': u"{}\n{}".format(url, html2markdwn.convert(fn_inputs.get('jira_description', '')))
            }
        }

        if fn_inputs.get('jira_priority'):
            data['fields']['priority'] = {"id": fn_inputs['jira_priority']}

        if fn_inputs.get('jira_assignee'):
            data['fields']['assignee'] = {"name": fn_inputs['jira_assignee']}

        return data
