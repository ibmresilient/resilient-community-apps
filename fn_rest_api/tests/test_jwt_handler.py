import jwt, json
import unittest, pytest

from collections import OrderedDict
from resilient_lib import IntegrationError
from fn_rest_api.lib.authentication_handler import JWTHandler
from fn_rest_api.lib.authentication_handler import JWT_KEY, JWT_TOKEN, JWT_HEADERS, JWT_PAYLOAD, \
    JWT_ALGORITHM, JWT_TOKEN_TYPE, DEFAULT_JWT_ENCRYPTION_ALGORITHM, AUTHORIZATION_KEY, HEADERS

def test_jwt_constants():
    """ Check to see if any of the constants values required for JWT are changed """
    assert JWT_KEY == "key"
    assert JWT_TOKEN == "token"
    assert JWT_HEADERS == "headers"
    assert JWT_PAYLOAD == "payload"
    assert JWT_ALGORITHM == "algorithm"
    assert JWT_TOKEN_TYPE == "token_type"
    assert DEFAULT_JWT_ENCRYPTION_ALGORITHM == "HS256"

def test_jwt_constructor():
    jwt_client = JWTHandler({})
    assert jwt_client._jwt_properties
    assert JWT_KEY in jwt_client._jwt_properties
    assert JWT_TOKEN in jwt_client._jwt_properties
    assert JWT_HEADERS in jwt_client._jwt_properties
    assert JWT_PAYLOAD in jwt_client._jwt_properties
    assert JWT_ALGORITHM in jwt_client._jwt_properties
    assert JWT_TOKEN_TYPE in jwt_client._jwt_properties
    assert DEFAULT_JWT_ENCRYPTION_ALGORITHM == jwt_client._jwt_properties[JWT_ALGORITHM]

    _props = {
        JWT_KEY : "key123" ,
        JWT_TOKEN : "token123",
        JWT_HEADERS : {"header"  : "value"},
        JWT_PAYLOAD : {"payload" : "value"},
        JWT_ALGORITHM : "RS256",
        JWT_TOKEN_TYPE : "jwt"}
    jwt_client = JWTHandler(_props)
    assert _props == jwt_client._jwt_properties

def test_compile_headers_jwt_token_type():
    _props = {
        JWT_TOKEN : "token123",
        JWT_TOKEN_TYPE : "jwt"}
    jwt_client = JWTHandler(_props)
    assert jwt_client._compile_headers() == {'Authorization': 'jwt token123'}

def test_compile_headers_bearer_token_type():
    _props = {
        JWT_TOKEN : "token123",
        JWT_TOKEN_TYPE : "bearer" }
    jwt_client = JWTHandler(_props)
    assert jwt_client._compile_headers() == {'Authorization': 'bearer token123'}

def test_compile_headers_valid_token_missing_key():
    _props = {
        JWT_TOKEN : "token123"}
    jwt_client = JWTHandler(_props)
    assert jwt_client.check_jwt_ready()

def test_compile_headers_valid_key_missing_token():
    _props = {
        JWT_KEY : "key123"}
    jwt_client = JWTHandler(_props)
    assert jwt_client.check_jwt_ready()

def test_fail_jwt_ready_empty():
    jwt_client = JWTHandler({})
    assert jwt_client.check_jwt_ready() == False

def test_jwt_ready_missing_token_and_key():
    _props = {
        JWT_HEADERS : {"header"  : "value"},
        JWT_PAYLOAD : {"payload" : "value"},
        JWT_ALGORITHM : "RS256",
        JWT_TOKEN_TYPE : "jwt"}
    jwt_client = JWTHandler(_props)
    assert jwt_client.check_jwt_ready() == False


def test_empty_dict():
    jwt_client = JWTHandler({})
    assert jwt_client.check_jwt_ready() == False
    assert jwt_client.add_jwt_headers({}) == {'headers': {}}

def test_just_token():
    jwt_client = JWTHandler({JWT_TOKEN : "token123"})
    assert jwt_client.check_jwt_ready()
    assert jwt_client.add_jwt_headers({}) == {'headers': {'Authorization': 'bearer token123'}}

def test_token_with_custom_token_type():
    jwt_client = JWTHandler({JWT_TOKEN : "token123", JWT_TOKEN_TYPE : "lock-key"})
    assert jwt_client.check_jwt_ready()
    assert jwt_client.add_jwt_headers({}) == {'headers': {'Authorization': 'lock-key token123'}}

def test_with_jwt_key():
    jwt_client = JWTHandler({JWT_KEY : "key112233"})
    assert jwt_client.check_jwt_ready()
    processed_header = jwt_client.add_jwt_headers({})
    assert "headers" in processed_header
    assert "Authorization" in processed_header["headers"]
    assert "bearer" in processed_header["headers"]["Authorization"]

def test_with_jwt_key_custom_token_type():
    jwt_client = JWTHandler({JWT_KEY : "key112233", JWT_TOKEN_TYPE:'lock-key'})
    assert jwt_client.check_jwt_ready()
    processed_header = jwt_client.add_jwt_headers({})
    assert "headers" in processed_header
    assert "Authorization" in processed_header["headers"]
    assert "lock-key" in processed_header["headers"]["Authorization"]

def test_access_toke_already_exists():
    jwt_client = JWTHandler({JWT_KEY : "key112233", JWT_TOKEN_TYPE:'lock-key'})
    with pytest.raises(IntegrationError) as err:
        jwt_client.add_jwt_headers({HEADERS: {AUTHORIZATION_KEY : "112233"}})


def test_compile_tokens_key():
    _props = {}
    _props[JWT_KEY] = "encryptionkey"
    _props[JWT_ALGORITHM] = "HS256"
    jwt_client = JWTHandler(_props)
    jwt_client._compile_jwt_token()
    processed_token = jwt_client._jwt_properties[JWT_TOKEN]
    assert len(processed_token.split(".")) == 3
    if processed_token != 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.e30.xptMQAf_YCcAM7MSt3xifgItgCQAYUDFccm0uz-ENFc':
        assert json.loads(jwt.utils.base64url_decode(processed_token.split(".")[0])) == {"typ":"JWT","alg":"HS256"}
        assert json.loads(jwt.utils.base64url_decode("e30")) == {}

def test_compile_tokens_key_header():
    _props = {
        JWT_KEY : "encryptionkey",
        JWT_HEADERS: OrderedDict({"key1" : "value1", "key2": "value2"}),
        JWT_ALGORITHM : "HS256"
    }
    jwt_client = JWTHandler(_props)
    jwt_client._compile_jwt_token()
    processed_token = jwt_client._jwt_properties[JWT_TOKEN]
    assert len(processed_token.split(".")) == 3
    if processed_token != 'eyJhbGciOiJIUzI1NiIsImtleTEiOiJ2YWx1ZTEiLCJrZXkyIjoidmFsdWUyIiwidHlwIjoiSldUIn0.e30.yRfHHke4q-bNQ2paunR_iRBRO72KZnRSPARvYyP3kpA':
        assert json.loads(jwt.utils.base64url_decode(processed_token.split(".")[0])) == {'alg': 'HS256', 'key1': 'value1', 'key2': 'value2', 'typ': 'JWT'}
        assert json.loads(jwt.utils.base64url_decode("e30")) == {}

def test_compile_tokens_key_header_payload():
    _props = {
        JWT_KEY : "encryptionkey",
        JWT_HEADERS : OrderedDict({"key1" : "value1", "key2": "value2"}),
        JWT_PAYLOAD : OrderedDict({"key1" : "value1", "key2": "value2"}),
        JWT_ALGORITHM : "HS256"
    }
    jwt_client = JWTHandler(_props)
    jwt_client._compile_jwt_token()
    processed_token = jwt_client._jwt_properties[JWT_TOKEN]
    assert len(processed_token.split(".")) == 3
    if processed_token != 'eyJhbGciOiJIUzI1NiIsImtleTEiOiJ2YWx1ZTEiLCJrZXkyIjoidmFsdWUyIiwidHlwIjoiSldUIn0.eyJrZXkxIjoidmFsdWUxIiwia2V5MiI6InZhbHVlMiJ9.Vl6UkvGJycRS9uwraqmLPQnU44vp-MtTG7PyXzIZfqM':
        assert json.loads(jwt.utils.base64url_decode(processed_token.split(".")[0])) == {'alg': 'HS256', 'key1': 'value1', 'key2': 'value2', 'typ': 'JWT'}
        assert json.loads(jwt.utils.base64url_decode(processed_token.split(".")[1])) == {"key1":"value1","key2":"value2"}
