# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

from asn1crypto import x509
from oscrypto import asymmetric
from smail import sign_message, encrypt_message
from resilient_lib import s_to_b

def _get_private_key(private_pem: bytes, private_key_password: str=None):
    if private_pem:
        return asymmetric.load_private_key(private_pem, private_key_password)


def _get_public_key(public_pem: str):
    if public_pem:
        return asymmetric.load_certificate(public_pem)


def _get_file(file_path: str):
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as f:
            return s_to_b(f.read())

def get_private_key_from_file(private_pem_file_path: str, private_key_password=None):
    return _get_private_key(_get_file(private_pem_file_path), private_key_password=private_key_password)

def get_public_key_from_file(public_pem_file_path: str):
    return public_pem_file_path #_get_public_key(_get_file(public_pem_file_path))

def _get_x509_certificate(cert: bytes):
    return x509.Certificate.load(cert)

def sign_email_message(message, key_signer, cert_signer):
    return sign_message(message, key_signer, cert_signer)

def encrypt_email_message(message, cert_list: list):
    return encrypt_message(message, cert_list)
