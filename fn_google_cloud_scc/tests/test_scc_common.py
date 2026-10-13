import copy
from datetime import datetime
from unittest.mock import patch

import pytest
from google.cloud import securitycenter
from resilient_lib import RequestsCommon

from fn_google_cloud_scc.lib.scc_common import GoogleSCCCommon, linkify

from .data.mock_objs import (MockSecurityCenterClient, assets, config_data,
                             findings, to_dict)


@pytest.fixture(scope="module")
def fx_scc_common():
    with patch.object(securitycenter.SecurityCenterClient, "from_service_account_file", MockSecurityCenterClient.from_service_account_file) as _:
        return GoogleSCCCommon(config_data, RequestsCommon())


@patch.object(securitycenter.ListFindingsResponse.ListFindingsResult, "to_dict")
@patch.object(securitycenter.SecurityCenterClient, "list_findings")
def test_query_entities_since_ts(mock_list_findings, mock_to_dict, fx_scc_common: GoogleSCCCommon):
    mock_list_findings.side_effect = MockSecurityCenterClient.list_findings
    mock_to_dict.side_effect = to_dict
    app_common = fx_scc_common

    findings_result_list = app_common.query_entities_since_ts(datetime.now().timestamp()*1000)

    assert len(findings_result_list) == 1
    assert "finding_url" in findings_result_list[0].get("finding")
    assert "linkified_recommendation" in findings_result_list[0].get("finding")

def test_enrich_finding(fx_scc_common: GoogleSCCCommon):
    app_common = fx_scc_common

    assert "finding_url" not in findings[0].get("finding")

    # have to make a deep copy to allow for parallel processing here
    finding = copy.deepcopy(findings[0].get("finding"))

    finding = app_common.enrich_finding(finding)

    assert "finding_url" in finding

def test_make_finding_linkback_url(fx_scc_common: GoogleSCCCommon):
    app_common = fx_scc_common

    link = app_common.make_finding_linkback_url(findings[0].get("finding"))
    
    assert link == "https://console.cloud.google.com/security/command-center/findings?organizationId=123456789&resourceId=organizations%2F%3Corg_id%3E%2Fsources%2F%3Csource_id%3E%2Ffindings%2F%3Cfinding_id%3E"

def test_make_asset_linkback_url(fx_scc_common: GoogleSCCCommon):
    app_common = fx_scc_common

    link = app_common.make_asset_linkback_url(assets[0].get("asset"))
    
    assert link == "https://console.cloud.google.com/security/command-center/assets?organizationId=123456789&resourceId=organizations%2F259357470209%2Fassets%2F11712294571846742175"

def test_create_initial_note(fx_scc_common: GoogleSCCCommon):
    app_common = fx_scc_common

    note = app_common.create_initial_note(findings[0].get("finding"))
    assert note == 'description<br><br>recommendation. follow link: <a href="https://example.com/dot_at_end_not_included" target="_blank">https://example.com/dot_at_end_not_included</a>.<br><br>See more details in the Google SCC tab of this incident.'

def test_get_finding_id():
    f_id = GoogleSCCCommon.get_finding_id(findings[0].get("finding"), "finding")

    assert f_id == "<finding_id>"

def test_is_finding_close():
    assert GoogleSCCCommon.is_finding_closed(findings[0].get("finding"), "state")
    assert not GoogleSCCCommon.is_finding_closed({"state": "ACTIVE"}, "state")

def test_get_finding_source_property():
    assert GoogleSCCCommon.get_finding_source_property(findings[0].get("finding"), "ScannerName") == "CONTAINER_SCANNER"
    assert GoogleSCCCommon.get_finding_source_property(findings[0].get("finding"), "Explanation") == "explanation"

def test_linkify():
    assert linkify("some text and a http://link.com with more text") == 'some text and a <a href="http://link.com" target="_blank">http://link.com</a> with more text'
    assert linkify("https://test.com", "Link NAME") == '<a href="https://test.com" target="_blank">Link NAME</a>'
    assert linkify("text") == "text"
    assert linkify("https://test.com", "") == '<a href="https://test.com" target="_blank">https://test.com</a>'
    assert linkify("BIG text here then a https://example.com.", "LINK") == 'BIG text here then a <a href="https://example.com" target="_blank">LINK</a>.'

