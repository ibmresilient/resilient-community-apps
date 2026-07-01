# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_mcafee_tie
"""

import logging
from dxlclient.client_config import DxlClientConfig
from dxlclient.client import DxlClient

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

PACKAGE_NAME='fn_mcafee_opendxl'

def selftest_function(opts):

    options = opts.get(PACKAGE_NAME, {})

    try:
        try:
            config_file = options.get("dxlclient_config")
            if config_file is None:
                log.error("dxlclient_config is not set. You must set this path to run this function")
                raise ValueError("dxlclient_config is not set. You must set this path to run this function")

            # Create configuration from file for DxlClient
            dxlclient_config = DxlClientConfig.create_dxl_config_from_file(config_file)
        except AttributeError:
            log.error("There is no [fn_mcafee_opendxl] section in the config file, "
                      "please set that by running resilient-circuits config -u")
            raise AttributeError("[fn_mcafee_open] section is not set in the config file")

        dxlclient = DxlClient(dxlclient_config)
        dxlclient.connect()
        if dxlclient.connected:
            state = 'success'
            reason = None
        else:
            state = 'failure'
            reason = 'authorization failure'

        return {
               'state': state,
               'reason': reason
                }

    except Exception as exc:
        return {
               'state': 'failure',
               'reason': exc
               }