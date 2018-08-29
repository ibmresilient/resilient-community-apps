# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_service_now"""

from __future__ import print_function


def config_section_data():
  """Produce the default configuration section for app.config,
      when called by `resilient-circuits config [-c|-u]`
  """
  config_data = u"""[fn_service_now]
sn_host=https://instance.service-now.com
sn_username=
sn_password=
"""
  return config_data
