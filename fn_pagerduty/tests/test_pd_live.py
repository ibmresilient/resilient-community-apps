# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import unittest
import logging
import sys
import time
from fn_pagerduty.components.pd_common import *


log = logging.getLogger(__name__)

# test constants
API_TOKEN = '<API Token>'


class TestPagerDuty(unittest.TestCase):
    incident_id = ''

    def setUp(self):
        self.baseDict = {
            'api_token': API_TOKEN,
            'resilient_url': 'https://localhost:8443',
            'verifyFlag': False
        }


    def test1CreateIncident(self):
        """
        test creating an incident
        :return: JSON result
        """
        payloadDict = self._buildIncidentDict(self.baseDict, True)

        resp = create_incident(log, payloadDict)

        self.assertIsNotNone(resp)
        self.assertIn('incident', resp)

        self.__class__.incident_id = resp['incident']['id']  # save new value


    def test2EscalateIncident(self):
        """
        create an incident and acknowledge with a higher prioritiy
        :return:
        """

        resp = update_incident(log, self.baseDict, self.__class__.incident_id, 'acknowledged', 'p1', None)

        self.assertIsNotNone(resp)
        self.assertIn('incident', resp)


    def test3CreateNote(self):
        """ create a note and check for success """
        resp = create_note(log, self.baseDict, self.__class__.incident_id, 'description here')

        self.assertIsNotNone(resp)
        self.assertIn('note', resp)


    def test4ResolveIncident(self):
        """
        create an incident and acknowledge with a higher prioritiy
        :return:
        """
        resp = update_incident(log, self.baseDict, self.__class__.incident_id, 'resolved', None, 'resolved note')

        self.assertIsNotNone(resp)
        self.assertIn('incident', resp)


    def testGetPriorities(self):
        """
        test finding a priority
        :return:
        """
        id = find_priority_by_name(None, self.baseDict, 'P1')
        self.assertIsNotNone(id)

        id = find_priority_by_name(None, self.baseDict, 'p1')
        self.assertIsNotNone(id)

        id = find_priority_by_name(None, self.baseDict, 'p1 ')
        self.assertIsNotNone(id)

        id = find_priority_by_name(None, self.baseDict, 'xx')
        self.assertIsNone(id)


    def testGetEscalationPolicy(self):
        """
        test finding an escalation policy
        :return:
        """
        id = find_escalation_policy_by_name(None, self.baseDict, 'Default')
        self.assertIsNotNone(id)

        id = find_escalation_policy_by_name(None, self.baseDict, 'default ')
        self.assertIsNotNone(id)

        id = find_escalation_policy_by_name(None, self.baseDict, 'xx')
        self.assertIsNone(id)


    def testGetService(self):
        """
        test finding a service
        :return:
        """
        id = find_service_by_name(None, self.baseDict, 'API Service')
        self.assertIsNotNone(id)

        id = find_service_by_name(None, self.baseDict, 'api service ')
        self.assertIsNotNone(id)

        id = find_service_by_name(None, self.baseDict, 'xx')
        self.assertIsNone(id)


    def _buildIncidentDict(self, baseDict, makeIncidentKey):
        payloadDict = baseDict.copy()
        payloadDict['title'] = 'myTitle'
        payloadDict['description'] = 'free form description'
        payloadDict['service'] = 'API service'
        payloadDict['escalation_policy'] = 'default'
        payloadDict['priority'] = 'p2'
        if makeIncidentKey:
            payloadDict['incident_key'] = 'Res-'+str(int(time.time()))

        return payloadDict


    def tearDown(self):
        pass


if __name__ == '__main__':
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger(__name__).setLevel( logging.DEBUG )
    unittest.main()
