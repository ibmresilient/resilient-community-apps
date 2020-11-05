# (c) Copyright IBM Corp. 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
import csv
import re
import sys
import time
if sys.version_info.major < 3:
    from StringIO import StringIO
    from io import BytesIO
else:
    from io import StringIO, BytesIO
from collections import OrderedDict
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, \
                               FunctionResult, FunctionError
from fn_datatable_utils.util.helper import RESDatatable, get_function_input
from resilient_lib import ResultPayload, get_file_attachment, get_file_attachment_name

PACKAGE_NAME = "fn_datatable_utils"
LOG = logging.getLogger(__name__)

TZ_FORMAT = re.compile(r"%[zZ]")
TZ_VALUE = re.compile(r"[-+]\d{4}")


class FunctionPayload(object):
    """Class that contains the payload sent back to UI and available in the post-processing script"""
    def __init__(self, inputs):
        self.success = True
        self.inputs = inputs
        self.rows = None

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'dt_utils_create_csv_table''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("dt_utils_create_csv_table")
    def _dt_utils_create_csv_table_function(self, event, *args, **kwargs):
        """Function: Create a utility function to take csv data and add the results to a named datatable."""

        try:
            # Instantiate new Resilient API object
            res_client = self.rest_client()

            inputs = {
                "incident_id": get_function_input(kwargs, "incident_id", optional=False),  # number (required)
                "attachment_id": get_function_input(kwargs, "attachment_id", optional=True),  # number (optional)
                "has_headers": get_function_input(kwargs, "dt_has_headers", optional=False),  # boolean (optional)
                "csv_data": get_function_input(kwargs, "dt_csv_data", optional=True),  # text (optional)
                "datable_name": get_function_input(kwargs, "dt_datable_name", optional=False),  # text (required)
                "mapping_table": get_function_input(kwargs, "dt_mapping_table", optional=True),  # text (optional)
                "date_time_format": get_function_input(kwargs, "dt_date_time_format", optional=True),  # text (optional)
                "max_rows": get_function_input(kwargs, "dt_max_rows", optional=True),  # text (optional)
            }

            LOG.info(inputs)

            yield StatusMessage("Starting ...")
            mapping_table = convert_json(inputs['mapping_table'])
            if not mapping_table:
                raise ValueError(u"Unable to convert mapping_table to json: %s", inputs['mapping_table'])

            # Create payload dict with inputs
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            if (inputs["attachment_id"] and inputs["csv_data"]) or \
               not (inputs["attachment_id"] or inputs["csv_data"]):
                raise ValueError("Specify either attachment_id or csv_data")

            # Either an attachment ID or CSV Data is needed to be able to add rows
            if inputs["attachment_id"]:
                attachment_name = get_file_attachment_name(res_client, inputs['incident_id'],
                                                           attachment_id=inputs["attachment_id"])
                b_csv_data = get_file_attachment(res_client, inputs['incident_id'],
                                               attachment_id=inputs["attachment_id"])
                csv_data = b_csv_data.decode("utf-8")
                if sys.version_info.major < 3:
                    inline_data = BytesIO(b_csv_data)
                else:
                    inline_data = StringIO(csv_data)
            else:
                attachment_name = None
                csv_data = inputs["csv_data"]
                if sys.version_info.major < 3:
                    inline_data = StringIO(csv_data.encode("utf-8"))
                else:
                    inline_data = StringIO(csv_data)

            # We need to know how to interpret the data
            if not (inputs["has_headers"] or inputs["mapping_table"]):
                raise ValueError("You must provide a mapping table or indicate if the data contains column headings")

            datatable = RESDatatable(res_client, inputs["incident_id"], inputs["datable_name"])

            # Retrieve the column names for the datatable, and their data_types,
            # to compare against what the user provides, and attempt data conversion, if necessary
            fields = datatable.get_dt_headers()
            dt_ordered_columns = {fields[field]['order']: (fields[field]['name'],fields[field]['input_type']) for field in fields}
            # ordered column names if we need to assign the headers to the columns in column order
            dt_column_names = OrderedDict([dt_ordered_columns[field] for field in sorted (dt_ordered_columns.keys())])

            # different readers if we have headers or not
            dialect = csv.Sniffer().sniff(csv_data)
            # py2 needs changes to dialect to avoid unicode attributes
            if sys.version_info.major < 3:
                for attr in dir(dialect):
                    a = getattr(dialect, attr)
                    if type(a) == unicode:
                        setattr(dialect, attr, bytes(a))

            if inputs["has_headers"]:
                reader = csv.DictReader(inline_data, dialect=dialect)  # each row is a dictionary keyed by the column name
                csv_headers = reader.fieldnames # just the headers
            else:
                reader = csv.reader(inline_data, dialect=dialect)  # each row is a list of values
                csv_headers = []

            mapping_table = build_mapping_table(mapping_table, csv_headers, dt_column_names)
            LOG.debug("csv headers to datatable columns: %s", mapping_table)

            # perform the api calls to the datatable
            number_of_added_rows, number_of_rows_with_errors = self.add_to_datatable(reader, datatable,
                                                                                     mapping_table, dt_column_names,
                                                                                     inputs['date_time_format'],
                                                                                     inputs['max_rows'])
            LOG.info("Number of rows added: %s ", number_of_added_rows)
            LOG.info("Number of rows that could not be added: %s", number_of_rows_with_errors)

            row_data = {
                "data_source": attachment_name if attachment_name else "CSV data",
                "rows_added": number_of_added_rows,
                "rows_with_errors": number_of_rows_with_errors
            }
            results = rp.done(True, row_data)

            yield StatusMessage("Ending ...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionError(err)

    def add_to_datatable(self, reader, datatable, mapping_table, dt_column_names, date_format, max_rows):
        """add the csv data to the named datatable. Filter out fields which don't map to the datatable columns
           and convert the data to the column's format, as necessary

        Args:
            reader (csv reader): reader for csv data
            datatable (object): object to handle datatable API calls
            mapping_table (dict): provided by the function
            dt_column_names (OrderDict): column_name: column_type
            date_format (str): '%Y-%m-%dT%H:%M:%S%z'
            max_rows (int): None or max number to add
        Returns:
            [int, int]: number_of_added_rows, number_of_rows_with_errors
        """
        number_of_added_rows = 0
        number_of_rows_with_errors = 0

        for row in reader:
            LOG.debug(row)
            cells_data = build_row(row, mapping_table, dt_column_names, date_format)
            LOG.debug(cells_data)

            new_row = datatable.dt_add_rows(cells_data)

            if "error" in new_row:
                number_of_rows_with_errors += 1
            else:
                number_of_added_rows += 1

            if max_rows and number_of_added_rows >= max_rows:
                break

        return number_of_added_rows, number_of_rows_with_errors

def build_mapping_table(input_mapping_table, csv_headers, dt_column_names):
    """Build a mapping table of the columns and datatable columns which are possible to map.

    Args:
        input_mapping_table (dict): provided to the function or None. It may be correct or
        csv_headers (list): [description]
        dt_column_names (OrderedDict): column_name: column_type

    Returns:
        [dict]: valid mapping table with incorrect datatable columns filtered out. if input_mapping_table is None,
          keys in returned dict are positional values: 0, 1, 2, 3
    """
    mapping_table = {}

    if input_mapping_table:
        # only use columns which match the column names in our datatable
        mapping_table = input_mapping_table.copy()
        for csv_header, dt_column_name in input_mapping_table.items():
            if dt_column_name not in dt_column_names:
                LOG.warning(u"Column '%s' not found in datatable. Ignoring.", dt_column_name)
                mapping_table.pop(csv_header)
                continue

    else: # has_headers is set, so map to dt columns in header order
        # map each header to a column sequentially for all datatable columns
        mapping_table = {}
        indx = 0
        for header in csv_headers:
            if indx > len(dt_column_names):
                break

            # get the datatable column with the same index
            # it's possible that fewer datatable columns exist
            if indx < len(dt_column_names):
                dt_column  = dt_column_names[indx]
                mapping_table[header] = dt_column
            indx += 1

    return mapping_table

def build_row(csv_row, matching_table, dt_column_names, date_format):
    """
    Build the json structure needed to import a datatable row into Resilient.
    The matching_table is used to identify the datatable column. If matching_table keys are integers,
    refer to the dt_column_names by index location.

    Args:
        csv_row (list): list column data to add to the datatable
        matching_table (dict): "csv_hdr_name":"column_name"
        dt_column_names (OrderedDict): column_name: column_type
        date_format (str): For converting string-based date fields. Ex. '%Y-%m-%dT%H:%M:%S%z'

    Returns:
        [dict]: set of columns and values to import into the datatable
    """
    row = {}
    indx = 0
    for csv_column in csv_row:
        # excel spreadsheets can have BOM ("ByteOrder Mark")
        try:
            if csv_column.startswith(u'\ufeff'):
                csv_column_encoded = csv_column[1:]
            else:
                csv_column_encoded = csv_column
        except UnicodeDecodeError:
            # py2
            if csv_column.startswith('\xef\xbb\xbf'):
                csv_column_encoded = csv_column[3:]
            else:
                csv_column_encoded = csv_column

        try:
            # get the matching datatable column name
            if isinstance(csv_row, list):
                ## use ordered_columns
                if indx in matching_table:
                    row[matching_table[indx]] = \
                       {"value": convert_field(csv_column_encoded, dt_column_names[matching_table[indx]], date_format)}
                else:
                    LOG.warning("Unable to find mapping entry for column index: %s", indx)
            # csv_row == dict
            elif csv_column_encoded in matching_table:
                row[matching_table[csv_column_encoded]] = \
                    {"value": convert_field(csv_row[csv_column], dt_column_names[matching_table[csv_column_encoded]],
                    date_format)}
            else:
                LOG.warning(u"Unable to find mapping entry for csv column: %s", csv_column_encoded)
        except Exception as err:
            LOG.error(u"%s, indx: %s, column: %s, mapping_table: %s",
                      err, indx, csv_column, matching_table)

        indx += 1

    return row

def convert_json(str_json):
    """convert string-encoded json
    Args:
        str_json (string)

    Returns:
        dictionary: converted json or None if an error occurred
    """
    try:
        return json.loads(str_json)
    except:
        return None

def convert_field(value, column_type, date_format):
    """convert values based on the datatable column type

    Args:
        value (multiple): value to convert. No conversions return value unchanged
        column_type (str): column type: text, number, boolean, datetimepicker, select, etc.
        date_format (str): when string-based date values exist, the format of the string: 
          ex. "%d/%m/%YT%H:%M:%S%Z"

    Returns:
        multiple: converted value, if needed or None if a conversion error occurred
    """
    if not value:
        return None

    if column_type in ["text", "textarea"]:
        return str(value)

    if column_type.startswith("date") and not isinstance(value, int):
        return date_to_timestamp(value, date_format)

    if column_type == "number" and not isinstance(value, int):
        try:
            return int(value)
        except:
            LOG.error(u"Unable to convert value to int: %s", value)
            return None

    if column_type == "boolean" and not isinstance(value, (bool, int)):
        return value.lower() in ['true', '1', 'yes', 'y']

    if column_type == "multiselect":
        return [a.strip() for a in value.split(',')]

    return value

def date_to_timestamp(date_value, date_format):
    """convert the sting based time value to epoch value

    Args:
        date_value (str): ex. "02/12/2020T12:00:00-5000"
        date_format (str): ex. "%d/%m/%YT%H:%M:%S%Z"

    Returns:
        [int]: convert value to epoch. If errors, None is returned
    """
    if not date_format:
        return None

    try:
        return int(time.mktime(time.strptime(date_value, date_format)))*1000
    except:
        # python 2 can't do timezone information, strip out if present
        if sys.version_info.major < 3 and TZ_FORMAT.search(date_format):
            new_date_format = TZ_FORMAT.sub("", date_format)
            new_date_value = TZ_VALUE.sub("", date_value)
            try:
                return int(time.mktime(time.strptime(new_date_value, new_date_format)))*1000
            except Exception as err:
                LOG.error(str(err))

    LOG.error(u"Unable to convert date to timestamp: %s", date_value)
    return None
