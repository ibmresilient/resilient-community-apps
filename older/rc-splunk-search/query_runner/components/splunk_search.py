"""Action Module circuits component to update incidents from Splunk searches"""
import logging
from datetime import datetime, timedelta
import calendar
import time
from string import Template
from pkg_resources import Requirement, resource_filename
import json
import resilient_circuits.template_functions as template_functions
from query_runner.lib.query_action import QueryRunner
from query_runner.lib.splunk_client import SplunkClient
from query_runner.lib.misc import SearchTimeout, SearchFailure

try:
    basestring
except NameError:
    basestring = str

LOG = logging.getLogger(__name__)
CONFIG_DATA_SECTION = 'splunk'

def config_section_data():
    """sample config data for use in app.config"""
    section_config_fn = resource_filename(Requirement("rc-splunk-search"), "query_runner/data/app.config.splunk")
    query_dir = resource_filename(Requirement.parse("rc-splunk-search"), "query_runner/data/queries_splunk")

    with open(section_config_fn, 'r') as section_config_file:
        section_config = Template(section_config_file.read())
        return section_config.safe_substitute(directory=query_dir)

class SplunkQueryRunner(QueryRunner):
    """ Acknowledges and fires off new query requests """

    def __init__(self, opts):
        query_options = opts.get(CONFIG_DATA_SECTION, {})

        jinja_filters = template_functions.JINJA_FILTERS
        jinja_filters["datetime"] = self._datetime_filter
        jinja_filters["ms"] = self._ms_filter
        jinja_filters["mstz"] = self._mstz_filter
        template_functions.ENV.filters.update(jinja_filters)
        super(SplunkQueryRunner, self).__init__(opts, query_options, run_search)

    def _datetime_filter(self, val):
        """ JINJA filter to convert ms to mm/dd/YYYY:H:M:S """
        # http://docs.splunk.com/Documentation/Splunk/6.5.0/Search/Specifytimemodifiersinyoursearch
        dt = datetime.fromtimestamp(val/1000.0)
        return dt.strftime("%m/%d/%Y:%H:%M:%S")

    def _mstz_filter(self, val):
        """ JINJA filter to convert YYYY-MM-DDTHH:MM:SS.mmm+00:00 to ms """
        if not val:
            return val
        try:
            if len(val) != 29:
                raise ValueError("Invalid timestamp length %s" % val)
            ts, tz_sign, tz_hr, tz_min = val[:23], val[23:24], val[24:26], val[27:]
            ts_format = "%Y-%m-%dT%H:%M:%S.%f"
            dt = datetime.strptime(ts, ts_format)
            tz_hr = int(tz_hr)
            tz_min = int(tz_min)
            if tz_sign == '-':
                tz_hr = -1 * tz_hr
                tz_min = -1 * tz_min
            dt = dt + timedelta(hours=tz_hr, minutes=tz_min)
            return calendar.timegm(dt.timetuple()) * 1000
        except Exception, e:
            LOG.exception("%s Not in expected timestamp format YYYY-MM-DDTHH:MM:SS.mmm+00:00", val)
            return None

    def _ms_filter(self, val):
        """ JINJA filter to convert YYYY-MM-DD HH:MM:SS.mmm to ms """
        if not val:
            return val
        try:
            ts_format = "%Y-%m-%d %H:%M:%S.%f"
            result = int(time.mktime(time.strptime(val, ts_format))) * 1000
            return result
        except Exception, e:
            LOG.exception("%s Not in expected timestamp format YYYY-MM-DD HH:MM:SS.mmm", val)
            return None


#############################
# Functions for running Query
#############################
def _wait_for_query_to_complete(job, splunk_client, timeout, polling_interval):
    """ Poll Splunk until search execution finishes """
    start_time = time.time()
    finished = False

    while not finished:
        if not job.is_ready():
            pass
        else:
            finished = splunk_client.search_complete(job)

            stats = {"name": job.name,
                     "isDone": job.isDone,
                     "scanCount": int(job["scanCount"]),
                     "eventCount": int(job["eventCount"]),
                     "doneProgress": float(job["doneProgress"])*100,
                     "resultCount": int(job["resultCount"])}

            status = ("\r%(doneProgress)03.1f%%   %(scanCount)d scanned   "
                      "%(eventCount)d matched   %(resultCount)d results") % stats

            LOG.debug(status)
        if not finished:
            if timeout != 0:
                if time.time() - start_time > timeout:
                    splunk_client.cancel_search(job)
                    raise SearchTimeout(job.name, job["dispatchState"])
            time.sleep(polling_interval)

    if job["dispatchState"] != "DONE" or job["isFailed"] == True:
        raise SearchFailure(job.name, job["dispatchState"]+ u", " + unicode(job["messages"]))
# end _wait_for_query_to_complete


def _get_query_results(job, splunk_client, limit):
    """ Get results from a complete Splunk query """
    # Get the results and display them
    response = splunk_client.get_results(job, limit)

    # Replace "null" with ""
    if response:
        response = remove_nulls(response)
    return response
# end _get_query_results


def remove_nulls(d):
    """ recursively replace 'null' with '' in dictionary """
    if isinstance(d, basestring):
        if d in (u"null", u"NULL"):
            return u""
        else:
            return d

    new = {}
    for k, v in d.items():
        if isinstance(v, dict):
            v = remove_nulls(v)
        elif isinstance(v, list):
            v = [remove_nulls(v1) for v1 in v]
        elif isinstance(v, basestring) and v in (u"null", u"NULL"):
            v = u""
        new[k] = v
    return new


def run_search(options, query_definition, event_message):
    """ run Splunk query and get results """
    splunk_host = options.get("host", "")
    splunk_port = options.get("port", "")
    splunk_ui_port = int(options.get("ui_port", 8000))
    splunk_user = options.get("user", "")
    splunk_pass = options.get("password", "")
    job_ttl = options.get("job_ttl")
    timeout = int(options.get("query_timeout", 600))
    polling_interval = int(options.get("polling_interval", 5))
    result_link_prefix = "http://%s:%d/app/search/search?sid=" % (splunk_host, splunk_ui_port)

    if not all((splunk_host, splunk_port,
                splunk_user, splunk_pass,
                polling_interval)):
        LOG.error("Configuration file missing required values!")
        raise Exception("Missing Configuration Values")

    client = SplunkClient(splunk_host, splunk_port,
                          splunk_user, splunk_pass)

    kwargs = {}
    limit = 0
    if query_definition.limit:
        kwargs["max_results"] = query_definition.limit
        limit = query_definition.limit
    if job_ttl:
        kwargs["job_ttl"] = job_ttl
    job = client.search(query_definition.query, **kwargs)

    if not job:
        return "Search Failed"

    LOG.info("Queued Search %s", job.name)

    _wait_for_query_to_complete(job, client, timeout, polling_interval)

    # Query Execution Finished, Get Results
    response = _get_query_results(job, client, limit)
    if not response:
        LOG.warn("No data returned from query")
        return "Query returned no data"

    LOG.info("Query finished")
    response["metadata"] = {"job": job.name,
                            "result_url": result_link_prefix + job.name}
    LOG.debug("QUERY RESULT: %s", json.dumps(response, indent=2))
    return response
