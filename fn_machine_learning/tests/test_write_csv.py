# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
#
import fn_machine_learning.lib.resilient_utils as resilient_utils
#
#   Make sure our CSV writer can handle different kinds of user input, including errors
#

field_dict = {"description": 1,
              "incident_ids": 2,
              "confirmed": 3,
              "owner_id": 4,
              "中文": 5,
              "custom_field": 6}

inc1 = {
    "description": 'This one contains comma, and imbalanced ", and \', and even \n ',
    "incident_ids": [1,2,3,4,5],
    "confirmed": False,
    "owner_id": 123456,
    "中文":"国际商用机器公司",
    "properties": {
        "custom_field": 1.02
    }
}

inc2 = {
    "description": 'This one contains commas,\n and imbalanced " and \', and even \n. Also Chinese word 中文 ',
    "incident_ids": [],
    "confirmed": False,
    "owner_id": 123456,
    "中文": "苹果",
    "properties": {
        "custom_field": 1.02
    }
}

def test_write():
    incidents = [inc1, inc2]

    num = resilient_utils.write_to_csv(incidents=incidents,
                                       fields_dict=field_dict,
                                       filename="tmp.csv")
    assert num==2
