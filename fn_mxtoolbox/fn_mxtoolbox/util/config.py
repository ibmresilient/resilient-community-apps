# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# Copyright IBM Corp. - Confidential Information

"""Generate a default configuration-file section for fn_mxtoolbox"""

from __future__ import print_function

CONFIG_SECTION = "fn_mxtoolbox"
def config_section_data():

   config_data = """
   [fn_mxtoolbox]
   url=https://api.mxtoolbox.com/api/v1/Lookup
   api_token=
   """
   return config_data