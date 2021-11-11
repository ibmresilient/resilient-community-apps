# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
#
#   Resilient Utils
#

from resilient_circuits import ResilientComponent
import logging
from fn_qradar_integration.util.exceptions.custom_exceptions import ResilientActionError

UPDATE_FIELD = "/types/actioninvocation/fields/{}"
GET_FIELD = "/types/actioninvocation/fields/{}?include_principals=true"

LOG = logging.getLogger(__name__)

class resilient_utils(ResilientComponent):
    def __init__(self, opts):
        super(resilient_utils, self).__init__(opts)
        self.res_rest_client = self.rest_client()

    def create_payload(self, field_name, field_text, field_values=None):
        """
        Create payload to be sent to resilient
        :param field_name: activity field name
        :param field_value: values to add to the activity field object
        :return: payload
        """
        if field_values is None:
            field_values = []
        param_values = []
        payload = {"name": "", "text": "", "prefix": "properties", "tooltip": "", "placeholder": "",
                        "input_type": "select", "blank_option": False, "values": []}
        
        for value in field_values:
            param_values.append({"label": str(value), "enabled": "true", "hidden": "false"})

        payload["name"] = field_name
        payload["text"] = field_text
        payload["values"] = param_values
        return payload

    def update_rule_action_field_values(self, field_name, field_text, field_values=None):
        """
        Update values in qradar_servers select field
        :param field_name: activity field name
        :param field_value: values to add to the activity field object
        :return:
        """
        try:
            fields = self.res_rest_client.get(GET_FIELD.format(field_name))

            LOG.debug(str(fields))

            if type(fields) == list or fields.get("input_type") != "select":
                return None

            if fields.get("value"):
                select_field_name = "value"
            if fields.get("values"):
                select_field_name = "values"
            in_use_values = [
                value.get("label")
                for value in fields.get(select_field_name)
            ]

            fields_to_add = [
                value
                for value in field_values
                if value not in in_use_values
            ]

            if fields_to_add:
                payload = self.create_payload(field_name, field_text, fields_to_add)
                self.res_rest_client.put(UPDATE_FIELD.format(field_name), payload, timeout=1000)

        except Exception as err_msg:
            LOG.warning("Action filed: {} error: {}".format(field_name, err_msg))
            raise ResilientActionError("Error while updating action field: {}".format(field_name))
