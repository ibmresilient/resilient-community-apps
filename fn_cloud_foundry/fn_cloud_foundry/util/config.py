# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_cloud_foundry"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_cloud_foundry]
#Base url endpoint of your CF platform
#For example, for IBM’s BlueMix it is: https://api.ng.bluemix.net/
cf_api_base=https://api.ng.bluemix.net/
#
#Enter only what’s required by your authenticator.
#For example, the default BlueMixCF authenticator only requires apikey.
#
cf_api_apikey=
#Enter username and password if needed for access to DockerHub for Create Application function
cf_api_username=
cf_api_password=
    """
    return config_data
