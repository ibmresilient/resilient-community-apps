# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_pa_panorama"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_pa_panorama]
# URL/IP of Panorama
panorama_host=<https://0.0.0.0>
api_key=<Panorama_api_key>
location=

# Name of the vsys is needed when location is vsys or Panorama-pushed
#vsys=
"""
    return config_data
