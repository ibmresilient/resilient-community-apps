# -*- coding: utf-8 -*-
"""Generate a default configuration-file section for rc-cts-abuseipdb"""

from __future__ import print_function

URL_BASE = "https://api.abuseipdb.com/api/v2/check"

def config_section_data():
    return """[abuseipdb_cts]
abuseipdb_url={}
abuseipdb_key=
ignore_white_listed=True
""".format(URL_BASE)