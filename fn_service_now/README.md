# IBM Resilient Integration for ServiceNow

- [Overview](#overview)
- [Key Features](#key-features)
- [Requirements](#requirements)
- [Install](#install)
- [Customize](#customize)
- [Documentation](#documentation)

---

## Overview
Bi-directional integration with ServiceNow and IBM Resilient allowing SEC Ops Professionals to communicate security incidents in realtime. This integration allows for bi-directional synchronization of Incidents, Tasks, Notes and Attachments enabling the security and operations teams to be aligned during critical security events.

---

## Key Features
* Bi-directional integration between Records in the ServiceNow Incident Table and Incidents and Tasks in the IBM Resilient platform.
* Create a Resilient Incident or Task from a ServiceNow Record in the Incident Table.
* Create a ServiceNow Record in the Incident Table from a Resilient Incident or Task.
* Sync notes between a related Resilient Incident or Task and a ServiceNow Record.
* Send Attachments from a Resilient Incident or Task to a related ServiceNow Record.

---

## Requirements
* ServiceNow Instance with ITSM enabled and running a `Kingston`, `London` or `Madrid` release
* The ServiceNow `IBM Resilient App >= v1.0.0` installed on your ServiceNow Instance which you can download from [the ServiceNow Store](http://ibm.biz/get-ibm-resilient-service-now-app)
* Access to the **Incident Table** in ServiceNow
* If IBM Resilient is not publicly accessible (behind firewall) a ServiceNow MID Server is required
* IBM Resilient >= `v31.0.0`
* An Integrations Server running `resilient-circuits >= v31.0.0` with `fn_service_now >= v1.0.0` installed which you can download from our [App Exchange](http://ibm.biz/get-ibm-resilient-service-now-integration)

---

## Install
* Follow our [Install Guide](./docs/install_guide) to get up and running. 

---

## Customize
* Out-of-the-box we meet a lot of use cases, however to adapt the Integration to suit your Incident Response Workflow follow our Customize guides:
  - [Customize ServiceNow App Guide](./docs/customize_snow_guide)
  - [Customize Resilient Functions Guide](./docs/customize_resilient_guide)

---

## Documentation
* See [ibm.biz/res-snow-docs](http://ibm.biz/res-snow-docs) for our latest documentation

---