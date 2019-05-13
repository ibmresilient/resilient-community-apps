# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
import base64
import logging
from requests import request, HTTPError
import re
from zipfile import ZipFile
from io import BytesIO
import xml.etree.ElementTree as ET
try:
    from urllib.parse import urljoin
except:
    from urlparse import urljoin

LOG = logging.getLogger(__name__)
# Magic number for zip file
ZIP_MAGIC = "\x50\x4b\x03\x04"

class RequestsSep(object):
    """
    This class inherits from class RequestsCommon and over-rides the execute_call method.
    The class will be used to manage REST calls.

    """
    def __init__(self, opts=None, function_opts=None):
        # capture the properties for the integration as well as the global settings for all integrations for proxy urls
        self.integration_options = opts.get('integrations', None) if opts else None
        self.function_opts = function_opts

    def get_proxies(self):
        """ proxies can be specified globally for all integrations or specifically per function """
        proxies = None
        if self.integration_options and (self.integration_options.get("http_proxy") or self.integration_options.get("https_proxy")):
            proxies = {'http': self.integration_options.get("http_proxy"), 'https': self.integration_options.get("https_proxy")}

        if self.function_opts and (self.function_opts.get("http_proxy") or self.function_opts.get("https_proxy")):
            proxies = {'http': self.function_opts.get("http_proxy"), 'https': self.function_opts.get("https_proxy")}

        return proxies

    def execute_call(self, verb, url, params=None, data=None, json=None, log=None, basicauth=None, verify_flag=True,
                     headers=None, proxies=None, timeout=None, stream=False):
        """Method which initiates the REST API call. Default method is the GET method also supports POST, PATCH and
        DELETE. Retries are attempted if a Rate limit exception (429) is  detected.

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
                        re.match("^https://.*/sepm/api/v1/policy-objects/fingerprints.*$", url, ):
                        # We are probably trying to access/delete fingerprint list which doesn't exist.
                    LOG.error("Got '410' error, possible attempt to {} a fingerprint list which doesn't exist."
                              .format(verb))
                    # Allow error to bubble up to the Resilient function.
                    pass
                elif e.response.status_code == 409 and verb.upper() in ["POST"] and \
                        re.match("^https://.*/sepm/api/v1/policy-objects/fingerprints.*$", url, ):
                        # We are probably trying to re-add a hash to fingerprint list which already exists.
                    LOG.error("Got '409' error, possible attempt to re-add a hash to a fingerprint list.")
                    # Allow error to bubble up to the Resilient function.
                    pass
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
        key = c_unzipped = None
        try:
            zfile = ZipFile(BytesIO(content), 'r')
            for file in zfile.namelist():
                if len(file) in [64, 40, 32] or file == "metadata.xml":
                    f = zfile.open(file)
                    if len(file) in [64, 40, 32]:
                        # Get the hash file name.
                        c_unzipped = f.read()
                    elif file == "metadata.xml":
                        # Get the key.
                        meta = ET.fromstring(f.read().encode('utf8', 'ignore'))
                        for item in meta.findall('File'):
                            key = item.attrib["Key"]
                else:
                    raise ValueError('Unknown hash type or key for zipfile contents: ' + file)

            return (key, c_unzipped)

        except ET.ParseError as e:
            LOG.error("There was an error trying to process content XML.", e.__repr__(), e.message)
            raise e

    @staticmethod
    def decrypt_xor(data, key):
        """ Unencrypt XORed data.

        :param data: XORed zip file data.
        :return: Unencrypted data.
        """
        data = bytearray(data)
        for i in xrange(len(data)):
            data[i] ^= int(key)
        return data