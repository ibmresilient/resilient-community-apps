# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_github"""

import base64
import os
import io
try:
    from resilient import ImportDefinition
except ImportError:
    # Support Apps running on resilient-circuits < v35.0.195
    from resilient_circuits.util import ImportDefinition

RES_FILE = "data/export.res"


def codegen_reload_data():
    """
    Parameters required reload codegen for the fn_github package
    """
    return {
        "package": u"fn_github",
        "message_destinations": [u"fn_github"],
        "functions": [u"github_create_branch", u"github_create_file", u"github_create_release", u"github_delete_branch", u"github_delete_file", u"github_get_branch", u"github_get_commit", u"github_get_commits", u"github_get_file", u"github_get_latest_release", u"github_get_release", u"github_get_releases", u"github_get_repositories", u"github_list_directory", u"github_update_file"],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [u"Convert JSON to rich text v1.3"],
        "playbooks": [u"github_create_branch", u"github_create_file", u"github_create_release", u"github_delete_branch", u"github_delete_file", u"github_get_branch", u"github_get_commit", u"github_get_commits", u"github_get_file", u"github_get_latest_release", u"github_get_release", u"github_list_directory_files", u"github_list_repositories"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 45.0.7899

    Contents:
    - Message Destinations:
        - fn_github
    - Functions:
        - github_create_branch
        - github_create_file
        - github_create_release
        - github_delete_branch
        - github_delete_file
        - github_get_branch
        - github_get_commit
        - github_get_commits
        - github_get_file
        - github_get_latest_release
        - github_get_release
        - github_get_releases
        - github_get_repositories
        - github_list_directory
        - github_update_file
    - Playbooks:
        - github_create_branch
        - github_create_file
        - github_create_release
        - github_delete_branch
        - github_delete_file
        - github_get_branch
        - github_get_commit
        - github_get_commits
        - github_get_file
        - github_get_latest_release
        - github_get_release
        - github_list_directory_files
        - github_list_repositories
    - Scripts:
        - Convert JSON to rich text v1.3
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)