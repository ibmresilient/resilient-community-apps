from time import time
from json import dumps
from logging import getLogger
from pymisp import PyMISP
from resilient_lib import IntegrationError

log = getLogger(__name__)


def get_misp_client(URL, API_KEY, VERIFY_CERT, proxies):
    return PyMISP(URL, API_KEY, VERIFY_CERT, 'json', proxies=proxies)


def create_misp_event(misp_client, misp_distribution, misp_threat_level, misp_analysis_level, misp_event_name):
    return misp_client.new_event(misp_distribution, misp_threat_level, misp_analysis_level, misp_event_name)


def create_misp_attribute(misp_client, misp_event_id, misp_attribute_type, misp_attribute_value):
    return misp_client.add_named_attribute(misp_event_id, misp_attribute_type, misp_attribute_value)


def create_misp_sighting(misp_client, misp_sighting):
    sighting_json = {
        "values": [f"{misp_sighting}"],
        "timestamp": int(time())
    }
    return misp_client.set_sightings(sighting_json)


def search_misp_attribute(misp_client, search_attribute):
    search_results = misp_client.search('attributes', values=search_attribute)
    log.debug(dumps(search_results, indent=4))
    if not isinstance(search_results.get('response', {}).get('Attribute'), list):
        raise IntegrationError("Received an unexpected response type from the MISP API. "
                               "Expected a dictionary containing a list of attributes, but received: {}".format(type(search_results.get('response', {}).get('Attribute'))))
    search_results_len = len(search_results.get(
        'response', {}).get('Attribute'))
    return {
        "search_status": True if search_results_len > 0 else False,
        "search_results": search_results.get('response', {}).get('Attribute')
    }


def get_event_list(misp_client, attribute):
    return [event_id.get('event_id') for event_id in attribute]


def get_event_tags(misp_client, misp_event_id):
    misp_tags = []
    event_results_long = misp_client.get_event(misp_event_id)
    event_results = event_results_long.get('Event')
    log.debug(dumps(event_results, indent=4))
    if 'Tag' in event_results.keys():
        for event_tag in event_results.get('Tag'):
            log.debug(event_tag)
            misp_tags.append(event_tag)
    else:
        log.debug("No Tag Found for Event Result")
    return misp_tags


def get_attribute_tags(attribute_result):
    misp_tags = []
    if 'Tag' in attribute_result.keys():
        for attribute_tag in attribute_result.get('Tag'):
            log.debug(attribute_tag)
            misp_tags.append(attribute_tag)
    else:
        log.debug("No Tag Found for Attribute Result")
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
        misp_tag_names.append(misp_tag.get('name'))
    misp_tag_names = list(set(misp_tag_names))

    return misp_tag_names


def get_misp_sighting_list(misp_client, event_id):
    return misp_client.sighting_list(event_id, 'event')
