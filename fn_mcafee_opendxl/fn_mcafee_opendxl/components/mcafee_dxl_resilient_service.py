# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Service listener implementation"""

import logging
import json
from resilient_circuits import ResilientComponent
from resilient_circuits.rest_helper import get_resilient_client
from dxlclient.client import DxlClient
from dxlclient import EventCallback
from dxlclient.client_config import DxlClientConfig
try:
    from fn_mcafee_opendxl.util.helper import verify_config, get_topic_template_dict, map_values, \
        create_incident, add_methods_to_global
except ModuleNotFoundError:
    from fn_mcafee_opendxl.fn_mcafee_opendxl.util.helper import verify_config, get_topic_template_dict, \
        map_values, create_incident, add_method_to_global

log = logging.getLogger(__name__)


def get_connected_resilient_client(config):
    opts = config.get("opts")
    client = get_resilient_client(opts)
    client.connect(opts.email, opts.password)

    return client


class DxlComponentListener(ResilientComponent):

    def __init__(self, opts):
        super(DxlComponentListener, self).__init__(opts)
        self.config = verify_config(opts)
        add_methods_to_global()

        # Create and connect DXL client
        config_client_file = self.config.get("config_client")
        dxl_config = DxlClientConfig.create_dxl_config_from_file(config_client_file)
        self.client = DxlClient(dxl_config)
        self.client.connect()

        self.main()

    def main(self):
        if self.config["topic_listener_on"] == "True":
#            res_client = self.rest_client()
            log.info("Service Listener called")

            self.event_subscriber(self.config)
        else:
            log.info("Event subscriber not listening. To turn on set topic_listener_on to True")

    def event_subscriber(self, config):
#        config_client_file = config.get("config_client")
#        dxl_config = DxlClientConfig.create_dxl_config_from_file(config_client_file)

#        # Create the client
#        with DxlClient(dxl_config) as client:

#            # Connect to the fabric
#            client.connect()

            #
            # Register the Event
            #
#            EVENT_TOPIC = config.get("topic_name")
#            template = config.get("incident_template")
        try:
            mapping_dict = config.get("incident_mapping")

            topic_template_dict = get_topic_template_dict(config.get("custom_template_dir"))

            class ResilientEventSubscriber(EventCallback):

                def __init__(self, template):
                    super(ResilientEventSubscriber, self).__init__()
                    self.temp = template

                def on_event(self, event):
                    message = event.payload.decode(encoding="UTF-8")
                    log.info("Event received payload: " + message)

                    message_dict = json.loads(message)

                    # Map values from topic to incident template to create new incident
#                    inc_temp = map_values_old(self.temp, mapping_dict, message)
                    inc_data = map_values(self.temp, message_dict)

                    # Create new Incident in Resilient
                    log.info(inc_data)
                    response = create_incident(get_connected_resilient_client(config), inc_data)
                    log.info("Created incident {}".format(str(response.get("id"))))

            for event_topic, template in topic_template_dict.iteritems():
                self.client.add_event_callback(event_topic, ResilientEventSubscriber(template))
#                        client.add_event_callback(EVENT_TOPIC, ResilientEventSubscriber)
                log.info("Resilient DXL Subscriber listening on {} ...".format(event_topic))
#                        log.info("Listening on {}".format(EVENT_TOPIC))
        except Exception as e:
            log.error(e)
            self.client.destroy()

            # Wait forever
#            while True:
#                continue

