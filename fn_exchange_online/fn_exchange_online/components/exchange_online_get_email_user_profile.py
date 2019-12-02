# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import json
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, RequestsCommon, ResultPayload
from fn_exchange_online.lib.ms_graph_helper import MSGraphHelper

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

        # Get proxies if defined
        rc = RequestsCommon(self.opts, self.options)
        proxies = rc.get_proxies()

        # Get the MS Graph helper class
        self.MS_graph_helper = MSGraphHelper(self.options.get("microsoft_graph_url"),
                                             self.options.get("tenant_id"),
                                             self.options.get("client_id"),
                                             self.options.get("client_secret",
                                             proxies))
    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        # Get proxies if defined
        rc = RequestsCommon(self.opts, self.options)
        proxies = rc.get_proxies()

        # Get the MS Graph helper class
        self.MS_graph_helper = MSGraphHelper(self.options.get("microsoft_graph_url"),
                                             self.options.get("tenant_id"),
                                             self.options.get("client_id"),
                                             self.options.get("client_secret",
                                             proxies))

    @function("exchange_online_get_email_user_profile")
    def _exchange_online_get_email_user_profile_function(self, event, *args, **kwargs):
        """Function: This function will get Exchange Online user profile for a given email address."""
        try:
            log = logging.getLogger(__name__)

            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters
            email_address = kwargs.get("exo_email_address")  # text

            if not email_address:
                raise ValueError("Exchange Online Get User Profile: email address must be specified.")
            else:
                log.info("Exchange Online get user profile exo_email_address: %s", email_address)

            # Call MS Graph API to get the user profile
            response = self.MS_graph_helper.get_user_profile(email_address)

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
            log.error(err)
            yield FunctionError()