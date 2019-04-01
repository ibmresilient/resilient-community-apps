# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import json
from google.protobuf.json_format import MessageToDict
from fn_grpc_interface.util.grpc_helper import *
import logging
import six
import re

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

    @function("function_grpc")
    def _function_grpc_function(self, event, *args, **kwargs):
        """Function: A function to communicate with GRPC Servers based on the Communication Methods Specified."""

        try:
            # Initialising grpc helper class
            grpc_helper_obj = GrpcHelperClass(logger_object=log)

            # Get the function parameters:
            grpc_channel = kwargs.get("grpc_channel")  # text
            grpc_function = kwargs.get("grpc_function")  # text
            grpc_function_data = kwargs.get("grpc_function_data")  # text

            log.info("grpc_channel: %s", grpc_channel)
            log.info("grpc_function: %s", grpc_function)
            log.info("grpc_function_data: %s", grpc_function_data)

            yield StatusMessage("Connecting to gRPC Server...!")

            # Parsing the variable data from config file and resilient inputs

            # validate the gRPC Function Parameter to make sure data in this `helloworld:SayHello(HelloRequest)`
            match_found = re.match(r'\w+\:\w+\(\w+\)$', grpc_function, re.IGNORECASE)
            if match_found:
                log.info("gRPC Function input parameter 'grpc_function' data is validated.")
            else:
                raise ValueError(
                    "Please provide gRPC input parameter 'grpc_function' data correctly in resilient input section")
            try:
                _grpc_package_name = grpc_function.split(':')[0].strip()
                _grpc_rpc_stub_method_name = grpc_function.split(':')[1].split("(")[0].strip()
                _grpc_request_method_name = re.sub("\)", '', grpc_function.split(':')[1].split("(")[1])
                _grpc_request_method_name = _grpc_request_method_name.strip()
            except Exception as err:
                raise ValueError("failed to parse the function parameters.{0}".format(err))

            # Parsing the service configuration data
            service_config_data = self.options.get(_grpc_package_name)
            if not service_config_data:
                raise ValueError(
                    "Configuration parameter not found in Resilient configuration file for service : {0}".format(
                        _grpc_package_name))
            else:
                try:
                    config_file_data = service_config_data.split(',')
                    _grpc_secure_connection = config_file_data[1]
                    _grpc_communication_type = config_file_data[0]
                    _grpc_google_tocken = config_file_data[2]
                    _grpc_certificate_path = config_file_data[2]
                except Exception:
                    raise ValueError("Failed to parse service {0} config params,"\
                    "please define in the correct format in Resilient config file.".format(_grpc_package_name))

            _grpc_interface_file_dir = self.options.get('interface_dir')
            if not _grpc_interface_file_dir:
                raise ValueError("Interface directory not found in Resilient config file.")

            log.info("gRPC Package Name : {} gRPC Stub Method Name : {} gRPC Request Class Name : {}" \
                     .format(_grpc_package_name, _grpc_rpc_stub_method_name, _grpc_request_method_name))


            # Importing gRPC proto buff files from the given interface directory.
            try:
                module_files = grpc_helper_obj.get_interface_file_names(_grpc_interface_file_dir, _grpc_package_name)

                # Removing __pycache__ directory from module list since it's not required
                if "__pycache__" in module_files:
                    pycache_index = module_files.index("__pycache__")
                    module_files.pop(pycache_index)

                if not module_files:
                    raise ValueError(
                        "Interface gRPC proto buff Files not Found.please copy the files in the interface directory")
                else:
                    for file_name in module_files:
                        if file_name.endswith('.py'):
                            if file_name.find('pb') == -1:
                                raise ValueError("Interface gRPC proto buff Files Error Please Copy Correct Files.")
                        else:
                            raise ValueError("Interface gRPC proto buff Files Error Please Copy Correct Files.")

                grpc_interface_module_list = grpc_helper_obj.get_grpc_interface_module(module_files,
                                                                                       _grpc_interface_file_dir,
                                                                                       _grpc_package_name)
                log.debug(grpc_interface_module_list)

                grpc_stub_tuple = grpc_helper_obj.get_grpc_class(grpc_interface_module_list, 'stub')
                if not grpc_stub_tuple:
                    raise ValueError("gRPC Interface Buffer pb2 files error not found any stub objects")

                grpc_request_tuple = grpc_helper_obj.get_grpc_class(grpc_interface_module_list,
                                                                    _grpc_request_method_name.lower())
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
                    stub_class_obj, grpc_channel_obj = grpc_helper_obj.gRPC_Connect_Server(_grpc_secure_connection,
                                                                                           grpc_channel,
                                                                                           grpc_stub_tuple[1],
                                                                                           _grpc_certificate_path)
                    stub_method = grpc_helper_obj.get_method_from_stub_object(stub_class_obj, _grpc_communication_type,
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
