
def get_mock_config_data():
    return u"""[fn_crowdstrike_falcon]
# API Client Authentication, CrowdStrike's newer standard based on OAuth2
cs_falcon_oauth2_base_url=https://api.crowdstrike.com
cs_falcon_oauth2_cid=xxxxxxxx
cs_falcon_oauth2_key=xxxxxxxx

# API Key Authentication, CrowdStrike's legacy authentication standard
cs_falcon_bauth_base_url=https://falconapi.crowdstrike.com
cs_falcon_bauth_api_uuid=xxxxxxxxx
cs_falcon_bauth_api_key=xxxxxxxxxx

cs_falcon_ping_timeout=10
cs_falcon_ping_delay=5
"""


def get_mock_device_response():
    return [{u'modified_timestamp': u'2019-02-25T14:30:01Z', u'config_id_platform': u'8', u'system_manufacturer': u'innotek GmbH', u'meta': {u'version': u'750'}, u'first_seen': u'2019-02-07T14:07:52Z', u'platform_id': u'3', u'local_ip': u'10.0.2.15', u'hostname': u'localhost.localdomain', u'config_id_build': u'6705', u'minor_version': u'10', u'os_version': u'CentOS 7', u'provision_status': u'Provisioned', u'mac_address': u'08-00-27-7d-a7-d2', u'bios_version': u'VirtualBox', u'agent_load_flags': u'0', u'status': u'contained', u'bios_manufacturer': u'innotek GmbH', u'product_type_desc': u'Server', u'device_policies': {u'sensor_update': {u'applied': True, u'applied_date': u'2019-02-25T14:30:01.762114269Z', u'settings_hash': u'65994753|8|2|automatic', u'policy_type': u'sensor-update', u'assigned_date': u'2019-02-25T14:28:10.932921642Z', u'policy_id': u'4eac5ba86b27414098820732fe7876f6'}, u'prevention': {u'applied': True, u'applied_date': u'2019-02-08T14:47:54.526691595Z', u'settings_hash': u'd4cbb29', u'policy_type': u'prevention', u'assigned_date': u'2019-02-08T14:47:47.25675937Z', u'policy_id': u'25291d90954c476d86c6fb2db38d7d72'}}, u'agent_local_time': u'2019-02-25T09:28:24.242Z', u'slow_changing_modified_timestamp': u'2019-02-25T14:29:02Z', u'device_id': u'606e693c6ac040107c07dcc7c7ed6785', u'system_product_name': u'VirtualBox', u'cid': u'b1e43228990c4bfe8e979969d955b800', u'external_ip': u'37.228.237.156', u'major_version': u'3', u'platform_name': u'Linux', u'config_id_base': u'65994753', u'policies': [{u'applied': True, u'applied_date': u'2019-02-08T14:47:54.526691595Z', u'settings_hash': u'd4cbb29', u'policy_type': u'prevention', u'assigned_date': u'2019-02-08T14:47:47.25675937Z', u'policy_id': u'25291d90954c476d86c6fb2db38d7d72'}], u'agent_version': u'4.21.6705.0', u'last_seen': u'2019-02-25T14:29:01Z'}]


def get_mock_results_content():
    return [{u'modified_timestamp': 1551105001000, u'major_version': u'3', u'config_id_platform': u'8', u'system_manufacturer': u'innotek GmbH', u'meta': {u'version': u'750'}, u'first_seen': 1549548472000, u'platform_name': u'Linux', u'product_type_desc': u'Server', u'hostname': u'localhost.localdomain', u'config_id_build': u'6705', u'minor_version': u'10', u'os_version': u'CentOS 7', u'provision_status': u'Provisioned', u'mac_address': u'08-00-27-7d-a7-d2', u'bios_version': u'VirtualBox', u'agent_load_flags': u'0', u'status': u'contained', u'bios_manufacturer': u'innotek GmbH', u'device_policies': {u'sensor_update': {u'applied': True, u'applied_date': u'2019-02-25T14:30:01.762114269Z', u'settings_hash': u'65994753|8|2|automatic', u'policy_type': u'sensor-update', u'assigned_date': u'2019-02-25T14:28:10.932921642Z', u'policy_id': u'4eac5ba86b27414098820732fe7876f6'}, u'prevention': {u'applied': True, u'applied_date': u'2019-02-08T14:47:54.526691595Z', u'settings_hash': u'd4cbb29', u'policy_type': u'prevention', u'assigned_date': u'2019-02-08T14:47:47.25675937Z', u'policy_id': u'25291d90954c476d86c6fb2db38d7d72'}}, u'agent_local_time': 1551086904242, u'slow_changing_modified_timestamp': u'2019-02-25T14:29:02Z', u'device_id': u'606e693c6ac040107c07dcc7c7ed6785', u'system_product_name': u'VirtualBox', u'local_ip': u'10.0.2.15', u'external_ip': u'37.228.237.156', u'cid': u'b1e43228990c4bfe8e979969d955b800', u'platform_id': u'3', u'config_id_base': u'65994753', u'policies': [{u'applied': True, u'applied_date': u'2019-02-08T14:47:54.526691595Z', u'settings_hash': u'd4cbb29', u'policy_type': u'prevention', u'assigned_date': u'2019-02-08T14:47:47.25675937Z', u'policy_id': u'25291d90954c476d86c6fb2db38d7d72'}], u'last_seen': 1551104941000, u'agent_version': u'4.21.6705.0'}]

def get_mock_contain_device_results_content():
    return {'meta': 'xxxxxx', 'device_status': 'contained', 'device_id': 'xxxxxx'}