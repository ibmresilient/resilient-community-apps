# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_send_sms_via_sns"""

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return """[fn_aws_utilities]
aws_access_key_id=
aws_secret_access_key=
# aws region identifier
aws_region_name=us-east-1
aws_sms_topic_name=
"""
