# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_apility"
FUNCTION_NAME = "fn_apility"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_apility_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_apility", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_apility_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnApility:
    """ Tests for the fn_apility function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("apility_lookup_type, apility_lookup_value, expected_results", [
        ('Domain', "mailnator.com", {"value": {'response': {'domain': {'blacklist': ['DEA', 'IVOLO-DED', 'LISINGE-DED', 'MARTENSON-DED'], 'blacklist_mx': ['DEA', 'IVOLO-DED', 'LISINGE-DED', 'MARTENSON-DED'], 'blacklist_ns': [], 'mx': ['mail2.mailinator.com', 'mail.mailinator.com'], 'ns': ['betty.ns.cloudflare.com', 'james.ns.cloudflare.com'], 'score': -1}, 'ip': {'address': '104.25.199.31', 'blacklist': ['IVOLO-DED-IP', 'LISINGE-DED-IP', 'MARTENSON-DED-IP'], 'is_quarantined': False, 'score': -1}, 'source_ip': {'address': '203.163.232.254', 'blacklist': [], 'is_quarantined': False, 'score': 0}, 'score': -2}, 'type': 'baddomain', 'query': 'mailinator.com'}}),
        ('Email Sender', "test@mailnator.com", {"value": {'response': {'email': {'blacklist': [], 'score': 0}, 'domain': {'blacklist': ['DEA', 'IVOLO-DED', 'LISINGE-DED', 'MARTENSON-DED'], 'blacklist_mx': ['DEA', 'IVOLO-DED', 'LISINGE-DED', 'MARTENSON-DED'], 'blacklist_ns': [], 'mx': ['mail2.mailinator.com', 'mail.mailinator.com'], 'ns': ['betty.ns.cloudflare.com', 'james.ns.cloudflare.com'], 'score': -1}, 'disposable': {'is_disposable': True, 'score': -1}, 'freemail': {'is_freemail': False, 'score': 0}, 'ip': {'blacklist': ['IVOLO-DED-IP', 'LISINGE-DED-IP', 'MARTENSON-DED-IP'], 'is_quarantined': False, 'address': '104.25.199.31', 'score': -1}, 'source_ip': {'blacklist': [], 'is_quarantined': False, 'address': '203.163.232.254', 'score': 0}, 'address': {'is_role': False, 'is_well_formed': True, 'score': 0}, 'smtp': {'exist_mx': True, 'exist_address': True, 'exist_catchall': True, 'graylisted': False, 'timedout': False, 'score': 0}, 'score': -3, 'email_address': 'test@mailinator.com'}, 'type': 'bademail', 'query': 'test@mailinator.com'}}),
        ('IP Address', "185.157.185.248", {"value": {'fullip': {'geo': {'address': '185.157.185.248', 'hostname': '', 'country': 'ES', 'country_names': {'de': 'Spanien', 'en': 'Spain', 'es': 'España', 'fr': 'Espagne', 'ja': 'スペイン', 'pt-BR': 'Espanha', 'ru': 'Испания', 'zh-CN': '西班牙'}, 'country_geoname_id': 2510769, 'continent': 'EU', 'continent_names': {'de': 'Europa', 'en': 'Europe', 'es': 'Europa', 'fr': 'Europe', 'ja': 'ヨーロッパ', 'pt-BR': 'Europa', 'ru': 'Европа', 'zh-CN': '欧洲'}, 'continent_geoname_id': 6255148, 'latitude': 38.0883, 'longitude': -0.7235, 'time_zone': 'Europe/Madrid', 'region': 'Alicante', 'region_names': {'de': 'Alicante', 'en': 'Alicante', 'es': 'Alicante', 'fr': 'Alicant', 'ja': 'アリカンテ'}, 'region_geoname_id': 2521976, 'city': 'Rojales', 'city_names': {'en': 'Rojales', 'es': 'Rojales', 'ru': 'Рохалес', 'zh-CN': '罗哈莱斯'}, 'city_geoname_id': 2511752, 'accuracy_radius': 1000, 'postal': '03170', 'as': {'asn_date': '2016-06-29', 'networks_v6': [], 'asn_registry': 'ripencc', 'asn_country_code': 'ES', 'networks': ['185.157.184.0/22'], 'name': 'Meganet Plus Slu', 'asn_description': 'MEGANETPLUS, ES', 'networks_v4': [], 'country': 'ES', 'asn': '202658'}}, 'hostname': '', 'baddomain': {'domain': {}, 'source_ip': {}, 'ip': {}, 'score': 0}, 'badip': {'score': 0, 'blacklists': []}, 'history': {'score': -1, 'activity': [{'ip': '185.157.185.248', 'timestamp': 1539217701729, 'command': 'rem', 'blacklists': '', 'blacklist_change': 'UCEPROTECT-LEVEL1'}, {'ip': '185.157.185.248', 'timestamp': 1538656513112, 'command': 'rem', 'blacklists': 'UCEPROTECT-LEVEL1', 'blacklist_change': 'NIXSPAM-IP'}, {'ip': '185.157.185.248', 'timestamp': 1538563826814, 'command': 'add', 'blacklists': 'UCEPROTECT-LEVEL1,NIXSPAM-IP', 'blacklist_change': 'NIXSPAM-IP'}, {'ip': '185.157.185.248', 'timestamp': 1538235059844, 'command': 'add', 'blacklists': 'UCEPROTECT-LEVEL1', 'blacklist_change': 'UCEPROTECT-LEVEL1'}], 'score_1day': False, 'score_7days': False, 'score_30days': False, 'score_90days': True, 'score_180days': True, 'score_1year': True}, 'score': -1, 'whois': {'nir': None, 'asn_registry': 'ripencc', 'asn': '202658', 'asn_cidr': '185.157.184.0/22', 'asn_country_code': 'ES', 'asn_date': '2016-06-29', 'asn_description': 'MEGANETPLUS, ES', 'query': '185.157.185.248', 'network': {'handle': '185.157.184.0 - 185.157.187.255', 'status': None, 'remarks': None, 'notices': [{'title': 'Filtered', 'description': 'This output has been filtered.', 'links': None}, {'title': 'Source', 'description': 'Objects returned came from source\nRIPE', 'links': None}, {'title': 'Terms and Conditions', 'description': 'This is the RIPE Database query service. The objects are in RDAP format.', 'links': ['http://www.ripe.net/db/support/db-terms-conditions.pdf']}], 'links': ['https://rdap.db.ripe.net/ip/185.157.185.248', 'http://www.ripe.net/data-tools/support/documentation/terms'], 'events': [{'action': 'last changed', 'timestamp': '2017-01-22T09:53:23Z', 'actor': None}], 'raw': None, 'start_address': '185.157.184.0', 'end_address': '185.157.187.255', 'cidr': '185.157.184.0/22', 'ip_version': 'v4', 'type': 'ALLOCATED PA', 'name': 'ES-MEGANETPLUS-20160629', 'country': 'ES', 'parent_handle': 'EU-ZZ-185'}, 'entities': ['AR36599-RIPE'], 'objects': {'AR36599-RIPE': {'handle': 'AR36599-RIPE', 'status': None, 'remarks': None, 'notices': None, 'links': None, 'events': None, 'raw': None, 'roles': ['abuse'], 'contact': {'name': 'Abuse-C Role', 'kind': 'group', 'address': [{'type': None, 'value': 'Calle Presidente de la Generalitat local numero 5\n03170\nRojales\nSPAIN'}], 'phone': None, 'email': [{'type': None, 'value': 'abuse@meganetplus.com'}], 'role': None, 'title': None}, 'events_actor': None, 'entities': ['es-meganetplus-1-mnt']}}, 'raw': None}}, 'query': '185.157.185.248'}})
    ])
    def test_success(self, circuits_app, apility_lookup_type, apility_lookup_value, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "apility_lookup_type": apility_lookup_type,
            "apility_lookup_value": apility_lookup_value
        }
        results = call_fn_apility_function(circuits_app, function_params)
        assert(expected_results == results)