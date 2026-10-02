# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long

import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.x509 import Certificate as x509Certificate, ExtensionNotFound, oid
from email.mime.multipart import MIMEMultipart
from logging import getLogger
from smail import sign_message, encrypt_message
from resilient_lib import s_to_b

LOG = getLogger(__name__)

def convert_base64(contents: bytes) -> bytes:
    """determine if data is base64 encoded, and if so, return the decoded content

    :param contents: content which may or may not be base64 encoded
    :type contents: bytes
    :return: decoded data
    :rtype: bytes
    """
    if contents:
        try:
            decoded_contents = base64.b64decode(contents)
            # using 'in' as last char may be \n
            return decoded_contents if base64.b64encode(decoded_contents) in contents else contents
        except Exception:
            return contents

def get_p12_info(file_path: str, private_key: str):
    """read the signer p12 certificate and return the parts

    :param file_path: /path/to/cert.p12
    :type file_path: str
    :param private_key: private key to decode cert
    :type private_key: str
    :return: private_key, public_cert and additional certificates
    :rtype: serialization.RSAPrivateKey, x509.Certificate, [list of additional x509.Certificates]
    """
    if not file_path:
        return None, None, None

    # get cert data - it may be in base64 format
    p12_cert = convert_base64(_get_file(file_path, mode='rb', return_bytes=False))

    if p12_cert:
        private_key, certificate, additional_certificates = serialization.pkcs12.load_key_and_certificates(
            p12_cert,
            s_to_b(private_key)
        )

        return private_key, certificate, additional_certificates
    else:
        LOG.error(f"No certificate information decoded for filepath: {file_path}")
        return None, None, None

def _get_file(file_path: str, mode='r', return_bytes=True) -> bytes:
    """read contents of a file into byte format

    :param file_path: /path/to/file
    :type file_path: str
    :param mode: file access mode: r, rb, etc.
    :param mode: str
    :param return_bytes: True to convert str as bytes
    :param bool
    :return: byte format of file contents if return_bytes=True
    :rtype: Any
    """
    if file_path:
        with open(file_path, mode) as f:
            result = f.read()
            return s_to_b(result) if return_bytes else result

def sign_email_message(message: MIMEMultipart,
                       key_signer: RSAPrivateKey,
                       cert_signer: x509Certificate,
                       additional_certs: list) -> MIMEMultipart:
    """Sign the email message using the email sender's private key

    :param message: message to encrypt
    :type message: MIMEMultipart
    :param cert_signer: public certificate
    :type cert_signer: bytes
    :param additional_certs: additional certificates to include in the signature
    :type additional_certs: list[x509Certificate]
    :return: Signed message
    :rtype: MIMEMultipart
    """
    # convert to bytes for compatible format to sign_message
    private_pem = key_signer.private_bytes(serialization.Encoding.PEM,
                                           serialization.PrivateFormat.TraditionalOpenSSL,
                                           serialization.NoEncryption())

    additional_certs_pem = [cert.public_bytes(serialization.Encoding.PEM)  for cert in additional_certs] \
        if additional_certs else []

    return sign_message(message,
                        private_pem,
                        cert_signer.public_bytes(serialization.Encoding.PEM),
                        additional_certs=additional_certs_pem)

def encrypt_email_message(message: MIMEMultipart, cert_list: list) -> MIMEMultipart:
    """Encrypt the message using the recipient(s) public key

    :param message: message to encrypt
    :type message: MIMEMultipart
    :param cert_list: list of recipient public certificates in PEM format
    :type cert_list: list[bytes]
    :return: encrypted message
    :rtype: MIMEMultipart
    """
    return encrypt_message(message, cert_list)

def get_extended_key_usage_from_certificate(certificate: x509Certificate):
    """
    Given an X.509 certificate, extract and return the extendedKeyUsage
    extension.
    """
    if not certificate:
        return []

    try:
        return certificate.extensions.get_extension_for_oid(
            oid.ExtensionOID.EXTENDED_KEY_USAGE
        ).value
    except ExtensionNotFound:
        return []

def isUsageValid(certificate: x509Certificate, test_usage=oid.ExtendedKeyUsageOID.EMAIL_PROTECTION) ->bool:
    """Confirm that the certificate has the specified extension

    :param certificate: certificate to verify
    :type certificate: x509Certificate
    :param test_usage: extension to validate, defaults to oid.ExtendedKeyUsageOID.EMAIL_PROTECTION
    :type test_usage: oid.ExtendedKeyUsageOID, optional
    :return: True if the certificate extension is found
    :rtype: bool
    """
    usages = get_extended_key_usage_from_certificate(certificate)
    return bool(test_usage in usages)
