# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, write_to_tmp_file, write_file_attachment
from fn_bitsight_cyber_insurance.util.helper import bitsight_client, PACKAGE_NAME
import os, shutil
from json import dumps

FN_NAME = "bitsight_cyber_insurance_get_company_details"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'bitsight_cyber_insurance_get_company_details'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get a company’s details, including: Their rating, Rating history, Risk vector grades, Company information, and Relationship details.
        Inputs:
            -   fn_inputs.bitsight_ci_company_guid
            -   fn_inputs.bitsight_ci_fields
            -   fn_inputs.bitsight_ci_soar_incident_id
            -   fn_inputs.bitsight_ci_return_as_attachment
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        path_tmp_dir = None
        # Validate required inputs
        validate_fields(["bitsight_ci_company_guid", "bitsight_ci_soar_incident_id"], fn_inputs)
        try:
            resp = bitsight_client(self.rc, self.options).get_company_details(
                company_guid=fn_inputs.bitsight_ci_company_guid.strip(),
                fields=fn_inputs.bitsight_ci_fields if getattr(fn_inputs, "bitsight_ci_fields", None) else None
            )
            # If bitsight_ci_return_as_attachment is True, then add am attachment to the SOAR incident with the Company Details
            if getattr(fn_inputs, "bitsight_ci_return_as_attachment", None):
                file_name = f"BitSight_Company_Details_{fn_inputs.bitsight_ci_company_guid.strip()}.txt"
                # Create temp file from results
                path_tmp_file, path_tmp_dir = write_to_tmp_file(dumps(resp, indent=4).encode("utf-8"), tmp_file_name=file_name)
                with open(path_tmp_file, "rb") as data_stream:
                    write_file_attachment(self.rest_client(), file_name, data_stream, fn_inputs.bitsight_ci_soar_incident_id)

            yield FunctionResult(resp)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
        finally:
            if path_tmp_dir and os.path.isdir(path_tmp_dir):
                shutil.rmtree(path_tmp_dir)
