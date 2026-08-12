# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Test fn_floss.component.function_floss utility helper functions"""
#
#   Unit test for fn_floss utility helper functions
#
import tempfile
from floss import main
from fn_floss.lib.floss_util import get_binary_data_from_file, get_floss_params, extract_strings, call_floss
from mock import Mock
from mock import patch


def test_get_binary_data_from_file():
    mocked_client = Mock()
    mocked_client.get_content.return_value = "incident article data"
    file_data = get_binary_data_from_file(mocked_client, 100, None, 200, None)
    assert file_data == "incident article data"

    mocked_client.get_content.return_value = "incident attachment data"
    file_data = get_binary_data_from_file(mocked_client, 100, None, None, 300)
    assert file_data == "incident attachment data"

    mocked_client.get_content.return_value = "task attachment data"
    file_data = get_binary_data_from_file(mocked_client, None, 400, None, 300)
    assert file_data == "task attachment data"

    mocked_client.get_content.side_effect = ValueError("task_id or incident_id must be specified with attachment")
    try:
        file_data = get_binary_data_from_file(mocked_client, None, None, None, 300)
        assert False
    except:
        assert True

    mocked_client.get_content.side_effect = ValueError("artifact or attachment or incident id must be specified")
    try:
        file_data = get_binary_data_from_file(mocked_client, None, None, None, None)
        assert False
    except:
        assert True
        
def test_get_floss_params():
    filename = "/user/file.bin"
    list_expected = ["main", "-q", "-s", "-n 5", filename]
    options = "-q,-s,-n 5"
    list_floss = get_floss_params(options, filename)
    assert len(list_floss) == len(list_expected)
    assert list_floss == list_expected

@patch("floss.main.main")
def test_call_floss(mocked_floss):
    # Test the case where running Floss produces an error an error and
    # returns value of 1. (Return value of zero means success.)
    options = "-q,-s,-n 5"

    with tempfile.NamedTemporaryFile('w', bufsize=0) as temp_file_binary:

        # Write binary data to a temporary file.
        data = "these strings might not be found in floss"
        temp_file_binary.write(data)

        mocked_floss.return_value = 1
        try:
            list_string = call_floss(options, temp_file_binary)
        except RuntimeError:
            assert True
        else:
            assert False

        # Test the where Floss returns success.  Make sure that no exception is thrown
        mocked_floss.return_value = 0
        try:
            list_string = call_floss(options, temp_file_binary)
        except RuntimeError:
            assert False
        else:
            assert True


@patch("fn_floss.lib.floss_util.call_floss")
def test_extract_strings(mocked_floss):
    list_expected = ["these", "strings", "might", "found", "floss"]
    mocked_floss.return_value = list_expected
    options = "-q,-s,-n 5"
    data = "these strings might not be found in floss"
    list_floss = extract_strings(options, data)
    assert len(list_floss) == len(list_expected)
    assert list_floss == list_expected


