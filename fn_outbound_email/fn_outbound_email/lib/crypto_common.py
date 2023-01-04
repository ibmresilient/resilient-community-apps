# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long

import base64
from cryptography.hazmat.primitives import serialization
from email.mime.multipart import MIMEMultipart
import logging
from smail import sign_message, encrypt_message
from resilient_lib import s_to_b

LOG = logging.getLogger(__name__)

def convert_base64(contents: bytes):
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
    :rtype: serialization.RSAPrivateKey, serialization.Certificate, [list of additional Certificates]
    """
    # get cert data - it may be in base64 format
    p12_cert = convert_base64(_get_file(file_path, mode='rb', return_bytes=False))

    private_key, certificate, additional_certificates = serialization.pkcs12.load_key_and_certificates(
        p12_cert,
        s_to_b(private_key)
    )

    return private_key, certificate, additional_certificates

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

    return None

def sign_email_message(message: bytes,
                       key_signer,
                       cert_signer,
                       additional_certs: list) -> MIMEMultipart:
    """Sign the email message using the email sender's private key

    :param message: message to encrypt
    :type message: MultiPart object
    :param cert_signer: public certificate
    :type cert_signer: bytes
    :return: Signed message
    :rtype: MultiPart
    """
    # convert to bytes for compatible format to sign_message
    private_pem = key_signer.private_bytes(serialization.Encoding.PEM,
                                           serialization.PrivateFormat.TraditionalOpenSSL,
                                           serialization.NoEncryption())

    additional_certs_pem = [cert.public_bytes(serialization.Encoding.PEM)  for cert in additional_certs]

    return sign_message(message,
                        private_pem,
                        cert_signer.public_bytes(serialization.Encoding.PEM),
                        additional_certs=additional_certs_pem)

def encrypt_email_message(message, cert_list: list) -> MIMEMultipart:
    """Encrypt the message using the recipient(s) public key

    :param message: message to encrypt
    :type message: MultiPart
    :param cert_list: list of recipient public certifcates in PEM format
    :type cert_list: list
    :return: encrypted message
    :rtype: MultiPart
    """
    return encrypt_message(message, cert_list)
