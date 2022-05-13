import pytest
from io import StringIO
from logging import getLogger
from collections import OrderedDict
from csv import DictReader, Sniffer, reader
from fn_datatable_utils.components.dt_utils_create_csv_table import build_row, build_mapping_table, convert_field

LOG = getLogger(__name__)
DATE_FORMAT = '%Y-%m-%dT%H:%M:%S%z'  # "2017-06-09T00:00:00+0000"
DT_COLUMN_NAMES = OrderedDict([
    ("col0", "text"),
    ("col1", "int"),
    ("col2", "select"),
    ("col3", "datetimepicker"),
    ("col4", "boolean")
])

@pytest.mark.parametrize("inputs, mapping_table, expected_results", [
    ("'h1','h2','h3'\n'a','b','c'", {'h3': "col0", 'h1': "col1", 'h2': "col2"}, {
     'col1': {'value': "a"}, 'col2': {'value': "b"}, 'col0': {'value': "c"}}),
    ("'h1','h2','h3'\n'a','b','c'", {'h3': "col0", 'h2': "col2"}, {
        'col0': {'value': "c"}, 'col2': {'value': "b"}})
])
def test_build_row_has_header(inputs, mapping_table, expected_results):
    s = StringIO(inputs)
    csv_reader = DictReader(s, dialect=Sniffer().sniff(inputs))
    for data_row in csv_reader:
        result = build_row(data_row, mapping_table,
                           DT_COLUMN_NAMES, DATE_FORMAT)
        for col in result:
            assert col in expected_results
            assert result[col] == expected_results[col]

@pytest.mark.parametrize("inputs, mapping_table, expected_results", [
    ("'a','b','c'", {2: "col0", 0: "col1", 1: "col2"}, {
     'col1': {'value': "a"}, 'col2': {'value': "b"}, 'col0': {'value': "c"}}),
    ("'a','b','c'", {0: "col1", 1: "col2"}, {
     'col1': {'value': "a"}, 'col2': {'value': "b"}})
])
def test_build_row_no_header(inputs, mapping_table, expected_results):
    s = StringIO(inputs)
    csv_reader = reader(s, dialect=Sniffer().sniff(inputs))
    for data_row in csv_reader:
        result = build_row(data_row, mapping_table,
                           DT_COLUMN_NAMES, DATE_FORMAT)
        for col in result:
            assert col in expected_results
            assert result[col] == expected_results[col]

@pytest.mark.parametrize("inputs, mapping_table, expected_results", [
    ("'h1','h2','h3'\n'a','b','2020-10-02T16:00:42+0000'", {'h3': "col3", 'h1': "col1", 'h2': "col2"},
     {'col1': {'value': "a"}, 'col2': {'value': "b"}, 'col3': {'value': 1601654442000}}),
    ("'h1','h2','h3'\n'a','b','1601668842000'", {'h3': "col3", 'h1': "col1", 'h2': "col2"},
     {'col1': {'value': "a"}, 'col2': {'value': "b"}, 'col3': {'value': 1601668842000}}),
    ("'h1','h2','h3'\n'a','b',1601668842000", {'h3': "col3", 'h1': "col1", 'h2': "col2"},
     {'col1': {'value': "a"}, 'col2': {'value': "b"}, 'col3': {'value': 1601668842000}}),
    ("'h1','h2','h3'\n'a','b','1601668842'", {'h3': "col3", 'h1': "col1", 'h2': "col2"},
     {'col1': {'value': "a"}, 'col2': {'value': "b"}, 'col3': {'value': 1601668842000}}),
])
def test_build_row_datetime(inputs, mapping_table, expected_results):
    s = StringIO(inputs)
    csv_reader = DictReader(s, dialect=Sniffer().sniff(inputs))
    for data_row in csv_reader:
        result = build_row(data_row, mapping_table,
                           DT_COLUMN_NAMES, DATE_FORMAT)
        for col in result:
            assert col in expected_results
            assert result[col] == expected_results[col]

@pytest.mark.parametrize("mapping_table, csv_headers, dt_column_names, expected_results", [
    ({'h3': "col0", 'h1': "col1", 'h2': "col2"}, ['h1', 'h2', 'h3'], [
     'col0', 'col1', 'col2'], {'h1': 'col1', 'h2': 'col2', 'h3': 'col0'}),
    ({'h3': "colx", 'h1': "col1", 'h2': "col2"}, ['h1', 'h2', 'h3'], [
     'col0', 'col1', 'col2'], {'h1': 'col1', 'h2': 'col2'}),
    ({'hx': "col0", 'h1': "col1", 'h2': "col2"}, ['h1', 'h2', 'h3'], [
     'col0', 'col1', 'col2'], {'h1': 'col1', 'h2': 'col2'}),
    (['a', 'b', 'c'], None, ['a', 'b', 'c'], {0: 'a', 1: 'b', 2: 'c'}),
    ([None, 'b', 'c'], None, ['a', 'b', 'c'], {1: 'b', 2: 'c'}),
    ([None, 'b', 'd'], None, ['a', 'b', 'c'], {1: 'b'}),
    ([None, None, 'c', None, 'b', 'a'], None, [
     'a', 'b', 'c'], {2: 'c', 4: 'b', 5: 'a'})
])
def test_build_mapping_table(mapping_table, csv_headers, dt_column_names, expected_results):
    mapping_table = build_mapping_table(
        mapping_table, csv_headers, dt_column_names)
    for key in expected_results.keys():
        assert mapping_table.get(key)
        assert mapping_table[key] == expected_results[key]

@pytest.mark.parametrize("value, data_type, date_format, expected_value", [
    ("abc", "text", None, "abc"),
    ("10", "number", None, 10),
    (10, "number", None, 10),
    ('2020-10-02T16:00:42+0000', "datetimepicker", DATE_FORMAT, 1601654442000),
    (1601668842000, "datetimepicker", DATE_FORMAT, 1601668842000),
    ("true", "boolean", None, True),
    (True, "boolean", None, True),
    ("a", "select", None, "a"),
    ("a,b", "multiselect", None, ['a', 'b'])
])
def test_convert_field(value, data_type, date_format, expected_value):
    return_value = convert_field(value, data_type, date_format)
    assert return_value == expected_value
