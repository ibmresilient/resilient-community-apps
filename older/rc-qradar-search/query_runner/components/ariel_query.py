"""Action Module circuits component to update incidents from QRadar Ariel queries"""
import logging
from datetime import datetime
import time
import copy
import json
from string import Template
from pkg_resources import Requirement, resource_filename
import resilient_circuits.template_functions as template_functions
from query_runner.lib.query_action import QueryRunner
from query_runner.lib.qradar_rest_client import QRadarClient
from query_runner.lib.misc import SearchTimeout, SearchFailure

try:
    basestring
except NameError:
    basestring = str

LOG = logging.getLogger(__name__)
CONFIG_DATA_SECTION = 'ariel'


def config_section_data():
    """sample config data for use in app.config"""
    section_config_fn = resource_filename(Requirement("rc-qradar-search"), "query_runner/data/app.config.qradar")
    query_dir = resource_filename(Requirement("rc-qradar-search"), "query_runner/data/queries_ariel")

    with open(section_config_fn, 'r') as section_config_file:
        section_config = Template(section_config_file.read())
        return section_config.safe_substitute(directory=query_dir)


class AQLIncidentUpdate(QueryRunner):
    """ Acknowledges and fires off new query requests """

    def __init__(self, opts):
        query_options = opts.get(CONFIG_DATA_SECTION, {})

        jinja_filters = template_functions.JINJA_FILTERS
        jinja_filters["datetime"] = self._datetime_filter
        template_functions.ENV.filters.update(jinja_filters)
        super(AQLIncidentUpdate, self).__init__(opts, query_options, run_search)

    def _datetime_filter(self, val):
        """ JINJA filter to convert ms to YYYY-MM-DD HH:mm:ss """
        dt = datetime.fromtimestamp(val/1000.0)
        return dt.strftime("%Y-%m-%d %H:%M:%S")


#############################
# Functions for running Query
#############################
def _wait_for_query_to_complete(search_id, qradar_client, timeout, polling_interval):
    """ Poll QRadar until search execution finishes """
    start_time = time.time()
    search_status = qradar_client.get_search_status(search_id)
    if not search_status:
        # Sometimes it takes a little while to be able to query a search id
        time.sleep(4)
        search_status = qradar_client.get_search_status(search_id)
    while search_status.get("status", "") in ("WAIT", "EXECUTE", "SORTING"):
        if timeout != 0:
            if time.time() - start_time > timeout:
                raise SearchTimeout(search_id, search_status.get("status", ""))
        time.sleep(polling_interval)
        search_status = qradar_client.get_search_status(search_id)

    if search_status.get("status", "") != "COMPLETED":
        LOG.error(search_status)
        raise SearchFailure(search_id, search_status.get("status", ""))
# end _wait_for_query_to_complete


def _get_query_results(search_id, qradar_client, item_range):
    """ Get results from a complete QRadar query """
    if item_range:
        headers = {"Range": item_range}
    else:
        headers = None

    url = "ariel/searches/{0}/results".format(search_id, headers=headers)
    response = qradar_client.get(url)
    LOG.debug(response)
    # Replace "NULL" with ""
    response = remove_nulls(response)
    return response
# end _get_query_results


def remove_nulls(d):
    """ recursively replace 'NULL' with '' in dictionary """
    if isinstance(d, basestring):
        if d == u'NULL':
            return u''
        else:
            return d

    new = {}
    LOG.debug("d={d} ".format(d=d))
    LOG.debug("type of d is {t}".format(t=type(d)))

    for k, v in d.items():
        if isinstance(v, dict):
            v = remove_nulls(v)
        elif isinstance(v, list):
            v = [remove_nulls(v1) for v1 in v]
        elif isinstance(v, basestring) and v == u'NULL':
            v = u''

        new[k] = v

    LOG.info("Returning: {n}".format(n=new))

    return new


def run_search(options, query_definition, event_message):
    """ Run Ariel search and return result """

    # Read the options and construct a QRadar client
    qradar_url = options.get("qradar_url", "")
    qradar_token = options.get("qradar_service_token", "")
    timeout = int(options.get("query_timeout", 600))
    polling_interval = int(options.get("polling_interval", 5))
    if not all((qradar_url, qradar_token, timeout, polling_interval)):
        LOG.error("Configuration file missing required values!")
        raise Exception("Missing Configuration Values")

    verify = options.get("qradar_verify", "")
    if verify[:1].lower() in ("0", "f", "n"):
        verify = False
    else:
        verify = True

    qradar_client = QRadarClient(qradar_url, qradar_token, verify=verify)

    error = None
    response = None
    try:
        params = {'query_expression': query_definition.query}
        url = "ariel/searches"
        response = qradar_client.post(url, params=params)
        LOG.debug(response)
        search_id = response.get('search_id', '')
        if not search_id:
            error = "Query Failed: " + response.get("message", "No Error Message Found")
        else:
            LOG.info("Queued Search %s", search_id)
            _wait_for_query_to_complete(search_id, qradar_client, timeout, polling_interval)
            # Query Execution Finished, Get Results
            response = _get_query_results(search_id, qradar_client, query_definition.range)
    except Exception as exc:
        if not query_definition.onerror:
            raise
        LOG.error(exc)
        error = u"{}".format(exc)

    if error:
        mapdata = copy.deepcopy(event_message)
        mapdata.update(query_definition.vars)
        mapdata.update({"query": query_definition.query})
        mapdata.update({"error": error})
        error_template = json.dumps({"events": [query_definition.onerror]}, indent=2)
        error_rendered = template_functions.render_json(error_template, mapdata)
        response = error_rendered

    if not response or len(response["events"]) == 0:
        LOG.warn("No data returned from query")
        if query_definition.default:
            mapdata = copy.deepcopy(event_message)
            mapdata.update(query_definition.vars)
            mapdata.update({"query": query_definition.query})
            default_template = json.dumps({"events": [query_definition.default]}, indent=2)
            default_rendered = template_functions.render_json(default_template, mapdata)
            response = default_rendered

    return response
# end run_search
