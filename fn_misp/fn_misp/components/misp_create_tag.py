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
from resilient_lib import IntegrationError


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

    @function("misp_create_tag")
    def _misp_create_tag_function(self, event, *args, **kwargs):
        """Function: Creates a Tag"""
        try:

            # Get the function parameters:
            misp_tag_type = self.get_select_param(kwargs.get("misp_tag_type"))  # select, values: "Event", "Attribute"
            misp_tag_name = kwargs.get("misp_tag_name")  # text
            misp_attribute_value = kwargs.get("misp_attribute_value")  # text
            misp_event_id = kwargs.get("misp_event_id")  # number

            # ensure misp_event_id is an integer so we can get an event by it's index
            if not isinstance(misp_event_id, int):
                raise IntegrationError(
                    u"Unexpected input type for MISP Event ID. Expected and integer, received {}".format(type(misp_event_id)))

            API_KEY, URL, VERIFY_CERT = common.validate(self.options)

            log = logging.getLogger(__name__)
            log.info("misp_tag_type: %s", misp_tag_type)
            log.info("misp_tag_name: %s", misp_tag_name)
            log.info("misp_attribute_value: %s", misp_attribute_value)
            log.info("misp_event_id: %s", misp_event_id)

            if sys.version_info.major < 3:
                raise FunctionError("Tagging is only supported when using Python 3")

            yield StatusMessage("Setting up connection to MISP")

            proxies = common.get_proxies(self.opts, self.options)

            misp_client = misp_helper.get_misp_client(URL, API_KEY, VERIFY_CERT, proxies=proxies)

            yield StatusMessage(u"Tagging {} with {}".format(misp_tag_type, misp_tag_name))

            tag_result = misp_helper.create_tag(misp_client, misp_attribute_value, misp_tag_type, misp_tag_name, misp_event_id)
            if 'errors' in tag_result:
                raise IntegrationError(u"Unable to save the tag. {}".format(tag_result['errors'][1]['errors']))

            log.debug(tag_result)

            yield StatusMessage("Tag has been created")

            response_results = {"success": True}

            # Produce a FunctionResult with the results
            yield FunctionResult(response_results)
        except Exception:
            yield FunctionError()
