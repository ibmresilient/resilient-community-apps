# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_bitsight_cyber_insurance.util.helper import bitsight_client, PACKAGE_NAME,\
    DEFAULT_LIMIT, DEFAULT_OFFSET

FN_NAME = "bitsight_cyber_insurance_get_portfolio_details"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'bitsight_cyber_insurance_get_portfolio_details'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get information about the companies in your portfolio.
        Inputs:
            -   fn_inputs.bitsight_ci_open_ports
            -   fn_inputs.bitsight_ci_vendor_action_plan
            -   fn_inputs.bitsight_ci_infections
            -   fn_inputs.bitsight_ci_life_cycle_slug
            -   fn_inputs.bitsight_ci_rating_lt
            -   fn_inputs.bitsight_ci_providers
            -   fn_inputs.bitsight_ci_vulnerabilities
            -   fn_inputs.bitsight_ci_subscription_type_slug
            -   fn_inputs.bitsight_ci_exclude_subscription_type_slug
            -   fn_inputs.bitsight_ci_tier
            -   fn_inputs.bitsight_ci_industry_slug
            -   fn_inputs.bitsight_ci_folder_guid
            -   fn_inputs.bitsight_ci_countries
            -   fn_inputs.bitsight_ci_risk_vectors_slug
            -   fn_inputs.bitsight_ci_limit
            -   fn_inputs.bitsight_ci_risk_vectors_grade
            -   fn_inputs.bitsight_ci_security_incident_categories
            -   fn_inputs.bitsight_ci_rating_lte
            -   fn_inputs.bitsight_ci_relationship_slug
            -   fn_inputs.bitsight_ci_software_name
            -   fn_inputs.bitsight_ci_filter_group
            -   fn_inputs.bitsight_ci_offset
            -   fn_inputs.bitsight_ci_industry
            -   fn_inputs.bitsight_ci_products
            -   fn_inputs.bitsight_ci_product_types
            -   fn_inputs.bitsight_ci_rating_gte
            -   fn_inputs.bitsight_ci_rating_gt
            -   fn_inputs.bitsight_ci_rating_type
            -   fn_inputs.bitsight_ci_rating
            -   fn_inputs.bitsight_ci_software_category
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        try:
            resp = bitsight_client(self.rc, self.options).get_portfolio_details(
                limit=fn_inputs.bitsight_ci_limit if getattr(fn_inputs, "bitsight_ci_limit", None) else DEFAULT_LIMIT,
                offset=fn_inputs.bitsight_ci_offset if getattr(fn_inputs, "bitsight_ci_offset", None) else DEFAULT_OFFSET,
                countries=fn_inputs.bitsight_ci_countries if getattr(fn_inputs, "bitsight_ci_countries", None) else None,
                exclude_subscription_type_slug=fn_inputs.bitsight_ci_exclude_subscription_type_slug.replace(", ", ",").split(",") if getattr(fn_inputs, "bitsight_ci_exclude_subscription_type_slug", None) else None,
                filter_group=fn_inputs.bitsight_ci_filter_group if getattr(fn_inputs, "bitsight_ci_filter_group", None) else None,
                risk_vectors_grade=fn_inputs.bitsight_ci_risk_vectors_grade if getattr(fn_inputs, "bitsight_ci_risk_vectors_grade", None) else None,
                risk_vectors_slug=fn_inputs.bitsight_ci_risk_vectors_slug if getattr(fn_inputs, "bitsight_ci_risk_vectors_slug", None) else None,
                software_category=fn_inputs.bitsight_ci_software_category if getattr(fn_inputs, "bitsight_ci_software_category", None) else None,
                software_name=fn_inputs.bitsight_ci_software_name if getattr(fn_inputs, "bitsight_ci_software_name", None) else None,
                folder=fn_inputs.bitsight_ci_folder.replace(", ", ",").split(",") if getattr(fn_inputs, "bitsight_ci_folder", None) else None,
                industry_name=fn_inputs.bitsight_ci_industry if getattr(fn_inputs, "bitsight_ci_industry", None) else None,
                industry_slug=fn_inputs.bitsight_ci_industry_slug if getattr(fn_inputs, "bitsight_ci_industry_slug", None) else None,
                infections=fn_inputs.bitsight_ci_infections.replace(", ", ",").split(",") if getattr(fn_inputs, "bitsight_ci_infections", None) else None,
                life_cycle_slug=fn_inputs.bitsight_ci_life_cycle_slug if getattr(fn_inputs, "bitsight_ci_life_cycle_slug", None) else None,
                open_ports=fn_inputs.bitsight_ci_open_ports.replace(", ", ",").split(",") if getattr(fn_inputs, "bitsight_ci_open_ports", None) else None,
                products=fn_inputs.bitsight_ci_products.replace(", ", ",").split(",") if getattr(fn_inputs, "bitsight_ci_products", None) else None,
                product_types=fn_inputs.bitsight_ci_product_types.replace(", ", ",").split(",") if getattr(fn_inputs, "bitsight_ci_product_types", None) else None,
                providers=fn_inputs.bitsight_ci_providers if getattr(fn_inputs, "bitsight_ci_providers", None) else None,
                rating=fn_inputs.bitsight_ci_rating if getattr(fn_inputs, "bitsight_ci_rating", None) else None,
                rating_gt=fn_inputs.bitsight_ci_rating_gt if getattr(fn_inputs, "bitsight_ci_rating_gt", None) else None,
                rating_gte=fn_inputs.bitsight_ci_rating_gte if getattr(fn_inputs, "bitsight_ci_rating_gte", None) else None,
                rating_lt=fn_inputs.bitsight_ci_rating_lt if getattr(fn_inputs, "bitsight_ci_rating_lt", None) else None,
                rating_lte=fn_inputs.bitsight_ci_rating_lte if getattr(fn_inputs, "bitsight_ci_rating_lte", None) else None,
                relationship_slug=fn_inputs.bitsight_ci_relationship_slug if getattr(fn_inputs, "bitsight_ci_relationship_slug", None) else None,
                security_incident_categories=fn_inputs.bitsight_ci_security_incident_categories.replace(", ", ",").split(",") if getattr(fn_inputs, "bitsight_ci_security_incident_categories", None) else None,
                subscription_type_slug=fn_inputs.bitsight_ci_subscription_type_slug.replace(", ", ",").split(",") if getattr(fn_inputs, "bitsight_ci_subscription_type_slug", None) else None,
                tier=fn_inputs.bitsight_ci_tier if getattr(fn_inputs, "bitsight_ci_tier", None) else None,
                vendor_action_plan=fn_inputs.bitsight_ci_vendor_action_plan if getattr(fn_inputs, "bitsight_ci_vendor_action_plan", None) else None,
                vulnerabilities=fn_inputs.bitsight_ci_vulnerabilities.replace(", ", ",").split(",") if getattr(fn_inputs, "bitsight_ci_vulnerabilities", None) else None,
            )

            yield FunctionResult(resp.get("results", []))
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
