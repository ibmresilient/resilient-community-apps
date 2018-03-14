import requests
import json
import logging
import re
from resilient_circuits import FunctionError

'''
This module implements the calls needed for jira api access. API operations supported:
) create an issue
) create a comment
) transition an issue
'''

# URL fragments needed along with the base jira URL
SEARCH_URL = 'rest/api/2/search'
ISSUE_URL  = 'rest/api/2/issue'
TRANSITION_PARAM = 'transitions'

COMMENT_PARAM = 'comment'

def create_issue(log, appDict):
    """Function: create a jira issue.
    Return the raw JSON returned from the api call
    """

    issue_url = '/'.join((appDict['url'], ISSUE_URL))

    payload = _mkCreatePayload(appDict)
    log.info(payload)

    result = execute_call(log, 'post', issue_url, appDict['user'], appDict['password'], payload)
    # log.info(result)

    return result


def transition_issue(log, appDict):
    """Function: transition a jira issue.
    Return the raw JSON returned from the api call
    """

    url = '/'.join((appDict['url'], TRANSITION_PARAM))
    payload = _mkTransitionPayload(appDict)
    log.info(payload)

    result = execute_call(log, 'post', url, appDict['user'], appDict['password'], payload)
    # log.info(result)

    if appDict['comment']:
        create_comment(log, appDict)

    return result

def create_comment(log, appDict):
    """Function: create a jira comment in a Jira issue. No JSON is returned on success"""

    url = '/'.join((appDict['url'], COMMENT_PARAM))

    payload = _mkCommentPayload(appDict)
    log.info(payload)

    resp =  execute_call(log, 'post', url, appDict['user'], appDict['password'], payload)

    return resp


def execute_call(log, verb, url, user, password, payload):
    """Function: perform the http API call. Different types of http operations are supported: 
        GET, POST, PUT
        Errors raise FunctionError
    """
    
    try:
        headers = {'content-type': 'application/json'}

        log.info(payload)

        if verb == 'get':
            resp = requests.get(url, verify=False, headers=headers, data=payload, auth=(user, password)) ## verify=False for debugging
        elif verb == 'post':
            resp = requests.post(url, verify=False, headers=headers, data=payload, auth=(user, password)) ## verify=False for debugging
        elif verb == 'put':
            resp = requests.put(url, verify=False, headers=headers, data=payload, auth=(user, password)) ## verify=False for debugging
        else:
            raise FunctionError("unknown verb {}".format(verb))

        if resp is None:
            raise FunctionError('no response returned')

        if resp.status_code >= 300:
            log.info(resp)
            # get the result
            raise FunctionError(resp.text)


        # check if anything returned
        log.info(resp.text)
        if resp.text is None or len(resp.text) == 0:
            return { }          # make sure to always return a dictionary

        # get the result
        r = resp.json()

        # Produce a FunctionError with the return value
        return r      # json object needed, not a string representation
    except Exception as err:
        raise FunctionError(err)

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
        payload['fields'][key] = _cleanHtml(appDict['fields'][key])

    return json.dumps(payload)

def _mkCommentPayload(appDict):
    '''
    Build the payload for adding a Jira comment
    :param **dict could be **kwargs:
    :return: json payload for jira update
    '''
    
    payload = { "body": _cleanHtml(appDict['comment']) }

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

def _cleanHtml(htmlFragment):
    '''
    Resilient textarea fields return html fragments. This routine will remove the html and insert any code within <div></div>
    with a linefeed
    :param htmlFragment:
    :return: cleaned up code
    '''

    tmp = re.sub(r'</div>', '\n', htmlFragment)
    tmp = re.sub(r'</ol>', '\n', tmp)
    tmp = re.sub(r'</li>', '\n', tmp)
    return re.sub(r'<([^>]+)>', '', tmp)       # removes all remaining html

if (__name__) == '__main__':
    log = logging.getLogger(__name__)
    # myDict = {
    #      'url': 'https://jira1-01.internal.resilientsystems.com/',
    #      'user': 'mscherfling',
    #      'password': 'EL3V@te1bm',
    #      'project': 'DISCO',
    #      'issuetype': 'Bug',
    #      'fields': {
    #         'summary': 'Resilient Issue',
    #         'description': 'Test here'
    #      }
    #  }
    # #
    # create_issue(log, myDict)

    myDict = {
          'url': 'https://jira1-01.internal.resilientsystems.com/rest/api/2/issue/DISCO-44',
          'user': 'mscherfling',
          'password': 'EL3V@te1bm',
          'transitionId': '41',
          'comment': 'resolution comment'
    }
    #
    transition_issue(log, myDict)

    # myDict = {
    #     'url': 'https://jira1-01.internal.resilientsystems.com/rest/api/2/issue/DISCO-8',
    #     'user': 'mscherfling',
    #     'password': 'EL3V@te1bm',
    #     'fields': {
    #         'labels': 'newLabel',
    #         'description': 'new description'
    #     },
    #     'comment': 'added comment'
    # }
    # #
    # update_issue(log, myDict)