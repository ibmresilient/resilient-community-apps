# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long

import logging

from resilient_lib.ui import Datatable, Field, Tab, create_tab, Section, HTMLBlock
from resilient_lib.ui.common import update_summary_layout
LOG = logging.getLogger(__name__)

PACKAGE = "fn_relations"

# Continue if exception is thrown
def init_relations_layout(opts):
    
    # this needs to be a nested class in order to use 'opts'
    class ChildIncidentTab(Tab):
      SECTION = PACKAGE
      NAME = "Child Incidents"
      UUID = "f831db07-27a0-b94e-aec7-2d599c68ad48"

      CONTAINS = [
          Datatable("dt_relations_child_incidents")
      ]

      SHOW_IF = [
          SelectField("relations_level", opts).conditions.equals("Parent")
      ]


    try:
        create_tab(ChildIncidentTab, opts, update_existing=True)
        LOG.info("Tab created: %s", ChildIncidentTab.NAME)

        section_list = [
            Section([
                      HTMLBlock("<h3>Relations</h3>"),
                      Field("relations_level")
                    ], 
                    [SelectField("relations_level", opts).conditions.equals("Parent")]),
            Section([
                      HTMLBlock("<h4>Relations</h4>"),
                      Field("relations_level"),
                      Field("relations_parent_id")
                    ],
                    [SelectField("relations_level", opts).conditions.equals("Child")])
        ]

        update_summary_layout(opts,
                              section_list,
                              header_of_block_to_add_after="Summary")
        LOG.info("Relation Sections created: %s", section_list)

    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", ChildIncidentTab.NAME, e)

## temporary definitions until code in resilient-lib
from resilient import get_client
from resilient_lib.ui.conditions import FieldConditions

class SelectFieldCondition(FieldConditions):
    def __init__(self, api_name, res_client):
        super(SelectFieldCondition, self).__init__(api_name)
        self.client = res_client

    def _get_value_for_select_field(self, value):
        types = self.client.cached_get("/types/incident")
        for value_mapping in types.get("fields", {}).get(self.api_name, {}).get("values", {}):
            if value_mapping.get("label") == value:
                return value_mapping.get("value")
        raise ValueError("Couldn't find value {0} for select field {1}".format(value, self.api_name))

    def has_value(self):
        return {
            "field": "incident.{}".format(self.api_name),
            "condition": "has_a_value"
        }

    def equals(self, value):
        return {
            "field": "incident.{}".format(self.api_name),
            "condition": "equals",
            "value": self._get_value_for_select_field(value)
        }

    def contains(self, value):
        return {
            "field": "incident.{}".format(self.api_name),
            "condition": "contains",
            "value": self._get_value_for_select_field(value)
        }

    def doesnt_contain(self, value):
        return {
            "field": "incident.{}".format(self.api_name),
            "condition": "not_contains",
            "value": self._get_value_for_select_field(value)
        }

    def doesnt_equal(self, value):
        return {
            "field": "incident.{}".format(self.api_name),
            "condition": "not_equals",
            "value": self._get_value_for_select_field(value)
        }

    def doesnt_have_value(self):
        return {
            "field": "incident.{}".format(self.api_name),
            "condition": "not_has_a_value"
        }

    def has_one_of(self, values):
        return {
            "field": "incident.{}".format(self.api_name),
            "condition": "in",
            "value": [self._get_value_for_select_field(value) for value in values]
        }

    def doesnt_have_one_of(self, values):
        return {
            "field": "incident.{}".format(self.api_name),
            "condition": "not_in",
            "value": [self._get_value_for_select_field(value) for value in values]
        }

class SelectField(Field):
    def __init__(self, api_name, opts):
        super(SelectField, self).__init__(api_name)
        res_client = get_client(opts)
        self.conditions = SelectFieldCondition(api_name=api_name, res_client=res_client)
