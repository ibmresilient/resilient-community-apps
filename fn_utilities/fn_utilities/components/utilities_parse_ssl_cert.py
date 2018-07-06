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
import tempfile
from cryptography import x509 # Used for certificates
from cryptography.hazmat.backends import default_backend
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_parse_ssl_cert"""


    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

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
            incident_id = kwargs.get("incident_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number

            log = logging.getLogger(__name__)
            log.info("certificate: %s", certificate)
            log.info("incident_id: %s", incident_id)
            log.info("artifact_id: %s", artifact_id)
            client = self.rest_client()

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")
            # If certificate is none then it try to parse it either by JSON artifact
            if certificate is not None:

                try:  # Try catch inside a try catch ?
                    yield StatusMessage("Attempting to parse the cert as JSON")
                    parsed_cert_json = json.loads(certificate)

                    '''
                    Maybe we could throw json.decoder.JSONDecodeError here ??
                    '''
                    # Load the cert into PyOpenSSL; Throws OpenSSL.crypto.Error if problems
                    parsed_cert_openssl = OpenSSL.crypto.load_certificate(
                        OpenSSL.crypto.FILETYPE_PEM, parsed_cert_json)
                    # Load cert also with cryptography; this package has better date attributes
                    parsed_cert_crypto = x509.load_pem_x509_certificate(
                        str(parsed_cert_json), default_backend())
                    #  Prepare results for return; many fields need to be wrapped as strings or as JSON.
                    results = {

                        "subject": json.dumps(parsed_cert_openssl.get_subject().get_components()),
                        "notBefore": str(parsed_cert_crypto.not_valid_before),
                        "notAfter": str(parsed_cert_crypto.not_valid_after),
                        "issuer": json.dumps(parsed_cert_openssl.get_issuer().get_components()),
                        "version": parsed_cert_openssl.get_version(),
                        "expiration_status": ('Valid' if self._date_within_range(parsed_cert_crypto.not_valid_before, parsed_cert_crypto.not_valid_after, datetime.datetime.today()) is True else 'Expired')
                    }
                except ValueError:
                    yield StatusMessage('Problem encountered loading the certificate as JSON;')
                    '''
                        2 Possible causes for reaching this ValueError
                        -- Non valid JSON was provided; Maybe malformed cert
                        -- A file was provided and the filename thew exception

                        In the case of cause 2 try to load the file using the rest API

                    '''
                    artifact_data = self.get_binary_data_from_file(client, incident_id, artifact_id)


                    # Create a temporary file to write the binary data to.
                    with tempfile.NamedTemporaryFile('w+b', bufsize=0) as temp_file:
                        # Write binary data to a temporary file.
                        temp_file.write(artifact_data)
                        st_cert=open(temp_file.name, 'rt').read()

                        c=OpenSSL.crypto
                        parsed_cert_openssl=c.load_certificate(c.FILETYPE_PEM, st_cert)

                        # Load cert also with cryptography; this package has better date attributes
                        parsed_cert_crypto = x509.load_pem_x509_certificate(
                            st_cert, default_backend())

                        yield("File parsed from rest API")
                        log.info("Info gathered from cert files subject")
                        log.info(json.dumps(parsed_cert_openssl.get_subject().get_components()))


                        
                        #  Prepare results for return; many fields need to be wrapped as strings or as JSON.
                        results = {

                            "subject": json.dumps(parsed_cert_openssl.get_subject().get_components()),
                            "notBefore": str(parsed_cert_crypto.not_valid_before),
                            "notAfter": str(parsed_cert_crypto.not_valid_after),
                            "issuer": json.dumps(parsed_cert_openssl.get_issuer().get_components()),
                            "version": parsed_cert_openssl.get_version(),
                            "expiration_status": ('Valid' if self._date_within_range(parsed_cert_crypto.not_valid_before, parsed_cert_crypto.not_valid_after, datetime.datetime.today()) is True else 'Expired')
                        }
                
                        yield FunctionResult(results)
                        
                else:
                    # Produce a FunctionResult with the results if no exceptions happened
                    yield FunctionResult(results)

            


        except Exception:
            yield FunctionError()

    @staticmethod
    def _date_within_range(lower_bound, upper_bound, the_date):

        if lower_bound <= the_date <= upper_bound:
            return True
        else:
            return False
    @staticmethod
    def get_binary_data_from_file(client, incident_id, artifact_id):
        """get_binary_data_from_file calls the REST API to get the attachment or artifact data"""

        if artifact_id and incident_id:
            data_uri = "/incidents/{}/artifacts/{}/contents".format(incident_id, artifact_id)
        else:
            raise ValueError("artifact and incident id must be specified")

        # Get the data
        data = client.get_content(data_uri)

        return data
