# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-grpc-interface
    resilient-circuits selftest --print-env -l fn-grpc-interface

Return examples:
    return {
        "state": "success",
        "reason": "Successful connection to third party endpoint"
    }

    return {
        "state": "failure",
        "reason": "Failed to connect to third party endpoint"
    }
"""

import logging
import grpc

from fn_grpc_interface.util.grpc_helper import GrpcHelperClass

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_grpc_interface", {})

    try:
        grpc_helper_obj = GrpcHelperClass(logger_object=log)

        package_names, _grpc_interface_file_dir, _grpc_channel = _check_config_data(app_configs)
        _check_files(grpc_helper_obj, _grpc_interface_file_dir, package_names)
        _check_connection(_grpc_channel)
    except Exception as e:
        return {
            "state": "failure",
            "reason": str(e)
        }
        
    return { "state": "success" }


def _check_config_data(app_configs):
    # Parsing the service configuration data

    try:
        _grpc_interface_file_dir = app_configs.pop("interface_dir")
    except Exception as e:
        raise ValueError("'interface_dir' is not defined in the app.config file")

    try:
        _grpc_channel = app_configs.pop("grpc_channel")
    except Exception as e:
        log.info("No grpc_channel config found. Make sure you enter the channel info when invoking the grpc function.")

    if len(app_configs) == 0:
        raise ValueError("No configurations found in the app.config file")

    for _grpc_package_name in app_configs:
        service_config_data = app_configs.get(_grpc_package_name)
        
        try:
            # check in correct csv format
            config_file_data = service_config_data.split(',')
            _grpc_secure_connection = config_file_data[1]
            _grpc_communication_type = config_file_data[0]
            _grpc_certificate_path = config_file_data[2]
        except Exception:
            raise ValueError("""Failed to parse the configurations for '{0}' in the app.config file. Ensure it is in the correct CSV format. e.g. {0}=unary,None,None""".format(_grpc_package_name))

    return app_configs.keys(), _grpc_interface_file_dir, _grpc_channel

def _check_files(grpc_helper_obj, _grpc_interface_file_dir, package_names):
    for _grpc_package_name in package_names:
        module_files = grpc_helper_obj.get_interface_file_names(_grpc_interface_file_dir, _grpc_package_name)

        # Removing __pycache__ directory from module list since it's not required
        if "__pycache__" in module_files:
            pycache_index = module_files.index("__pycache__")
            module_files.pop(pycache_index)

        if not module_files:
            raise ValueError("No gRPC protocol buffer files found in your interface_dir for the service '{0}'. Please copy the {0}_pb2.py and {0}_pb2_grpc.py files to your interface_dir".format(_grpc_package_name))
        else:
            for file_name in module_files:
                if not (file_name.endswith('.py') or file_name.endswith('.pyc')) and 'pb' not in file_name:
                    raise ValueError("Invalid file '{0}' found in your interface_dir for the service '{1}'.Please only copy the {1}_pb2.py and {1}_pb2_grpc.py files to your interface_dir".format(file_name, _grpc_package_name))

def _check_connection(channel):
    if channel:
        try:
            channel_object = grpc.insecure_channel(channel)
        except Exception as e:
            raise ValueError("Given channel '{0}' failed to connect. Make sure 'grpc_channel' details are correct.")
