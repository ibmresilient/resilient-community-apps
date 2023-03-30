# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
import logging
from resilient_lib import validate_fields, IntegrationError
from kafka import KafkaProducer

PACKAGE_NAME = "fn_kafka"
LOG = logging.getLogger(__name__)

def get_broker_section(opts, broker_label):
    # find the broker section
    broker_section_name = "{}:{}".format(PACKAGE_NAME, broker_label)
    broker_section = opts.get(broker_section_name)
    if not broker_section:
        msg = "Unable to find app.config section: {}".format(broker_section_name)
        raise IntegrationError(msg)
    else:
        validate_fields(["bootstrap_servers"], broker_section)

    return broker_section

def create_producer(opts, broker_label):
        # find the broker section
        broker_section = get_broker_section(opts, broker_label)

        # remove parts which don't relate to creating a producer
        pop_key(["topics", "template_dir", "group_id"], broker_section)
        return KafkaProducer(**broker_section)

def s_to_b(value):
    """[string to binary]"""
    if isinstance(value, dict):
        return_value = {}          
        for k, v in value.items():
            return_value[s_to_b(k)] = s_to_b(v)
    else:
        return_value = _s_to_b(value)
    return return_value
        
def _s_to_b(value):
    """[string to binary single value]"""
    try:
        return bytes(value, 'utf-8')
    except:
        return value

def b_to_s(value):
    """[binary to string]"""
    try:
        return value.decode()
    except:
        return value

def pop_key(keys, pop_dict):
    """[Pop key and return value if one is in argument. 
        otherwise just pop off dictionary]
    """
    if isinstance(keys, list):
        for key in keys:
            pop_key(key, pop_dict)

    elif keys in pop_dict:
        return pop_dict.pop(keys)

    return None 
