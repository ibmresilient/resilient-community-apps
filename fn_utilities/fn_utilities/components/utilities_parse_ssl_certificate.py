# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, broad-except,pointless-string-statement
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
import tempfile
import OpenSSL # Used for certificates
from cryptography import x509 # Used for certificates
from cryptography.x509 import DNSName, ExtensionNotFound, ExtensionOID
from cryptography.hazmat.backends import default_backend
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_parse_ssl_certificate"""

    @function("utilities_parse_ssl_certificate")
    def _utilities_parse_ssl_certificate_function(self, event, *args, **kwargs):
        """Function: Takes in an SSL Certificate.
        Attempts to parse information from this certificate and return it for use.
        
        results =
        {
            "subject": JSON Encoded Array of subject components,
            "notBefore": The certificate is only valid AFTER this date; Formatted as Datetime,
            "notAfter": The certificate is only valid BEFORE this date; Formatted as Datetime,
            "issuer": JSON Encoded Array of issuer details,
            "version": The Version of the certificate v1/v2,
            "expiration_status": Check if the date is within the range of notBefore and notAfter
            "extensions": Object containing the various extensions a cert may have
        }"""
        try:
            # Get the function parameters:
            artifact_id = kwargs.get("artifact_id")  # number
            certificate = kwargs.get("utilities_certificate")  # text
            incident_id = kwargs.get("incident_id")  # number

            log = logging.getLogger(__name__)
            log.info("artifact_id: %s", artifact_id)
            log.info("certificate: %s", certificate)
            log.info("incident_id: %s", incident_id)
            client = self.rest_client()

            if certificate is None and (artifact_id is None or incident_id is None):
                raise ValueError("Error: Either a certificate string, \
                    or BOTH artifact_id and incident_id must be supplied.")

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            try:  # Nested try catch
                yield StatusMessage("Attempting to parse the cert as JSON")
                parsed_cert_json = json.loads(certificate)
                # Load the cert into PyOpenSSL; Throws OpenSSL.crypto.Error if problems
                parsed_cert_openssl = OpenSSL.crypto.load_certificate(
                    OpenSSL.crypto.FILETYPE_PEM, parsed_cert_json)

                # Load cert also with cryptography; this package has better date attributes
                parsed_cert_crypto = x509.load_pem_x509_certificate(
                    str(parsed_cert_json).encode('utf-8'), default_backend())
                
            except ValueError:
                yield StatusMessage('Problem encountered loading the certificate as JSON.')
                yield StatusMessage('Attempting to load from REST API instead.')
                """
                    2 Possible causes for reaching this ValueError
                    -- Non valid JSON was provided; Maybe malformed cert
                    -- A file was provided and the filename threw exception

                    In the case of cause 2 try to load the file using the rest API
                """
                # Get the artifact from the REST API
                artifact_data = self._get_binary_data_from_file(client, incident_id, artifact_id)
                parsed_cert_openssl = OpenSSL.crypto.load_certificate(
                    OpenSSL.crypto.FILETYPE_PEM, artifact_data)
                # Load cert also with cryptography; this package has better date attributes
                parsed_cert_crypto = x509.load_pem_x509_certificate(
                    artifact_data, default_backend())
                
            #  Prepare results for return; many fields need to be wrapped as strings or as JSON.
            #  Some fields must be serialised into JSON in order to be compatible with STOMP
            results = {
                "subject": json.dumps(str(parsed_cert_openssl.get_subject().get_components())),
                "notBefore": str(parsed_cert_crypto.not_valid_before),
                "notAfter": str(parsed_cert_crypto.not_valid_after),
                "issuer": json.dumps(str(parsed_cert_openssl.get_issuer().get_components())),
                "version": parsed_cert_openssl.get_version(),
                "expiration_status": ('Valid' if self._date_within_range(parsed_cert_crypto.not_valid_before, parsed_cert_crypto.not_valid_after, datetime.datetime.today()) is True else 'Expired'),
                "signature_algorithm": str(parsed_cert_openssl.get_signature_algorithm()),
                "public_key": str(OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_PEM, parsed_cert_openssl.get_pubkey())),
                "extensions": {
                    "subjectAltNames": json.dumps(self._get_dns_subject_alternative_names(parsed_cert_crypto)),
                    "basicConstraints": json.dumps(self._get_basic_constraints(parsed_cert_crypto)),
                    "issuerAltNames": json.dumps(self._get_issuer_alternative_names(parsed_cert_crypto))
                }

            }
            # Return the formatted data we have received.
            yield StatusMessage("Finishing...")
            yield FunctionResult(results)
        
        except Exception:
            yield FunctionError()

            

            
    """
    Takes in 3 params
    :param lower_bound the earliest date acceptable for validation
    :param upper_bound the latest date acceptable
    :param the_date the date we are checking, usually the current date at time of execution


    This function is used to ensure a SSL Cert is within a provided date range.

    Returns true if the_date is within the two bounds
    False otherwise
    """
    @staticmethod
    def _date_within_range(lower_bound, upper_bound, the_date):

        if lower_bound <= the_date <= upper_bound:
            return True
        else:
            return False

    """
    Takes in 3 params
    :client -- REST client to be used
    :incident_id -- The incident to be queried
    :artifact_id -- The artifact that will be queried

    Attempts to gather the binary data for an artifacts attachmentment.

    Performs a HTTP to the Resilient REST API and attempts to gather the attachment.
    Returns the data in binary form which can then be written to a local file.
    """
    @staticmethod
    def _get_binary_data_from_file(client, incident_id, artifact_id):
        """get_binary_data_from_file calls the REST API to get the attachment or artifact data"""

        if artifact_id and incident_id:
            data_uri = "/incidents/{}/artifacts/{}/contents".format(incident_id, artifact_id)
        else:
            raise ValueError("artifact and incident id must be specified")

        # Get the data
        data = client.get_content(data_uri)

        return data
    """
    Takes in 1 params
    :certificate -- Certificate string we are checking

    Attempts to gather the subject alternative names for a cert
    """
    @staticmethod
    def _get_dns_subject_alternative_names(certificate):
        # type: (cryptography.x509.Certificate) -> List[Text]
        """Retrieve all the DNS entries of the Subject Alternative Name extension.
        """
        subj_alt_names = []
        try:
            san_ext = certificate.extensions.get_extension_for_oid(ExtensionOID.SUBJECT_ALTERNATIVE_NAME)
            subj_alt_names = san_ext.value.get_values_for_type(DNSName)
        except ExtensionNotFound:
            pass
        return subj_alt_names
    """
    Takes in 1 params
    :certificate -- Certificate string we are checking

    Attempts to gather the issuer alternative names for a cert
    """
    @staticmethod
    def _get_issuer_alternative_names(certificate):
        # type: (cryptography.x509.Certificate) -> List[Text]
        """Retrieve all the DNS entries of the Subject Alternative Name extension.
        """
        issuer_alt_names = []
        try:
            san_ext = certificate.extensions.get_extension_for_oid(ExtensionOID.ISSUER_ALTERNATIVE_NAME)
            issuer_alt_names = san_ext.value.get_values_for_type(DNSName)
        except ExtensionNotFound:
            pass
        return issuer_alt_names

    @staticmethod
    def _get_basic_constraints(certificate):
        # return true/false based on basic constraints
        try:
            ext = certificate.extensions.get_extension_for_oid(ExtensionOID.BASIC_CONSTRAINTS)
            return ext.value.ca
        except ExtensionNotFound:
            pass
        return False