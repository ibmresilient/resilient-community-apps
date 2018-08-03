# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_exchange.util.exchange_utils import exchange_utils


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'exchange_move_and_delete_folder"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_exchange", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_exchange", {})

    @function("exchange_move_and_delete_folder")
    def _exchange_move_and_delete_folder_function(self, event, *args, **kwargs):
        """Function: """
        try:
            # Get the function parameters:
            exchange_email = kwargs.get("exchange_email")  # text
            exchange_folder_path = kwargs.get("exchange_folder_path")  # text
            exchange_destination_folder_path = kwargs.get("exchange_destination_folder_path")  # text

            log = logging.getLogger(__name__)
            # Use default connection email if one was not specified
            if exchange_email is None:
                exchange_email = self.options.get('email')
                log.info('No connection email was specified, using value from config file')
            log.info("exchange_email: %s" % exchange_email)
            log.info("exchange_folder_path: %s" % exchange_folder_path)
            log.info("exchange_destination_folder_path: %s" % exchange_destination_folder_path)

            # Initialize utils
            utils = exchange_utils(self.options)

            # Get folders
            yield StatusMessage("Getting folders")
            from_folder = utils.go_to_folder(exchange_email, exchange_folder_path)
            to_folder = utils.go_to_folder(exchange_email, exchange_destination_folder_path)
            yield StatusMessage("Done getting folders")

            results = {}
            # Get items before moving
            yield StatusMessage("Getting items")
            results = utils.create_email_function_results(from_folder.all())
            yield StatusMessage("Done getting items")

            # Move items
            yield StatusMessage("Moving items")
            for item in from_folder.all():
                item.move(to_folder)
            yield StatusMessage("Done moving items")

            # Delete folder
            yield StatusMessage("Deleting folder %s" % exchange_folder_path)
            from_folder.delete()
            yield StatusMessage("%s deleted" % exchange_folder_path)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()