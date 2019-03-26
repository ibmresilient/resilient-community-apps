# IBM Resilient Integration for ServiceNow

## Documentation
  - [Overview](#overview)
  - [Current Limitations](#current-limitations)
  - [Install Guide](./docs/install_guide)
  - [Customize ServiceNow App Guide](./docs/customize_snow_guide)
  - [Customize Resilient Functions Guide](./docs/customize_resilient_guide)

## Overview
Bi-directional integration with ServiceNow and IBM Resilient allowing SEC Ops Professionals to communicate security incidents in realtime. This integration allows for bi-directional synchronization of notes and incidents enabling the security and operations teams to be aligned during critical security events.

## Key Features
* Bi-directional integration between Records in the ServiceNow Incident Table and Incidents/Tasks in IBM Resilient
* Create an IBM Resilient Incident/Task from a ServiceNow Record in the Incident Table
* Create a ServiceNow Record in the Incident Table from a IBM Resilient Incident/Task
* Sync notes between a related IBM Resilient Incident/Task and a ServiceNow Record
* Send Attachments from an IBM Resilient Incident/Task to a related ServiceNow Record

## Requirements
* ServiceNow Instance running >= Kingston release
* The ServiceNow `IBM Resilient App >= v1.0.0` installed on your ServiceNow Instance
* Access to the Incident Table in ServiceNow
* If IBM Resilient is not publicly accessible (behind firewall) a ServiceNow MID Server is required
* IBM Resilient >= `v31.0.0`
* An Integrations Server running `resilient-circuits >= v31.0.0` with `fn_service_now >= v1.0.0` installed

### fn_service_now:
* Hosted on our public GitHub and Community App Exchange
* You download, install and run it on your Resilient Integrations Server
* The package includes *customizations* that are imported into your Resilient Appliance using the `resilient-circuits customize` command

### IBM Resilient ServiceNow App:
* This is new
* Currently hosted on GitHub
* Will be available on the ServiceNow App Store in the future
* You download and install it on your ServiceNow instance

Both components work in conjunction with each other and allow for a **bi-directional Integration** that gives you the ability to create Incidents in Resilient from ServiceNow Records and Records in ServiceNow from Resilient Incidents - and MUCH more...

Follow our [Install Guide](./docs/install_guide) to get up and running. Then using our customization guides (links above), adapt the Integration to suit your Incident Response Workflow

## Current Limitations:
While we put our IBM Resilient ServiceNow App through the ServiceNow Certification process, this Integration has some current limitations:

* The current ServiceNow App is **pre-certified** which really means that we have a ServiceNow App developed, but not hosted on the ServiceNow App Store.
* In order to distribute the App, we host it on a Public GitHub Repository. 
* To install the App the ServiceNow admin must get the App from GitHub. 
* The limitations are:
  * There is no 'clean' way to update the App once installed. 
  * If the ServiceNow admin pulls in the latest version of the ServiceNow App from GitHub, the Integration will break as **all 'references' between ServiceNow Records and Resilient Incidents/Tasks will be deleted**. Once we have it 'certified' and on the ServiceNow App Store the update process will be more seamless and this will not be an issue.

