# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import RequestsCommon, ResultPayload, validate_fields
from fn_ansible_tower.lib.common import SECTION_HDR, TOWER_API_BASE, JSON_HEADERS, get_common_request_items, clean_url

AD_HOC_URL = 'ad_hoc_commands/'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'ansible_tower_run_an_ad_hoc_command"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(SECTION_HDR, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(SECTION_HDR, {})

    @function("ansible_tower_run_an_ad_hoc_command")
    def _ansible_tower_list_job_templates_function(self, event, *args, **kwargs):
        """Function: Run an ansible module outside of the job template"""
        try:
            validate_fields(("url"), self.options) # validate key app.config settings

            # Get the function parameters:
            tower_hosts = kwargs.get("tower_hosts")  # text
            tower_module = self.get_select_param(kwargs.get("tower_module"))  # text
            tower_arguments = kwargs.get("tower_arguments")  # text
            tower_inventory = kwargs.get("tower_inventory") # number
            tower_credential = kwargs.get("tower_credential") # number

            log = logging.getLogger(__name__)
            log.info("tower_hosts: %s", tower_hosts)
            log.info("tower_module: %s", tower_module)
            log.info("tower_arguments: %s", tower_arguments)
            log.info("tower_inventory: %s", tower_inventory)
            log.info("tower_credential: %s", tower_credential)

            result = ResultPayload(SECTION_HDR, **kwargs)
            rc = RequestsCommon(self.opts, self.options)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            url = "/".join((clean_url(self.options['url']), TOWER_API_BASE, AD_HOC_URL))
            # common
            basic_auth, cafile = get_common_request_items(self.options)

            arguments = {
                "module_name": tower_module,
                "limit": tower_hosts,
                "module_args": tower_arguments,
                "inventory": tower_inventory,
                "credential": tower_credential
            }

            rc = RequestsCommon(self.opts, self.options)
            results = rc.execute_call_v2("post", url, auth=basic_auth,
                                         json=arguments, headers=JSON_HEADERS,
                                         verify=cafile)

            result_payload = result.done(True, results.json())
            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(result_payload)
        except Exception:
            yield FunctionError()
