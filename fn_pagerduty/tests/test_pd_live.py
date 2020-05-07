# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import unittest
import pytest
import logging
import sys
import time
from fn_pagerduty.components.pd_common import *


log = logging.getLogger(__name__)

# test constants
API_TOKEN = 'CHANGEME'


class TestPagerDuty(unittest.TestCase):
    incident_id = ''

    def setUp(self):
        self.baseDict = {
            'api_token': API_TOKEN,
            'resilient_client': 'IBM Resilient',
            'from_email': 'CHANGEME@ibm.com',
            'verifyFlag': False
        }

    @pytest.mark.livetest
    def test1CreateIncident(self):
        """
        test creating an incident
        :return: JSON result
        """
        payloadDict = self._buildIncidentDict(self.baseDict, True)

        resp = create_incident(payloadDict)

        self.assertIsNotNone(resp)
        self.assertIn('incident', resp)

        self.__class__.incident_id = resp['incident']['id']  # save new value

    @pytest.mark.livetest
    def test2EscalateIncident(self):
        """
        create an incident and acknowledge with a higher prioritiy
        :return:
        """

        resp = update_incident(self.baseDict, self.__class__.incident_id, 'acknowledged', 'p1', 'resolved')

        self.assertIsNotNone(resp)
        self.assertIn('incident', resp)

    @pytest.mark.livetest
    def test3CreateNote(self):
        """ create a note and check for success """
        resp = create_note(self.baseDict, self.__class__.incident_id, 'description here')

        self.assertIsNotNone(resp)
        self.assertIn('note', resp)

    @pytest.mark.livetest
    def test4ResolveIncident(self):
        """
        create an incident and acknowledge with a higher prioritiy
        :return:
        """
        resp = update_incident(self.baseDict, self.__class__.incident_id, 'resolved', None, 'resolved note')

        self.assertIsNotNone(resp)
        self.assertIn('incident', resp)

    @pytest.mark.livetest
    def testGetPriorities(self):
        """
        test finding a priority
        :return:
        """
        id = find_element_by_name(self.baseDict, 'priorities', 'P1')
        self.assertIsNotNone(id)

        id = find_element_by_name(self.baseDict, 'priorities', 'p1')
        self.assertIsNotNone(id)

        id = find_element_by_name(self.baseDict, 'priorities', 'p1 ')
        self.assertIsNotNone(id)

        id = find_element_by_name(self.baseDict, 'priorities', 'xx')
        self.assertIsNone(id)

    @pytest.mark.livetest
    def testGetEscalationPolicy(self):
        """
        test finding an escalation policy
        :return:
        """
        id = find_element_by_name(self.baseDict, 'escalation_policies', 'Default')
        self.assertIsNotNone(id)

        id = find_element_by_name(self.baseDict, 'escalation_policies', 'default ')
        self.assertIsNotNone(id)

        id = find_element_by_name(self.baseDict, 'escalation_policies', 'xx')
        self.assertIsNone(id)

    @pytest.mark.livetest
    def testGetService(self):
        """
        test finding a service
        :return:
        """
        id = find_element_by_name(self.baseDict, 'services', 'API Service')
        self.assertIsNotNone(id)

        id = find_element_by_name(self.baseDict, 'services', 'api service ')
        self.assertIsNotNone(id)

        id = find_element_by_name(self.baseDict, 'services', 'xx')
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

