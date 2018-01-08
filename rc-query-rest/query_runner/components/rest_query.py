"""Action Module circuits component to execute simple REST API queries"""
import logging
import base64
import copy
import json
import requests
from string import Template
from pkg_resources import Requirement, resource_filename
from circuits.six import string_types as string_types
from resilient import SimpleHTTPException
import resilient_circuits.template_functions as template_functions
from query_runner.lib.query_action import QueryRunner
from query_runner.lib.misc import SearchTimeout, SearchFailure

try:
    basestring
except NameError:
    basestring = str

LOG = logging.getLogger(__name__)
CONFIG_DATA_SECTION = 'rest'


def config_section_data():
    """sample config data for use in app.config"""
    section_config_fn = resource_filename(Requirement("rc-query-rest"), "query_runner/data/app.config.rest")
    query_dir = resource_filename(Requirement("rc-query-rest"), "query_runner/data/queries_rest")

    with open(section_config_fn, 'r') as section_config_file:
        section_config = Template(section_config_file.read())
        return section_config.safe_substitute(directory=query_dir)


class QueryREST(QueryRunner):
    """ Acknowledges and fires off new query requests """

    def __init__(self, opts):
        query_options = opts.get(CONFIG_DATA_SECTION, {})
        jinja_filters = template_functions.JINJA_FILTERS
        jinja_filters['b64encode'] = base64.b64encode
        template_functions.ENV.filters.update(jinja_filters)

        super(QueryREST, self).__init__(opts, query_options, rest_call)


def rest_call(options, query_definition, event_message):
    """ Make a REST call and return result """

    # options
    timeout = int(options.get("query_timeout", 60))

    verify = options.get("verify", "")
    if verify[:1].lower() in ("0", "f", "n"):
        verify = False
    else:
        verify = True

    # The REST URL to call is the rendered query expression
    rest_url = query_definition.query

    # The REST method is can be set in 'vars'
    http_method = query_definition.vars.get("http-method", "GET")
    LOG.debug("HTTP method: %s", http_method)

    # HTTP headers can be set in 'vars'
    http_headers = query_definition.vars.get("http-headers", {})
    LOG.debug("HTTP headers: %s", http_headers)

    # HTTP post body can be set in 'vars'
    http_body = query_definition.vars.get("http-body")
    if isinstance(http_body, string_types):
        http_body = json.loads(http_body)
    LOG.debug("HTTP body: %s", http_body)

    session = requests.Session()
    error = None
    response = None
    try:
        response = session.request(http_method, rest_url,
                                   headers=http_headers,
                                   json=http_body,
                                   verify=verify,
                                   timeout=timeout)
        if response.status_code not in [200, 201]:
            raise SimpleHTTPException(response)
        response = response.json()
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

    if not response:
        LOG.warn("No data returned from query")
        if query_definition.default:
            mapdata = copy.deepcopy(event_message)
            mapdata.update(query_definition.vars)
            mapdata.update({"query": query_definition.query})
            default_template = json.dumps({"events": [query_definition.default]}, indent=2)
            default_rendered = template_functions.render_json(default_template, mapdata)
            response = default_rendered

    LOG.debug("Response: %s", json.dumps(response))
    return {"result": response}
# end run_search
