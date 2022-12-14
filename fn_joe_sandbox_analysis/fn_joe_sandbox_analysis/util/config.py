# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_joe_sandbox_analysis"""

from __future__ import print_function


def config_section_data():
  """Produce the default configuration section for app.config,
      when called by `resilient-circuits config [-c|-u]`
  """
  return u"""[fn_joe_sandbox_analysis]
jsb_accept_tac=True
jsb_api_key=
# API endpoint url for free version is below
jsb_analysis_url=https://www.joesandbox.com/api/
# If using pro version comment out above jsb_analysis_url and uncomment below jsb_analysis_url
# jsb_analysis_url=https://jbxcloud.joesecurity.org/api/
jsb_analysis_report_ping_delay=120
jsb_analysis_report_request_timeout=1800
# jsb_verify can be False or a path to a certificate
jsb_verify=False
#jsb_http_proxy=http://user:pass@10.10.1.10:3128
#jsb_https_proxy=http://user:pass@10.10.1.10:1080"""
