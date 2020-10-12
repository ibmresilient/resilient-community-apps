# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Function implementation"""

import logging
from fn_mcafee_epo.lib.epo_helper import init_client, get_list
from resilient_lib import ResultPayload, validate_fields
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

LOG = logging.getLogger(__name__)
PACKAGE_NAME = "fn_mcafee_epo"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_epo_remove_tag''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    @function("mcafee_epo_remove_tag")
    def _mcafee_epo_remove_tag_function(self, event, *args, **kwargs):
        """
        Function: A function which takes two inputs:

        mcafee_epo_system: Comma separated list of Hostnames/IpAddress. These systems must be managed on ePO.
        mcafee_epo_tag: A Tag managed on ePO.

        Applies tag to the systems in ePO.
        """
        try:
            yield StatusMessage("Starting...")

            # Get the function parameters:
            validate_fields(["mcafee_epo_systems", "mcafee_epo_tag"], kwargs)
            mcafee_epo_systems = kwargs.get("mcafee_epo_systems")  # text
            mcafee_epo_tag = self.get_select_param(kwargs.get("mcafee_epo_tag"))  # text, or multi-select

            LOG.info("mcafee_epo_systems: %s", mcafee_epo_systems)
            LOG.info("mcafee_epo_tag: %s", mcafee_epo_tag)

            # determine if a list of tags was given
            tag_list = get_list(mcafee_epo_tag)

            rc = ResultPayload(PACKAGE_NAME, **kwargs)
            client = init_client(self.opts, self.options)

            for tag in tag_list:
                params = {
                    "names": mcafee_epo_systems.strip(),
                    "tagName": tag
                }
                response = client.request("system.clearTag", params)

            yield StatusMessage("Finished")

            results = rc.done(True, response)

            yield StatusMessage("Tag Applied...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            LOG.error(e)
            yield FunctionError(e)
