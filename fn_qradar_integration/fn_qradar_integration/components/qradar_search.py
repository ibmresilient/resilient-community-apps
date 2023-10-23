# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from logging import getLogger
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields
from fn_qradar_integration.util.qradar_utils import QRadarClient, QRadarServers
from fn_qradar_integration.util import function_utils
from fn_qradar_integration.lib.configure_tab import init_qradar_siem_tab
LOG = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_search"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        init_qradar_siem_tab()
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.servers_list = function_utils.get_servers_list(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.servers_list = function_utils.get_servers_list(opts)

    @function("qradar_search")
    def _qradar_search_function(self, event, *args, **kwargs):
        """Function: Search QRadar"""
        try:
            # Get the wf_instance_id of the workflow this Function was called in, if not found return a backup string
            wf_instance_id = event.message.get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")
            yield StatusMessage(f"Starting 'qradar_search' that was running in workflow '{wf_instance_id}'")

            validate_fields(["qradar_query", "qradar_query_all_results"], kwargs)
            # Get the function parameters:
            qradar_query = self.get_textarea_param(kwargs.get("qradar_query"))  # textarea
            qradar_search_param1 = kwargs.get("qradar_search_param1")  # text
            qradar_search_param2 = kwargs.get("qradar_search_param2")  # text
            qradar_search_param3 = kwargs.get("qradar_search_param3")  # text
            qradar_search_param4 = kwargs.get("qradar_search_param4")  # text
            qradar_search_param5 = kwargs.get("qradar_search_param5")  # text
            qradar_query_range_start = kwargs.get("qradar_query_range_start")  # number
            qradar_query_range_end = kwargs.get("qradar_query_range_end")  # number
            qradar_label = kwargs.get("qradar_label")  # text

            qradar_query_all_results = False
            if "Yes" in self.get_select_param(kwargs.get("qradar_query_all_results")):
                qradar_query_all_results = True

            LOG.info(f"qradar_query: {qradar_query}")
            LOG.info(f"qradar_search_param1: {qradar_search_param1}")
            LOG.info(f"qradar_search_param2: {qradar_search_param2}")
            LOG.info(f"qradar_search_param3: {qradar_search_param3}")
            LOG.info(f"qradar_search_param4: {qradar_search_param4}")
            LOG.info(f"qradar_search_param5: {qradar_search_param5}")
            LOG.info(f"qradar_query_range_start: {qradar_query_range_start}")
            LOG.info(f"qradar_query_range_end: {qradar_query_range_end}")
            LOG.info(f"qradar_query_all_results: {qradar_query_all_results}")
            LOG.info(f"qradar_label: {qradar_label}")

            options = QRadarServers.qradar_label_test(qradar_label, self.servers_list)
            qradar_verify_cert = False if options.get("verify_cert", "false").lower() == "false" else options.get("verify_cert")

            timeout = None
            try:
                if "search_timeout" in options:
                    timeout = float(options.get("search_timeout"))
            except Exception:
                LOG.debug(f"Failed to read search_timeout: {options.get('search_timeout')}")

            LOG.debug("Connection to {} using {}".format(options.get("host"),
                                                         options.get("username") or "service token"))

            query_string = function_utils.make_query_string(qradar_query,
                                                            [qradar_search_param1,
                                                             qradar_search_param2,
                                                             qradar_search_param3,
                                                             qradar_search_param4,
                                                             qradar_search_param5])

            LOG.info(f"Running query: {query_string}")

            qradar_client = QRadarClient(host=options.get("host"),
                                         username=options.get("username", None),
                                         password=options.get("qradarpassword", None),
                                         token=options.get("qradartoken", None),
                                         cafile=qradar_verify_cert,
                                         opts=self.opts, function_opts=options)

            results = qradar_client.ariel_search(query_string,
                                                 qradar_query_all_results,
                                                 range_start=qradar_query_range_start,
                                                 range_end=qradar_query_range_end,
                                                 timeout=timeout)

            results["inputs"] = {"qradar_query": qradar_query, "qradar_query_all_results": qradar_query_all_results, "qradar_search_param1": qradar_search_param1, "qradar_search_param2": qradar_search_param2, "qradar_search_param3": qradar_search_param3, "qradar_search_param4": qradar_search_param4, "qradar_search_param5": qradar_search_param5, "qradar_label": qradar_label}

            yield StatusMessage(f"Finished 'qradar_search' that was running in workflow '{wf_instance_id}'")

            yield FunctionResult(results)
        except Exception as e:
            LOG.error(str(e))
            yield FunctionError()
