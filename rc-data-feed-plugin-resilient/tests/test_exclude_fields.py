from data_feeder_plugins.resilientfeed.resilientfeed import exclude_incident_fields

TEST_PAYLOAD = {
                'dtm': {},
                'cm': {'unassigneds': [{'geo': 1000, 'count': 0}, {'geo': 1001, 'count': 0}], 'total': 0, 'geo_counts': {}},
                'regulators': {'ids': [149]},
                'hipaa': {'hipaa_adverse': None, 'hipaa_misused': None, 'hipaa_acquired': None, 'hipaa_additional_misuse': None, 'hipaa_breach': None, 'hipaa_adverse_comment': '', 'hipaa_misused_comment': '', 'hipaa_acquired_comment': '', 'hipaa_additional_misuse_comment': '', 'hipaa_breach_comment': ''},
                'tasks': None, 'artifacts': None, 'name': 'not synced',
                'description': '<div class="rte"><div>ssaavz12345</div></div>', 'phase_id': 1054, 'inc_training': False,
                'vers': 4, 'addr': None, 'city': None,
                'creator': {'id': 3, 'fname': 'Resilient', 'lname': 'Sysadmin', 'display_name': 'Resilient Sysadmin', 'status': 'A', 'email': 'a@example.com', 'last_login': 1584357940074, 'locked': False, 'password_changed': False, 'last_modified_time': 1584357940075, 'create_date': 1562157359632, 'is_external': False},
                'creator_principal': {'id': 3, 'type': 'user', 'name': 'a@example.com', 'display_name': 'Resilient Sysadmin'},
                'exposure_type_id': 1, 'incident_type_ids': [22, 21], 'reporter': None, 'state': None, 'country': None,
                'zip': '012345', 'workspace': 8, 'exposure': 0, 'org_handle': 208, 'members': [], 'negative_pr_likely': None,
                'perms': {'read': True, 'write': True, 'comment': True, 'assign': True, 'close': True, 'change_members': True, 'attach_file': True, 'read_attachments': True, 'delete_attachments': True, 'create_milestones': True, 'list_milestones': True, 'create_artifacts': True, 'list_artifacts': True, 'delete': True, 'change_workspace': True},
                'confirmed': True,
                'task_changes': {'added': [], 'removed': []},
                'assessment': '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n',
                'data_compromised': None, 'draft': False,
                'properties': {'custom_number': None, 'custom_datetime': None, 'custom_one': None, 'campaign_task_id': None, 'jira_url': None, 'messageID': None, 'proofpoint_trap_incident_id': None, 'qradar_id': None, 'ansible_value': None, 'custom_org_resilient': None, 'df_org_id': None, 'campaign_name': None, 'df_inc_id': None, 'jira_internal_url': None, 'scheduler_demo': None, 'campaign': None, 'custom_bool': None, 'campaign_id': None},
                'resolution_id': None, 'resolution_summary': None,
                'pii': {'data_compromised': None, 'determined_date': 1584317546746, 'harmstatus_id': 2, 'data_encrypted': None, 'data_contained': None, 'impact_likely': None, 'data_source_ids': [], 'data_format': None, 'assessment': '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<assessment>\n    <rollups/>\n    <optional>There are 1 required and 0 optional tasks from 1 regulators.</optional>\n</assessment>\n', 'exposure': 0, 'gdpr_harm_risk': None, 'gdpr_lawful_data_processing_categories': [], 'alberta_health_risk_assessment': None},
                'gdpr': {'gdpr_breach_circumstances': [], 'gdpr_breach_type': None, 'gdpr_personal_data': None, 'gdpr_identification': None, 'gdpr_consequences': None, 'gdpr_final_assessment': None, 'gdpr_breach_type_comment': None, 'gdpr_personal_data_comment': None, 'gdpr_identification_comment': None, 'gdpr_consequences_comment': None, 'gdpr_final_assessment_comment': None, 'gdpr_subsequent_notification': None},
                'regulator_risk': {}, 'inc_last_modified_date': 1584358007558, 'comments': None, 'actions': [],
                'admin_id': None, 'creator_id': 3, 'crimestatus_id': 5, 'employee_involved': None, 'end_date': None,
                'exposure_dept_id': None, 'exposure_individual_name': None, 'exposure_vendor_id': None, 'jurisdiction_name': None,
                'jurisdiction_reg_id': None, 'start_date': None, 'inc_start': None, 'org_id': 208, 'is_scenario': False,
                'hard_liability': 0, 'nist_attack_vectors': [], 'id': 2881, 'discovered_date': 1584317546746, 'due_date': None,
                'create_date': 1584358006532, 'owner_id': 3, 'severity_code': 1303, 'plan_status': 'A'
               }

def test_field():
    filters = ['confirmed', 'zip']

    payload = exclude_incident_fields(filters, TEST_PAYLOAD)
    for filter in filters:
        assert not payload.get(filter, None)

def test_section():
    filters = ['pii', 'gdpr']

    payload = exclude_incident_fields(filters, TEST_PAYLOAD)
    for filter in filters:
        assert not payload.get(filter, None)

def test_section_field():
    # part of pii section
    filters = ['determined_date']

    payload = exclude_incident_fields(filters, TEST_PAYLOAD)
    assert payload.get("pii", None)
    assert not payload["pii"].get('determined_date', None)
