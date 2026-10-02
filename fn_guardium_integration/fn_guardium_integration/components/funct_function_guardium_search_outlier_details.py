# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Function implementation"""
import logging
from datetime import datetime
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields
from fn_guardium_integration.lib.resilient_rest_services import ResilientRestService
from fn_guardium_integration.lib.grd_rest_endpoints_service import GrdRestEndpoint
from fn_guardium_integration.util.process_outlier_details import update_outlier_details_table
from fn_guardium_integration.util.static_data import SEARCH_TIME_FORMAT


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'function_guardium_search_outlier_details"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_guardium_integration", {})
        self.opts_data = opts

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_guardium_integration", {})

    @function("function_guardium_search_outlier_details")
    def _function_guardium_search_outlier_details_function(self, event, *args, **kwargs):
        """Function: A function to enrich outliers data."""
        try:
            # Get the function parameters:
            resilient_incident_id = kwargs.get("grd_resilient_incident_id")  # number
            guardium_period_from = kwargs.get("guardium_period_from")  # datetimepicker
            guardium_period_to = kwargs.get("guardium_period_to")  # datetimepicker
            search_date_time = kwargs.get("grd_search_date_time")  # datetimepicker

            # converting to date and time
            guardium_period_from = datetime.fromtimestamp(guardium_period_from / 1000).strftime(SEARCH_TIME_FORMAT)
            guardium_period_to = datetime.fromtimestamp(guardium_period_to / 1000).strftime(SEARCH_TIME_FORMAT)
            search_date_time = datetime.fromtimestamp(search_date_time / 1000).strftime(SEARCH_TIME_FORMAT)

            search_username = kwargs.get("grd_search_username")  # text
            search_ip_address = kwargs.get("grd_search_ip_address")  # text
            search_database = kwargs.get("grd_search_database")  # text

            # Validating Mandatory app.config param
            validate_fields(["outlier_table"], self.options)

            outlier_table_id = self.options.get("outlier_table")

            log = logging.getLogger(__name__)
            log.info("Resilient Incident ID: %s", resilient_incident_id)
            log.info("Search Period From: %s", guardium_period_from)
            log.info("Search Period To: %s", guardium_period_to)
            log.info("Outlier DB User: %s", search_username)
            log.info("Outlier Server: %s", search_ip_address)
            log.info("Outlier Database: %s", search_database)
            log.info("Outlier Time Frame: %s", search_date_time)

            yield StatusMessage(u"Started - Searching Outlier Details")
            resilient_object = ResilientRestService(self.opts_data, self.options, log)
            grd_rest_object = GrdRestEndpoint(self.options, resilient_object.client_secret, resilient_object.unique_id,
                                              log)
            if not resilient_object.client_secret:
                raise ValueError(u"Guardium client secret not generated, please run `Generate Guardium Client Secret`")

            # Forming search query
            query_param = []
            for param in [search_username, search_ip_address, search_database, search_date_time]:
                if param and param != "N/A" and param != "N\\A":
                    query_param.append(param)
            query_string = " AND ".join(query_param)

            search_result = grd_rest_object.grd_search(query="({})".format(query_string), category="OUTLIER",
                                                       start_time=guardium_period_from, end_time=guardium_period_to)

            # Updating the outliers table with returned search results.
            update_outlier_details_table(resilient_object, table_id=outlier_table_id, inc_id=resilient_incident_id,
                                         search_data=search_result)

            msg = u"Completed - Searching Outlier Details."
            yield StatusMessage(msg)

            results = {
                "content": msg
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as fun_er:
            yield FunctionError(fun_er)
