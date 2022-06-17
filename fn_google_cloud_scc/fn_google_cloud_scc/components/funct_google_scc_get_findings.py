# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields, make_payload_from_template

from fn_google_cloud_scc.util.scc_common import PACKAGE_NAME, GoogleSCCCommon
from fn_google_cloud_scc.poller.soar_common import SOARCommon
from fn_google_cloud_scc.poller.google_cloud_scc_poller import SOAR_ENTITY_ID_FIELD, CLOSE_INCIDENT_TEMPLATE, ENTITY_LABEL, get_entity_id

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

        self.app_common = GoogleSCCCommon(self.options)
        self.soar_common = SOARCommon(self.rest_client())

        # if no filter given, defaults to value from app.config if present
        # -- ok to be None if not given and not in app.config
        if not fn_inputs.google_scc_filter:
            fn_inputs.google_scc_filter = self.options.get("findings_filter")

        findings = self.app_common.get_findings(findings_filter=fn_inputs.google_scc_filter)

        # check if should close incident upon state change to INACTIVE
        cases_closed = []
        if fn_inputs.google_scc_close_case_on_change and len(findings) == 1:
            finding_result_obj = findings[0]
            finding = finding_result_obj.get(ENTITY_LABEL)
            finding_id = get_entity_id(finding)
            finding["finding_id"] = finding_id

            soar_case, _error_msg = self.soar_common.get_soar_case({ SOAR_ENTITY_ID_FIELD: finding_id }, open_cases=False)

            if soar_case and soar_case["plan_status"] == "A":
                soar_case_id = soar_case["id"]

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
        elif fn_inputs.google_scc_close_case_on_change:
            raise IntegrationError("Cannot set 'google_scc_close_case_on_change' when given filter returns more than one incident. Use filter like: 'name = \\\"<finding_name>\\\"'")

        results = {
            "findings_list": findings,
            "cases_closed_from_function": cases_closed
        }

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
