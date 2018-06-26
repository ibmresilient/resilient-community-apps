# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
import OpenSSL
from OpenSSL.crypto import X509
import json
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "utilities_extract_ssl_cert"
FUNCTION_NAME = "utilities_extract_ssl_cert_from_url"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_utilities_extract_ssl_cert_from_url_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("utilities_extract_ssl_cert_from_url", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("utilities_extract_ssl_cert_from_url_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUtilitiesExtractSslCertFromUrl:
    """ Tests for the utilities_extract_ssl_cert_from_url function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("https_url, expected_results", [
        ("www.ibm.com", {"successful": True}),
        ("www.google.com", {"successful": True}),
        ("https://self-signed.badssl.com", {"successful": True}),
        ("https://untrusted-root.badssl.com", {"successful": True}),
        ("https://revoked.badssl.com", {"successful": True}),
        ("https://10000-sans.badssl.com", {"successful": True}),
        ("notaurl", {"successful": False}),
        ("htp:/www.google.com", {"successful": False}),
        ("https://superfish.badssl.com", {"successful": True}),
        ("https://dh512.badssl.com", {"successful": True}),
        ("https://rc4-md5.badssl.com/", {"successful": True}),
        ("https://rc4.badssl.com/", {"successful": True}),
        ("https://3des.badssl.com/", {"successful": True}),
        ("https://null.badssl.com/", {"successful": True}),
        ("https://tls-v1-0.badssl.com:1010/", {"successful": True}),
        ("https://tls-v1-1.badssl.com:1011/", {"successful": True}),
        ("www.tls-v1-1.badssl.com:1011/", {"successful": True})

    ])
    def test_validate_cert(self, circuits_app, https_url, expected_results):
        """ Test the functions return type 'Certificate'
            When the function is successful in parsing the URL
            It should return a value we can parse into a certificate

            OpenSSL.crypto.load_certificate should be able to get a valid certificate

            When the function isint successful -- None"""
        function_params = {
            "https_url": https_url
        }
        # If we expected the result to be unsuccesful it should raise an error
        if expected_results['successful'] == False:
            with pytest.raises(Exception):
                call_utilities_extract_ssl_cert_from_url_function(circuits_app, function_params)

        else:

            results = call_utilities_extract_ssl_cert_from_url_function(circuits_app, function_params)
            # assert(results['successful'] == expected_results['successful'])  # Assert we actually have some results
            if results['successful']:
                assert (isinstance(
                    OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, json.loads(results['certificate'])),
                    X509))  # Assert our successful results are of type X509
            else:
                # assert(results['certificate'] == 'null')
                assert (isinstance(results['certificate'], type(None)))

    @pytest.mark.parametrize("https_url, expected_results", [
        ("www.ibm.com", {"successful": True}),
        ("www.google.com", {"successful": True}),
        ("https://self-signed.badssl.com", {"successful": True}),
        ("https://untrusted-root.badssl.com", {"successful": True}),
        ("https://revoked.badssl.com", {"successful": True}),
        ("https://10000-sans.badssl.com", {"successful": True}),
        ("notaurl", {"successful": False}),
        ("htp:/www.google.com", {"successful": False}),
        ("https://superfish.badssl.com", {"successful": True}),
        ("https://dh512.badssl.com", {"successful": True}),
        ("https://rc4-md5.badssl.com/", {"successful": True}),
        ("https://rc4.badssl.com/", {"successful": True}),
        ("https://3des.badssl.com/", {"successful": True}),
        ("https://null.badssl.com/", {"successful": True}),
        ("https://tls-v1-0.badssl.com:1010/", {"successful": True}),
        ("https://tls-v1-1.badssl.com:1011/", {"successful": True}),
        ("www.tls-v1-1.badssl.com:1011", {"successful": True})

    ])
    def test_validate_json_result(self, circuits_app, https_url, expected_results):
        """ Test the functions return type 'Certificate'
            When the function is successful in parsing the URL
            It should return a valid JSON string
            The JSON string is validated using JSON.loads

            When the function isint successful -- None"""
        function_params = {
            "https_url": https_url
        }
        # If we expected the result to be unsuccesful it should raise an error
        if expected_results['successful'] == False:
            with pytest.raises(Exception):
                call_utilities_extract_ssl_cert_from_url_function(circuits_app, function_params)

        else:
            results = call_utilities_extract_ssl_cert_from_url_function(circuits_app, function_params)
            # assert(results['successful'] == expected_results['successful'])  # Assert we actually have some results
            if results['successful']:
                assert (self.is_json(results['certificate']))
            else:  # IF the success flag is false; there should be a result
                assert (isinstance(results['certificate'], type(None)))

    @pytest.mark.parametrize("https_url, expected_results", [
        ("www.ibm.com", {"successful": True}),
        ("www.google.com", {"successful": True}),
        ("https://self-signed.badssl.com", {"successful": True}),
        ("https://untrusted-root.badssl.com", {"successful": True}),
        ("https://revoked.badssl.com", {"successful": True}),
        ("https://10000-sans.badssl.com", {"successful": True}),
        ("notaurl", {"successful": False}),
        ("htp:/www.google.com", {"successful": False}),
        ("https://superfish.badssl.com", {"successful": True}),
        ("https://dh512.badssl.com", {"successful": True}),
        ("https://rc4-md5.badssl.com/", {"successful": True}),
        ("https://rc4.badssl.com/", {"successful": True}),
        ("https://3des.badssl.com/", {"successful": True}),
        ("https://null.badssl.com/", {"successful": True}),
        ("https://tls-v1-0.badssl.com:1010/", {"successful": True}),
        ("https://tls-v1-1.badssl.com:1011/", {"successful": True}),
        ("www.tls-v1-1.badssl.com:1011", {"successful": True})

    ])
    def test_success(self, circuits_app, https_url, expected_results):
        """ Test calling with sample values for the parameters

            Some sample values are not valid URLs and they should be unsuccessful

            Some invalid URLs should return success -- e.g www.google.com is technically invalid but should return"""
        function_params = {
            "https_url": https_url
        }
        if expected_results['successful'] == False:
            with pytest.raises(Exception):
                call_utilities_extract_ssl_cert_from_url_function(circuits_app, function_params)

        else:
            results = call_utilities_extract_ssl_cert_from_url_function(circuits_app, function_params)
            assert (results['successful'] == expected_results['successful'])  # Assert we actually have some results

    def is_json(self, myjson):
        try:
            json_object = json.loads(myjson)
        except ValueError:
            return False
        return True
