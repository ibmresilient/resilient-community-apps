# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_exchange_online
"""

import logging
from resilient_lib import RequestsCommon, validate_fields
from resilient_lib.components.integration_errors import IntegrationError
from fn_exchange_online.lib.ms_graph_helper import MSGraphHelper, MAX_RETRIES_TOTAL, MAX_RETRIES_BACKOFF_FACTOR

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
                     'client_id', 'client_secret', 'max_messages', 'max_users'], options)

    # Read configuration settings:
    token_url = options.get('microsoft_graph_token_url')
    graph_url = options.get('microsoft_graph_url')
    tenant_id = options.get('tenant_id')
    client_id = options.get('client_id')
    client_secret = options.get('client_secret')
    max_messages = int(options.get('max_messages'))
    max_users = int(options.get('max_users'))
    max_retries_total = int(options.get('max_retries_total', MAX_RETRIES_TOTAL))
    max_retries_backoff_factor = int(options.get('max_retries_backoff_factor', MAX_RETRIES_BACKOFF_FACTOR))
    try:
        log.info(u'Calling MS Graph API with: \n token_url: %s', token_url)
        log.info(u'MS Graph API url: %s',graph_url)
        log.info(u'tenant_id: %s', tenant_id)
        log.info(u'client_id: %s', client_id)
        log.info(u'max_messages: %s', str(max_messages))
        log.info(u'max_users: %s', str(max_users))
        log.info(u'max_retries_total: %s', str(max_retries_total))
        log.info(u'max_retries_backoff_factor: %s', str(max_retries_backoff_factor))

        state, reason = "", ""

        # Create MSGraphHelper class object
        ms_graph_helper = MSGraphHelper(token_url,
                                        graph_url,
                                        tenant_id,
                                        client_id,
                                        client_secret,
                                        max_messages,
                                        max_users,
                                        max_retries_total,
                                        max_retries_backoff_factor,
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