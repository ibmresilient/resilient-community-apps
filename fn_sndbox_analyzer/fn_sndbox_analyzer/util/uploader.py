import time
import random
from StringIO import StringIO
import gzip
import json
import requests
import logging

log = logging.getLogger(__name__)


class SandboxError(Exception):
    """
    Custom exception class to be raised by known errors in SandboxAPI and its
    subclasses, and caught where this library is used.
    """
    pass


class ApiUploader(object):
    """Sandbox API wrapper base class."""

    def __init__(self, api_key, url=None, verify_ssl=True, proxies=None, **kwargs):
        """Initialize the interface to Sandbox API.
        :type  proxies: dict
        :param proxies: Optional proxies dict passed to requests calls.
        """

        self.api_url = url or 'https://api.sndbox.com'

        # turn SSL verify on by default
        self.verify_ssl = True

        self.proxies = None or proxies

        self.api_key = api_key
        self.verify_ssl = verify_ssl

    def _parse_status(self, status):
        """Parse analysis status

        check that both static and dynamic parts are done with success status (1)

        Arguments:
            status {object} -- analysis status object

        Returns:
            bool -- True if complete
        """
        static_status = status.get('static', {}).get('code', 0)
        dynamic_status = status.get('dynamic', {}).get('code', 0)
        return static_status * dynamic_status == 1

    def _request(self, uri, method='GET', params=None, files=None):
        """Robustness wrapper. Tries up to 3 times to dance with the Sandbox API.
        :type  uri:     str
        :param uri:     URI to append to api_url.
        :type  params:  dict
        :param params:  Optional parameters for API.
        :type  files:   dict
        :param files:   Optional dictionary of files for multipart post.
        :rtype:  requests.response.
        :return: Response object.
        :raises SandboxError: If all attempts failed.
        """

        # make up to three attempts to dance with the API, use a jittered
        # exponential back-off delay
        for i in range(3):
            try:
                full_url = '{b}/developers/files{u}?apikey={a}'.format(
                    b=self.api_url, u=uri, a=self.api_key)

                response = None
                if method == 'POST':
                    response = requests.post(
                        full_url, data=params, files=files, verify=self.verify_ssl, proxies=self.proxies)
                else:
                    response = requests.get(
                        full_url, params=params, verify=self.verify_ssl, proxies=self.proxies)

                # if the status code is 503, is no longer available.
                if response.status_code >= 500:
                    # server error
                    raise SandboxError("server returned {c} status code on {u}, assuming unavailable...".format(
                        c=response.status_code, u=response.url))
                else:
                    return response

            # 0.4, 1.6, 6.4, 25.6, ...
            except requests.exceptions.RequestException:
                time.sleep(random.uniform(0, 4 ** i * 100 / 1000.0))

        # raise an exception.
        msg = "exceeded 3 attempts with sandbox API: {u}, p:{p}, f:{f}".format(
            u=full_url, p=params, f=files)
        try:
            msg += "\n" + response.content.decode('utf-8')
        except AttributeError:
            pass
        raise SandboxError(msg)

    def submit_samples(self, handle, file_names):
        """Submit a file for analysis.
        :type  handle:   File handle
        :param handle:   Handle to file to upload for analysis.
        :rtype:  str
        :return: Analysis ID.
        """
        # multipart post files.
        files = {"file": handle}

        try:
            response = self._request("/", method='POST', files=files)

            if response.status_code == requests.codes.created:
                return response.json()['id']
            else:
                raise SandboxError("api error in analyze ({u}): {r}".format(
                    u=response.url, r=response.content))
        except (ValueError, KeyError, IndexError) as e:
            raise SandboxError("error in analyze: {e}".format(e=e))

    def check(self, analysis_id):
        """Check if an analysis is complete.
        :type  analysis_id: str
        :param analysis_id: Analysis ID to check.
        :rtype:  bool
        :return: Boolean indicating if a report is done or not.
        """
        response = self._request("/{}".format(analysis_id))

        if response.status_code == requests.codes.not_found:
            # unknown id
            return False

        try:
            return self._parse_status(response.json()['status'])

        except (ValueError, KeyError) as e:
            raise SandboxError(e)

        return False

    def get_sample_report(self, analysis_id):
        """Retrieves the specified report for the sample item, referenced by sample_id.
        Available formats include: json, pcap.
        :type  analysis_id:       str
        :param analysis_id:       Analysis ID number
        :rtype:  dict
        :return: Dictionary representing the JSON parsed data or raw / JSON parsing failure.
        """

        try:
            response = self._request("/{}".format(analysis_id))
            if response.status_code == requests.codes.not_found:
                # unknown id
                return False

            report = response.json()
            report['sample_url'] = 'https://app.sndbox.com/sample/' + analysis_id
            return report

        except (ValueError, KeyError) as e:
            raise SandboxError(e)
