# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""
A file to Package static variables
"""
F_URL = "https://{bso_ip}/netaccess/connstatus.html"
F_LOGIN_URL = "https://{bso_ip}/netaccess/loginuser.html"
DEFAULT_INTERVAL = 600  # In Seconds
DEFAULT_DELTA_SCAN_RANGE = 900  # In seconds

# Resilient Rest URL
INCIDENT_TYPE = "/incident_types?handle_format=names"
ADD_INC_FIELDS = "/types/incident/fields"
ADD_INCIDENT = "/incidents?want_full_data=false&want_tasks=false&handle_format=names"
INCIDENT_TYPES = ["Guardium Policy Violations", "Guardium Outliers"]
GET_TABLE_DATA_BY_ID = "/incidents/{inc_id}/table_data/{table_id}?handle_format=names"
DELETE_TABLE_ROW = u"/incidents/{inc_id}/table_data/{table_id}/row_data/{row_id}"
TABLE_ADD_ROW = "/incidents/{}/table_data/{}/row_data?handle_format=names"
INC_FIELDS_PAYLOAD = {"name": "api_name", "input_type": "text", "required": None, "text": "field_name",
                      "blank_option": True, "changeable": True, "placeholder": "", "rich_text": False}
INC_TYPE_PAYLOAD = {"system": False, "parent_id": None, "create_date": None, "name": "new_inc_type", "hidden": False,
                    "enabled": True, "id": None, "description": "Created via new incident wizard"}
UPDATE_FIELD = "/types/{type}/fields/{field}?handle_format=names&include_principals=false"
CREATE_ACTION_FIELD = "/types/actioninvocation/fields?handle_format=names"

# This below field is used to store the client secret data generated from guardium
# This field created/updated by `generate client secret component`
SECRET_STORE_FIELD = "guardium_system_reference"

# Guardium Rest URL
GRD_BASE_URL = "https://{host}:{port}"
TOCKEN_URL = "{}/oauth/token".format(GRD_BASE_URL)
GRD_SEARCH = "{base_url}/restAPI/search?START_TIME={start_time}&END_TIME={end_time}"
GRD_FIELD = "{}/restAPI/fieldsTitles".format(GRD_BASE_URL)
GRD_LIST_PARAM = "{}/restAPI/list_parameter_names_by_report_name".format(GRD_BASE_URL)
GRD_ONLINE_REPORT = "{}/restAPI/online_report".format(GRD_BASE_URL)
GRD_GRP_MEMBER_BY_DESC = "{}/restAPI/group_members_by_group_desc".format(GRD_BASE_URL)
GRD_CREATE_GRP_MEM_BY_DESC = "{}/restAPI/group_member".format(GRD_BASE_URL)
RE_INSTALL_POLICY_URL = "{}/restAPI/reinstall_policy".format(GRD_BASE_URL)
LIST_INSTALLED_POLICY = "{}/restAPI/list_installed_policies".format(GRD_BASE_URL)

# Guardium Fields Data Default
GRD_FIELDS_JSON = {'44': 'File Path', '45': 'Command', '46': 'Avg. Response Time', '48': 'Total Instances',
                   '44;45': 'lucene.field.filepath.command', '8;9': 'Date Time', '90': 'Passed', '91': 'Failed',
                   '92': 'Textual Description', '50': 'High volume Outlier', '94': 'Sensitive Object',
                   '51': 'Vulnerable obj. Outlier', '52': 'New Outlier', '53': 'Diverse Outlier', '10': 'Database',
                   '54': 'Error Outlier', '11': 'Object', '55': 'Ongoing Outlier ', '12': 'Verb', '56': 'Alert Outlier',
                   '13': 'Details', '57': 'Failure', '14': 'Error', '58': 'Temp', '15': 'Violation', '59': 'New',
                   '16': 'Severity', '26;27': 'Classification Entities', '18': 'Anomaly Score',
                   '19': 'Number of Instances', '0': 'lucene.field.category', '1': 'OS User', '2': 'DB User',
                   '3': 'Client IP', '4': 'Source Program', '5': 'Client Host name', '11;12': 'Object Verb',
                   '6': 'Server', '7': 'DB Type', '8': 'Date', '9': 'Time', '60': 'Alert', '61': 'High volume',
                   '62': 'Privileged User', '63': 'Total Records Affected', '20': 'lucene.field.cluster',
                   '64': 'Effective Volume', '22': 'Outlier Reason', '23': 'Count', '25': 'Size',
                   '26': 'Classification', '27': 'Entities', '28': 'Owner', '70': 'Datasource Name', '71': 'DB Name',
                   '72': 'Version Level', '73': 'Patch Level', '74': 'Full Version Info',
                   '31': 'Read Privileged Groups', '75': 'Description', '32': 'Read Privileged Users', '76': 'Host',
                   '33': 'Write Privileged Groups', '77': 'Test Description', '34': 'Write Privileged Users',
                   '78': 'Test Score', '35': 'Execute Privileged Groups', '79': 'Score Description',
                   '36': 'Execute Privileged Users', '37': 'Delete Privileged Groups', '38': 'Delete Privileged Users',
                   '39': 'Modification Time', '_shard_': 'Guardium Appliance', '80': 'Result Text',
                   '81': 'Recommendation', '82': 'Assessment Description', '83': 'Port', '40': 'Creation Time',
                   '84': 'Datasource Id', '41': 'Effective End Time', '42': 'lucene.field.server.hostname',
                   '86': 'Result Details', '87': 'Category', '43': 'Time frame'}

SEARCH_TIME_FORMAT = "%Y%m%d+%H:%M:%S"
REPORT_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
SEARCH_COUNT = 10000
AUTOMATIC_INCIDENT_CREATION = False  # True - Enable Automatic Incident creation.
