# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
import time
from datetime import datetime, timedelta
import six
from fn_guardium_integration.lib.action_handler import thread_controller
from fn_guardium_integration.util.static_data import INCIDENT_TYPES, SEARCH_TIME_FORMAT


def evaluate_data(response, cls_ref, category):
    """
    param: response  - restful service get response for violations/outliers.
    param: cls_res   - GrdRestEndpoint Instance.
    param: category  - VIOLATION/OUTLIER.
    return: Evaluated data, a list contains dicts.
    """
    __last_proc_data = []
    __last_processed_time = []
    __eligible_events = []
    __tmp_fields = []
    __match_field = 1
    __match_element = 1
    __data_items_list = response[0].get("items")

    if category == "VIOLATION":
        __last_proc_data = cls_ref.last_proc_violation_data
    else:
        __last_proc_data = cls_ref.last_proc_outliers_data

    if __last_proc_data:
        for p_iteam in __last_proc_data:
            __last_processed_time.append("{}T{}".format(p_iteam.get("Date"), p_iteam.get("Time")))
        for event_data in __data_items_list:
            event_time = "{}T{}".format(event_data.get("Date"), event_data.get("Time"))
            for evt_k, evt_v in event_data.items():
                if evt_k != "id":
                    __tmp_fields.append(evt_k)
            if event_time in __last_processed_time:
                for p_iteam in __last_proc_data:
                    for f_data in __tmp_fields:
                        if p_iteam.get(f_data) == event_data.get(f_data):
                            __match_field *= 1
                        else:
                            __match_field *= 0
                    if __match_field:
                        __match_element *= 0
                        break
                    else:
                        __match_element *= 1
                        __match_field = 1
            if __match_element:
                __eligible_events.append(event_data)
            __match_element = 1
            __tmp_fields = []
        return __eligible_events

    else:
        return __data_items_list


def create_incident(data, cls_ref=None, inc_type="Other"):
    """
    Wrapper to create Resilient Incident for outliers and violations.
    {"name": "", "discovered_date": "", "start_date": "", "create_date": "",
                    "description": {"format": "text", "content": "Some description"},
                    "severity_code": {"name": "High"}, "plan_status": "Active",
                    "incident_type_ids": ["Table_Data_Store"]
                    }
    """
    gr_dt_string = "{}T{}".format(data.get("Date"), data.get("Time"))
    time_stamp_object = datetime.strptime(gr_dt_string, "%Y-%m-%dT%H:%M:%S")
    if six.PY2:
        gr_mili = int((time_stamp_object - datetime.fromtimestamp(0)).total_seconds()) * 1000
    else:
        gr_mili = int(time_stamp_object.timestamp() * 1000)
    if inc_type == INCIDENT_TYPES[0]:

        # Block to Generate the payload for Guardium Policy violations

        severity = ""
        gr_severity = int(data.get("Severity"))
        if gr_severity <= 4:
            severity = "Low"
        elif 5 <= gr_severity <= 7:
            severity = "Medium"
        elif 8 <= gr_severity <= 10:
            severity = "High"
        payload = {"name": "Guardium - {}".format(data.get("Violation")),
                   "discovered_date": gr_mili, "start_date": gr_mili, "create_date": int(time.time() * 1000),
                   "description": {"format": "text", "content": data.get("Violation")},
                   "severity_code": {"name": severity},
                   "plan_status": "Active", "incident_type_ids": [inc_type],
                   "properties": {"grd_inc_field_server": data.get("Server"),
                                  "grd_inc_field_database_type": data.get("DB Type"),
                                  "grd_inc_field_os_user": data.get("OS User"),
                                  "grd_inc_field_client_hostname": data.get("Client Host name"),
                                  "grd_inc_field_client_ip": data.get("Client IP"),
                                  "grd_inc_field_database": data.get("Database"),
                                  "grd_inc_field_source_program": data.get("Source Program"),
                                  "grd_inc_field_db_user": data.get("DB User")
                                  }
                   }
    else:

        # Block to Generate the payload for Guardium Outliers

        payload = {"name": "Guardium Outlier Server: {} and DB User: {} and Database: {}".format(data.get("Server"),
                                                                                                 data.get("DB User"),
                                                                                                 data.get("Database")),
                   "discovered_date": gr_mili, "start_date": gr_mili, "create_date": int(time.time() * 1000),
                   "description": {"format": "text", "content": "Guardium outlier summary event incident"},
                   "severity_code": {"name": "High"}, "plan_status": "Active", "incident_type_ids": [inc_type],
                   "properties": {"grd_inc_field_confidence_score": data.get("Anomaly Score"),
                                  "grd_inc_field_high_volume_outlier": data.get("High volume Outlier"),
                                  "grd_inc_field_vulnerable_obj_outlier": data.get("Vulnerable obj. Outlier"),
                                  "grd_inc_field_rare_or_new_behavior": data.get("New Outlier"),
                                  "grd_inc_field_diverse_behavior": data.get("Diverse Outlier"),
                                  "grd_inc_field_error_outlier": data.get("Error Outlier"),
                                  "grd_inc_field_ongoing_outlier": data.get("Ongoing Outlier "),
                                  "grd_inc_field_server": data.get("Server"),
                                  "grd_inc_field_database": data.get("Database"),
                                  "grd_inc_field_db_user": data.get("DB User"),
                                  "grd_inc_field_unusual_working_hours": data.get("Time frame"),
                                  "grd_inc_field_privileged_user": data.get("Privileged User")
                                  }
                   }

    cls_ref.resilient_rest_object.add_incident(payload)


def get_policy_violations_outliers(cls_ref):
    """
    param: cls_ref  -    FunctionComponent self
    """
    cls_ref.running_status = True  # Set the Running status flag
    # A block to reload the client secret data if not available
    if not cls_ref.grd_rest_object.client_secret:
        cls_ref.resilient_rest_object.log.info(
            u"Guardium client secret not generated, please run `Generate Guardium Client Secret`")
        secret, c_id, unit_type = cls_ref.resilient_rest_object.get_client_secret()
        if secret:
            cls_ref.grd_rest_object.client_secret = secret
            cls_ref.grd_rest_object.unique_id = c_id
            cls_ref.grd_rest_object.set_headers_with_new_access_token()
    else:
        # Get policy violation/outliers from guardium
        current_time = datetime.now()
        end_time = current_time.strftime(SEARCH_TIME_FORMAT)
        start_time = (current_time - timedelta(seconds=cls_ref.grd_rest_object.utc_offset)).strftime(SEARCH_TIME_FORMAT)

        cls_ref.grd_rest_object.log.info(
            u"Policy Violations & outliers Scan Range {} - {}".format(start_time, end_time))

        policy_violation_data = cls_ref.grd_rest_object.grd_search(category="VIOLATION", start_time=start_time,
                                                                   end_time=end_time)

        cls_ref.resilient_rest_object.log.info(
            u"Scanned Policy Violations Count: {}".format(policy_violation_data[0].get("numRows")))

        outliers_data = cls_ref.grd_rest_object.grd_search(category="OUTLIER_SUMMARY", start_time=start_time,
                                                           end_time=end_time)

        cls_ref.resilient_rest_object.log.info(
            u"Scanned Policy Outliers Count: {}".format(outliers_data[0].get("numRows")))

        evaluated_violation_data = evaluate_data(response=policy_violation_data, cls_ref=cls_ref, category="VIOLATION")
        evaluated_outliers_data = evaluate_data(response=outliers_data, cls_ref=cls_ref, category="OUTLIER")
        cls_ref.resilient_rest_object.log.debug(u"Evaluated violation data: {}".format(evaluated_violation_data))
        cls_ref.resilient_rest_object.log.debug(u"Evaluated outliers data: {}".format(evaluated_outliers_data))

        # Saving the current call to compare the duplicates in next call
        cls_ref.last_proc_violation_data = policy_violation_data[0].get("items")
        cls_ref.last_proc_outliers_data = outliers_data[0].get("items")

        thread_controller(function_object=create_incident, data=evaluated_violation_data, cls_ref=cls_ref,
                          inc_type=INCIDENT_TYPES[0])

        thread_controller(function_object=create_incident, data=evaluated_outliers_data, cls_ref=cls_ref,
                          inc_type=INCIDENT_TYPES[1])
    cls_ref.running_status = False  # Release the Running status flag
