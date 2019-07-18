# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
"""Test helper functions"""
import pytest
from fn_sep.lib.helpers import *
from mock_artifacts import mocked_res_client, get_computers, get_command_status_processed
import time
from datetime import datetime
"""
Suites of tests to test the Symantec SEP Helper functions
"""

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def convert_value_to_none(v):
    # Convert "None" string value to None value.
    if type(v) == str and v.lower() == 'none':
        v = None
    return v

def add_readable_timestamps(rtn):
    now = time.time()
    for i in range(len(rtn["content"])):
        for f in ["lastScanTime", "lastUpdateTime", "lastVirusTime"]:
            try:
                secs = int(rtn["content"][i][f]) / 1000
                timediff = now - secs
                ts_readable = datetime.fromtimestamp(secs).strftime('%Y-%m-%d %H:%M:%S')
                # New keys will be "readableLastScanTime", "readableLastUpdateTime", "readableLastVirusTime"
                rtn["content"][i]["readable" + f[0].capitalize() + f[1:]] = ts_readable
                rtn["content"][i]["timediff" + f[0].capitalize() + f[1:]] = timediff
            except ValueError:
                raise ValueError("A timestamp value was incorrectly specified")
    return rtn

class TestSepHelpersTransformKwargs:
    """Test transform_kwargs function"""

    @pytest.mark.parametrize("sep_hardwarekey, sep_groupid", [
        ("DC7D24D6465566D2941F35BC8D17801E","8E20F39B0946C25D118925C2E28C2D59"),
        (None, None),
        ('none', 'None')
    ])
    def test_transform_kwargs(self, sep_hardwarekey, sep_groupid):
        new_kwargs = {
            "hardwarekey": convert_value_to_none(sep_hardwarekey),
            "groupid": convert_value_to_none(sep_groupid)
        }
        kwargs = {
            "sep_hardwarekey": sep_hardwarekey,
            "sep_groupid": sep_groupid
        }
        params = transform_kwargs(kwargs)
        for key in new_kwargs:
            assert (key in params)

class TestSepHelpersGetEndpointsStatus:
    """Test get_endpoints_status function"""

    @pytest.mark.parametrize("rtn, expected_results", [
        (add_readable_timestamps(get_computers("non-compliant")), [1, 2, 2, 1, 2, 2, 0])
    ])
    def test_get_endpoints_status(self, rtn, expected_results):

        keys = ["disabled", "hi_failed", "non_compliant", "offline", "out_of_date", "total", "up_to_date"]

        response = get_endpoints_status(rtn)
        assert_keys_in(response, *keys)
        for i in range(len(keys)):
            assert expected_results[i] == response[keys[i]]

class TestSepHelpersGetEndpointsStatusDetails:
    """Test get_endpoints_status_details function"""

    @pytest.mark.parametrize("rtn, expected_results", [
        (add_readable_timestamps(get_computers("non-compliant")), [1, None, 2, 2, 1, 2, 2, 0])
    ])
    def test_get_endpoints_status_details(self, rtn, expected_results):

        keys = ["disabled", "eps", "hi_failed", "non_compliant", "offline", "out_of_date", "total", "up_to_date"]
        keys_2 = ["readableLastScanTime", "daOnOff", "elamOnOff", "readableLastVirusTime", "avEngineOnOff",
                  "pepOnOff", "tamperOnOff", "onlineStatus", "cidsBrowserIeOnOff", "readableLastUpdateTime", "apOnOff",
                  "computer_name", "firewallOnOff", "cidsDrvOnOff", "host_integrity_check", "ptpOnOff", "cidsBrowserFfOnOff"]
        response = get_endpoints_status_details(rtn)
        assert_keys_in(response, *keys)
        for i in range(len(keys)):
            if keys[i] !=  "eps":
                assert expected_results[i] == response[keys[i]]
        eps = response["eps"]
        for j in range(len(eps)):
            assert_keys_in(eps[j], *keys_2)



class TestHelpersCreateAttachment:
    """ Tests for the create_attachment function"""

    @pytest.mark.parametrize("file_name, file_content, params", [
        ("test_file.xml", 'My test data', {"incident_id": 12345})
    ])
    def test_create_attachment(self, file_name, file_content, params):
        """ Test create_attachment using mocked data.  """
        keys = ["name", "inc_id"]

        results = create_attachment(mocked_res_client("post_attachment", file_name, params["incident_id"]), file_name, file_content, params)
        assert_keys_in(results, *keys)
        assert results["name"] == file_name
        assert results["inc_id"] == params["incident_id"]

class TestHelpersGenerateResultCvs:
    """ Tests for the generate_result_cvs function"""

    @pytest.mark.parametrize("rtn, sep_commandid, expected_results", [
        (get_command_status_processed(), "3FEB081B2A144479A32980272C9C1E23",
         ["3FEB081B2A144479A32980272C9C1E23", ",C:\\temp\\My_file_1.txt,", ",SHA256,b82758fc5f737a58078d3c60e2798a70d895443a86aa39adf52dec70e98c2bed"])
    ])
    def test_generate_result_cvs(self, rtn, sep_commandid, expected_results):
        """ Test  generate_result_cvs using mocked data.  """
        content_values = expected_results[1:]
        result_time = datetime.today().strftime('%Y%m%d%H%M%S')
        (file_name, file_content) = generate_result_csv(rtn, sep_commandid)
        assert "EOC_scan_results_for_commandid_"+expected_results[0]+"_"+result_time+".csv" == file_name
        for c in file_content.split('\n'):
            assert_keys_in(file_content, *content_values)
