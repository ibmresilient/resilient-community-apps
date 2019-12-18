# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Class for Resilient circuits Functions supporting REST API client for Proofpoint TRAP  """
import logging
import json
import datetime as dt
from datetime import datetime
from sys import version_info
import os
import requests
if version_info.major < 3:
    from urlparse import urljoin
else:
    from urllib.parse import urljoin

try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

from resilient_lib import RequestsCommon
from resilient_lib.components.integration_errors import IntegrationError

LOG = logging.getLogger(__name__)

def timestamp_minutes_ago(minutes):
    """
    Return ISO 8601 Timestamp of X minutes ago
    :param minutes:
    :return:
    """
    now = dt.datetime.now()
    past = now - dt.timedelta(minutes=minutes)
    return past.isoformat()

def incident_details_exception_handler(response):
    """ Callback to process incident details HTTPError exceptions.

    :param response: Request response.
    :return:
    """
    try:
        response.raise_for_status()

        # Return requests.Response object
        return response

    except requests.exceptions.HTTPError as err:
        if err.response.content is not None:
            try:
                custom_error_content = json.loads(err.response.content)
            except JSONDecodeError:
                raise ValueError(err)  # raise ValueError(custom_error_content)
            return custom_error_content
        raise ValueError(err)


def incidents_exception_handler(response):
    """ Callback to process incident details HTTPError exceptions.

    :param response: Request response.
    :return:
    """
    try:
        response.raise_for_status()

        # Return requests.Response object
        return response

    except requests.exceptions.HTTPError as err:
        if err.response.content is not None:
            try:
                custom_error_content = json.loads(err.response.content)
            except JSONDecodeError:
                return {'error': '{}'.format(err)}
            return custom_error_content
        return {'error': 'HTTP error {}'.format(err)}

class PPTRClient(object):
    """
    Client class used to expose Proof Point TRAP api.
    """
    def __init__(self, options, function_options=None):
        """
        Class constructor
        """
        self.base_url = function_options['base_url']
        self.api_key = function_options['api_key']
        cafile = function_options.get('cafile', False)
        self.bundle = os.path.expanduser(cafile) if cafile else False
        # Rest request endpoints
        self._endpoints = {
            # REST endpoints
            "incident":         "/incidents/{}.json",
            "incidents":        "/incidents",
            "list_member":      "/lists/{}/members/{}.json",
            "list_members":     "/lists/{}/{}",
            "add_members":      "/lists/{}/members.json",
        }
        self._req = RequestsCommon(options, function_options)
        self._headers = {"Authorization": "{0}".format(self.api_key)}

    def get_incidents(self, lastupdate=None):
        """Get incidents in TRAP. The amount of incidends returned can be filtered by parameter lastupdate.

        :param lastupdate: - Minutes since last update
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["incidents"])
        params = {}
        if type(lastupdate) is int:
            params['created_after'] = timestamp_minutes_ago(lastupdate)
        else:
            if lastupdate is None:
                # first run, fetch all
                LOG.info("First Run in progress - this may take a while.")
        try:
            r = self._req.execute_call_v2('get', url, callback=incidents_exception_handler, headers=self._headers,
                                          params=params, verify=self.bundle, proxies=self._req.get_proxies())

        except IntegrationError as ierr:
            msg = str(ierr)
            return {'error': 'Request to {0} failed with error {1}.'.format(url, msg)}

        # If an error caught in the error handler return the error dict.
        if "error" in r:
            return r

        try:
            return r.json()
        except ValueError:
            # Default response likely not in json format just return content as is.
            return r.content
        return r

    def get_incident_details(self, incident_id=None):
        """Get incident details for an  incident id.

        :param incident_id: - Incident id for request.
        :return Result in json format.
        """
        rtn = {}
        url = urljoin(self.base_url, self._endpoints["incident"]).format(incident_id)

        try:
            r = self._req.execute_call_v2('get', url, callback=incident_details_exception_handler,
                                          headers=self._headers, verify=self.bundle, proxies=self._req.get_proxies())

        except IntegrationError as ierr:
            msg = str(ierr)
            raise Exception('Request to {0} failed with error {1}.'.format(url, msg))

        if isinstance(r, dict) and "error" in r:
            return r
        else:
            rtn['href'] = url
            try:
                rtn['data'] = r.json()
            except ValueError:
                # Default response likely not in json format just return content as is.
                rtn['data'] = r.content
            return rtn

    def get_list_members(self, list_id=None, member_id=None, members_type=None):
        """Gets member(s) from a list.

        :param list_id: The id value of a list (integer).
        :param member_id: The id of a member of a list (integer).
        :param members_type: The information format to get in return. (path).
                                include: members.pan (for published lists)
                                         members.bluecoat (for published lists)
                                         members.json.
        :return Result in json format.
        """
        if member_id is not None:
            url = urljoin(self.base_url, self._endpoints["list_member"]).format(list_id, member_id)
        else:
            url = urljoin(self.base_url, self._endpoints["list_members"]).format(list_id, members_type)

        r = self._req.execute_call_v2('get', url, verify=self.bundle, headers=self._headers, proxies=self._req.get_proxies())
        try:
            return r.json()
        except ValueError:
            # Default response likely not in json format just return content as is.
            return r.content
        return r


    def add_list_member(self, list_id=None, member=None, description=None, expiration=None, duration=None):
        """Add members to a list.

        :param list_id: The id value of a list (integer).
        :param member: Member to add (string). Can host, IP address, or URL to a list.
        :param description: Description of Proofpoint TRAP list member (string)
        :param expiration: Timestamp to expire Proofpoint TRAP list member (Unix type timestamp).
        :param duration: Number of minutes after which to expire Proofpoint TRAP list membership (integer).
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["add_members"]).format(list_id)
        # Convert expiration timestamp to UTC format.
        if expiration is not None:
            expiration = datetime.utcfromtimestamp(int(str(expiration)[0:-3])).strftime('%Y-%m-%dT%H:%M:%SZ')

        if duration is not None:
            # Convert parameter (in minutes) to milliseconds for api.
            duration = int(duration) * 60 * 1000

        payload = json.dumps({
                "member": member, "description": description, "expiration": expiration, "duration": duration
            }
        )
        r = self._req.execute_call_v2('post', url, verify=self.bundle, headers=self._headers, json=payload, proxies=self._req.get_proxies())
        try:
            return r.json()
        except ValueError:
            # Default response likely not in json format just return content as is.
            return r.content
        return r

    def update_list_member(self, list_id=None, member_id=None, description=None, expiration=None, duration=None):
        """Update member of a list.

        :param list_id: The id value of a list (integer).
        :param member: The id of a member of a list (integer).
        :param description: Description of Proofpoint TRAP list member (string).
        :param expiration: Timestamp to expire Proofpoint TRAP list member (Unix type timestamp).
        :param duration: Number of minutes after which to expire Proofpoint TRAP list membership (integer).
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["list_member"]).format(list_id, member_id)
        # Convert expiration timestamp to UTC format.
        if expiration is not None:
            expiration = datetime.utcfromtimestamp(int(str(expiration)[0:-3])).strftime('%Y-%m-%dT%H:%M:%SZ')

        if duration is not None:
            # Convert parameter (in minutes) to milliseconds for api.
            duration = int(duration) * 60 * 1000

        payload = json.dumps({
                "description": description, "expiration": expiration, "duration": duration
            }
        )
        r = self._req.execute_call_v2('put', url, verify=self.bundle, headers=self._headers, json=payload, proxies=self._req.get_proxies())
        try:
            return r.json()
        except ValueError:
            # Default response likely not in json format just return content as is.
            return r.content
        return r

    def delete_list_member(self, list_id=None, member_id=None):
        """Delete member from a list.

        :param list_id: The id value of a list (integer).
        :param member_id: The id of a member of a list (integer).
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["list_member"]).format(list_id, member_id)

        r = self._req.execute_call_v2('delete', url, verify=self.bundle, headers=self._headers, proxies=self._req.get_proxies())
        try:
            return r.json()
        except ValueError:
            # Default response likely not in json format just return content as is.
            # Covert bypes to string fro python 3.
            if version_info.major < 3:
                return r.content
            else:
                return r.content.decode('utf-8')

        return r