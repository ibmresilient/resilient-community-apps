# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

"""Generate a default configuration-file section for fn_grpc_interface"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_grpc]
#interface_dir = <<path to interface buffer pb2 files parent directory>>
#<<package_name=communication_type,secure connection type,certificate_path or google API token>>
interface_dir = /home/neetin/gRPC_Project/
helloword=unary,SSL/TLS,/home/neetin/self_signed_certificate/certificate.pem
calculator=unary,None,None

#Note : create a folder same as package name, and copy the interface buffer pb2 files inside the directory.
#config data settings details as follows :
#       package_Name(gRPC package name) = communication type(i.e gRPC client-server communication type 
#       example - unary(Simple RPC),server_stream(response-streaming RPC),client_stream(request-streaming RPC),
#       bidirectional_stream(bidirectionally-streaming RPC)),secure connection type(i.e None,SSL/TLS,OAuth2),
#       certificate_path or google API token(i.e None,path to certificate/token).
#       for more info on gRPC communication types : https://grpc.io/docs/tutorials/basic/python.html
     """
    return config_data