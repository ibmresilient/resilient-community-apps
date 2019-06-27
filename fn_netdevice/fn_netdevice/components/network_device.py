# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import os
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, str_to_bool
from fn_netdevice.lib.netmiko_core import execute


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn-netdevice"""

    SECTION_HDR = "fn_netdevice"

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(FunctionComponent.SECTION_HDR, {})

        self.init_function()

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(FunctionComponent.SECTION_HDR, {})

        self.init_function()

    def init_function(self):
        """
        configure the environment for netmiko
        """
        self.template_dir = self.options.get("template_dir")
        if self.template_dir:
            if not os.path.isdir(self.template_dir):
                raise ValueError("Template directory not found %s", self.template_dir)

            os.environ["NET_TEXTFSM"] = self.template_dir

    @function("fn_netdevice_query")
    def _network_device_query_function(self, event, *args, **kwargs):
        """Function: function to connect with firewalls via ssh to retrieve stats
         This integration uses the netMiko library to access the hosts.
        """
        try:
            # Get the function parameters:
            netdevice_ids = kwargs.get("netdevice_ids")  # text
            netdevice_cmd = kwargs.get("netdevice_send_cmd")  # text
            use_textfsm = str_to_bool(kwargs.get("netdevice_use_textfsm", 'False')) # bool

            log = logging.getLogger(__name__)
            log.info("netdevice_ids: %s", netdevice_ids)
            log.info("netdevice_cmd: %s", netdevice_cmd)
            log.info("netdevice_use_textfsm: %s", use_textfsm)

            if not netdevice_cmd:
                raise ValueError("Specify netdevice_send_cmd")

            if use_textfsm and not self.template_dir:
                raise ValueError("'netdevice_use_textfsm' set but no template directory is specified in app.config")

            yield StatusMessage("starting...")

            result_payload = ResultPayload(FunctionComponent.SECTION_HDR, **kwargs)

            rc, result = self._run_netdevice(netdevice_ids, netdevice_cmd, None, use_textfsm)
            status = result_payload.done(rc, result)

            yield StatusMessage("done")

            # Produce a FunctionResult with the results
            yield FunctionResult(status)
        except Exception:
            yield FunctionError()

    @function("fn_netdevice_config")
    def _network_device_config_function(self, event, *args, **kwargs):
        """Function: function to connect with firewalls via ssh to perform configuration changes.
         This integration uses the netMiko library to access the hosts.
        """
        try:
            # Get the function parameters:
            netdevice_ids = kwargs.get("netdevice_ids")  # text
            netdevice_config = kwargs.get("netdevice_config_cmd")  # text

            log = logging.getLogger(__name__)
            log.info("netdevice_ids: %s", netdevice_ids)
            log.info("netdevice_config: %s", netdevice_config)

            if not netdevice_config:
                raise ValueError("Specify netdevice_config_cmd")

            yield StatusMessage("starting...")

            result_payload = ResultPayload(FunctionComponent.SECTION_HDR, **kwargs)

            rc, result = self._run_netdevice(netdevice_ids, None, netdevice_config, False)

            status = result_payload.done(rc, result)

            yield StatusMessage("done")

            # Produce a FunctionResult with the results
            yield FunctionResult(status)
        except Exception:
            yield FunctionError()

    def _run_netdevice(self, netdevice_ids, netdevice_cmd, netdevice_config, use_textfsm):
        """
        Perform the netdevice execution
        :param netdevice_ids:
        :param netdevice_cmd:
        :param net_device_config:
        :param use_textfsm:
        :param kwargs:
        :return: json of status object
        """

        log = logging.getLogger(__name__)

        result = {}
        rc = True
        for device_id in netdevice_ids.split(','):

            # find the access information
            device_info = self.opts.get(device_id.strip(), None)
            if not device_info:
                msg = u"Unable to find section for '{}'".format(device_id)
                result[device_id] = {
                    "status": 'failure',
                    "reason": msg
                }
                rc = False

                log.warning(msg)
                continue

            device_commit = str_to_bool(device_info.pop('use_commit', 'False')) # pop
            result[device_id] = execute(device_info, netdevice_cmd, netdevice_config, device_commit, use_textfsm)

        return rc, result
