# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

import json
import re
from resilient_circuits import ResilientComponent
from fn_guardium_integration.util.static_data import INCIDENT_TYPE, INC_TYPE_PAYLOAD, ADD_INC_FIELDS, \
    INC_FIELDS_PAYLOAD, ADD_INCIDENT
from fn_guardium_integration.lib.custom_exceptions import TabledataRestCallError, ResilientActionError
from fn_guardium_integration.util.static_data import TABLE_ADD_ROW, DELETE_TABLE_ROW, GET_TABLE_DATA_BY_ID, \
    UPDATE_FIELD, CREATE_ACTION_FIELD, SECRET_STORE_FIELD


class ResilientRestService(ResilientComponent):
    """
    Resilient Rest Service handler
    """

    def __init__(self, opts, options, log):
        super(ResilientRestService, self).__init__(opts)
        self.opts = opts
        self.options = options
        self.log = log
        self.res_rest_client = self.rest_client()
        self.client_secret, self.unique_id, self.unit_type = self.get_client_secret()

    def get_client_secret(self):
        """
        Retrieve resilient incident Data
        :return:client Secret, uniqueID, guardium unit type i.e standlone/central Manager
        """
        field_data = self.get_field_definition(SECRET_STORE_FIELD)
        if not field_data or not field_data.get("values"):
            return None, None, None
        secret_data = field_data.get("values")[0].get("label")
        if secret_data:
            secret_data = re.sub("u'", "\"", secret_data)
            secret_data = re.sub("'", "\"", secret_data)
            json_data = json.loads(secret_data)
            return json_data.get("secret"), json_data.get("unique_id"), json_data.get("unit_type")

    def create_incident_type(self, incident_type_name):
        """
        Creates Resilient Incident type
        :param incident_type_name: Name of the incident type to be created in Resilient.
        :return:
        """
        payload = INC_TYPE_PAYLOAD.copy()
        payload["name"] = incident_type_name
        try:
            data = self.res_rest_client.post(INCIDENT_TYPE, payload=payload, timeout=300)
            self.log.info(u"Successfully created Incident type: {}".format(data))
        except Exception as er_msg:
            self.log.error(u"Failed to create Incident types: {}".format(er_msg))

    def add_incident_fields(self, field_name):
        """
        Adds Incident field to resilient
        :param field_name: Name of the incident field to be created.
        :return:
        """
        payload = INC_FIELDS_PAYLOAD.copy()
        payload["text"] = field_name
        payload["name"] = re.sub("\s", "_", field_name).lower()
        try:
            data = self.res_rest_client.post(ADD_INC_FIELDS, payload=payload, timeout=300)
            self.log.info(u"Successfully created Incident field: {}".format(data.get("name")))
        except Exception as er_msg:
            self.log.error(u"Failed to create Incident field: {}".format(er_msg))

    def add_incident(self, payload):
        """
        Creates new incident in resilient
        :param payload: Incident data payload
        :return:
        """
        try:
            data = self.res_rest_client.post(ADD_INCIDENT, payload=payload, timeout=300)
            self.log.info(u"--------------Resilient Incident Created--------------: {}".format(data.get('id')))
        except Exception as er_msg:
            self.log.error(u"Failed to create New Incident: {}".format(er_msg))

    def add_sigle_table_row_data(self, row_data, incident_id, table_id):
        """
        Method to add table row data.
        """
        try:
            self.res_rest_client.post(TABLE_ADD_ROW.format(incident_id, table_id), row_data, timeout=300)
        except Exception as err_msg:
            self.log.error(str(err_msg))

    def delete_resilient_table_row_data(self, row_id, incident_id, table_id):
        """
        Wrapper to delete a row from the data table
        :param res_rest_obj: Resilient rest client object
        :param incident_id: Resilient Incident ID
        :param table_id: Resilient table ID
        :param row_id: Resilient table row id to be deleted
        :return: on success return delete call result.
        """
        try:
            row_delete_status = self.res_rest_client.delete(
                DELETE_TABLE_ROW.format(inc_id=incident_id, table_id=table_id, row_id=row_id), timeout=300)
            return row_delete_status
        except Exception as er_msg:
            self.log.error(er_msg)

    def return_table_data_by_table_id(self, table_id, incident_id):
        """
        :param table_id: Resilient Table internal ID/name of the table
        :param incident_id: Resilient Incident ID
        :return: Table Data for the given table ID
        """
        try:
            __table_data = self.res_rest_client.get(GET_TABLE_DATA_BY_ID.format(inc_id=incident_id, table_id=table_id),
                                                    timeout=300)
        except Exception as err:
            raise TabledataRestCallError("Fetch Table data Rest Call Error - {}".format(err))
        if __table_data:
            return __table_data
        self.log.debug(u"No Table Data found in Resilient Incident : {}".format(incident_id))
        return None

    def get_field_definition(self, field_name, resilient_type="actioninvocation"):
        try:
            response = self.res_rest_client.get(UPDATE_FIELD.format(type=resilient_type, field=field_name),
                                                timeout=1000)
            return response
        except Exception as err_msg:
            self.log.warning("Error get field definition: {}, {}".format(field_name, err_msg))
            return dict()

    def update_rule_action_filed_values(self, managed_units, resilient_type="actioninvocation",
                                        resilient_field="grd_remote_data_source"):
        """
        :param managed_units: Host Name lists from Guardium
        :param resilient_type: Resilient field type
        :param resilient_field: Resilient action field name
        :return:
        """

        def update_actioninvocation_field(payload):
            param_values = []
            payload_values = payload.get("values", [])
            for each_value in payload_values:
                if each_value.get("label") == "Default":
                    param_values.append(each_value)
            if managed_units:
                for m_host in managed_units:
                    param_values.append({"label": str(m_host), "enabled": True, "hidden": False})
            payload["values"] = param_values
            return payload

        try:
            self.res_rest_client.get_put(UPDATE_FIELD.format(type=resilient_type, field=resilient_field),
                                         lambda payload: update_actioninvocation_field(payload), timeout=1000)
        except Exception as err_msg:
            raise ResilientActionError("Error: Resilient field : {} update error. {}".format(resilient_field, err_msg))

    def create_rule_action_select_field(self, field_name, field_value=None):
        """
        Function to Create new rule action select filed with given name & values.
        :param field_name: Resilient field name to be created
        :param field_value: List of Resilient filed value to added to field.
        :return: True on success, False on already exists
        {"label": "", "enabled": True, "hidden": False}
        """
        if field_value is None:
            field_value = []
        param_values = []
        __payload = {"name": "", "text": "", "prefix": "properties", "tooltip": "", "placeholder": "",
                     "input_type": "select", "blank_option": False, "values": [], "allow_default_value": False
                     }
        for each_value in field_value:
            param_values.append({"label": str(each_value), "enabled": True, "hidden": False})

        __payload["name"] = field_name
        __payload["text"] = field_name
        __payload["values"] = param_values

        try:
            self.res_rest_client.post(CREATE_ACTION_FIELD, payload=__payload, timeout=1000)
            return True
        except Exception as err_msg:
            self.log.warning("Action filed: {} create error: {}".format(field_name, err_msg))
            if str(err_msg).find("already exists in the type actioninvocation") != -1:
                return False
            raise ResilientActionError("Error while creating action field: {}".format(field_name))
