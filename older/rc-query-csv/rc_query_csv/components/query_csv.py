# -*- coding: utf-8 -*-
"""Action Module circuits component to search comma-separated text files"""

from __future__ import print_function

import logging
import os.path
from string import Template
from pkg_resources import Requirement, resource_filename
from query_runner.lib.query_action import QueryRunner
from rc_query_csv.lib.utils import (unicode_csv_dict_reader, unicode_csv_reader, matching_lines)

LOG = logging.getLogger(__name__)

CONFIG_DATA_SECTION = 'query_csv'


def config_section_data():
    """sample configuration section for use in app.config"""
    config_section = """
# -----------------------------------------------------------------------------
# The 'Query CSV' action component
# -----------------------------------------------------------------------------
[query_csv]

# Message destination
queue=query_csv

# Directory containing query definition files
query_definitions_dir=${directory}

"""
    query_dir = resource_filename(Requirement.parse("rc-query-csv"), "rc_query_csv/data/queries_csv")
    section_config = Template(config_section)
    return section_config.safe_substitute(directory=query_dir)


class QueryCSV(QueryRunner):
    """Search local text files for data and other file handling"""

    def __init__(self, opts):
        options = opts[CONFIG_DATA_SECTION]
        super(QueryCSV, self).__init__(opts, options, search_file, wait_for_complete=True)


def search_file(options, query_definition, event_message):
    """Get rows from a file that match a regular expression and parse them"""
    params = query_definition.params

    # Placeholder for future file types
    # For now we only search utf8-encoded CSV
    file_format = params.get("file_format", "csv")
    if file_format not in (u"csv",):
        LOG.error("file_type must be one of: csv")
        raise ValueError("'%s' is not a supported file_type", file_format)

    # Name of the CSV file to search
    filename = params.get("filename")
    if not filename:
        raise ValueError("filename is a required parameter")
    filename = os.path.expandvars(os.path.expanduser(filename))
    LOG.info("File: %s", filename)

    if file_format == "csv":
        return do_csv_search(options, query_definition, event_message, filename)


def do_csv_search(options, query_definition, event_message, filename):
    """Find matching lines in a CSV file"""
    params = query_definition.params
    col_names_row = params.get("col_names_row")
    lookup_column = params.get("column_name_for_lookup", "")
    lookup_value = params.get("value_for_lookup", "")
    limit = params.get("limit")
    if limit:
        limit = int(limit)

    if query_definition.query:
        LOG.debug("Query: %s", query_definition.query)
    if lookup_column and lookup_value:
        LOG.debug("Match: %s='%s'", lookup_column, lookup_value)

    if col_names_row:
        # CSV file doesn't contain a row with column headers
        # Parse the column headers row from the provided string instead
        reader = unicode_csv_reader([col_names_row], delimiter=',', skipinitialspace=True)
        col_names = list(reader)
        col_names = col_names[0]
        LOG.debug("Column names: %s", ",".join(col_names))
    else:
        LOG.debug("Column names will be pulled from first row of CSV file")
        col_names = None

    with open(filename, 'r') as csv_file:
        # Get all matching rows in file
        result_rows = []
        if query_definition.query:
            rows = matching_lines(csv_file, query_definition.query,
                                  include_header=False if col_names else True)
        else:
            # No query to filter with, just use every line in the file
            rows = csv_file

        rows_matched = 0
        reader = unicode_csv_dict_reader(rows, fieldnames=col_names, skipinitialspace=True)

        for row in reader:
            if lookup_column and lookup_value:
                # We only want rows that have a specific value in a specific column
                if row.get(lookup_column) != lookup_value:
                    # Row doesn't contain our search value in the lookup column
                    continue
            result_rows.append(row)
            rows_matched = rows_matched + 1
            if limit and rows_matched == limit:
                LOG.info("Reached row limit: %d", limit)
                break

    return {"results": result_rows}
