# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
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

    @function("exchange_move_folder_contents_and_delete_folder")
    def _exchange_move_folder_contents_and_delete_folder_function(self, event, *args, **kwargs):
        """Function: """
        try:
            # Get the function parameters:
            exchange_email = kwargs.get("exchange_email")  # text
            exchange_delete_if_no_subfolders = kwargs.get("exchange_delete_if_no_subfolders") # boolean
            exchange_folder_path = kwargs.get("exchange_folder_path")  # text
            exchange_destination_folder_path = kwargs.get("exchange_destination_folder_path")  # text

            log = logging.getLogger(__name__)
            # Use default connection email if one was not specified
            if exchange_email is None:
                exchange_email = self.options.get('email')
                log.info('No connection email was specified, using value from config file')
            log.info("exchange_delete_emails_if_no_subfolders: %s" % exchange_delete_if_no_subfolders)
            log.info("exchange_email: %s" % exchange_email)
            log.info("exchange_folder_path: %s" % exchange_folder_path)
            log.info("exchange_destination_folder_path: %s" % exchange_destination_folder_path)

            # Initialize utils
            utils = exchange_utils(self.options)

            # Get folders
            from_folder = utils.go_to_folder(exchange_email, exchange_folder_path)
            to_folder = utils.go_to_folder(exchange_email, exchange_destination_folder_path)

            if exchange_delete_if_no_subfolders:
                if from_folder.child_folder_count != 0:
                    raise FunctionError('%s has subfolders' % exchange_folder_path)
                else:
                    queryset = from_folder.all()
            else:
                queryset = utils.get_emails(exchange_email, folder_path=exchange_folder_path, search_subfolders=True)

            # Get items before moving
            yield StatusMessage("Getting items")
            results = utils.create_email_function_results(queryset)

            # Move items
            yield StatusMessage("Moving items")
            item_count = queryset.count()
            for item in queryset:
                item.move(to_folder)

            # Delete folder
            yield StatusMessage("Deleting folder %s" % exchange_folder_path)
            from_folder.delete()
            yield StatusMessage("%s deleted, %d items moved" % (exchange_folder_path, item_count))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()