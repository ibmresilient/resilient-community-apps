# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
#
#   Resilient Utils
#

from resilient_circuits import ResilientComponent
import logging
from fn_qradar_integration.util.exceptions.custom_exceptions import ResilientActionError

UPDATE_FIELD = "/types/actioninvocation/fields/{}?include_principals=false"

LOG = logging.getLogger(__name__)

class resilient_utils(ResilientComponent):
    def __init__(self, opts):
        super(resilient_utils, self).__init__(opts)
        self.res_rest_client = self.rest_client()

    def update_rule_action_field_values(self, field_name, field_values=None):
        """
        Update values in qradar_servers select field
        :param field_name: activity field name
        :param field_value: values to add to the activity field object
        :return:
        """
        try:
            def update_actioninvocation_field(payload):
                if type(payload) == list:
                    return payload

                if payload.get("values"):
                    for each_value in payload.get("values"):
                        if each_value.get("label") in field_values:
                            field_values.remove(each_value.get("label"))

                param_values = [
                    {"label": str(value), "enabled": True, "hidden": False}
                    for value in field_values
                ]

                payload["values"] = param_values

                return payload

            self.res_rest_client.get_put(UPDATE_FIELD.format(field_name), lambda payload: update_actioninvocation_field(payload), timeout=1000)

        except Exception as err_msg:
            LOG.warning("Action filed: {} error: {}".format(field_name, err_msg))
            raise ResilientActionError("Error while updating action field: {}".format(field_name))
