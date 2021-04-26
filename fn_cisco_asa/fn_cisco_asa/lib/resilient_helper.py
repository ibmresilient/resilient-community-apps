# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
import ipaddress
from resilient_lib import IntegrationError

def init_select_list_choices(rest_client, field_name, field_value=None):
    """
    Update the rule activity select field choices at run time.  
    We do not know the firewall and network object group lists till run time as
    these are defined by the user in the app.config.  
    """
    try: 
        # Get the current firewall rule activity select list.
        uri = "/types/actioninvocation/fields/{0}".format(field_name)
        get_response = rest_client.get(uri)

        values = []

        # Add each firewall as a select list entry.
        for label in field_value:
            entry = {'label': label,
                     'enabled': True,
                     'hidden': False}
            values.append(entry)

        # Put the new values into the select list to replace the current values there.
        get_response['values'] = values
        put_response = rest_client.put(uri, payload=get_response)

        return put_response

    except Exception as err:
        raise IntegrationError(err)


def is_valid_ipv4_addr(ip):
    """ Determines if input is an IPV4 Address"""
    try:
        return isinstance(ipaddress.ip_address(ip), ipaddress.IPv4Address)
    except Exception as e:
        return False

def is_valid_ipv6_addr(ip):
    """ Determines if input is an IPV6 Address"""
    try:
        return isinstance(ipaddress.ip_address(ip), ipaddress.IPv6Address)
    except Exception as e:
        return False

def artifact_to_network_object(artifact_type, artifact_value, netmask, range_end_ip, fqdn_version):
    """ Given an artifact type and value, return the Cisco ASA network object kind and value.
    """
    if artifact_type == "DNS Name":
        network_object_kind = fqdn_version
        network_object_value = artifact_value
    elif artifact_type == "IP Address":
        if netmask:
            network_object_kind, network_object_value = compute_ip_with_netmask("IPv4Network", artifact_value, netmask)
        elif range_end_ip:
            network_object_kind = "IPv4Range"
            network_object_value = compute_ip_with_range("IPv4Address", artifact_value, range_end_ip)
        else:
            network_object_kind = "IPv4Address"
            network_object_value = artifact_value
    elif artifact_type == "String":
        if is_valid_ipv4_addr(artifact_value):
            if netmask:
                network_object_kind, network_object_value = compute_ip_with_netmask("IPv4Network", artifact_value, netmask)
            elif range_end_ip:
                network_object_kind = "IPv4Range"
                network_object_value = compute_ip_with_range("IPv4Address", artifact_value, range_end_ip)
            else:
                network_object_kind = "IPv4Address"
                network_object_value = artifact_value
        elif is_valid_ipv6_addr(artifact_value):
            if netmask:
                network_object_kind, network_object_value = compute_ip_with_netmask("IPv6Network", artifact_value, netmask)
            elif range_end_ip:
                network_object_kind = "IPv6Range"
                network_object_value = compute_ip_with_range("IPv6Address", artifact_value, range_end_ip)
            else:
                network_object_kind = "IPv6Address"
                network_object_value = artifact_value
        else:
            raise IntegrationError("Unknown artifact type to convert to network object.")
    else:
        raise IntegrationError("Unknown artifact type to convert to network object.")

    return network_object_kind, network_object_value

def compute_ip_with_netmask(ip_kind, ip_value, ip_netmask):
    """ Compute the network object value of an IPv4Range or IPv6Range kind of network object.
    """
    if not ip_netmask:
        raise IntegrationError ("IP netmask not defined.")

    # IPv4 netmask contains / in the input but IPv6 does not. 
    # Using the same input format as ASDM.
    if "/" in ip_netmask:
        netmask = int(ip_netmask.split("/")[1])
    else: 
        netmask = int(ip_netmask)
    if ip_kind == "IPv4Network":
        # Netmask /32 is treated differently. It is a single IP address where as other
        # netmask cover a range of IPs.  Set the network object type to IPv4Address
        # in this special case.

        if netmask == 32:
            network_object_kind = "IPv4Address"
            network_object_value = u"{0}/{1}".format(ip_value, "255.255.255.255")
        else:
            network_object_kind = "IPv4Network"
            network_object_value = u"{0}/{1}".format(ip_value, netmask)
    elif ip_kind == "IPv6Network":
        if netmask > 128 or netmask < 8:
            raise IntegrationError ("Invalid IPv6Network prefix length must be less than or equal to 128 and greater than 8.")
        if netmask == 128:
            network_object_kind = "IPv6Address"
        else:
            network_object_kind = "IPv6Network"
        network_object_value = u"{0}/{1}".format(ip_value, ip_netmask)               
    else:
        raise IntegrationError ("Invalid network object kind for IP netmask.")

    return network_object_kind, network_object_value

def compute_ip_with_range(ip_kind, ip_value, ip_end_range):
    """ Compute the network object value of an IPv4Range kind of network object.
    """
    if not ip_end_range:
        raise IntegrationError ("IP netmask not defined.")

    if ip_kind == "IPv4Address":
        if not is_valid_ipv4_addr(ip_end_range):
            raise IntegrationError ("IPv4Address end range is not a valid IP.")
    elif ip_kind == "IPv6Address":
        if not is_valid_ipv6_addr(ip_end_range):
            raise IntegrationError ("IPv6Address end range is not a valid IP.")
    else:
        raise IntegrationError ("Invalid network object kind for IP end range.")

    network_object_value = u"{0}-{1}".format(ip_value, ip_end_range)
    return network_object_value