# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from logging import getLogger
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
LOG = getLogger(__name__)

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
    """Component that implements SOAR function 'dt_utils_create_csv_table''"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
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
            # Instantiate new SOAR API object
            res_client = self.rest_client()

            inputs = {
                "incident_id": get_function_input(kwargs, "incident_id", optional=False),  # number (required)
                "attachment_id": get_function_input(kwargs, "attachment_id", optional=True),  # number (optional)
                "has_headers": get_function_input(kwargs, "dt_has_headers", optional=False),  # boolean (optional)
                "csv_data": get_function_input(kwargs, "dt_csv_data", optional=True),  # text (optional)
                "datable_name": get_function_input(kwargs, "dt_datable_name", optional=False),  # text (required)
                "mapping_table": get_function_input(kwargs, "dt_mapping_table", optional=False),  # text (optional)
                "date_time_format": get_function_input(kwargs, "dt_date_time_format", optional=True),  # text (optional)
                "start_row": get_function_input(kwargs, "dt_start_row", optional=True),  # number (optional)
                "max_rows": get_function_input(kwargs, "dt_max_rows", optional=True),  # number (optional)
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

            datatable = RESDatatable(res_client, inputs["incident_id"], inputs["datable_name"])

            # Retrieve the column names for the datatable, and their data_types,
            # to compare against what the user provides, and attempt data conversion, if necessary
            fields = datatable.get_dt_headers()
            dt_ordered_columns = {fields[field]['order']: (fields[field]['name'],fields[field]['input_type']) for field in fields}
            # Ordered column names if we need to assign the headers to the columns in column order
            dt_column_names = OrderedDict([dt_ordered_columns[field] for field in sorted (dt_ordered_columns.keys())])

            # Different readers if we have headers or not
            dialect = csv.Sniffer().sniff(csv_data[0:csv_data.find('\n')]) # Limit analysis to first row
            # py2 needs changes to dialect to avoid unicode attributes
            if sys.version_info.major < 3:
                for attr in dir(dialect):
                    a = getattr(dialect, attr)
                    if type(a) == unicode:
                        setattr(dialect, attr, bytes(a))
            LOG.debug(dialect.__dict__)

            if inputs["has_headers"]:
                reader = csv.DictReader(inline_data, dialect=dialect)  # Each row is a dictionary keyed by the column name
                csv_headers = reader.fieldnames # Just the headers
            else:
                reader = csv.reader(inline_data, dialect=dialect)  # Each row is a list of values
                csv_headers = []

            mapping_table = build_mapping_table(mapping_table, csv_headers, dt_column_names)
            LOG.debug("csv headers to datatable columns: %s", mapping_table)

            # Perform the api calls to the datatable
            number_of_added_rows, number_of_rows_with_errors = self.add_to_datatable(reader, datatable,
                                                                                     mapping_table, dt_column_names,
                                                                                     inputs['date_time_format'],
                                                                                     inputs['start_row'],
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

    def add_to_datatable(self, reader, datatable, mapping_table, dt_column_names, date_format,
                         start_row, max_rows):
        """Add the csv data to the named datatable. Filter out fields which don't map to the datatable columns
           and convert the data to the column's format, as necessary

        Args:
            reader (csv reader): Reader for csv data
            datatable (object): Object to handle datatable API calls
            mapping_table (dict): Provided by the function
            dt_column_names (OrderDict): column_name: column_type
            date_format (str): '%Y-%m-%dT%H:%M:%S%z'
            start_row (int): Number of row to start adding or None
            max_rows (int): None or max number to add
        Returns:
            [int, int]: number_of_added_rows, number_of_rows_with_errors
        """
        number_of_added_rows = 0
        number_of_rows_with_errors = 0

        indx = 1
        for row in reader:
            LOG.debug("%s: %s",indx, row)
            if not start_row or (start_row and indx >= start_row):
                cells_data = build_row(row, mapping_table, dt_column_names, date_format)
                LOG.debug("cells: %s", cells_data)

                new_row = datatable.dt_add_rows(cells_data)

                if "error" in new_row:
                    number_of_rows_with_errors += 1
                else:
                    number_of_added_rows += 1

                if max_rows and number_of_added_rows >= max_rows:
                    break

            indx += 1

        return number_of_added_rows, number_of_rows_with_errors

def build_mapping_table(input_mapping_table, csv_headers, dt_column_names):
    """Build a mapping table of the columns and datatable columns which are possible to map.

    Args:
        input_mapping_table (dict): Provided to the function
        csv_headers (list): List of csv_headers if they present
        dt_column_names (OrderedDict): column_name: column_type

    Returns:
        [dict]: Valid mapping table with incorrect datatable columns filtered out. If input_mapping_table is None,
          keys in returned dict are positional values: 0, 1, 2, 3
    """
    mapping_table = {}

    # Convert list of fields for csv data without a header
    if isinstance(input_mapping_table, list):
        indx = 0
        for col_name in input_mapping_table:
            if col_name in dt_column_names:
                if csv_headers:
                    if indx < len(csv_headers):
                        mapping_table[csv_headers[indx]] = col_name
                    else:
                        LOG.warning("csv header index: %s larger than list of headers: %s", indx, csv_headers)
                else:
                    mapping_table[indx] = col_name
            else:
                LOG.warning("Skipping datatable column not found. Entry: %s, column name: %s", indx, col_name)
            indx += 1
    else:
        # Only use columns which match the column names in our datatable
        mapping_table = input_mapping_table.copy()
        for csv_header, dt_column_name in input_mapping_table.items():
            if dt_column_name not in dt_column_names:
                LOG.warning(u"Column '%s' not found in datatable. Ignoring.", dt_column_name)
                mapping_table.pop(csv_header)

    return mapping_table

def build_row(csv_row, matching_table, dt_column_names, date_format):
    """
    Build the json structure needed to import a datatable row into SOAR.
    The matching_table is used to identify the datatable column. If matching_table keys are integers,
    refer to the dt_column_names by index location.

    Args:
        csv_row (list): List column data to add to the datatable
        matching_table (dict): "csv_hdr_name":"column_name"
        dt_column_names (OrderedDict): column_name: column_type
        date_format (str): For converting string-based date fields. Ex. '%Y-%m-%dT%H:%M:%S%z'

    Returns: [dict]: Set of columns and values to import into the datatable
    """
    row = {}
    indx = 0
    for csv_column in csv_row:
        # Excel spreadsheets can have BOM ("ByteOrder Mark")
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
            # Index specific mapping_table (no headers used)
            if csv_column_encoded in matching_table:
                dt_col_name = matching_table[csv_column_encoded]
                csv_value = csv_row[csv_column]
            # Get the matching datatable column name
            elif indx in matching_table:
                dt_col_name = matching_table[indx]
                csv_value = csv_column
            else:
                LOG.debug(u"Unable to find mapping entry for csv column: %s", csv_column_encoded)

            converted_value = convert_field(csv_value, dt_column_names[dt_col_name], date_format)

            if dt_col_name in row:
                LOG.warning("Replacing value: '%s' with '%s' for column: '%s'",
                            row.get(dt_col_name),
                            converted_value,
                            dt_col_name)

            row[dt_col_name] = {"value": converted_value}
        except Exception as err:
            LOG.error(u"%s, indx: %s, column: %s, mapping_table: %s",
                      err, indx, csv_column, matching_table)

        indx += 1

    return row

def convert_json(str_json):
    """Convert string-encoded json
    Args:
        str_json (string)

    Returns: [dict]: Converted json or None if an error occurred
    """
    try:
        return json.loads(str_json)
    except:
        return None

def convert_field(value, column_type, date_format):
    """Convert values based on the datatable column type

    Args:
        value (str, int, bool, list): Value to convert. No conversion returns value unchanged
        column_type (str): Column type: text, number, boolean, datetimepicker, select, etc.
        date_format (str): When string-based date values exist, the format of the string:
          ex. "%d/%m/%YT%H:%M:%S%Z"

    Returns:
        multiple: Converted value, if needed or None if a conversion error occurred
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
    """Convert the sting based time value to epoch value

    Args:
        date_value (str): ex. "02/12/2020T12:00:00-5000" or "1604694813000"
        date_format (str): ex. "%d/%m/%YT%H:%M:%S%Z"

    Returns: [int]: Convert value to epoch. If errors, None is returned
    """

    try:
        # Try to see if this is an epoch value
        new_date_value = int(date_value)
        tm = time.gmtime(new_date_value)
        # If in milliseconds, year will be huge
        return new_date_value if tm.tm_year > 3000 else new_date_value*1000
    except ValueError as err:
        pass

    # Try now to convert using date_format pattern
    if not date_format:
        return None

    try:
        return int(time.mktime(time.strptime(date_value, date_format)))*1000
    except Exception as err:
        # python 2 can't do timezone information, strip out if present
        if sys.version_info.major < 3 and TZ_FORMAT.search(date_format):
            new_date_format = TZ_FORMAT.sub("", date_format)
            new_date_value = TZ_VALUE.sub("", date_value)
            try:
                return int(time.mktime(time.strptime(new_date_value, new_date_format)))*1000
            except Exception as err1:
                LOG.error(str(err1))

    LOG.error(u"Unable to convert date to timestamp: '%s' with format '%s'", date_value, date_format)
    return None
