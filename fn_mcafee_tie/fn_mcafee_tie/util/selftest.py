# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_mcafee_tie
"""

import logging
from dxlclient.client_config import DxlClientConfig
from dxlclient.client import DxlClient
from dxltieclient import TieClient

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

CONFIG_DATA_SECTION='fn_mcafee_tie'

def selftest_function(opts):

    options = opts.get(CONFIG_DATA_SECTION, {})

    try:
        try:
            config_file = options.get("dxlclient_config")
            if config_file is None:
                log.error("dxlclient_config is not set. You must set this path to run this function")
                raise ValueError("dxlclient_config is not set. You must set this path to run this function")

            # Create configuration from file for DxlClient
            dxlclient_config = DxlClientConfig.create_dxl_config_from_file(config_file)
        except AttributeError:
            log.error("There is no [fn_mcafee_tie] section in the config file, "
                      "please set that by running resilient-circuits config -u")
            raise AttributeError("[fn_mcafee_tie] section is not set in the config file")

        dxlclient = DxlClient(dxlclient_config)
        dxlclient.connect()
        tie_client = TieClient(dxlclient)
        if dxlclient.connected and tie_client:
            state = 'success'
            reason = 'success'
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

