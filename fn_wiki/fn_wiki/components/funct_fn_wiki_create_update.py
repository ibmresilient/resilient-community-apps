# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Function implementation"""

import logging
from fn_wiki.lib.wiki_common import WikiHelper
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload

PACKAGE_NAME = "fn_wiki"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_wiki_create_update''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("fn_wiki_create_update")
    def _fn_wiki_create_update_function(self, event, *args, **kwargs):
        """Function: Create or Update a wiki page in Resilient"""
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            #wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]
            #yield StatusMessage("Starting 'fn_wiki_create_update' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            wiki_create_if_missing = bool(kwargs.get("wiki_create_if_missing", False))  # boolean
            wiki_title_or_id = kwargs.get("wiki_title_or_id")  # text
            wiki_parent_title_or_id = kwargs.get("wiki_parent_title_or_id")  # text
            wiki_body = kwargs.get("wiki_body")  # text

            log = logging.getLogger(__name__)
            log.info("wiki_create_if_missing: %s", wiki_create_if_missing)
            log.info("wiki_title_or_id: %s", wiki_title_or_id)
            log.info("wiki_parent_title_or_id: %s", wiki_parent_title_or_id)
            log.info("wiki_body: %s", wiki_body)

            ##############################################
            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
            ##############################################
            helper = WikiHelper(self.rest_client())
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            content = helper.get_wiki_contents(wiki_title_or_id, wiki_parent_title_or_id)
            reason = None
            result_content = None

            # update if content found
            if content:
                result_content = helper.update_wiki(content['id'], content['title'], content['parent'], wiki_body)
            elif wiki_create_if_missing:
                # determine if the parent exists
                parent_id = None
                if wiki_parent_title_or_id:
                    parent_content = helper.get_wiki_contents(wiki_parent_title_or_id, None)
                    if not parent_content:
                        reason = u"Unable to find parent page: '{}'".format(wiki_parent_title_or_id)
                        yield StatusMessage(reason)
                    else:
                        parent_id = parent_content['id']

                if not reason:
                    result_content = helper.create_wiki(wiki_title_or_id, parent_id, wiki_body)
            else:
                reason = u"Unable to find page with title/id: {}".format(wiki_title_or_id)
                result_content = None

            results = rp.done(False if reason else True, result_content, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
