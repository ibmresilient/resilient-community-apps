# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

from oscrypto import asymmetric
from smail import sign_message, encrypt_message
from resilient_lib import s_to_b

def _get_private_key(private_pem: bytes, private_key_password: str=None):
    """load a private key into the oscrypto.asymmetric.PrivateKey format

    :param private_pem: byte content of the private key
    :type private_pem: bytes
    :param private_key_password: password for private key, if needed, defaults to None
    :type private_key_password: str, optional
    :return: private key
    :rtype: oscrypto.asymmetric.PrivateKey
    """
    if private_pem:
        return asymmetric.load_private_key(private_pem, private_key_password)



def _get_file(file_path: str):
    """read contents of a file into byte format

    :param file_path: /path/to/file
    :type file_path: str
    :return: byte format of file contents
    :rtype: bytes
    """
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as f:
            return s_to_b(f.read())

def get_private_key_from_file(private_pem_file_path: str, private_key_password=None):
    """load a private key into the oscrypto.asymmetric.PrivateKey format

    :param private_pem_file_path: /path/to/private.key
    :type private_pem: str
    :param private_key_password: password for private key, if needed, defaults to None
    :type private_key_password: str, optional
    :return: private key
    :rtype: oscrypto.asymmetric.PrivateKey
    """
    return _get_private_key(_get_file(private_pem_file_path), private_key_password=private_key_password)

def get_public_key_from_file(public_pem_file_path: str):
    """load a public certificate into oscrypto.asymmetric.PublicKey

    :param public_pem_file_path: /path/to/public.crt
    :type public_pem_file_path: str
    :return: public key
    :rtype:  bytes
    """
    return _get_file(public_pem_file_path) # future ability to convert to an object


def sign_email_message(message, key_signer, cert_signer):
    """Sign the email message using the email sender's private key

    :param message: message to encrypt
    :type message: MultiPart object
    :param key_signer: sender's private key
    :type key_signer: oscrypto.asymmetric.PrivateKey
    :param cert_signer: public certificate
    :type cert_signer: bytes
    :return: Signed message
    :rtype: MultiPart
    """
    return sign_message(message, key_signer, cert_signer)

def encrypt_email_message(message, cert_list: list):
    """Encrypt the message using the recipient(s) public key

    :param message: message to encrypt
    :type message: MultiPart
    :param cert_list: list of recipient public certifcates in PEM format
    :type cert_list: list
    :return: encrypted message
    :rtype: MultiPart
    """
    return encrypt_message(message, cert_list)
