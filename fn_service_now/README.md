# ServiceNow

```{toctree}
:maxdepth: 1
:hidden:

docs/install_guide/README
docs/customize_snow_guide/README
docs/customize_resilient_guide/README
```

## Release Notes
<!--
  Specify all changes in this release. Do not remove the release
  notes of a previous release
-->
### v2.3.1
* Add new input for function fn_snow_create_record. The new boolean input, sn_add_soar_link_on_snow, will determine if a link to the SOAR incident will be added in a note on the ServiceNow incident.

### v2.3.0
* Multiple tables can be used at the same time. See the "Create Record" function in **Customize SOAR Guide** for details.
* Configuration test updated to ensure that ServiceNow app configuration includes table name in `ServiceNowAllowedTables` list.
* New automatic playbook in SOAR to close SOAR incidents automatically when record is closed in ServiceNow.
  Playbook is disabled by default, enable the playbook to get this functionality.
* The SOAR app now supports synchronization with records from any supported table. This is an improvement from v2.2.x where only the
  table listed in app.config was fully supported. See the "Create Record" function in **Customize SOAR Guide** for details.
* Configuration test updated to ensure that ServiceNow app configuration includes table name in `ServiceNowAllowedTables` list
* Added two new manual playbooks to send SOAR Tasks to ServiceNow as either child incidents for the `incident` (Incident) table or Security Incident Tasks
  for the `sn_si_incident` (Security Incident Response) table. These playbooks will only activate when the parent incident in SOAR is
  linked to the respective table (example: incident from table `incident` will allow to send task as child incident).
* Verified on ServiceNow Washington DC release.

### v2.2.1
* Bug fix for breaking html formatted fields on a SOAR incident.

### v2.2.0
* Added playbooks.
* Validated on ServiceNow Vancouver release (use v2.1.0 on ServiceNow).

### 2.2.0 Changes
Since v2.2, the existing rules and workflows have been replaced with playbooks.
This change is made to support the ongoing, newer capabilities of playbooks.
Each playbook has the same functionality as the previous, corresponding rule/workflow.

If upgrading from a previous release, you'll notice that the previous release's rules/workflows remain in place. Both sets of rules and playbooks are active. For manual actions, playbooks have the same name as it's corresponding rule, but with "(PB)" added at the end.
For automatic actions, the playbooks will be disabled by default to avoid conflict with the automatic rules.
All rules and workflows packaged with previous versions of the app should be removed so that
the latest playbooks can be used. Once complete, please enable the automatic playbooks for the app.
To accommodate potential upgrades from pre v2.2 versions, these automatic playbooks will remain
disabled out of the box. For any future upgrades, they will be reset to disabled and should always be
re-enabled after upgrade.

You can continue to use the rules/workflows.
But migrating to playbooks provides greater functionality along with future app enhancements and bug fixes.

### v2.1.0
* Added optional `render_rich_text` configuration. If set to True, rich text notes will be sent to SNOW.
* Verified on ServiceNow Tokyo release
* Verified on ServiceNow Utah release

### v2.0.9
* Support added for ServiceNow Security Incident Response (SIR)
* Support added for API Key authentication from ServiceNow to IBM SOAR
* AppHost support for proxies
* App renamed to IBM Security QRadar SOAR App for ServiceNow
* Verified on ServiceNow San Diego release

### v1.0.5 <!-- omit in toc -->
* Verified on ServiceNow Quebec release

### v1.0.4 <!-- omit in toc -->
* Verified on ServiceNow Paris release

### v1.0.3 <!-- omit in toc -->
* Verified on ServiceNow Orlando release
* Support added for SOAR AppHost

### v1.0.2 <!-- omit in toc -->
* Verified on ServiceNow New York release

### v1.0.1 <!-- omit in toc -->
* Verified on ServiceNow Madrid release

### v1.0.0 <!-- omit in toc -->
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
* ServiceNow Instance with ITSM enabled and running `Utah`, or newer releases
* Access to the **Incident Table** in ServiceNow
* ServiceNow `IBM SOAR App >= v2.3.0` installed on your ServiceNow Instance which you can download from [the ServiceNow Store](http://ibm.biz/get-ibm-resilient-service-now-app)
  * If integrating with ServiceNow Security Incident Table (SIR), `IBM SOAR App >= 2.3.0` and ServiceNow Security Incident Response with its dependencies are required. More information [here](https://www.servicenow.com/products/security-incident-response.html).
* If IBM SOAR is not publicly accessible (behind a firewall), a ServiceNow MID Server is required. See the [Install Guide](./docs/install_guide/README.md) for more information
* IBM Cloud Pak for Security `>= 1.10.18` *or* IBM SOAR `>= v51.0.0.0`
* App Host `>= v1.15.1.0` (recommended) *or* an Integration Server running `resilient-circuits >= v51.0.2.0`.
  - `fn_service_now >= v2.3.0` installed, which you can download from our [App Exchange](http://ibm.biz/get-ibm-resilient-service-now-integration)

---

## Install
Follow our [Install Guide](./docs/install_guide/README.md) to get up and running.

---

## Customize
The default configuration satisfies the requirements for a number of use cases. To adapt the app for your specific requirements, see these customization guides:
- [Customize ServiceNow App Guide](./docs/customize_snow_guide/README.md)
- [Customize SOAR Functions Guide](./docs/customize_resilient_guide/README.md)

---

## Documentation
* See [ibm.biz/res-snow-docs](http://ibm.biz/res-snow-docs) for our latest documentation
