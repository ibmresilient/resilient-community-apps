# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from pymisp import PyMISP
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function(s)"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_misp", {})

    @function("misp_create_attribute")
    def _misp_create_attribute_function(self, event, *args, **kwargs):
        """Function: """
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
            misp_event_id = kwargs.get("misp_event_id")  # number
            misp_attribute_value = kwargs.get("misp_attribute_value")  # text
            misp_attribute_type = kwargs.get("misp_attribute_type")  # text

            log = logging.getLogger(__name__)
            log.info("misp_event_id: %s", misp_event_id)
            log.info("misp_attribute_value: %s", misp_attribute_value)
            log.info("misp_attribute_type: %s", misp_attribute_type)

            yield StatusMessage("Setting up connection to MISP")

            misp_client = PyMISP(URL, API_KEY, VERIFY_CERT, 'json')

            """
            default_map = { 
                "DNS Name": "domain",
                "Email Attachment": "email-attachment",
                "Email Body": "email-body",
                "Email Recipient": "email-dst",
                "Email Sender": "email-src",
                "Email subject": "email-subject",
                "File Name": "filename",
                "DNS Name": "hostname",
                "MAC Address": "mac-address",
                "Malware MD5 Hash": "md5",
                "Port": "port",
                "Malware SHA-1 Hash": "sha1",
                "Malware SHA-256 Hash": "sha256",
                "URI Path": "uri",
                "URL": "url",
                "Threat CVE ID": "vulnerability",
                "IP Address": "ip-dst"
            }
            """

            yield StatusMessage("Creating new misp attribute {} {}".format(misp_attribute_type, misp_attribute_value))

            attribute = misp_client.add_named_attribute(misp_event_id, misp_attribute_type, misp_attribute_value)

            log.info(event)

            results = { "success": True,
                        "content": attribute
                      }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
