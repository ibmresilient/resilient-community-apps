# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Function implementation"""

import logging
from fn_wiki.lib.wiki_common import WikiHelper
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields

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
            validate_fields(["wiki_path"], kwargs)
            # Get the wf_instance_id of the workflow this Function was called in
            #wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]
            #yield StatusMessage("Starting 'fn_wiki_create_update' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            wiki_create_if_missing = bool(kwargs.get("wiki_create_if_missing", False))  # boolean
            wiki_path = kwargs.get("wiki_path")  # text
            wiki_body = kwargs.get("wiki_body")  # text

            log = logging.getLogger(__name__)
            log.info("wiki_create_if_missing: %s", wiki_create_if_missing)
            log.info(u"wiki_path: %s", wiki_path)
            log.info("wiki_body: %s", wiki_body)

            ##############################################
            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
            ##############################################
            helper = WikiHelper(self.rest_client())
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # separate the target wiki from it's parent path
            wiki_list = wiki_path.strip().split("/")
            wiki_title = wiki_list.pop()

            content = helper.get_wiki_contents(wiki_title, wiki_list)
            reason = None
            result_content = None

            # update if content found
            if content:
                result_content = helper.update_wiki(content['id'], content['title'],
                                                    content['parent'], wiki_body)
            elif wiki_create_if_missing:
                parent_title = wiki_list.pop() if wiki_list else None
                # determine if the parent exists
                parent_id = None
                if parent_title:
                    parent_content = helper.get_wiki_contents(parent_title, wiki_list)
                    if not parent_content:
                        reason = u"Unable to find parent page: '{}'".format(parent_title)
                        yield StatusMessage(reason)
                    else:
                        parent_id = parent_content['id']

                if not reason:
                    result_content = helper.create_wiki(wiki_title, parent_id, wiki_body)
            else:
                reason = u"Unable to find page with title: {}".format(wiki_title)
                result_content = None

            results = rp.done(not bool(reason), result_content, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
