# IBM Resilient Integration for ServiceNow

## Documentation
  - [Overview](#overview)
  - [Install Guide](./docs/install_guide)
  - [Customize ServiceNow App Guide](./docs/customize_snow_guide)
  - [Customize Resilient Functions Guide](./docs/customize_resilient_guide)

## Overview
In order to integrate with ServiceNow, two components are required **fn_service_now** and the **IBM Resilient ServiceNow App** to be installed on your Resilient Integrations Server and ServiceNow Instance, respectively

### fn_service_now:
* This is what we are familiar with, a Python package
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

