"""Action Module circuits component to update incidents from Queries"""

import logging
import time
from signal import SIGINT, SIGTERM
from collections import defaultdict
from multiprocessing import Lock
from circuits.core.handlers import handler
from circuits import task
from resilient_circuits.actions_component import ResilientComponent, ActionMessage
import resilient_circuits.template_functions as template_functions
from query_runner.lib.misc import NiceEvent, InterruptibleWorker
from query_runner.lib.jinja_filters import *
from query_runner.lib.query_definition import QueryDefinition
from query_runner.lib.query_update import update_with_results

try:
    basestring
except NameError:
    basestring = str

LOG = logging.getLogger(__name__)


class QueryEvent(NiceEvent):
    pass


def search_and_update(run_search, res_client, options, query_definition,
                      event_message, context_token, loglevel, datatable_locks):
    """ Run Query and update incident with results """
    try:
        # In Windows, the loglevel is not passed to threads. Must reset it.
        LOG.setLevel(loglevel)
        logging.getLogger(run_search.__module__).setLevel(loglevel)
        timestamp = int(time.time() * 1000)
        response = run_search(options, query_definition, event_message)
        if response:
            # Add timestamp to search metadata
            if "metadata" in response:
                response["metadata"]["current_time"] = timestamp
            else:
                response["metadata"] = {"current_time": timestamp}
        update_with_results(res_client, query_definition, event_message, response,
                            datatable_locks, context_token)
        return "Query updates finished"
    except:
        LOG.exception("search_and_update error")
        return "Query updates failed"


class QueryRunner(ResilientComponent):
    """
    Base class for query-runner.  Implementations should inherit from this.
    Acknowledges and fires off new query requests.
    """
    datatable_locks = defaultdict(Lock) # Share across all instances

    def __init__(self, all_opts, query_opts, run_search_function, wait_for_complete=False):
        super(QueryRunner, self).__init__(all_opts)
        self.run_search = run_search_function
        self.wait_for_complete = wait_for_complete
        self.options = query_opts
        self.directory = query_opts.get("query_definitions_dir", None)
        if not all((self.directory,
                    self.options.get("queue"))):
            raise Exception("query_definitions_dir, queue are required parameters")
        LOG.debug(self.options)

        # The queue name must be specified in the config file
        self.channel = "actions." + query_opts["queue"]

        # Caches for template rendering (NOTE: not expired, these have the lifetime of the component)
        self.users = None
        self.field_defs = None

        jinja_filters = template_functions.JINJA_FILTERS
        jinja_filters["user"] = self._user_filter
        jinja_filters["value"] = self._value_filter
        jinja_filters["properties_value"] = properties_select_value_filter
        jinja_filters["artifact_type"] = artifact_type_filter
        jinja_filters["prefix"] = prefix_filter
        jinja_filters["suffix"] = suffix_filter
        jinja_filters["fmt"] = fmt_filter
        jinja_filters["split"] = split_filter
        jinja_filters["dict"] = dict_filter
        jinja_filters["zip"] = zip_filter
        template_functions.ENV.filters.update(jinja_filters)

        # Workers to handle multiple queries at once
        self.worker = InterruptibleWorker(process=False, workers=5, channel=self.channel)
        self.worker.register(self)
    # end __init__

    def _user_filter(self, email):
        """
        JINJA filter function to replace a Resilient user's email address 'email' with their full info.
        Use case: Easily check whether a Resilient user exists, or provide their displayname.
        """
        # If no field name specified, nothing to do
        if email == "":
            return None
        # Get the list of all users (requires master-admin)
        if self.users is None:
            self.users = self.rest_client().get("/users")

        # Match 'email' against the current users
        for user in self.users:
            if user["email"].lower() == email.lower():
                return user
        return None

    def _value_filter(self, container, fieldname=None):
        """JINJA filter function to replace Resilient select value 'val' with string"""
        # For translating select, multiselect, multiselect_members, and select_owner type fields
        # For incident fields, container should be a dict, one of "incident", "incident.properties"
        # For artifact properties, container should be a dict "properties"
        # If no field name specified, nothing to extract
        if not fieldname:
            return container

        # Get the current type definitions (merge incident-fields and action-fields)
        field_defs = []
        field_defs.extend(self.rest_client().get("/types/incident/fields"))
        field_defs.extend(self.rest_client().get("/types/actioninvocation/fields"))
        val = container.get(fieldname)
        if not val:
            raise ValueError("field %s not found", fieldname)
        if isinstance(val, list):
            return [self._translate_value(val_id, fieldname, field_defs) for val_id in val]
        else:
            return self._translate_value(val, fieldname, field_defs)

    def _translate_value(self, val, fieldname, field_defs):
        # Match 'val' against the current type definitions
        for field in field_defs:
            if field["name"] == fieldname:
                if field["input_type"] not in ("select", "select_owner", "multiselect",
                                               "multiselect_members"):
                    # Not a type that has an ID that needs translating
                    return val

                values = field.get("values", [])
                for value in values:
                    if value["enabled"] and value["value"] == val:
                        if field["input_type"] in ["multiselect_members", "select_owner"]:
                            # Labels for /fields/incident/members and /fields/incident/owner are not reliable;
                            # users return as "Full Name (email@whatever)" but to set a value requires just email
                            try:
                                user = self.rest_client().get("/users/{}".format(val))
                                return user["email"]
                            except:
                                pass
                        return value["label"]
        else:
            # Field not found in definiton!
            raise ValueError("Field %s not found in Resilient types definition", fieldname)

    # Transformers, etc

    def render_template(self, template, mapdata):
        # Render a JINJA template, using our filters etc
        return template_functions.render(template, mapdata)

    def render_json(self, template, mapdata):
        # Render a JINJA template, using our filters etc
        return template_functions.render_json(template, mapdata)

    @handler()
    def handle_action(self, event, *args, **kwargs):
        """ Action name will tell which query to run """

        if not isinstance(event, ActionMessage):
            # Some event we are not interested in
            return

        # Load the query that is named by the action
        action_name = event.name
        query_definition = QueryDefinition(self.directory, action_name)

        # Render the query template, using values from the event message
        # Add the config options to the event so they can be used for mapping
        event.message.update({"options": self.options})
        query_definition.render_query(event.message, renderer=self.render_template)

        # Any query-runner config section can specify 'loglevel=DEBUG' (etc)
        numeric_log_level = LOG.getEffectiveLevel()
        loglevel = self.options.get("loglevel")
        if loglevel:
            try:
                numeric_log_level = getattr(logging, loglevel)
            except AttributeError:
                pass
            except TypeError:
                pass
        LOG.debug("Log level %s", numeric_log_level)

        # Execute the query
        if self.wait_for_complete:
            search_and_update(self.run_search, self.rest_client(), self.options,
                              query_definition, event.message,
                              event.context, LOG.getEffectiveLevel(),
                              QueryRunner.datatable_locks)
            for name in query_definition.additional_queries:
                # Run any additional queries linked to this action
                other_query_definition = QueryDefinition(self.directory, name)
                other_query_definition.render_query(event.message, renderer=self.render_template)
                search_and_update(self.run_search, self.rest_client(), self.options,
                                  other_query_definition, event.message,
                                  event.context, numeric_log_level,
                                  QueryRunner.datatable_locks)
            yield "Query Completed"
        else:
            self.fire(QueryEvent(query_definition, event))
            for name in query_definition.additional_queries:
                # Start any additional queries linked to this action
                query_definition = QueryDefinition(self.directory, name)
                query_definition.render_query(event.message, renderer=self.render_template)
                self.fire(QueryEvent(query_definition, event))

            yield "Started Query"
    # end handle_action

    @handler("signal")
    def _on_signal(self, signo, stack):
        """Add a signal handler to the worker processes otherwise they swallow SIGINT, SIGTERM
           (see FallBackSignalHandler in circuits/core/helpers.py)
        """
        if signo in [SIGINT, SIGTERM]:
            LOG.info("Interrupted")
            raise SystemExit(0)

    @handler("QueryEvent")
    def _query_event(self, query_definition, action_event):
        """ Handler that kicks off queries and updates """
        numeric_log_level = LOG.getEffectiveLevel()
        loglevel = self.options.get("loglevel")
        if loglevel:
            try:
                numeric_log_level = getattr(logging, loglevel)
            except AttributeError:
                pass
            except TypeError:
                pass
        LOG.debug("Log level %s", numeric_log_level)

        yield self.call(task(search_and_update,
                             self.run_search,
                             self.rest_client(),
                             self.options,
                             query_definition,
                             action_event.message,
                             action_event.context,
                             numeric_log_level,
                             QueryRunner.datatable_locks))
