import time
import json
import logging
from pymisp import ExpandedPyMISP, MISPAttribute, MISPEvent, MISPSighting
from resilient_lib import IntegrationError


log = logging.getLogger(__name__)

def get_misp_client(URL, API_KEY, VERIFY_CERT, proxies):
    misp_client = ExpandedPyMISP(URL, API_KEY, ssl=VERIFY_CERT, proxies=proxies)
    return misp_client

def create_misp_event(misp_client, misp_distribution, misp_threat_level, misp_analysis_level, misp_event_name):
    misp_event = MISPEvent()
    misp_event.distribution = misp_distribution
    misp_event.threat_level_id = misp_threat_level
    misp_event.analysis = misp_analysis_level
    misp_event.info = misp_event_name
    event_response = misp_client.add_event(misp_event)
    return event_response

def create_misp_attribute(misp_client, misp_event_id, misp_attribute_type, misp_attribute_value):
    misp_event = MISPEvent()
    misp_event.id = int(misp_event_id)
    misp_event.uuid = get_event_uuid(misp_client, misp_event_id)
    misp_attribute = MISPAttribute()
    misp_attribute.type = misp_attribute_type
    misp_attribute.value = misp_attribute_value
    attribute_response = misp_client.add_attribute(misp_event, misp_attribute)
    return attribute_response

def create_misp_sighting(misp_client, my_misp_sighting):
    misp_sighting = MISPSighting()
    misp_sighting.value = my_misp_sighting
    misp_sighting.timestamp = int(time.time())
    misp_sighting.source = "IBM Resilient SOAR"
    sighting_response = misp_client.add_sighting(misp_sighting)
    return sighting_response

def search_misp_attribute(misp_client, search_attribute):
    search_results = misp_client.search(value=search_attribute)
    if not isinstance(search_results, list):
        raise IntegrationError("Received an unexpected response type from the MISP API. Expected a list but received: {}".format(type(search_results)))
    search_results_len = len(search_results)
    if search_results_len == 0:
        success_status = False
    elif search_results_len > 0:
        success_status = True
    else:
        success_status = False
    search_results_response = { 
                                "search_status": success_status,
                                "search_results" : search_results
                            }
    return search_results_response

def get_event_tags(event):
    search_tags = []
    if "Tag" in event["Event"]:
        tags = event["Event"]["Tag"]
        for tag in tags:
            log.info("found tag {}".format(tag["name"]))
            search_tags.append(tag["name"])
    return search_tags

def get_attribute_tags(attribute):
    search_tags = []
    if "Tag" in attribute:
        for tag in attribute["Tag"]:
            log.info("found tag {}".format(tag["name"]))
            search_tags.append(tag["name"])
    return search_tags

def get_misp_attribute_tags(misp_client, search_results):
    search_tags = []
    log.debug(json.dumps(search_results, indent=4))
    for event in search_results:
        # Grab Event Tags
        search_tags += get_event_tags(event)
        # Grab Attribute Tags
        for attribute in event["Event"]["Attribute"]:
            search_tags += get_attribute_tags(attribute)
    search_tags = list(set(search_tags))
    return search_tags

def get_misp_sighting_list(misp_client, misp_event_id):
    misp_event = MISPEvent()
    misp_event.id = int(misp_event_id)
    sighting_result = misp_client.sightings(misp_event)
    return sighting_result

def get_event_uuid(misp_client, misp_event_id):
    # returns list with a single element: an event dict
    result = misp_client.search(eventid=misp_event_id)
    for event in result:
        event_uuid = event['Event']['uuid']
    return event_uuid
  
def get_attribute_uuid(misp_client, misp_attribute_value, misp_event_id):
    misp_event = MISPEvent()
    misp_event.id = int(misp_event_id)
    event_response = misp_client.get_event(misp_event)
    attribute_uuid = None
    if not event_response['Event']['Attribute']:
        log.error("Could not get a uuid for event = {} and attribute = {}. Does it exist?".format(misp_event_id, misp_attribute_value))
        raise IntegrationError("Failed to find any attributes on event {}".format(misp_event_id))

    else:
        for attribute in event_response['Event']['Attribute']:
            if attribute['value'] == misp_attribute_value:
                attribute_uuid = attribute['uuid']
        if attribute_uuid:
            return attribute_uuid
        else:
            raise IntegrationError("Failed to match attribute value = {} for any attributes associated with event = {}".format(misp_attribute_value, misp_event_id))

def create_tag(misp_client, misp_attribute_value, misp_tag_type, misp_tag_name, misp_event_id):
    if misp_tag_type == "Event":
        object_uuid = get_event_uuid(misp_client, misp_event_id)
    elif misp_tag_type == "Attribute":
        object_uuid = get_attribute_uuid(misp_client, misp_attribute_value, misp_event_id)
    tag_result = misp_client.tag(object_uuid, misp_tag_name)
    return tag_result