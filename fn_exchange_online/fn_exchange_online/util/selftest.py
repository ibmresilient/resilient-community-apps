# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_exchange_online
"""

import logging
from resilient_lib import RequestsCommon, validate_fields
from resilient_lib.components.integration_errors import IntegrationError
from fn_exchange_online.lib.ms_graph_helper import MSGraphHelper

CONFIG_DATA_SECTION = 'fn_exchange_online'
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

    validate_fields(['microsoft_graph_token_url', 'microsoft_graph_url', 'tenant_id',
                     'client_id', 'client_secret'], options)

    # Read configuration settings:
    token_url = options['microsoft_graph_token_url']
    graph_url = options['microsoft_graph_url']
    tenant_id = options['tenant_id']
    client_id = options['client_id']
    client_secret = options['client_secret']

    try:
        log.info(
            u'Calling MS Graph API with: \n token_url: ' + token_url + u'\n MS Graph API url: ' + graph_url +
            u'\n tenant_id: ' + tenant_id + u'\n client_id: ' + client_id)

        state, reason = "", ""

        # Create MSGraphHelper class object
        ms_graph_helper = MSGraphHelper(token_url,
                                        graph_url,
                                        tenant_id,
                                        client_id,
                                        client_secret,
                                        RequestsCommon(opts, options).get_proxies())

        # Get a MS Graph session token
        session_token = ms_graph_helper.authenticate()

        if ms_graph_helper and session_token:
            state = "success"
        else:
            state = "failure"
            reason = "N/A"
    except IntegrationError as err:
        state = "failure"
        reason = err.value

    result = {
        "state": state,
        "reason": reason
    }

    log.info(result)
    return result