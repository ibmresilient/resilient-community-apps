# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.

"""
    This is sample code from MITRE:
    https://www.mitre.org/capabilities/cybersecurity/overview/cybersecurity-blog/attck%E2%84%A2-content-available-in-stix%E2%84%A2-20-via

    Here it is used to check the connection to the MITRE STIX TAXII server

"""

from stix2 import TAXIICollectionSource
from taxii2client import Server
from proxies import get_proxies

# Instantiate server and get API Root
server = Server("https://cti-taxii.mitre.org/taxii/", proxies=get_proxies())
api_root = server.api_roots[0]

# Print name and ID of all ATT&CK technology-domains available as collections
for collection in api_root.collections:
    print(collection.title + ": " + collection.id)
