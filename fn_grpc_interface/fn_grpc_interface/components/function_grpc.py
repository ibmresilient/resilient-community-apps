# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import sys
import os
import json
import grpc
import re
import inspect
from google.protobuf.json_format import MessageToDict
import six

try:
    # PY3
    import importlib.util
except ImportError as e:
    # PY2
    logging.debug("The Import Error raised for the module importlib trying with imp module : {}".format(e))
    import imp

if six.PY2:
    # Used to Convert unicode strings to utf-8 for python 2.7
    import ast

log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements generic wrapper for the gRPC client on the Resilient platform"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_grpc_interface", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_grpc_interface", {})

    def _get_grpc_interface_module(self, interface_files=[], base_dir=None, files_dir=None):
        """
        component that imports all the modules in the current workspace and returns the given imported modules objects.
        :param interface_files: List of all buffer pb2 files absolute path to import in the current work space
        :param base_dir:  interface pb2 files parent directory.
        :param files_dir: interface pb2 files directory i.e same as package name.
        :return: returns imported interface pb2 files module objects on the successful execution, else returns None object.
        """
        if not isinstance(interface_files, list):
            raise ValueError("This Parameter "'"interface_files"'" should be list data type")
        if base_dir is None:
            raise ValueError("The param base_dir should contain parents parent directory of gRPC interface files")
        if files_dir is None:
            raise ValueError("The param files_dir should points to parent directory of gRPC interface files")

        if interface_files:
            abs_file_path_json = dict()
            interface_module = []

            # creating files abs path
            for file_name in interface_files:
                abs_file_path = os.path.join(base_dir, files_dir, file_name)
                abs_file_path_json[file_name] = abs_file_path

            # Adding Module path into sys.path variable
            interface_dir_path = os.path.join(base_dir, files_dir)
            if interface_dir_path not in sys.path:
                sys.path.append(interface_dir_path)

            # compatibility for python 2.7 and 3.6
            log.info("Loading The Modules : {}".format(interface_files))

            if six.PY3:
                for file_name in interface_files:
                    if file_name.endswith('.py'):
                        module_name = file_name.split('.')[0]
                        spec = importlib.util.spec_from_file_location(module_name, abs_file_path_json[file_name])
                        if spec:
                            module_obj = importlib.util.module_from_spec(spec)
                            spec.loader.exec_module(module_obj)
                            interface_module.append(module_obj)
                    else:
                        log.debug("No python modules found to import.")
            elif six.PY2:
                for file_name in interface_files:
                    if file_name.endswith('.py'):
                        module_name = file_name.split('.')[0]
                        module_obj = imp.load_source(module_name, abs_file_path_json[file_name])
                        interface_module.append(module_obj)
            else:
                raise ValueError("We do not support this version of python")

            return interface_module
        else:
            log.debug("No Interface file found, please specify the interface file")
            return None

    def _get_grpc_class(self, grpc_module_list, class_name):
        """
        component that return the given class object from the list of given module objects,
        evaluates based on the given class names.
        :param grpc_module_list: imported interface pb2 files module objects list
        :param class_name:  interested class name in the given module objects list
        :return:  tuple of name and class object of the given class name if class name found in the given module
        objects, else returns an empty tuple.
        """
        for grpc_module in grpc_module_list:
            for name, obj in inspect.getmembers(grpc_module, inspect.isclass):
                log.debug("Class Name : {} Object : {}".format(name, obj))
                if name.lower().find(class_name.lower()) != -1:
                    return name, obj
        else:
            return ()

    def _gRPC_Connect_Server(self, auth_type=None, channel=None, stub_class=None, certificate_path=None):
        """

        :param auth_type: Input Secure Connection type
        :param channel: gRPC Channel
        :param stub_class: a Stub Class object from imported pb2 library
        :param certificate_path: path of the ssl/tls certificate
        :return: stub class object
        """
        # Checking supplied Input Arguments
        if channel is None:
            raise ValueError("channel argument should not be None type")
        if stub_class is None:
            raise ValueError("stub class object should not be None type")

        if auth_type.lower().strip() not in ['ssl', 'tls', 'oauth2'] and auth_type.lower().strip() == "none":
            log.info("gRPC Channel Connection is not secure.")
            channel_object = grpc.insecure_channel(channel)
            stub_class_obj = stub_class(channel_object)
            return stub_class_obj, channel_object
        elif auth_type.lower().strip().find('ssl') != -1 or auth_type.lower().strip().find('tls') != -1:
            log.info("Channel Authentication is secure : {0}".format(auth_type))
            if certificate_path is None:
                raise ValueError("Please specify the valid certificate path")
            if certificate_path.lower() == 'none':
                raise ValueError("Please specify the valid certificate path")
            with open(certificate_path, 'rb') as certificate:
                channel_cred = grpc.ssl_channel_credentials(root_certificates=certificate.read())
            channel_object = grpc.secure_channel(channel, channel_cred)
            stub_class_obj = stub_class(channel_object)
            return stub_class_obj, channel_object
        else:
            raise NotImplementedError("The authentication type {0} is not supported".format(auth_type))

    @function("function_grpc")
    def _function_grpc_function(self, event, *args, **kwargs):
        """Function: A function to communicate with GRPC Servers based on the Communication Methods Specified."""

        def _get_interface_file_names(base_dir=None, files_dir=None):
            """
            component that return the absolute path of all files in the given directory
            :param base_dir:  interface pb2 files parent directory
            :param files_dir:  interface pb2 files directory i.e same as package name
            :return: lists of all pb2 files absolute path inside the given directory path
            """
            __dir_path = os.path.join(base_dir, files_dir)
            return os.listdir(__dir_path)

        def _get_method_from_stub_object(stub_object, comm_type, stub_name=''):
            """
            component that returns stub method from the given stub class objects, evaluates based on the given stub name and
            communication type param.
            :param stub_object:  stub Class object
            :param comm_type:   communication type (i.e unary, server_stream,client_stream,bidirectional_stream)
            :param stub_name:   name of the stub method in the stub class
            :return: returns tuple of name and object of the stub method on success else returns None object
            """
            _found_stub_name = None
            _found_stub_object = None
            stub_elements = inspect.getmembers(stub_object)
            for name, obj in stub_elements:
                if name not in ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__ge__',
                                '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
                                '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
                                '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '__dir__']:

                    if str(obj).lower().find(comm_type) != -1 and name.lower().strip() == stub_name.lower().strip():
                        log.debug("found Stub name : {} and object : {}".format(name, obj))
                        _found_stub_name = name
                        _found_stub_object = obj

            return _found_stub_name, _found_stub_object

        try:
            # Get the function parameters:
            grpc_channel = kwargs.get("grpc_channel")  # text
            grpc_function = kwargs.get("grpc_function")  # text
            grpc_function_data = kwargs.get("grpc_function_data")  # text

            log.info("grpc_channel: %s", grpc_channel)
            log.info("grpc_function: %s", grpc_function)
            log.info("grpc_function_data: %s", grpc_function_data)

            yield StatusMessage("Connecting to gRPC Server...!")

            # Parsing the variable data from config file and resilient inputs
            try:
                # validate the gRPC Function Parameter to make sure data in this `helloword:SayHello(HelloRequest)`
                match_found = re.match(r'\w+\:\w+\(\w+\)$', grpc_function, re.IGNORECASE)
                if match_found:
                    log.info("gRPC Function input parameter 'grpc_function' data is validated.")
                else:
                    raise ValueError(
                        "Please provide gRPC input parameter 'grpc_function' data correctly in resilient input section.value")

                _grpc_package_name = grpc_function.split(':')[0].strip()
                _grpc_rpc_stub_method_name = grpc_function.split(':')[1].split("(")[0].strip()
                _grpc_request_method_name = re.sub("\)", '', grpc_function.split(':')[1].split("(")[1])
                _grpc_request_method_name = _grpc_request_method_name.strip()

                config_file_data = self.options.get(_grpc_package_name).split(',')
                _grpc_secure_connection = config_file_data[1]
                _grpc_communication_type = config_file_data[0]
                _grpc_google_tocken = config_file_data[2]
                _grpc_certificate_path = config_file_data[2]
                _grpc_interface_file_dir = self.options.get('interface_dir')

                log.info("gRPC Package Name : {} gRPC Stub Method Name : {} gRPC Request Class Name : {}" \
                         .format(_grpc_package_name, _grpc_rpc_stub_method_name, _grpc_request_method_name))
            except Exception as err:
                raise ValueError("failed to parse the function parameters.{0}".format(err))

            # Importing gRPC proto buff files from the given interface directory.
            try:
                module_files = _get_interface_file_names(_grpc_interface_file_dir, _grpc_package_name)
                grpc_interface_module_list = self._get_grpc_interface_module(module_files, _grpc_interface_file_dir,
                                                                             _grpc_package_name)
                log.debug(grpc_interface_module_list)

                grpc_stub_tuple = self._get_grpc_class(grpc_interface_module_list, 'stub')
                grpc_request_tuple = self._get_grpc_class(grpc_interface_module_list, _grpc_request_method_name.lower())
            except Exception as error_msg:
                raise ValueError("failed to load the gRPC proto buff files : {0}".format(error_msg))

            # Converting resilient function input data into json object
            try:
                # Inside Function Component
                grpc_function_json_data = json.loads(grpc_function_data)
            except Exception:
                raise FunctionError("Input Data must be in json formatted..!")

            # Checking Communication type
            if _grpc_communication_type.lower().strip() == "unary":
                try:
                    # Connecting to gRPC Server with given Authentication type
                    stub_class_obj, grpc_channel_obj = self._gRPC_Connect_Server(_grpc_secure_connection, grpc_channel, \
                                                                                 grpc_stub_tuple[1],
                                                                                 _grpc_certificate_path)
                    stub_method = _get_method_from_stub_object(stub_class_obj, _grpc_communication_type,
                                                               stub_name=_grpc_rpc_stub_method_name)
                    if grpc_function_json_data:
                        if stub_method[1] is not None:
                            if six.PY2:
                                # convert unicode strings to utf-8 for python 2.7
                                grpc_function_json_data_tmp = ast.literal_eval(json.dumps(grpc_function_json_data))
                            else:
                                grpc_function_json_data_tmp = grpc_function_json_data

                            response_received_tmp = stub_method[1](grpc_request_tuple[1](**grpc_function_json_data_tmp))

                            # Closing the gRPC Server Connection
                            grpc_channel_obj.close()
                        else:
                            raise FunctionError("Stub method not found, please specify the valid stub method.")
                    else:
                        raise FunctionError("Please Specify the valid data input form the Resilient.")
                except grpc.RpcError as rpc_err:
                    status_code = rpc_err.code()
                    log.debug(
                        "{}\n connection status :{} \n name : {}\n value : {}".format(rpc_err, rpc_err.details(),
                                                                                      status_code.name,
                                                                                      status_code.value))
                    raise FunctionError("Server Connection status : {}".format(rpc_err.details()))
                else:
                    log.info("Response received from the server : {}".format(response_received_tmp))
            else:
                raise NotImplementedError(
                    "Not Implemented these {} communication types ".format(_grpc_communication_type))

            # Attempting to convert received data into JSON object
            try:
                if isinstance(response_received_tmp, dict):
                    response_received = response_received_tmp
                else:
                    response_received = json.loads(response_received_tmp)
                log.debug("The Received Data is Converted into JSON Object : {}".format(response_received))
            except Exception as e:
                try:
                    response_received = MessageToDict(response_received_tmp)
                except Exception as e:
                    log.debug("The Received data is not converted into JSON Object {}".format(e))
                    response_received = str(response_received_tmp)

            results = {
                "content": response_received,
                "channel": grpc_channel
            }

            yield StatusMessage("Received Data from gRPC Server...!")
            log.debug("RESULTS: %s", results)
            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
