# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
import time
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_service_now.util.resilient_helper import ResilientHelper
from fn_service_now.util.external_ticket_status_datatable import ExternalTicketStatusDatatable



class FunctionPayload(object):
    """Class that contains the payload sent back to UI and available in the post-processing script"""
    def __init__(self, inputs):
        self.success = True
        self.inputs = inputs
        self.row_id = None            # The row_id of the row created in Datatable
        self.res_id = None            # RES-<incId>-<taskId>
        self.res_link = None          # Link to res incident/task
        self.sn_ref_id = None         # Local (to its table) unique id of ServiceNow record
        self.sn_sys_id = None         # Global unique id of ServiceNow record
        self.sn_record_link = None    # Link to ServiceNow record
        self.sn_time_created = None   # Timestamp from Resilient Integration server when record was created

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'sn_utilities_create_in_servicenow"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_service_now", {})

        # Get host as needed to create link to incident/task
        self.host = opts.get("host")

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_service_now", {})

    @function("sn_utilities_create_in_servicenow")
    def _sn_utilities_create_in_servicenow_function(self, event, *args, **kwargs):
        """Function: A function that sends Task or Incident information to a custom endpoint in ServiceNow in order to create an associated ServiceNow record"""

        log = logging.getLogger(__name__)

        # Convert unicode dict to str dict
        def _byteify(data):
            if isinstance(data, unicode):
                return data.encode("utf-8")

            elif isinstance(data, dict):
                return {_byteify(key): _byteify(value) for key, value in data.items()}

            return None

        try:
            # Instansiate helper (which gets appconfigs from file)
            res_helper = ResilientHelper(self.options)

            # Get the function inputs:
            inputs = {
                "incident_id": res_helper.get_function_input(kwargs, "incident_id"),  # number (required)
                "task_id": res_helper.get_function_input(kwargs, "task_id", True),  # number (optional)
                "sn_init_work_note": res_helper.get_function_input(kwargs, "sn_init_work_note", True),  # text (optional)
                "sn_optional_fields": res_helper.get_function_input(kwargs, "sn_optional_fields", True)  # text, JSON String (optional)
            }

            # Convert 'sn_optional_fields' JSON string to Dictionary
            try:
                inputs["sn_optional_fields"] = json.loads(inputs["sn_optional_fields"], object_hook=_byteify)
            except Exception:
                raise ValueError("sn_optional_fields JSON String is invalid")

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Instansiate new Resilient API object
            res_client = self.rest_client()

            # Instansiate a reference to the ServiceNow Datatable
            datatable = ExternalTicketStatusDatatable(res_client, payload.inputs["incident_id"])

            # Generate the res_link
            payload.res_link = res_helper.generate_res_link(payload.inputs["incident_id"], self.host, payload.inputs["task_id"])

            # Generate the request_data
            request_data = res_helper.generate_sn_request_data(
                res_client,
                datatable,
                payload.inputs["incident_id"],
                res_helper.SN_TABLE_NAME,
                payload.res_link,
                payload.inputs["task_id"],
                payload.inputs["sn_init_work_note"],
                payload.inputs["sn_optional_fields"])

            yield StatusMessage("Creating a new record in ServiceNow")
            # Call POST and get response
            create_in_sn_response = res_helper.sn_POST("/create", data=json.dumps(request_data))

            if create_in_sn_response is not None:

                yield StatusMessage("Record Created")

                # Get current time (*1000 as API does not accept int)
                now = int(time.time() * 1000)

                # Add values to payload
                payload.res_id = create_in_sn_response["res_id"]
                payload.sn_ref_id = create_in_sn_response["sn_ref_id"]
                payload.sn_sys_id = create_in_sn_response["sn_sys_id"]
                payload.sn_record_link = res_helper.generate_sn_link("number={0}".format(payload.sn_ref_id))
                payload.sn_time_created = now

                try:
                    yield StatusMessage("Updating Datatable")
                    # Add row to the datatable
                    add_row_response = datatable.add_row(
                        payload.sn_time_created,
                        payload.res_id,
                        payload.sn_ref_id,
                        res_helper.convert_text_to_richtext("Active"),
                        res_helper.convert_text_to_richtext("Sent to ServiceNow"),
                        """<a href="{0}">RES</a> <a href="{1}">SN</a>""".format(payload.res_link, payload.sn_record_link))

                    payload.row_id = add_row_response["id"]

                except Exception as err_msg:
                    payload.success = False
                    raise ValueError("Failed to add row to datatable {0}".format(err_msg))

            else:
                payload.success = False

            results = payload.as_dict()

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
