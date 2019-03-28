# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
import os
import sys
import six
import logging
import inspect
import grpc

try:
    # PY3
    import importlib.util
except ImportError as e:
    # PY2
    logging.debug("The Import Error raised for the module importlib trying with imp module : {}".format(e))
    import imp


class GrpcHelperClass(object):
    def __init__(self, logger_object):
        self.log_object = logger_object

    def get_grpc_interface_module(self, interface_files=[], base_dir=None, files_dir=None):
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
            self.log_object.info("Loading The Modules : {}".format(interface_files))

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
                        self.log_object.debug("No python modules found to import.")
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
            self.log_object.debug("No Interface file found, please specify the interface file")
            return None

    def get_grpc_class(self, grpc_module_list, class_name):
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
                self.log_object.debug("Class Name : {} Object : {}".format(name, obj))
                if name.lower().find(class_name.lower()) != -1:
                    return name, obj
        else:
            return ()

    def gRPC_Connect_Server(self, auth_type=None, channel=None, stub_class=None, certificate_path=None):
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
            self.log_object.info("gRPC Channel Connection is not secure.")
            channel_object = grpc.insecure_channel(channel)
            stub_class_obj = stub_class(channel_object)
            return stub_class_obj, channel_object
        elif auth_type.lower().strip().find('ssl') != -1 or auth_type.lower().strip().find('tls') != -1:
            self.log_object.info("Channel Authentication is secure : {0}".format(auth_type))
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

    @staticmethod
    def get_interface_file_names(base_dir=None, files_dir=None):
        """
        component that return the absolute path of all files in the given directory
        :param base_dir:  interface pb2 files parent directory
        :param files_dir:  interface pb2 files directory i.e same as package name
        :return: lists of all pb2 files absolute path inside the given directory path
        """
        __dir_path = os.path.join(base_dir, files_dir)
        return os.listdir(__dir_path)

    def get_method_from_stub_object(self, stub_object, comm_type, stub_name=''):
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
                    self.log_object.debug("found Stub name : {} and object : {}".format(name, obj))
                    _found_stub_name = name
                    _found_stub_object = obj

        return _found_stub_name, _found_stub_object
