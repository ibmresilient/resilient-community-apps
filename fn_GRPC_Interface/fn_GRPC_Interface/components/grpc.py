# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""
import os
import sys
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_GRPC_Interface.util.selftest as selftest
import grpc_tools
import grpc
import inspect

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'grpc"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_GRPC_Interface", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_GRPC_Interface", {})

    def __get_interface_file_names(self, base_dir=None, files_dir=None):
        __dir_path = os.path.join(base_dir, files_dir)
        return os.listdir(__dir_path)

    def __get_grpc_interface_module(self, interface_files=[], base_dir=None, files_dir=None):
        assert isinstance(interface_files, list), "This Parameter "'"interface_files"'" should be list data type"
        assert base_dir is not None, "The param base_dir should contain parents parent directory of gRPC interface \
        files"
        assert files_dir is not None, "The param files_dir should points to parent directory of gRPC interface files"
        if interface_files:
            abs_file_path_json = dict()
            interface_module = []

            # creating files abs path
            for file in interface_files:
                abs_file_path = os.path.join(base_dir, files_dir, file)
                abs_file_path_json[file] = abs_file_path

            # Adding Module path into sys.path variable
            interface_dir_path = os.path.join(base_dir, files_dir)
            if interface_dir_path not in sys.path:
                sys.path.append(interface_dir_path)
            else:
                pass

            # compatibility for python 2.7 and 3.6
            logging.info("Loading The Modules : {}".format(interface_files))

            try:
                import importlib.util
                for file_name in interface_files:
                    if file_name.find('.py') != -1:
                        module_name = file_name.split('.')[0]
                        spec = importlib.util.spec_from_file_location(module_name, abs_file_path_json[file_name])
                        if spec:
                            module_obj = importlib.util.module_from_spec(spec)
                            spec.loader.exec_module(module_obj)
                            interface_module.append(module_obj)
                    else:
                        logging.debug("File is not Python File.")

            except ImportError as e:
                logging.info("The Import Error raised for the module importlib trying with imp module : {}".format(e))
                import imp
                for file_name in interface_files:
                    if file_name.find('.py') != -1:
                        module_name = file_name.split('.')[0]
                        module_obj = imp.load_source(module_name, abs_file_path_json[file_name])
                        interface_module.append(module_obj)
            return interface_module
        else:
            logging.debug("No Interface file found, please specify the interface file")
            return None

    def __get_grpc_class(self, grpc_module_list, class_name):
        for grpc_module in grpc_module_list:
            for name, obj in inspect.getmembers(grpc_module, inspect.isclass):
                logging.info("NAME : {} OBJECT : {}".format(name, obj))
                if name.lower().find(class_name.lower()) != -1:
                    return name, obj
        else:
            return ()

    def __get_method_from_stub_object(self, stub_object, comm_type):

        stub_elements = inspect.getmembers(stub_object)
        logging.debug("Stub Object Elements : {}".format(stub_elements))
        for name, obj in stub_elements:

            if name not in ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__ge__',
                            '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
                            '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
                            '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']:
                if str(obj).lower().find(comm_type) != -1:
                    logging.info("found Stub name : {} and object : {}".format(name,obj))
                    return name, obj

    @function("grpc")
    def _grpc_function(self, event, *args, **kwargs):
        """Function: A function to communicate with gRPC Servers"""
        try:
            # Get the function parameters:
            grpc_channel = kwargs.get("grpc_channel")  # text
            grpc_interface_dir = kwargs.get("grpc_interface_dir")  # text
            grpc_secure_connection = kwargs.get("grpc_secure_connection")  # boolean
            grpc_io_name = kwargs.get("grpc_io_name")  # text
            grpc_communication_type = kwargs.get("grpc_communication_type")  # text
            grpc_data = kwargs.get("grpc_data")  # text
            grpc_request_function_name = kwargs.get("grpc_request_function_name")  # text

            log = logging.getLogger(__name__)
            log.info("grpc_channel: %s", grpc_channel)
            log.info("grpc_interface_dir: %s", grpc_interface_dir)
            log.info("grpc_secure_connection: %s", grpc_secure_connection)
            log.info("grpc_io_name: %s", grpc_io_name)
            log.info("grpc_communication_type: %s", grpc_communication_type)
            log.info("grpc_data: %s", grpc_data)
            log.info("grpc_request_function_name: %s", grpc_request_function_name)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")
            files = self.__get_interface_file_names(grpc_interface_dir, grpc_io_name)

            grpc_interface_module_list = self.__get_grpc_interface_module(files, grpc_interface_dir,grpc_io_name)
            logging.debug(grpc_interface_module_list)
            grpc_stub_tuple = self.__get_grpc_class(grpc_interface_module_list, 'stub')
            grpc_request_tuple = self.__get_grpc_class(grpc_interface_module_list, grpc_request_function_name.lower())
            if not grpc_secure_connection:
                logging.info("gRPC Channel Connection is not secure.")
                if grpc_communication_type.lower().find('unary') != -1:
                    with grpc.insecure_channel(grpc_channel) as channel:

                        stub = grpc_stub_tuple[1](channel)
                        stub_method = self.__get_method_from_stub_object(stub, grpc_communication_type)
                        response_received = stub_method[1](grpc_request_tuple[1](name=grpc_data))
                else:
                    logging.info("Connection type is Server_Stream or other")
            else:
                logging.info("gRPC Connection is Secure..")
                response_received = None
            yield StatusMessage("done...")

            results = {
                "value": str(response_received)
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)

