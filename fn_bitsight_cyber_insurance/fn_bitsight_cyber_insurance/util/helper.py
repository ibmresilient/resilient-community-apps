# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.

from resilient_lib import IntegrationError
from re import match
from logging import getLogger

LOG = getLogger(__name__)
PACKAGE_NAME = "fn_bitsight_cyber_insurance"
DATE_PATTERN = r"^\d{4}-\d{2}-\d{2}$"
GUID_PATTERN = r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
DEFAULT_LIMIT = 20
DEFAULT_OFFSET = 0

def clear_datatable(rest_client, incident_id, table_name):
    """Clear data in given table on SOAR

    Args:
        res_rest_client (obj, required): SOAR rest client connection
        table_name (str, required): API access name of the table to clear
        incident_id (int, required): SOAR ID for the incident
    """
    try:
        rest_client.delete(f"/incidents/{incident_id}/table_data/{table_name}/row_data?handle_format=names")
        LOG.info(f"Data in table {table_name} in incident {incident_id} has been cleared")

    except Exception as err_msg:
        LOG.error(f"Failed to clear table: {table_name} error: {err_msg}")

def check_filter_value_format(pattern, filter_value):
    """Test if the given filter value matches the given pattern.

    Args:
        pattern (str): The pattern to match.
        filter_value (str): The filter value.

    Returns:
        bool: True if the filter_value matches the given pattern else False.
    """
    return True if match(pattern, filter_value) else False

class bitsight_client():
    def __init__(self, rc, options):
        self.rc = rc
        self.base_url = options.get("bitsight_url", None)
        self.token = options.get("bitsight_api_token", None)

    def selftest(self):
        """ This makes an api call to rating/v2/ for the purpose of checking connectivity to BitSight.

        Returns:
            dict: A dictionary containing a list of resources using the v2 api call.
        """
        return self.rc.execute("GET", f"{self.base_url}v2/", auth=(self.token, '')).json()

    def get_alerts(self, limit: int=100, offset: int=0, alert_date: str=None, alert_date_gt: str=None, alert_date_gte: str=None,
                   alert_date_lt: str=None, alert_date_lte: str=None, alert_type: str=None, company_guid: str=None,
                   expand: str=None, folder_guid: str=None, severity: str=None):
        """See your existing alerts and their details.

        Args:
            limit (int, optional): Set the maximum number of results. The results might include fewer records (even zero), but not more. Defaults to 100.
            offset (int, optional): Set the starting point of the return. Defaults to 0.
            alert_date (str, optional): Filter alerts by the specified alert date. Format YYYY‑MM‑DD
            alert_date_gt (str, optional): Filter alerts after the requested date. This parameter is incompatible with alert_date. Format YYYY‑MM‑DD
            alert_date_gte (str, optional): Filter alerts after or on the requested date. This parameter is incompatible with alert_date. Format YYYY‑MM‑DD
            alert_date_lt (str, optional): Filter alerts prior to the requested date. This parameter is incompatible with alert_date. Format YYYY‑MM‑DD
            alert_date_lte (str, optional): Filter alerts prior to or on the requested date. This parameter is incompatible with alert_date. Format YYYY‑MM‑DD
            alert_type (str, optional): Filter alerts by the specified alert category. Allowed values: PERCENT_CHANGE, RATING_THRESHOLD, RISK_CATEGORY,
                                        NIST_CATEGORY, INFORMATIONAL, PUBLIC_DISCLOSURE, VULNERABILITY, FINDINGS_FILTER
            company_guid (str, optional): Filter by company.
            expand (str, optional): Include additional alert details. Examples: company_custom_id or details only one can be given.
            folder_guid (str, optional): Filter alerts by the specified folder. Folder unique identifier.
            severity (str, optional): Filter alerts by the specified change severity. Allowed values: CRITICAL, WARN, INCREASE, INFORMATIONAL
        """
        # Build URL with given parameters
        url = f"{self.base_url}v2/alerts?limit={limit}&offset={offset}"
        if alert_date and check_filter_value_format(DATE_PATTERN, alert_date):
            url += f"&alert_date={alert_date}"
        else: # If alert data is given then the other alert_date filters can not be used
            for date_name, date_value in {"alert_date_gt": alert_date_gt, "alert_date_gte": alert_date_gte, "alert_date_lt": alert_date_lt, "alert_date_lte": alert_date_lte}.items():
                if date_value and check_filter_value_format(DATE_PATTERN, date_value):
                    url += f"&{date_name}={date_value}"
        if alert_type in ["PERCENT_CHANGE", "RATING_THRESHOLD", "RISK_CATEGORY", "NIST_CATEGORY", "INFORMATIONAL", "PUBLIC_DISCLOSURE", "VULNERABILITY", "FINDINGS_FILTER"]:
            url += f"&alert_type={alert_type}"
        for filter_name, filter_value in {"company_guid": company_guid, "expand": expand, "folder_guid": folder_guid}.items():
            if filter_value:
                url += f"&{filter_name}={filter_value}"
        if severity in ["CRITICAL", "WARN", "INCREASE", "INFORMATIONAL"]:
            url += f"&severity={severity}"
        # Make API call to BitSight using given parameters
        return self.rc.execute("GET", url, auth=(self.token, '')).json()

    def get_latest_alerts(self, limit: int=100, offset: int=0, alert_type: str=None, company_guid: str=None,
                          expand: str=None, folder_guid: str=None, severity: str=None):
        """Get alerts generated during the most recent daily platform update.

        Args:
            limit (int, optional): Set the maximum number of results. The results might include fewer records (even zero), but not more. Defaults to 100.
            offset (int, optional): Set the starting point of the return. Defaults to 0.
            alert_type (str, optional): Filter alerts by the specified alert category. Allowed values: PERCENT_CHANGE, RATING_THRESHOLD, RISK_CATEGORY,
                                        NIST_CATEGORY, INFORMATIONAL, PUBLIC_DISCLOSURE, VULNERABILITY, FINDINGS_FILTER
            company_guid (str, optional): Filter by company.
            expand (str, optional): Include additional alert details. Examples: company_custom_id or details only one can be given.
            folder_guid (str, optional): Filter alerts by the specified folder. Folder unique identifier.
            severity (str, optional): Filter alerts by the specified change severity. Allowed values: CRITICAL, WARN, INCREASE, INFORMATIONAL
        """
        # Build URL with given parameters
        url = f"{self.base_url}v2/alerts/latest?limit={limit}&offset={offset}"
        if alert_type in ["PERCENT_CHANGE", "RATING_THRESHOLD", "RISK_CATEGORY", "NIST_CATEGORY", "INFORMATIONAL", "PUBLIC_DISCLOSURE", "VULNERABILITY", "FINDINGS_FILTER"]:
            url += f"&alert_type={alert_type}"
        for filter_name, filter_value in {"company_guid": company_guid, "expand": expand, "folder_guid": folder_guid}.items():
            if filter_value:
                url += f"&{filter_name}={filter_value}"
        if severity in ["CRITICAL", "WARN", "INCREASE", "INFORMATIONAL"]:
            url += f"&severity={severity}"
        # Make API call to BitSight using given parameters
        return self.rc.execute("GET", url, auth=(self.token, '')).json()

    def get_company_search(self, limit: int=100, offset: int=0, domain: str=None, expand: str=None, guids: str=None, industry: str=None,
                           industry_slug: str=None, in_portfolio: bool=None, name: str=None, scope: str=None):
        """Search for a company in the Bitsight inventory by name or domain.

        Args:
            limit (int, optional): Set the maximum number of results. The results might include fewer records (even zero), but not more. Defaults to 100.
            offset (int, optional): Set the starting point of the return. Defaults to 0.
            domain (str, optional): The domain of a company. Search by domain name.
            expand (str, optional): Include additional alert details. Examples: details. Using this parameter could slow the performance of the endpoint and limit results to 10 companies.
            guids (str, optional): Company unique identifier. This disables the name and domain parameters.
            industry (str, optional): Industry name.
            industry_slug (str, optional): Industry slug name.
            in_portfolio (bool, optional): true = Limit results to only portfolio companies.
            name (str, optional): The name of a company.
            scope (str, optional): Filter by Security Performance Management and Benchmarking companies. spm.
        """
        # Validate required fields
        if not domain and not name and not guids:
            raise IntegrationError("You must provide a domain, name, or guids parameter.")
        # Build URL with given parameters
        url = f"{self.base_url}v1/companies/search?limit={limit}&offset={offset}"
        for filter_name, filter_value in {"domain": domain, "expand": expand, "guids": guids, "industry": industry, "industry_slug": industry_slug, "in_portfolio": in_portfolio, "name": name, "scope": scope}.items():
            if filter_value != None:
                url += f"&{filter_name}={filter_value}"
        # Make API call to BitSight using given parameters
        return self.rc.execute("GET", url, auth=(self.token, '')).json()

    def get_company_details(self, company_guid: str=None, fields: str=None):
        """Get a company’s details, including: Their rating, Rating history, Risk vector grades, Company information, and Relationship details.

        Args:
            company_guid (str, required): Company unique identifier.
            fields (str, optional): Comma-separated field names, which are available in the response. The order of the specific fields might not be reflected in the response when using this parameter. Example: [industry_average, industry_percentile]
        """
        # Validate required field
        if not company_guid:
            raise IntegrationError("company_guid parameter is required for function GET: Company Details.")

        # Build URL with given parameters
        url = f"{self.base_url}v1/companies/{company_guid}?"
        if fields:
            url += f"fields={fields}"
        # Make API call to BitSight using given parameters
        return self.rc.execute("GET", url, auth=(self.token, '')).json()

    def get_company_finding_details(self, limit: int=100, offset: int=0, company_guid: str=None, affects_rating: bool=None, affects_rating_details: str=None,
                                    assets_asset: str=None, assets_category: str=None, assets_combined_importance: str=None, assets_hosted_by: str=None, attributed_companies_guid: list=None,
                                    attributed_companies_name: list=None, cvss_base_gte: float=None, cvss_base_lte: float=None, details_grade: str=None,
                                    details_grade_gt: str=None, details_grade_lt: str=None, details_infection_family: str=None, details_observed_ips_contains: str=None,
                                    details_vulnerabilities_severity: str=None, evidence_key: str=None, expand: str=None, first_seen: str=None, first_seen_gt: str=None,
                                    first_seen_gte: str=None, first_seen_lt: str=None, first_seen_lte: str=None, last_remediation_status_date: str=None,
                                    last_remediation_status_date_gt: str=None, last_remediation_status_date_gte: str=None, last_remediation_status_date_lt: str=None,
                                    last_remediation_status_date_lte: str=None, last_remediation_status_label: str=None, last_seen: str=None, last_seen_gt: str=None,
                                    last_seen_gte: str=None, last_seen_lt: str=None, last_seen_lte: str=None, remediation_assignments: str=None, risk_vector_label: str=None,
                                    severity: float=None, severity_gt: float=None, severity_gte: float=None, severity_lt: float=None, severity_lte: float=None,
                                    severity_category: float=None, tags_contains: str=None, unsampled: bool=None, vulnerabilities: str=None):
        """Get an organization’s finding details.
        This includes the finding details of risk types that affect or will affect security ratings; Compromised Systems, Diligence (except Domain Squatting), and User Behavior (File Sharing).
        This does not include Domain Squatting and Public Disclosures (Security Incidents and Other Disclosures), as their findings cannot be queried via the API

        Args:
            limit (int, optional): Set the maximum number of results. The results might include fewer records (even zero), but not more. Defaults to 100.
            offset (int, optional): Set the starting point of the return. Defaults to 0.
            company_guid (str, required): Company unique identifier.
            affects_rating (bool, optional): true = Include only the findings that have an impact on the letter grade. Filter by findings that have an impact on the letter grade.
            affects_rating_details (str, optional): Allowed values are AFFECTS_RATING and LIFETIME_EXPIRED. AFFECTS_RATING - Affects the risk vector grade. LIFETIME_EXPIRED - Does not affect the risk vector grade because the finding has reached the end of its lifetime.
            assets_asset (str, optional): Either a Domain or an IP Address. Filter by asset.
            assets_category (str, optional): Allowed values are low, medium, high, and critical. Filter by asset importance.
            assets_combined_importance (str, optional): Comma-separated asset importance. Allowed values are low, medium, high, and critical. Filter by combined asset importance.
            assets_hosted_by (str, optional): Hosting provider’s unique identifier entity_guid. Filter by the hosting provider.
            attributed_companies_guid (list, optional): Comma-separated My Company or My Subsidiary unique identifiers entity_guid. Filter by companies in your Ratings Tree that are attributed to the finding.
            attributed_companies_name (list, optional): Comma-separated company names. Filter by companies in your Ratings Tree that are attributed to the finding.
            cvss_base_gte (float, optional): Decimal 1 to 10. Include findings with vulnerabilities with a CVSS score greater than or equal to this value.
            cvss_base_lte (float, optional): Decimal 1 to 10. Include findings with vulnerabilities with a CVSS score less than or equal to this value.
            details_grade (str, optional): Allowed values are GOOD, FAIR, WARN, BAD, NEUTRAL, and NA. Filter by Diligence finding grade or N/A for Compromised Systems and User Behavior findings. Incompatible with grade_lt and grade_gt.
            details_grade_gt (str, optional): Allowed values are GOOD, FAIR, WARN, BAD, NEUTRAL, and NA. Include a range from the selected Diligence finding grade to GOOD. Incompatible with grade.
            details_grade_lt (str, optional): Allowed values are GOOD, FAIR, WARN, BAD, NEUTRAL, and NA. Include a range from the selected Diligence finding grade to BAD. Incompatible with grade.
            details_infection_family (str, optional): Comma-separated infection names. Example Gamarue. Filter by infections.
            details_observed_ips_contains (str, optional): IP Address. Include findings from a particular IP address.
            details_vulnerabilities_severity (str, optional): The Bitsight severity of vulnerabilities. Allowed values are minor, moderate, material, and severe. Filter by vulnerability severity.
            evidence_key (str, optional): Either a domain or IP address. Filter by the company’s asset (domain or IP address) that’s attributed to the finding.
            expand (str, optional): Allowed values are attributed_companies, remediation_history, assets.tag_details, and tag_details. attributed_companies = Include companies that are attributed to the finding. remediation_history = Issue tracking history. assets.tag_details = Tag details associated with each asset that relates to the finding. tag_details = Tag details associated with the finding. Include additional information.
            first_seen (str, optional): Date in format YYYY-MM-DD. Include findings that were first seen on this date. Incompatible with first_seen_lt and first_seen_gt.
            first_seen_gt (str, optional): Date in format YYYY-MM-DD. Include findings that were first seen after this date. Incompatible with first_seen.
            first_seen_gte (str, optional): Date in format YYYY-MM-DD. Include findings that were first seen on and after this date. Incompatible with first_seen.
            first_seen_lt (str, optional): Date in format YYYY-MM-DD. Include findings that were first seen prior to this date. Incompatible with first_seen.
            first_seen_lte (str, optional): Date in format YYYY-MM-DD. Include findings that were first seen on and prior to this date. Incompatible with first_seen.
            last_remediation_status_date (str, optional): Date in format YYYY-MM-DD. Include findings that last had a remediation status change on this date. Incompatible with last_remediation_status_date_lt and last_remediation_status_date_gt.
            last_remediation_status_date_gt (str, optional): Date in format YYYY-MM-DD. Include findings that last had a remediation status change after this date. Incompatible with last_remediation_status_date.
            last_remediation_status_date_gte (str, optional): Date in format YYYY-MM-DD. Include findings that last had a remediation status change on and after this date. Incompatible with last_remediation_status_date.
            last_remediation_status_date_lt (str, optional): Date in format YYYY-MM-DD. Include findings that last had a remediation status change prior to this date. Incompatible with last_remediation_status_date.
            last_remediation_status_date_lte (str, optional): Date in format YYYY-MM-DD. Include findings that last had a remediation status change prior to and on this date. Incompatible with last_remediation_status_date.
            last_remediation_status_label (str, optional): The remediation status of the finding. Allowed values are No Status, Open, To Do, Work In Progress, Resolved, and Risk Accepted. Filter by the current remediation status of the finding.
            last_seen (str, optional): Date in format YYYY-MM-DD. Include findings that were last seen on this date. Incompatible with last_seen_lt and last_seen_gt.
            last_seen_gt (str, optional): Date in format YYYY-MM-DD. Include findings that were last seen after this date. Incompatible with last_seen.
            last_seen_gte (str, optional): Date in format YYYY-MM-DD. Include findings that were last seen on and after this date. Incompatible with last_seen.
            last_seen_lt (str, optional): Date in format YYYY-MM-DD. Include findings that were last seen prior to this date. Incompatible with last_seen.
            last_seen_lte (str, optional): Date in format YYYY-MM-DD. Include findings that were last seen on and prior to this date. Incompatible with last_seen.
            remediation_assignments (str, optional): Comma-separated user unique identifier user_guid. Filter by users assigned to the findings.
            risk_vector_label (str, optional): Comma-separated risk vector slug names. Examples: botnet_infections, spam_propagation, spf_domains, open_ports, and file_sharing. Filter by particular risk vectors. Does not include Domain Squatting, Security Incidents, and Other Disclosures.
            severity (float, optional): Decimal severity. 1 to 3.9 is Minor, 4 to 6.9 is Moderate, 7 to 8.9 is Material, and 9 to 10 is Severe. Filter by finding severity.
            severity_gt (float, optional): Decimal severity. 1 to 3.9 is Minor, 4 to 6.9 is Moderate, 7 to 8.9 is Material, and 9 to 10 is Severe. Include finding severity that are of greater severity.
            severity_gte (float, optional): Decimal severity. 1 to 3.9 is Minor, 4 to 6.9 is Moderate, 7 to 8.9 is Material, and 9 to 10 is Severe. Include finding severity that are of greater or equal severity.
            severity_lt (float, optional): Decimal severity. 1 to 3.9 is Minor, 4 to 6.9 is Moderate, 7 to 8.9 is Material, and 9 to 10 is Severe. Include finding severity that are of lesser severity.
            severity_lte (float, optional): Decimal severity. 1 to 3.9 is Minor, 4 to 6.9 is Moderate, 7 to 8.9 is Material, and 9 to 10 is Severe. Include finding severity that are of lesser or equal severity.
            severity_category (float, optional): Decimal severity. 1 to 3.9 is Minor, 4 to 6.9 is Moderate, 7 to 8.9 is Material, and 9 to 10 is Severe. Filter by finding severity.
            tags_contains (str, optional): Infrastructure tags, which are defined by the company to identify assets that belong to them. Filter by infrastructure tags.
            unsampled (bool, optional): true = Enable unsampled findings. false = Sample findings. If you have Unsampled Findings [beta] enabled, get your My Company’s or My Subsidiary’s unsampled findings data.
            vulnerabilities (str, optional): Comma-separated vulnerability name. Example: CVE-2021-3618, Example: CVE-2021-3618, Example: CVE-2021-3618. Filter by vulnerability.

        Returns:
            Dict: Results of API call.
        """
        # Validate required field
        if not company_guid:
            raise IntegrationError("company_guid parameter is required for function GET: Finding Details.")
        # Build URL with given parameters
        url = f"{self.base_url}v1/companies/{company_guid}/findings?limit={limit}&offset={offset}"
        filters = { # Dictionary of filter names and their values
            "affects_rating": affects_rating, "affects_rating_details": affects_rating_details, "assets.asset": assets_asset, "assets.category": assets_category, "assets.combined_importance": assets_combined_importance,
            "assets.hosted_by": assets_hosted_by, "attributed_companies.guid": attributed_companies_guid, "attributed_companies.name": attributed_companies_name, "details.cvss.base_gte": cvss_base_gte,
            "details.cvss.base_lte": cvss_base_lte, "details.grade": details_grade, "details.grade_gt": details_grade_gt, "details.grade_lt": details_grade_lt, "details.infection.family": details_infection_family,
            "details.observed_ips_contains": details_observed_ips_contains, "details.vulnerabilities.severity": details_vulnerabilities_severity, "evidence_key": evidence_key, "expand": expand,
            "first_seen": first_seen, "first_seen_gt": first_seen_gt, "first_seen_gte": first_seen_gte, "first_seen_lt": first_seen_lt, "first_seen_lte": first_seen_lte, "last_remediation_status_date": last_remediation_status_date,
            "last_remediation_status_date_gt": last_remediation_status_date_gt, "last_remediation_status_date_gte": last_remediation_status_date_gte, "last_remediation_status_date_lt": last_remediation_status_date_lt,
            "last_remediation_status_date_lte": last_remediation_status_date_lte, "last_remediation_status_label": last_remediation_status_label, "last_seen": last_seen, "last_seen_gt": last_seen_gt,
            "last_seen_gte": last_seen_gte, "last_seen_lt": last_seen_lt, "last_seen_lte": last_seen_lte, "remediation_assignments": remediation_assignments, "risk_vector_label": risk_vector_label,
            "severity": severity, "severity_gt": severity_gt, "severity_gte": severity_gte, "severity_lt": severity_lt, "severity_lte": severity_lte, "severity_category": severity_category,
            "tags_contains": tags_contains, "unsampled": unsampled, "vulnerabilities": vulnerabilities
        }
        date_filters = ["last_remediation_status_date_lte", "last_remediation_status_date_lt", "last_remediation_status_date_gte", "last_remediation_status_date_gt", "last_remediation_status_date", "first_seen_lte",
                        "first_seen_lt", "first_seen_gte", "first_seen_gt", "first_seen", "last_seen_lte", "last_seen_lt", "last_seen_gt", "last_seen_gte", "last_seen"]
        for filter_name, filter_value in filters.items():
            if filter_value != None:
                if filter_name == "last_remediation_status_label" and filter_value not in ["No Status", "Open", "To Do", "Work In Progress", "Resolved", "Risk Accepted"]:
                    # Do not add the last_remediation_status_label filter if the value is not in the list of allowed values
                    continue
                if filter_name in date_filters and not check_filter_value_format(DATE_PATTERN, filter_value):
                    # Do not add a date type filter if the value is not formatted properly.
                    continue
                if (type(filter_value) == float or type(filter_value) == int) and not (filter_value >= 1, filter_value <= 10):
                    # Do not add decimal filters that have a value less than 1 or greater then 10
                    continue
                if filter_name in ["remediation_assignments", "attributed_companies.guid", "assets.hosted_by"]:
                    # Check if given values are all properly formatted guids. If they are not do not add the filter.
                    valid_guids = True
                    list_value = filter_value
                    if type(filter_value) == str:
                        list_value = filter_value.split(",")
                    for value in list_value:
                        if not check_filter_value_format(GUID_PATTERN, value):
                            valid_guids = False
                            break
                    if not valid_guids:
                        continue
                if filter_name == "expand" and filter_value not in ["attributed_companies", "remediation_history", "assets.tag_details", "tag_details"]:
                    # Check if values given for the filter expand is in the allowed values. If it is not do not add the filter.
                    continue
                if filter_name == "details.vulnerabilities.severity" and filter_value not in ["minor", "moderate", "material", "severe"]:
                    # Check if the value given for the filter details.vulnerabilities.severity is in the allowed values. If it is not do not add the filter.
                    continue
                if filter_name in ["details.grade_gt", "details.grade_lt"] and details_grade:
                    # If a value is given for the filter details.grade then the filters details.grade_gt and details.grade_lt can not be set.
                    continue
                if filter_name == "details.grade" and filter_value.upper() not in ["GOOD", "FAIR", "WARN", "BAD", "NEUTRAL", "NA"]:
                    # Check if the value given for the filter details.grade is in the allowed values. If it is not do not add the filter.
                    continue
                if filter_name in ["assets.combined_importance", "assets.category"]:
                    # Check if the values given for the filter assets.combined_importance is in the allowed values. If it is not do not add the filter.
                    valid_importance = True
                    for importance in filter_value.split(","):
                        if importance.strip().lower() not in ["critical", "high", "medium", "low"]:
                            valid_importance = False
                            break
                    if not valid_importance:
                        continue
                if filter_name == "affects_rating_details" and filter_value not in ["AFFECTS_RATING", "LIFETIME_EXPIRED"]:
                    # Check if the values given for the filter affects_rating_details is in the allowed values. If it is not do not add the filter.
                    continue
                if filter_name == "first_seen" and (first_seen_gt or first_seen_lt):
                    # The filter first_seen is incompatible with the filters first_seen_gt and first_seen_lt
                    continue
                if filter_name in ["first_seen_gt", "first_seen_gte", "first_seen_lt", "first_seen_lte"] and first_seen:
                    # The filters first_seen_gt, first_seen_gte, first_seen_lt, and first_seen_lte are incompatible with the filter first_seen.
                    continue
                if filter_name == "last_remediation_status_date" and (last_remediation_status_date_lt or last_remediation_status_date_gt):
                    # The filter last_remediation_status_date is incompatible with last_remediation_status_date_lt and last_remediation_status_date_gt.
                    continue
                if filter_name in ["last_remediation_status_date_gt", "last_remediation_status_date_gte", "last_remediation_status_date_lt", "last_remediation_status_date_lte"] and last_remediation_status_date:
                    # The filters last_remediation_status_date_gt, last_remediation_status_date_gte, last_remediation_status_date_lt, and last_remediation_status_date_lte are incompatible with last_remediation_status_date.
                    continue
                if filter_name == "last_seen" and (last_seen_gt or last_seen_lt):
                    # The filter last_seen is incompatible with last_seen_gt and last_seen_lt
                    continue
                if filter_name in ["last_seen_gt", "last_seen_gte", "last_seen_lt", "last_seen_lte"] and last_seen:
                    # The filters last_seen_gt, last_seen_gte, last_seen_lt, and last_seen_lte are incompatible wit last_seen.
                    continue
                url += f"&{filter_name}={filter_value}"
        # Make API call to BitSight using given parameters
        return self.rc.execute("GET", url, auth=(self.token, '')).json()

    def get_portfolio_details(self, limit: int=100, offset: int=0, countries: str=None, exclude_subscription_type_slug: list=None, filter_group: str=None,
                              risk_vectors_grade: str=None, risk_vectors_slug: str=None, software_category: str=None, software_name: str=None, folder: list=None,
                              industry_name: str=None, industry_slug: str=None, infections: list=None, life_cycle_slug: str=None, open_ports: list=None,
                              products: list=None, product_types: list=None, providers: str=None, rating: int=None, rating_gt: int=None, rating_gte: int=None,
                              rating_lt: int=None, rating_lte: int=None, relationship_slug: str=None, security_incident_categories: list=None,
                              subscription_type_slug: list=None, tier: str=None, type: str=None, vendor_action_plan: str=None, vulnerabilities: list=None):
        """Get information about the companies in your portfolio.

        Args:
            limit (int, optional): Set the maximum number of results. The results might include fewer records (even zero), but not more. Defaults to 100.
            offset (int, optional): Set the starting point of the return. Defaults to 0.
            countries (str, optional): Country codes. Use EUU for all EU countries and NEU for all non-EU countries. Example: US, CA. Filter companies by one or more countries in which they have IP addresses.
            exclude_subscription_type_slug (list, optional): Subscription slug names. Exclude one or more subscription types.
            filter_group (str, optional): Group filters and modify the way the filters intersect with each other. Examples: risk_vectors or software.
            risk_vectors_grade (str, optional): Risk vector letter grades. Filter companies with certain risk vector letter grades. Does not include N/A letter grades. On its own, this includes companies that have any of the specified grades in any risk vector. This can only be used if filter_group=risk_vectors.
            risk_vectors_slug (str, optional): Risk vector slug names. Filter companies with graded risk vectors. On its own, this includes companies with a grade in any of the specified risk vectors. This can only be used if filter_group=risk_vectors.
            software_category (str, optional): The supported status: Supported, Unsupported, and Unknown. Filter companies by the supported statuses of their software. On its own, this includes companies that have at least one software of any of the specified categories. This can only be used if filter_group=software.
            software_name (str, optional): Software name. Filter companies with certain software detected on their network. On its own, this includes companies that have any of the specified software, across all software categories. This can only be used if filter_group=software.
            folder (list, optional): Folder unique identifiers folder_guid. null to include companies that are not in a folder. Filter companies by folder.
            industry_name (str, optional): Industry name. Filter companies by their industry.
            industry_slug (str, optional): Industry slug name. Filter companies by their industry.
            infections (list, optional): Comma-separated infection names. Filter companies that have certain infections.
            life_cycle_slug (str, optional): Life Cycle slug names. null to include companies that have not been assigned to a Life Cycle stage. Example: onboarding,null. Filter companies by their Life Cycle stage.
            open_ports (list, optional): Comma-separated service names and port numbers. Example: SIP, Port 8081, HTTPS, Port 443. Filter companies by open ports.
            products (list, optional): Comma-separated product names. Filter by companies that use certain service provider products.
            product_types (list, optional): Comma-separated product types. Filter by companies that use certain service provider product types.
            providers (str, optional): The name of the service provider. Filter companies that rely on certain service providers.
            rating (int, optional): A 10-point incremental number between 250 and 900. Filter companies by their rating.
            rating_gt (int, optional): A 10-point incremental number between 250 and 900. Filter companies that have a rating greater than the given value.
            rating_gte (int, optional): A 10-point incremental number between 250 and 900. Filter companies that have a rating greater than or equal to the given value.
            rating_lt (int, optional): A 10-point incremental number between 250 and 900. Filter companies that have a rating less than the given value.
            rating_lte (int, optional): A 10-point incremental number between 250 and 900. Filter companies that have a rating less than or equal to the given value.
            relationship_slug (str, optional): Relationship slug name. Allowed values: vendor, strategic_partner, fourth_party, subsidiary, benchmark, other, or null. Filter companies of certain relationships.
            security_incident_categories (list, optional): Comma-separated Public Disclosure risk type slug names. Examples: breach, general, other. Filter companies (including their subsidiaries) that have been affected by a Public Disclosures event in the past year.
            subscription_type_slug (list, optional): Comma-separated subscription slug names. Examples: applicants, countries, one-time, alerts-only, continuous_monitoring, and vendor-selection. Filter companies by subscription type.
            tier (str, optional): Tier unique identifiers tier_guid. null to include companies that are not in a tier. Filter companies by their tier.
            type (str, optional): Rating type name. Rating type name. Values: CURATED, SELF_PUBLISHED, and PRIVATE. Filter companies by rating type.
            vendor_action_plan (str, optional): Action plan slug name. Values: monitor, review, and escalate. Filter companies by action plan.
            vulnerabilities (list, optional): Comma-separated vulnerability names. Example: CVE-2016-10712. Filter companies that have certain vulnerabilities.
        """
        # Build URL with given parameters
        url = f"{self.base_url}v2/portfolio?limit={limit}&offset={offset}"
        filter_dict = {"countries": countries, "exclude_subscription_type.slug": exclude_subscription_type_slug, "filter_group": filter_group, "risk_vectors.grade": risk_vectors_grade,
                       "risk_vectors.slug": risk_vectors_slug, "software.category": software_category, "software.name": software_name, "folder": folder, "industry.name": industry_name,
                       "industry.slug": industry_slug, "infections": infections, "life_cycle.slug": life_cycle_slug, "open_ports": open_ports, "products": products, "product_types": product_types,
                       "providers": providers, "rating": rating, "rating_gt": rating_gt, "rating_gte": rating_gte, "rating_lt": rating_lt, "rating_lte": rating_lte, "relationship.slug": relationship_slug,
                       "security_incident_categories": security_incident_categories, "subscription_type.slug": subscription_type_slug, "tier": tier, "type": type, "vendor_action_plan": vendor_action_plan,
                       "vulnerabilities": vulnerabilities}
        # Add filters to the url
        for filter_name, filter_value in filter_dict.items():
            if filter_value:
                if filter_name == "software.category" and filter_value not in ["Supported", "Unsupported", "Unknown"]:
                    # The filter software.category can only be equal to Supported, Unsupported, and Unknown.
                    continue
                if filter_group and filter_group == "risk_vectors" and filter_name not in ["risk_vectors.grade", "risk_vectors.slug"]:
                    # The filters risk_vectors.grade and risk_vectors.slug can only be set if the filter filter_group is equal to risk_vectors
                    continue
                if filter_group and filter_group == "software" and filter_name not in ["software.category", "software.name"]:
                    # The filters software.category and software.name can only be used if the filter filter_group is equal to software
                    continue
                if filter_name in ["rating", "rating_gt", "rating_gte", "rating_lt", "rating_lte"] and filter_value not in range(250, 900, 10):
                    # The rating filters can only be a 10-point incremental number between 250 and 900.
                    continue
                if filter_name == "vendor_action_plan" and filter_value not in ["monitor", "review", "escalate"]:
                    # The filter vendor_action_plan can only equal monitor, review or escalate.
                    continue
                if filter_name == "relationship.slug" and filter_value not in ["vendor", "strategic_partner", "fourth_party", "subsidiary", "benchmark", "other", "null"]:
                    # The filter relationship.slug can only be one of the above values.
                    continue
                if filter_name == "type" and filter_value not in ["CURATED", "SELF_PUBLISHED", "PRIVATE"]:
                    # The filter type can only be one of the above values.
                    continue
                url += f"&{filter_name}={filter_value}"

        # Make API call to BitSight using given parameters
        return self.rc.execute("GET", url, auth=(self.token, '')).json()

    def get_rapid_underwriting_assessments(self, industry: str=None, generate_report: bool=None, url: str=None):
        """Use Rapid Underwriting Assessments to quickly get rating details for any mapped or unmapped company within 1 minute.

        Args:
            industry (str, optional): Industry name. Compare the average security rating and risk vector letter grades of a particular industry or sub-industry. The return is based on the industry, rather than the sub-industry. If two sub-industries belong to the same industry, they will result in the same response.
            generate_report (bool, optional): true = Include the Amazon Simple Storage Service (S3) PDF link in the response. The request must also include the industry parameter. Get the Amazon Simple Storage Service (S3) link to download a PDF of the report.
            url (str, required): The domain of the company to query. Example: http://saperix.com
        """
        # Build URL with given parameters
        url = f"{self.base_url}v1/fast-ratings"
        payload = {"url": url}
        if industry:
            payload["industry"] = industry
            payload["generate_report"] = str(generate_report)
        # Make API call to BitSight using given parameters
        return self.rc.execute("POST", url, auth=(self.token, ''), data=payload).json()
