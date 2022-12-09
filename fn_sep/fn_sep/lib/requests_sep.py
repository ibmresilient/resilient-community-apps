# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long

""" Process https requests """
import logging
import re
import xml.etree.ElementTree as ET
from zipfile import ZipFile
from io import BytesIO
from sys import version_info
from resilient_lib import RequestsCommon

LOG = logging.getLogger(__name__)
# Magic number for zip file
ZIP_MAGIC = b"\x50\x4b\x03\x04"
# Hash lengths: SHA256 = 64, SHA-1 = 40, MD5 = 32
HASH_LENGTHS = [64, 40, 32]


class RequestsSep(object):
    """
    The class will be used to manage REST calls.

    """
    def __init__(self, opts=None, function_opts=None):
        # capture the properties for the integration as well as the global settings for all integrations for proxy urls
        self.integration_options = opts.get('integrations', None) if opts else None
        self.base_path = opts.get("sep_base_path")
        self.function_opts = function_opts

        self.rc = RequestsCommon(opts, function_opts)

    def execute_call(self, verb, url, **kwargs):
        """Perform REST API Call

        :param verb: put, post, get
        :type verb: str
        :param url: url to call
        :type url: str
        :param kwargs: parameters for the API call
        :type kwargs: dict
        :return: dict
        :rtype: result of API call
        """
        return self.rc.execute(verb, url,
                               callback=callback,
                               **kwargs)


def get_unzipped_contents(content):
    """ Unzip file content zip file returned in response.
    Response zip will have contents as follows:

        |- <file with hash (sha256) as name>
        |- metadata.xml

    :param content: Response content.
    :return: Tuple with Unzipped file with hash as name and key.
    """
    key = c_unzipped = meta = None
    try:
        with ZipFile(BytesIO(content), 'r') as zfile:
            for zip_file_name in zfile.namelist():
                if len(zip_file_name) in HASH_LENGTHS or zip_file_name == "metadata.xml":
                    f = zfile.open(zip_file_name)
                    if len(zip_file_name) in HASH_LENGTHS:
                        # Get the hash file name.
                        c_unzipped = f.read()
                    elif zip_file_name == "metadata.xml":
                        # Get the key.
                        if version_info.major == 3:
                            meta = ET.fromstring(f.read())
                        else:
                            meta = ET.fromstring(f.read().encode('utf8', 'ignore'))
                        for item in meta.findall('File'):
                            key = item.attrib["Key"]
                else:
                    raise ValueError('Unknown hash type or key for zipfile contents: ' + zip_file_name)
        return (key, c_unzipped)

    except ET.ParseError as e:
        LOG.error("During metadata file XML processing, Got exception type: %s, msg: %s", e.__repr__(), e.message)
        raise e

def decrypt_xor(data, key):
    """ Unencrypt XORed data.

    :param data: XORed zip file data.
    :return: Unencrypted data.
    """
    data = bytearray(data)
    for i in range(len(data)):
        data[i] ^= int(key)
    return data

def callback(response):
    if response.status_code == 410 and \
            re.findall("/policy-objects/fingerprints.*$", response.url):
        # We are probably trying to access/delete fingerprint list which doesn't exist.
        LOG.error("Got '410' error, possible attempt to access a fingerprint list which doesn't exist.")
        # Allow error to bubble up to the Resilient function.
    elif response.status_code == 400 and \
            re.findall("/groups/.*/system-lockdown/fingerprints/.*$", response.url):
        # We are probably trying to re-add a hash to fingerprint list which already exists.
        LOG.error("Got '400' error, possible attempt to access a fingerprint list which doesn't exist.")
        # Allow error to bubble up to the Resilient function.
    elif response.status_code == 409 and \
            re.findall("/policy-objects/fingerprints.*$", response.url):
        # We are probably trying to re-add a hash to fingerprint list which already exists.
        LOG.error("Got '409' error, possible attempt to re-add a hash to a fingerprint list.")
        # Allow error to bubble up to the Resilient function.
    else:
        #  Firstly check if a zip file is returned.
        key = content = None
        if response.content and response.content.startswith(ZIP_MAGIC):
            (key, content) = get_unzipped_contents(response.content)
            return decrypt_xor(content, key)

    #  Else try to see if is json.
    try:
        return response.json()
    except ValueError:
        # Default response likely not in json format just return content as is.
        return response.content
