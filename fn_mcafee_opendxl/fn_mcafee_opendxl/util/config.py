# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_mcafee_opendxl"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_mcafee_opendxl]
dxlclient_config=/home/integration/.resilient/mcafee/dxlclient.config

# Set topic_listener to False to prevent it from listening on any topics
topic_listener_on=True

# custom_template_dir is optional and used to specify the directory where new 
# templates can be found/to override any default templates
custom_template_dir=
"""
    return config_data
