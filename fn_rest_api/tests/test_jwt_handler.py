from fn_rest_api.lib.authentication_handler import JWTHandler
from fn_rest_api.lib.authentication_handler import JWT_KEY, JWT_TOKEN, JWT_HEADERS, JWT_PAYLOAD, \
    JWT_ALGORITHM, JWT_TOKEN_TYPE, DEFAULT_JWT_ENCRYPTION_ALGORITHM

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


def test_compile_headers():
    _props = {
        JWT_TOKEN : "token123",
        JWT_TOKEN_TYPE : "jwt"}

    jwt_client = JWTHandler(_props)
    assert jwt_client._compile_headers() == {'Authorization': 'jwt token123'}
    
    _props = {
        JWT_TOKEN : "token123",
        JWT_TOKEN_TYPE : "bearer" }

    jwt_client = JWTHandler(_props)
    assert jwt_client._compile_headers() == {'Authorization': 'bearer token123'}


def test_compile_headers():
    _props = {
        JWT_TOKEN : "token123"}
    jwt_client = JWTHandler(_props)
    assert jwt_client._check_jwt_ready()

    _props = {
        JWT_KEY : "key123"}
    jwt_client = JWTHandler(_props)
    assert jwt_client._check_jwt_ready()

    jwt_client = JWTHandler({})
    assert jwt_client._check_jwt_ready() == False
    
    _props = {
        JWT_HEADERS : {"header"  : "value"},
        JWT_PAYLOAD : {"payload" : "value"},
        JWT_ALGORITHM : "RS256",
        JWT_TOKEN_TYPE : "jwt"}
    assert jwt_client._check_jwt_ready() == False