# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2023. All Rights Reserved.

import pytest
import sys
from resilient_circuits.actions_component import ResilientComponent
from fn_proofpoint_tap.components.fn_pp_threat_polling import PP_ThreatPolling
if sys.version_info.major == 2:
    from mock import patch
else:
    from unittest.mock import patch

MOCKED_OPS = {
    "fn_proofpoint_tap": {
        "base_url": "tap_base_url",
        "username": "tap_username",
        "password": "tap_password",
        "polling_interval": "tap_polling_interval",
        "startup_interval": "tap_startup_interval",
        "type_filter": "tap_type_filter",
        "score_threshold": "50"
    }
}

THREATS_INFO_MAP1 = {'threatsInfoMap': [{'threatID': 'threatID1', 'campaignId': 'campaignId1'}]}
THREATS_INFO_MAP1_RESULT = {'threatID1':'Proofpoint Threat ID', 'campaignId1':'Proofpoint Campaign ID'}

THREATS_INFO_MAP2 = {'threatsInfoMap': [{'threatID': 'threatID2', 'campaignId': 'campaignID2'}]}
THREATS_INFO_MAP2_RESULT = {'threatID2':'Proofpoint Threat ID', 'campaignID2':'Proofpoint Campaign ID'}

THREATS_INFO_MAP3 = {'threatsInfoMap': [{'threatID': 'threatID3', 'campaignId': 'campaignID3'},
                                        {'threatID': 'threatID4', 'campaignID': 'campaignID4'}]}
THREATS_INFO_MAP3_RESULT = {'threatID3':'Proofpoint Threat ID', 'campaignID3':'Proofpoint Campaign ID',
                            'threatID4':'Proofpoint Threat ID', 'campaignID4':'Proofpoint Campaign ID'}

THREATS_INFO_MAP4 = {'threatsInfoMap': [{}]}
THREATS_INFO_MAP4_RESULT = {}

THREATS_INFO_MAP5 = {'threatsInfoMap': [{'campaignID': '', 'threatID': u''}]}
THREATS_INFO_MAP5_RESULT = {}

class BlankClass(object):
    def __init__(self, opts):
        pass


class TestPPThreatPolling(object):
    """ Tests for the Proofpoint TAP Poller"""

    @staticmethod
    @patch('fn_proofpoint_tap.components.fn_pp_threat_polling.PP_ThreatPolling.getclass2typeids')
    @patch('fn_proofpoint_tap.components.fn_pp_threat_polling.PP_ThreatPolling._parseopts')
    @patch('fn_proofpoint_tap.components.fn_pp_threat_polling.PP_ThreatPolling.main')
    def get_pp_threat_polling(monkeypatch, mocked_main, mocked_parseops, mocked_getclass2typeids):
        """ get PP_ThreatPolling"""
        mocked_getclass2typeids.return_value = {'Malware': 19, 'Other': 18, 'impostor': 18, 'spam': 18,
                                                 'Phishing': 22, 'phish': 22, 'TBD / Unknown': 16, 'unknown': 16}
        mocked_parseops.return_value = None
        mocked_main.return_value = None
        if sys.version_info.major == 2:
            monkeypatch.setattr(ResilientComponent, "__init__", BlankClass)
        else:
            monkeypatch.setattr(ResilientComponent, "__init__", BlankClass.__init__)
        poller = PP_ThreatPolling(MOCKED_OPS)
        return poller

    @pytest.mark.parametrize("inputs,results", [
        (None, None),
        ("all", None),
        ("spam,, ALL  , phish", None),
        ("SpaM, ,", ({"spam"})),
        ("SpaM, MALWARE, Phish,", ({"spam", "malware", "phish"}))
    ])
    def test_get_type_filter(self, inputs, results, monkeypatch):
        """ Test getting set of type ids for the type_filter string."""
        poller = self.get_pp_threat_polling(monkeypatch)
        filters = poller._get_type_filter(inputs)
        assert filters == results

    @pytest.mark.parametrize("inputs,results", [
        (None, "N/A"),
        ([], "N/A"),
        (set(), "None"),
        ({"phish"}, "phish")
    ])
    def test_format_set(self, inputs, results):
        """
        Test format content of set and return str.
        """
        assert PP_ThreatPolling._format_set(inputs) == results

    @pytest.mark.parametrize("input_score_threshold,input_data,results", [
        (float(50), {'classification': 'malware', 'spamScore': 60, 'impostorScore': 0.0, 'malwareScore': 60, 'phishScore': 0}, {'malware', 'spam'}),
        (float(50), {'classification': 'malware', 'spamScore': 60, 'impostorScore': 0.0, 'malwareScore': 49, 'phishScore': 0}, {'spam'}),
        (float(50), {'classification': 'malware', 'spamScore': 49, 'impostorScore': 0.0, 'malwareScore': 49, 'phishScore': 0}, set()),
        (None, {'classification': 'malware', 'spamScore': 100, 'impostorScore': 0.0, 'malwareScore': 100, 'phishScore': 0}, {'malware'}),
        (float(50), {'classification': 'malware', 'spamScore': -1, 'impostorScore': -1, 'malwareScore': -1, 'phishScore': -1}, {'malware'})
    ])
    def test_get_threat_types(self, input_score_threshold, input_data, results, monkeypatch):
        """
        test pull the the threat types from the data.
        """
        poller = self.get_pp_threat_polling(monkeypatch)
        poller.score_threshold = input_score_threshold
        assert poller._get_threat_types(input_data) == results

    @pytest.mark.parametrize("inputs,results", [
        ({'malware', 'spam'}, {19, 18}),
        (None, set()),
        (set(), set())
    ])
    def test_map_to_incident_type_ids(self, inputs, results, monkeypatch):
        """
        Test mapping the threat types to incident type ids based on the class2typeids map.
        """
        poller = self.get_pp_threat_polling(monkeypatch)
        assert poller.map_to_incident_type_ids(inputs) == results

    @pytest.mark.parametrize("input_type_filter, type_filter, input_threat_types,results", [
        (None, None, {'malware', 'spam'}, [18, 19]),
        ({18}, {'spam'}, {'malware', 'spam'}, [18, 19]),
        ({22}, {'phish'}, {'malware', 'spam'}, None)
    ])
    def test_filtered_threat_types(self, input_type_filter, type_filter, input_threat_types, results, monkeypatch):
        """
        Test mapping the threat types to incident type ids and check to see if filtering is requested.
        """
        poller = self.get_pp_threat_polling(monkeypatch)
        poller.id_type_filter = input_type_filter
        poller.type_filter = type_filter
        assert poller._filtered_threat_types(input_threat_types) == results

    @pytest.mark.parametrize("threatsInfoMap, results", [
        (THREATS_INFO_MAP1, THREATS_INFO_MAP1_RESULT),
        (THREATS_INFO_MAP2, THREATS_INFO_MAP2_RESULT),
        (THREATS_INFO_MAP3, THREATS_INFO_MAP3_RESULT),
        (THREATS_INFO_MAP4, THREATS_INFO_MAP4_RESULT),
        (THREATS_INFO_MAP5, THREATS_INFO_MAP5_RESULT)
    ])
    def test_build_artifacts(self, threatsInfoMap, results, monkeypatch):
        poller = self.get_pp_threat_polling(monkeypatch)
        artifact_payload = poller.build_artifacts(threatsInfoMap)
        print (artifact_payload)
        for key in results:
            assert artifact_payload[key] == results[key]
