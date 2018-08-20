# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from json2html import *
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_json2html"""

    @function("utilities_json2html")
    def _utilities_json2html_function(self, event, *args, **kwargs):
        """Function: convert a json string to html. Optionally, reference a portion of the json to render"""
        try:
            # Get the function parameters:
            json2html_data = kwargs.get("json2html_data")  # text
            json2html_keys = kwargs.get("json2html_keys")  # text

            log = logging.getLogger(__name__)
            log.info("json2html_data: %s", json2html_data)
            log.info("json2html_keys: %s", json2html_keys)

            json_node = json.loads(json2html_data)

            # look for path information to narrow the amount of json to render
            if json2html_keys:
                for key in json2html_keys.split('.'):
                    if json_node.get(key) is None:
                        raise ValueError("{} key not found".format(key))
                    else:
                        json_node = json_node.get(key)

            result = json2html.convert(json = json_node)

            results = {
                "content": result
            }

            log.debug(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()