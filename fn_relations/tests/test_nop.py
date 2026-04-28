from resilient_circuits.util import get_function_definition

PACKAGE_NAME = "fn_relations"
FUNCTION_NAME = "relations_assign_parent"

def test_function_definition():
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None
