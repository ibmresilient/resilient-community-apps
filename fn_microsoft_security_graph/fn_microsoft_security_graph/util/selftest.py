# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_microsoft_security_graph
"""

import logging
from resilient_lib.components.integration_errors import IntegrationError
from fn_microsoft_security_graph.lib.ms_graph_helper import connect_MSGraph

CONFIG_DATA_SECTION = 'fn_microsoft_security_graph'
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    # Get app.config parameters.
    options = opts.get(CONFIG_DATA_SECTION, {})

    try:
        log.info(u'Calling MS Graph API with: \n token_url: %s', options['microsoft_graph_token_url'])
        log.info(u'MS Graph API url: %s', options['microsoft_graph_url'])
        log.info(u'tenant_id: %s', options['tenant_id'])
        log.info(u'client_id: %s', options['client_id'])

        state, reason = "", ""

        # Create MSGraphHelper class object
        ms_graph_helper = connect_MSGraph(opts)

        # Get a MS Graph session token
        session_token = ms_graph_helper.authenticate()

        if ms_graph_helper and session_token:
            state = "success"
        else:
            state = "failure"
            reason = "authenication failed"
    except IntegrationError as err:
        state = "failure"
        reason = err.value

    result = {
        "state": state,
        "reason": reason
    }

    log.info(result)
    return result
