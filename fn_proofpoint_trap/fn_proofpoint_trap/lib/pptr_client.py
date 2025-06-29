# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=line-too-long, too-many-positional-arguments, too-many-arguments
""" Class for Resilient circuits Functions supporting REST API client for Proofpoint TRAP  """
import logging
import json
import datetime as dt
from pytz import timezone
from sys import version_info
import os
import requests
from resilient_lib import RequestsCommon
from resilient_lib.components.integration_errors import IntegrationError

try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

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
        if err.response.content:
            try:
                custom_error_content = json.loads(err.response.content)
            except JSONDecodeError:
                raise ValueError(err) from err  # raise ValueError(custom_error_content)
            return custom_error_content
        raise ValueError(err) from err


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
        if err.response.content:
            try:
                custom_error_content = json.loads(err.response.content)
            except JSONDecodeError:
                return {'error': f"{err}"}
            return custom_error_content
        return {'error': f"HTTP error {err}"}

class PPTRClient():
    """
    Client class used to expose Proof Point TRAP api.
    """
    def __init__(self, options, function_options=None):
        """
        Class constructor
        """
        self.base_url = function_options['base_url'].rstrip('/')
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
        self._headers = {"Authorization": f"{self.api_key}"}

    def get_incidents(self, lastupdate=None, state=None):
        """Get incidents in TRAP. The amount of incidents returned can be filtered by parameter lastupdate.

        :param lastupdate: - Minutes since last update
        :param state: - Filter incidents by state.
        :return Result in json format.
        """
        url = f"{self.base_url}{self._endpoints.get('incidents')}"
        params = {}
        if isinstance(lastupdate, int):
            params['created_after'] = timestamp_minutes_ago(lastupdate)
        else:
            if lastupdate is None:
                # first run, fetch all
                LOG.info("First Run in progress - this may take a while.")

        if state:
            # Filter by incident state.
            params['state'] = state.lower()

        try:
            res = self._req.execute_call_v2('get', url, callback=incidents_exception_handler, headers=self._headers,
                                            params=params, verify=self.bundle, proxies=self._req.get_proxies())

        except IntegrationError as ierr:
            msg = str(ierr)
            return {'error': f"Request to {url} failed with error {msg}."}

        # If an error caught in the error handler return the error dict.
        if isinstance(res, dict) and "error" in res:
            return res

        try:
            return res.json()
        except ValueError:
            # Default response likely not in json format just return content as is.
            return res.content

    def get_incident_details(self, incident_id=None):
        """Get incident details for an  incident id.

        :param incident_id: - Incident id for request.
        :return Result in json format.
        """
        rtn = {}

        url = "{}{}".format(self.base_url, self._endpoints["incident"].format(incident_id))

        try:
            res = self._req.execute_call_v2('get', url, callback=incident_details_exception_handler,
                                            headers=self._headers, verify=self.bundle, proxies=self._req.get_proxies())

        except IntegrationError as ierr:
            msg = str(ierr)
            raise requests.exceptions.RequestException(f"Request to {url} failed with error {msg}.") from ierr

        if isinstance(res, dict) and "error" in res:
            return res

        rtn['href'] = url
        try:
            rtn['data'] = res.json()
        except ValueError:
            # Default response likely not in json format just return content as is.
            rtn['data'] = res.content
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
        if member_id:
            url = "{}{}".format(self.base_url, self._endpoints["list_member"].format(list_id, member_id))
        else:
            url = "{}{}".format(self.base_url, self._endpoints["list_members"].format(list_id, members_type))

        res = self._req.execute_call_v2('get', url, verify=self.bundle, headers=self._headers,
                                        proxies=self._req.get_proxies())
        try:
            return res.json()
        except ValueError:
            # Default response likely not in json format just return content as is.
            return res.content


    def add_list_member(self, list_id=None, member=None, description=None, expiration=None, duration=None):
        """Add members to a list.

        :param list_id: The id value of a list (integer).
        :param member: Member to add (string). Can host, IP address, or URL to a list.
        :param description: Description of Proofpoint TRAP list member (string)
        :param expiration: Timestamp to expire Proofpoint TRAP list member (Unix type timestamp).
        :param duration: Number of minutes after which to expire Proofpoint TRAP list membership (integer).
        :return Result in json format.
        """
        url = "{}{}".format(self.base_url, self._endpoints["add_members"].format(list_id))
        # Convert expiration timestamp to UTC format.
        if expiration:
            expiration = dt.datetime.fromtimestamp(int(str(expiration)[0:-3]), timezone('UTC')).strftime('%Y-%m-%dT%H:%M:%SZ')

        if duration:
            # Convert parameter (in minutes) to milliseconds for api.
            duration = int(duration) * 60 * 1000

        payload = json.dumps({
            "member": member, "description": description, "expiration": expiration, "duration": duration
        })
        res = self._req.execute_call_v2('post', url, verify=self.bundle, headers=self._headers, json=payload,
                                        proxies=self._req.get_proxies())
        try:
            return res.json()
        except ValueError:
            # Default response likely not in json format just return content as is.
            return res.content

    def update_list_member(self, list_id=None, member_id=None, description=None, expiration=None, duration=None):
        """Update member of a list.

        :param list_id: The id value of a list (integer).
        :param member: The id of a member of a list (integer).
        :param description: Description of Proofpoint TRAP list member (string).
        :param expiration: Timestamp to expire Proofpoint TRAP list member (Unix type timestamp).
        :param duration: Number of minutes after which to expire Proofpoint TRAP list membership (integer).
        :return Result in json format.
        """
        url = "{}{}".format(self.base_url, self._endpoints["list_member"].format(list_id, member_id))
        # Convert expiration timestamp to UTC format.
        if expiration:
            expiration = dt.datetime.fromtimestamp(int(str(expiration)[0:-3]), timezone('UTC')).strftime('%Y-%m-%dT%H:%M:%SZ')

        if duration:
            # Convert parameter (in minutes) to milliseconds for api.
            duration = int(duration) * 60 * 1000

        payload = json.dumps({
            "description": description, "expiration": expiration, "duration": duration
        })
        res = self._req.execute_call_v2('put', url, verify=self.bundle, headers=self._headers, json=payload,
                                        proxies=self._req.get_proxies())
        try:
            return res.json()
        except ValueError:
            # Default response likely not in json format just return content as is.
            return res.content

    def delete_list_member(self, list_id=None, member_id=None):
        """Delete member from a list.

        :param list_id: The id value of a list (integer).
        :param member_id: The id of a member of a list (integer).
        :return Result in json format.
        """
        url = "{}{}".format(self.base_url, self._endpoints["list_member"].format(list_id, member_id))

        res = self._req.execute_call_v2('delete', url, verify=self.bundle, headers=self._headers,
                                        proxies=self._req.get_proxies())
        try:
            return res.json()
        except ValueError:
            # Default response likely not in json format just return content as is.
            # Covert bypes to string fro python 3.
            if version_info.major < 3:
                return res.content

            return res.content.decode('utf-8')
