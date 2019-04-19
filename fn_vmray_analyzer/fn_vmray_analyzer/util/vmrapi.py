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
        msg = "exceeded 3 attempts with sandbox API: {u}, p:{p}, f:{f}".format(u=full_url, p=params, f=files)
        try:
            msg += "\n" + response.content.decode('utf-8')
        except AttributeError:
            pass
        raise SandboxError(msg)

    def submit_samples(self, handle, filename):
        """Submit a file for analysis.
        :type  handle:   File handle
        :param handle:   Handle to file to upload for analysis.
        :type  filename: str
        :param filename: File name.
        :rtype:  str
        :return: Json dict.
        """
        # multipart post files.
        files = {"sample_file": (filename, handle)}

        response = self._request("/sample/submit", method='POST', files=files, headers=self.headers)

        try:
            if response.status_code == 200:
                return response.json()['data']['samples']
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
        if self.server_available:
            return True

        # otherwise, we have to check with the cloud.
        else:
            try:
                response = self._request("/system_info", headers=self.headers)

                # VMRay is reachable!
                if response.status_code == 200:
                    self.server_available = True
                    return True
            except SandboxError:
                pass

        self.server_available = False
        return False

    def get_sample_report(self, sample_id, report_format="json"):
        """Retrieves the specified report for the sample item, referenced by sample_id.
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
        try:
            sample_report = self._request("/sample/{sample_id}".format(sample_id=sample_id),
                                          headers=self.headers)
            return sample_report.json()

        except (ValueError, KeyError) as e:
            raise SandboxError(e)

    def get_sample_anlysis_report(self, sample_id, report_format="json"):
        """Retrieves the specified report for the sample item, referenced by sample_id.
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
        try:
            sample_analysis_report = self._request("/analysis/sample/{sample_id}".format(sample_id=sample_id),
                                                   headers=self.headers)
            return sample_analysis_report.json()

        except (ValueError, KeyError) as e:
            raise SandboxError(e)

    def get_sample_reputation_report(self, sample_id, report_format="json"):
        """Retrieves the specified report for the sample item, referenced by sample_id.
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
        try:
            # grab an analysis id from the submission id.
            sample_analysis_report = self._request("/reputation_lookup/sample/{sample_id}".format(sample_id=sample_id),
                                                   headers=self.headers)

            return sample_analysis_report.json()

        except (ValueError, KeyError) as e:
            raise SandboxError(e)

    def get_analysis_report(self, analysis_id):
        """Retrieves the specified report for analysis items, referenced by analysis_id
        :type   analysis_id: str
        :param analysis_id:  Analysis ID

        :rtype: dict
        :return:    Dictionary representing the JSON parsed data or raw, for other
                 formats / JSON parsing failure.
        """
        try:
            analysis_report = self._request(
                "/analysis/{analysis_id}/archive/logs/summary.json".format(analysis_id=analysis_id),
                headers=self.headers)
        except SandboxError:
            pass

        return analysis_report.json()

    def get_analysis_report_archive(self, analysis_id):
        """Retrieve  the archive zip file for analysis object, referenced by analysis_id
        :param analysis_id:  str
        :return:  zip file
        """
        try:
            archive = self._request("/analysis/{analysis_id}/archive".format(analysis_id=analysis_id), headers=self.headers)
        except SandboxError:
            pass
        return archive.content
