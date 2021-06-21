# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
import os
import threading
import resilient
from kafka import KafkaConsumer
from resilient_circuits import ResilientComponent
from resilient_lib import IntegrationError, validate_fields
from resilient import SimpleHTTPException
from fn_kafka.lib.jinja_common import JinjaEnvironment
from fn_kafka.lib.kafka_common import b_to_s, PACKAGE_NAME, get_broker_section

INCIDENT_URL = "/incidents"

CREATE_TEMPLATE = "{}_create_template.jinja"
UPDATE_TEMPLATE = "{}_update_template.jinja"

LOG = logging.getLogger(__name__)

class KafkaListener(threading.Thread):
    """[listen on app.config defined topics and create/update incidents based on user specified templates]

    Args:
        threading ([type]): [description]
    """
    def __init__(self, rest_client, section):
        super(KafkaListener, self).__init__()
        # pop the settings we'll define separately and pass the others to the constructor
        validate_fields(["topics", "bootstrap_servers"], section)

        self.rest_client = rest_client
        self.topics = [topic.strip() for topic in section.pop("topics").split(",")]
        self.template_dir = section.pop("template_dir") \
            if "template_dir" in section else None

        self.jinja_env = JinjaEnvironment()

        # setup the connection
        LOG.info("Starting Kafka listener on topics: %s", self.topics)
        self.kafka_listener = KafkaConsumer(*self.topics, **section)

    def run(self):
        """[main poller logic. consume messages]
        msg.key: optional incident id for existing incident updates
        msf.json: string encoded json of payload to create/upate an incident
        """
        for msg in self.kafka_listener:
            try:
                LOG.debug(msg)

                msg_value = msg.value
                msg_incident_id = msg.key   # this refers to an existing incident id
                msg_topic = msg.topic
                # convert to json
                msg_json = convert_msg(msg_value)
                if not msg_json:
                    LOG.error("Unable to convert kafka msg to json: %s", msg_value)
                    continue

                existing_incident = None
                if msg_incident_id:
                    msg_incident_id = b_to_s(msg_incident_id)
                    # determine if the incident is found
                    existing_incident = self.find_incident(msg_incident_id)
                    if not existing_incident:
                        LOG.error("Incident Id not found: %s. exiting", msg_incident_id)
                        continue

                if msg_incident_id:
                    jinja_template_file = os.path.join(self.template_dir, UPDATE_TEMPLATE.format(msg_topic))
                else:
                    jinja_template_file = os.path.join(self.template_dir, CREATE_TEMPLATE.format(msg_topic))

                if os.path.isfile(jinja_template_file):
                    payload = self.jinja_env.make_payload_from_template(jinja_template_file, None, \
                                                                        msg_json)
                else:
                    LOG.debug("No mapping template referenced")
                    payload = msg_json

                try:
                    self.create_update_incident(payload, existing_incident)
                except SimpleHTTPException as err:
                    LOG.error("Unable to create incident: %s", str(err))
            except Exception as err:
                LOG.error("Kafka listener error %s", str(err))

    def find_incident(self, inc_id):
        # find the incident in Resilient
        try:
            url = "/".join([INCIDENT_URL, str(inc_id)])
            incident = self.rest_client.get(url)
            return incident
        except SimpleHTTPException:
            return None

    def create_update_incident(self, payload, existing_incident):
        """[create or update the incident]

        Args:
            payload ([dict]): [payload of fields to create/update]
            existing_incident ([dict]): existing incident fields, or None for create operation
        :return: incident created or updated
        """
        LOG.debug(payload)
        if existing_incident:
            # patch the incident
            incident = self.update_incident(payload, existing_incident)
            LOG.info("Updated incident: %s", incident['id'])
        else:
            incident = self.rest_client.post(INCIDENT_URL, payload)
            LOG.info("Created incident: %s", incident['id'])

        return incident

    def update_incident(self, payload, existing_incident):
        """ update_incident will update an incident with the specified json payload.
        ;param payload: incident fields to be updated.
        existing_incident ([dict]): existing incident fields, or None for create operation
        :return: incident updated
        """
        try:
            # Update incident
            incident_url = "/".join([INCIDENT_URL, str(existing_incident['id'])])

            patch = resilient.Patch(existing_incident)

            # Iterate over payload dict.
            for name, _ in payload.items():
                if name == 'properties':
                    for field_name, field_value in payload['properties'].items():
                        patch.add_value(field_name, field_value)
                else:
                    payload_value = payload.get(name)
                    patch.add_value(name, payload_value)

            patch_result = self.rest_client.patch(incident_url, patch)
            result = self._chk_status(patch_result)
            # add back the incident id
            result['id'] = existing_incident['id']
            return result

        except Exception as err:
            raise IntegrationError(err)

    def _chk_status(self, resp, rc=200):
        """
        check the return status. If return code is not met, raise IntegrationError,
        if success, return the json payload
        :param resp:
        :param rc:
        :return:
        """
        if hasattr(resp, "status_code"):
            if isinstance(rc, list):
                if resp.status_code < rc[0] or resp.status_code > rc[1]:
                    raise IntegrationError(u"status code failure: {0}".format(resp.status_code))
            elif resp.status_code != rc:
                raise IntegrationError(u"status code failure: {0}".format(resp.status_code))

            return resp.json()

        return {}


class KafkaListenerComponent(ResilientComponent):
    """
    Event-driven polling for Sentinel Incidents
    """

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(KafkaListenerComponent, self).__init__(opts)
        self.jinja_env = JinjaEnvironment()
        self.options = opts.get(PACKAGE_NAME, {})
        self.listeners = []

        brokers = self.options.get("listener_brokers", None)
        if brokers:
            broker_list = [broker.strip() for broker in brokers.split(",")]
            self.setup_brokers(broker_list)
        else:
            LOG.info("No Kafka Listeners defined. Poller disabled")

    def setup_brokers(self, broker_list):
        # find the section information
        for broker in broker_list:
            try:
                broker_section = get_broker_section(self.opts, broker)
            except IntegrationError:
                continue

            listener = KafkaListener(self.rest_client(), broker_section)
            listener.start()
            self.listeners.append(listener)

def convert_msg(msg):
    try:
        return json.loads(msg)
    except Exception as err:
        LOG.error(str(err))
        return None
