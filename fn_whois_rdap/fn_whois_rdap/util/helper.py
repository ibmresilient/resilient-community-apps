# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

import tldextract
from ipwhois import IPWhois

ip_from_domain = None

def check_input_ip(query):
    """This function checks if the input is an IP, URL or DNS

    Arguments:
        query {string} -- Artifact.value

    Returns:
        {bool, str} -- True or False, registered domain
    """
    input_is_ip = True
    ext = tldextract.extract(query)
    if ext.registered_domain:
        input_is_ip = False
    return input_is_ip, ext.registered_domain

# Gather registry information
def get_whois_registry_info(ip_input):
    """Gather registry information
    Arguments:
        ip_input {string} -- Artifact.value
    Returns:
        {object} -- Contains all registry information
    """
    internet_protocol_address_object = IPWhois(ip_input)
    whois_response = internet_protocol_address_object.lookup_whois()
    if internet_protocol_address_object.dns_zone:
        whois_response["dns_zone"] = internet_protocol_address_object.dns_zone
    return whois_response

def get_rdap_registry_info(ip_input, rdap_depth):
    """Gathers registry info in RDAP protocol

    Arguments:
        ip_input {string} -- Artifact.value
        rdap_depth {int} -- 0,1 or 2

    Returns:
        {object} -- Registry info, RDAP Protocol
    """
    internet_protocol_address_object = IPWhois(ip_input)
    rdap_response = internet_protocol_address_object.lookup_rdap(rdap_depth)
    if internet_protocol_address_object.dns_zone:
        rdap_response["dns_zone"] = internet_protocol_address_object.dns_zone
    return rdap_response
