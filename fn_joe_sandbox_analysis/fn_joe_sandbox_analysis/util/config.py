# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_joe_sandbox_analysis"""

from __future__ import print_function


def config_section_data():
  """Produce the default configuration section for app.config,
      when called by `resilient-circuits config [-c|-u]`
  """
  return u"""[fn_joe_sandbox_analysis]
# Joe Sandbox Cloud requires accepting the Terms and Conditions
jsb_accept_tac=True
# API key
jsb_api_key=
# API endpoint url for free version is below
jsb_api_url=https://www.joesandbox.com/api/
# If using pro version comment out above jsb_api_url and uncomment below jsb_api_url
# jsb_api_url=https://jbxcloud.joesecurity.org/api/
# Name of system to use or comment out for automatic selection
#jsb_systems=w7x64
# Enables secondary Results such as Yara rule generation, classification via Joe Sandbox Class as well as several detail reports.
jsb_secondary_results=True
# Time in seconds to wait between submission status checks
jsb_analysis_report_ping_delay=120
# Max time in seconds an analysis can take to run before timeout
jsb_analysis_report_request_timeout=1800
# jsb_verify can be False or a path to a certificate
jsb_verify=False
# Send an e-mail upon completion of the analysis
jsb_email_notification=True
#https_proxy=http://user:pass@10.10.1.10:1080"""
