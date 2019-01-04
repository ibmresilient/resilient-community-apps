# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import sys
import os
import json
import grpc
import grpc_tools
import re
import inspect
class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'function_grpc"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_grpc", {})


    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_grpc", {})


    def _get_interface_file_names(self, base_dir=None, files_dir=None):
        __dir_path = os.path.join(base_dir, files_dir)
        return os.listdir(__dir_path)


    def _get_grpc_interface_module(self, interface_files=[], base_dir=None, files_dir=None):
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


    def _get_grpc_class(self, grpc_module_list, class_name):
        for grpc_module in grpc_module_list:
            for name, obj in inspect.getmembers(grpc_module, inspect.isclass):
                logging.info("NAME : {} OBJECT : {}".format(name, obj))
                if name.lower().find(class_name.lower()) != -1:
                    return name, obj
        else:
            return ()


    def _get_method_from_stub_object(self, stub_object, comm_type, stub_name =''):

        stub_elements = inspect.getmembers(stub_object)
        logging.debug("Stub Object Elements : {}".format(stub_elements))
        for name, obj in stub_elements:

            if name not in ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__ge__',
                            '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
                            '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
                            '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']:
                if str(obj).lower().find(comm_type) != -1 and name.find(stub_name) != -1:
                    logging.info("found Stub name : {} and object : {}".format(name,obj))
                    return name, obj


    @function("function_grpc")
    def _function_grpc_function(self, event, *args, **kwargs):
        """Function: A function to communicate with GRPC Servers based on the Communication Methods Specified."""
        try:
            # Get the function parameters:
            grpc_channel = kwargs.get("grpc_channel")  # text
            grpc_function = kwargs.get("grpc_function")  # text
            grpc_function_data = kwargs.get("grpc_function_data")  # text

            log = logging.getLogger(__name__)
            log.info("grpc_channel: %s", grpc_channel)
            log.info("grpc_function: %s", grpc_function)
            log.info("grpc_function_data: %s", grpc_function_data)

            yield StatusMessage("starting...")
            response_received = None
            grpc_function_json_data = None

            # Parsing the variable data from config file and resilient inputs
            try:
                _grpc_package_name = grpc_function.split(':')[0]
                _grpc_rpc_stub_method_name = grpc_function.split(':')[1].split("(")[0]
                _grpc_request_method_name = re.sub("\)", '', grpc_function.split(':')[1].split("(")[1])
                config_file_data = self.options.get(_grpc_package_name).split(',')
                _grpc_secure_connection = config_file_data[1]
                _grpc_communication_type = config_file_data[0]
                _grpc_google_tocken = config_file_data[2]
                _grpc_certificate_path = config_file_data[2]
                _grpc_interface_file_dir = self.options.get('interface_dir')
                log.info("grpc_package_name : {} grpc_rpc_stub_method_name : {} grpc_request_method_name : {}".format(_grpc_package_name,_grpc_rpc_stub_method_name,_grpc_request_method_name))
            except Exception as e:
                yield StatusMessage("failed to parse the function parameters.{}".format(e))
                raise FunctionError(e)

            # importing grpc protobuf files from the given interface directory
            try:
                module_files = self._get_interface_file_names(_grpc_interface_file_dir, _grpc_package_name)
                grpc_interface_module_list = self._get_grpc_interface_module(module_files, _grpc_interface_file_dir, _grpc_package_name)
                logging.debug(grpc_interface_module_list)

                grpc_stub_tuple = self._get_grpc_class(grpc_interface_module_list, 'stub')
                grpc_request_tuple = self._get_grpc_class(grpc_interface_module_list, _grpc_request_method_name.lower())
            except Exception as e:
                yield StatusMessage("failed to load the grpc protobuf files : {}".format(e))
                raise FunctionError(e)

            # converting resilient input data into json object
            try:
                grpc_function_data = re.sub("'", '"', grpc_function_data)
                grpc_function_json_data = json.loads(grpc_function_data)
            except Exception as e:
                raise FunctionError("Input Data must be in json formatted..!")

            # Checking the secure connection type
            if _grpc_secure_connection.lower() not in ['ssl','tsl','oauth2'] and not eval(_grpc_secure_connection):
                logging.info("gRPC Channel Connection is not secure.")
                # Checking Communication type
                if _grpc_communication_type.lower().find('unary') != -1:
                    # Initiating the connection to channel to send the data from client to grpc server
                    try:
                        with grpc.insecure_channel(grpc_channel) as channel:
                            stub = grpc_stub_tuple[1](channel)
                            stub_method = self._get_method_from_stub_object(stub, _grpc_communication_type, stub_name=_grpc_rpc_stub_method_name)
                            if grpc_function_json_data:
                                response_received = stub_method[1](grpc_request_tuple[1](**grpc_function_json_data))
                    except grpc.RpcError as rpc_err:
                        status_code = rpc_err.code()
                        log.info("{}\n connection status :{} \n name : {}\n value : {}".format(rpc_err,rpc_err.details(),status_code.name,status_code.value))
                    else:
                        log.info("Response received from the server : {}".format(str(response_received)))
                else:
                    logging.info("Connection type is Server_Stream or client_stream,Bidirectional or other\n \
                    Not Implemented these {} communication types ".format(_grpc_communication_type))
            else:
                logging.info("gRPC Channel Connection is Secure..")

            yield StatusMessage("done...")
            results = {
                "server_response": str(response_received),
                "channel": grpc_channel
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)