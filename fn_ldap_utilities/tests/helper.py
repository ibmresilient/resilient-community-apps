# (c) Copyright IBM Corp. 2018. All Rights Reserved.

from ldap3 import Server, Connection, ALL, ALL_ATTRIBUTES, MOCK_SYNC
from mock import Mock
import os


class TestingHelper():

  def __init__(self, isSearch=False):

    self.MOCK_DATA_PATH = os.getcwd() + "/tests/mock_data/"

    if isSearch:
      self.MOCK_DATA_PATH = os.getcwd() + "/tests/mock_data/search_specific/"
    
    # Create a fake LDAP server from the info and schema json files
    self.FAKE_SERVER = Server.from_definition('my_fake_server', self.MOCK_DATA_PATH + 'mock_server_info.json', self.MOCK_DATA_PATH + 'mock_server_schema.json')

  def mocked_server(self):
    """Mock ldap3 server.
    :return: Return mocked server object
    """
    server = Mock(return_value=self.FAKE_SERVER)
    return server

  def mocked_connection(self):
    """Mock ldap3 connection.
    :return: Return mocked connection object
    """
    # Create a MockSyncStrategy connection to the fake server
    mocked_connection = Connection(self.FAKE_SERVER, user='cn=my_user,ou=test,o=lab', password='my_password', client_strategy=MOCK_SYNC)
    
    # Populate the DIT of the fake server with mock entries
    mocked_connection.strategy.entries_from_json(self.MOCK_DATA_PATH + 'mock_server_entries.json')

    connection = Mock(return_value=mocked_connection)
    return connection

def get_mock_config_data():
    return u"""[fn_ldap_utilities]
ldap_server=192.168.0.1
ldap_port=389
ldap_use_ssl=False
ldap_auth=SIMPLE
ldap_user_dn=CN=Username,CN=Users,DC=example,DC=com
ldap_password=password
ldap_is_active_directory=True
ldap_connect_timeout=10"""