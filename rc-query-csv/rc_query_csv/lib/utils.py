# -*- coding: utf-8 -*-
"""Some utility functions"""

import csv
import re
import sys
import logging

LOG = logging.getLogger(__name__)


# From https://docs.python.org/2/library/csv.html
def _unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
                            dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]


def _unicode_csv_dict_reader(unicode_csv_data, fieldnames=None, **kwargs):
    if fieldnames:
        fieldnames = [val.encode('utf-8') for val in fieldnames]
    csv_reader = csv.DictReader(unicode_csv_data,
                                fieldnames=fieldnames, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield {unicode(key, 'utf-8'): unicode(value, 'utf-8') for key, value in row.items()}


def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')


def _matching_lines_py2(input_stream, pattern_string, include_header=False):
    """return lines that match a regular expression pattern"""
    pattern = re.compile(pattern_string)
    this_is_header = include_header
    for line in input_stream:
        if this_is_header:
            yield line
            this_is_header = False
        else:
            if pattern.match(unicode(line, 'utf-8')):
                yield line


def _matching_lines_py3(input_stream, pattern_string, include_header=False):
    """return lines that match a regular expression pattern"""
    pattern = re.compile(pattern_string)
    this_is_header = include_header
    for line in input_stream:
        if this_is_header:
            yield line
            this_is_header = False
        else:
            if pattern.match(line):
                yield line


if sys.version_info[0] == 3:
    unicode_csv_dict_reader = csv.DictReader
    unicode_csv_reader = csv.reader
    matching_lines = _matching_lines_py3
else:
    unicode_csv_dict_reader = _unicode_csv_dict_reader
    unicode_csv_reader = _unicode_csv_reader
    matching_lines = _matching_lines_py2
