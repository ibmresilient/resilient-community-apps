# Resilient Function for Splunk integration

## Description

This function package provides the following features to be used in a workflow:

1. Add a new threat intelligence item to the collections of Splunk ES
2. Delete a threat intelligence item
3. Execute a given Splunk or Splunk ES search/query
4. Update a Splunk ES notable event

## System Requirements
- Resilient Server version 35 or later
- Splunk version 7.0 or later, or Splunk Cloud
- Splunk ES 4.7.2 or later, or Splunk ES Cloud
- Ability to connect to Resilient server with HTTPS on port 443 and 65001
- Ability to connect to Splunk server with HTTPS on port 8089

## Package Dependencies
- python requests
- resilient-lib
- Splunk SDK
- resilient_circuits version 30 or later

### App Host Installation
All the components for running this integration in a container already exist when using the App Host app.

To install,

* Navigate to Administrative Settings and then the Apps tab.
* Click the Install button and select the downloaded file: app-fn_splunk-integration-x.x.x.zip.
* Go to the Configuration tab and edit the app.config file, editing the URL and access credentials for Splunk.

## Integration Server Installation
* Download the `app-fn_splunk-integration-x.x.x.zip` file.
* Copy the `.zip` to your Integration Server and SSH into it.
* Unzip the package:
  ```
  $ unzip app-fn_splunk-integration-x.x.x.zip
  ```
* Install the package:
  ```
  $ pip install fn_splunk-integration-x.x.x.tar.gz
  
### Setup
Create app.config by running `resilient-circuits config -c -l fn-splunk-integration` or `resilient-circuits config -u -l fn-splunk-integration` .

The app.config needs the following configuration values, in addition to the appropriate [resilient] section for connecting to your Resilient platform:  

```
[fn_splunk_integration]  
host = splunk-server-hostname-or-ip-address  
port = 8089-or-splunk-port-for-REST-api  
username = splunk-login-user-name 
splunkpassword = splunk-password-keyring-protection-recommended
verify_cert = [true, false] for verify https certtificate or not
```
### Customize
Run with: `resilient-circuits customize -l fn-splunk-integration` to install function definitions and sample workflows to the Resilient server.

### Start
Start this function app with: `resilient-circuits run`

### Samples
Please refer to the installation doc for more details about sample searches and workflows included in this package.

### Uninstall
Run with `pip uninstall fn-splunk-integration`

