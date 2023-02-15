from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from fn_qradar_integration.util.qradar_constants import PACKAGE_NAME
from circuits import Event
import pytest

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_qradar_function(circuits, function_params, func_name, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction(func_name, function_params)
    circuits.app.opts.update({PACKAGE_NAME: {"host": 1, "verify_cert": False}})
    circuits.manager.fire(Event.create("reload", opts=circuits.app.opts))
    event = circuits.watcher.wait(
        "reload_complete", parent=evt, timeout=timeout)
    circuits.manager.fire(Event.create("load", name="QradarSearchFunctionComponent"))
    circuits.watcher.wait("load_complete", parent=None, timeout=timeout)

    circuits.manager.fire(evt)

    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)
    if exception_event is not False:
        exception = exception_event.args[1]
        if len(exception.args) > 1:
            exception = exception.args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait(func_name + "_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value

class TestQRadarFunction:
    """ Tests for the utilities_excel_query function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """

        func = get_function_definition(
            PACKAGE_NAME, "qradar_search")
        assert func is not None

    # this needs full E2E tests, but the verification of options currently is hard to pass