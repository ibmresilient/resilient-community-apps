# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import os
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, str_to_bool
from fn_netdevice.lib.netmiko import execute


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'network_device_locker"""

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
        template_dir = self.options.get("template_dir")
        if template_dir:
            if not os.path.isdir(template_dir):
                raise ValueError("Template directory not found %s", template_dir)

            os.environ["NET_TEXTFSM"] = template_dir

    @function("fn_netdevice")
    def _network_device_function(self, event, *args, **kwargs):
        """Function: function to connect with firewalls via ssh to retrieve stats or to perform configuration changes.
         This integration uses the netMiko library to access the hosts.
        """
        try:
            # Get the function parameters:
            netdevice_ids = kwargs.get("netdevice_ids")  # text
            netdevice_cmd = kwargs.get("netdevice_send_cmd")  # text
            netdevice_config = kwargs.get("netdevice_config_cmd")  # text
            use_textfsm = kwargs.get("netdevice_use_textfsm", False) # bool

            log = logging.getLogger(__name__)
            log.info("netdevice_ids: %s", netdevice_ids)
            log.info("netdevice_cmd: %s", netdevice_cmd)
            log.info("netdevice_config: %s", netdevice_config)
            log.info("netdevice_use_textfsm: %s", use_textfsm)

            if not netdevice_cmd and not netdevice_config:
                raise ValueError("Specify at least netdevice_send_cmd or netdevice_config_cmd")

            yield StatusMessage("starting...")

            result_payload = ResultPayload(FunctionComponent.SECTION_HDR, **kwargs)

            result = {}
            for device_id in netdevice_ids.split(','):

                # find the access information
                device_info = self.opts.get(device_id.strip(), None)
                if not device_info:
                    msg = u"Unable to find section for {}".format(device_id)
                    result[device_id] = {
                        "status": 'failure',
                        "reason": msg
                    }

                    log.warning(msg)
                    yield StatusMessage(msg)
                    continue

                device_commit = str_to_bool(device_info.pop('use_commit', 'False'))

                result[device_id] = execute(device_info, netdevice_cmd, netdevice_config, device_commit, use_textfsm)

            status = result_payload.done(True, result)

            yield StatusMessage("done")

            # Produce a FunctionResult with the results
            yield FunctionResult(status)
        except Exception:
            yield FunctionError()
