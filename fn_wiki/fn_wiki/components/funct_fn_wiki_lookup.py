# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Function implementation"""

import logging
import re
from fn_wiki.lib.wiki_common import WikiHelper
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload

PACKAGE_NAME = "fn_wiki"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function(s)"""

    @function("fn_wiki_lookup")
    def _wiki_lookup_function(self, event, *args, **kwargs):
        """Function: """
        try:
            # Get the function parameters:
            wiki_title_or_id = kwargs.get("wiki_title_or_id")  # text
            wiki_parent_title_or_id = kwargs.get("wiki_parent_title_or_id")  # text
            wiki_search_term = kwargs.get("wiki_search_term")  # text

            log = logging.getLogger(__name__)
            log.info("wiki_title_or_id: %s", wiki_title_or_id)
            log.info("wiki_parent_title_or_id: %s", wiki_parent_title_or_id)
            log.info(u"wiki_search_term: %s", wiki_search_term)

            # Setup Resilient rest client
            helper = WikiHelper(self.rest_client())
            rp = ResultPayload(PACKAGE_NAME, **kwargs)
            reason = matching_wiki_content = None

            content = helper.get_wiki_contents(wiki_title_or_id, wiki_parent_title_or_id)

            if not content:
                reason = u"Can't find the wiki with title or id: '{}'".format(wiki_title_or_id)
                yield StatusMessage(reason)
            else:
                log.debug(content)

                matching_wiki_content = do_lookup(wiki_search_term, content)

                # Handle no matches
                if not matching_wiki_content:
                    reason = u"No matches found for {} in the Wiki {}".format(wiki_search_term, 
                                                                              wiki_title_or_id)
                    yield StatusMessage(reason)

                yield StatusMessage("Found {} matching entries".format(len(matching_wiki_content)))

            results = rp.done(False if reason else True, matching_wiki_content, reason=reason)
            # add the title of the wiki page
            results['title'] = content.get('title') if content else None

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()

def do_lookup(wiki_search_term, content):
    search = re.compile(wiki_search_term)

    # break up into list of lines for search
    wiki_content = content['text'].split('\n')

    # if search term is in the wiki pull that line and add to a new list
    return [s for s in wiki_content if search.search(s)]
