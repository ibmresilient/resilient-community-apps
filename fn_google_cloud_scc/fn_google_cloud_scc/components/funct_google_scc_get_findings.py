# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from fn_google_cloud_scc.poller.google_cloud_scc_poller import (
    CLOSE_INCIDENT_TEMPLATE, ENTITY_LABEL, SOAR_ENTITY_ID_FIELD, get_entity_id)
from fn_google_cloud_scc.poller.soar_common import SOARCommon
from fn_google_cloud_scc.lib.scc_common import PACKAGE_NAME, GoogleSCCCommon
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import IntegrationError, make_payload_from_template, validate_fields

FN_NAME = "google_scc_get_findings"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'google_scc_get_findings'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

        self.soar_close_case_template = self.options.get("soar_close_case_template")

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Function to get findings from Google Cloud Security Command Center. Optional filter is available.
        Inputs:
            -   fn_inputs.google_scc_filter
            -   fn_inputs.google_scc_close_case_on_change
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields(["google_scc_close_case_on_change"], fn_inputs)

        self.app_common = GoogleSCCCommon(self.options)
        self.soar_common = SOARCommon(self.rest_client())

        # this will be set to the app.config default if not given
        findings_filter = getattr(fn_inputs, "google_scc_filter", None)

        # check whether the case should be closed in SOAR if the finding is inactive
        # this one is required and is validated above
        close_case_if_inactive = fn_inputs.google_scc_close_case_on_change

        findings = self.app_common.get_findings(findings_filter=findings_filter)

        # check if should close incident upon state change to INACTIVE
        cases_closed = []
        if close_case_if_inactive and len(findings) == 1:
            finding_result_obj = findings[0]
            finding = finding_result_obj.get(ENTITY_LABEL)
            finding_id = get_entity_id(finding)
            finding["finding_id"] = finding_id

            soar_case, _error_msg = self.soar_common.get_soar_case({ SOAR_ENTITY_ID_FIELD: finding_id }, open_cases=False)

            if soar_case and soar_case.get("plan_status", "") == "A":
                soar_case_id = soar_case.get("id")

                soar_close_payload = make_payload_from_template(
                                                self.soar_close_case_template,
                                                CLOSE_INCIDENT_TEMPLATE,
                                                finding
                                            )
                self.soar_common.update_soar_case(
                                                soar_case_id,
                                                soar_close_payload
                                            )

                cases_closed.append(soar_case_id)
                yield self.status_message("Closed SOAR case {0} from {1} {2}".format(soar_case_id, ENTITY_LABEL, finding_id))
        elif close_case_if_inactive:
            raise IntegrationError("Cannot set 'google_scc_close_case_on_change' to 'True' when given filter returns more than one incident. Use filter like: 'name = \\\"<finding_name>\\\"'")

        results = {
            "findings_list": findings,
            "cases_closed_from_function": cases_closed
        }

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
