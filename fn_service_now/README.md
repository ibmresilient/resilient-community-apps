# IBM Security QRadar SOAR App for ServiceNow

- [Release Notes](#release-notes)
- [Overview](#overview)
- [Key Features](#key-features)
- [Requirements](#requirements)
- [Install](#install)
- [Customize](#customize)
- [Documentation](#documentation)

---
## Release Notes
<!--
  Specify all changes in this release. Do not remove the release 
  notes of a previous release
-->

### v2.0.9
* Support added for ServiceNow Security Incident Response (SIR)
* Support added for API Key authentication from ServiceNow to IBM SOAR
* AppHost support for proxies
* App renamed to IBM Security QRadar SOAR App for ServiceNow
* Verified on ServiceNow San Diego release

### v1.0.5
* Verified on ServiceNow Quebec release

### v1.0.4
* Verified on ServiceNow Paris release

### v1.0.3
* Verified on ServiceNow Orlando release
* Support added for SOAR AppHost

### v1.0.2
* Verified on ServiceNow New York release

### v1.0.1
* Verified on ServiceNow Madrid release

### v1.0.0
* Initial release

---

## Overview
Bi-directional app with ServiceNow and IBM Security QRadar SOAR allows SEC Ops Professionals to communicate security incidents in realtime. The app allows for bi-directional synchronization of Incidents/Cases, Tasks, Notes and Attachments, which enables the security and operations teams to be aligned during critical security events.

---

## Key Features
* Bi-directional app between records in the ServiceNow Incident Table and Incidents and Tasks in the SOAR platform.
* Bi-directional app between records in the ServiceNow Security Incident table and Security Incident Response Task table with Incidents and Tasks in the SOAR platform.
* Create a SOAR Incident or Task from a ServiceNow Record in the Incident or Security Incident Table.
* Create a ServiceNow Record in the Incident or Security Incident Table from a SOAR Incident or Task.
* Sync notes between a related SOAR Incident or Task and a ServiceNow Record.
* Send Attachments from a SOAR Incident or Task to a related ServiceNow Record.

---

## Requirements
* ServiceNow Instance with ITSM enabled and running `Kingston`, or newer releases
* Access to the **Incident Table** in ServiceNow
* ServiceNow `IBM SOAR App >= v1.0.0` installed on your ServiceNow Instance which you can download from [the ServiceNow Store](http://ibm.biz/get-ibm-resilient-service-now-app)
  * If integrating with ServiceNow Security Incident Table (SIR), `IBM SOAR App >= 2.0.9` and ServiceNow Security Incident Response with its dependencies are required. More information [here](https://www.servicenow.com/products/security-incident-response.html).
* If IBM SOAR is not publicly accessible (behind a firewall), a ServiceNow MID Server is required. See the [Install Guide](./docs/install_guide) for more information
* IBM Cloud Pak for Security `>= 1.6.0` *or* IBM SOAR `>= v41.2.0`
* App Host `>= v1.5.0` (recommended) *or* an Integrations Server running `resilient-circuits >= v42.0.0`.
  - `fn_service_now >= v1.0.0` installed, which you can download from our [App Exchange](http://ibm.biz/get-ibm-resilient-service-now-integration)
  - If integrating with SIR, `fn_service_now >= v2.0.9` is required

---

## Install
Follow our [Install Guide](./docs/install_guide) to get up and running. 

---

## Customize
The default configuration satisfies the requirements for a number of use cases. To adapt the app for your specific requirements, see these customization guides:
- [Customize ServiceNow App Guide](./docs/customize_snow_guide)
- [Customize SOAR Functions Guide](./docs/customize_resilient_guide)

---

## Documentation
* See [ibm.biz/res-snow-docs](http://ibm.biz/res-snow-docs) for our latest documentation

---