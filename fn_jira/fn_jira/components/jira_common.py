# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""
 These are methods for accessing Jira. The Jira REST API is used for general access.
 Requirements: JIRA URL and basic authentication user/password
"""
import json
from fn_jira.lib.requests_common import execute_call

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
    log and log.debug(payload)

    result = execute_call(log, 'post', issue_url, appDict['user'], appDict['password'], payload, appDict['verifyFlag'], HTTP_HEADERS)
    log and log.debug(result)

    return result


def transition_issue(log, appDict):
    """Function: transition a jira issue.
    :return: the raw JSON returned from the api call
    """

    url = '/'.join((appDict['url'], TRANSITION_PARAM))
    payload = _mkTransitionPayload(appDict)
    log and log.debug(payload)

    #find_transitions(log, appDict) # uncomment to see transitions for this enterprise

    result = execute_call(log, 'post', url, appDict['user'], appDict['password'], payload, appDict['verifyFlag'], HTTP_HEADERS)
    log and log.debug(result)

    return result

def find_transitions(log, appDict):
    """
    determine the ticket transitions for a given issue
    :param log: 
    :param appDict: 
    :return: None
    """
    url = '/'.join((appDict['url'], TRANSITION_PARAM))

    result = execute_call(log, 'get', url, appDict['user'], appDict['password'], None, appDict['verifyFlag'], HTTP_HEADERS)
    log and log.debug(result)

    return result


def create_comment(log, appDict):
    """Function: create a jira comment in a Jira issue. No JSON is returned on success
        :return: dictionary for a comment
    """

    url = '/'.join((appDict['url'], COMMENT_PARAM))

    payload = _mkCommentPayload(appDict)
    log and log.debug(payload)

    result =  execute_call(log, 'post', url, appDict['user'], appDict['password'], payload, appDict['verifyFlag'], HTTP_HEADERS)
    log and log.debug(result)

    # successfully added comments return an empty dictionary: { }
    return result

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
        payload['fields'][key] = appDict['fields'][key]

    return json.dumps(payload)

def _mkCommentPayload(appDict):
    '''
    Build the payload for adding a Jira comment
    :param **dict could be **kwargs:
    :return: json payload for jira update
    '''
    
    payload = { "body": appDict['comment'] }

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

    if appDict.get('comment'):
        comment = \
        { "comment":
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

