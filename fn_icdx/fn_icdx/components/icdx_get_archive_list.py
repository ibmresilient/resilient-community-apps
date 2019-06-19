# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_icdx.util.helper import ICDXHelper
from fn_icdx.util.amqp_facade import AmqpFacade

GET_ARCHIVE_LIST_CODE = 12


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'icdx_get_archive_list"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_icdx", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_icdx", {})

    @function("icdx_get_archive_list")
    def _icdx_get_archive_list_function(self, event, *args, **kwargs):
        """Function: The Get Archive List API is used to return a list of archives in the ICDx system. The response is an unsorted list of archive metadata objects which can then be searched by a user."""

        log = logging.getLogger(__name__)
        try:
            helper = ICDXHelper(self.options)
            yield StatusMessage("Attempting to gather config and setup the AMQP Client")
            try:
                # Initialise the AmqpFacade, pass in config values
                amqp_client = AmqpFacade(host=helper.get_config_option("icdx_amqp_host"),
                                         port=helper.get_config_option("icdx_amqp_port", True),
                                         virtual_host=helper.get_config_option("icdx_amqp_vhost"),
                                         username=helper.get_config_option("icdx_amqp_username"),
                                         amqp_password=helper.get_config_option("icdx_amqp_password")
                                         )

                yield StatusMessage("Config options gathered and AMQP client setup.")
            except Exception:
                raise FunctionError("Encountered error while initialising the AMQP Client")
            # Prepare request payload
            request = {
                "id": GET_ARCHIVE_LIST_CODE
            }

            # Make the call to ICDx and get a handle on any results
            archives, status = amqp_client.call(json.dumps(request))

            yield StatusMessage("ICDX call complete with status: {}".format(status))

            # If status code in the message header is 200 we have results, 204 is empty response.
            results = {
                "success": (False if status != 200 else True),
                "archives": (json.loads(archives) if archives is not None else None)
            }
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
            log.info("Complete")
        except Exception:
            yield FunctionError()
