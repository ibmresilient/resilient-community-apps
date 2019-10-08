# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2019. All Rights Reserved.

import logging
from requests.auth import HTTPBasicAuth
from six import string_types
from requests.exceptions import HTTPError
from resilient_lib.components.integration_errors import IntegrationError
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

log = logging.getLogger(__name__)


def get_threat_list(rc, options, lastupdate, bundle):
    base_url = options['base_url']
    username = options['username']
    password = options['password']
    basic_auth = HTTPBasicAuth(username, password)
    url = '{0}/siem/all?format=JSON'.format(base_url)  # /v2/siem/all Fetch events for all clicks and messages relating to known threats within the specified time period

    if isinstance(lastupdate, string_types):
        url += '&sinceTime={}'.format(lastupdate)
    else:
        if lastupdate is None:
            # first run, fetch for time span equivalent to polling interval
            lastupdate = int(options['polling_interval']) * 60
        url += '&sinceSeconds={}'.format(lastupdate)

    res = rc.execute_call_v2('get', url, auth=basic_auth, verify=bundle, proxies=rc.get_proxies())

    # Debug logging
    log.debug("Response content: {}".format(res.content))
    return res.json()


def custom_response_err_msg(response):
    """
    Custom handler for response handling.
    :param response:
    :return: response
    """
    try:
        # Raise error is bad status code is returned
        response.raise_for_status()

        # Return requests.Response object
        return response

    except Exception as err:
        msg = str(err)

        if isinstance(err, HTTPError) and response.status_code == 404:
            msg = response.content + " please make sure you are invoking the appropriate Rule for chosen Artifact"

        log and log.error(msg)
        raise IntegrationError(msg)

