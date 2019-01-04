# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_grpc_interface"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_grpc]
     #package_Name = communication type(i.e unary,server_stream,client_stream,bidirection_stream),secure connection type(i.e None,TLS,SSL,OAuth2),certificate_path or google API Tocken,Interface pb2 files parent directory
helloword=unary,None,None
interface_dir = /home/neetin/gRPC_Project/
calculator=unary,None,None
     """
    return config_data