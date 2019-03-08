# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.

"""Generate a default configuration-file section for fn_docker"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_docker]
# A comma separated list of approved images that can be used. May not be blank.
docker_approved_images=volatility,nsrl,amass

# Whether or not to use remote connection.
docker_use_remote_conn=False

# A ssh:// or tcp:// url to be used for remote connections
docker_remote_url=<ssh | tcp connection string>

# A app.config section for the volatility image to be used with Docker
[docker_volatility]
docker_image=remnux/volatility
# The folder on your host which will be used for volume binding
primary_source_dir=/tmp/bind_folder
# The folder within the container which will be used for volume binding
primary_dest_dir=/home/nonroot/memdumps
#The operation that will be done with the image, used only for images which have multiple entrypoint operations
cmd_operation=pslist
# The command that will be send to the container 
cmd=vol.py -f {{internal_vol}}/{{attachment_input}} {{operation}}
# A comma separated list of approved operations. Leave this blank/commented out to allow all operations
# The format of this config value should be {image}_approved_operations similar to the section header [docker_{image}]
volatility_approved_operations=pslist,kdbgscan

# A app.config section for the nsrl image to be used with Docker
[docker_nsrl]
# The command that will be send to the container 
# The default NSRL image expects an optional -v flag and an MD5 hash
cmd= -v "{{docker_input}}"
docker_image=blacktop/nsrl

# A app.config section for the amass image to be used with Docker
[docker_amass]
docker_image=amass
# The command that will be sent to the container 
cmd=--passive -d "{{docker_input}}"
"""
    return config_data
