# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2026. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
"""AppFunction implementation"""

import ast
import logging
import sys
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import str_to_bool
from rc_data_feed.lib.rest_client_helper import RestClientHelper
from rc_data_feed.components.threadpool import PluginPool
from .feed_ingest import Reload

PACKAGE_NAME = "rc_data_feed"
FN_NAME = "data_feeder_sync_incidents"

LOG = logging.getLogger(__name__)


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'data_feeder_sync_incidents'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Synchronize Incident(s) and their associated tasks, notes,
        attachments, artifacts, milestones and associated datatables"""
        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        try:
            # Get the function parameters:
            df_min_incident_id = fn_inputs.df_min_incident_id  # number
            df_max_incident_id = getattr(fn_inputs, "df_max_incident_id", df_min_incident_id) or df_min_incident_id  # number
            df_query_api_method = getattr(fn_inputs, "df_query_api_method", False)  # boolean

            LOG.info("df_min_incident_id: %s", df_min_incident_id)
            LOG.info("df_max_incident_id: %s", df_max_incident_id)

            if df_min_incident_id > df_max_incident_id:
                raise ValueError("Min value {} greater than max value {}".format(df_min_incident_id, df_max_incident_id))

            # select all incidents up to max if 0 given
            if df_max_incident_id == 0:
                df_max_incident_id = sys.maxsize

            yield self.status_message("Synchronizing incidents {} to {}...".format(df_min_incident_id, df_max_incident_id))

            rest_client_helper = RestClientHelper(self.rest_client)

            # app_configs is a dict (since resilient-circuits v49+)
            options = self.app_configs

            # build the list of workspaces to plugin, if present
            workspaces = ast.literal_eval("{{ {} }}".format(options.get("workspaces", "")))

            # expose attachment content setting
            incl_attachment_data = str_to_bool(options.get("include_attachment_data", "false"))

            plugin_pool = PluginPool.get_instance(rest_client_helper,
                                                  int(self.opts.get("resilient", {}).get("num_workers", 0)),
                                                  options,
                                                  self.opts,
                                                  workspaces)

            # collect the workflow/playbook instance id
            workflow_id = self.get_fn_msg().get("workflow_instance", {}).get("workflow_instance_id")

            df = Reload(plugin_pool,
                        [t.strip() for t in options.get("reload_types", "").split(",") if t],
                        query_api_method=df_query_api_method,
                        incl_attachment_data=incl_attachment_data,
                        workflow_id=workflow_id)

            reloaded_incidents = df.reload_all(min_inc_id=df_min_incident_id, max_inc_id=df_max_incident_id)

            yield self.status_message("Finished App Function: '{}'".format(FN_NAME))
            yield FunctionResult({"num_of_sync_incidents": reloaded_incidents})

        except Exception as error:
            yield FunctionResult({}, success=False, reason=str(error))
