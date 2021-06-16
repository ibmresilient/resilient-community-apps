# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
import sys
if sys.version_info[0] >= 3:
    from json.decoder import JSONDecodeError as ValueError

from resilient import SimpleHTTPException
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields

PACKAGE_NAME = "fn_incident_utils"
FN_NAME = "search_incidents"

INCIDENT_QUERY_PAGED = "/incidents/query_paged"
QUERY_PAGED_RETURN_LEVEL = "?return_level="

LOG = logging.getLogger(__name__)
class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'search_incidents''"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.fn_options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.fn_options = opts.get(PACKAGE_NAME, {})

    @function(FN_NAME)
    def _search_incidents_function(self, event, *args, **kwargs):
        """Function: Search for incidents based on filter criteria. Sorting field are optional"""
        try:
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting '{0}' running in workflow '{1}'".format(FN_NAME, wf_instance_id))

            fn_inputs = validate_fields(
                [],
                kwargs
            )

            LOG.info("'{0}' inputs: %s", fn_inputs)

            filter_conditions, reason = convert_json('inc_filter_conditions', fn_inputs['inc_filter_conditions'], default=[])
            if reason:
                yield FunctionResult(rp.done(False, None, reason=reason))
                return

            sort_fields, reason = convert_json('inc_sort_fields', fn_inputs['inc_sort_fields'], default=[])
            if reason:
                yield FunctionResult(rp.done(False, None, reason=reason))
                return

            # build the filter json structure
            filter = {
                "filters": [
                    {
                        "conditions": filter_conditions
                    }
                ],
                "sorts": sort_fields
            }

            # Run the search and return the results
            yield StatusMessage("Searching...")
            try:
                url = "{}{}{}".format(INCIDENT_QUERY_PAGED, QUERY_PAGED_RETURN_LEVEL,
                                      self.fn_options.get("search_result_level", "normal"))
                search_results = self.rest_client().post(url, filter)
                reason = None
            except SimpleHTTPException as err:
                search_results = None
                reason = "Check input fields: {}".format(str(err))
                LOG.error(reason)

            yield StatusMessage("Finished '{0}' that was running in workflow '{1}'".format(FN_NAME, wf_instance_id))

            results = rp.done(True if not reason else False, search_results, reason=reason)

            LOG.info("'%s' complete", FN_NAME)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)


def convert_json(field_name, value, default=None):
    """[convert string encoded json to a dictionary]

    Args:
        field_name ([str]): [field name for logging purposes]
        value ([string]): [string encoded json]
        default ([various], optional): [if value is None, return this value]. Defaults to None.

    Returns:
        [dict, string]: return json result and reason string if error
    """
    if not value:
        return default, None

    try:
        result = json.loads(value)
        return result, None
    except ValueError as jerr:
        reason = u"Failure parsing json content in '{}': {}\n{}".format(field_name, value, str(jerr))
        LOG.error(reason)
        return None, reason
