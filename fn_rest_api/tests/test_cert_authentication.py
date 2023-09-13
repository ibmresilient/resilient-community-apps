import pytest
from unittest.mock import patch
from fn_rest_api.lib.authentication_handler import *
from fn_rest_api.lib.helper import *

def test_prepare_certificates():
    cert_content = """
    -----BEGIN PRIVATE KEY-----
    MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDY803clWbyoyRu
    T5cASQNPqroXQYil4foi0bHQ7+azCvLmz7nRJdnDLLsv6P2uFn9zOFy5NERzvQwX
    I7jwxItVpZhru2bGyh5Asksmck9xV7mmZITg/jVwz0CrlEXyx65C2qkYD+kCQ1UQ
    uv9Nt7Px38fnEhAxMK5v3neTfEyUd1k1knBRpSBD7BlvEW3EByYPclQZnqUS5GGU
    IMCE/hb9s21OWhhiBUtNADQKOZdajyvzyxC55suqr5LnO3TuTtfzNiQD2oWM1oNW
    D3XY7vvlyJPgNl/ixHJRhhrsqk5WXzg8/xtqTHsQoQ6IEctX3lhbQqVdQz8ysvod
    JKLK6uxdAgMBAAECggEAbu0wQXnucl9yECkHtzCdzc0oax2p5c8+WzFGruMK3T7a
    Y0VTUE2EXmwDs7KdqgECmbz4
    -----END PRIVATE KEY-----
    """
    cert_name = "privateKey_test"
    cert_type = ".key"
    certs_path = {}

    prepare_certificates(cert_content, cert_name, cert_type, certs_path)

    assert "privateKey_test" in certs_path
    assert "file" in certs_path["privateKey_test"]
    assert "dir" in certs_path["privateKey_test"]
    assert os.path.isdir(certs_path["privateKey_test"]["dir"])
    assert os.path.isfile(certs_path["privateKey_test"]["file"])

    with open(certs_path.get("privateKey_test").get("file"), "r") as file:
        assert cert_content == file.read()
    
    delete_certificates(certs_path)


def test_delete_certificates():
    cert_content = """
    -----BEGIN PRIVATE KEY-----
    -----END PRIVATE KEY-----
    """
    cert_name = "privateKey_test"
    cert_type = ".key"
    certs_path = {}

    prepare_certificates(cert_content, cert_name, cert_type, certs_path)
    with open(certs_path.get("privateKey_test").get("file"), "r") as file:
        assert cert_content == file.read()
    
    actual_path = certs_path.copy()
    assert os.path.isdir(certs_path["privateKey_test"]["dir"])
    assert os.path.isfile(certs_path["privateKey_test"]["file"])
    delete_certificates(certs_path)
    assert not os.path.isdir(actual_path["privateKey_test"]["dir"])
    assert not os.path.isfile(actual_path["privateKey_test"]["file"])
    assert certs_path == {}
    assert delete_certificates(certs_path)

    with pytest.raises(ValueError):
        assert delete_certificates({"temp_file" : {"dir" : "/invalid/directory"}})


def test_check_certificate():
    cert_properties = {
        "client_auth_cert" : "------> Authentication Certificate <------",
        "client_auth_key"  : "------>        Private Key         <------"}
    certs_path = {}

    certificates = check_certificate(cert_properties, certs_path)
    assert isinstance(certificates, tuple)
    assert len(certificates) == 2
    assert "client_auth_cert.csr" in certificates[0]
    assert "client_auth_key.key"  in certificates[1]
    assert os.path.isfile(certificates[0])
    assert os.path.isfile(certificates[1])
    delete_certificates(certs_path)
    assert certs_path == {}
    
    cert_properties = {
    "client_auth_pem" : "------> Authentication Certificate PEM <------"}
    certificates = check_certificate(cert_properties, certs_path)
    assert isinstance(certificates, str)
    assert "client_auth_pem.pem" in certificates
    assert os.path.isfile(certificates)
    delete_certificates(certs_path)
    assert certs_path == {}


@pytest.mark.parametrize("test_case, expected_response", [
    ("title: foo\n body : bar\n  userId:1\n", {'title': 'foo', 'body': 'bar', 'userId': '1'}),
    ('{"title": "foo", "body" : "bar",  "userId":"1"}', {'title': 'foo', 'body': 'bar', 'userId': '1'}),
    ('{"title": "foo", "body": ["bar1", "bar2"], "userId": "1"}', {'title': 'foo', 'body': ['bar1', 'bar2'], 'userId': '1'}),
    ('{"title": "foo", "body" : ["bar1", "bar2"],  "userId":"1", "sub_dict" : {"title": "foo", "body" : ["bar1", "bar2"],  "userId":"1"}}', {'title': 'foo', 'body': ['bar1', 'bar2'], 'userId': '1', 'sub_dict' : {'title': 'foo', 'body': ['bar1', 'bar2'], 'userId': '1'}})
])
def test_build_dict(test_case, expected_response):
    generated_response = build_dict(test_case)
    assert expected_response == generated_response