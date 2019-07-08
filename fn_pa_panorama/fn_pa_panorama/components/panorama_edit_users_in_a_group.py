# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
"""Function implementation"""

import logging
import xmltodict
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from resilient_lib.components.resilient_common import validate_fields
from fn_pa_panorama.util.panorama_util import PanoramaClient


log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'panorama_get_address_groups"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_pa_panorama", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_pa_panorama", {})

    @function("panorama_edit_users_in_a_group")
    def _panorama_edit_users_in_a_group_function(self, event, *args, **kwargs):
        """Function: Panorama get address groups returns the list of address groups """
        try:
            # Response code should equal 20 indicating the call went through successfully
            PASS_CONSTANT = "20"

            yield StatusMessage("Editing list of users in a group")
            rp = ResultPayload("fn_pa_panorama", **kwargs)

            validate_fields(["panorama_user_group_xpath", "panorama_user_group_xml"], kwargs)

            # Get the function parameters:
            user_group_xpath = kwargs.get("panorama_user_group_xpath")  # text
            user_group_xml = self.get_textarea_param(kwargs.get("panorama_user_group_xml"))  # textarea

            # Log inputs
            log.info(u"panorama_user_group_xpath: {}".format(user_group_xpath))
            log.info(u"panorama_user_group_xml: {}".format(user_group_xml))

            panorama_util = PanoramaClient(self.opts, None)
            xml_response = panorama_util.edit_users_in_a_group(user_group_xpath, user_group_xml)
            dict_response = xmltodict.parse(xml_response)

            try:
                if dict_response["response"].get("@code") == PASS_CONSTANT:
                    yield StatusMessage("User group was successfully edited.")
                else:
                    raise FunctionError("Editing the user group was unsuccessful with code {}, raising FunctionError.".
                                        format(dict_response["response"]["@code"]))
            except KeyError as e:
                yield StatusMessage("Editing the user group was unsuccessful.")
                raise FunctionError(e)

            # add to dict_response to allow for more options in Resilient scripting and make some actions easier
            dict_response["xml_response"] = xml_response
            results = rp.done(True, dict_response)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
