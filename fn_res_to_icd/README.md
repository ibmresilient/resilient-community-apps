# Escalation of resilient incidents to ICD desk for IBM Resilient

## Table of Contents

- [Function - Escalate resilient incident to icd dashboard](#function---res-to-icd-function)
- [Workflow - Trigger escalation of resilient incident to icd dashboard](#workflow---res-to-icd-workflow)

This community app allows for the escalation of a incident from Resilient to the ICD desk, via a manual rule on each incident. A word document is attached which explains the mapping of resilient fields to the icd ticket fields for specific use cases. This integration is customizable and allows for rearrangement of those use cases. If the icd_field_severity or icd_priority is not defined, the INTERNAL PRIORITY on icd desk (4) will be set on the escalated ticket corresponding to that resilient incident. IP Sources or Destination Artifacts will be automatically added to the icd ticket if the icd_field_severity is not None (or a negative number) in the app config settings.

To install the package,

`pip install dist/fn-res-to-icd-x.x.x.tar.gz`

To install in "development mode"

`pip install -e ./fn_res_to_icd/`

Please create (or update) the config settings via:

`resilient-circuits config -c [-u]`

Customize with:

`resilient-circuits customize`

After installation, the package will be loaded by `resilient-circuits run`.

---

## res-to-icd-function

**This package contains 1 Function, 1 Workflow, and 1 Manual Rule (at the resilient incident level) that helps you to escalate a resilient incident to an icd ticket**

![screenshot](./screenshots/1.png)

## res-to-icd-workflow

*res-to-icd-workflow: gives you the ability to escalate the incident from resilient to icd

![screenshot](./screenshots/0.png)

## Config settings and prerequisites

All packages used are supported by pypi, import errors between python 2 and 3 are handled. The icd_severity can be specified by a custom value on the UI that can be specified here or can be given a numeric value.

```bash
[fn_res_to_icd]
icd_email=<YOUR ICD EMAIL>
icd_pass=<YOUR ICD PASSWORD>
icd_severity_value=custom_severity
icd_priority=<1-4>
icd_url=https://icdaas.sccd.ibmserviceengage.com/maximo_cbs-dev2
```

A custom field can be specified (qradar_severity in this case) in the UI that can correspond to the icd_severity_value:

![screenshot](./screenshots/4.png)

For testing of credentials and icd endpoint, the developer may run the command:

"resilient-circuits selftest"

To verify that input credentials to icd dashboard are valid via an api call. A failing test here indicate that credentials are invalid or the endpoint is down.

An incident on the resilient can be escalated to the icd desk by running the "Escalate to ICD" manual rule. An example incident is displayed below:
![screenshot](./screenshots/2.png)

When the manual rule is pressed, a correpsponding ticket will be created on the ICD dashboard:
![screenshot](./screenshots/3.png)
