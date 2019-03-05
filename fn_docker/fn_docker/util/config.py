# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.

"""Generate a default configuration-file section for fn_docker"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_docker]
docker_approved_images=volatility,nsrl,amass
docker_use_remote_conn=False
docker_remote_url=<ssh | tcp connection string>
[docker_volatility]
docker_image=remnux/volatility
primary_source_dir=/tmp/bind_folder
primary_dest_dir=/home/nonroot/memdumps
cmd_operation=pslist
cmd=vol.py -f {{internal_vol}}/{{attachment_input}} {{operation}}
volatility_approved_operations=pslist,kdbgscan

[docker_nsrl]
#The default NSRL image expects an optional -v flag and an MD5 hash
cmd= -v "{{docker_input}}"
docker_image=blacktop/nsrl

[docker_amass]
docker_image=amass
cmd=--passive -d "{{docker_input}}"
"""
    return config_data
