# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_mcafee_tie
"""

import logging
from fn_mcafee_tie.lib.mcafee_tie_common import get_mcafee_client, get_tie_client, PACKAGE_NAME

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):

    options = opts.get(PACKAGE_NAME, {})

    try:
        dxlclient = get_mcafee_client(options)
        tie_client = get_tie_client(dxlclient)
        if dxlclient.connected and tie_client:
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
               'reason': str(exc)
               }
