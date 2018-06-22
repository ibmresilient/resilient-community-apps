# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_mcafee_opendxl"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_mcafee_opendxl]
dxlclient_config=/home/integration/.resilient/mcafee/dxlclient.config
# Should be set to /mcafee/event/epo/threat/response if listening from ePO
topic_name=/resilient/something
topic_listener_on=True
incident_template=/Users/brianwal/.resilient/mcafee_config/incident_template.json.jinja2
incident_template_mapping=/Users/brianwal/.resilient/mcafee_config/incident_mapping.json.jinja2
"""
    return config_data
