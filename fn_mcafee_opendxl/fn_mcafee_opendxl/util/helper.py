# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

import logging
import json
from dxlclient.client import DxlClient
from dxlclient import EventCallback
from dxlclient.client_config import DxlClientConfig
from jinja2 import Template

log = logging.getLogger(__name__)


def verify_config(opts):
    config_opts = opts.get("fn_mcafee_opendxl")
    if config_opts is None:
        log.error("There is no [fn_mcafee_opendxl] section in the config file,"
                  "please set that by running resilient-circuits config -u")
        raise ValueError("[fn_mcafee_opendxl] section is not set in the config file")

    config_client = config_opts.get("dxlclient_config")
    topic_name = config_opts.get("topic_name")
    topic_listener_on = config_opts.get("topic_listener_on")
    incident_template = config_opts.get("incident_template")
    incident_mapping = config_opts.get("incident_template_mapping")

    if config_client is None:
        log.error("dxlclient_config is not set. You must set this path to run this service")
        raise ValueError("dxlclient_config is not set. You must set this path to run this service")

    if topic_name is None:
        log.error("topic_name is not set. You must set this value to run this service")
        raise ValueError("topic_name is not set. You must set this value to run this service")

    if topic_listener_on is None:
        log.error("topic_listener_on is not set. You must set this value to run this service")
        raise ValueError("topic_listener_on is not set. You must set this value to run this service")

    if incident_template is None:
        log.error("incident_template is not set. You must set this path to run this service")
        raise ValueError("incident_template is not set. You must set this path to run this service")

    if incident_mapping is None:
        log.error("incident_mapping is not set. You must set this path to run this service")
        raise ValueError("incident_mapping is not set. You must set this path to run this service")

    config = {
        "config_client": config_client,
        "topic_name": topic_name,
        "topic_listener_on": topic_listener_on,
        "incident_template": incident_template,
        "incident_mapping": incident_mapping
    }

    return config


def _create_incident(resilient_client, payload):
    uri = "/incidents"
    payload_dict = json.loads(payload)
    log.info("Creating incident with payload: {}".format(json.dumps(payload_dict)))
    log.debug("Payload: {}".format(payload))

    response = resilient_client.post(uri=uri, payload=payload_dict)
    log.info("Created incident {}".format(str(response.get("id"))))


def _add_artifact(resilient_client, inc_id):
    uri = "/incidents/{}/artifacts".format(inc_id)
    payload = {}
    resilient_client.post(uri=uri, payload=payload)


def _map_values(template_file, mapping_template_file, message):

    with open(template_file, 'r') as template, open(mapping_template_file, 'r') as map_temp:
        f = map_temp.read()
        mapping_template = Template(f)
        message_dict = json.loads(message)
        mapping_template = mapping_template.render(message_dict)

        incident_template = Template(template.read())
        mapping_dict = json.loads(mapping_template)
        incident_template = incident_template.render(mapping_dict)

        return incident_template


def event_subscriber(res_client, config):
    config_client_file = config.get("config_client")
    dxl_config = DxlClientConfig.create_dxl_config_from_file(config_client_file)

    # Create the client
    with DxlClient(dxl_config) as client:

        # Connect to the fabric
        client.connect()

        #
        # Register the Event
        #
        EVENT_TOPIC = config.get("topic_name")
        template = config.get("incident_template")
        mapping_dict = config.get("incident_mapping")

        class ResilientEventSubscriber(EventCallback):
            def on_event(self, event):
                message = event.payload.decode(encoding="UTF-8")
                log.info("Event received payload: " + message)

                # Map values from topic to incident template to create new incident
                inc_temp = _map_values(template, mapping_dict, message)

                # Create new Incident in Resilient
                _create_incident(res_client, inc_temp)

        client.add_event_callback(EVENT_TOPIC, ResilientEventSubscriber)

        log.info("Resilient DXL Listener running...")

        # Wait forever
        while True:
            continue
