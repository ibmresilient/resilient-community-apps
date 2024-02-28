from fn_outbound_email.lib.crypto_common import convert_base64


def test_convert_base64():
    assert b"test data" == convert_base64(b'dGVzdCBkYXRh') 
    assert b"test data" == convert_base64(b"test data")
