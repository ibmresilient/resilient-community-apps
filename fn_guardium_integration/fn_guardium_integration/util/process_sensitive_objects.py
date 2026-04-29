# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
import time
import six
from fn_guardium_integration.lib.action_handler import thread_controller
from fn_guardium_integration.lib.custom_exceptions import TabledataRestCallError


def update_sensitive_object_table(cls_ref, table_id, inc_id, search_data):
    """
    :param table_id: Resilient sensitive table
    :param inc_id: Resilient Incident ID
    :param search_data:Guardium Search data
    :return:
    """
    # clearing the existing table data
    try:
        existing_table_data = cls_ref.return_table_data_by_table_id(table_id=table_id, incident_id=inc_id)
        if existing_table_data.get("rows"):
            rows_data = existing_table_data.get("rows")
            rows_id_list = [x.get("id") for x in rows_data]
            if six.PY2:
                for row_id in rows_id_list:
                    cls_ref.delete_resilient_table_row_data(row_id, inc_id, table_id)
                    time.sleep(1)
            else:
                thread_controller(cls_ref.delete_resilient_table_row_data, rows_id_list, inc_id, table_id)
        else:
            cls_ref.log.debug("Selected table ID : {} is empty.".format(table_id))
    except Exception as er_msg:
        raise TabledataRestCallError(str(er_msg))

    # Processing the data
    data_list = construct_sensitive_objects_data(search_data)

    # Add data to the table
    thread_controller(cls_ref.add_sigle_table_row_data, data_list, inc_id, table_id)


def construct_sensitive_objects_data(list_search_results):
    facets_final_data = dict()
    table_cells_data = []
    for search_obj in list_search_results:
        facets_data = search_obj[0].get("facets")
        for facet_el in facets_data:
            event_cat = facet_el.get("label")
            if event_cat not in facets_final_data:
                facets_final_data[event_cat] = dict()
            subfacets_list = facet_el.get("subFacets")
            for sub_el in subfacets_list:
                sub_label = sub_el.get("label")
                sub_results = sub_el.get("numSubResults")
                if sub_label not in facets_final_data[event_cat]:
                    facets_final_data[event_cat][sub_label] = dict()
                    facets_final_data[event_cat][sub_label]["count"] = 0
                last_results = facets_final_data[event_cat][sub_label]["count"]
                sub_results += last_results
                facets_final_data[event_cat][sub_label]["count"] = sub_results
                if sub_results > 0:
                    for sub_sub_el in sub_el.get("subFacets"):
                        sub_sub_lable = sub_sub_el.get("label")
                        sub_sub_res = sub_sub_el.get("count")
                        if sub_sub_lable not in facets_final_data[event_cat][sub_label]:
                            facets_final_data[event_cat][sub_label][sub_sub_lable] = dict()
                            facets_final_data[event_cat][sub_label][sub_sub_lable] = 0
                        last_sub_sub_res = facets_final_data[event_cat][sub_label][sub_sub_lable]
                        sub_sub_res += last_sub_sub_res
                        facets_final_data[event_cat][sub_label][sub_sub_lable] = int(sub_sub_res)

    update_time = int(round(time.time() * 1000))
    for evt_cat, evt_sub_obj in facets_final_data.items():
        data_format = {"cells": {"grd_table_sensitive_event_category": {"value": ""},
                                 "grd_table_sensitive_date_generated": {"value": update_time},
                                 "grd_table_sensitive_event_property": {"value": ""},
                                 "grd_table_sensitive_highest_count_property": {"value": ""}
                                 }
                       }
        data_format["cells"]["grd_table_sensitive_event_category"]["value"] = evt_cat
        event_property = ""
        event_highest_property = ""
        for evt_sub, evt_sub_value in evt_sub_obj.items():
            evt_count = evt_sub_value.get("count")
            event_property += "<div><b>{}:</b>{}</div>".format(evt_sub, evt_count)
            if evt_count > 0:
                for evt_sub_value_key, evt_sub_value_value in evt_sub_value.items():
                    if evt_sub_value_key != "count":
                        event_highest_property += "<div><b>{}:</b>{}</div>".format(evt_sub_value_key,
                                                                                   evt_sub_value_value)
                data_format["cells"]["grd_table_sensitive_highest_count_property"]["value"] = event_highest_property
        data_format["cells"]["grd_table_sensitive_event_property"]["value"] = event_property
        table_cells_data.append(data_format)
    return table_cells_data
