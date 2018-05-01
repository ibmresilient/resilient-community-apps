# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from fn_cisco_enforcement.components.event import *
from fn_cisco_enforcement.lib.resilient_common import *
from mock import patch
import logging


# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

class TestEvent:
    """ Tests for the event function"""

    @pytest.mark.parametrize(
        " cisco_dstip, cisco_eventseverity, cisco_eventtype,cisco_eventdescription, cisco_eventhash, cisco_filename, cisco_filehash, cisco_externalurl, cisco_src, expected",
        [
            ("True", "grand", "smallgettogether", "A gathering of like minded individuals to discuss our general interests", "index.html", "0EB547304658805AAD788D320F10BF1F292797B5E6D745A3BF617584DA017051", "www.blahbla.com", "this test", "text","text")
        ])
    @patch.object(FunctionComponent, "__init__",return_value= None)
    # Testing the non mandatory fields are added to data object correctly
    def test_addothers(self,circuits_app,cisco_dstip, cisco_eventseverity, cisco_eventtype,cisco_eventdescription, cisco_eventhash, cisco_filename, cisco_filehash, cisco_externalurl, cisco_src,expected):
        fn=FunctionComponent(None)
        data={"cisco_dstip":""}
        expected={'cisco_dstip': 'True', 'cisco_eventseverity': 'grand', 'cisco_eventtype': 'smallgettogether', 'cisco_filehash': 'www.blahbla.com', 'cisco_filename': '0EB547304658805AAD788D320F10BF1F292797B5E6D745A3BF617584DA017051', 'cisco_externalurl': 'this test', 'cisco_eventdescription': 'A gathering of like minded individuals to discuss our general interests', 'cisco_eventhash': 'index.html', 'cisco_src': 'text'}
        results=fn.addothers(data,cisco_dstip, cisco_eventseverity, cisco_eventtype,cisco_eventdescription, cisco_eventhash, cisco_filename, cisco_filehash, cisco_externalurl, cisco_src)
        assert (expected==results)

    # Test created data object
    @pytest.mark.parametrize("cisco_deviceid,cisco_deviceversion,cisco_eventtime,cisco_alerttime,cisco_eventdescription,cisco_dsturl,cisco_dstdomain,expected",[("12","1",1518367008000,1518367008000,"test description","www.myurl.com/tt","/tt",{'eventTime': '2018-02-11T16:36:48Z', 'alertTime': '2018-02-11T16:36:48Z', 'deviceId': '12', 'providerName': 1, 'protocolVersion': 1, 'cisco_eventdescription': 'test description', 'dstDomain': '/tt', 'dstUrl': '/tt', 'deviceVersion': '1'})])
    @patch.object(FunctionComponent, "__init__", return_value=None)
    def test_createdataobject(self,circuits_app,cisco_deviceid,cisco_deviceversion,cisco_eventtime,cisco_alerttime,cisco_eventdescription,cisco_dsturl,cisco_dstdomain,expected):
        args={"cisco_deviceid":cisco_deviceid,"cisco_deviceversion":cisco_deviceversion,"cisco_eventtime":cisco_eventtime,"cisco_alerttime":cisco_alerttime,"cisco_eventdescription":cisco_eventdescription,"cisco_dsturl":cisco_dsturl,"cisco_dstdomain":cisco_dstdomain}
        fn = FunctionComponent(None)

        # Default values from app config, just need to be set for this test
        fn.options={"protocol_version":1,"provider_name":1}
        log = logging.getLogger(__name__)
        fn.log=log
        results = fn.createdataobject(args)
        assert (expected == results)

    @pytest.mark.parametrize("fields,expected",
                             [(["protocol_version"],{"protocol_version": "1"}),(['provider_name'],{"provider_name":"me"})])
    # Test fields are correctly validated
    def test_validatefields_correct(self,fields,expected):
        results=validateFields(fields,expected)
        assert(results==None)

    @pytest.mark.parametrize("fields,expected",
                             [(["protocol_versio2n"], 'Required field is missing or empty: protocol_versio2n'),
                              (['provider_1name'], 'Required field is missing or empty: provider_1name')])
    # Test fields are correctly validated
    def test_validatefields_incorrect(self, fields, expected):

        with pytest.raises(ValueError) as e:
                validateFields(fields, '')
                assert (e.value.message == expected)

    @pytest.mark.parametrize("time,expected",[(1525075238,'2018-04-30T08:00:38Z'),(1518367008,'2018-02-11T16:36:48Z')])
    # Test for correct time format
    def test_readabledatetime_seconds(self,time,expected):
        results = readableDateTime(time, False)
        assert (results == expected)

    @pytest.mark.parametrize("time,expected",
                             [(1525075238, '2018-04-30T08:00:39Z'), (1518367008, '2018-02-11T16:36:49Z')])
    # Test for incorrect time format
    def test_readabledatetime_miliseconds(self,time,expected):
        results = readableDateTime(1525075238, True)
        assert (results != expected)








