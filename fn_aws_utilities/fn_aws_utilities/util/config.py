# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_send_sms_via_sns"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_aws_utilities]
aws_access_key_id=
aws_secret_access_key=
aws_region_name=us-east-1  # aws region identifier
aws_sms_topic_name=resilient_aws_sns  # topic name used to send sms
"""

    return config_data
