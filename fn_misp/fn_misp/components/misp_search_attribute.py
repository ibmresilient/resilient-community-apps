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
from resilient_lib import RequestsCommon

PACKAGE= "fn_misp"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function(s)"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE, {})

    @function("misp_search_attribute")
    def _misp_search_attribute_function(self, event, *args, **kwargs):
        """Function: Search to see if an attribute exists for a given artifact value"""
        try:

            def get_config_option(option_name, optional=False):
                """Given option_name, checks if it is in app.config. Raises ValueError if a mandatory option is missing"""
                option = self.options.get(option_name)

                if option is None and optional is False:
                    err = "'{0}' is mandatory and is not set in ~/.resilient/app.config file. You must set this value to run this function".format(option_name)
                    raise ValueError(err)
                else:
                    return option

            API_KEY = get_config_option("misp_key")
            URL = get_config_option("misp_url")
            VERIFY_CERT = True if get_config_option("verify_cert").lower() == "true" else False

            # Get the function parameters:
            search_attribute = kwargs.get("misp_attribute_value")  # text

            log = logging.getLogger(__name__)
            log.info("search_attribute: %s", search_attribute)

            yield StatusMessage("Setting up connection to MISP")

            # get proxies
            rc = RequestsCommon(opts=self.opts, function_opts=self.options)
            proxies = rc.get_proxies()

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
