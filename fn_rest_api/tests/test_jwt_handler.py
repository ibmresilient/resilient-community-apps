import unittest, pytest

from collections import OrderedDict
from resilient_lib import IntegrationError
from fn_rest_api.lib.authentication_handler import JWTHandler
from fn_rest_api.lib.authentication_handler import JWT_KEY, JWT_TOKEN, JWT_HEADERS, JWT_PAYLOAD, \
    JWT_ALGORITHM, JWT_TOKEN_TYPE, DEFAULT_JWT_ENCRYPTION_ALGORITHM, AUTHORIZATION_KEY, HEADERS

class TestJWT(unittest.TestCase):

    def test_jwt_constants(self):
        """ Check to see if any of the constants values required for JWT are changed """
        assert JWT_KEY == "key"
        assert JWT_TOKEN == "token"
        assert JWT_HEADERS == "headers"
        assert JWT_PAYLOAD == "payload"
        assert JWT_ALGORITHM == "algorithm"
        assert JWT_TOKEN_TYPE == "token_type"
        assert DEFAULT_JWT_ENCRYPTION_ALGORITHM == "HS256"

    def test_jwt_constructor(self):
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
        self.assertDictEqual(_props, jwt_client._jwt_properties)

    def test_compile_headers_jwt_token_type(self):
        _props = {
            JWT_TOKEN : "token123",
            JWT_TOKEN_TYPE : "jwt"}
        jwt_client = JWTHandler(_props)
        assert jwt_client._compile_headers() == {'Authorization': 'jwt token123'}

    def test_compile_headers_bearer_token_type(self):
        _props = {
            JWT_TOKEN : "token123",
            JWT_TOKEN_TYPE : "bearer" }
        jwt_client = JWTHandler(_props)
        assert jwt_client._compile_headers() == {'Authorization': 'bearer token123'}

    def test_compile_headers_valid_token_missing_key(self):
        _props = {
            JWT_TOKEN : "token123"}
        jwt_client = JWTHandler(_props)
        assert jwt_client._check_jwt_ready()

    def test_compile_headers_valid_key_missing_token(self):
        _props = {
            JWT_KEY : "key123"}
        jwt_client = JWTHandler(_props)
        assert jwt_client._check_jwt_ready()

    def test_fail_jwt_ready_empty(self):
        jwt_client = JWTHandler({})
        self.assertFalse(jwt_client._check_jwt_ready())

    def test_jwt_ready_missing_token_and_key(self):
        _props = {
            JWT_HEADERS : {"header"  : "value"},
            JWT_PAYLOAD : {"payload" : "value"},
            JWT_ALGORITHM : "RS256",
            JWT_TOKEN_TYPE : "jwt"}
        jwt_client = JWTHandler(_props)
        assert jwt_client._check_jwt_ready() == False


class TestAddJWTHeaders(unittest.TestCase):

    def test_empty_dict(self):
        jwt_client = JWTHandler({})
        self.assertFalse(jwt_client._check_jwt_ready())
        self.assertDictEqual(jwt_client.add_jwt_headers({}), {'headers': {}})

    def test_just_token(self):
        jwt_client = JWTHandler({JWT_TOKEN : "token123"})
        assert jwt_client._check_jwt_ready()
        self.assertDictEqual(jwt_client.add_jwt_headers({}), {'headers': {'Authorization': 'bearer token123'}})

    def test_token_with_custom_token_type(self):
        jwt_client = JWTHandler({JWT_TOKEN : "token123", JWT_TOKEN_TYPE : "lock-key"})
        assert jwt_client._check_jwt_ready()
        self.assertDictEqual(jwt_client.add_jwt_headers({}), {'headers': {'Authorization': 'lock-key token123'}})
    
    def test_with_jwt_key(self):
        jwt_client = JWTHandler({JWT_KEY : "key112233"})
        assert jwt_client._check_jwt_ready()
        self.assertDictEqual(jwt_client.add_jwt_headers({}), {'headers': {'Authorization': 'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.e30.KFMTstbOO6XBZ8GRoPFQc5NO9SxSLuYunIK9SPdPVBo'}})

    def test_with_jwt_key_custom_token_type(self):
        jwt_client = JWTHandler({JWT_KEY : "key112233", JWT_TOKEN_TYPE:'lock-key'})
        assert jwt_client._check_jwt_ready()
        self.assertDictEqual(jwt_client.add_jwt_headers({}), {'headers': {'Authorization': 'lock-key eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.e30.KFMTstbOO6XBZ8GRoPFQc5NO9SxSLuYunIK9SPdPVBo'}})

    def test_access_toke_already_exists(self):
        jwt_client = JWTHandler({JWT_KEY : "key112233", JWT_TOKEN_TYPE:'lock-key'})
        with pytest.raises(IntegrationError) as err:
            jwt_client.add_jwt_headers({HEADERS: {AUTHORIZATION_KEY : "112233"}})


class TestCompileJWTTokens(unittest.TestCase):
    def test_compile_tokens_key(self):
        _props = OrderedDict({
            JWT_KEY : "encryptionkey",
            JWT_ALGORITHM : "HS256"
        })
        jwt_client = JWTHandler(_props)
        jwt_client._compile_jwt_token()
        assert len(jwt_client._jwt_properties[JWT_TOKEN].split(".")) == 3
        assert jwt_client._jwt_properties[JWT_TOKEN] == 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.e30.xptMQAf_YCcAM7MSt3xifgItgCQAYUDFccm0uz-ENFc'

    def test_compile_tokens_key_header(self):
        _props = OrderedDict({
            JWT_KEY : "encryptionkey",
            JWT_HEADERS: OrderedDict({"key1" : "value1", "key2": "value2"}),
            JWT_ALGORITHM : "HS256"
        })
        jwt_client = JWTHandler(_props)
        jwt_client._compile_jwt_token()
        assert len(jwt_client._jwt_properties[JWT_TOKEN].split(".")) == 3
        assert jwt_client._jwt_properties[JWT_TOKEN] == 'eyJhbGciOiJIUzI1NiIsImtleTEiOiJ2YWx1ZTEiLCJrZXkyIjoidmFsdWUyIiwidHlwIjoiSldUIn0.e30.yRfHHke4q-bNQ2paunR_iRBRO72KZnRSPARvYyP3kpA'

    def test_compile_tokens_key_header_payload(self):
        _props = OrderedDict({
            JWT_KEY : "encryptionkey",
            JWT_HEADERS : OrderedDict({"key1" : "value1", "key2": "value2"}),
            JWT_PAYLOAD : OrderedDict({"key1" : "value1", "key2": "value2"}),
            JWT_ALGORITHM : "HS256"
        })
        jwt_client = JWTHandler(_props)
        jwt_client._compile_jwt_token()
        assert len(jwt_client._jwt_properties[JWT_TOKEN].split(".")) == 3
        assert jwt_client._jwt_properties[JWT_TOKEN] == 'eyJhbGciOiJIUzI1NiIsImtleTEiOiJ2YWx1ZTEiLCJrZXkyIjoidmFsdWUyIiwidHlwIjoiSldUIn0.eyJrZXkxIjoidmFsdWUxIiwia2V5MiI6InZhbHVlMiJ9.Vl6UkvGJycRS9uwraqmLPQnU44vp-MtTG7PyXzIZfqM'
