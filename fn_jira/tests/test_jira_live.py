from fn_jira.components.jira_common import *
from fn_jira.components.resilient_common import merge_two_dicts
import logging
import unittest


class TestJira(unittest.TestCase):
    url = None

    def setUp(self):
        self.baseDict = {
            'url': 'https://<JIRA>',
            'user': '<USER>',
            'password': '<PASSWORD',
            # use verifyFlag to disable untrusted certificate verification
            'verifyFlag': False
        }
        self.log = logging.getLogger(__name__)

    def tearDown(self):
        pass

    def test1_CreateIssue(self):
        appDict = self._build_createPayload()

        resp = create_issue(self.log, appDict)
        self.assertIsNotNone(resp)
        self.assertIn('self', resp)

        TestJira.url = resp['self']


    def test5_CreateComment(self):
        appDict = self._build_commentPayload()

        resp = create_comment(self.log, appDict)
        self.assertIsNotNone(resp)


    def test7_TransitionIssue(self):
        appDict = self._build_transitionPayload()

        resp = transition_issue(self.log, appDict)
        self.assertIsNotNone(resp)


    def _build_createPayload(self):
        createDict = {
            'project': 'DISCO',
            'issuetype': 'Bug',
            'fields': {
                'summary': 'test name for Jira Issue',
                'description': "test description",
                'priority': { 'id': '2' }
            }
        }

        appDict = merge_two_dicts(self.baseDict, createDict)

        return appDict


    def _build_commentPayload(self):
        appDict = self.baseDict.copy()
        appDict['comment'] = 'test comment'
        appDict['url'] = TestJira.url

        return appDict


    def _build_transitionPayload(self):
        appDict = self.baseDict.copy()
        appDict['transitionId'] = '41'
        appDict['url'] = TestJira.url
        appDict['comment'] = 'test closed'

        return appDict
