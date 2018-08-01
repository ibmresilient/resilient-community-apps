# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, pointless-string-statement
"""
    Function utilities_extract_ssl_cert_from_url receives a HTTPS_URL as a parameter.
    It then attempts to gather the certificate for this provided URL.

    Uses the built in SSL and urlparse librarys to accomplish the functionality
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
from resilient_circuits import ResilientComponent, function,\
     FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_extract_ssl_cert_from_url"""


    @function("utilities_extract_ssl_cert_from_url")
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
        try:
            # Get the function parameters:
            https_url = kwargs.get("https_url")  # text

            log = logging.getLogger(__name__)
            log.info("https_url: %s", https_url)

            if https_url is None:
                raise ValueError("Error: https_url must be specified.")

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

                if url_dict.port is not None:
                    conn = ssl.create_connection((url_dict.hostname, url_dict.port))
                else:
                    conn = ssl.create_connection((url_dict.hostname, 443))
                context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
                sock = context.wrap_socket(conn, server_hostname=url_dict.hostname)
                certificate = ssl.DER_cert_to_PEM_cert(sock.getpeercert(True))
            except Exception:
                raise KeyError("Problem encountered while parsing the cert.")

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
                "certificate": (serialized_cert if serialized_cert is not 'null' else None),
                # x509 starts out as a None type; if unsuccessful it will still be a none type
                "successful": (certificate is not None)
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()