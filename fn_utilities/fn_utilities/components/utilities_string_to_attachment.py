# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import sys
import logging
from io import BytesIO
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import write_file_attachment

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_string_to_attachment"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_utilities", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_utilities", {})

    @function("utilities_string_to_attachment")
    def _utilities_string_to_attachment_function(self, event, *args, **kwargs):
        """Function: Create a new attachment from an inputted string"""
        
        try:
            # Check required inputs are defined
            string_to_convert_to_attachment = kwargs.get('string_to_convert_to_attachment')  # text (required)
            if not string_to_convert_to_attachment:
              raise ValueError('string_to_convert_to_attachment is required')

            attachment_name = kwargs.get('attachment_name')  # text (required)
            if not attachment_name:
              raise ValueError('attachment_name is required')
            attachment_name = '{0}.txt'.format(attachment_name)  # text (required)

            incident_id = kwargs.get('incident_id')  # number (required)
            if not incident_id:
              raise ValueError('incident_id is required')

            # Optional Inputs
            task_id = kwargs.get('task_id')  # number (optional)

            # Define local variables
            content_type = 'text/plain'
            new_attachment = None

            # Initialize logging
            log = logging.getLogger(__name__)
            log.info('string_to_convert_to_attachment: %s', string_to_convert_to_attachment)
            log.info('attachment_name: %s', attachment_name)
            log.info('incident_id: %s', incident_id)
            log.info('task_id: %s', task_id)

            yield StatusMessage('Writing attachment...')

            if sys.version_info.major < 3:
                datastream = BytesIO(string_to_convert_to_attachment)
            else:
                datastream = BytesIO(string_to_convert_to_attachment.encode("utf-8"))

            #  Access Resilient API
            client = self.rest_client()

            # POST the new attachment
            new_attachment = write_file_attachment(client, attachment_name, datastream,
                                                   incident_id, task_id=task_id,
                                                   content_type=content_type)

            # If the attachment succeeded in POSTing, print message, return result
            if new_attachment is not None:
              yield StatusMessage('Attachment {0} was created'.format(new_attachment['id']))
              yield FunctionResult({'attachment_id' : new_attachment['id']})

            # Else, raise an error
            else:
              yield StatusMessage('Failed creating attachment')
              raise FunctionError(u'Failed creating attachment')
            
        except Exception:
            yield FunctionError()
