# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_netdevice"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_netdevice]
# specify the directory if using textFSM templates
#template_dir=

# for each network device to communicate with, define it's section below to match the device_ids field in the function input parameter
#[device_id]
#device_type=<see devices defined here https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py>
#ip=
#username=
#password=
#port=22
#secret=<leave commented for default of no secret>
#verbose=False
#use_commit=False
"""
    return config_data