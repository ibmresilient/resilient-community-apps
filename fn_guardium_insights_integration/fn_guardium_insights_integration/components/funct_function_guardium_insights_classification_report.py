# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import json
import logging
import re

import six
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload

from fn_guardium_insights_integration.lib.insights_services import InsightsServices
from fn_guardium_insights_integration.lib.resilient_table_opeations import ResilientTableOperations
from fn_guardium_insights_integration.lib.time_conversions import convert_epoch_utc_date_time


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'function_guardium_insights_classification_report"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_guardium_insights_integration", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_guardium_insights_integration", {})

    @function("function_guardium_insights_classification_report")
    def _function_guardium_insights_classification_report_function(self, event, *args, **kwargs):
        """Function: A function to get classification report data."""
        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            input_field_guardium_insights_who = kwargs.get("input_field_guardium_insights_who")  # text
            input_field_guardium_insights_what = kwargs.get("input_field_guardium_insights_what")  # text
            input_field_guardium_insights_from_date = kwargs.get(
                "input_field_guardium_insights_from_date")  # datetimepicker
            input_field_guardium_insights_to_date = kwargs.get(
                "input_field_guardium_insights_to_date")  # datetimepicker
            input_field_guardium_insights_fetch_size = kwargs.get("input_field_guardium_insights_fetch_size")  # number

            log = logging.getLogger(__name__)
            log.info("Incident ID: %s", incident_id)
            log.info("Input GI who: %s", input_field_guardium_insights_who)
            log.info("Input GI what: %s", input_field_guardium_insights_what)
            log.info("Input GI from date: %s", input_field_guardium_insights_from_date)
            log.info("Input GI to date: %s", input_field_guardium_insights_to_date)
            log.info("Input GI report fetch size: %s", input_field_guardium_insights_fetch_size)

            yield StatusMessage("Generating classification report on incident: {}".format(incident_id))

            # Validating app.config settings
            validate_fields(["datatable_id"], self.options)

            # Reading app.config settings
            datatable_id = self.options.get("datatable_id")

            # Initialize GI service
            gi_services = InsightsServices(self.options, log)

            # Initialize Resilient RESTful service
            res_dt_service = ResilientTableOperations(datatable_id, incident_id, self.rest_client(), log)

            # Initialize Result payload.
            res_pay = ResultPayload("fn_guardium_insights_integration", **kwargs)
            res_status = False
            reason = ""

            # converting milli to sec
            input_field_guardium_insights_from_date = int(input_field_guardium_insights_from_date / 1000)
            input_field_guardium_insights_to_date = int(input_field_guardium_insights_to_date / 1000)

            # Converting epoch seconds UTC Date time format.
            _from_date = convert_epoch_utc_date_time(input_field_guardium_insights_from_date)
            _to_date = convert_epoch_utc_date_time(input_field_guardium_insights_to_date)

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

            report_payload = gi_services.generate_report_payload(_from_date, _to_date,
                                                                 input_field_guardium_insights_fetch_size,
                                                                 _datasourceip,
                                                                 _port)
            gi_list_reports = gi_services.list_all_reports()
            report_id = gi_services.get_report_id(gi_list_reports, "Classification")
            if report_id:
                # Run classification report.
                report_data = gi_services.run_report(report_payload)

                # Correcting received response, if its not correct.
                if six.PY3:
                    if isinstance(report_data, str):
                        report_data = re.sub(r"{.result.*\{.total_number_of_rows.*\}", "", report_data)
                        report_data = json.loads(report_data)
                elif six.PY2:
                    if isinstance(report_data, str) or isinstance(report_data, unicode):
                        if isinstance(report_data, unicode):
                            report_data = str(report_data)
                        report_data = re.sub(r"{.result.*\{.total_number_of_rows.*\}", "", report_data)
                        report_data = json.loads(report_data)

                # clearing the existing table data
                log.info("Clearing existing table data...")
                res_dt_service.clear_existing_table_data()

                # adding report data to the resilient table
                log.info("Adding report data to the resilient table...")
                data = report_data.get("result", {}).get("data", {})
                if data:
                    cell_data_list = []
                    for each_data in data:
                        event = each_data.get("results")
                        cell_data = res_dt_service.construct_table_payload(event)
                        cell_data_list.append(cell_data)
                    res_dt_service.add_table_data(cell_data_list)
                    res_status = True
                    reason = "Classification report generated successfully..."
                else:
                    reason = "Classification report: No results found. Try adjusting the report settings."
                    log.info(reason)
            else:
                reason = "--------Classification report not found in Guardium Insight system---------"
                log.info(reason)

            yield StatusMessage("classification report completed: incident ID{}".format(incident_id))

            fun_result = res_pay.done(res_status, {}, reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(fun_result)
        except Exception as fn_err:
            yield FunctionError(fn_err)
