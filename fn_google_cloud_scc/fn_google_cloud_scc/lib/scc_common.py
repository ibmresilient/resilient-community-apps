# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import logging
import os
import re
from datetime import datetime, timezone
from urllib.parse import urlencode

from google.api_core.exceptions import InvalidArgument
from google.cloud.securitycenter import (Finding, ListAssetsResponse,
                                         ListFindingsResponse,
                                         SecurityCenterClient, SecurityMarks)
from google.protobuf.field_mask_pb2 import FieldMask
from resilient_lib import IntegrationError, readable_datetime, validate_fields

# alias the ListFindingsResponse.ListFindingsResult to FindingResult
# and same for assets
FindingResult = ListFindingsResponse.ListFindingsResult
AssetResult = ListAssetsResponse.ListAssetsResult

PACKAGE_NAME = "fn_google_cloud_scc"
ASSETS_BASE_URL = "/security/command-center/assets"
FINDINGS_BASE_URL = "/security/command-center/findings"
ORG_NAME_FRAGMENT = "organizations"
SOAR_ID_MARK = "IBM_SOAR_ID"
DT_NAME = "google_scc_finding_source_properties_dt"

ENV_HTTP_PROXY = "HTTP_PROXY"
ENV_HTTPS_PROXY = "HTTPS_PROXY"
ENV_GRPC_HTTP_PROXY = "http_proxy"
ENV_GRPC_HTTPS_PROXY = "https_proxy"

LOG = logging.getLogger(__name__)

class GoogleSCCCommon():

    def __init__(self, options, rc):

        validate_fields([
            "google_application_credentials_path",
            "google_cloud_organization_id",
            "google_cloud_base_url"
        ], options)

        self.console_base_url = options.get("google_cloud_base_url")

        self._set_proxies(rc)

        cred_file = options.get("google_application_credentials_path")
        self.client = SecurityCenterClient.from_service_account_file(cred_file)

        self.org_id = options.get("google_cloud_organization_id")
        self.default_findings_filter = options.get("findings_filter") # ok if None

        self.org_name = f"{ORG_NAME_FRAGMENT}/{self.org_id}"

    def _set_proxies(self, rc):
        """
        Set the appropriate proxy env variables required for
        Google SCC connections. This is slightly different from
        our normal proxies as this requires a Grpc connection
        which uses a *lower-case* version of the proxy vars
        that isn't set automatically in our standard framework.

        So we have to check if the proxies are set in the settings
        or already in the ENV and then use that value to set
        the appropriate associated lower-case versions.

        :param rc: RequestsCommon object to find app.config proxy settings if present
        :type rc: resilient_lib.RequestsCommon
        """

        rc_proxies = rc.get_proxies() # NOTE: this returns None if the requests proxies are set in the ENV
        if rc_proxies: # check if proxies are set through app settings
            # don't overwrite the proxies if they're already set
            if not os.getenv(ENV_GRPC_HTTP_PROXY):
                os.environ[ENV_GRPC_HTTP_PROXY] = rc_proxies.get("http")
            if not os.getenv(ENV_GRPC_HTTPS_PROXY):
                os.environ[ENV_GRPC_HTTPS_PROXY] = rc_proxies.get("https")
        # if they were set through env variables,
        # then also set them for the required GRPC variables (lowercase version)
        else:
            # Don't overwrite the proxies if they're already set
            if os.getenv(ENV_HTTP_PROXY) and not os.getenv(ENV_GRPC_HTTP_PROXY):
                os.environ[ENV_GRPC_HTTP_PROXY] = os.getenv(ENV_HTTP_PROXY)
            if os.getenv(ENV_HTTPS_PROXY) and not os.getenv(ENV_GRPC_HTTPS_PROXY):
                os.environ[ENV_GRPC_HTTPS_PROXY] = os.getenv(ENV_HTTPS_PROXY)


    def query_entities_since_ts(self, timestamp, *_args, **_kwargs):
        """
        Get changed entities since last poller run

        :param timestamp: datetime when the last poller ran
        :type timestamp: datetime
        :param *_args: additional positional parameters needed for endpoint queries
        :type _args: dict
        :param **_kwargs: additional key/value paris needed for endpoint queries
        :type _kwargs: dict

        :return: changed entity list
        :rtype: list
        """

        findings_filter = f"eventTime >= \"{readable_datetime(timestamp)}\""
        if self.default_findings_filter:
            findings_filter = f"{findings_filter} AND ({self.default_findings_filter})"

        return self.get_findings(
            findings_filter=findings_filter
        )


    def get_findings(self, findings_filter=None, findings_read_time=None, compare_duration=None, order_by=None, fields_to_return=None, return_findings_result_list=False):
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
        :param fields_to_return: (Optional) A field mask listed as a comma-separated string of fields to be returned
        :type fields_to_return: str
        :return: list of finding results. see above for format
        :rtype: list[dict]
        """

        # if no filter was given but a default filter is defined in the
        # config, take that filter for all findings requests
        if not findings_filter and self.default_findings_filter:
            LOG.info("Using default list findings filter from app.config.")
            findings_filter = self.default_findings_filter

        # The "sources/-" suffix lists findings across all sources.
        all_sources = f"{self.org_name}/sources/-"

        findings_request = {
            "parent": all_sources, 
            "filter": findings_filter, 
            "read_time": findings_read_time,
            "compare_duration": compare_duration,
            "order_by": order_by,
            "field_mask": FieldMask(paths=[field.strip() for field in fields_to_return.split(",")]) if fields_to_return else None
        }

        finding_result_iterator = self.client.list_findings(request=findings_request)

        if return_findings_result_list:
            return [finding for finding in finding_result_iterator]

        # convert to dict so that the objs are formatted to the fomat below and 
        # enums are converted to their string representation
        # [
        #   {"finding": {...}, "resource": {...}, "state_change": "<some_val>"},
        #   {"finding": {...}, "resource": {...}, "state_change": "<some_val>"},
        #   ...
        # ]

        finding_results = []

        for finding_result in finding_result_iterator:
            finding_result = FindingResult.to_dict(finding_result, use_integers_for_enums=False)

            # add resources from result obj to finding obj
            finding_result["finding"]["resource"] = finding_result.get("resource")

            finding_result["finding"] = self.enrich_finding(finding_result["finding"])

            finding_results.append(finding_result)

        return finding_results

    def enrich_finding(self, finding_dict):
        """
        Adds some custom fields and cleans some fields of the finding
        to make it easier to parse for jinja templates and postprocessing

        Adds the following fields to the dictionary:
            ["finding_url", "linkified_description", "recommendation", 
            "linkified_recommendation", "indicator", "vulnerability"]

        NOTE: indicator and vulnerability may already exist - if they do, they remain unchanged.
        if they don't, default empty values are added for easy parsing in jinja template.
        the default empty values match the format that would be there if they existed
        as of ``google-cloud-securitycenter`` v1.11.1

        :param finding_dict: the result of converting a finding to a dictionary with the google API
        :type finding_dict: dict
        :return: modified dict with new fields
        """

        # create linkback
        finding_dict["finding_url"] = self.make_finding_linkback_url(finding_dict)

        # create a second description that is linkified
        finding_dict["linkified_description"] = linkify(finding_dict.get("description"))

        # add recommendation and href version
        finding_dict["recommendation"] = self.get_finding_source_property(finding_dict, "Recommendation")
        finding_dict["linkified_recommendation"] = linkify(finding_dict.get("recommendation"))

        # some properties aren't always there but we want to have something so that the templates don't fail
        finding_dict["indicator"] = finding_dict.get("indicator", {"ip_addresses": [], "domains": []})
        finding_dict["vulnerability"] = finding_dict.get("vulnerability", {"cve": None})

        return finding_dict

    def update_security_mark(self, finding_name, mark_key, mark_value=None):
        """
        Add/change/delete security marks on a finding.

        mark_value can be None, in which case the mark_key will be deleted

        :param finding_name: The finding's name
        :type finding_name: str
        :param mark_key: The key of the security mark to be added
        :type mark_key: str
        :param mark_value: The value associated with the given key to be added
        :type mark_value: str|int|None
        :return: updated marks and the marks that were given to SCC
        :rtype: tuple(dict, dict)
        """

        name = f"{finding_name}/securityMarks"

        field_mask = FieldMask(paths=[f"marks.{mark_key}"])
        marks = {mark_key: str(mark_value)}

        marks_request = {
            # if you want to delete, then just pass {"name": name}
            "security_marks": {"name": name, "marks": marks} if mark_value else {"name": name},
            "update_mask": field_mask
        }

        updated_marks = self.client.update_security_marks(request=marks_request)

        return SecurityMarks.to_dict(updated_marks), marks

    def update_finding(self, finding_with_updates: Finding, fields_to_update: list):
        """
        Use the Google API to update a finding.
        Requires that a Finding object is given, with the name of the finding
        that is to be changed and the other fields that should be modified set
        to their modified values.
        A field mask will be created off of the list of fields_to_update so that
        only those fields are modified in the call — be careful in what you pass
        to that list as it must match the fields that are modified in the given finding
        and also should not have any extraneous fields to avoid unintended updates.

        :param finding_with_updates: the finding object with original name and desired fields updated
        :type finding_with_updates: ``google.cloud.securitycenter.Finding``
        :param fields_to_updated: list of fields that are to be updated
        :type fields_to_update: list
        :return: finding object representing the finding's updated state
        :rtype: ``google.cloud.securitycenter.Finding``
        """
        event_time = datetime.now(tz=timezone.utc)
        finding_with_updates.event_time = event_time
        fields_to_update.append("event_time")

        update_mask = FieldMask(
            paths=fields_to_update
        )

        update_request = {
            "finding": finding_with_updates,
            "update_mask": update_mask
        }

        return self.client.update_finding(request=update_request)


    def list_assets(self, filter=None, fields_to_return=None, read_time=None, compare_duration=None, order_by=None):
        """
        List the assests of the organization under monitoring by SCC.
        The filter and ``fields_to_return`` are important parts of this
        method.

        This method assumes the ``fields_to_return`` field is given in the format
        that would come from the SOAR pre-processing script, i.e. a string
        of comma-separated values that indicate the values to return.
        Google's API is quite picky about the format of these so here are a
        few examples of acceptable ``fields_to_return`` formats:

        Example:

        .. code-block::python

            fields_to_return = "asset.resource_properties, asset.security_center_properties"

        :param filter: (Optional) Filter for assets to be found., defaults to None
        :type filter: str, optional
        :param read_time: (Optional) Time used as a reference point when filtering findings. SCC allows for filtering findings at any point in time, defaults to None
        :type read_time: google.protobuf.timestamp_pb2.Timestamp, optional
        :param compare_duration: (Optional) Updates the returned objects "state_change" value to indicate if the object changed during the given duration, defaults to None
        :type compare_duration: google.protobuf.duration_pb2.Duration, optional
        :param order_by: (Optional) Expression that defines what fields and order to use for sorting, defaults to None
        :type order_by: str, optional
        :param fields_to_return: (Optional) A field mask listed as a comma-separated string of fields to be returned, defaults to None
        :type fields_to_return: str, optional
        :return: list of assets results
        :rtype: list[dict]
        """

        assets_request = {
            "parent": self.org_name,
            "filter": filter,
            "read_time": read_time,
            "compare_duration": compare_duration,
            "order_by": order_by,
            "field_mask": FieldMask(paths=[field.strip() for field in fields_to_return.split(",")]) if fields_to_return else None
        }

        try:
            # list the assets
            asset_iterator = self.client.list_assets(request=assets_request)
        except InvalidArgument as e:
            # it is probably pretty common that the user might input
            # the field mask or filter wrong as it is hard to get right...
            # if that is the case, try to given them as good a message
            # as possible to remedy the field_mask issue
            if hasattr(e, "message") and "invalid field_mask" in e.message.lower():
                msg = "Invalid Field Mask: {0}. Field Mask should be given like: 'asset.resource_properties,...'".format(fields_to_return)
                raise IntegrationError(msg)
            elif hasattr(e, "message") and "invalid filter" in e.message.lower():
                msg = "Invalid Filter: {0}. Filter should be given like: 'securityMarks.marks.test=\"1\"'".format(filter)
                raise IntegrationError(msg)
            else:
                raise e

        assets_results = []

        for asset_result in asset_iterator:
            asset_result = AssetResult.to_dict(asset_result, use_integers_for_enums=False)
            asset_result["asset"]["link"] = self.make_asset_linkback_url(asset_result["asset"])
            assets_results.append(asset_result)

        return assets_results

    def format_assets(self, assets):
        """
        Take assets list as given from Google SCC API, and
        format it in a nice, readable way for presentation in
        a note in SOAR.

        This method obscures out the values of the asset that are
        deemed less-useful for nice formatting. The rest of the data
        will still be returned from the function, but will need to
        be manually parsed and displayed in a post-processing script.

        :param assets: dict representation of the asset query result
        :type assets: dict
        :param app_common: SCC app object
        :type app_common: GoogleSCCCommon
        :return: HTML formatted string to neatly represent the assets list result
        :rtype: str
        """

        formatted_assets_list = ""

        for asset in assets:
            # just grab the asset information from the whole asset object
            # i.e. ignore the state_change data
            asset = asset.get("asset", {})

            # list the link as a ref to name
            link = asset.get("link")
            name = asset.get("name")
            formatted_assets_list += f"<a target='_blank' href={link}>{name}</a>\n"

            # parse out the security center props and resource props
            security_center_props = asset.get("security_center_properties", {})
            resource_props = asset.get("resource_properties", {})
            # build the strs associated and append them
            formatted_assets_list += self._format_section(security_center_props, "Security Center Properties")
            formatted_assets_list += self._format_section(resource_props, "Resource Properties")

            # Handle any security marks as span objects for nice formatting
            marks = asset.get("security_marks", {}).get("marks", {})
            # NOTE: no need to compute length here (unlike the others) due to the nature
            # of security marks; there won't be marks if the key's value doesn't exist
            formatted_assets_list += f"\t<b>Security Marks ({len(marks)}){':' if len(marks) else ''}</b>"
            for key in marks:
                value = marks.get(key)
                if value:
                    formatted_assets_list += f" <span class='label' rel='tooltip' title='{key}'>{key} : {value}</span>"
            formatted_assets_list += "\n"

            # append create and update times
            create_time = asset.get("create_time", "")
            update_time = asset.get("update_time", "")
            formatted_assets_list += f"\t<b>Create time</b>: {create_time}\n\t<b>Update time</b>: {update_time}\n"

            # add news lines for next asset
            formatted_assets_list += "\n"

        return formatted_assets_list

    @staticmethod
    def _format_section(section, section_title):
        """
        Small helper method for format_assets to help format the
        security center properties and resource properties
        sections.

        :param section: dict of the section's data
        :type section: dict
        :param section_title: title for the section (i.e. Security Center Properties)
        :type section_title: str
        :return: formatted string with the title in bold and the contents presented neatly
        :rtype: str
        """

        length = 0
        section_str = ""

        for key in section:
            # list out each property
            value = section.get(key)
            if value:
                length += 1
                section_str += f"\t\t<b>{key}</b>: {value}\n"

        return f"\t<b>{section_title} ({length}):</b>\n" + section_str



    def make_finding_linkback_url(self, finding):
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

    def make_asset_linkback_url(self, asset):
        """
        Create a link back to the asset as that is not readily available from the API

        :param asset: The asset response object's asset dict
        :type asset: dict
        :return: the link to the asset
        :rtype: str
        """
        name = asset.get("name")

        query = urlencode(query={ "organizationId": self.org_id, "resourceId": name })
        return f"{self.console_base_url}{ASSETS_BASE_URL}?{query}"

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

        return linkify(description) + "<br><br>" + linkify(recommendation) + "<br><br>" + "See more details in the Google SCC tab of this incident."

    @staticmethod
    def get_finding_id(finding, entity_id):
        """
        Given a finding, get the finding ID by parsing the name and getting the ID from the end
        """
        name = finding.get("name")

        parsed_path = SecurityCenterClient.parse_finding_path(name)
        return parsed_path.get(entity_id)

    @staticmethod
    def is_finding_closed(finding, finding_close_field):
        """
        Given a finding, is it's state "INACTIVE"?
        """
        current_state = finding.get(finding_close_field)
        return current_state == Finding.State.INACTIVE.name

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
