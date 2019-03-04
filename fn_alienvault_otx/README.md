
#About This Package

This Alien Vault OTX function is RESTful Web service API providing a way to search for threat intelligence information from the Alien Vault database.
   Threat intelligence indicators information can be searched for IP Address, Domain, Host Name, File Hashes, URL, CVE.
 
   For more information on alien vault OTX : https://otx.alienvault.com/api
    
#Prerequisites:

* resilient version 31 or later
* resilient_circuits version 30 or later
* Account in alien vault OTX : https://otx.alienvault.com/
* DirectConnect OTX API Key from Alien Vault

#Resilient Installation

This package requires that it is installed on a RHEL or CentOS platform and uses the resilient-circuits framework.
Install this package with 'pip', such as:
    
 To install Package 

    pip install fn_alienvault_otx/
    
 The .tar.gz file can be installed using

    pip install fn_alienvault_otx-<version>.tar.gz
        
To import the function and example rule and workflows into Resilient, run the following command:

    resilient-circuits customize
    
 Reply to the prompt for package import. 

To uninstall,

    pip uninstall fn_alienvault_otx
 
#Resilient Configuration

Run the following command to generate the alien vault configuration section in the app.config file:

    resilient-circuits config [-u | -c]     

The following gRPC configuration data is added:
                    
    [fn_alienvault_otx]
    # OTX API Key to Access the Alien Vault OTX Service 
    av_api_key=<<DirectConnect OTX API Key>>
    #Base URL Path of Alien Vault OTX
    av_base_url=https://otx.alienvault.com/api/v1
    # Proxy Server by Default it will be None
    proxy=None

Edit the [fn_alienvault_otx] properties as follows:
    
   1. av_api_key : Alien vault OTX DirectConnect API Key.
    
After installation & configuration, the package will be loaded by `resilient-circuits run`.
  
#Using the Alien Vault OTX Function
    
  The Alien Vault Function can be called on artifact like IP Address, DNS Name, System Name, URL, URL Referer, 
  Hashes, Threat CVE ID.
  after calling function from artifact we needs to choose `Section` based on the artifact. for more info on section 
  please refer on link : https://otx.alienvault.com/api
  
##Function Payload Data Format
  The Payload from the function will be always in the JSON format sample out format is given.
  Basically `api_call` key is used to segregate the data.
  
    {
       "content": API Response Data
    }
    
##Function Post-Process Script
 It can be parsed within the post-process script as `results.get("content")`.
 by default Alien Vault function data is displayed on incident Notes. 



