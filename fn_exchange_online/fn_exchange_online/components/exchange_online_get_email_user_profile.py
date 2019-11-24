# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import json
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, RequestsCommon, ResultPayload, OAuth2ClientCredentialsSession
import time

CONFIG_DATA_SECTION = 'fn_exchange_online'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'exchange_online_get_email_user_profile"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

        # Get app.config parameters.
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        # Validate required fields in app.config are set
        required_fields = ["microsoft_graph_url", "tenant_id", "client_id", "client_secret"]
        validate_fields(required_fields, self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @function("exchange_online_get_email_user_profile")
    def _exchange_online_get_email_user_profile_function(self, event, *args, **kwargs):
        """Function: This function will get Exchange Online user profile for a given email address."""
        try:
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)
            rc = RequestsCommon(self.opts, self.options)

            # Get the function parameters:
            email_address = kwargs.get("exo_email_address")  # text

            if not email_address:
                raise ValueError("Exchange Online get user profile: email address must be specified.")

            log = logging.getLogger(__name__)
            log.info("exo_email_address: %s", email_address)

            # Authenticate and get oauth2 token for the session.
            token_url = u'https://login.microsoftonline.com/{0}/oauth2/v2.0/token'.format(self.options['tenant_id'])
            graph_session = OAuth2ClientCredentialsSession(token_url,
                                                           client_id=self.options['client_id'],
                                                           client_secret=self.options['client_secret'],
                                                           scope=['.default'],
                                                           proxies=rc.get_proxies())

            # Query the MS Graph user profile endpoint.
            ms_graph_url = u'{0}/users/{1}'.format(self.options['microsoft_graph_url'], email_address)
            response = graph_session.get(ms_graph_url)

            if response.status_code >= 300 and response.status_code != 404 :
                raise FunctionError("Invalid response from Microsoft Graph")

            response_json = response.json()
            results = rp.done(True, response_json)

            # Add pretty printed string for easier to read output text in note.
            pretty_string = json.dumps(response_json, sort_keys=True, indent=4, separators=(',', ': '))
            results['pretty_string'] = pretty_string

            yield StatusMessage("Returning Exchange Online user profile results")

            log.debug(json.dumps(results['content']))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionError()