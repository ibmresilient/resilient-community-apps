# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
""" SOAR functions component to run a Symantec SEPM query - get groups. """

# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST query against a SYMANTEC SEPM server.
from fn_sep.lib.sep_client import Sepclient, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError
from fn_sep.lib.helpers import transform_kwargs

FN_NAME = "fn_sep_get_groups"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_sep_get_groups' of package fn_sep.
    The function can be used to query to get information on groups.

    The Function takes the following parameter:
        sep_domain, sep_fullpathname, sep_mode, sep_order, sep_pageindex, sep_pagesize, sep_sort.

    The function will execute a REST api get request against a SYMANTEC SEPM server for information on group and
    returns a result in JSON format.
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Gets a group list."""
        try:
            params = transform_kwargs(fn_inputs._asdict()) if fn_inputs._asdict() else {}

            # Get the function parameters:
            sep_domain = getattr(fn_inputs, "sep_domain", None)  # text
            sep_fullpathname = getattr(fn_inputs, "sep_fullpathname", None)  # text
            sep_mode = getattr(fn_inputs, "sep_mode", None)  # text
            sep_order = getattr(fn_inputs, "sep_order", None)  # text
            sep_pageindex = getattr(fn_inputs, "sep_pageindex", None)  # number
            sep_pagesize = getattr(fn_inputs, "sep_pagesize", None)  # number
            sep_sort = getattr(fn_inputs, "sep_sort", None)  # text

            self.LOG.info("sep_domain: %s", sep_domain)
            self.LOG.info("sep_fullpathname: %s", sep_fullpathname)
            self.LOG.info("sep_mode: %s", sep_mode)
            self.LOG.info("sep_order: %s", sep_order)
            self.LOG.info("sep_pageindex: %s", sep_pageindex)
            self.LOG.info("sep_pagesize: %s", sep_pagesize)
            self.LOG.info("sep_sort: %s", sep_sort)

            yield self.status_message("Running Symantec SEP Get Groups query...")

            sep = Sepclient(self.options)

            results = sep.get_paginated_results(sep.get_groups, **params)

            yield self.status_message("Returning 'Symantec SEP Get Groups' results")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            self.LOG.exception("Exception in SOAR function for Symantec SEP.")
            yield FunctionError()
