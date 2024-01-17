# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long

import logging

from resilient_circuits.app import AppArgumentParser
from resilient_lib.ui import Datatable, Field, Tab, create_tab, Section, HTMLBlock
from resilient_lib.ui.common import update_summary_layout
LOG = logging.getLogger(__name__)

PACKAGE = "fn_relations"

class ChildIncidentTab(Tab):
    SECTION = PACKAGE
    NAME = "Child Incidents"
    UUID = "f831db07-27a0-b94e-aec7-2d599c68ad48"

    CONTAINS = [
        Datatable("dt_relations_child_incidents")
    ]

    SHOW_IF = [
        Field("relations_level").conditions.equals("Parent")
    ]

# Continue if exception is thrown
def init_relations_layout(opts):
    try:
        create_tab(ChildIncidentTab, opts, update_existing=True)
        LOG.info("Tab created: %s", ChildIncidentTab.NAME)

        section_list = [
            Section([Field("relations_level")], 
                    [Field("relations_level").conditions.equals("Parent")]),
            Section([
                      Field("relations_level"),
                      Field("relations_parent_id")
                    ],
                    [Field("relations_level").conditions.equals("Child")])
        ]

        update_summary_layout(opts,
                              section_list,
                              header_of_block_to_add_after="Summary")
        LOG.info("Relation Sections created: %s", section_list)

    except SystemExit as e:
        LOG.warning("Failed to create tab: %s.\nERROR: %s", ChildIncidentTab.NAME, e)

# extra UUIDs if needed. found by running:
# >>> import uuid
# >>> uuid.uuid4()
#
# UUID('b27793a5-7a40-407f-a8a6-ab0376875813')
# UUID('f986581c-93e7-4c71-a6fb-a0dd01993ff1')

    """
    {
      "element" : "section",
      "field_type" : null,
      "fields" : [ {
        "content" : "Incident Relations",
        "element" : "html",
        "field_type" : null,
        "show_if" : null,
        "show_link_header" : false,
        "step_label" : null
      }, {
        "content" : "relations_level",
        "element" : "field",
        "field_type" : "incident",
        "show_if" : null,
        "show_link_header" : false,
        "step_label" : null
      } ],
      "show_if" : [ {
        "condition" : "has_a_value",
        "field" : "incident.relations_level",
        "value" : null
      } ],
      "show_link_header" : false,
      "step_label" : null
    }, {
      "element" : "section",
      "field_type" : null,
      "fields" : [ {
        "content" : "relations_parent_id",
        "element" : "field",
        "field_type" : "incident",
        "show_if" : null,
        "show_link_header" : false,
        "step_label" : null
      } ],
      "show_if" : [ {
        "condition" : "has_a_value",
        "field" : "incident.relations_parent_id",
        "value" : null
      } ],
      "show_link_header" : false,
      "step_label" : null
    }
    """