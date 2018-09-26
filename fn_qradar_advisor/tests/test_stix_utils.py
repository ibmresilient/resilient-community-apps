# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

#
# Test file for relation_visitor.py
#
from fn_qradar_advisor.lib import stix_utils

import logging
logging.basicConfig(filename="testing.log", level=logging.DEBUG)

class TestStixUtils(object):

    def test_find_object_by_id(self):
        match_id = "match id"
        obj1 = {"id": "other id"}
        obj2 = {"id": match_id}
        obj3 = {"id": "obj3 id"}

        stix_objects = [obj1, obj2, obj3]

        obj = stix_utils.find_object_by_id(stix_objects, match_id)

        assert obj == obj2

    def test_get_observable(self):
        relevant = "high"
        toxicity = "low"
        type = "file"
        name = "fake file name"
        stix_obj = {
            stix_utils.IBM_RELEVANCE: relevant,
            "type": type,
            stix_utils.IBM_TOXICITY: toxicity,
            "name": name
        }

        observable = stix_utils.get_observable(stix_obj, logging)

        assert observable[u"toxicity"] == toxicity
        assert observable[u"relevance"] == relevant
        assert observable[u"type"] == type
        assert observable[u"description"] == name

    def test_get_observable_from_relation(self):
        stix_obj = {
            stix_utils.IBM_RELEVANCE: "high",
            "type": "relationship",
            stix_utils.IBM_TOXICITY: "low",
            "name": "fake name"
        }

        # a stix relation does not correspond to any observable
        ret = stix_utils.get_observable(stix_obj, logging)
        assert not ret

    def test_get_observables(self):
        relevant = "high"
        toxicity = "low"
        type = "file"
        name = "fake file name"
        stix_obj1 = {
            stix_utils.IBM_RELEVANCE: relevant,
            "type": type,
            stix_utils.IBM_TOXICITY: toxicity,
            "name": name
        }
        stix_obj2 = {
            stix_utils.IBM_RELEVANCE: relevant,
            "type": type,
            stix_utils.IBM_TOXICITY: toxicity,
            "name": "name 2"
        }
        stix_obj3 = {
            stix_utils.IBM_RELEVANCE: "high",
            "type": "relationship",
            stix_utils.IBM_TOXICITY: "low",
            "name": "fake name"
        }

        stix_json = {
            "objects": [stix_obj1, stix_obj2, stix_obj3]
        }

        observables = stix_utils.get_observables(stix_json, logging)

        # The relation shall not be here
        assert len(observables) == 2
        observable = observables[0]
        assert observable[u"toxicity"] == toxicity
        assert observable[u"relevance"] == relevant
        assert observable[u"type"] == type
        assert observable[u"description"] == name

    def test_get_observable_type(self):
        obj_type = "url"
        stix_obj = {
            stix_utils.IBM_RELEVANCE: "high",
            "id":"fake id",
            "type": "indicator",
            stix_utils.IBM_TOXICITY: "low",
            "name": "IpAddress",
            "objects":{
                "0": {
                    "type": obj_type
                },
                "1": {
                    "type": "Unknown"
                }
            }
        }

        obs_type = stix_utils.get_observable_type(stix_obj, logging)
        assert obs_type == "ipv4-addr"

        stix_obj["name"] = "Url"
        assert stix_utils.get_observable_type(stix_obj, logging) == "url"

        stix_obj["name"] = "DomainName"
        assert stix_utils.get_observable_type(stix_obj, logging) == "domain"

        # if we don't know how to map, use the object type
        stix_obj["name"] = "Fake"
        assert stix_utils.get_observable_type(stix_obj, logging) == stix_obj["type"]

        stix_obj["type"] = "observed-data"
        assert stix_utils.get_observable_type(stix_obj, logging) == obj_type

    def test_get_observable_description(self):
        obj_des = "object description"
        stix_obj = {
            stix_utils.IBM_RELEVANCE: "high",
            "id": "fake id",
            "type": "observed-data",
            stix_utils.IBM_TOXICITY: "low",
            "name": "IpAddress",
            "objects": {
                "0": {
                    "type": "fake type",
                    "value": obj_des
                },
                "1": {
                    "type": "Unknown"
                }
            }
        }

        assert obj_des == stix_utils.get_observable_description(stix_obj, logging)

        stix_obj["type"] = "indicator"
        ip_address = "8.8.8.8"
        stix_obj["pattern"] = "[ipv4-addr:value='" + ip_address + "']"
        assert ip_address == stix_utils.get_observable_description(stix_obj, logging)

        url = "https://www.google.com"
        stix_obj["name"] = "Url"
        stix_obj["pattern"] = "[url:value='" + url + "']"
        assert url == stix_utils.get_observable_description(stix_obj, logging)

        domain = "machine.company.com"
        stix_obj["name"] = "DomainName"
        stix_obj["pattern"] = "[domain-name:value='" + domain + "']"
        assert domain == stix_utils.get_observable_description(stix_obj, logging)

        stix_obj["name"] = "unknown name"
        # Don't know how to handle unknown name, return the pattern as string
        assert str(stix_obj["pattern"]) == stix_utils.get_observable_description(stix_obj, logging)

