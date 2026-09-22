# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, readable_datetime
from fn_bitsight_cyber_insurance.util.helper import bitsight_client, PACKAGE_NAME,\
    DEFAULT_LIMIT, DEFAULT_OFFSET

FN_NAME = "bitsight_cyber_insurance_get_finding_details"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'bitsight_cyber_insurance_get_finding_details'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get an organization’s finding details.
This includes the finding details of risk types that affect or will affect security ratings; Compromised Systems, Diligence (except Domain Squatting), and User Behavior (File Sharing).
This does not include Domain Squatting and Public Disclosures (Security Incidents and Other Disclosures), as their findings cannot be queried via the API.
        Inputs:
            -   fn_inputs.bitsight_ci_last_remediation_status_label
            -   fn_inputs.bitsight_ci_details_observed_ips_contains
            -   fn_inputs.bitsight_ci_last_remediation_status_date_gt
            -   fn_inputs.bitsight_ci_details_grade
            -   fn_inputs.bitsight_ci_details_grade_gt
            -   fn_inputs.bitsight_ci_first_seen_lt
            -   fn_inputs.bitsight_ci_company_guid
            -   fn_inputs.bitsight_ci_first_seen_gt
            -   fn_inputs.bitsight_ci_vulnerabilities
            -   fn_inputs.bitsight_ci_severity_gt
            -   fn_inputs.bitsight_ci_details_vulnerabilities_severity
            -   fn_inputs.bitsight_ci_affects_rating
            -   fn_inputs.bitsight_ci_severity_lt
            -   fn_inputs.bitsight_ci_last_seen
            -   fn_inputs.bitsight_ci_last_remediation_status_date_lte
            -   fn_inputs.bitsight_ci_severity_lte
            -   fn_inputs.bitsight_ci_limit
            -   fn_inputs.bitsight_ci_last_remediation_status_date
            -   fn_inputs.bitsight_ci_assets_combined_importance
            -   fn_inputs.bitsight_ci_affects_rating_details
            -   fn_inputs.bitsight_ci_severity_category
            -   fn_inputs.bitsight_ci_expand_findings
            -   fn_inputs.bitsight_ci_offset
            -   fn_inputs.bitsight_ci_remediation_assignments
            -   fn_inputs.bitsight_ci_assets_category
            -   fn_inputs.bitsight_ci_last_remediation_status_date_gte
            -   fn_inputs.bitsight_ci_cvss_base_gte
            -   fn_inputs.bitsight_ci_evidence_key
            -   fn_inputs.bitsight_ci_last_seen_gte
            -   fn_inputs.bitsight_ci_last_seen_lte
            -   fn_inputs.bitsight_ci_first_seen
            -   fn_inputs.bitsight_ci_last_seen_lt
            -   fn_inputs.bitsight_ci_risk_vector_label
            -   fn_inputs.bitsight_ci_cvss_base_lte
            -   fn_inputs.bitsight_ci_details_grade_lt
            -   fn_inputs.bitsight_ci_last_remediation_status_date_lt
            -   fn_inputs.bitsight_ci_last_seen_gt
            -   fn_inputs.bitsight_ci_unsampled
            -   fn_inputs.bitsight_ci_severity_num
            -   fn_inputs.bitsight_ci_first_seen_lte
            -   fn_inputs.bitsight_ci_assets_asset
            -   fn_inputs.bitsight_ci_details_infection_family
            -   fn_inputs.bitsight_ci_attributed_companies_name
            -   fn_inputs.bitsight_ci_severity_gte
            -   fn_inputs.bitsight_ci_tags_contains
            -   fn_inputs.bitsight_ci_assets_hosted_by
            -   fn_inputs.bitsight_ci_attributed_companies_guid
            -   fn_inputs.bitsight_ci_first_seen_gte
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate required configs
        validate_fields(["bitsight_ci_company_guid"], fn_inputs)
        try:
            # Make call to BitSight to get finding details.
            resp = bitsight_client(self.rc, self.options).get_company_finding_details(
                limit=fn_inputs.bitsight_ci_limit if getattr(fn_inputs, "bitsight_ci_limit", None) else DEFAULT_LIMIT,
                offset=fn_inputs.bitsight_ci_offset if getattr(fn_inputs, "bitsight_ci_offset", 0) else DEFAULT_OFFSET,
                company_guid=fn_inputs.bitsight_ci_company_guid,
                affects_rating=fn_inputs.bitsight_ci_affects_rating if getattr(fn_inputs, "bitsight_ci_affects_rating", None) else None,
                affects_rating_details=fn_inputs.bitsight_ci_affects_rating_details if getattr(fn_inputs, "bitsight_ci_affects_rating_details", None) else None,
                assets_asset=fn_inputs.bitsight_ci_assets_asset if getattr(fn_inputs, "bitsight_ci_assets_asset", None) else None,
                assets_category=fn_inputs.bitsight_ci_assets_category if getattr(fn_inputs, "bitsight_ci_assets_category", None) else None,
                assets_combined_importance=fn_inputs.bitsight_ci_assets_combined_importance if getattr(fn_inputs, "bitsight_ci_assets_combined_importance", None) else None,
                assets_hosted_by=fn_inputs.bitsight_ci_assets_hosted_by if getattr(fn_inputs, "bitsight_ci_assets_hosted_by", None) else None,
                attributed_companies_guid=fn_inputs.bitsight_ci_attributed_companies_guid.strip() if getattr(fn_inputs, "bitsight_ci_attributed_companies_guid", None) else None,
                attributed_companies_name=fn_inputs.bitsight_ci_attributed_companies_name.strip() if getattr(fn_inputs, "bitsight_ci_attributed_companies_name", None) else None,
                cvss_base_gte=float(fn_inputs.bitsight_ci_cvss_base_gte) if getattr(fn_inputs, "bitsight_ci_cvss_base_gte", None) else None,
                cvss_base_lte=float(fn_inputs.bitsight_ci_cvss_base_lte) if getattr(fn_inputs, "bitsight_ci_cvss_base_lte", None) else None,
                details_grade=fn_inputs.bitsight_ci_details_grade if getattr(fn_inputs, "bitsight_ci_details_grade", None) else None,
                details_grade_gt=fn_inputs.bitsight_ci_details_grade_gt if getattr(fn_inputs, "bitsight_ci_details_grade_gt", None) else None,
                details_grade_lt=fn_inputs.bitsight_ci_details_grade_lt if getattr(fn_inputs, "bitsight_ci_details_grade_lt", None) else None,
                details_infection_family=fn_inputs.bitsight_ci_details_infection_family if getattr(fn_inputs, "bitsight_ci_details_infection_family", None) else None,
                details_observed_ips_contains=fn_inputs.bitsight_ci_details_observed_ips_contains if getattr(fn_inputs, "bitsight_ci_details_observed_ips_contains", None) else None,
                details_vulnerabilities_severity=fn_inputs.bitsight_ci_details_vulnerabilities_severity if getattr(fn_inputs, "bitsight_ci_details_vulnerabilities_severity", None) else None,
                evidence_key=fn_inputs.bitsight_ci_evidence_key if getattr(fn_inputs, "bitsight_ci_evidence_key", None) else None,
                expand=fn_inputs.bitsight_ci_expand_findings if getattr(fn_inputs, "bitsight_ci_expand_findings", None) else None,
                first_seen=readable_datetime(fn_inputs.bitsight_ci_first_seen, rtn_format="%Y-%m-%d") if getattr(fn_inputs, "bitsight_ci_first_seen", None) else None,
                first_seen_gt=readable_datetime(fn_inputs.bitsight_ci_first_seen_gt, rtn_format="%Y-%m-%d") if getattr(fn_inputs, "bitsight_ci_first_seen_gt", None) else None,
                first_seen_gte=readable_datetime(fn_inputs.bitsight_ci_first_seen_gte, rtn_format="%Y-%m-%d") if getattr(fn_inputs, "bitsight_ci_first_seen_gte", None) else None,
                first_seen_lt=readable_datetime(fn_inputs.bitsight_ci_first_seen_lt, rtn_format="%Y-%m-%d") if getattr(fn_inputs, "bitsight_ci_first_seen_lt", None) else None,
                first_seen_lte=readable_datetime(fn_inputs.bitsight_ci_first_seen_lte, rtn_format="%Y-%m-%d") if getattr(fn_inputs, "bitsight_ci_first_seen_lte", None) else None,
                last_remediation_status_date=readable_datetime(fn_inputs.bitsight_ci_last_remediation_status_date, rtn_format="%Y-%m-%d") if getattr(fn_inputs, "bitsight_ci_last_remediation_status_date", None) else None,
                last_remediation_status_date_gt=readable_datetime(fn_inputs.bitsight_ci_last_remediation_status_date_gt, rtn_format="%Y-%m-%d") if getattr(fn_inputs, "bitsight_ci_last_remediation_status_date_gt", None) else None,
                last_remediation_status_date_gte=readable_datetime(fn_inputs.bitsight_ci_last_remediation_status_date_gte, rtn_format="%Y-%m-%d") if getattr(fn_inputs, "bitsight_ci_last_remediation_status_date_gte", None) else None,
                last_remediation_status_date_lt=readable_datetime(fn_inputs.bitsight_ci_last_remediation_status_date_lt, rtn_format="%Y-%m-%d") if getattr(fn_inputs, "bitsight_ci_last_remediation_status_date_lt", None) else None,
                last_remediation_status_date_lte=readable_datetime(fn_inputs.bitsight_ci_last_remediation_status_date_lte, rtn_format="%Y-%m-%d") if getattr(fn_inputs, "bitsight_ci_last_remediation_status_date_lte", None) else None,
                last_remediation_status_label=fn_inputs.bitsight_ci_last_remediation_status_label if getattr(fn_inputs, "bitsight_ci_last_remediation_status_label", None) else None,
                last_seen=readable_datetime(fn_inputs.bitsight_ci_last_seen, rtn_format="%Y-%m-%d") if getattr(fn_inputs, "bitsight_ci_last_seen", None) else None,
                last_seen_gt=readable_datetime(fn_inputs.bitsight_ci_last_seen_gt, rtn_format="%Y-%m-%d") if getattr(fn_inputs, "bitsight_ci_last_seen_gt", None) else None,
                last_seen_gte=readable_datetime(fn_inputs.bitsight_ci_last_seen_gte, rtn_format="%Y-%m-%d") if getattr(fn_inputs, "bitsight_ci_last_seen_gte", None) else None,
                last_seen_lt=readable_datetime(fn_inputs.bitsight_ci_last_seen_lt, rtn_format="%Y-%m-%d") if getattr(fn_inputs, "bitsight_ci_last_seen_lt", None) else None,
                last_seen_lte=readable_datetime(fn_inputs.bitsight_ci_last_seen_lte, rtn_format="%Y-%m-%d") if getattr(fn_inputs, "bitsight_ci_last_seen_lte", None) else None,
                remediation_assignments=fn_inputs.bitsight_ci_remediation_assignments if getattr(fn_inputs, "bitsight_ci_remediation_assignments", None) else None,
                risk_vector_label=fn_inputs.bitsight_ci_risk_vector_label if getattr(fn_inputs, "bitsight_ci_risk_vector_label", None) else None,
                severity=float(fn_inputs.bitsight_ci_severity) if getattr(fn_inputs, "bitsight_ci_severity", None) else None,
                severity_gt=float(fn_inputs.bitsight_ci_severity_gt) if getattr(fn_inputs, "bitsight_ci_severity_gt", None) else None,
                severity_category=float(fn_inputs.bitsight_ci_severity_category) if getattr(fn_inputs, "bitsight_ci_severity_category", None) else None,
                severity_gte=float(fn_inputs.bitsight_ci_severity_gte) if getattr(fn_inputs, "bitsight_ci_severity_gte", None) else None,
                severity_lt=float(fn_inputs.bitsight_ci_severity_lt) if getattr(fn_inputs, "bitsight_ci_severity_lt", None) else None,
                severity_lte=float(fn_inputs.bitsight_ci_severity_lte) if getattr(fn_inputs, "bitsight_ci_severity_lte", None) else None,
                tags_contains=fn_inputs.bitsight_ci_tags_contains if getattr(fn_inputs, "bitsight_ci_tags_contains", None) else None,
                unsampled=fn_inputs.bitsight_ci_unsampled if getattr(fn_inputs, "bitsight_ci_unsampled", None) else None,
                vulnerabilities=fn_inputs.bitsight_ci_vulnerabilities if getattr(fn_inputs, "bitsight_ci_vulnerabilities", None) else None
            )

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            yield FunctionResult(resp.get("results", []))
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
