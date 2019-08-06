# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
"""
 These are methods for accessing Jira. The Jira REST API is used for general access.
 Requirements: JIRA URL and basic authentication user/password
"""
import json
import fn_jira.lib.constants as constants
from resilient_lib import RequestsCommon

"""
This module implements the calls needed for jira api access. API operations supported:
) create an issue
) create a comment
) transition an issue
"""

# URL fragments needed along with the base jira URL
ISSUE_URL = 'rest/api/2/issue'
TRANSITION_PARAM = 'transitions'

COMMENT_PARAM = 'comment'

class JiraCommon:
    def __init__(self, opts, function_opts):
        self.req_common = RequestsCommon(opts=opts, function_opts=function_opts)


    def create_issue(self, log, appDict):
        """Function: create a jira issue.
        :return the raw JSON returned from the api call
        """

        issue_url = '/'.join((appDict['url'], ISSUE_URL))

        payload = self._mkCreatePayload(appDict)

        resp = self.req_common.execute_call_v2('post', issue_url, auth=(appDict['user'], appDict['password']),
                                               data=payload, verify=appDict['verifyFlag'], headers=constants.HTTP_HEADERS)
        log and log.debug(resp)

        return self.get_json_result(resp)


    def transition_issue(self, log, appDict):
        """Function: transition a jira issue.
        :return: the raw JSON returned from the api call
        """

        url = '/'.join((appDict['url'], TRANSITION_PARAM))
        payload = self._mkTransitionPayload(appDict)

        #find_transitions(log, appDict) # uncomment to see transitions for this enterprise

        log and log.debug(payload)

        resp = self.req_common.execute_call_v2('post', url, auth=(appDict['user'], appDict['password']),
                                               data=payload, verify=appDict['verifyFlag'], headers=constants.HTTP_HEADERS)
        log and log.debug(resp)

        return self.get_json_result(resp)

    def find_transitions(self, log, appDict):
        """
        determine the ticket transitions for a given issue
        :param log:
        :param appDict:
        :return: None
        """
        url = '/'.join((appDict['url'], TRANSITION_PARAM))

        resp = self.req_common.execute_call_v2('get', url, auth=(appDict['user'], appDict['password']),
                                               verify=appDict['verifyFlag'], headers=constants.HTTP_HEADERS)
        log and log.debug(resp)

        return self.get_json_result(resp)


    def create_comment(self, log, appDict):
        """Function: create a jira comment in a Jira issue. No JSON is returned on success
            :return: dictionary for a comment
        """

        url = '/'.join((appDict['url'], COMMENT_PARAM))

        payload = self._mkCommentPayload(appDict)

        resp = self.req_common.execute_call_v2('post', url, auth=(appDict['user'], appDict['password']),
                                               data=payload, verify=appDict['verifyFlag'], headers=constants.HTTP_HEADERS)

        log and log.debug(resp)

        # successfully added comments return an empty dictionary: { }
        return self.get_json_result(resp)

    def get_json_result(self, resp):
        """
        get the response in json format, if possible
        :param resp:
        :return: None if errors or not json
        """
        try:
            result = resp.json() if resp and resp.content else None
        except:
            result = None

        return result

    def _mkCreatePayload(self, appDict):
        '''
        Build the payload for creating a Jira issue
        :param **dict could be **kwargs:
        :return: json payload for jira update
        '''

        payload = {
            "fields": {
                "project": {
                    "key": appDict.get('project')
                },
                "issuetype": {
                    "name": appDict.get('issuetype')
                }
            }
        }

        for key in appDict['fields']:
            payload['fields'][key] = appDict['fields'][key]

        return json.dumps(payload)

    def _mkCommentPayload(self, appDict):
        '''
        Build the payload for adding a Jira comment
        :param **dict could be **kwargs:
        :return: json payload for jira update
        '''

        payload = {"body": appDict['comment']}

        return json.dumps(payload)

    def _mkTransitionPayload(self, appDict):
        '''
        Build the payload needed to transition a Jira issue
        :param **dict could be **kwargs:
        :return: json payload for jira call
        '''

        payload = {
            "transition": {
                "id": appDict['transitionId']
            }
        }

        if appDict.get('comment'):
            comment = \
            {"comment":
                [
                    {
                        "add": {
                            "body": appDict['comment']
                        }
                    }
                ]
            }
            payload['update'] = comment

        if appDict.get('resolution'):
            resolution = {
                "resolution": {
                    "name": appDict['resolution']
                }
            }
            payload['fields'] = resolution

        return json.dumps(payload)
