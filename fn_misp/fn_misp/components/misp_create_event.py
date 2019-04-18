# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from pymisp import PyMISP
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

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

    @function("misp_create_event")
    def _misp_create_event_function(self, event, *args, **kwargs):
        """Function: create a MISP event from an incident """
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
            misp_event_name = kwargs.get("misp_event_name")  # text
            misp_distribution = kwargs.get("misp_distribution")  # number
            misp_analysis_level = kwargs.get("misp_analysis_level")  # number
            misp_threat_level = kwargs.get("misp_threat_level")  # number

            log = logging.getLogger(__name__)
            log.info("misp_event_name: %s", misp_event_name)
            log.info("misp_distribution: %s", misp_distribution)
            log.info("misp_analysis_level: %s", misp_analysis_level)
            log.info("misp_threat_level: %s", misp_threat_level)

            yield StatusMessage("Setting up connection to MISP")

            misp_client = PyMISP(URL, API_KEY, VERIFY_CERT, 'json')

            event = misp_client.new_event(misp_distribution, misp_threat_level, misp_analysis_level, misp_event_name)

            log.info(event)

            yield StatusMessage("Event has been created")

            results = {
                "success": True,
                "content": event
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
