# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
"""Function implementation"""

import ast
import logging
import sys
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult
from resilient_lib import ResultPayload, str_to_bool
from rc_data_feed.lib.rest_client_helper import RestClientHelper
from rc_data_feed.components.threadpool import PluginPool
from .feed_ingest import Reload

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'data_feeder_sync_incidents"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("feeds", {})
        self.opts = opts

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("feeds", {})
        self.opts = opts

    @function("data_feeder_sync_incidents")
    def _data_feeder_sync_incidents_function(self, event, *args, **kwargs):
        """Function: Synchronize Incident(s) and their associated tasks, notes, attachments, artifacts, milestones and associated datatables"""
        try:
            result = ResultPayload("data_feeder", **kwargs)

            # Get the function parameters:
            df_min_incident_id = kwargs.get("df_min_incident_id")  # number
            df_max_incident_id = kwargs.get("df_max_incident_id", df_min_incident_id)  # number
            df_query_api_method = kwargs.get("df_query_api_method", False) # boolean

            log = logging.getLogger(__name__)
            log.info("df_min_incident_id: %s", df_min_incident_id)
            log.info("df_max_incident_id: %s", df_max_incident_id)

            # collect the workflow/playbook instance id
            workflow_id = event.message['workflow_instance'].get('workflow_instance_id')

            if not df_max_incident_id:
                df_max_incident_id = df_min_incident_id

            if df_min_incident_id > df_max_incident_id:
                raise ValueError("Min value {} greater than max value {}".format(df_min_incident_id, df_max_incident_id))

            # select all incidents as max
            if df_max_incident_id == 0:
                df_max_incident_id = sys.maxsize

            yield StatusMessage("starting...")
            rest_client_helper = RestClientHelper(self.rest_client)

            # build the list workspaces to plugin, if present
            self.workspaces = ast.literal_eval("{{ {} }}".format(self.options.get("workspaces", "")))

            # expose attachment content setting
            self.incl_attachment_data = str_to_bool(self.options.get("include_attachment_data", 'false'))

            plugin_pool = PluginPool.get_instance(rest_client_helper,
                                                  int(self.opts.get("resilient", {}).get("num_workers", 0)),
                                                  self.options.get("feed_names", None),
                                                  self.opts,
                                                  self.workspaces)

            df = Reload(plugin_pool,
                        [ type.strip() for type in self.options.get("reload_types", "").split(",") \
                            if type ],
                        query_api_method=df_query_api_method,
                        incl_attachment_data=self.incl_attachment_data,
                        workflow_id=workflow_id)
            reloaded_incidents = df.reload_all(min_inc_id=df_min_incident_id, max_inc_id=df_max_incident_id)

            result_payload = result.done(True, {"num_of_sync_incidents": reloaded_incidents})

            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(result_payload)
        except Exception as err:
            result_payload = result.done(False, {}, str(err))
            yield FunctionResult(result_payload)
