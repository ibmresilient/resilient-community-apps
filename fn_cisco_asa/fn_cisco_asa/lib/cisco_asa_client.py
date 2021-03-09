# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""Cisco ASA REST API client"""

import os
import sys
import json
import base64
import logging
from resilient_lib import validate_fields, IntegrationError

LOG = logging.getLogger(__name__)


def get_headers(username, password):
    url_key = u'{0}:{1}'.format(username, password)

    string_encoded_url_key = base64.b64encode(str.encode(str(url_key)))
    auth_token = string_encoded_url_key.decode("utf-8")

    # Create the headers
    headers = {'Authorization': u'Basic {0}'.format(auth_token),
               'Content-Type': 'application/json', 
               'User-Agent': 'REST API Agent'}
    return headers

class CiscoASAClient(object):
    def __init__(self, firewall_name, global_options, options, rc):
        # Read the configuration options
        required_fields = ["host"]
        validate_fields(required_fields, options)

        self.firewall_name = firewall_name
        self.rc = rc
        self.host = options.get("host")
        self.base_url = "https://{0}".format(self.host)
        self.username = options.get("username", global_options.get("username"))
        self.password = options.get("password", global_options.get("password"))
        if self.username is None or self.password is None:
            raise IntegrationError("Cisco ASA username and password must be defined.")
        self.cafile = options.get("cafile")
        self.bundle = os.path.expanduser(self.cafile) if self.cafile else False

        self.headers = get_headers(self.username, self.password)
    
    def get_network_object_group(self, group):
        """ Return the members of a network object list.
        """
        url = u"{0}/api/objects/networkobjectgroups/{1}".format(self.base_url, group)

        response = self.rc.execute_call_v2("get", url, headers=self.headers, verify=self.bundle,
                                           proxies=self.rc.get_proxies())
        return response.json()

    def is_object_in_network_object_group(self, net_obj_group, obj_kind, obj_value):
        """ Get the members of a network object group and determine if specified object is 
            contained in the group. 
        """
        response_group = self.get_network_object_group(net_obj_group)
        members = response_group.get("members")
        found = False
        for member in members:
            if member.get("value") == obj_value and member.get("kind") == obj_kind:
                found = True
                break
        return found

    def add_to_network_object_group(self, group, obj_kind, obj_value):
        """ Add a network object to the specified network object group.
            This function returns False if the object to be added is already in the group.
        """
        # Check if this object is already in the network object group
        found = self.is_object_in_network_object_group(group, obj_kind, obj_value)
        if found:
            LOG.info(u"%s %s is already in firewall: %s group: %s.", obj_kind, obj_value, 
                    self.firewall_name, group)
            return False

        # Add this object to the network object group
        url = u"{0}/api/objects/networkobjectgroups/{1}".format(self.base_url, group)
        data = {"members.add":[{
                    "kind": obj_kind,
                    "value": obj_value
                    }]
                }
        data_string = json.dumps(data)
        response = self.rc.execute_call_v2("patch", url, headers=self.headers, data=data_string,
                                            verify=self.bundle, proxies=self.rc.get_proxies())

        # If the object is added then write this change to ASA memory.
        if response.status_code == 204:
            wr_mem_response = self.write_memory()
            if wr_mem_response.status_code == 200:
                return True
            else:
                raise IntegrationError("Write memory failed.")
        else:    
            raise IntegrationError("Object was not added to network object group.")

    def remove_from_network_object_group(self, group, obj_kind, obj_value):
        """ Remove network object from the specified network object group.
            This function returns False if the object to be added is already in the group.
        """
        # Check if this object is already in the network object group
        found = self.is_object_in_network_object_group(group, obj_kind, obj_value)
        if not found:
            LOG.info(u"%s %s is not in firewall: %s group: %s.", obj_kind, obj_value, 
                    self.firewall_name, group)
            return False

        # Remove this object from the network object group
        url = u"{0}/api/objects/networkobjectgroups/{1}".format(self.base_url, group)
        data = {"members.remove":[{
                    "kind": obj_kind,
                    "value": obj_value
                    }]
                }
        data_string = json.dumps(data)
        response = self.rc.execute_call_v2("patch", url, headers=self.headers, data=data_string,
                                            verify=self.bundle, proxies=self.rc.get_proxies())

        # If the object is added then write this change to ASA memory.
        if response.status_code == 204:
            wr_mem_response = self.write_memory()
            if wr_mem_response.status_code == 200:
                return True
            else:
                raise IntegrationError("Write memory failed.")
        else:    
            raise IntegrationError("Object was not added to network object group.")

    def write_memory(self):
        url = u"{0}/api/commands/writemem".format(self.base_url)

        response = self.rc.execute_call_v2("post", url, headers=self.headers, verify=self.bundle,
                                           proxies=self.rc.get_proxies())
        return response

    