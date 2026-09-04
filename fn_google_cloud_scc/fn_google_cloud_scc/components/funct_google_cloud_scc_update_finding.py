# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from fn_google_cloud_scc.lib.scc_common import PACKAGE_NAME, GoogleSCCCommon
from google.cloud.securitycenter import Finding
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import IntegrationError, validate_fields

FN_NAME = "google_cloud_scc_update_finding"

FINDING_NAME_KEY = "name"
SOURCE_PROPS_PREFIX = "source_properties"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'google_cloud_scc_update_finding'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Function to update values of findings from Google Cloud Security Command Center.
        Inputs:
            -   fn_inputs.google_scc_filter
            -   fn_inputs.google_scc_update_value
            -   fn_inputs.google_scc_update_key
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        self.app_common = GoogleSCCCommon(self.options, self.rc)

        validate_fields(["google_scc_update_key"], fn_inputs)
        update_key = fn_inputs.google_scc_update_key
        update_value = getattr(fn_inputs, "google_scc_update_value", "") # allow for empty string update values

        # this will be set to the app.config default if not given
        findings_filter = fn_inputs.google_scc_filter
        if not findings_filter:
            self.LOG.warning("No filter provided to {0}. This is dangerous as it can cause unexpected updates to multiple findings in Google SCC. Use with caution!".format(FN_NAME))

        findings_result_list = self.app_common.get_findings(findings_filter=findings_filter, return_findings_result_list=True)

        findings_list = []

        # get findings returns a list -- this funciton supports updating
        # multiple findings at once so loop through them all
        # NOTE: the workflow that ships with this app only calls this
        # function with a filter that will update *one* finding
        # but the function will work for multiple as long as the filter is
        # well defined
        for finding_result in findings_result_list:
            finding = finding_result.finding

            try:
                result = self.app_common.update_finding(
                    self._build_finding_update(finding.name, update_key, update_value),
                    [update_key]
                )
            except ValueError as e:
                if "Unknown field for Finding" in str(e):
                    raise IntegrationError("Invalid SCC Finding key: '{0}'".format(update_key))
                raise e

            # convert finding back to dictionary for results
            result = Finding.to_dict(result, use_integers_for_enums=False)
            # enrich the finding with custom fields
            result = self.app_common.enrich_finding(result)

            findings_list.append({"finding": result})


        results = {
            "findings_list": findings_list,
            "updated_key": update_key,
            "updated_value": update_value,
        }

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)


    @staticmethod
    def _build_finding_update(finding_name, update_key, update_value):
        """
        Builds a google.cloud.securitycenter.Finding object to be passed
        to the scc_common method update_finding

        Parses source_properties properly to that they are accepted by the Google API
        """

        # multiple nested keys are not supported.
        # only supports single keys or <parent>.<key>
        if len(update_key.split(".")) > 2:
            raise IntegrationError("'{0}' does not support updating multiple nested properties. Max nesting = 1\nFor example '<parent>.<key>'".format(FN_NAME))
        elif len(update_key.split(".")) == 2:
            # grab the parent key, set value equal to {<key> : <value>}
            key = update_key.split(".")[0]
            value = {update_key.split(".")[1]: update_value}
        else:
            # standard key : value
            key = update_key
            value = update_value

        # create the finding object with the name of the finding, and the update key-value pair
        return Finding({
            FINDING_NAME_KEY: finding_name,
            key: value
        })
