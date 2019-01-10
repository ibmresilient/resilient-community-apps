"""
This module contains the FileFeedDestination for writing Resilient data
to a local directory.
"""

import os
import json
import logging
from io import open

from rc_data_feed.lib.feed import FeedDestinationBase
from rc_data_feed.lib.type_info import TypeInfo


LOG = logging.getLogger(__name__)


class FileFeedDestination(FeedDestinationBase):  # pylint: disable=too-few-public-methods
    """Feed destination for writing Resilient data to a local directory."""
    def __init__(self, rest_client, options):   # pylint: disable=unused-argument
        super(FileFeedDestination, self).__init__()

        self.dir = options.get("directory", ".")

    def send_data(self, context, payload):
        """
        Write a simplified version of the payload to a creatively named
        file in the configured 'directory'.
        """
        name = context.type_info.get_pretty_type_name()

        output_file = self._make_file_path(context, name, payload)

        LOG.debug('writing %s to %s', name, output_file)

        payload = context.type_info.flatten(payload, TypeInfo.translate_value)

        with open(output_file, 'w') as out:
            out.write(json.dumps(payload, indent=2))

    def _make_file_path(self, context, type_name, payload):
        """Makes a file name where we can write the payload"""
        inc_id = context.inc_id

        if type_name == 'incident':
            name_part = 'incident_{}.json'.format(inc_id)
        else:
            name_part = 'incident_{}_{}_{}.json'.format(inc_id, type_name, payload['id'])

        return os.path.join(self.dir, name_part)
