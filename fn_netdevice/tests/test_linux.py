# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from fn_netdevice.lib.netmiko_core import execute

connection =  {
    'device_type': 'linux',
    'ip':   '192.168.56.3',
    'username': 'root',
    'password': 'Passw0rd',
    'port' : 22,        # optional, defaults to 22
    'secret': '',            # optional, defaults to ''
    'verbose': True     # optional, defaults to False
}

@pytest.mark.live
def test_success():

    my_connection = connection.copy()

    result = execute(my_connection, "ip address", None, False, False)

    assert not result.get('reason')
    assert result['status'] == 'success'
    assert result['send_result'].find('inet') != -1

@pytest.mark.live
def test_bad_password():

    my_connection = connection.copy()
    my_connection['password'] = ''

    result = execute(my_connection, None, None, False, False)

    assert result.get('reason')
    assert result['reason'].find('Authentication failure') != -1
    assert result['status'] == 'failure'

