# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""
 These are methods for accessing Jira. The Jira REST API is used for general access.
 Requirements: JIRA URL and basic authentication user/password
"""
import json
from fn_jira.lib.requests_common import execute_call
from fn_jira.lib.resilient_common import clean_html

"""
This module implements the calls needed for jira api access. API operations supported:
) create an issue
) create a comment
) transition an issue
"""

# URL fragments needed along with the base jira URL
ISSUE_URL  = 'rest/api/2/issue'
TRANSITION_PARAM = 'transitions'
HTTP_HEADERS = {'content-type': 'application/json'}

COMMENT_PARAM = 'comment'


def create_issue(log, appDict):
    """Function: create a jira issue.
    :return the raw JSON returned from the api call
    """

    issue_url = '/'.join((appDict['url'], ISSUE_URL))

    payload = _mkCreatePayload(appDict)
    log and log.info(payload)

    result = execute_call(log, 'post', issue_url, appDict['user'], appDict['password'], payload, appDict['verifyFlag'], HTTP_HEADERS)

    return result


def transition_issue(log, appDict):
    """Function: transition a jira issue.
    :return: the raw JSON returned from the api call
    """

    url = '/'.join((appDict['url'], TRANSITION_PARAM))
    payload = _mkTransitionPayload(appDict)
    log and log.info(payload)

    result = execute_call(log, 'post', url, appDict['user'], appDict['password'], payload, appDict['verifyFlag'], HTTP_HEADERS)
    # log.info(result)

    if appDict['comment']:
        create_comment(log, appDict)

    return result

def create_comment(log, appDict):
    """Function: create a jira comment in a Jira issue. No JSON is returned on success
        :return: dictionary for a comment
    """

    url = '/'.join((appDict['url'], COMMENT_PARAM))

    payload = _mkCommentPayload(appDict)
    log and log.info(payload)

    resp =  execute_call(log, 'post', url, appDict['user'], appDict['password'], payload, appDict['verifyFlag'], HTTP_HEADERS)

    # successfully added comments return an empty dictionary: { }
    return resp

def _mkCreatePayload(appDict):
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
        payload['fields'][key] = clean_html(appDict['fields'][key])

    return json.dumps(payload)

def _mkCommentPayload(appDict):
    '''
    Build the payload for adding a Jira comment
    :param **dict could be **kwargs:
    :return: json payload for jira update
    '''
    
    payload = { "body": clean_html(appDict['comment'])}

    return json.dumps(payload)

def _mkTransitionPayload(appDict):
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

    return json.dumps(payload)
