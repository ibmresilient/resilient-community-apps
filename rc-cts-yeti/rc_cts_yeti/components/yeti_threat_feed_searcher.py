#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
import traceback

import resilient_circuits.template_functions as template_functions
from circuits import BaseComponent, handler
from jinja2 import FileSystemLoader, Environment
from rc_cts import searcher_channel
from rc_cts.components.threat_webservice import ThreatServiceLookupEvent

import pyeti

LOG = logging.getLogger(__name__)

CONFIG_SECTION = "yeti"


def config_section_data():

    config_result = """
[yeti]
urlbase=http://9.70.194.30:5000/api
username=yeti
password=
api_key=e9ebc8358de715ccf8a060d313408d65f840a6cd981433f3aadd83ba2015d24ca522c0d473222a98
# Directory to load jinja templates from
template_dir=/usr/local/lib/python2.7/site-packages/rc_cts_yeti/data/jinja

    """
    return config_result


class YetiThreatFeedSearcher(BaseComponent):
    """
       YETI custom threat searcher component

       Test using 'curl':
           curl -v -X OPTIONS 'http://127.0.0.1:9000/cts/yeti_threat_service'
           curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"email.header",
           "value":"test@example.com"}' 'http://127.0.0.1:9000/cts/yeti_threat_service'
           curl -v -k --header "Content-Type: application/json" --data-binary '{"type":"email.header.to",
           "value":"safe@email2.com"}' 'http://127.0.0.1:9000/cts/yeti_threat_service'

    """
    channel = searcher_channel("yeti_threat_service")

    def __init__(self, opts):
        super(YetiThreatFeedSearcher, self).__init__(opts)

        self.options = opts.get(CONFIG_SECTION)
        url = self.options.get("urlbase")
        username = self.options.get("username")
        password = self.options.get("password")
        api_key = self.options.get("api_key")

        self.yeti_client = pyeti.YetiApi(url, (username, password), api_key)

        # init jinja
        # get the installed template folder
        # check if the config has an override set
        template_dir = self.options.get("template_dir")
        if not template_dir:
            raise Exception('template_dir config setting is required')
        LOG.info('Using template directory:' + template_dir)
        self.jinja_env = Environment(loader=FileSystemLoader(template_dir),
                                     extensions=['jinja2.ext.do'])
        self.jinja_env.filters.update(template_functions.JINJA_FILTERS)

    @handler()
    def lookup_artifact(self, event, *args, **kwargs):
        """
        Use YETI to search for artifact value

        """

        if not isinstance(event, ThreatServiceLookupEvent):
            return

        LOG.info("Querying YETI")

        artifact = event.artifact
        artifact_value = artifact['value']
        LOG.info(artifact)
        LOG.info("Looking up ({art_type}): {art_value}"
                 .format(art_type=artifact['type'], art_value=artifact_value))

        try:
            # init new indicators object
            indicators = self.yeti_client.observable_search(regex=False,
                                                            value=artifact_value)
            LOG.debug(indicators)
        except ValueError as e:
            LOG.error(traceback.format_exc())
            raise e

        if not indicators or len(indicators) < 1:
            return []

        my_template = self.jinja_env.get_template('yeti_indicator.json.jinja')
        indicator_result = my_template.render(artifact=artifact,
                                              indicator_list=indicators,
                                              yeti_client=self.yeti_client)
        LOG.debug(indicator_result)
        try:
            return json.loads(indicator_result)
        except Exception as e:
            LOG.error(traceback.format_exc())
            raise e
