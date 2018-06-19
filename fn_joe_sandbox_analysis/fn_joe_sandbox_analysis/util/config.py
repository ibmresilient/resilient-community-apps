# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_joe_sandbox_analysis"""

from __future__ import print_function


def config_section_data():
  """Produce the default configuration section for app.config,
      when called by `resilient-circuits config [-c|-u]`
  """
  config_data = u"""[fn_joe_sandbox_analysis]
jsb_accept_tac=True
jsb_api_key=
jsb_analysis_url=https://jbxcloud.joesecurity.org/analysis
jsb_analysis_report_default_ping_delay=120
jsb_analysis_report_request_timeout=1800
#jsb_http_proxy=http://user:pass@10.10.1.10:3128
#jsb_https_proxy=http://user:pass@10.10.1.10:1080"""

  return config_data