# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""Cisco ASA REST API client"""

import os
import json
import base64
import logging 
from resilient_lib import validate_fields, IntegrationError

LOG = logging.getLogger(__name__)

CISCO_ASA_DEFAULT_LIMIT = 100

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

        self.headers = self.get_headers(self.username, self.password)
    
    def get_headers(self, username, password):
        """ Return the authorization header.
        """
        url_key = u'{0}:{1}'.format(username, password)

        string_encoded_url_key = base64.b64encode(str.encode(str(url_key)))
        auth_token = string_encoded_url_key.decode("utf-8")

        # Create the headers
        headers = {'Authorization': u'Basic {0}'.format(auth_token),
                   'Content-Type': 'application/json', 
                   'User-Agent': 'REST API Agent'}
        return headers

    def get_network_object(self, objectId):
        """ Return the details of a single network object.
        """
        url = u"{0}/api/objects/networkobjects/{1}".format(self.base_url, objectId)

        response = self.rc.execute_call_v2("get", url, headers=self.headers, verify=self.bundle,
                                           proxies=self.rc.get_proxies())
        return response.json()
    
    def post_network_object(self, obj_data):
        """ Create a single network object.
        """
        url = u"{0}/api/objects/networkobjects".format(self.base_url)

        response, msg = self.rc.execute_call_v2("post", url, headers=self.headers, json=obj_data, 
                                            verify=self.bundle, proxies=self.rc.get_proxies(), callback=callback)
        return response, msg

    def get_network_objects(self, limit=None):
        """ Return the network objects of the firewall (host).
        Return the number of objects specified in the limit parameter.
        Cisco ASA will return 100 objects by default.
        """
        url = u"{0}/api/objects/networkobjects".format(self.base_url)
        
        if not limit:
            limit = CISCO_ASA_DEFAULT_LIMIT
            
        params = {"limit": limit}

        response = self.rc.execute_call_v2("get", url, headers=self.headers, params=params,
                                            verify=self.bundle, proxies=self.rc.get_proxies())
        status_code = response.status_code

        return status_code, response.json()

    def get_network_object_group(self, group):
        """ Return the members of a network object group.
        """
        url = u"{0}/api/objects/networkobjectgroups/{1}".format(self.base_url, group)

        response = self.rc.execute_call_v2("get", url, headers=self.headers, verify=self.bundle,
                                           proxies=self.rc.get_proxies())
        return response.json()

    def get_network_object_group_detailed(self, group):
        """ Return the members of a network object group as a list.  
        This function is called by the function that fills the Cisco ASA Network Object data table.
        This function also calls get_network_object for each non-primitive network object so that 
        objectId (name) is stored in the datable.  Primitive objects (like IPv4Address and IPv4Network
        do not require a name) but network objects (like IPv4FQDN and IPv4Range) do require a
        Name (objectId).  
        """
        url = u"{0}/api/objects/networkobjectgroups/{1}".format(self.base_url, group)

        response = self.rc.execute_call_v2("get", url, headers=self.headers, verify=self.bundle,
                                           proxies=self.rc.get_proxies())
        group = response.json()
        members = group.get("members")
        network_object_list = []
        for member in members:
            if member.get("kind") == "objectRef#NetworkObj":
                object_id = member.get("objectId")
                net_object = self.get_network_object(object_id)
                network_object_list.append(net_object)
            else:
                network_object_list.append(member)
        return network_object_list

    def is_object_in_network_object_group(self, net_obj_group, obj_name, obj_kind, obj_value):
        """ Get the members of a network object group and determine if specified object is 
            contained in the group. 

            Returns:
                [bool]: [True is the object is in the network group
                         False if the object is not in the network group]
        """
        response_group = self.get_network_object_group(net_obj_group)
        members = response_group.get("members")
        found = False
        for member in members:
            member_kind = member.get("kind")
            if member_kind in ('object#NetworkObj', 'objectRef#NetworkObj'):
                if member.get("objectId") == obj_name:
                    found = True
                    break
            elif member_kind == obj_kind and not obj_name:
                if member.get("value") == obj_value:
                    found = True
                    break

        return found

    def is_object_in_network(self, obj_name, obj_kind, obj_value):
        """ Get the network objects of the server and determine if specified object is 
            already in the global firewall network. 

            Returns:
                [bool]: [True is the object is in the network
                         False if the object is not in the network]
        """
        status, response_group = self.get_network_objects(limit=CISCO_ASA_DEFAULT_LIMIT)
        items = response_group.get("items")
        found = False
        for item in items:
            item_name = item.get("name") 
            item_host = item.get('host')
            item_kind = item.get("kind")
            host_kind = item_host.get("kind")
            host_value = item_host.get("value")
            if item_name == obj_name and item_kind == "object#NetworkObj":
                if host_kind == obj_kind and host_value == obj_value:
                    found = True
                    break

        return found

    def add_to_network_object_group(self, group, obj_name, obj_desc, obj_kind, obj_value):
        """ Add a network object to the specified network object group.

            Returns:
                [bool]: [True is the object is added
                         False if not added to the group]
                [string]: [message indicating why the message was not added]
        """
        # Check if this object is already in the network object group
        found = self.is_object_in_network_object_group(group, obj_name, obj_kind, obj_value)
        if found:
            reason = u"Object Kind: {0}, Object Value: {1}, Object Name: {2} is already in Firewall: {3} Group: {4}".format(obj_kind, obj_value, obj_name, 
                     self.firewall_name, group)
            LOG.info(reason)
            return False, reason

        # If object to be added has a name, then it is not a primitive object.
        # Create a network object for this object.
        if obj_name:
            new_object = {
                "kind": "object#NetworkObj",
                "name": obj_name,
                "host": {
                    "kind": obj_kind,
                    "value": obj_value
                },
                "description": obj_desc
            }
 
            post_response, error_msg = self.post_network_object(new_object)

            if error_msg:
                return False, error_msg

        # Add this object to the network object group
        url = u"{0}/api/objects/networkobjectgroups/{1}".format(self.base_url, group)

        # Members of a network object group can be of type network object or IPv4Address or IPv6
        if obj_kind in ('IPv4Address', 'IPv4Network', 'IPv6Address') and not obj_name:
            data = {"members.add":[{
                        "kind": obj_kind,
                        "value": obj_value
                        }]
                    }
        else:
            data = {"members.add":[{
                        "kind": "objectRef#NetworkObj",
                        "objectId" : obj_name
                        }]
                    }
        data_string = json.dumps(data)

        response, error_msg = self.rc.execute_call_v2("patch", url, headers=self.headers, data=data_string,
                                                      verify=self.bundle, proxies=self.rc.get_proxies(), 
                                                      callback=callback)

        # If the object is added then write this change to ASA memory.
        if response.status_code == 204:
            wr_mem_response = self.write_memory()
            if wr_mem_response.status_code == 200:
                reason = u"Object Kind: {0}, Object Value: {1}, Object Name: {2}, is added to Firewall: {3}, Group: {4}".format(obj_kind, 
                         obj_value, obj_name, self.firewall_name, group)
                LOG.info(reason)
                return True, reason
            else:
                reason = u"Object Kind: {0}, Object Value: {1}, Object Name: {2}, is added to Firewall: {3}, Group: {4} but write mem failed.".format(obj_kind, 
                         obj_value, obj_name, self.firewall_name, group)
                LOG.info(reason)
                return False, reason        
        else:
            reason = u"Object Kind: {0}, Object Value: {1}, Object Name: {2}, is NOT added to Firewall: {3}, Group: {4}\n{5}".format(obj_kind, 
                     obj_value, obj_name, self.firewall_name, group, error_msg)
            LOG.info(reason)
            return False, reason

    def remove_from_network_object_group(self, group, obj_kind, obj_value, obj_id):
        """ Remove network object from the specified network object group.

            Returns:
                [bool]: [True is the object is removed
                         False if not removed and is not in the group]
                [string]: [message indicating why the message was not removed]
        """
        # Check if this object is already in the network object group
        obj_name = obj_id
        found = self.is_object_in_network_object_group(group, obj_name, obj_kind, obj_value)
        if not found:
            reason = u"Object Kind: {0}, Object Value: {1}, Object Name: {2} is not in Firewall: {3} Group: {4}".format(obj_kind, obj_value, obj_name, 
                     self.firewall_name, group)
            LOG.info(reason)
            return False, reason

        # Remove this object from the network object group
        url = u"{0}/api/objects/networkobjectgroups/{1}".format(self.base_url, group)
        # Key is different when dealing with a network object vs an IP address.
        if obj_kind in ('IPv4Address', 'IPv4Network', 'IPv6Address') and not obj_name:
            data = {"members.remove":[{
                        "kind": obj_kind,
                        "value": obj_value
                        }]
                    }
        else:
            data = {"members.remove":[{
                        "kind": "objectRef#NetworkObj",
                        "objectId" : obj_name
                        }]
                    }

        data_string = json.dumps(data)
        LOG.debug(data_string)

        response, error_msg = self.rc.execute_call_v2("patch", url, headers=self.headers, data=data_string,
                                                    verify=self.bundle, proxies=self.rc.get_proxies(), callback=callback)

        # If the object is added then write this change to ASA memory.
        if response.status_code == 204:
            wr_mem_response = self.write_memory()
            if wr_mem_response.status_code == 200:
                reason = u"Object Kind: {0}, Object Value: {1}, Object Name: {2}, is removed from Firewall: {3}, Group: {4}".format(obj_kind, 
                         obj_value, obj_name, self.firewall_name, group)
                LOG.info(reason)
                return True, reason
            else:
                reason = u"Object Kind: {0}, Object Value: {1}, Object Name: {2}, is removed from Firewall: {3}, Group: {4} but write mem failed.".format(obj_kind, 
                         obj_value, obj_name, self.firewall_name, group)
                LOG.info(reason)
                return False, reason               
        else:    
            reason = u"Object Kind: {0}, Object Value: {1}, Object Name: {2}, is NOT removed from Firewall: {3}, Group: {4}\n\n{5}".format(obj_kind, 
                     obj_value, obj_name, self.firewall_name, group, error_msg)
            LOG.info(reason)
            return False, reason

    def write_memory(self):
        """Send a write memory command to the Cisco ASA device to save the current running 
           configuration to the startup configuration.  Call after making an update to the device.

        Returns:
            [int]: [status code 200 if success (no payload)]
        """
        url = u"{0}/api/commands/writemem".format(self.base_url)

        response = self.rc.execute_call_v2("post", url, headers=self.headers, verify=self.bundle,
                                           proxies=self.rc.get_proxies())
        return response

def callback(response):
    """
    callback needed for certain REST API calls to return a formatted error message
    :param response:
    :return: response, error_msg
    """
    error_msg = None
    if response.status_code >= 300:
        resp = response.json()
        msg = resp['messages']
        error_msg  = u"Cisco ASA Error: \n    status code: {0}\n    messages: {1}".format(response.status_code, msg)

    return response, error_msg
