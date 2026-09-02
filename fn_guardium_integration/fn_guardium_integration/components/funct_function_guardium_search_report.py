# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Function implementation"""

import logging
from datetime import datetime
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_guardium_integration.lib.grd_rest_endpoints_service import GrdRestEndpoint
from fn_guardium_integration.lib.resilient_rest_services import ResilientRestService
from fn_guardium_integration.util.process_search_data import update_search_to_table
from fn_guardium_integration.util.static_data import REPORT_TIME_FORMAT


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'function_guardium_search_report"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_guardium_integration", {})
        self.opts_data = opts

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_guardium_integration", {})

    @function("function_guardium_search_report")
    def _function_guardium_search_report_function(self, event, *args, **kwargs):
        """Function: A function to search guardium reports."""
        try:
            # Initialize the logger, Resilient, Guardium classes
            logger_object = logging.getLogger(__name__)
            resilient_object = ResilientRestService(self.opts_data, self.options, logger_object)
            grd_rest_object = GrdRestEndpoint(self.options, resilient_object.client_secret, resilient_object.unique_id,
                                              logger_object)

            # Get the function parameters:
            guardium_report = kwargs.get("guardium_report")  # text
            guardium_period_from = kwargs.get("guardium_period_from")  # datetimepicker
            guardium_period_to = kwargs.get("guardium_period_to")  # datetimepicker
            # converting to date and time
            guardium_period_from = datetime.fromtimestamp(guardium_period_from / 1000).strftime(REPORT_TIME_FORMAT)
            guardium_period_to = datetime.fromtimestamp(guardium_period_to / 1000).strftime(REPORT_TIME_FORMAT)
            guardium_show_aliases = kwargs.get("guardium_show_aliases")  # text
            guardium_show_aliases = "TRUE" if guardium_show_aliases in ["Default", "On"] else "FALSE"

            guardium_remote_data_source = kwargs.get("guardium_remote_data_source")  # text
            guardium_remote_data_source = "" if guardium_remote_data_source == "Default" else guardium_remote_data_source

            guardium_parameter_label = kwargs.get("guardium_parameter_label")  # text
            guardium_parameter_value = kwargs.get("guardium_parameter_value")  # text
            guardium_fetchsize = kwargs.get("guardium_fetchsize")  # number

            guardium_sortcolumn = kwargs.get("guardium_sortcolumn")  # text
            guardium_sortcolumn = "" if not guardium_sortcolumn else guardium_sortcolumn

            guardium_sorttype = kwargs.get("guardium_sorttype")  # text
            if guardium_sorttype:
                if guardium_sorttype == "ascending":
                    guardium_sorttype = "asc"
                else:
                    guardium_sorttype = "desc"
            else:
                guardium_sorttype = ""

            incident_id = kwargs.get("grd_resilient_incident_id")  # Incident Number
            table_id = self.options.get('search_table')

            log = logging.getLogger(__name__)
            log.info(u"Guardium report: %s", guardium_report)
            log.info(u"Guardium period from: %s", guardium_period_from)
            log.info(u"Guardium period to: %s", guardium_period_to)
            log.info(u"Guardium show aliases: %s", guardium_show_aliases)
            log.info(u"Guardium remote data source: %s", guardium_remote_data_source)
            log.info(u"Guardium parameter label: %s", guardium_parameter_label)
            log.info(u"Guardium parameter value: %s", guardium_parameter_value)
            log.info(u"Guardium fetchsize: %s", guardium_fetchsize)
            log.info(u"Guardium sortcolumn: %s", guardium_sortcolumn)
            log.info(u"Guardium sorttype: %s", guardium_sorttype)
            log.info(u"Incident Number: %s", incident_id)

            if not resilient_object.client_secret:
                raise ValueError(u"Guardium client secret not generated, please run `Generate Guardium Client Secret`")

            yield StatusMessage(u"Started searching report: {}".format(guardium_report))
            res = grd_rest_object.create_online_report(guardium_report, guardium_fetchsize,
                                                       period_from=guardium_period_from, period_to=guardium_period_to,
                                                       show_aliases=guardium_show_aliases,
                                                       remote_data_source=guardium_remote_data_source,
                                                       param_label=guardium_parameter_label,
                                                       param_value=guardium_parameter_value,
                                                       sortcolumn=guardium_sortcolumn, sorttype=guardium_sorttype)
            # Updating search table
            update_search_to_table(resilient_object, table_id, incident_id, res, guardium_report)
            msg = u"Completed searching report: {}".format(guardium_report)
            yield StatusMessage(msg)

            results = {
                "content": msg
            }
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as er_msg:
            yield FunctionError(er_msg)
