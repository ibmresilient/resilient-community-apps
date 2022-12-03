import io
import json
from json import JSONDecodeError
import os
import pytest
import sys
from datetime import datetime
from resilient_circuits import SubmitTestFunction, FunctionResult

TS = datetime.now()

def read_json_file(path):
    """
    If the contents of the file at path is valid JSON,
    returns the contents of the file as a dictionary

    :param path: Path to JSON file to read
    :type path: str
    :return: File contents as a dictionary
    :rtype: dict
    """
    file_contents = None
    with io.open(path, mode="rt", encoding="utf-8") as the_file:
        try:
            file_contents = json.load(the_file)
        # In PY2.7 it raises a ValueError and in PY3.6 it raises
        # a JSONDecodeError if it cannot load the JSON from the file
        except (ValueError, JSONDecodeError) as err:
            raise Exception("Could not read corrupt JSON file at {0}\n{1}".format(path, err))
    return file_contents


def github_config(function_name):
    # get the file path as an environment variable
    file_path = os.environ.get("TEST_GITHUB_CONFIG")
    return dict(read_json_file(file_path)[function_name])

def create_branch_inputs(ts):
    setup = github_config('create_branch')

    setup["github_branch"] = f"{setup['github_branch'] }_{ts.strftime('%Y%m%d_%H%M%S')}"
    return setup

def create_branch(circuits_app, ts):
    setup = create_branch_inputs(ts)

    results = call_github_create_branch_function(circuits_app, setup)

    return results, setup["github_branch"]

def call_github_create_branch_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("github_create_branch", function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("github_create_branch_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value