# Resilient Function for Splunk integration

## Description

This function package provides the following features to be used in a workflow:

1. Execute a given Splunk or Splunk ES search/query
2. Update a Splunk ES notable event
3. Add a new threat intelligence item to the collections of Splunk ES
4. Delete a threat intelligence item

## System Requirements
- Resilient Server version 30 or later
- Splunk version 7.0 or later, or Splunk Cloud
- Splunk ES 4.7.2 or later, or Splunk ES Cloud
- Ability to connect to Resilient server with HTTPS on port 443 and 65001
- Ability to connect to Splunk server with HTTPS on port 8089

## Package Dependences
- python requests
- Splunk SDK
- resilient_circuits version 30 or later

## Installation
Install this package with 'pip', or run `python setup.py install`

## Setup
Create app.config by running `resilient-circuits config -u`.

The app.config needs the following configuration values:  

[resilient]  
host = resilient-server-hostname-or-ip-address  
org = organization-to-use  
email = resilient-login-email  
password = resilient-login-password-or-use-keyrings  
port = resilient-server-port  
loglevel = DEBUG-or-INFO  
cafile = false-for-skipping-cert-verification  
componentsdir = path-to-the-components-folder-of-this-package  
splunkpassword =s plunk-password-or-use-keyrings
[splunk_integration]  
host = splunk-server-hostname-or-ip-address  
port = 8089-or-splunk-port-for-REST-api  
username = splunk-login-user-name  



## Start
Start this function app with: `resilient-circuits run`

## Customize
Run with: `resilient-circuits customize` to install function definitions and sample workflows to the Resilient server.

## Samples
Please refer to the installation doc for more details about sample searches and workflows included in this package.

## Uninstall
Run with `pip uninstall fn_splunk_integration`

