""" Class to store queries and result handling for a Resilient action """

import logging
import json
import os
import copy
import resilient_circuits.template_functions as template_functions
LOG = logging.getLogger(__name__)


class QueryDefinition(object):
    """ Store query and mapping rules for a query action definition """
    query_definitions = {}

    def __init__(self, directory, action_name):
        LOG.info("QueryDefinition: %s/%s", directory, action_name)
        query_definition = self._get_definition(directory, action_name)
        self.name = action_name

        # The 'vars' block defines expressions that are available later
        # to be substituted into the query and processing functions.
        # Useful to calculate variable values that will be used multiple times in the query,
        # or just to extract portions of the query for easier maintenance.
        self.variables = query_definition.get("vars", {})

        # Most actions will have a query (although 'calc' actions don't)
        query = query_definition.get("query", {})

        # The template for the query expression.
        # This can include JINJA expressions, to substitute values from the event message.
        self.query_template = query.get("expression")

        # Ariel supports range-based queries (result pagination), Like 0-50
        self.range = query.get("range", None)

        # Max number of results to retrieve
        self.limit = query.get("limit", None)

        # ODBC can substitute an array of positional parameters into the query expression
        self.parameters = query.get("parameters")
        self.foreach = query.get("foreach")
        if self.parameters is not None and self.foreach is not None:
            raise Exception("Cannot specify both 'parameters' and 'foreach'")

        # You can specify a default row to return in the case that the actual query returns nothing
        self.default = query.get("default")

        # You can specify an error row to return in the case that the query fails with an error
        self.onerror = query.get("onerror")

        # Additional query defitions to run for this action.
        self.additional_queries = query.get("additional_queries", [])

        # The key in the query result object that contains the rows to iterate over as "row"
        # If not provided, the entire query result object will be used
        self.result_container = query.get("extract_results_from")

        # The mapping definitions are handled by update_with_results():
        # If more than one mapping is defined for a single query, they are all processed.

        # Instructions to map the results onto a file attachment
        self.attachment_mapping = query_definition.get("attachment", [])

        # Instructions to map the results onto fields on the incident
        self.incident_mapping = query_definition.get("incident_fields", {})

        # Instructions to map the results onto artifacts
        self.artifact_mapping = query_definition.get("artifacts", [])

        # Instructions to map the results onto data-table rows
        self.data_table_mapping = query_definition.get("datatables", [])

        # Instructions to map the results onto tasks
        self.task_mapping = query_definition.get("tasks", [])

        # Instructions to map the results onto notes
        self.note_mapping = query_definition.get("notes", [])

        # These will be populated when the query is rendered
        self.mapdata = None
        self.vars = None
        self.params = None
        self.each = None
        self.query = None
    # end __init__

    @classmethod
    def _get_definition(cls, directory, action_name):
        try:
            action_filename = os.path.join(directory, action_name)
            mtime = os.path.getmtime(action_filename)
        except OSError:
            LOG.exception("File %s Not Found. Can't run query.", action_name)
            raise

        if action_name in cls.query_definitions:
            timestamp, query_definition = cls.query_definitions[action_name]
            if mtime == timestamp:
                LOG.debug("Using cached query definition for %s", action_name)
                return query_definition
            else:
                LOG.debug("Query definition for %s has been updated. Reload.", action_name)

        # Parse action definition file and store
        with open(action_filename, 'r') as query_file:
            query_definition = json.load(query_file)
            cls.query_definitions[action_name] = mtime, query_definition

        return query_definition
    # end _get_definition

    @staticmethod
    def _json(result):
        for n in range(1, 32):
            result = result.replace(chr(n), " ")
        try:
            value = json.loads(result)
        except:
            LOG.debug("Not JSON: %s", result)
            value = result
        return value

    def render_query(self, map_data, renderer=template_functions.render):
        """ User map_data to render the query expression """
        # Copy the map properties for rendering
        self.mapdata = copy.deepcopy(map_data)
        #
        # If the query definition has any vars, render them, and copy into the mapdata.
        # That's a convenient way to define constants or evaluated values for the mapping.
        # Render as json so that the result can be any type, not just strings.
        if self.variables is not None:
            self.vars = {var_name: self._json(renderer(var_template, self.mapdata)) for (var_name, var_template) in self.variables.items()}
            LOG.debug("Vars: %s", json.dumps(self.vars, indent=2))
        self.mapdata.update(self.vars)
        #
        # Render the 'parameters' (which can be an array or a dict) (but don't add parameters into the map)
        if self.parameters is not None:
            if isinstance(self.parameters, list):
                self.params = [renderer(param_template, self.mapdata) for param_template in self.parameters]
            elif isinstance(self.parameters, dict):
                self.params = {key: renderer(param_template, self.mapdata) for (key, param_template) in self.parameters.items()}
            LOG.info("Query parameters: %s", json.dumps(self.params))
        if self.foreach is not None:
            if isinstance(self.foreach, list):
                self.each = [renderer(param_template, self.mapdata) for param_template in self.foreach]
            elif isinstance(self.parameters, dict):
                self.each = {key: renderer(param_template, self.mapdata) for (key, param_template) in self.foreach.items()}
            else:
                self.each = self._json(renderer(self.foreach, self.mapdata))
            LOG.info("Query for each: %s", json.dumps(self.each))
        #
        # Render the query expression
        if self.query_template is not None:
            self.query = renderer(self.query_template, self.mapdata)

        LOG.info("Query to run: %s", self.query)
    # end render_query

    def render_value(self, value, renderer=template_functions.render):
        """ User map_data to render a value. """
        if self.mapdata is None:
            LOG.warn("Render with no map data!!")
            return value
        return renderer(value, self.mapdata)
    # end render_value
