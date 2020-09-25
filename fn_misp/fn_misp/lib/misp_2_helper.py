import time
import json
import logging
from pymisp import PyMISP
from resilient_lib import IntegrationError

log = logging.getLogger(__name__)

def get_misp_client(URL, API_KEY, VERIFY_CERT, proxies):
    misp_client = PyMISP(URL, API_KEY, VERIFY_CERT, 'json', proxies=proxies)
    return misp_client

def create_misp_event(misp_client, misp_distribution, misp_threat_level, misp_analysis_level, misp_event_name):
    misp_event = misp_client.new_event(misp_distribution, misp_threat_level, misp_analysis_level, misp_event_name)
    return misp_event

def create_misp_attribute(misp_client, misp_event_id, misp_attribute_type, misp_attribute_value):
    misp_attribute = misp_client.add_named_attribute(misp_event_id, misp_attribute_type, misp_attribute_value)
    return misp_attribute


def create_misp_sighting(misp_client, misp_sighting):
    sighting_json = {
                    "values":[u"{}".format(misp_sighting)], 
                    "timestamp": int(time.time())
                    }
    misp_sighting = misp_client.set_sightings(sighting_json)
    return misp_sighting


def search_misp_attribute(misp_client, search_attribute):
    search_results = misp_client.search('attributes', values=search_attribute)
    log.debug(json.dumps(search_results, indent=4))
    if not isinstance(search_results['response']['Attribute'], list):
        raise IntegrationError("Received an unexpected response type from the MISP API. "
                                "Expected a dictionary containing a list of attributes, but received: {}".format(type(search_results['response']['Attribute'])))
    search_results_len = len(search_results['response']['Attribute'])
    if search_results_len == 0:
        success_status = False
    elif search_results_len > 0:
        success_status = True
    else:
        success_status = False
    search_results_response = { 
                                "search_status": success_status,
                                "search_results" : search_results['response']['Attribute']
                            }
    return search_results_response

def get_event_list(misp_client, attribute):
    misp_event_list = []
    for event_id in attribute:
        misp_event_list.append(event_id['event_id'])
    return misp_event_list

def get_event_tags(misp_client, misp_event_id):
    misp_tags = []
    event_results_long = misp_client.get_event(misp_event_id)
    event_results = event_results_long['Event']
    log.debug(json.dumps(event_results, indent=4))
    if 'Tag' in event_results.keys():
        for event_tag in event_results['Tag']:
            log.debug(event_tag)
            misp_tags.append(event_tag)
    else:
        log.debug("No Tag Found for Event Result")
        pass
    return misp_tags

def get_attribute_tags(attribute_result):
    misp_tags = []
    if 'Tag' in attribute_result.keys():
            for attribute_tag in attribute_result['Tag']:
                log.debug(attribute_tag)
                misp_tags.append(attribute_tag)
    else:
        log.debug("No Tag Found for Attribute Result")
        pass
    return misp_tags

def get_misp_attribute_tags(misp_client, search_results):
    misp_tags = []
    misp_tag_names = []

    attribute_json = search_results
    
    # Gets attribute tags 
    for attribute_result in attribute_json:
        misp_tags += get_attribute_tags(attribute_result)

    # Get events attribute is in
    misp_event_list = get_event_list(misp_client, attribute_json)
    # Get event tags for each event attribute is in
    for misp_event_id in misp_event_list:
        misp_tags += get_event_tags(misp_client, misp_event_id)

    for misp_tag in misp_tags:
        misp_tag_names.append(misp_tag['name'])
    misp_tag_names = list(set(misp_tag_names))
    
    return misp_tag_names

def get_misp_sighting_list(misp_client, event_id):
    sighting_result = misp_client.sighting_list(event_id, 'event')
    return sighting_result