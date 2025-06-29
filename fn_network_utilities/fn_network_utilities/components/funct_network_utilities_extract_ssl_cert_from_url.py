# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# pragma pylint: disable=pointless-string-statement, line-too-long, wrong-import-order

"""
    Function network_utilities_extract_ssl_cert_from_url receives a HTTPS_URL as a parameter.
    It then attempts to gather the certificate for this provided URL.
    Uses the built in SSL and urlparse libraries to accomplish the functionality

    In test cases it uses pyOpenSSL library (https://pyopenssl.org/en/stable/index.html)
    to confirm the output certificate data is in valid PEM format.
    Returns the certificate encoded in JSON along with a 'successful' boolean.
    This indicates whether the operation was successful.
    If a valid URL is provided, the cert is saved as an artifact in the Post-Processing Script.
"""
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

import logging
import ssl
import json
from resilient_circuits import ResilientComponent, handler, function,\
     FunctionResult, FunctionError
from resilient_lib import RequestsCommon, validate_fields

SECTION_HDR = "fn_network_utilities"

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'utilities_extract_ssl_cert_from_url"""
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(SECTION_HDR, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(SECTION_HDR, {})

    def init_proxies(self):
        self.proxy_host = None
        self.proxy_port = None

        rc = RequestsCommon(self.opts, self.options)
        proxies = rc.get_proxies()

        if proxies:
            proxy = proxies.get('https', proxies.get('http'))

            if proxy:
                proxy_url = urlparse.urlparse(proxy)
                self.proxy_host = proxy_url.hostname
                self.proxy_port = proxy_url.port

    @function("network_utilities_extract_ssl_cert_from_url")
    def _utilities_extract_ssl_cert_from_url_function(self, event, *args, **kwargs):
        """Function:
        This function takes in a HTTPS URL and attempts to acquire its Certificate, saving it as an artifact.
        Inputs: A HTTPS_URL.
        Outputs: Certificate file encoded in JSON.
        Schema of the results :
        results =
        {
            "certificate": Certificate string encoded as JSON or NoneType,
            "successful": True if certificate is not NoneType; False otherwise
        }
        """
        validate_fields(["network_utilities_https_url"], kwargs)
        try:
            # Get the function parameters:
            https_url = kwargs.get("network_utilities_https_url")  # text

            log = logging.getLogger(__name__)
            log.info(f"https_url: {https_url}")

            self.init_proxies()
            url_dict = urlparse.urlparse(https_url)
            certificate = None  # Init x509 as None and try to gather the cert
            conn = None   # Init conn as None to prevent reference before assign
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

                if self.proxy_host:
                    log.debug("Using proxy: %s:%s", self.proxy_host, self.proxy_port)
                    conn = ssl.create_connection((self.proxy_host, self.proxy_port))
                else:
                    conn = ssl.create_connection((url_dict.hostname, url_dict.port if url_dict.port else 443))

                context = ssl.SSLContext(ssl.PROTOCOL_TLS)
                sock = context.wrap_socket(conn, server_hostname=url_dict.hostname)
                certificate = ssl.DER_cert_to_PEM_cert(sock.getpeercert(True))
            except Exception as err:
                raise KeyError(f"Problem encountered while parsing the cert.: {str(err)}")

            finally:
                # Close the connection once we have what we want
                if conn is not None:
                    conn.close()

            # Prepares a JSON object from the get_server_certificate function result
            serialized_cert = json.dumps(certificate, default=lambda o: o.__dict__,
                                         sort_keys=True, indent=4)
            # Results are used in PostProcessing script to create artifact on the platform
            results = {
                # If the certificate wasn't parsed; 'null' will be the result
                "certificate": (serialized_cert if serialized_cert != 'null' else None),
                # x509 starts out as a None type; if unsuccessful it will still be a none type
                "successful": (certificate is not None)
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
