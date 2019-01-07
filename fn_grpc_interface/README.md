#About gRPC

The gRPC component provides a general wrapper for the gRPC client application and can call methods on
    a server application on a different machine as if it was a local object, making it easier for you 
    to create distributed applications and services with IBM resilient.
    In this edition we have implemented only simple RPC gRPC Service method.

For more details - https://grpc.io/docs/

#Resilient Configuration

Follow the steps to add a gRPC section to your app.config file and updating the fields:
    
Run the following command to generate the gRPC data in the app.config file

    resilient-circuits config [-u | -c]  
    
After running config command data should be generated in the app.config file as below
    
    [fn_grpc]
    interface_dir = <<path to interface buffer pb2 files parent directory>>
    #<<package_name=communication_type,secure connection type,certificate_path or google API token>>
    #helloword=unary,None,None
    #Note : create a folder same as package name, and copy the interface buffer pb2 files inside the directory.
    #config data settings details as follows :
    #       package_Name(gRPC package name) = communication type(i.e gRPC client-server communication type 
    #       example - unary(Simple RPC),server_stream(response-streaming RPC),client_stream(request-streaming RPC),
    #       bidirectional_stream(bidirectionally-streaming RPC)),secure connection type(i.e None,TLS,SSL,OAuth2),
    #       certificate_path or google API token(i.e None,path to certificate/token).
    #       for more info on gRPC communication types : https://grpc.io/docs/tutorials/basic/python.html 
    
Please edit the app.config file as per you application configurations, instruction to update the app.config files are given below.
  
  1.    interface_dir  :  please specify the parent directory path of buffer pb2 files, generated from grpc-tools according
        to your *.proto file.
        
        example : /usr/local/sys_name/helloword/helloworld_pb2.py then,
        interface_dir = /usr/local/sys_name/
        
  2.    package_name = communication type,secure connection,certificate/google token
        
        Create the folder name as package name under the interface directory and keep both interface buffer pb2 files 
        inside this directory and this is must.
        
        communication type : this value can be - unary/server_stream/client_stream/bidirectional_stream
        
        gRPC client-server communication type example - unary(Simple RPC)/server_stream(response-streaming RPC)/
        client_stream(request-streaming RPC)/bidirectional_stream(bidirectionally-streaming RPC))
        https://grpc.io/docs/tutorials/basic/python.html
        
        secure connection : this value can be None/TLS/SSL/OAuth2
        
        certificate/google token : if the secure connection type is other than the None, needs to specify either path to 
        certificate file or token from google
        
#using gRPC Function

This component supports only Simple RPC(unary) communication mechanism.
Sample Hello word gRPC example - https://grpc.io/docs/quickstart/python.html
Below is details of Input and outputs of the API

Resilient Inputs :
  1. grpc_channel : localhost:50051 - This is the channel information hostname:port where server 
                    application is running.
  2. grpc_function: helloword:SayHello(HelloRequest) - this should be package_name:rpc function name(rpc request function name).
                    for better understanding compare example data with sample helloword program.
                    
      sample gRPC helloword program
      proto : https://github.com/grpc/grpc/blob/master/examples/protos/helloworld.proto
      gRPC Application : https://github.com/grpc/grpc/tree/master/examples/python
  3. grpc_function_data: This can any artifact value example string,IP Address, DNS name etc
  
#Resilient Pre-Process Script Configuration
    example  Pre-Process Script: 
    dict_data = {"name":str(artifact.value)}
    inputs.grpc_function_data = str(dict_data)
    
   we need to create the json object from the artifact value,here in the above example we have created one key-value 
   pair json object. key is "name" and value will be str(artifact.value).
   
   json object key "name" refers to name of the input parameter specified in the proto file server request method 
   to send the data to gRPC server.
   
   if more than one parameter is specified in the request method,then json object should also be included with those 
   parameters.
    
   compare this proto : https://github.com/grpc/grpc/blob/master/examples/protos/helloworld.proto file with the 
   above "name" parameter for better understanding of function input data parameters.
   
   
To generate resilient code for the function integration

    resilient-circuits codegen -p fn_grpc_interface [-f function_grpc] [-w ]



To install in "development mode"

    pip install -e ./fn_grpc_interface/

After installation, the package will be loaded by `resilient-circuits run`.


To uninstall,

    pip uninstall fn_grpc_interface


To package for distribution,

    python ./fn_grpc_interface/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz
