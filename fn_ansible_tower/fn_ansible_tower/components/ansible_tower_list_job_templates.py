# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, \
                               StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_ansible_tower.lib.common import get_job_template_by_project, SECTION_HDR

LIST_URL = 'job_templates/'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'ansible_tower_list_job_templates"""

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

    @function("ansible_tower_list_job_templates")
    def _ansible_tower_list_job_templates_function(self, event, *args, **kwargs):
        """Function: List available job templates"""
        try:
            # validate key app.config settings
            validate_fields(("url"), self.options)

            # Get the function parameters:
            tower_project = kwargs.get("tower_project")  # text

            log = logging.getLogger(__name__)
            log.info("tower_project: %s", tower_project)

            result = ResultPayload(SECTION_HDR, **kwargs)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")
            json_templates = get_job_template_by_project(self.opts, self.options, tower_project)

            result_payload = result.done(True, json_templates)
            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(result_payload)
        except Exception:
            yield FunctionError()
