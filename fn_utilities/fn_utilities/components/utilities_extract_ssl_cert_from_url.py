# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

import logging
import ssl
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_extract_ssl_cert_from_url"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("utilities_extract_ssl_cert", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("utilities_extract_ssl_cert", {})

    @function("utilities_extract_ssl_cert_from_url")
    def _utilities_extract_ssl_cert_from_url_function(self, event, *args, **kwargs):
        """Function: This function takes in a HTTPS URL and attempts to acquire its Certificate, saving it as an artifact.
Inputs: A HTTPS_URL.
Outputs: Certificate file encoded in JSON."""
        try:
            # Get the function parameters:
            https_url = kwargs.get("https_url")  # text

            log = logging.getLogger(__name__)
            log.info("https_url: %s", https_url)

            if https_url is None:
                raise FunctionError("Error: https_url must be specified.")

            url_dict = urlparse.urlparse(https_url)
            x509 = None  # Init x509 as None and try to gather the cert
            try:

                '''
                    Not all input URLs will be formed properly

                    Some may be all good and have the Scheme, netloc,path
                    Others will not e.g www.google.com when passed to urlparse will not have a netloc param 

                    In these cases urlparse will stick the URL in the path attribute if at all
                    https://docs.python.org/2/library/ssl.html#ssl.get_server_certificate

                '''
                # If netloc is an empty string; we had issues parsing it from urlparse
                if not url_dict.netloc:  # Empty strings are 'falsy';
                    # Add '//' to the URL this will sort out any 'www' url
                    url_dict = urlparse.urlparse(
                        '//' + https_url)  # Note; this wont fix urls with bad schemes i.e htp:/
                    if bool(url_dict.hostname) & bool(url_dict.port):
                        x509 = ssl.get_server_certificate((url_dict.hostname, url_dict.port))
                    else:
                        x509 = ssl.get_server_certificate((url_dict.hostname, 443))
                else:  # If we reach here then we know there was a netloc provided

                    '''
                        If no port is provided default to the standard port 443.
                    '''
                    if url_dict.port is not None:
                        x509 = ssl.get_server_certificate((url_dict.hostname, url_dict.port))
                    else:
                        x509 = ssl.get_server_certificate((url_dict.hostname, 443))

            except Exception:
                raise FunctionError("Problem encountered while parsing the cert.")

            # Prepares a JSON object from the get_server_certificate function result
            serialized_cert = json.dumps(x509, default=lambda o: o.__dict__,
                                         sort_keys=True, indent=4)
            # Results are used in PostProcessing script to create artifact on the platform
            results = {
                # If the certificate wasn't parsed; 'null' will be the result
                "certificate": (serialized_cert if serialized_cert is not 'null' else None),
                # x509 starts out as a None type; if unsuccessful it will still be a none type
                "successful": (x509 is not None)
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()