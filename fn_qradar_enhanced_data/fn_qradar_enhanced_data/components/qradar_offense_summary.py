# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2020. All Rights Reserved.
#
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import datetime
import logging
import fn_qradar_enhanced_data.util.qradar_constants as qradar_constants
from resilient_lib import validate_fields
from fn_qradar_enhanced_data.util.qradar_utils import QRadarClient
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


"""
    For a given Offense ID , get the offense summary.
"""


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_offense_summary"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get("fn_qradar_integration", {})
        required_fields = ["host", "verify_cert"]
        validate_fields(required_fields, self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get("fn_qradar_integration", {})

    @function("qradar_offense_summary")
    def _qradar_offense_summary(self, event, *args, **kwargs):
        """Function: QRadar Offense "summary"""
        log = logging.getLogger(__name__)
        try:
            required_fields = ["qradar_query_type","qradar_offense_id"]
            validate_fields(required_fields, kwargs)
            # Get the function parameters:
            qradar_offenseid = kwargs.get("qradar_offense_id")  # QRadar Offense ID
            qradar_fn_type = kwargs.get("qradar_query_type")  # Function type based on the datatable/fields to populate

            log.info("qradar_offenseid: %s", qradar_offenseid)

            qradar_verify_cert = True
            if "verify_cert" in self.options and self.options["verify_cert"].lower() == "false":
                qradar_verify_cert = False

            log.debug("Connection to {} using {}".format(self.options["host"],
                                                         self.options.get("username", None) or self.options.get("qradartoken", None) ))

            yield StatusMessage("starting...")
            qradar_client = QRadarClient(host=self.options["host"],
                                         username=self.options.get("username", None),
                                         password=self.options.get("qradarpassword", None),
                                         token=self.options.get("qradartoken", None),
                                         cafile=qradar_verify_cert,
                                         opts=self.opts, function_opts=self.options)

            results = {
                "qrhost": self.options["host"],
                "offenseid": qradar_offenseid
            }

            # Fetch the Offense Summary if function type is OFFENSE_SUMMARY
            if qradar_fn_type == qradar_constants.OFFENSE_SUMMARY:

                offense_summary = qradar_client.get_offense_summary_data(qradar_offenseid)
                results["offense"]= offense_summary["content"]

            # Fetch the Contributing Rules if function type is OFFENSE_RULES
            elif qradar_fn_type == qradar_constants.OFFENSE_RULES:

                rules_data = qradar_client.get_rules_data(qradar_offenseid)
                rules_data = rules_data["content"]["rules"]
                results["rules_data"]=rules_data

            # Fetch the Assets Info if function type is OFFENSE_ASSETS
            elif qradar_fn_type == qradar_constants.OFFENSE_ASSETS:

                # Get all sources for the given Offense ID
                offense_source = qradar_client.get_offense_source(qradar_offenseid)
                results["assets"]=[]

                # Get Asset Info for each source
                for source in offense_source["content"]:
                    offense_assets = qradar_client.get_offense_asset_data(source)["content"]

                    if offense_assets:
                        offense_assets["sourceip"] = source["sourceIp"]
                        # Sorting the asset users list based on the last seen time
                        offense_assets["users"].sort(key=lambda x:int(x["lastSeenProfiler"]),reverse=True)

                        # Get the Operating System ID for the Asset
                        asset_prop = list(filter(lambda x:x["propertyType"]["name"] == "Primary OS ID",
                                                 offense_assets["properties"]))
                        offense_assets["osid"] = asset_prop[0]["value"] if len(asset_prop)>0 else ""

                        # Get the Unified Name for the Asset
                        asset_prop = list(filter(lambda x: x["propertyType"]["name"] == "Unified Name",
                                                 offense_assets["properties"]))
                        offense_assets["name"] = asset_prop[0]["value"] if len(asset_prop) > 0 else ""
                        results["assets"].append(offense_assets)

            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            log.error(str(e))
            yield FunctionError()

