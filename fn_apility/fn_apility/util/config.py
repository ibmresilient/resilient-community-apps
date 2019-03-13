# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_apility"""

from __future__ import print_function

def config_section_data():

   config_data = u"""[fn_apility]
url=https://api.apility.net
api_token=<your-api-token>
"""
   return config_data