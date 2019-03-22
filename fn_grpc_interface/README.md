# gRPC Function for IBM Resilient

# Table of Contents  
 - [About This Package](#about-this-package)
 - [Prerequisites](#prerequisites)
 - [Installation](#installation)
 - [Data Table](#data-table)
 - [Function Inputs](#function-inputs)
 - [Function Output](#function-output)
 - [Pre-Process Script](#pre-process-script)
 - [Post-Process Script](#post-process-script)
 - [Rules](#rules)
 ---
 
## About this Package 
  
This gRPC function provides a general purpose wrapper for use with any gRPC client application. It can be used for request/response style communication during incident response management such as   
  
* artifact enrichment  
* enterprise containment actions  
* communication and coordination with other enterprise solutions  
  
In this edition we have implemented the `unary` communication type service method.  
  
For more information on [gRPC](https://grpc.io/docs/)  
  
![screenshot](./screenshots/1.png)

## Prerequisites:  
  
* Resilient Appliance >= v31.0.0
* Integrations Server running resilient_circuits >= v30.0.0
* grpcio version >=v1.19.0 
  
## Installation 
This package requires that it is installed on a RHEL or CentOS platform and uses the resilient-circuits framework.  
Install this package with 'pip', such as:  
  
`pip install fn-grpc-<version>.tar.gz`  
  
To import the function and example rule and workflows into Resilient, run the following command:  
  
`resilient-circuits customize -y -l fn-grpc-interface`  
  
Answer the prompts for the package to import.  
  
To uninstall,  
  
 pip uninstall fn_grpc_interface  
  
#Resilient Configuration  
  Run the following command to generate the gRPC configuration section in the app.config file:  
  
 resilient-circuits config [-u | -c] The following gRPC configuration data is added:  
     
 [fn_grpc] interface_dir = <<path to interface buffer pb2 files parent directory>> #<<package_name=communication_type,secure connection type,certificate_path or google API token>> #helloword=unary,None,None #Note : create a folder same as package name, and copy the interface buffer pb2 files inside the directory. #config data settings details as follows : #       package_Name(gRPC package name) = communication type(i.e gRPC client-server communication type    #       example - unary(Simple RPC),server_stream(response-streaming RPC),client_stream(request-streaming RPC),  
 #       bidirectional_stream(bidirectionally-streaming RPC)),secure connection type(i.e None,TLS,SSL,OAuth2), #       certificate_path or google API token(i.e None,path to certificate/token). #       for more info on gRPC communication types : https://grpc.io/docs/tutorials/basic/python.html Edit the [fn_grpc] properties as follows:  
    
 1. interface_dir:  the parent directory containing the gRPC client (pb2) files. These files are auto-generated from your .proto file via the grpc-tools utility  
          
        Ex. interface_dir = /usr/local/grpc_clients/  
          
 2. package_name: communication type,secure connection,certificate/google token  
          
        Create a separate line for each client application to enable for Resilient.  
  
       Ex. helloworld = unary,SSL,/usr/local/grpc_clients/helloworld/helloworld.crt  
          
        Within interface_dir, create a folder matching package_name where the client pb2   
        files will reside.  
          
 a. communication type: this value can be - unary, server_stream, client_stream, or bidirectional_stream. Presently, only `unary` is supported.         For further information, refer to https://grpc.io/docs/tutorials/basic/python.html  
       b. secure connection: this value can be None, SSL/TLS, OAuth2. Presently only None, SSL/TLS are supported.  
       c. certificate/google token: if the secure connection type is other than the None, specify either a path to the certificate file or token provided from google.  
  #Using the gRPC Function  
Below are details of the input fields and outputs results of the function.  
  
##Function Inputs Fields:  
  
 1. grpc_channel: *hostname:port* Ex. localhost:50051   
       
     This is the channel information where the gRPC server application is running.  
 2. grpc_function: *package_name:rpc function name(rpc request)* Ex. helloword:SayHello(HelloRequest)   
  
     This information is derived from the .proto file similar to the following example:  
       
     ```  
 package helloworld;  
 // The greeting service definition. service Greeter { // Sends a greeting rpc SayHello (HelloRequest) returns (HelloReply) {} } ``` 3. grpc\_function\_data: Ex. '{ "name": "128.23.43.56" }'   
       
     This will contain string formatted json containing artifact data and additional parameters required by the gRPC function call.  
       
##Function Pre-Process Script  
  
A pre-processor script will build and format the grpc\_function\_data input field similar to this example:  
  
      
 dict_data = {"name": str(artifact.value)} inputs.grpc_function_data = str(dict_data)      
 "name" refers to name of the input parameter specified in the .proto file request message as in this example:  
     
 ``` // The request message containing the user's name. message HelloRequest { string name = 1; } ```  If more than one parameter is specified in the request message, then the pre-process script's json object should also include those parameters.  
      
##Function Payload Data Format  
The payload from integration will wrap the results of the gRPC server response in the following JSON structure.  
An attempt is made to return `response_recieved` as a dictionary if the response is actually a string representation of JSON or a nature dictionary object.   
Otherwise, `response_recieved` will be returned as a string representation of the result.  
  
 { "content": response_received, "channel": grpc_channel }  
  
##Function Post-Process Script  
If `response_received` is in JSON or dictionary format, it can be parsed within the post-process script as `results.content.get("<key>")`. Otherwise, the result will be in string format.   
  
The sample helloword gRPC example can be found at `https://grpc.io/docs/quickstart/python.html`.