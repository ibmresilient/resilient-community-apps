# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import openpyxl


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_excel_query"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_utilities", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_utilities", {})

    @function("utilities_excel_query")
    def _utilities_excel_query_function(self, event, *args, **kwargs):
        """Function: Extract ranges of data or named ranges specified by the user from an excel document."""
        try:
            # Get the function parameters:
            attachment_id = kwargs.get("attachment_id")  # number
            excel_ranges = kwargs.get("excel_ranges")  # text
            excel_defined_names = kwargs.get("excel_defined_names")  # text
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number

            log = logging.getLogger(__name__)
            log.info("attachment_id: %s", attachment_id)
            log.info("excel_ranges: %s", excel_ranges)
            log.info("excel_defined_names: %s", excel_defined_names)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()


class WorksheetData(object):
    """
    Facade pattern with openpyxl library that will parse the given worksheet into
    the json of requested content.
    """
    # These constant adjust the return JSON namings
    SHEETS_TITLES = "titles"
    SHEET_SIZE = "size_range"
    START_ROW = "start_row"
    END_ROW = "end_row"
    PARSED_SHEETS = "sheets"
    PARSED_SHEETS_LIST = "parsed_sheets"
    NAMED_RANGES = "named_ranges"

    def __init__(self, path, opts={}):
        """
        :param path : String
            an absolute path to the file
        :param opts: Dict
            contains options with the following options
            named_ranges: String or List, to grab those from the file
            sheets:     List if only specific sheets need to be grabbed
                        False is none of the sheets should be parsed
            start_row:  True if for all sheets the start row should be recorded
            end_row:    True if for all sheets the end row should be recorded
            titles:     True if want to receive a list of all sheet names
        """
        super().__init__()
        self._file_path = path
        self.wb = openpyxl.load_workbook(self._file_path, read_only=True)
        # options
        self.opts = opts
        # the eventual return value
        self.result = {}
        # store option as a variable, so every sheet doesn't do this check
        self._start_row = False
        self._end_row = False
        self._size = False

        self.parse()

    def parse(self):
        """
        Goes through the options and fills our self.result accordingly
        """
        self.result = {}

        self._start_row = True if "start_row" in self.opts and self.opts["start_row"] else False
        self._end_row = True if "end_row" in self.opts and self.opts["end_row"] else False
        self._size = True if "size" in self.opts and self.opts["size"] else False

        # check of "titles" is required
        if "titles" in self.opts and self.opts["titles"]:
            self.result[self.SHEETS_TITLES] = self.wb.sheetnames

        # check if "named_ranges" is in the opts, and is not falsy
        if "named_ranges" in self.opts and self.opts["named_ranges"]:
            self.parse_named_ranges()

        # check if "sheets" is in the opts, and is not falsy
        if "sheets" in self.opts:
            if self.opts["sheets"]:
                self.parse_workbook(self.opts["sheets"])
        else:
            self.parse_workbook(self.wb.sheetnames)

    def parse_named_ranges(self):
        """
        Gets a list or a string of named ranges from options
        and calls parse_named_range for each of them
        """
        self.result[self.NAMED_RANGES] = {}
        # check if a list of named ranged is requested or a single named range
        if isinstance(self.opts['named_ranges'], list):
            for name in self.opts['named_ranges']:
                self.parse_named_range(name)
        elif isinstance(self.opts['named_ranges'], str):
            self.parse_named_range(self.opts["named_ranges"])
        elif isinstance(self.opts['named_ranges'], bool):
            for range in self.wb.defined_names.definedName:  # defined_names is a list of DefinedName objects
                self.parse_named_range(range.name)

    def parse_named_range(self, name):
        """
        :param name: String
             name of the named range to add to the return.
             It contains multiple ranges itself.
        """
        result = []
        # check if the named range is really in the workbook
        if name not in self.wb.defined_names:
            return
        ranges = self.wb.defined_names[name]  # get the data of the named range
        destinations = ranges.destinations  # returns a generator of tuples (ws title, range)
        for sheet_name, range in destinations:
            # worksheet
            ws = self.wb[sheet_name]
            result.append(ws[range])

        self.result[self.NAMED_RANGES][name] = result

    def parse_workbook(self, sheets):
        """

        :param sheets: List of Strings
            List of the sheets to get the data from
        """
        self.result[self.PARSED_SHEETS_LIST] = sheets
        self.result[self.PARSED_SHEETS] = {}
        for sheet in sheets:
            self.parse_sheet(self.wb[sheet])

    def parse_sheet(self, sheet):
        """
        Gets the requested data from a particular worksheet
        :param sheet: openpyxl's Worksheet class
        """
        sheet.calculate_dimension(force=True)
        self.result[self.PARSED_SHEETS][sheet.title] = {}

        if self._size:
            self.record_size(sheet)
        if self._start_row:
            self.record_start_row(sheet)
        if self._end_row:
            self.record_end_row(sheet)

    def record_size(self, sheet):
        """
        Records the known size of the sheet
        :param sheet: Sheet
        """
        self.result[self.PARSED_SHEETS][sheet.title][self.SHEET_SIZE] = {
                "range": sheet.calculate_dimension(),
                "max_row": sheet.max_row,
                "min_row": sheet.min_row,
                "max_col": sheet.max_column,
                "min_col": sheet.min_column
            }

    def record_start_row(self, sheet):
        """
        Records the first row
        :param sheet: Sheet
        """
        result = []
        # try/except to catch library errors in empty sheets
        try:
            result = [cell.value for cell in sheet[sheet.min_row]]
        except IndexError:
            pass
        self.result[self.PARSED_SHEETS][sheet.title][self.START_ROW] = result

    def record_end_row(self, sheet):
        """
        Records the last row
        :param sheet: Sheet
        """
        result = []
        # try/except to catch library errors in empty sheets
        try:
            result = [cell.value for cell in sheet[sheet.max_row]]
        except IndexError:
            pass
        self.result[self.PARSED_SHEETS][sheet.title][self.END_ROW] = result
