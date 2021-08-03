# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""
import json
import logging
import re

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload

from fn_guardium_insights_integration.lib.insights_services import InsightsServices
from fn_guardium_insights_integration.lib.resilient_incident_operations import ResilientIncidentHelper
from fn_guardium_insights_integration.lib.time_conversions import compute_start_stop_times


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'function_guardium_insights_populate_breach_data_types"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_guardium_insights_integration", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_guardium_insights_integration", {})

    @function("function_guardium_insights_populate_breach_data_types")
    def _function_guardium_insights_populate_breach_data_types_function(self, event, *args, **kwargs):
        """Function: A function to populate the incident breach data types."""
        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            input_field_guardium_insights_who = kwargs.get("input_field_guardium_insights_who")  # text
            input_field_guardium_insights_what = kwargs.get("input_field_guardium_insights_what")  # text

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("input_field_guardium_insights_who: %s", input_field_guardium_insights_who)
            log.info("input_field_guardium_insights_what: %s", input_field_guardium_insights_what)

            yield StatusMessage("populating breach data types on incident: {}".format(incident_id))

            # Validating app.config settings
            validate_fields(["report_period", "report_fetch_size"], self.options)

            # Reading app.config settings
            report_period = self.options.get("report_period")
            report_fetch_size = self.options.get("report_fetch_size")

            # Initialize GI service
            gi_services = InsightsServices(self.options, log)

            # Initialize resilient service
            res_service = ResilientIncidentHelper(self.rest_client(), log)

            # Initialize Result payload.
            res_pay = ResultPayload("fn_guardium_insights_integration", **kwargs)
            res_status = False
            reason = ""

            _from_date, _to_date = compute_start_stop_times(report_period)

            # Converting string json to json object
            try:
                input_field_guardium_insights_what = json.loads(input_field_guardium_insights_what)
            except json.decoder.JSONDecodeError as err_msg:
                log.info("error converting what information to json object: {}".format(err_msg))
                input_field_guardium_insights_what = dict()

            _datasourceip = _port = None
            if input_field_guardium_insights_what:
                _datasourceip = input_field_guardium_insights_what.get("server_ip")
                _port = input_field_guardium_insights_what.get("server_port")
            if _datasourceip or _port:
                report_payload = gi_services.generate_report_payload(_from_date, _to_date, report_fetch_size,
                                                                     _datasourceip, _port)
                gi_list_reports = gi_services.list_all_reports()
                report_id = gi_services.get_report_id(gi_list_reports, "Classification")
                if report_id:
                    # Run classification report.
                    report_data = gi_services.run_report(report_payload)

                    # Correcting received response, if its not correct.
                    if isinstance(report_data, str):
                        report_data = re.sub(r"{.result.*\{.total_number_of_rows.*\}", "", report_data)
                        report_data = json.loads(report_data)

                    # Populating breach data types
                    res_service.populate_breach_data_types(incident_id, report_data)

                    reason = "populating breach data types completed: incident ID{}".format(incident_id)
                else:
                    reason = "--------Classification report not found in Guardium Insight system---------"
                    log.info(reason)
            else:
                reason = "--------Data SourceIP and Port Information is not available in the incident---------"
                log.info(reason)
            yield StatusMessage("populating breach data types completed: incident ID{}".format(incident_id))

            fun_result = res_pay.done(res_status, {}, reason)
            # Produce a FunctionResult with the results
            yield FunctionResult(fun_result)
        except Exception as fn_err:
            yield FunctionError(fn_err)
