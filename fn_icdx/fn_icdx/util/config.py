# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Generate a default configuration-file section for fn_icdx"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_icdx]
icdx_amqp_host = <YOUR_ICDX_URL> #Hostname for the ICDx installation, should be like my-server.com
icdx_amqp_port = <YOUR_ICDX_PORT> #Port for the ICDx AMQP Service, defaults to 5672
icdx_amqp_vhost = <YOUR_ICDX_VHOST> #Virtual Host for the AMQP Exchange. Default is dx
icdx_amqp_username = <YOUR_ICDX_USERNAME> #Username of ICDx user
icdx_amqp_password = <YOUR_ICDX_PASSWORD> #Password of ICDx user
icdx_search_limit = <Customizable Limit> #A limiter for how many results are queried in ICDx. Default is 100 unless this value exceeds that
icdx_forwarder_toggle = <True / False> #Boolean specifying whether the forwarder should be enabled when circuits is started
icdx_forwarder_inc_owner = <USER_EMAIL / USER_ID / GROUP_NAME> #Who will be assigned incidents created by the forwarder
"""
    return config_data
