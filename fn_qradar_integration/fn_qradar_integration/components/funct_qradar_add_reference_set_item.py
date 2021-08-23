# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
#
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from fn_qradar_integration.components.funct_qradar_get_all_reference_tables import PACKAGE_NAME
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields
from fn_qradar_integration.util.qradar_utils import QRadarClient
from fn_qradar_integration.lib.functions_common import QRadarServers

PACKAGE_NAME = "fn_qradar_integration"

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_add_reference_set_item"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.servers_list = {}

        options = opts.get(PACKAGE_NAME, {})

        if options:
            server_list = {PACKAGE_NAME}
        else:
            servers = QRadarServers(opts, options)
            server_list = servers.get_server_name_list()

        for server_name in server_list:
            self.servers_list[server_name] = opts.get(server_name, {})
            options = self.servers_list[server_name]

            required_fields = ["host", "verify_cert"]
            validate_fields(required_fields, options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.servers_list = {}

        options = opts.get(PACKAGE_NAME, {})

        if options:
            server_list = {PACKAGE_NAME}
        else:
            servers = QRadarServers(opts, options)
            server_list = servers.get_server_name_list()

        for server_name in server_list:
            self.servers_list[server_name] = opts.get(server_name, {})

    @function("qradar_add_reference_set_item")
    def _qradar_add_reference_set_item_function(self, event, *args, **kwargs):
        """Function: Add an item to the given QRadar reference set"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in, if not found return a backup string
            wf_instance_id = event.message.get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")

            yield StatusMessage("Starting 'qradar_add_reference_set_item' that was running in workflow '{0}'".format(wf_instance_id))

            required_fields = ["qradar_reference_set_name", "qradar_reference_set_item_value"]
            validate_fields(required_fields, kwargs)
            # Get the function parameters:
            qradar_reference_set_name = kwargs.get("qradar_reference_set_name")  # text
            qradar_reference_set_item_value = kwargs.get("qradar_reference_set_item_value")  # text

            LOG.info("qradar_reference_set_name: %s", qradar_reference_set_name)
            LOG.info("qradar_reference_set_item_value: %s", qradar_reference_set_item_value)

            qradar_label = kwargs.get("qradar_label")
            if qradar_label and PACKAGE_NAME+":"+qradar_label in self.servers_list:
                options = self.servers_list[PACKAGE_NAME+":"+qradar_label]
            elif len(self.servers_list) == 1 or qradar_label == PACKAGE_NAME:
                for server_name in self.servers_list:
                    options = self.servers_list[server_name]
            else:
                raise Exception("{} did not match labels given in the app.config".format(qradar_label))

            qradar_verify_cert = True
            if "verify_cert" in options and options["verify_cert"].lower() == "false":
                qradar_verify_cert = False

            LOG.debug("Connection to {} using {}".format(options["host"],
                                                         options.get("username") or "service token"))

            qradar_client = QRadarClient(host=options["host"],
                                         username=options.get("username", None),
                                         password=options.get("qradarpassword", None),
                                         token=options.get("qradartoken", None),
                                         cafile=qradar_verify_cert,
                                         opts=self.opts, function_opts=options)

            result = qradar_client.add_ref_element(qradar_reference_set_name,
                                                   qradar_reference_set_item_value)

            result["inputs"] = {
                "qradar_label": qradar_label,
                "qradar_reference_set_name": qradar_reference_set_name,
                "qradar_reference_set_item_value": qradar_reference_set_item_value
            }

            yield StatusMessage("Finished 'qradar_add_reference_set_item' that was running in workflow '{0}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(result)
        except Exception as e:
            LOG.error(str(e))
            yield FunctionError()
