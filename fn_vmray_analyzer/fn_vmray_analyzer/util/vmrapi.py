import time
import random

import requests
import logging

log = logging.getLogger(__name__)


class SandboxError(Exception):
    """
    Custom exception class to be raised by known errors in SandboxAPI and its
    subclasses, and caught where this library is used.
    """
    pass


class VMRayAPI(object):
    """Sandbox API wrapper base class."""

    def __init__(self, api_key, url=None, verify_ssl=True, proxies=None, **kwargs):
        """Initialize the interface to Sandbox API.
        :type  proxies: dict
        :param proxies: Optional proxies dict passed to requests calls.
        """

        self.base_url = url or 'https://cloud.vmray.com'
        self.api_url = self.base_url + '/rest'

        # assume is *not* available.
        self.server_available = False

        # turn SSL verify on by default
        self.verify_ssl = True

        self.proxies = None or proxies

        self.api_key = api_key
        self.verify_ssl = verify_ssl

        # define once and use later
        self.headers = {'Authorization': 'api_key {a}'.format(a=api_key)}

    def _request(self, uri, method='GET', params=None, files=None, headers=None, auth=None):
        """Robustness wrapper. Tries up to 3 times to dance with the Sandbox API.
        :type  uri:     str
        :param uri:     URI to append to base_url.
        :type  params:  dict
        :param params:  Optional parameters for API.
        :type  files:   dict
        :param files:   Optional dictionary of files for multipart post.
        :type  headers: dict
        :param headers: Optional headers to send to the API.
        :type  auth:    dict
        :param auth:    Optional authentication object to send to the API.
        :rtype:  requests.response.
        :return: Response object.
        :raises SandboxError: If all attempts failed.
        """

        # make up to three attempts to dance with the API, use a jittered
        # exponential back-off delay
        for i in range(3):
            try:
                full_url = '{b}{u}'.format(b=self.api_url, u=uri)

                response = None
                if method == 'POST':
                    response = requests.post(full_url, data=params, files=files, headers=headers,
                                             verify=self.verify_ssl, auth=auth, proxies=self.proxies)
                else:
                    response = requests.get(full_url, params=params, headers=headers,
                                            verify=self.verify_ssl, auth=auth, proxies=self.proxies)

                # if the status code is 503, is no longer available.
                if response.status_code >= 500:
                    # server error
                    self.server_available = False
                    raise SandboxError("server returned {c} status code on {u}, assuming unavailable...".format(
                        c=response.status_code, u=response.url))
                else:
                    return response

            # 0.4, 1.6, 6.4, 25.6, ...
            except requests.exceptions.RequestException:
                time.sleep(random.uniform(0, 4 ** i * 100 / 1000.0))

        # if we couldn't reach the API, we assume that the box is down and lower availability flag.
        self.server_available = False

        # raise an exception.
        msg = "exceeded 3 attempts with sandbox API: {u}, p:{p}, f:{f}".format(u=full_url,
                                                                               p=params, f=files)
        try:
            msg += "\n" + response.content.decode('utf-8')
        except AttributeError:
            pass

        raise SandboxError(msg)

    def analyze(self, handle, filename):
        """Submit a file for analysis.
        :type  handle:   File handle
        :param handle:   Handle to file to upload for analysis.
        :type  filename: str
        :param filename: File name.
        :rtype:  str
        :return: File ID as a string
        """
        # multipart post files.
        files = {"sample_file": (filename, handle)}
        log.info("files: " + str(files))

        # ensure the handle is at offset 0.
        handle.seek(0)

        response = self._request("/sample/submit", method='POST', files=files, headers=self.headers)
        log.info("response after submit a file to VMRay Analyzer: ")
        log.info(response.json())
        try:
            if response.status_code == 200:
                # if response.status_code == 200 and not response.json()['data']['errors']:
                # only support single-file submissions; just grab the first one.
                return response.json()['data']['samples'][0]['sample_id']
            else:
                raise SandboxError("api error in analyze ({u}): {r}".format(u=response.url, r=response.content))
        except (ValueError, KeyError, IndexError) as e:
            raise SandboxError("error in analyze: {e}".format(e=e))

    def check(self, sample_id):
        """Check if an analysis is complete.
        :type  sample_id: str
        :param sample_id_id: File ID to check.
        :rtype:  bool
        :return: Boolean indicating if a report is done or not.
        """
        response = self._request("/submission/sample/{sample_id}".format(sample_id=sample_id), headers=self.headers)

        if response.status_code == 404:
            # unknown id
            return False

        try:
            finished = False
            for submission in response.json()['data']:
                finished = finished or submission['submission_finished']
            if finished:
                return True

        except (ValueError, KeyError) as e:
            raise SandboxError(e)

        return False

    def is_available(self):
        """Determine if the VMRay API server is alive.
        :rtype:  bool
        :return: True if service is available, False otherwise.
        """
        # if the availability flag is raised, return True immediately.
        # NOTE: subsequent API failures will lower this flag. we do this here
        # to ensure we don't keep hitting VMRay with requests while
        # availability is there.
        if self.server_available:
            return True

        # otherwise, we have to check with the cloud.
        else:
            try:
                response = self._request("/system_info", headers=self.headers)

                # we've got vmray.
                if response.status_code == 200:
                    self.server_available = True
                    return True

            except SandboxError:
                pass

        self.server_available = False
        return False

    def report(self, sample_id, report_format="json"):
        """Retrieves the specified report for the analyzed item, referenced by item_id.
        Available formats include: json.
        :type  sample_id:       str
        :param sample_id:       File ID number
        :type  report_format: str
        :param report_format: Return format
        :rtype:  dict
        :return: Dictionary representing the JSON parsed data or raw, for other
                 formats / JSON parsing failure.
        """

        if report_format == "html":
            return "Report Unavailable"

        # grab an analysis id from the submission id.
        response = self._request("/analysis/sample/{sample_id}".format(sample_id=sample_id),
                                 headers=self.headers)

        log.info("sample_report:  " + str(response.json()) + "\n")

        try:
            # the highest score is probably the most interesting.
            # vmray uses this internally with sample_highest_vti_score so this seems like a safe assumption.
            analysis_id = 0
            top_score = -1
            for analysis in response.json()['data']:
                if analysis['analysis_vti_score'] > top_score:
                    top_score = analysis['analysis_vti_score']
                    analysis_id = analysis['analysis_id']


        except (ValueError, KeyError) as e:
            raise SandboxError(e)

        # assume report format json.
        response = self._request("/analysis/{analysis_id}/archive/logs/summary.json".format(analysis_id=analysis_id),
                                 headers=self.headers)
        archive = self._request("/analysis/{analysis_id}/archive".format(analysis_id=analysis_id), headers=self.headers)

        # if response is JSON, return it as an object.
        try:
            return analysis_id, response.json(), archive.content
        except ValueError:
            pass

        # otherwise, return the raw content.
        return analysis_id, response.content, archive.content

    def score(self, report):
        """Pass in the report from self.report(), get back an int 0-100"""
        try:
            return report['vti']['vti_score']
        except KeyError:
            return 0
