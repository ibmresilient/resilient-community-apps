# **User Guide:** fn_symantec_dlp_v1.0.0

## Table of Contents
- [**User Guide:** fn_symantec_dlp_v1.0.0](#user-guide-fnsymantecdlpv100)
  - [Table of Contents](#table-of-contents)
  - [Key Features](#key-features)
  - [Poller - Symantec DLP Incident Poller](#poller---symantec-dlp-incident-poller)
    - [Configuration](#configuration)
      - [Symantec DLP Report Configuration](#symantec-dlp-report-configuration)
  - [Function - Symantec DLP: Update Incident](#function---symantec-dlp-update-incident)
  - [Custom Fields](#custom-fields)

---

## Key Features
<!--
  List the Key Features of the Integration
-->
* Import Symantec DLP Incidents using a Configurable Poller Component
* Update a Symantec DLP Incident via a Resilient Function (unimplemented)

---

## Poller - Symantec DLP Incident Poller

A configurable circuits component which is used to automatically Poll a Symantec DLP instance using a defined interval. 

Interfacing with the Symantec DLP Incident and Reporting API, the Poller is able to receive all incidents in a saved report and then import each one into Resilient. As a part of the import, certain Artifacts are parsed from the Incident object and saved as the appropiate Resilient Artifact. 

### Configuration 
In order to configure the Poller to run, an app.config value named `sdlp_should_poller_run` needs to be set to `True`. 

See the README located at the root of the project for information on the app.config values. 

>Note: When the `sdlp_should_search_res` is set to True, the important incidents from DLP are filtered twice. Once on the resultant list of incidents filtering out those with a non-null `resilient_incident_id` custom attribute. The second filtering occurs if `sdlp_should_search_res` is set to True and for each Incident. A Resilient search_ex call is performed to ensure no Resilient Incident exists with the given DLP Incident ID set. The search is performed on the `sdlp_incident_id` Resilient Custom Field. This extra filter comes with a performance cost and such be disabled unless needed.

#### Symantec DLP Report Configuration
The Symantec DLP Incident and Reporting SOAP API requires that the polled Incidents be a part of a DLP Saved Report and this Saved Report ID is specified in the app.config. 

A Saved Report is a way to cluster a number of Incidents which match one or more filters. This can be use to pre-configure what sort of Incidents should be brought to Resilient. The DLP Filtering tool allows you to prepare a saved report which can simply be for all DLP Incidents with a non-null `resilient_incident_id` custom attribute. This will result in an ever shrinking list as the Incidents are brought into Resilient. For users targeting a near real-time experience, the above Filtering in addition to a lower polling interval would be recommended.
For an example of how to setup a Saved Report, see the README at the root of this project for a step by step instruction.


## Function - Symantec DLP: Update Incident

**Function is unimplementated**

## Custom Fields
| Label | API Access Name | Type | Prefix | Placeholder | Tooltip |
| ----- | --------------- | ---- | ------ | ----------- | ------- |
| Symantec DLP Incident URL  | `sdlp_incident_url` | `textarea` | `properties` | - | - |
| Symantec DLP Incident ID | `sdlp_incident_id` | `number` | `properties` | - | The ID of a Symantec DLP Incident |

---