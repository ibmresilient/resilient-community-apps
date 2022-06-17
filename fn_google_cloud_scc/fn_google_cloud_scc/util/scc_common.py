# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import re
from urllib.parse import urlencode

from google.cloud import securitycenter
from google.protobuf.field_mask_pb2 import FieldMask
from resilient_lib import readable_datetime, validate_fields

# alias the ListFindingsResponse.ListFindingsResult to FindingResult
FindingResult = securitycenter.ListFindingsResponse.ListFindingsResult

PACKAGE_NAME = "fn_google_cloud_scc"
CLOUD_CONSOLE_BASE_URL = "https://console.cloud.google.com/security/command-center/findings"
ORG_NAME_FRAGMENT = "organizations"
SOAR_MARKS_PATH="IBM_SOAR_ID"

class GoogleSCCCommon():

    def __init__(self, options):

        validate_fields([
            "google_application_credentials_path", 
            "google_cloud_organization_id"
        ], options)

        cred_file = options.get("google_application_credentials_path")
        self.client = securitycenter.SecurityCenterClient.from_service_account_file(cred_file)

        self.org_id = options.get("google_cloud_organization_id")
        self.default_findings_filter = options.get("findings_filter") # ok if None

        self.org_name = f"{ORG_NAME_FRAGMENT}/{self.org_id}"


    def query_entities_since_ts(self, timestamp, *args, **kwargs):
        """get changed entities since last poller run

        Args:
            timestamp (datetime): datetime when the last poller ran
            *args: additional positional parameters needed for endpoint queries
            **kwargs: additional key/value paris needed for endpoint queries

        Returns:
            list: changed entity list
        """

        findings_filter = f"eventTime >= \"{readable_datetime(timestamp)}\""
        if self.default_findings_filter:
            findings_filter = f"{findings_filter} AND ({self.default_findings_filter})"

        return self.get_findings(
            findings_filter=findings_filter
        )


    def get_findings(self, findings_filter=None, findings_read_time=None, compare_duration=None, order_by=None, field_mask=None):
        """
        TODO
        https://cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types
        """

        # if no filter was given but a default filter is defined in the
        # config, take that filter for all findings requests
        if not findings_filter and self.default_findings_filter:
            findings_filter = self.default_findings_filter

        # The "sources/-" suffix lists findings across all sources.  You
        # also use a specific source_name instead.
        # TODO: is this always what we want? Maybe not — CHECK!!
        all_sources = f"{self.org_name}/sources/-"

        # https://cloud.google.com/security-command-center/docs/how-to-api-list-findings#filtering_findings

        findings_request = {
            "parent": all_sources, 
            "filter": findings_filter, 
            "read_time": findings_read_time,
            "compare_duration": compare_duration,
            "order_by": order_by,
            "field_mask": field_mask
        }

        finding_result_iterator = self.client.list_findings(request=findings_request)


        # convert to dict so that the objs are formatted to the fomat below and 
        # enums are converted to their string representation
        # [
        #   {"finding": {...}, "resource": {...}, "state_change": "<some_val>"},
        #   {"finding": {...}, "resource": {...}, "state_change": "<some_val>"},
        #   ...
        # ]
        finding_results = [FindingResult.to_dict(finding, use_integers_for_enums=False) for finding in finding_result_iterator]

        for finding_result in finding_results:
            finding = finding_result.get("finding", {})

            # add resources from result obj to finding obj
            finding_result["finding"]["resource"] = finding_result.get("resource")

            # create linkback
            finding_result["finding"]["finding_url"] = self.make_linkback_url(finding)

            # create a second description that is linkified
            finding_result["finding"]["linkified_description"] = linkify(finding.get("description"))

            # add recommendation
            finding_result["finding"]["recommendation"] = self.get_finding_source_property(finding, "Recommendation")
            finding_result["finding"]["linkified_recommendation"] = linkify(finding.get("recommendation"))

            # some properties aren't always there but we want to have something so that the templates don't fail
            finding_result["finding"]["indicator"] = finding.get("indicator", {"ip_addresses": [], "domains": []})
            finding_result["finding"]["vulnerability"] = finding.get("vulnerability", {"cve": None})

        return finding_results

    def add_security_mark(self, finding, msg):
        """
        TODO
        """
        msg = str(msg)

        name = f"{finding.get('name')}/securityMarks"

        field_mask = FieldMask(paths=[f"marks.{SOAR_MARKS_PATH}"])
        marks = {SOAR_MARKS_PATH: msg}

        marks_request = {
            "security_marks": {"name": name, "marks": marks},
            "update_mask": field_mask
        }

        updated_marks = self.client.update_security_marks(request=marks_request)

        return updated_marks, marks

    def make_linkback_url(self, finding):
        """
        TODO
        """
        name = finding.get("name")

        query = urlencode(query={ "organizationId": self.org_id, "resourceId": name })
        return f"{CLOUD_CONSOLE_BASE_URL}?{query}"

    def create_initial_note(self, finding):
        """
        TODO
        """
        description =  finding.get("description")
        recommendation = self.get_finding_source_property(finding, 'Recommendation')

        return linkify(description) + "<br><br>" + linkify(recommendation)

    @staticmethod
    def get_finding_id(finding, entity_id):
        """
        TODO
        """
        name = finding.get("name")

        parsed_path = securitycenter.SecurityCenterClient.parse_finding_path(name)
        return parsed_path.get(entity_id)

    @staticmethod
    def is_finding_closed(finding, finding_close_field):
        """
        TODO
        """
        current_state = finding.get(finding_close_field)
        return current_state == securitycenter.Finding.State.INACTIVE.name

    @staticmethod
    def get_finding_source_property(finding, source_prop):
        """
        TODO
        """
        not_found_msg = f"'{source_prop}' not found for finding {finding.get('canonical_name')}"

        return finding.get("source_properties", {}).get(source_prop, not_found_msg)


def linkify(s, link_text=None):
    if s:
        # Replace url to link
        urls = re.compile(r"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)(?<![.,?!-])", re.MULTILINE|re.UNICODE)

        if not link_text:
            value = urls.sub(r'<a href="\1" target="_blank">\1</a>', s)
        else:
            value = urls.sub(r'<a href="\1" target="_blank">{0}</a>', s).format(link_text)

        return value
