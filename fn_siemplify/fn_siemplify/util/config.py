# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_siemplify"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_siemplify when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_siemplify]
base_url=<changeme>
api_key=<changeme>
# false|/path/to/certificate
cafile=
# set polling_interval=0 to disable. Otherwise set in seconds
polling_interval=120
# polling_lookback in minutes to look back first time poller starts
polling_lookback=120
# polling_filters specifies key/value pairs to escalate new Siemplify cases to SOAR
#  ex. polling_filters="startTime":"","tags":["tagA"],"priorities":[40,50],"importance":[],environments":["Default Enviornment"]
polling_filters=
# poller timezone to match Siemplify configuration
poller_timezone=Etc/GMT
# specify the environment for creating cases and entities
default_case_environment=Default Environment
# use playbook_mapping to define key/value mappings between soar incident types and playbooks when creating a Siemplify cases
# If necessary, use DEFAULT to specify playbook(s) when no mapping matches
#   playbook_mapping='<SOAR Incident Type>': 'playbook1,playbook2','Malware':'playbook3','DEFAULT':'playbook4'
#playbook_mappings=
# override default Siemplify and SOAR templates files as necessary
siemplify_create_case_template=
soar_close_case_template=
soar_update_case_template=
# use artifact_lookup_types to specify a JSON file to override the default settings
artifact_type_lookup=
"""
    return config_data
