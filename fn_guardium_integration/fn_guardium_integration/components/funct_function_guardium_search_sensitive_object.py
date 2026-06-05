# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

"""Function implementation"""
import time
import logging
import re
from datetime import datetime
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_guardium_integration.lib.grd_rest_endpoints_service import GrdRestEndpoint
from fn_guardium_integration.lib.resilient_rest_services import ResilientRestService
from fn_guardium_integration.util.process_sensitive_objects import update_sensitive_object_table
from fn_guardium_integration.util.static_data import SEARCH_TIME_FORMAT
from resilient_lib import validate_fields


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'function_guardium_search_sensitive_object"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts_data = opts
        self.options = opts.get("fn_guardium_integration", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_guardium_integration", {})

    @function("function_guardium_search_sensitive_object")
    def _function_guardium_search_sensitive_object_function(self, event, *args, **kwargs):
        """Function: A function Search for Sensitive objects."""
        try:
            # Get the function parameters:
            guardium_period_from = kwargs.get("guardium_period_from")  # datetimepicker
            guardium_period_to = kwargs.get("guardium_period_to")  #
            # converting to date and time
            guardium_period_from = datetime.fromtimestamp(guardium_period_from / 1000).strftime(SEARCH_TIME_FORMAT)
            guardium_period_to = datetime.fromtimestamp(guardium_period_to / 1000).strftime(SEARCH_TIME_FORMAT)

            search_username = kwargs.get("grd_search_username")  # text
            search_ip_address = kwargs.get("grd_search_ip_address")  # text
            incident_id = kwargs.get('grd_resilient_incident_id')  # number

            # Validating Mandatory app.config param
            validate_fields(["sensitive_table"], self.options)

            sensitive_table_id = self.options.get('sensitive_table')

            log = logging.getLogger(__name__)
            log.info(u"Guardium period from: %s", guardium_period_from)
            log.info(u"Guardium period to: %s", guardium_period_to)
            log.info(u"search username: %s", search_username)
            log.info(u"search ip address: %s", search_ip_address)

            yield StatusMessage(u"Starting to Search for Sensitive objects")
            resilient_object = ResilientRestService(self.opts_data, self.options, log)
            grd_rest_object = GrdRestEndpoint(self.options, resilient_object.client_secret, resilient_object.unique_id,
                                              log)
            if not resilient_object.client_secret:
                raise ValueError(u"Guardium client secret not generated, please run `Generate Guardium Client Secret`")

            # Getting sensitive object group members
            grp_members_data = grd_rest_object.group_members_by_group_desc(group_desc="Sensitive Objects")
            gr_member = [x.get("member") for x in grp_members_data.get("group_members")]

            # Grouping with 100's
            final_gr_member = []
            _tmp_list = []
            for x in gr_member:
                _tmp_list.append(x)
                if len(_tmp_list) > 100:
                    final_gr_member.append(_tmp_list)
                    _tmp_list = []
            if _tmp_list:
                final_gr_member.append(_tmp_list)

            # Preparing username ip search combination
            query_param = []
            for p in [search_username, search_ip_address]:
                if p and p != "N/A" and p != "N\\A":
                    query_param.append(p)
            query_string = " AND ".join(query_param)

            search_results_list = []
            for gr_member in final_gr_member:
                grp_condition = " OR ".join(gr_member)
                grp_condition = re.sub("%", "", grp_condition)

                if query_string:
                    final_query = "({} AND ({}))".format(query_string, grp_condition)
                else:
                    final_query = "({})".format(grp_condition)

                search_result = grd_rest_object.grd_search(query="{}".format(final_query), with_facets=1,
                                                           category="ACCESS", start_time=guardium_period_from,
                                                           end_time=guardium_period_to)
                search_results_list.append(search_result)
                time.sleep(10)
            # Updating the sensitive object table with returned search results.
            update_sensitive_object_table(resilient_object, table_id=sensitive_table_id, inc_id=incident_id,
                                          search_data=search_results_list)

            msg = u"Completed - Searching for Sensitive objects."

            yield StatusMessage(msg)

            results = {
                "content": msg
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as er_msg:
            yield FunctionError(er_msg)
