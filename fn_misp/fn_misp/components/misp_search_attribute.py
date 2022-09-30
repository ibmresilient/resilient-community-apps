# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import sys
if sys.version_info.major < 3:
    from fn_misp.lib import misp_2_helper as misp_helper
else:
    from fn_misp.lib import misp_3_helper as misp_helper
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_misp.lib import common


PACKAGE= "fn_misp"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function(s)"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(PACKAGE, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(PACKAGE, {})

    @function("misp_search_attribute")
    def _misp_search_attribute_function(self, event, *args, **kwargs):
        """Function: Search to see if an attribute exists for a given artifact value"""
        try:

            API_KEY, URL, VERIFY_CERT = common.validate(self.options)

            # Get the function parameters:
            search_attribute = kwargs.get("misp_attribute_value")  # text

            log = logging.getLogger(__name__)
            log.info("search_attribute: %s", search_attribute)

            yield StatusMessage("Setting up connection to MISP")

            proxies = common.get_proxies(self.opts, self.options)

            misp_client = misp_helper.get_misp_client(URL, API_KEY, VERIFY_CERT, proxies=proxies)

            yield StatusMessage(u"Searching for attribute - {}".format(search_attribute))

            results = {}

            search_results = misp_helper.search_misp_attribute(misp_client, search_attribute)

            log.debug(search_results)

            if search_results['search_status']:
                results['success'] = True
                results['content'] = search_results['search_results']
                misp_tags = misp_helper.get_misp_attribute_tags(misp_client, search_results['search_results'])
                results['tags'] = misp_tags
            else:
                results['success'] = False

            yield StatusMessage("Attribute search complete.")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
