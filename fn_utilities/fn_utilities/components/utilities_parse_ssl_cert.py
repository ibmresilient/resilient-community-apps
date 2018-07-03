# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, broad-except
"""
    Function utilities_parse_ssl_cert receives a certificate as a parameter.
    The certificate string is a JSON encoded string.

    Uses the OpenSSL and Cryptography packages to accomplish the functionality
    Expects a valid PEM format certificate.

    Returns the details for the provided cert.

    The results returned by this function can then be saved as a Rich Text note.
"""

import logging
import json
import datetime
import OpenSSL # Used for certificates
from cryptography import x509 # Used for certificates
from cryptography.hazmat.backends import default_backend
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_parse_ssl_cert"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("utilities_parse_ssl_cert", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("utilities_parse_ssl_cert", {})

    @function("utilities_parse_ssl_cert")
    def _utilities_parse_ssl_cert_function(self, event, *args, **kwargs):
        """Function: Takes in an SSL Certificate.
        Attempts to parse information from this certificate and save it as a note"""
        try:
            # Get the function parameters:
            certificate = kwargs.get("certificate")  # text

            log = logging.getLogger(__name__)
            log.info("certificate: %s", certificate)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            try:  # Try catch inside a try catch ?
                yield StatusMessage("Attempting to parse the cert as JSON")
                parsed_cert_json = json.loads(certificate)
                # Load the cert into PyOpenSSL; 
                parsed_cert_openssl = OpenSSL.crypto.load_certificate(
                    OpenSSL.crypto.FILETYPE_PEM, parsed_cert_json)
                # Load cert also with cryptography; this package has better date attributes
                parsed_cert_crypto = x509.load_pem_x509_certificate(
                    str(parsed_cert_json), default_backend())

                yield StatusMessage("Returning results")
                #  Prepare results for return; many fields need to be wrapped as strings or as JSON.
                results = {

                    "subject": json.dumps(parsed_cert_openssl.get_subject().get_components()),
                    "notBefore": str(parsed_cert_crypto.not_valid_before),
                    "notAfter": str(parsed_cert_crypto.not_valid_after),
                    "issuer": json.dumps(parsed_cert_openssl.get_issuer().get_components()),
                    "version": parsed_cert_openssl.get_version(),
                    "expiration_status": ('Valid' if self._date_within_range(parsed_cert_crypto.not_valid_before, parsed_cert_crypto.not_valid_after, datetime.datetime.today()) is True else 'Expired')
                }
                # Produce a FunctionResult with the results
                yield FunctionResult(results)
            except ValueError:
                yield StatusMessage('Problem loading the cert as JSON; Perhaps a file was provided?')

                raise FunctionError('Problem loading the certificate as JSON')


        except Exception:
            yield FunctionError()

    @staticmethod
    def _date_within_range(lower_bound, upper_bound, the_date):

        if lower_bound <= the_date <= upper_bound:
            return True
        else:
            return False
