# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_joe_sandbox_analysis"""

from __future__ import print_function


def config_section_data():
  """Produce the default configuration section for app.config,
      when called by `resilient-circuits config [-c|-u]`
  """
  config_data = u"""[fn_joe_sandbox_analysis]
joe_sandbox_api_key=
joe_sandbox_analysis_url=https://jbxcloud.joesecurity.org/analysis
joe_sandbox_analysis_report_request_timeout=1800"""

  return config_data