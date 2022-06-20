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
FINDINGS_BASE_URL = "/security/command-center/findings"
ORG_NAME_FRAGMENT = "organizations"
SOAR_MARKS_PATH="IBM_SOAR_ID"

class GoogleSCCCommon():

    def __init__(self, options):

        validate_fields([
            "google_application_credentials_path", 
            "google_cloud_organization_id",
            "google_cloud_base_url"
        ], options)

        self.console_base_url = options.get("google_cloud_base_url")

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
        Get findings given request parameters. See the SCC Client docs for more details on the parameters and their types.

        https://cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.types.ListFindingsRequest

        Returned type is a list of finding results converted to dictionaries for ease of use:
        [
            {"finding": {...}, "resource": {...}, "state_change": "<some_val>"},
            {"finding": {...}, "resource": {...}, "state_change": "<some_val>"},
            ...
        ]

        :param findings_filter: (Optional) Filter for findings to be found. When used with query_entities_since_ts, this filter is set to query all eventTime values greater than the last poll timestamp
        :type findings_filter: str
        :param findings_read_time: (Optional) Time used as a reference point when filtering findings. SCC allows for filtering findings at any point in time
        :type findings_read_time:  google.protobuf.timestamp_pb2.Timestamp 
        :param compare_duration: (Optional) Updates the returned objects "state_change" value to indicate if the object changed during the given duration
        :type compare_duration: google.protobuf.duration_pb2.Duration 
        :param order_by: (Optional) Expression that defines what fields and order to use for sorting
        :type order_by: str
        :param field_mask: (Optional) A field mask to specify the Finding fields to be listed in the response. An empty field mask will list all fields
        :type field_mask: google.protobuf.field_mask_pb2.FieldMask 
        :return: list of finding results. see above for format
        :rtype: list[dict]
        """

        # if no filter was given but a default filter is defined in the
        # config, take that filter for all findings requests
        if not findings_filter and self.default_findings_filter:
            findings_filter = self.default_findings_filter

        # The "sources/-" suffix lists findings across all sources.
        all_sources = f"{self.org_name}/sources/-"

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

    def add_security_mark(self, finding, soar_case_id):
        """
        Add security marks to a finding.

        :param finding: The finding response object's finding dict
        :type finding: dict
        :param soar_case_id: The case id to be associated in the added mark
        :type soar_case_id: str|int
        :return: updated marks and the marks that were given to SCC
        """
        soar_case_id = str(soar_case_id)

        name = f"{finding.get('name')}/securityMarks"

        field_mask = FieldMask(paths=[f"marks.{SOAR_MARKS_PATH}"])
        marks = {SOAR_MARKS_PATH: soar_case_id}

        marks_request = {
            "security_marks": {"name": name, "marks": marks},
            "update_mask": field_mask
        }

        updated_marks = self.client.update_security_marks(request=marks_request)

        return updated_marks, marks

    def make_linkback_url(self, finding):
        """
        Create a link back to the finding as that is not readily available from the API

        :param finding: The finding response object's finding dict
        :type finding: dict
        :return: the link to the finding
        :rtype: str
        """
        name = finding.get("name")

        query = urlencode(query={ "organizationId": self.org_id, "resourceId": name })
        return f"{self.console_base_url}{FINDINGS_BASE_URL}?{query}"

    def create_initial_note(self, finding):
        """
        Build the note for initial findings being polled in. Any links in the text are converted
        to HTML anchors for easy rich text rendering.

        :param finding: The finding response object's finding dict
        :type finding: dict
        :return: the note with description \n\n and recommendation
        :rtype: str
        """
        description =  finding.get("description")
        recommendation = self.get_finding_source_property(finding, 'Recommendation')

        return linkify(description) + "<br><br>" + linkify(recommendation)

    @staticmethod
    def get_finding_id(finding, entity_id):
        """
        Given a finding, get the finding ID by parsing the name and getting the ID from the end
        """
        name = finding.get("name")

        parsed_path = securitycenter.SecurityCenterClient.parse_finding_path(name)
        return parsed_path.get(entity_id)

    @staticmethod
    def is_finding_closed(finding, finding_close_field):
        """
        Given a finding, is it's state "INACTIVE"?
        """
        current_state = finding.get(finding_close_field)
        return current_state == securitycenter.Finding.State.INACTIVE.name

    @staticmethod
    def get_finding_source_property(finding, source_prop):
        """
        Helper method to get source properties which is a nested dict
        within a finding dict that has values that can change.
        Gives a default "not found" message if the property is not present
        """
        not_found_msg = f"'{source_prop}' not found for finding {finding.get('canonical_name')}"

        return finding.get("source_properties", {}).get(source_prop, not_found_msg)


def linkify(s, link_text=None):
    """
    Identify any links and replace them with HTML anchor tags.
    Optional "link_text" parameter to replace the displayed text of the link.
    If ommited, the link itself it given as the text.
    """
    if s:
        # Replace url to link
        urls = re.compile(r"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)(?<![.,?!-])", re.MULTILINE|re.UNICODE)

        if not link_text:
            value = urls.sub(r'<a href="\1" target="_blank">\1</a>', s)
        else:
            value = urls.sub(r'<a href="\1" target="_blank">{0}</a>', s).format(link_text)

        return value
