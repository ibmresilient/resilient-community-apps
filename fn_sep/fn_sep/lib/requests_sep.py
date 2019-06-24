# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

""" Process https requests """
import logging
import re
import xml.etree.ElementTree as ET
from zipfile import ZipFile
from io import BytesIO
from sys import version_info
from requests import request, HTTPError

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
        self.base_path = opts.get("base_path")
        self.function_opts = function_opts

    def get_proxies(self):
        """ proxies can be specified globally for all integrations or specifically per function """
        proxies = None
        if self.integration_options and (self.integration_options.get("http_proxy") or self.integration_options.get("https_proxy")):
            proxies = {'http': self.integration_options.get("http_proxy"), 'https': self.integration_options.get("https_proxy")}

        if self.function_opts and (self.function_opts.get("http_proxy") or self.function_opts.get("https_proxy")):
            proxies = {'http': self.function_opts.get("http_proxy"), 'https': self.function_opts.get("https_proxy")}

        return proxies

    def execute_call(self, verb, url, params=None, data=None, json=None, basicauth=None, verify_flag=True,
                     headers=None, proxies=None, timeout=None, stream=False):
        """Method which initiates the REST API call. Default method is the GET method also supports POST, PATCH,
        PUT, DELETE AND HEAD. Retries are attempted if a Rate limit exception (429) is  detected.

        :param uri: Used to form url
        :param verb: GET, HEAD, PATCH, POST, PUT, DELETE
        :param params: Parameters used by session request to form finished request
        :param data: Data body used in post requests
        :return: Response in json format

        """

        if proxies is None:
            proxies = self.get_proxies()

        if verb.upper() in ["GET", "HEAD", "PATCH", "POST", "PUT", "DELETE"]:
            try:
                r = request(verb.upper(), url, verify=verify_flag, headers=headers, params=params,
                            auth=basicauth, timeout=timeout, stream=stream, proxies=proxies, data=data, json=json)

                r.raise_for_status()  # If the request fails throw an error.

            except HTTPError as e:
                if e.response.status_code == 410 and verb.upper() in ["GET", "DELETE"] and \
                        re.match("^https://.*"+ self.base_path + "/policy-objects/fingerprints.*$", url, ):
                        # We are probably trying to access/delete fingerprint list which doesn't exist.
                    LOG.error("Got '410' error, possible attempt to '%s' a fingerprint list which doesn't exist.",
                              verb)
                    # Allow error to bubble up to the Resilient function.
                elif e.response.status_code == 400 and verb.upper() in ["PUT"] and \
                        re.match("^https://.*"+ self.base_path + "/groups/.*/system-lockdown/fingerprints/.*$", url, ):
                        # We are probably trying to re-add a hash to fingerprint list which already exists.
                    LOG.error("Got '400' error, possible attempt to access a fingerprint list which doesn't exist.")
                    # Allow error to bubble up to the Resilient function.
                elif e.response.status_code == 409 and verb.upper() in ["POST"] and \
                        re.match("^https://.*"+ self.base_path + "/policy-objects/fingerprints.*$", url):
                        # We are probably trying to re-add a hash to fingerprint list which already exists.
                    LOG.error("Got '409' error, possible attempt to re-add a hash to a fingerprint list.")
                    # Allow error to bubble up to the Resilient function.
                else:
                    # Re-raise
                    raise
        else:
            raise ValueError("Unsupported request method '{}'.".format(verb))

        #  Firstly check if a zip file is returned.
        key = content = None
        if r.content.startswith(ZIP_MAGIC):
            (key, content) = self.get_unzipped_contents(r.content)
            return self.decrypt_xor(content, key)
        #  Else try to see if is json.
        try:
            return r.json()
        except ValueError:
            # Default response likely not in json format just return content as is.
            return r.content

    @staticmethod
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

    @staticmethod
    def decrypt_xor(data, key):
        """ Unencrypt XORed data.

        :param data: XORed zip file data.
        :return: Unencrypted data.
        """
        data = bytearray(data)
        for i in range(len(data)):
            data[i] ^= int(key)
        return data
