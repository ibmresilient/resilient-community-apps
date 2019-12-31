class MockedResponse:
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data

def mocked_get_job_template_by_project():
    payload = {
        "count": 6,
        "next": None,
        "previous": None,
        "results": [
            {
                "id": 6,
                "type": "job_template",
                "url": "/api/v2/job_templates/6/",
                "related": {
                    "created_by": "/api/v2/users/1/",
                    "modified_by": "/api/v2/users/1/",
                    "labels": "/api/v2/job_templates/6/labels/",
                    "inventory": "/api/v2/inventories/1/",
                    "project": "/api/v2/projects/7/",
                    "extra_credentials": "/api/v2/job_templates/6/extra_credentials/",
                    "credentials": "/api/v2/job_templates/6/credentials/",
                    "last_job": "/api/v2/jobs/114/",
                    "jobs": "/api/v2/job_templates/6/jobs/",
                    "schedules": "/api/v2/job_templates/6/schedules/",
                    "activity_stream": "/api/v2/job_templates/6/activity_stream/",
                    "launch": "/api/v2/job_templates/6/launch/",
                    "notification_templates_any": "/api/v2/job_templates/6/notification_templates_any/",
                    "notification_templates_success": "/api/v2/job_templates/6/notification_templates_success/",
                    "notification_templates_error": "/api/v2/job_templates/6/notification_templates_error/",
                    "access_list": "/api/v2/job_templates/6/access_list/",
                    "survey_spec": "/api/v2/job_templates/6/survey_spec/",
                    "object_roles": "/api/v2/job_templates/6/object_roles/",
                    "instance_groups": "/api/v2/job_templates/6/instance_groups/",
                    "slice_workflow_jobs": "/api/v2/job_templates/6/slice_workflow_jobs/",
                    "copy": "/api/v2/job_templates/6/copy/"
                },
                "summary_fields": {
                    "inventory": {
                        "id": 1,
                        "name": "Demo Inventory",
                        "description": "",
                        "has_active_failures": True,
                        "total_hosts": 1,
                        "hosts_with_active_failures": 1,
                        "total_groups": 0,
                        "groups_with_active_failures": 0,
                        "has_inventory_sources": False,
                        "total_inventory_sources": 0,
                        "inventory_sources_with_failures": 0,
                        "organization_id": 1,
                        "kind": ""
                    },
                    "project": {
                        "id": 7,
                        "name": "2nd Project",
                        "description": "",
                        "status": "ok",
                        "scm_type": ""
                    },
                    "last_job": {
                        "id": 114,
                        "name": "2nd demo",
                        "description": "",
                        "finished": "2019-12-02T16:04:23.489501Z",
                        "status": "failed",
                        "failed": True
                    },
                    "last_update": {
                        "id": 114,
                        "name": "2nd demo",
                        "description": "",
                        "status": "failed",
                        "failed": True
                    },
                    "created_by": {
                        "id": 1,
                        "username": "admin",
                        "first_name": "",
                        "last_name": ""
                    },
                    "modified_by": {
                        "id": 1,
                        "username": "admin",
                        "first_name": "",
                        "last_name": ""
                    },
                    "object_roles": {
                        "admin_role": {
                            "description": "Can manage all aspects of the job template",
                            "name": "Admin",
                            "id": 34
                        },
                        "execute_role": {
                            "description": "May run the job template",
                            "name": "Execute",
                            "id": 35
                        },
                        "read_role": {
                            "description": "May view settings for the job template",
                            "name": "Read",
                            "id": 36
                        }
                    },
                    "user_capabilities": {
                        "edit": True,
                        "delete": True,
                        "start": True,
                        "schedule": True,
                        "copy": True
                    },
                    "labels": {
                        "count": 0,
                        "results": [

                        ]
                    },
                    "survey": {
                        "title": "",
                        "description": ""
                    },
                    "recent_jobs": [
                        {
                            "id": 114,
                            "status": "failed",
                            "finished": "2019-12-02T16:04:23.489501Z",
                            "type": "job"
                        },
                        {
                            "id": 85,
                            "status": "successful",
                            "finished": "2019-11-20T21:52:06.610300Z",
                            "type": "job"
                        },
                        {
                            "id": 84,
                            "status": "failed",
                            "finished": "2019-11-20T21:51:05.044460Z",
                            "type": "job"
                        },
                        {
                            "id": 83,
                            "status": "failed",
                            "finished": "2019-11-20T21:01:52.494021Z",
                            "type": "job"
                        },
                        {
                            "id": 82,
                            "status": "failed",
                            "finished": "2019-11-20T20:57:55.555327Z",
                            "type": "job"
                        },
                        {
                            "id": 81,
                            "status": "failed",
                            "finished": "2019-11-20T20:54:22.876251Z",
                            "type": "job"
                        },
                        {
                            "id": 80,
                            "status": "failed",
                            "finished": "2019-11-20T20:53:32.672157Z",
                            "type": "job"
                        },
                        {
                            "id": 72,
                            "status": "failed",
                            "finished": "2019-11-15T21:56:53.338202Z",
                            "type": "job"
                        },
                        {
                            "id": 68,
                            "status": "failed",
                            "finished": "2019-11-15T16:53:57.967123Z",
                            "type": "job"
                        },
                        {
                            "id": 67,
                            "status": "failed",
                            "finished": "2019-11-15T16:53:26.958466Z",
                            "type": "job"
                        }
                    ],
                    "credentials": [

                    ]
                },
                "created": "2019-11-13T21:48:20.796164Z",
                "modified": "2019-12-02T15:52:59.050449Z",
                "name": "2nd demo",
                "description": "",
                "job_type": "run",
                "inventory": 1,
                "project": 7,
                "playbook": "hello_world.yml",
                "forks": 0,
                "limit": "",
                "verbosity": 0,
                "extra_vars": "",
                "job_tags": "",
                "force_handlers": False,
                "skip_tags": "",
                "start_at_task": "",
                "timeout": 0,
                "use_fact_cache": False,
                "last_job_run": "2019-12-02T16:04:23.489501Z",
                "last_job_failed": True,
                "next_job_run": None,
                "status": "failed",
                "host_config_key": "",
                "ask_diff_mode_on_launch": False,
                "ask_variables_on_launch": True,
                "ask_limit_on_launch": True,
                "ask_tags_on_launch": True,
                "ask_skip_tags_on_launch": False,
                "ask_job_type_on_launch": False,
                "ask_verbosity_on_launch": False,
                "ask_inventory_on_launch": False,
                "ask_credential_on_launch": False,
                "survey_enabled": True,
                "become_enabled": False,
                "diff_mode": False,
                "allow_simultaneous": False,
                "custom_virtualenv": None,
                "job_slice_count": 3,
                "credential": None,
                "vault_credential": None
            },
            {
                "id": 5,
                "type": "job_template",
                "url": "/api/v2/job_templates/5/",
                "related": {
                    "created_by": "/api/v2/users/1/",
                    "modified_by": "/api/v2/users/1/",
                    "labels": "/api/v2/job_templates/5/labels/",
                    "inventory": "/api/v2/inventories/2/",
                    "project": "/api/v2/projects/4/",
                    "credential": "/api/v2/credentials/1/",
                    "extra_credentials": "/api/v2/job_templates/5/extra_credentials/",
                    "credentials": "/api/v2/job_templates/5/credentials/",
                    "last_job": "/api/v2/jobs/149/",
                    "jobs": "/api/v2/job_templates/5/jobs/",
                    "schedules": "/api/v2/job_templates/5/schedules/",
                    "activity_stream": "/api/v2/job_templates/5/activity_stream/",
                    "launch": "/api/v2/job_templates/5/launch/",
                    "notification_templates_any": "/api/v2/job_templates/5/notification_templates_any/",
                    "notification_templates_success": "/api/v2/job_templates/5/notification_templates_success/",
                    "notification_templates_error": "/api/v2/job_templates/5/notification_templates_error/",
                    "access_list": "/api/v2/job_templates/5/access_list/",
                    "survey_spec": "/api/v2/job_templates/5/survey_spec/",
                    "object_roles": "/api/v2/job_templates/5/object_roles/",
                    "instance_groups": "/api/v2/job_templates/5/instance_groups/",
                    "slice_workflow_jobs": "/api/v2/job_templates/5/slice_workflow_jobs/",
                    "copy": "/api/v2/job_templates/5/copy/"
                },
                "summary_fields": {
                    "inventory": {
                        "id": 2,
                        "name": "bad inventory",
                        "description": "",
                        "has_active_failures": True,
                        "total_hosts": 1,
                        "hosts_with_active_failures": 1,
                        "total_groups": 0,
                        "groups_with_active_failures": 0,
                        "has_inventory_sources": False,
                        "total_inventory_sources": 0,
                        "inventory_sources_with_failures": 0,
                        "organization_id": 1,
                        "kind": ""
                    },
                    "project": {
                        "id": 4,
                        "name": "Demo Project",
                        "description": "",
                        "status": "successful",
                        "scm_type": "git"
                    },
                    "last_job": {
                        "id": 149,
                        "name": "Demo Job Template",
                        "description": "",
                        "finished": "2019-12-18T16:25:40.839231Z",
                        "status": "failed",
                        "failed": True
                    },
                    "last_update": {
                        "id": 149,
                        "name": "Demo Job Template",
                        "description": "",
                        "status": "failed",
                        "failed": True
                    },
                    "created_by": {
                        "id": 1,
                        "username": "admin",
                        "first_name": "",
                        "last_name": ""
                    },
                    "modified_by": {
                        "id": 1,
                        "username": "admin",
                        "first_name": "",
                        "last_name": ""
                    },
                    "object_roles": {
                        "admin_role": {
                            "description": "Can manage all aspects of the job template",
                            "name": "Admin",
                            "id": 26
                        },
                        "execute_role": {
                            "description": "May run the job template",
                            "name": "Execute",
                            "id": 27
                        },
                        "read_role": {
                            "description": "May view settings for the job template",
                            "name": "Read",
                            "id": 28
                        }
                    },
                    "user_capabilities": {
                        "edit": True,
                        "delete": True,
                        "start": True,
                        "schedule": True,
                        "copy": True
                    },
                    "labels": {
                        "count": 0,
                        "results": [

                        ]
                    },
                    "recent_jobs": [
                        {
                            "id": 149,
                            "status": "failed",
                            "finished": "2019-12-18T16:25:40.839231Z",
                            "type": "job"
                        },
                        {
                            "id": 76,
                            "status": "failed",
                            "finished": "2019-11-15T21:59:25.256447Z",
                            "type": "job"
                        },
                        {
                            "id": 73,
                            "status": "failed",
                            "finished": "2019-11-15T21:58:21.534239Z",
                            "type": "job"
                        },
                        {
                            "id": 40,
                            "status": "failed",
                            "finished": "2019-11-15T12:45:14.954389Z",
                            "type": "job"
                        },
                        {
                            "id": 34,
                            "status": "failed",
                            "finished": "2019-11-13T20:50:11.112902Z",
                            "type": "job"
                        },
                        {
                            "id": 31,
                            "status": "failed",
                            "finished": "2019-11-13T20:47:28.475905Z",
                            "type": "job"
                        },
                        {
                            "id": 28,
                            "status": "failed",
                            "finished": "2019-11-12T20:24:26.956546Z",
                            "type": "job"
                        },
                        {
                            "id": 25,
                            "status": "successful",
                            "finished": "2019-11-12T20:21:21.173462Z",
                            "type": "job"
                        },
                        {
                            "id": 22,
                            "status": "successful",
                            "finished": "2019-11-12T20:19:10.365268Z",
                            "type": "job"
                        },
                        {
                            "id": 19,
                            "status": "successful",
                            "finished": "2019-11-12T16:08:39.462038Z",
                            "type": "job"
                        }
                    ],
                    "credentials": [
                        {
                            "id": 1,
                            "name": "Demo Credential",
                            "description": "",
                            "kind": "ssh",
                            "cloud": False,
                            "credential_type_id": 1
                        }
                    ]
                },
                "created": "2019-07-10T22:38:05.658620Z",
                "modified": "2019-11-12T20:23:33.515602Z",
                "name": "Demo Job Template",
                "description": "",
                "job_type": "run",
                "inventory": 2,
                "project": 4,
                "playbook": "hello_world.yml",
                "forks": 0,
                "limit": "",
                "verbosity": 0,
                "extra_vars": "",
                "job_tags": "",
                "force_handlers": False,
                "skip_tags": "",
                "start_at_task": "",
                "timeout": 0,
                "use_fact_cache": False,
                "last_job_run": "2019-12-18T16:25:40.839231Z",
                "last_job_failed": True,
                "next_job_run": None,
                "status": "failed",
                "host_config_key": "",
                "ask_diff_mode_on_launch": False,
                "ask_variables_on_launch": False,
                "ask_limit_on_launch": False,
                "ask_tags_on_launch": False,
                "ask_skip_tags_on_launch": False,
                "ask_job_type_on_launch": False,
                "ask_verbosity_on_launch": False,
                "ask_inventory_on_launch": False,
                "ask_credential_on_launch": False,
                "survey_enabled": False,
                "become_enabled": False,
                "diff_mode": False,
                "allow_simultaneous": False,
                "custom_virtualenv": None,
                "job_slice_count": 1,
                "credential": 1,
                "vault_credential": None
            }
        ]
    }
    
    return payload

def mocked_get_paged_jobs():
    payload = {
        "count": 3,
        "next": None,
        "previous": None,
        "results": [
            {
                "id": 1,
                "type": "job",
                "url": "/api/v2/jobs/1/",
                "related": {
                    "created_by": "/api/v2/users/1/",
                    "labels": "/api/v2/jobs/1/labels/",
                    "inventory": "/api/v2/inventories/1/",
                    "project": "/api/v2/projects/4/",
                    "credential": "/api/v2/credentials/1/",
                    "extra_credentials": "/api/v2/jobs/1/extra_credentials/",
                    "credentials": "/api/v2/jobs/1/credentials/",
                    "unified_job_template": "/api/v2/job_templates/5/",
                    "stdout": "/api/v2/jobs/1/stdout/",
                    "job_events": "/api/v2/jobs/1/job_events/",
                    "job_host_summaries": "/api/v2/jobs/1/job_host_summaries/",
                    "activity_stream": "/api/v2/jobs/1/activity_stream/",
                    "notifications": "/api/v2/jobs/1/notifications/",
                    "job_template": "/api/v2/job_templates/5/",
                    "cancel": "/api/v2/jobs/1/cancel/",
                    "project_update": "/api/v2/project_updates/3/",
                    "create_schedule": "/api/v2/jobs/1/create_schedule/",
                    "relaunch": "/api/v2/jobs/1/relaunch/"
                },
                "summary_fields": {
                    "inventory": {
                        "id": 1,
                        "name": "Demo Inventory",
                        "description": "",
                        "has_active_failures": True,
                        "total_hosts": 1,
                        "hosts_with_active_failures": 1,
                        "total_groups": 0,
                        "groups_with_active_failures": 0,
                        "has_inventory_sources": False,
                        "total_inventory_sources": 0,
                        "inventory_sources_with_failures": 0,
                        "organization_id": 1,
                        "kind": ""
                    },
                    "project": {
                        "id": 4,
                        "name": "Demo Project",
                        "description": "",
                        "status": "successful",
                        "scm_type": "git"
                    },
                    "project_update": {
                        "id": 3,
                        "name": "Demo Project",
                        "description": "",
                        "status": "successful",
                        "failed": False
                    },
                    "job_template": {
                        "id": 5,
                        "name": "Demo Job Template",
                        "description": ""
                    },
                    "unified_job_template": {
                        "id": 5,
                        "name": "Demo Job Template",
                        "description": "",
                        "unified_job_type": "job"
                    },
                    "instance_group": {
                        "name": "tower",
                        "id": 1
                    },
                    "created_by": {
                        "id": 1,
                        "username": "admin",
                        "first_name": "",
                        "last_name": ""
                    },
                    "user_capabilities": {
                        "delete": True,
                        "start": True
                    },
                    "labels": {
                        "count": 0,
                        "results": [

                        ]
                    },
                    "credentials": [
                        {
                            "id": 1,
                            "name": "Demo Credential",
                            "description": "",
                            "kind": "ssh",
                            "cloud": False,
                            "credential_type_id": 1
                        }
                    ]
                },
                "created": "2019-11-11T21:51:02.009680Z",
                "modified": "2019-11-11T21:51:07.426058Z",
                "name": "Demo Job Template",
                "description": "",
                "unified_job_template": 5,
                "launch_type": "manual",
                "status": "successful",
                "failed": False,
                "started": "2019-11-11T21:51:07.528070Z",
                "finished": "2019-11-11T21:51:12.398154Z",
                "elapsed": 4.87,
                "job_explanation": "",
                "execution_node": "localhost",
                "controller_node": "",
                "job_type": "run",
                "inventory": 1,
                "project": 4,
                "playbook": "hello_world.yml",
                "forks": 0,
                "limit": "",
                "verbosity": 0,
                "extra_vars": "{}",
                "job_tags": "",
                "force_handlers": False,
                "skip_tags": "",
                "start_at_task": "",
                "timeout": 0,
                "use_fact_cache": False,
                "job_template": 5,
                "passwords_needed_to_start": [

                ],
                "ask_diff_mode_on_launch": False,
                "ask_variables_on_launch": False,
                "ask_limit_on_launch": False,
                "ask_tags_on_launch": False,
                "ask_skip_tags_on_launch": False,
                "ask_job_type_on_launch": False,
                "ask_verbosity_on_launch": False,
                "ask_inventory_on_launch": False,
                "ask_credential_on_launch": False,
                "allow_simultaneous": False,
                "artifacts": {

                },
                "scm_revision": "347e44fea036c94d5f60e544de006453ee5c71ad",
                "instance_group": 1,
                "diff_mode": False,
                "job_slice_number": 0,
                "job_slice_count": 1,
                "credential": 1,
                "vault_credential": None
            },
            {
                "id": 4,
                "type": "job",
                "url": "/api/v2/jobs/4/",
                "related": {
                    "created_by": "/api/v2/users/1/",
                    "labels": "/api/v2/jobs/4/labels/",
                    "inventory": "/api/v2/inventories/1/",
                    "project": "/api/v2/projects/4/",
                    "credential": "/api/v2/credentials/1/",
                    "extra_credentials": "/api/v2/jobs/4/extra_credentials/",
                    "credentials": "/api/v2/jobs/4/credentials/",
                    "unified_job_template": "/api/v2/job_templates/5/",
                    "stdout": "/api/v2/jobs/4/stdout/",
                    "job_events": "/api/v2/jobs/4/job_events/",
                    "job_host_summaries": "/api/v2/jobs/4/job_host_summaries/",
                    "activity_stream": "/api/v2/jobs/4/activity_stream/",
                    "notifications": "/api/v2/jobs/4/notifications/",
                    "job_template": "/api/v2/job_templates/5/",
                    "cancel": "/api/v2/jobs/4/cancel/",
                    "project_update": "/api/v2/project_updates/6/",
                    "create_schedule": "/api/v2/jobs/4/create_schedule/",
                    "relaunch": "/api/v2/jobs/4/relaunch/"
                },
                "summary_fields": {
                    "inventory": {
                        "id": 1,
                        "name": "Demo Inventory",
                        "description": "",
                        "has_active_failures": True,
                        "total_hosts": 1,
                        "hosts_with_active_failures": 1,
                        "total_groups": 0,
                        "groups_with_active_failures": 0,
                        "has_inventory_sources": False,
                        "total_inventory_sources": 0,
                        "inventory_sources_with_failures": 0,
                        "organization_id": 1,
                        "kind": ""
                    },
                    "project": {
                        "id": 4,
                        "name": "Demo Project",
                        "description": "",
                        "status": "successful",
                        "scm_type": "git"
                    },
                    "project_update": {
                        "id": 6,
                        "name": "Demo Project",
                        "description": "",
                        "status": "successful",
                        "failed": False
                    },
                    "job_template": {
                        "id": 5,
                        "name": "Demo Job Template",
                        "description": ""
                    },
                    "unified_job_template": {
                        "id": 5,
                        "name": "Demo Job Template",
                        "description": "",
                        "unified_job_type": "job"
                    },
                    "instance_group": {
                        "name": "tower",
                        "id": 1
                    },
                    "created_by": {
                        "id": 1,
                        "username": "admin",
                        "first_name": "",
                        "last_name": ""
                    },
                    "user_capabilities": {
                        "delete": True,
                        "start": True
                    },
                    "labels": {
                        "count": 0,
                        "results": [

                        ]
                    },
                    "credentials": [
                        {
                            "id": 1,
                            "name": "Demo Credential",
                            "description": "",
                            "kind": "ssh",
                            "cloud": False,
                            "credential_type_id": 1
                        }
                    ]
                },
                "created": "2019-11-12T14:18:47.667936Z",
                "modified": "2019-11-12T14:18:52.396564Z",
                "name": "Demo Job Template",
                "description": "",
                "unified_job_template": 5,
                "launch_type": "manual",
                "status": "successful",
                "failed": False,
                "started": "2019-11-12T14:18:52.468318Z",
                "finished": "2019-11-12T14:18:56.932243Z",
                "elapsed": 4.464,
                "job_explanation": "",
                "execution_node": "localhost",
                "controller_node": "",
                "job_type": "run",
                "inventory": 1,
                "project": 4,
                "playbook": "hello_world.yml",
                "forks": 0,
                "limit": "",
                "verbosity": 0,
                "extra_vars": "{}",
                "job_tags": "",
                "force_handlers": False,
                "skip_tags": "",
                "start_at_task": "",
                "timeout": 0,
                "use_fact_cache": False,
                "job_template": 5,
                "passwords_needed_to_start": [

                ],
                "ask_diff_mode_on_launch": False,
                "ask_variables_on_launch": False,
                "ask_limit_on_launch": False,
                "ask_tags_on_launch": False,
                "ask_skip_tags_on_launch": False,
                "ask_job_type_on_launch": False,
                "ask_verbosity_on_launch": False,
                "ask_inventory_on_launch": False,
                "ask_credential_on_launch": False,
                "allow_simultaneous": False,
                "artifacts": {

                },
                "scm_revision": "347e44fea036c94d5f60e544de006453ee5c71ad",
                "instance_group": 1,
                "diff_mode": False,
                "job_slice_number": 0,
                "job_slice_count": 1,
                "credential": 1,
                "vault_credential": None
            },
            {
                "id": 7,
                "type": "job",
                "url": "/api/v2/jobs/7/",
                "related": {
                    "created_by": "/api/v2/users/1/",
                    "labels": "/api/v2/jobs/7/labels/",
                    "inventory": "/api/v2/inventories/1/",
                    "project": "/api/v2/projects/4/",
                    "credential": "/api/v2/credentials/1/",
                    "extra_credentials": "/api/v2/jobs/7/extra_credentials/",
                    "credentials": "/api/v2/jobs/7/credentials/",
                    "unified_job_template": "/api/v2/job_templates/5/",
                    "stdout": "/api/v2/jobs/7/stdout/",
                    "job_events": "/api/v2/jobs/7/job_events/",
                    "job_host_summaries": "/api/v2/jobs/7/job_host_summaries/",
                    "activity_stream": "/api/v2/jobs/7/activity_stream/",
                    "notifications": "/api/v2/jobs/7/notifications/",
                    "job_template": "/api/v2/job_templates/5/",
                    "cancel": "/api/v2/jobs/7/cancel/",
                    "project_update": "/api/v2/project_updates/9/",
                    "create_schedule": "/api/v2/jobs/7/create_schedule/",
                    "relaunch": "/api/v2/jobs/7/relaunch/"
                },
                "summary_fields": {
                    "inventory": {
                        "id": 1,
                        "name": "Demo Inventory",
                        "description": "",
                        "has_active_failures": True,
                        "total_hosts": 1,
                        "hosts_with_active_failures": 1,
                        "total_groups": 0,
                        "groups_with_active_failures": 0,
                        "has_inventory_sources": False,
                        "total_inventory_sources": 0,
                        "inventory_sources_with_failures": 0,
                        "organization_id": 1,
                        "kind": ""
                    },
                    "project": {
                        "id": 4,
                        "name": "Demo Project",
                        "description": "",
                        "status": "successful",
                        "scm_type": "git"
                    },
                    "project_update": {
                        "id": 9,
                        "name": "Demo Project",
                        "description": "",
                        "status": "successful",
                        "failed": False
                    },
                    "job_template": {
                        "id": 5,
                        "name": "Demo Job Template",
                        "description": ""
                    },
                    "unified_job_template": {
                        "id": 5,
                        "name": "Demo Job Template",
                        "description": "",
                        "unified_job_type": "job"
                    },
                    "instance_group": {
                        "name": "tower",
                        "id": 1
                    },
                    "created_by": {
                        "id": 1,
                        "username": "admin",
                        "first_name": "",
                        "last_name": ""
                    },
                    "user_capabilities": {
                        "delete": True,
                        "start": True
                    },
                    "labels": {
                        "count": 0,
                        "results": [

                        ]
                    },
                    "credentials": [
                        {
                            "id": 1,
                            "name": "Demo Credential",
                            "description": "",
                            "kind": "ssh",
                            "cloud": False,
                            "credential_type_id": 1
                        }
                    ]
                },
                "created": "2019-11-12T15:15:13.297516Z",
                "modified": "2019-11-12T15:15:20.604918Z",
                "name": "Demo Job Template",
                "description": "",
                "unified_job_template": 5,
                "launch_type": "manual",
                "status": "pending",
                "failed": False,
                "started": "2019-12-12T15:15:20.713567Z",
                "finished": "2019-12-12T15:15:28.768374Z",
                "elapsed": 8.055,
                "job_explanation": "",
                "execution_node": "localhost",
                "controller_node": "",
                "job_type": "run",
                "inventory": 1,
                "project": 4,
                "playbook": "hello_world.yml",
                "forks": 0,
                "limit": "",
                "verbosity": 0,
                "extra_vars": "{}",
                "job_tags": "",
                "force_handlers": False,
                "skip_tags": "",
                "start_at_task": "",
                "timeout": 0,
                "use_fact_cache": False,
                "job_template": 5,
                "passwords_needed_to_start": [

                ],
                "ask_diff_mode_on_launch": False,
                "ask_variables_on_launch": False,
                "ask_limit_on_launch": False,
                "ask_tags_on_launch": False,
                "ask_skip_tags_on_launch": False,
                "ask_job_type_on_launch": False,
                "ask_verbosity_on_launch": False,
                "ask_inventory_on_launch": False,
                "ask_credential_on_launch": False,
                "allow_simultaneous": False,
                "artifacts": {

                },
                "scm_revision": "347e44fea036c94d5f60e544de006453ee5c71ad",
                "instance_group": 1,
                "diff_mode": False,
                "job_slice_number": 0,
                "job_slice_count": 1,
                "credential": 1,
                "vault_credential": None
            }
        ]
    }

    return payload

def mocked_launch_job_template():
    payload = {
        "job": 152,
        "ignored_fields": {

        },
        "id": 152,
        "type": "job",
        "url": "/api/v2/jobs/152/",
        "related": {
            "created_by": "/api/v2/users/1/",
            "modified_by": "/api/v2/users/1/",
            "labels": "/api/v2/jobs/152/labels/",
            "inventory": "/api/v2/inventories/1/",
            "project": "/api/v2/projects/7/",
            "extra_credentials": "/api/v2/jobs/152/extra_credentials/",
            "credentials": "/api/v2/jobs/152/credentials/",
            "unified_job_template": "/api/v2/job_templates/6/",
            "stdout": "/api/v2/jobs/152/stdout/",
            "job_events": "/api/v2/jobs/152/job_events/",
            "job_host_summaries": "/api/v2/jobs/152/job_host_summaries/",
            "activity_stream": "/api/v2/jobs/152/activity_stream/",
            "notifications": "/api/v2/jobs/152/notifications/",
            "job_template": "/api/v2/job_templates/6/",
            "cancel": "/api/v2/jobs/152/cancel/",
            "create_schedule": "/api/v2/jobs/152/create_schedule/",
            "relaunch": "/api/v2/jobs/152/relaunch/"
        },
        "summary_fields": {
            "inventory": {
                "id": 1,
                "name": "Demo Inventory",
                "description": "",
                "has_active_failures": True,
                "total_hosts": 1,
                "hosts_with_active_failures": 1,
                "total_groups": 0,
                "groups_with_active_failures": 0,
                "has_inventory_sources": False,
                "total_inventory_sources": 0,
                "inventory_sources_with_failures": 0,
                "organization_id": 1,
                "kind": ""
            },
            "project": {
                "id": 7,
                "name": "2nd Project",
                "description": "",
                "status": "ok",
                "scm_type": ""
            },
            "job_template": {
                "id": 6,
                "name": "2nd demo",
                "description": ""
            },
            "unified_job_template": {
                "id": 6,
                "name": "2nd demo",
                "description": "",
                "unified_job_type": "job"
            },
            "created_by": {
                "id": 1,
                "username": "admin",
                "first_name": "",
                "last_name": ""
            },
            "modified_by": {
                "id": 1,
                "username": "admin",
                "first_name": "",
                "last_name": ""
            },
            "user_capabilities": {
                "delete": True,
                "start": True
            },
            "labels": {
                "count": 0,
                "results": [

                ]
            },
            "extra_credentials": [

            ],
            "credentials": [

            ]
        },
        "created": "2019-12-31T14:13:35.004317Z",
        "modified": "2019-12-31T14:13:35.117003Z",
        "name": "2nd demo",
        "description": "",
        "job_type": "run",
        "inventory": 1,
        "project": 7,
        "playbook": "hello_world.yml",
        "forks": 0,
        "limit": "all",
        "verbosity": 0,
        "extra_vars": "{\"msg\": \"hello\"}",
        "job_tags": "",
        "force_handlers": False,
        "skip_tags": "",
        "start_at_task": "",
        "timeout": 0,
        "use_fact_cache": False,
        "unified_job_template": 6,
        "launch_type": "manual",
        "status": "pending",
        "failed": False,
        "started": None,
        "finished": None,
        "elapsed": 0.0,
        "job_args": "",
        "job_cwd": "",
        "job_env": {

        },
        "job_explanation": "",
        "execution_node": "",
        "controller_node": "",
        "result_traceback": "",
        "event_processing_finished": False,
        "job_template": 6,
        "passwords_needed_to_start": [

        ],
        "ask_diff_mode_on_launch": False,
        "ask_variables_on_launch": True,
        "ask_limit_on_launch": True,
        "ask_tags_on_launch": True,
        "ask_skip_tags_on_launch": False,
        "ask_job_type_on_launch": False,
        "ask_verbosity_on_launch": False,
        "ask_inventory_on_launch": False,
        "ask_credential_on_launch": False,
        "allow_simultaneous": False,
        "artifacts": {

        },
        "scm_revision": "",
        "instance_group": None,
        "diff_mode": False,
        "job_slice_number": 0,
        "job_slice_count": 1,
        "credential": None,
        "vault_credential": None
    }

    return payload
