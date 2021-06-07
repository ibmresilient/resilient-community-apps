# -*- coding: utf-8 -*-

import json
import sys
import time
from collections import OrderedDict
from rc_data_feed.lib.kafka_feed import KafkaFeedDestination
from rc_data_feed.lib.type_info import ActionMessageTypeInfo
from confluent_kafka import Consumer, KafkaError

TYPE_NAME = "all_types"
TOPIC = "resilient_test"

APP_CONFIG = {
    "class": "KafkaFeed",
    "topic_map": "default={}".format(TOPIC),
    "bootstrap.servers": "localhost:9092",
    "acks": "all",
    "message.timeout.ms": 5000
}

ts = int(time.time())

MSG_PAYLOAD = OrderedDict({"id":  ts,
                           "inc_id": 2301,
                           "test_text": u"ƀ Ɓ Ƃ ƃ Ƅ ƅ Ɔ Ƈ ƈ",
                           "test_int": 1000,
                           "test_date": 1550073347448,
                           "test_datetime": 1550073347448,
                           "test_bool": True
                           })

RESULT_PAYLOAD = {  "id":  ts,
                    "inc_id": 2301,
                    "test_text": u"ƀ Ɓ Ƃ ƃ Ƅ ƅ Ɔ Ƈ ƈ",
                    "test_int": 1000,
                    "test_bool": 1
                 }

if sys.version_info.major == 2:
    RESULT_PAYLOAD['test_date']     = "2019-02-13T15:55:47"
    RESULT_PAYLOAD['test_datetime'] = "2019-02-13T15:55:47+00:00"
else:
    RESULT_PAYLOAD['test_date']     = "2019-02-13T15:55:47.448000"
    RESULT_PAYLOAD['test_datetime'] = "2019-02-13T15:55:47.448000+00:00"


def test_send():
    """
    test that all fields sent for a file_feed are present
    :return:
    """
    p_feed = KafkaFeedDestination(None, APP_CONFIG)

    context = Context()
    p_feed.send_data(context, MSG_PAYLOAD)

    _kafka_consumer(APP_CONFIG)


def _kafka_consumer(app_settings):
    settings = dict(app_settings)
    settings.pop("topic_map")
    settings.pop("class")
    settings["auto.offset.reset"] = "earliest"
    settings["group.id"] = "mygroup"

    c = Consumer(settings)

    c.subscribe([TOPIC])

    try:
        found = False
        for x in range(0, 5):
            msg = c.poll(1.0)

            if msg is None:
                continue

            assert msg and not msg.error()

            # test content
            assert msg and msg.value()
            found = True
            result = json.loads(msg.value())
            assert result['test_text'] == RESULT_PAYLOAD['test_text']
            assert result['test_bool'] == RESULT_PAYLOAD['test_bool']
            assert result['test_date'] == RESULT_PAYLOAD['test_date']
            assert result['test_datetime'] == RESULT_PAYLOAD['test_datetime']
            assert result['test_int'] == RESULT_PAYLOAD['test_int']

            # test headers
            assert msg.headers()
            for header in msg.headers():
                if header[0] == b"type":
                    assert header[1] == TYPE_NAME
                if header[0] == b"action":
                    assert header[1] == b"upsert"

            break
    finally:
        c.close()

    assert found



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
        self.is_deleted = is_deleted

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
        "type_id": 2,
        "input_type": "text"
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
