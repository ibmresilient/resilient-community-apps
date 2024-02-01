from time import time
from json import dumps
from logging import getLogger
from pymisp import ExpandedPyMISP, MISPAttribute, MISPEvent, MISPSighting
from resilient_lib import IntegrationError

log = getLogger(__name__)

def get_misp_client(URL, API_KEY, VERIFY_CERT, proxies):
    return ExpandedPyMISP(URL, API_KEY, ssl=VERIFY_CERT, proxies=proxies)

def create_misp_event(misp_client, misp_distribution, misp_threat_level, misp_analysis_level, misp_event_name):
    misp_event = MISPEvent()
    misp_event.distribution = misp_distribution
    misp_event.threat_level_id = misp_threat_level
    misp_event.analysis = misp_analysis_level
    misp_event.info = misp_event_name
    return misp_client.add_event(misp_event)

def create_misp_attribute(misp_client, misp_event_id, misp_attribute_type, misp_attribute_value):
    misp_event = MISPEvent()
    misp_event.id = int(misp_event_id)
    misp_event.uuid = get_event_uuid(misp_client, misp_event_id)
    misp_attribute = MISPAttribute()
    misp_attribute.type = misp_attribute_type
    misp_attribute.value = misp_attribute_value
    return misp_client.add_attribute(misp_event, misp_attribute)

def create_misp_sighting(misp_client, my_misp_sighting):
    misp_sighting = MISPSighting()
    misp_sighting.value = my_misp_sighting
    misp_sighting.timestamp = int(time())
    misp_sighting.source = "IBM QRadar SOAR"
    return misp_client.add_sighting(misp_sighting)

def search_misp_attribute(misp_client, search_attribute):
    # search_results = misp_client.search(value=search_attribute)
    body = {
        "returnFormat": "json",
        "value": search_attribute
    }
    search_results = misp_client.direct_call("attributes/restSearch", body)
    if not isinstance(search_results, list):
        raise IntegrationError(f"Received an unexpected response type from the MISP API. Expected a list but received: {type(search_results)}")
    return {
        "search_status": True if len(search_results) > 0 else False,
        "search_results" : search_results
    }

def get_event_tags(event):
    search_tags = []
    if "Tag" in event.get("Event"):
        tags = event.get("Event").get("Tag")
        for tag in tags:
            log.info(f"found tag {tag.get('name')}")
            search_tags.append(tag.get("name"))
    return search_tags

def get_attribute_tags(attribute):
    search_tags = []
    if "Tag" in attribute:
        for tag in attribute.get("Tag"):
            log.info(f"found tag {tag.get('name')}")
            search_tags.append(tag.get("name"))
    return search_tags

def get_misp_attribute_tags(misp_client, search_results):
    search_tags = []
    log.debug(dumps(search_results, indent=4))
    for event in search_results:
        # Grab Event Tags
        search_tags += get_event_tags(event)
        # Grab Attribute Tags
        for attribute in event.get("Event").get("Attribute"):
            search_tags += get_attribute_tags(attribute)
    search_tags = list(set(search_tags))
    return search_tags

def get_misp_sighting_list(misp_client, misp_event_id):
    misp_event = MISPEvent()
    misp_event.id = int(misp_event_id)
    return misp_client.sightings(misp_event)

def get_event_uuid(misp_client, misp_event_id):
    # returns list with a single element: an event dict
    result = misp_client.search(eventid=misp_event_id)
    for event in result:
        event_uuid = event.get('Event').get('uuid')
    return event_uuid

def get_attribute_uuid(misp_client, misp_attribute_value, misp_event_id):
    event_response = misp_client.get_event(int(misp_event_id))
    attribute_uuid = None
    attributes = event_response.get('Event').get('Attribute')
    if not attributes:
        log.error(f"Could not get a uuid for event = {misp_event_id} and attribute = {misp_attribute_value}. Does it exist?")
        raise IntegrationError(f"Failed to find any attributes on event {misp_event_id}")

    else:
        for attribute in attributes:
            if attribute['value'] == misp_attribute_value:
                attribute_uuid = attribute.get('uuid')
        if attribute_uuid:
            return attribute_uuid
        else:
            raise IntegrationError(f"Failed to match attribute value = {misp_attribute_value} for any attributes associated with event = {misp_event_id}")

def create_tag(misp_client, misp_attribute_value, misp_tag_type, misp_tag_name, misp_event_id):
    if misp_tag_type == "Event":
        object_uuid = get_event_uuid(misp_client, misp_event_id)
    elif misp_tag_type == "Attribute":
        object_uuid = get_attribute_uuid(misp_client, misp_attribute_value, misp_event_id)
    return misp_client.tag(object_uuid, misp_tag_name)
