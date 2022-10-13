# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Function implementation"""

"""
This module contains the ElasticFeedDestination for writing Resilient data
to an Elasticseach index.
"""

import base64
import copy
import logging

from ssl import create_default_context
from elasticsearch import Elasticsearch

from rc_data_feed.lib.feed import FeedDestinationBase
from rc_data_feed.lib.type_info import TypeInfo

LOG = logging.getLogger(__name__)

DEF_INDEX_SETTINGS = {
    "index": {
        "blocks": {
            "read_only_allow_delete": "false"
        }
    }
}

class ElasticFeedDestination(FeedDestinationBase):  # pylint: disable=too-few-public-methods
    """Feed destination for writing Resilient data to a local directory."""
    def __init__(self, rest_client_helper, options):   # pylint: disable=unused-argument
        super(ElasticFeedDestination, self).__init__()
        self.port = int(options.get("port", 9200))
        self.url = "{}:{}".format(options.get("url"), self.port)

        self.user = options.get("auth_user")
        self.password = options.get("auth_password")
        self.index_prefix = options.get("index_prefix")
        self.cafile = options.get("cafile")

        self.init_elastic()

    def init_elastic(self):
        basic_auth = None
        if self.user:
            basic_auth= (self.user, self.password)

        if self.url.lower().startswith('https'):
            # Attempt to create an SSL context, should work fine if no CERT is provided
            if self.cafile is None or self.cafile.lower() == 'false':
                context = create_default_context()
                # Connect to the ElasticSearch instance
                context.check_hostname = False
                self.es = Elasticsearch(self.url,
                        ssl_context=context,
                        basic_auth=basic_auth,
                        verify_certs=False)
            else:
                context = create_default_context(cafile=self.cafile)
                # Connect to the ElasticSearch instance
                self.es = Elasticsearch(self.url,
                                        ssl_context=context,
                                        basic_auth=basic_auth)
        else:
            # Connect without to Elastic without HTTPS
            self.es = Elasticsearch(self.url,
                                    basic_auth=basic_auth)


    def _create_index(self, index):
        if not self.es.indices.exists(index=index):
            results = self.es.indices.create(index=index, settings=DEF_INDEX_SETTINGS)
            LOG.debug(u"settings on {}: {}".format(index, results))


    def send_data(self, context, payload):
        """
        Write a simplified version of the payload to a creatively named
        file in the configured 'directory'.
        """
        name = context.type_info.get_pretty_type_name()

        elastic_payload = context.type_info.flatten(payload,
                                                    translate_func=translate_value_for_bytes(make_string))

        # add the incident_id and object id to all payloads, if needed
        elastic_payload['inc_id'] = context.inc_id
        if payload.get('id'):
            elastic_payload['id'] = payload['id']

        index = u"{}{}".format(self.index_prefix, name)
        # set index permissions
        self._create_index(index)

        if context.is_deleted:
            LOG.debug('deleting %s(%s) on index %s', name, payload['id'], index)
            self._fn_elasticsearch_delete(index, name, payload['id'])
        else:
            LOG.debug('indexing %s(%s) on index %s', name, payload['id'], index)
            self._fn_elasticsearch_index(index, name, payload['id'], elastic_payload)


    def _fn_elasticsearch_index(self, index, object_type, type_id, payload):
        """Function: Allows a user to index a specified payload"""

        result = self.es.index(index=index, id=type_id, document=payload)

        if result.get("result") not in ("created", "updated"):
            msg_error = u"Unable to index {}, {}, {} ({})".format(index, object_type, type_id, payload)
            raise RuntimeError(msg_error)


    def _perform_alter(self, index, object_type, type_id, alter_fields):
        fields = ("ctx._source.{0} = params.{0}".format(key for key in alter_fields.keys()))

        update_payload = {
            "script": {
                "inline": "; ".join(fields),
                "lang": "painless",
                "params": alter_fields
            }
        }

        result = self.es.update(index=index, id=type_id, doc=update_payload)


    def _fn_elasticsearch_delete(self, index, object_type, type_id):
        """Function: Allows a user to delete a specified payload"""

        result = self.es.delete(index=index, id=type_id)

        if result.get("result") not in ("deleted"):
            msg_error = u"Unable to delete {}, {}, {}".format(index, object_type, type_id)
            raise RuntimeError(msg_error)


    def filter_nulls(self, payload):
        """
        remove key values pairs where value is null, elastic cannot index these
        :param payload:
        :return: new_payload
        """
        new_payload =  dict((key, value) for key, value in payload.items() if value)
        return new_payload


def translate_value_for_bytes(bytes_func):
    """[define mappings for SOAR fields to Elastic fields]

    Args:
        blob_func ([method]): [method to run when encountering a blob field type. ie attachment content]

    Returns:
        [object]: [translated field ready for saving]
    """
    mapping = TypeInfo.get_default_mapping()
    mapping['blob'] = bytes_func

    def translate_value(type_info, field, value):
        chged_value = copy.copy(value)
        if chged_value is not None:
            input_type = field['input_type']
            if input_type in mapping:
                chged_value = mapping[input_type](type_info, field, chged_value)
            elif input_type != 'none':
                LOG.warning("Unable to find a mapping for field type: %s", input_type)

            if isinstance(chged_value, list):
                chged_value = mapping["list"](type_info, field, chged_value)

        return chged_value

    return translate_value

def make_string(type_info, field, value):
        """[convert byte array into base64 format required by the elastic]

        Args:
            value ([byte array]): [description]

        Returns:
            base64 converted format
        """

        if value:
            return base64.b64encode(value).decode('utf-8')
