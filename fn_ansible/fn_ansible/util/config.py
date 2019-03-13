# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_ansible"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_ansible]
#playbook_dir=</full/path/to/your/playbook/directory>
#user_name=<USERNAME-OF-HOSTS>
#root_password=<PASSWORD-OF-HOSTS>
#hosts_path=</full/path/of/your/inventory/file>
#playbook_become_method=<SUPER-USER-METHOD e.g. sudo>
#playbook_become_user=<NAME-OF-ROOT-USER e.g. root>
#vault_password_file=<OPTIONAL: /full/path/of/password/file>
#connection_type=<OPTIONAL: e.g. local, smart etc.>
#control_machine_username=<OPTIONAL: for user, REQUIRED: for developers and testers>
#control_machine_password=<OPTIONAL: for user, REQUIRED: for developers and testers>
"""
    return config_data