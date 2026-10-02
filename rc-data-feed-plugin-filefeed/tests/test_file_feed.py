# -*- coding: utf-8 -*-

import json
import os
import sys
from collections import OrderedDict
from data_feeder_plugins.filefeed.filefeed import FileFeedDestination
from rc_data_feed.lib.type_info import ActionMessageTypeInfo

DIRECTORY= "/tmp/filefeed"

TYPE_NAME = "incident"

APP_CONFIG = {
                "class": "FileFeed",
                "directory": DIRECTORY
             }

RESULT_PAYLOAD = {  "id":  10,
                    "inc_id": 2301,
                    "test_text": u"this is a text fieldँ ं ः अ आ इ ई उ ऊ ऋ ऌ ऍ ऎ",
                    "test_int": 1000,
                    "test_bool": 1
                  }

if sys.version_info.major == 2:
    RESULT_PAYLOAD['test_date']     = "2019-02-13T15:55:47"
    RESULT_PAYLOAD['test_datetime'] = "2019-02-13T15:55:47+00:00"
else:
    RESULT_PAYLOAD['test_date']     = "2019-02-13T15:55:47.448000"
    RESULT_PAYLOAD['test_datetime'] = "2019-02-13T15:55:47.448000+00:00"


MSG_PAYLOAD = OrderedDict({"id":  10,
                             "inc_id": 2301,
                             "test_text": u"this is a text fieldँ ं ः अ आ इ ई उ ऊ ऋ ऌ ऍ ऎ",
                             "test_int": 1000,
                             "test_date": 1550073347448,
                             "test_datetime": 1550073347448,
                             "test_bool": True
                           })

def test_file_feed():
    """
    test that all fields sent for a file_feed are present
    :return:
    """
    if not os.path.exists(DIRECTORY):
        os.mkdir(DIRECTORY)

    file_feed = FileFeedDestination(None, APP_CONFIG)

    context = Context()
    file_feed.send_data(context, MSG_PAYLOAD)

    # test the results
    name = context.type_info.get_pretty_type_name()

    output_file = file_feed._make_file_path(context, name, MSG_PAYLOAD)
    assert os.path.exists(output_file)

    with open(output_file, "r") as result_file:
        result = json.loads(result_file.read())

        for key, value in RESULT_PAYLOAD.items():
            assert result[key] == value

def test_update():
    """
    test that changed data appears after the first write
    :return:
    """
    if not os.path.exists(DIRECTORY):
        os.mkdir(DIRECTORY)

    file_feed = FileFeedDestination(None, APP_CONFIG)

    new_payload = MSG_PAYLOAD.copy()
    new_payload['test_text'] = u"a" * 1000  # changed data

    new_result = RESULT_PAYLOAD.copy()
    new_result["test_text"] = new_payload['test_text']

    context = Context()
    file_feed.send_data(context, new_payload)

    # test the results
    name = context.type_info.get_pretty_type_name()

    output_file = file_feed._make_file_path(context, name, new_payload)
    assert os.path.exists(output_file)

    with open(output_file, "r") as result_file:
        result = json.loads(result_file.read())

        for key, value in new_result.items():
            assert result[key] == value

def test_alter():
    """
    add a new field and confirm it's added
    :return:
    """
    if not os.path.exists(DIRECTORY):
        os.mkdir(DIRECTORY)

    file_feed = FileFeedDestination(None, APP_CONFIG)

    new_payload = MSG_PAYLOAD.copy()
    new_payload['alter_text'] = u"a" * 1000 # new field

    new_result = RESULT_PAYLOAD.copy()
    new_result["alter_text"] = new_payload['alter_text']

    context = Context()
    file_feed.send_data(context, new_payload)

    # test the results
    name = context.type_info.get_pretty_type_name()

    output_file = file_feed._make_file_path(context, name, new_payload)
    assert os.path.exists(output_file)

    with open(output_file, "r") as result_file:
        result = json.loads(result_file.read())

        for key, value in new_result.items():
            assert result[key] == value

class Context():
    """
    This class mimics that which is received when the message is dequeued from a message destination
    """
    def __init__(self, is_deleted=False):
        self.inc_id = RESULT_PAYLOAD['inc_id']
        self.type_info = ActionMessageTypeInfo(RESULT_PAYLOAD['id'],
                                               TYPE_INFO_MAP,
                                               None)        # no res_client is used
        # patch the two functions which make calls back to resilient to use our own dto objects
        self.type_info.get_all_fields = self.get_all_fields
        self.type_info.get_type = self.get_type
        self.is_deleted=is_deleted

    def get_all_fields(self, refresh=False):
        """
        mock the results
        :param refresh:
        :return:
        """
        return ALL_FIELDS_DTO

    def get_type(self, type_id):
        """
        mock the results
        :param type_id:
        :return:
        """
        return TYPE_DTO

# all_types object fields
FIELDS = {
    "id": {
        "id": 1,
        "name": "id",
        "prefix": None,
        "internal": False,
        "type_id": 1,
        "input_type": "number"
    },
    "inc_id": {
        "id": 2,
        "name": "inc_id",
        "prefix": None,
        "internal": False,
        "type_id": 1,
        "input_type": "number"
    },
    "test_text": {
        "id": 3,
        "name": "test_text",
        "prefix": None,
        "internal": False,
        "type_id": 2,
        "input_type": "text"
    },
    "test_int": {
        "id": 4,
        "name": "test_int",
        "prefix": None,
        "internal": False,
        "type_id": 1,
        "input_type": "number"
    },
    "test_date": {
        "id": 5,
        "name": "test_date",
        "internal": False,
        "type_id": 3,
        "input_type": "datepicker"
    },
    "test_datetime": {
        "id": 6,
        "name": "test_datetime",
        "prefix": None,
        "internal": False,
        "type_id": 4,
        "input_type": "datetimepicker",
    },
    "test_bool": {
        "id": 7,
        "name": "test_bool",
        "prefix": None,
        "internal": False,
        "type_id": 5,
        "input_type": "boolean"
    },
    "alter_text": {
        "id": 8,
        "name": "alter_text",
        "prefix": None,
        "internal": False,
        "type_id": 5,
        "input_type": "boolean"
    }
}

# format returned from api call /types/{type_id}
TYPE_DTO = {
    "id": 1,
    "type_id": 10,
    "type_name": "all_types",
    "fields": FIELDS
}

# format returned from /types/{type_id}/fields
ALL_FIELDS_DTO = [FIELDS[key] for key in FIELDS.keys()]

# format of data off the message queue
TYPE_INFO_MAP = {
    "all_types": {
        "fields": FIELDS
    }
}
