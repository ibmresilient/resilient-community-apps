# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Function implementation"""

import json
import logging
from fn_wiki.lib.wiki_common import WikiHelper
from resilient_circuits import ResilientComponent, handler, function, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload

PACKAGE_NAME = "fn_wiki"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_get_wiki_contents''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("fn_wiki_get_contents")
    def _fn_get_wiki_contents_function(self, event, *args, **kwargs):
        """Function: None"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            #wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]
            #yield StatusMessage("Starting 'fn_get_wiki_contents' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            wiki_contents_as_json = bool(kwargs.get("wiki_contents_as_json", False))  # boolean
            wiki_title_or_id = kwargs.get("wiki_title_or_id")  # text

            log = logging.getLogger(__name__)
            log.info("wiki_contents_as_json: %s", wiki_contents_as_json)
            log.info(u"wiki_title_or_id: %s", wiki_title_or_id)

            ##############################################
            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
            ##############################################
            rp = ResultPayload(PACKAGE_NAME, **kwargs)
            helper = WikiHelper(self.rest_client())

            # find the wiki page
            content = helper.get_wiki_contents(wiki_title_or_id)

            reason = None
            if content and wiki_contents_as_json:
                content['json'] = json.loads(content['text'])
            else:
                reason = u"Unable to find wiki by title or id: %s".format(wiki_title_or_id)
                yield StatusMessage(reason)

            #yield StatusMessage("Finished 'fn_get_wiki_contents' that was running in workflow '{0}'".format(wf_instance_id))

            results = rp.done(False if reason else True, content, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
