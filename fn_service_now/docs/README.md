# Installation Guide

## Step 1: *Create User in Resilient*
* Name: SNOW Integration
* Email: snow_integration@example.com
* On the Resilient Appliance, run:
  ```
  $ sudo resutil newuser -org "<org-name>" -email snow_integration@example.com -first "SNOW" -last "Integration"
  ```
--- 

## Step 2: *Create User in ServiceNow*
* Name: IBM Resilient
* User ID: ibmresilient
* Email: integrations@example.com
  >**NOTE:** use the same email address as the Resilient Orchestration Engine which is used in your in app.config file
--- 

## Step 3: *Download & Install fn_service_now Integration*
* Copy the package to your Integrations Service
* Install the package:
  ```
  $ pip install fn_service_now-1.0.0.tar.gz
  ```
* Update your app.config file:
  ```
  $ resilient-circuits config -u
  ```
* Open the config file and edit your ServiceNow credentials with the user you created above:
  ```
  $ nano ~/.resilient/app.config
  ```
* Import the package's customizations into Resilient:
  ```
  $ resilient-circuits customize
  ```
* Run resilient-circuits
  ```
  $ resilient-circuts run
  ```
--- 

## Step 4: *Get Resilient-ServiceNow App from Git*
**NOTE: this is temporary and will be replaced by an App on the ServiceNow App Store**
* To import the app from git, follow [these](https://docs.servicenow.com/bundle/london-application-development/page/build/applications/task/t_ImportAppFromSourceControl.html) instructions on your ServiceNow Instance
* The ServiceNow git repository is: https://gitlab.com/Curtin/service-now-resilient-app.git
--- 

## Step 5: *Input your Resilient Credentials in ServiceNow*
* Go to the ServiceNow Studio
* Click the IBM Resilient App
* On the left, click System Properties
* Enter details for:
  * Resilient Host:
  * Resilient Org Name:
  * Resilient User Email:
  * Resilient User Password
  * ServiceNow Username:
--- 

## Step 6: *Setup Mid Server (if needed)*
* A ServiceNow Mid-Server is needed if your Resilient Instance is not on a public network
* The ServiceNow Mid-Server must be setup on the network as your Resilient Instance
* The Resilient Host Address you input in the previous step must be relevant to your Mid Server
* To install, type mid-server into your ServiceNow search box and click Installation Instructions
--- 

