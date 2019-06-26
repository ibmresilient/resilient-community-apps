# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
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

    @function("panorama_get_users_in_a_group")
    def _panorama_get_users_in_a_group_function(self, event, *args, **kwargs):
        """Function: Panorama get address groups returns the list of address groups """
        try:
            yield StatusMessage("Getting list of users in a group")
            rp = ResultPayload("fn_pa_panorama", **kwargs)

            validate_fields(["panorama_user_group_xpath"], kwargs)

            # Get the function parameters:
            user_group_xpath = kwargs.get("panorama_user_group_xpath")  # text

            # Log inputs
            log.info("panorama_user_group_xpath: {}".format(user_group_xpath))

            panorama_util = PanoramaClient(self.opts, None)
            xml_response = panorama_util.get_users_in_a_group(user_group_xpath)
            dict_response = xmltodict.parse(xml_response)

            user_list = []
            try:
                members = dict_response["response"]["result"]["entry"]["user"]["member"]
                if isinstance(members, list):
                    # Multiple existing users
                    for m in members:
                        user_list.append(m.get("#text"))
                else:
                    # Single user in group
                    user_list.append(members.get("#text"))
            except KeyError:
                # No users returned
                yield StatusMessage("No users returned.")

            yield StatusMessage("{} users returned.".format(len(user_list)))

            # add to dict_response to allow for more options in Resilient scripting and make some actions easier
            dict_response["user_list"] = user_list
            dict_response["xml_response"] = xml_response
            results = rp.done(True, dict_response)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
