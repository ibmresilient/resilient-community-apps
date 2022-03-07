# -*- coding: utf-8 -*-
# pylint: disable=W0221
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
from json import dumps, JSONEncoder
import logging
from requests.compat import urljoin, quote
from .ReferenceObjectsBase import ReferenceObjectBase
from fn_qradar_integration.util.qradar_constants import REFERENCE_TABLE_URL
from resilient_lib import IntegrationError

LOG = logging.getLogger(__name__)
REF_TABLE_ENDPOINT = REFERENCE_TABLE_URL

class ByteEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8', errors='backslashreplace')
        return JSONEncoder.default(self, obj)

def get_as_str(a_str):
    """
    convert a python str from bytes type to str type if it was not a str type already
    """
    if not isinstance(a_str, str):
        return a_str.decode('utf-8')
    return a_str

class ReferenceTableFacade(ReferenceObjectBase):

    def __init__(self):
        self.failed_tbl_insert = 0

    @staticmethod
    def add_ref_element(client, ref_table, inner_key, outer_key, value):
        """
        Add the value to the given ref_table
        :param client: An instantiated rest client for QRadar 
        :type client: AuthInfo
        :param ref_table: the name of the reference table
        :type ref_table: str
        :param inner_key: The inner key of the reference table, similar to the row number for an sql table
        :type inner_key: str
        :param outer_key: The outer key of a given reference table entry
        :type outer_key: str
        :param value: The value to set for a reference table entry
        :type value: str
        :raises RequestError: If the API request is not successful an error is raised
        :return: the result of the API call
        :rtype: dict
        """
        ref_table_link = quote(ref_table, '')
        url = u"{}{}/{}?inner_key={}&outer_key={}&value={}".format(client.api_url, REF_TABLE_ENDPOINT,
                                         ref_table_link, inner_key, outer_key, value)

        ret = None
        try:
            data = {"value": value}
            response = client.make_call("POST", url, data=data)

            ret = {"status_code": response.status_code,
                   "content": response.json()}

        except Exception as e:
            LOG.error(str(e))
            raise IntegrationError("Request to url [{}] throws exception. Error [add_ref_element call failed with exception {}]".format(url, str(e)))

        else:
            return ret

    @staticmethod
    def update_ref_element(client, ref_table, inner_key, outer_key, value):
        """
        Update the value of an entry for the given ref_table
        :param client: An instantiated rest client for QRadar 
        :type client: AuthInfo
        :param ref_table: the name of the reference table
        :type ref_table: str
        :param inner_key: The inner key of the reference table, similar to the row number for an sql table
        :type inner_key: str
        :param outer_key: The outer key of a given reference table entry
        :type outer_key: str
        :param value: The value to set for a reference table entry
        :type value: str
        :raises RequestError: If the API request is not successful an error is raised
        :return: the result of the API call
        :rtype: dict
        """
        ref_table_link = quote(ref_table, '')
        value = quote(value, '')
        url = u"{}{}/{}?inner_key={}&outer_key={}&value={}".format(client.api_url, REF_TABLE_ENDPOINT,
                                         ref_table_link, inner_key, outer_key, value)
        ret = {}
        try:
            response = client.make_call("POST", url)

            ret = {"status_code": response.status_code,
                   "content": response.json()}

        except Exception as e:
            LOG.error(str(e))
            raise IntegrationError("Request to url [{}] throws exception. Error [update_ref_element call failed with exception {}]".format(url, str(e)))

        return ret

    @staticmethod
    def delete_ref_element(client, ref_table, inner_key, outer_key, value):
        """
        Delete a value from an entry in the given ref_table
        :param client: An instantiated rest client for QRadar 
        :type client: AuthInfo
        :param ref_table: the name of the reference table
        :type ref_table: str
        :param inner_key: The inner key of the reference table, similar to the row number for an sql table
        :type inner_key: str
        :param outer_key: The outer key of a given reference table entry
        :type outer_key: str
        :param value: The value to set for a reference table entry
        :type value: str
        :raises RequestError: If the API request is not successful an error is raised
        :return: the result of the API call
        :rtype: dict
        """
        ref_table_link = quote(ref_table, '')
        value = quote(value, '')

        url = u"{}{}/{}/{}/{}?value={}".format(client.api_url, REF_TABLE_ENDPOINT,
                                         ref_table_link, outer_key, inner_key, value)
        LOG.info(url)
        ret = {}
        try:
            response = client.make_call("DELETE", url)

            ret = {"status_code": response.status_code,
                   "content": response.json()}

        except Exception as e:
            LOG.error(str(e))
            raise IntegrationError("Delete request to url [{}] throws exception. Error [delete_ref_element failed with exception {}]".format(url, str(e)))

        return ret

    def bulk_upload(self, table_name, auth_info, data):
        """
        Adds or updates data in a reference table.  Supports bulk_load API which was introduced
        in version 7.0.  If bulk_load API is not supported the contents of the data is uploaded
        individually.
        @param data: the data to add or update in the reference table
        """
        number_failed_tble_insert = 0
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary!")
        request_url = urljoin(u"{}{}".format(
            REF_TABLE_ENDPOINT, '/bulk_load/'), quote(get_as_str(table_name)))
        dumps_data = dumps(data, cls=ByteEncoder)
        resp = auth_info.make_call("POST", request_url, data=dumps_data)
        if resp.status_code != 200:
            LOG.info('Error updating reference data table {0}; {1}'.format(
                table_name, resp.content), 'error')
            number_failed_tble_insert += 1
        self.failed_tbl_insert += number_failed_tble_insert

    @staticmethod
    def get_one_reference_table(client, table_name):
        """
        Get a list of all the reference tables.
        :return: list of reference table names
        """
        url = u"{}{}/{}".format(client.api_url, REF_TABLE_ENDPOINT, table_name)
        try:
            response = client.make_call("GET", url)
            #
            # Sample return:
            """
            [
                {
                    "timeout_type": "FIRST_SEEN",
                    "number_of_elements": 0,
                    "creation_time": 1516812810600,
                    "name": "Watson Advisor: File Action Blocked",
                    "element_type": "ALNIC"
                },
                ...
            ]
            """

        except Exception as e:
            LOG.error(str(e))
            raise IntegrationError("Request to url [{}] throws exception. Error [get_one_ref_teble call failed with exception {}]".format(url, str(e)))
        else:
            return response.json()

    @staticmethod
    def get_all_reference_tables(client):
        """
        Get a list of all the reference tables.
        :return: list of reference table names
        """
        url = u"{}{}".format(client.api_url, REF_TABLE_ENDPOINT)
        try:
            response = client.make_call("GET", url)
            #
            # Sample return:
            """
            [
                {
                    "timeout_type": "FIRST_SEEN",
                    "number_of_elements": 0,
                    "creation_time": 1516812810600,
                    "name": "Watson Advisor: File Action Blocked",
                    "element_type": "ALNIC"
                },
                ...
            ]
            """

        except Exception as e:
            LOG.error(str(e))
            raise IntegrationError("Request to url [{}] throws exception. Error [get_all_ref_tables call failed with exception {}]".format(url, str(e)))
        else:
            return response.json()
