# (c) Copyright IBM Corp. 2018. All Rights Reserved.

from ldap3 import Server, Connection, ALL, ALL_ATTRIBUTES, MOCK_SYNC
from mock import Mock
import os

MOCK_DATA_PATH = os.getcwd() + "/tests/mock_data/"

class TestingHelper:

  # Create a fake LDAP server from the info and schema json files
  fake_server = Server.from_definition('my_fake_server', MOCK_DATA_PATH + 'mock_server_info.json', MOCK_DATA_PATH + 'mock_server_schema.json')

  def mocked_server(self):
    """Mock ldap3 server.
    :return: Return mocked server object
    """
    server = Mock(return_value=self.fake_server)
    return server

  def mocked_connection(self):
    """Mock ldap3 connection.
    :return: Return mocked connection object
    """
    # Create a MockSyncStrategy connection to the fake server
    mocked_connection = Connection(self.fake_server, user='cn=my_user,ou=test,o=lab', password='my_password', client_strategy=MOCK_SYNC)
    
    # Populate the DIT of the fake server with mock entries
    mocked_connection.strategy.entries_from_json(MOCK_DATA_PATH + 'mock_server_entries.json')

    connection = Mock(return_value=mocked_connection)
    return connection
