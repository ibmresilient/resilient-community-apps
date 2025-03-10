# -*- coding: utf-8 -*-

import sys
import time
from collections import OrderedDict

import pytest
from data_feeder_plugins.elasticfeed.elasticfeed import ElasticFeedDestination
from elasticsearch import Elasticsearch
from mock import patch

from rc_data_feed.lib.type_info import ActionMessageTypeInfo

TYPE_NAME = "all_types"

APP_CONFIG = {
    "class": "ElasticFeed",
    "url": "https://9.46.73.248",
    "port": "9200",
    "auth_user": "elastic",
    "auth_password": "Af4L5LmnU9JyscOwtoYr",
    "index_prefix": "res_test_",
    "cafile": "false"
}

TS = int(time.time())

INDEX = u"{}{}".format(APP_CONFIG['index_prefix'], TYPE_NAME)

ES = Elasticsearch("{}:{}".format(APP_CONFIG['url'], APP_CONFIG['port']),
                   verify_certs=False,
                   basic_auth=(APP_CONFIG['auth_user'], APP_CONFIG['auth_password']))

MSG_PAYLOAD = OrderedDict({"id":  TS,
                           "inc_id": 2301,
                           "test_text": u"ƀ Ɓ Ƃ ƃ Ƅ ƅ Ɔ Ƈ ƈ",
                           "test_int": 1000,
                           "test_date": 1550073347448,
                           "test_datetime": 1550073347448,
                           "test_bool": True
                           })

RESULT_PAYLOAD = {  "id":  TS,
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

def test_send_data_index_with_patch():
    """
    simple test coverage for index
    """

    with patch("data_feeder_plugins.elasticfeed.elasticfeed.Elasticsearch") as mock_elastic:

        es_feed = ElasticFeedDestination(None, APP_CONFIG)
        context = Context()
        mock_elastic.return_value.index.return_value = {"result": "created"}
        es_feed.send_data(context, MSG_PAYLOAD)

        # check properly constructed
        assert mock_elastic.called
        # check that index was called
        assert mock_elastic.return_value.index.called

def test_send_data_delete_with_patch():
    """
    simple test coverage for index
    """

    with patch("data_feeder_plugins.elasticfeed.elasticfeed.Elasticsearch") as mock_elastic:

        es_feed = ElasticFeedDestination(None, APP_CONFIG)
        context = Context(is_deleted=True)
        mock_elastic.return_value.delete.return_value = {"result": "deleted"}
        es_feed.send_data(context, MSG_PAYLOAD)

        # check properly constructed
        assert mock_elastic.called
        # check that index was called
        assert mock_elastic.return_value.delete.called


@pytest.mark.livetest
def test_index():
    """
    test that all fields sent for a elastic_feed are present
    :return:
    """
    es_feed = ElasticFeedDestination(None, APP_CONFIG)

    context = Context()
    es_feed.send_data(context, MSG_PAYLOAD)

    # test the results
    result = ES.get(index=INDEX, id=MSG_PAYLOAD['id'])

    for key, value in RESULT_PAYLOAD.items():
        assert result["_source"][key] == value

    assert result["_version"] == 1

@pytest.mark.livetest
def test_update():
    """
    test that all fields sent for a elastic_feed are present
    :return:
    """
    es_feed = ElasticFeedDestination(None, APP_CONFIG)

    context = Context()

    update_payload = MSG_PAYLOAD.copy()
    update_payload['test_text'] = "a" * 100
    update_result = RESULT_PAYLOAD.copy()
    update_result['test_text'] = update_payload['test_text']

    es_feed.send_data(context, update_payload)

    # test the results
    ES.indices.refresh(index=INDEX)

    result = ES.get(index=INDEX, id=update_payload['id'])

    for key, value in update_result.items():
        assert result["_source"][key] == value

    # depends on previous tests
    assert result["_version"] == 2

@pytest.mark.livetest
def test_alter():
    """
    test that all fields sent for a elastic_feed are present
    :return:
    """
    es_feed = ElasticFeedDestination(None, APP_CONFIG)

    context = Context()

    update_payload = MSG_PAYLOAD.copy()
    update_payload['alter_text'] = "this is a new column " + str(TS)
    update_result = RESULT_PAYLOAD.copy()
    update_result['alter_text'] = update_payload['alter_text']

    result = es_feed.send_data(context, update_payload)

    # test the results
    ES.indices.refresh(index=INDEX)

    test_result = ES.get(index=INDEX, id=update_payload['id'])

    for key, value in update_result.items():
        assert test_result["_source"][key] == value

    # depends on previous tests
    assert test_result["_version"] == 3

@pytest.mark.livetest
def test_delete():
    es_feed = ElasticFeedDestination(None, APP_CONFIG)

    context = Context(is_deleted=True)

    es_feed.send_data(context, MSG_PAYLOAD)

    # test the results
    with pytest.raises(Exception) as err:
        test_result = ES.get(index=INDEX, id=MSG_PAYLOAD['id'])
        assert err['found'] == False


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
