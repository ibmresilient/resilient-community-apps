# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Class for Resilient circuits Functions supporting REST API client for Proofpoint TRAP  """
import logging
import json
from datetime import datetime
from resilient_lib import RequestsCommon
try:
    from urllib.parse import urljoin
except:
    from urlparse import urljoin

LOG = logging.getLogger(__name__)

class PPTRClient(object):
    """
    Client class used to expose Proof Point TRAP api.
    """
    def __init__(self, options, function_params=None):
        """
        Class constructor
        """
        self.base_url = options['base_url']
        self.api_key = options['api_key']
        # Rest request endpoints
        self._endpoints = {
            # REST endpoints
            "list_member":      "/lists/{}/members/{}.json",
            "list_members":     "/lists/{}/{}",
            "add_members":      "/lists/{}/members.json",
        }
        self._req = RequestsCommon(options, function_params)
        self._headers = {"Authorization": "{0}".format(self.api_key)}

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

        r = self._req.execute_call_v2('get', url, verify=False, headers=self._headers)
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
        :param description: The information format to get in return. (path).
        :param expiration: The information format to get in return. (path).
        :param duration The information format to get in return. (path).
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["add_members"]).format(list_id)
        # Convert expiration timestamp to UTC format.
        expiration = datetime.utcfromtimestamp(int(str(expiration)[0:-3])).strftime('%Y-%m-%dT%H:%M:%SZ')

        payload = json.dumps({
                "member": member, "description": description, "expiration": expiration, "duration": duration
            }
        )
        r = self._req.execute_call_v2('post', url, verify=False, headers=self._headers, json=payload)
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
        :param description: The information format to get in return. (path).
        :param expiration: The information format to get in return. (path).
        :param duration The information format to get in return. (path).
        :return Result in json format.
        """
        url = urljoin(self.base_url, self._endpoints["list_member"]).format(list_id, member_id)
        # Convert expiration timestamp to UTC format.
        if expiration is not None:
            expiration = datetime.utcfromtimestamp(int(str(expiration)[0:-3])).strftime('%Y-%m-%dT%H:%M:%SZ')

        payload = json.dumps({
                "description": description, "expiration": expiration, "duration": duration
            }
        )
        r = self._req.execute_call_v2('put', url, verify=False, headers=self._headers, json=payload)
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

        r = self._req.execute_call_v2('delete', url, verify=False, headers=self._headers)
        try:
            return r.json()
        except ValueError:
            # Default response likely not in json format just return content as is.
            return r.content
        return r