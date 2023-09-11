import pytest
from fn_service_now.util.resilient_helper import (
    SECOPS_PLAYBOOK_TASK_PREFIX, SECOPS_PLAYBOOK_TASK_TABLE_NAME,
    SECOPS_TABLE_NAME, ResilientHelper)


def test_get_table_name_non_secops():
	config_data = {
		"sn_host": "https://test.service-now.com",
		"sn_api_uri": "/api/x_ibmrt_resilient/api",
		"sn_table_name": "incident",
		"sn_username": "ibmresilient",
		"sn_password": "$testpassword"
	}

	res_helper = ResilientHelper(config_data)

	assert res_helper.get_table_name("INC1234") == "incident"

def test_get_table_name_secops():
	config_data = {
		"sn_host": "https://test.service-now.com",
		"sn_api_uri": "/api/x_ibmrt_resilient/api",
		"sn_table_name": SECOPS_TABLE_NAME,
		"sn_username": "ibmresilient",
		"sn_password": "$testpassword"
	}

	res_helper = ResilientHelper(config_data)

	assert res_helper.get_table_name("SIR1234") == SECOPS_TABLE_NAME
	
def test_get_table_name_secops_task():
	config_data = {
		"sn_host": "https://test.service-now.com",
		"sn_api_uri": "/api/x_ibmrt_resilient/api",
		"sn_table_name": SECOPS_TABLE_NAME,
		"sn_username": "ibmresilient",
		"sn_password": "$testpassword"
	}

	res_helper = ResilientHelper(config_data)

	assert res_helper.get_table_name(SECOPS_PLAYBOOK_TASK_PREFIX+"1234") == SECOPS_PLAYBOOK_TASK_TABLE_NAME
