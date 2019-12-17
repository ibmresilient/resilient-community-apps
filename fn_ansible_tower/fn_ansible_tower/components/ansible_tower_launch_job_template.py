# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import RequestsCommon, ResultPayload, validate_fields
from fn_ansible_tower.lib.common import get_job_template_by_name, SECTION_HDR, TOWER_API_BASE, JSON_HEADERS, make_extra_vars, \
    get_common_request_items

LAUNCH_URL = "job_templates/{id}/launch/"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'ansible_tower_launch_job_template"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(SECTION_HDR, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(SECTION_HDR, {})

    @function("ansible_tower_launch_job_template")
    def _ansible_tower_launch_job_template_function(self, event, *args, **kwargs):
        """Function: None"""
        try:
            validate_fields(("url"), self.options) # validate key app.config settings

            # Get the function parameters:
            tower_template_id = kwargs.get('tower_template_id') # number
            tower_template_name = kwargs.get('tower_template_name') # text
            tower_template_hosts = kwargs.get('tower_hosts') # text
            tower_template_run_tags = kwargs.get('tower_run_tags') # text
            tower_template_skip_tags = kwargs.get('tower_skip_tags') # text
            tower_template_arguments = kwargs.get('tower_arguments') # text

            log = logging.getLogger(__name__)
            log.info("tower_template_id: %s", tower_template_id)
            log.info("tower_template_name: %s", tower_template_name)
            log.info("tower_hosts: %s", tower_template_hosts)
            log.info("tower_arguments: %s", tower_template_arguments)
            log.info("tower_run_tags: %s", tower_template_run_tags)
            log.info("tower_skip_tags: %s", tower_template_skip_tags)

            result = ResultPayload(SECTION_HDR, **kwargs)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")
            if tower_template_id is None:
                if not tower_template_name:
                    raise ValueError("Specify either tower_template_id or tower_template_name")

                json_template = get_job_template_by_name(self.opts, self.options, tower_template_name)
                if not json_template:
                    raise KeyError(u"Unable to find job template: %s", tower_template_name)

                tower_template_id = json_template['id']

            tower_result = run_job_template(self.opts, self.options, tower_template_id,
                                            tower_template_hosts, tower_template_arguments,
                                            tower_template_run_tags, tower_template_skip_tags)

            result_payload = result.done(True, tower_result)
            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(result_payload)
        except Exception:
            yield FunctionError()

def run_job_template(opts, options, tower_template_id,
                     tower_template_hosts, tower_template_arguments,
                     tower_template_run_tags, tower_template_skip_tags):
    """
    invoke the call to launch a job
    :param opts: full set of app.config settings
    :param options: specific settings for ansible tower
    :param tower_template_id:
    :param tower_teemplate_hosts
    :param tower_template_arguments:
    :param tower_template_run_tags:
    :param tower_template_skip_tags:
    :return: json formatted job launch details
    """
    log = logging.getLogger(__name__)
    rc = RequestsCommon(opts, options)

    url = "/".join((options.get('url'), TOWER_API_BASE, LAUNCH_URL.format(id=tower_template_id)))

    arguments = {}
    if tower_template_arguments:
        arguments['extra_vars'] = make_extra_vars(tower_template_arguments)

    if tower_template_run_tags:
        arguments['job_tags'] = tower_template_run_tags

    if tower_template_skip_tags:
        arguments['skip_tags'] = tower_template_skip_tags

    if tower_template_hosts:
        arguments['limit'] = tower_template_hosts

    log.debug("Arguments: %s", arguments)

    # common
    basic_auth, cafile = get_common_request_items(options)
    tower_result = rc.execute_call_v2("post", url, auth=basic_auth,
                                      json=arguments, headers=JSON_HEADERS,
                                      verify=cafile)
    return tower_result.json()
