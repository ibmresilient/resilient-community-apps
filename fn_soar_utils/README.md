# SOAR Function Utilities for SOAR


## Table of Contents
- [Release Notes](#release-notes)
- [Overview](#overview)
  - [Key Features](#key-features)
- [Requirements](#requirements)
  - [SOAR platform](#soar-platform)
  - [Cloud Pak for Security](#cloud-pak-for-security)
  - [Proxy Server](#proxy-server)
  - [Python Environment](#python-environment)
- [Installation](#installation)
  - [Install](#install)
  - [App Configuration](#app-configuration)
- [Function - SOAR Utilities Artifact Hash](#function---soar-utilities-artifact-hash)
- [Function - SOAR Utilities: Attachment Hash](#function---soar-utilities-attachment-hash)
- [Function - SOAR Utilities: Attachment to Base64](#function---soar-utilities-attachment-to-base64)
- [Function - SOAR Utilities: Attachment Zip Extract](#function---soar-utilities-attachment-zip-extract)
- [Function - SOAR Utilities: Attachment Zip List](#function---soar-utilities-attachment-zip-list)
- [Function - SOAR Utilities: Base64 to Artifact](#function---soar-utilities-base64-to-artifact)
- [Function - SOAR Utilities: Base64 to Attachment](#function---soar-utilities-base64-to-attachment)
- [Function - SOAR Utilities: Close Incident](#function---soar-utilities-close-incident)
- [Function - SOAR Utilities: Create Incident](#function---soar-utilities-create-incident)
- [Function - SOAR Utilities: Get Contact Info](#function---soar-utilities-get-contact-info)
- [Function - SOAR Utilities: Search Incidents](#function---soar-utilities-search-incidents)
- [Function - SOAR Utilities: SOAR Search](#function---soar-utilities-soar-search)
- [Function - SOAR Utilities: String to Attachment](#function---soar-utilities-string-to-attachment)
- [Playbooks](#playbooks)
- [Troubleshooting & Support](#troubleshooting--support)

---

## Release Notes

| Version | Date | Notes |
| ------- | ---- | ----- |
| 1.1.0 | 06/2025 | Converted workflows to playbooks; fixed bug related to closing incidents; enhanced "Get Contact Info" to include group ownership details and display group members. |
| 1.0.2 | 09/2024 | Bug fix for attachment zip list function |
| 1.0.1 | 01/2023 | Bug fix and doc improvements |
| 1.0.0 | 10/2022 | Initial Release |

---

## Overview

**Useful playbook functions for common automation and integration activities in the SOAR platform.**

 ![screenshot: main](./doc/screenshots/main.png)
 

<p>SOAR functions taken from fn_utilities to simplify development of integrations by wrapping each external activity into an individual playbook component. The SOAR Platform sends data from artifacts, attachments, incident data, etc. to the function component and returns results to the playbook. The results can be acted upon by scripts, rules, and playbook decision points to dynamically orchestrate the security incident response activities.</p><br>

---

## Requirements

This app supports the IBM Security QRadar SOAR Platform and the IBM Security QRadar SOAR for IBM Cloud Pak for Security.

### SOAR platform
The SOAR platform supports two app deployment mechanisms, Edge Gateway (also known as App Host) and integration server.

If deploying to a SOAR platform with an App Host, the requirements are:
* SOAR platform >= `51.0.0.0.9339`.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

If deploying to a SOAR platform with an integration server, the requirements are:
* SOAR platform >= `51.0.0.0.9339`.
* The app is in the older integration format (available from the AppExchange as a `zip` file which contains a `tar.gz` file).
* Integration server is running `resilient-circuits>=51.0.0`.
* If using an API key account, make sure the account provides the following minimum permissions:
  | Name | Permissions |
  | ---- | ----------- |
  | Org Data | Read |
  | Function | Read |


The following SOAR platform guides provide additional information:
* _Edge Gateway Deployment Guide_ or _App Host Deployment Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings.
* _Integration Server Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings.
* _System Administrator Guide_: provides the procedure to install, configure and deploy apps.

The above guides are available on the IBM Documentation website at [ibm.biz/soar-docs](https://ibm.biz/soar-docs). On this web page, select your SOAR platform version. On the follow-on page, you can find the _Edge Gateway Deployment Guide_, _App Host Deployment Guide_, or _Integration Server Guide_ by expanding **Apps** in the Table of Contents pane. The System Administrator Guide is available by expanding **System Administrator**.

### Cloud Pak for Security
If you are deploying to IBM Cloud Pak for Security, the requirements are:
* IBM Cloud Pak for Security >= `1.10.15`.
* Cloud Pak is configured with an Edge Gateway.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

The following Cloud Pak guides provide additional information:
* _Edge Gateway Deployment Guide_ or _App Host Deployment Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings. From the Table of Contents, select Case Management and Orchestration & Automation > **Orchestration and Automation Apps**.
* _System Administrator Guide_: provides information to install, configure, and deploy apps. From the IBM Cloud Pak for Security IBM Documentation table of contents, select Case Management and Orchestration & Automation > **System administrator**.

These guides are available on the IBM Documentation website at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs). From this web page, select your IBM Cloud Pak for Security version. From the version-specific IBM Documentation page, select Case Management and Orchestration & Automation.

### Proxy Server
The app does support a proxy server.

### Python Environment
Python 3.9, 3.11, and 3.12 are officially supported. When deployed as an app, the app runs on Python 3.11.
Additional package dependencies may exist for each of these packages:
* resilient-circuits>=51.0.0




---

## Installation

### Install
* To install or uninstall an App or Integration on the _SOAR platform_, see the documentation at [ibm.biz/soar-docs](https://ibm.biz/soar-docs).
* To install or uninstall an App on _IBM Cloud Pak for Security_, see the documentation at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs) and follow the instructions above to navigate to Orchestration and Automation.

### App Configuration

No app.config setting required for this app.



 ---

## Function - SOAR Utilities Artifact Hash
Calculate hashes for a file artifact. Returns `md5`, `sha1`, `sha256` and other hashes of the file content.

 ![screenshot: fn-soar-utilities-artifact-hash ](./doc/screenshots/fn-soar-utilities-artifact-hash.png) 

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `artifact_id` | `number` | No | `-` | - |
| `incident_id` | `number` | Yes | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "blake2b": "26c1297f39*******ebf74e3e5ce49775ba7720f5cce375cabff28cd3b18511a8d9463c1c9f8c85a0cd6d9133b1e5d6486d1054946b2379e4dcafa1d91cc27",
  "blake2s": "9ee3fa9f*******21a7323aaf0bee5a4aa5eb59652911d3cde20567d90f75e",
  "content_type": "application/octet-stream",
  "created": 1663093337313,
  "filename": "fn_timer.log",
  "md5": "d6815ac6*******d87d21b942ed7c96f",
  "sha1": "44b7ed9*******89ead8977d04a0537fa3125ae",
  "sha224": "d85946*******dba558b6a4856f9517f3ab15ac3b338a96a815af7e",
  "sha256": "561976be4b*******13ea230e0f6a4e708e3b7befc61642dcd281bcacec975",
  "sha384": "83a8bc932*******c064a809c23aa8d737d2e1844b3c512e912fef14678f43bb0c994250a1d628b06b88075f2b441",
  "sha3_224": "18f24955*******9f550f52c7bc09d08e423552774674058511cefc",
  "sha3_256": "756508*******931e199674e65ff9ba5daa25914f75cca8d424efd7ab89f0d",
  "sha3_384": "6324f*******0a0dfcb59f0c2f991e0d68f81976b1e85777bb94827ec031a22720dd4b66b12e2576bde798b74a0645",
  "sha3_512": "d3e927*******f00eba36f137565ba945d311f694a40fd8d1998296d41391e7ff9b07269499346ad65bc8f9f27d79b46680b1dc5656ad9e213491c2e1523a",
  "sha512": "f6f5835d41*******ed7101ae0e21dc3548aab452f5c5d9a634f68c09b50b3ec062f086296628f8d226566637887e5c7be815c83abe2dc8b2746e324b70ac5c",
  "shake_128": "8d64165*******faefe04040f8151589fec8fb13e09aeb6ea68e5f5b98ef5032e5233a6463785f1f613e8ba5b0fdb385754845c5f40b6d8f620496366d72709daca6b711ed9646f971e2ad76f78e83077bc8525e8b37610bc6584b96e89439672b093594b541a4c1a9b54bc9b5594d61aaaa3eee7435890cfa9035b820495",
  "shake_256": "356ba4b*******ad64ed936f0d47e7b19022adfcfc236753182f13a82613c87e3b2dc206fb523952d1841837f785dd8bf137d74919253249327dec36a7b4f180a61cd29e2f2db53febac95deee3300519d4dd28ba08af297f29a5862653a314324e78e41fe2696ab25fb42aa80c63556eeb119d961157c0fb573d93953b7adc485e4cee5c3ecc5561acc5d45c2b1ccb5575a28763a877859d11c9f520d311a750314aebbd71e2459caa4d35a799aeee9f285934086f302d94f368ace46def566f6aac8884b5701914ff26f304b072931bbaeb697aa9d11a71d21767924c96ffe5793848aee50cf40d02dfe4f70f6d329cb83d380397f5f4081c1dcb39034458",
  "size": 14094
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.incident_id = incident.id
inputs.artifact_id = artifact.id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.artifact_hash_result
file_name = str(results.get("filename", ""))
artifact_value = artifact.value

hash_types = {
    "sha256": "Malware SHA-256 Hash",
    "sha1": "Malware SHA-1 Hash",
    "md5": "Malware MD5 Hash"
}

success = False

for hash_key, artifact_type in hash_types.items():
    hash_value = results.get(hash_key)
    if hash_value:
        incident.addArtifact(artifact_type, hash_value, f"{hash_key.upper()} hash of '{artifact_value}'")
        note_text = f"<b>SOAR Utils: Artifact Hash - Example (PB)</b> File {file_name} converted to {hash_key.upper()} successfully."
        incident.addNote(note_text)
        success = True

if not success:
    note_text = f"<b>SOAR Utils: Artifact Hash - Example (PB)</b> Failed: {results.get('reason', 'Unknown reason')}"
    incident.addNote(note_text)


```

</p>
</details>

---
## Function - SOAR Utilities: Attachment Hash
Calculate hashes for a file attachment. Returns `md5`, `sha1`, `sha256` and other hashes of the file content. Those hashes can then be used as artifacts or in other parts of your workflows.

 ![screenshot: fn-soar-utilities-attachment-hash ](./doc/screenshots/fn-soar-utilities-attachment-hash.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `attachment_id` | `number` | No | `-` | - |
| `incident_id` | `number` | Yes | `-` | - |
| `task_id` | `number` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "blake2b": "26c1297f39*******ebf74e3e5ce49775ba7720f5cce375cabff28cd3b18511a8d9463c1c9f8c85a0cd6d9133b1e5d6486d1054946b2379e4dcafa1d91cc27",
  "blake2s": "9ee3fa9f99*******a7323aaf0bee5a4aa5eb59652911d3cde20567d90f75e",
  "content_type": "application/octet-stream",
  "created": 1663177933110,
  "filename": "fn_timer.log",
  "md5": "d6815ac*******97d87d21b942ed7c96f",
  "sha1": "44b7ed9da*******ead8977d04a0537fa3125ae",
  "sha224": "d859465ac*******558b6a4856f9517f3ab15ac3b338a96a815af7e",
  "sha256": "561976be*******478c13ea230e0f6a4e708e3b7befc61642dcd281bcacec975",
  "sha384": "83a8bc932*******7c064a809c23aa8d737d2e1844b3c512e912fef14678f43bb0c994250a1d628b06b88075f2b441",
  "sha3_224": "18f24955d*******f550f52c7bc09d08e423552774674058511cefc",
  "sha3_256": "756508e72*******4931e199674e65ff9ba5daa25914f75cca8d424efd7ab89f0d",
  "sha3_384": "6324ff6*******b59f0c2f991e0d68f81976b1e85777bb94827ec031a22720dd4b66b12e2576bde798b74a0645",
  "sha3_512": "d3e927*******f00eba36f137565ba945d311f694a40fd8d1998296d41391e7ff9b07269499346ad65bc8f9f27d79b46680b1dc5656ad9e213491c2e1523a",
  "sha512": "f6f5835*******a1ed7101ae0e21dc3548aab452f5c5d9a634f68c09b50b3ec062f086296628f8d226566637887e5c7be815c83abe2dc8b2746e324b70ac5c",
  "shake_128": "8d64165fb*******aefe04040f8151589fec8fb13e09aeb6ea68e5f5b98ef5032e5233a6463785f1f613e8ba5b0fdb385754845c5f40b6d8f620496366d72709daca6b711ed9646f971e2ad76f78e83077bc8525e8b37610bc6584b96e89439672b093594b541a4c1a9b54bc9b5594d61aaaa3eee7435890cfa9035b820495",
  "shake_256": "356ba4b*******6ad64ed936f0d47e7b19022adfcfc236753182f13a82613c87e3b2dc206fb523952d1841837f785dd8bf137d74919253249327dec36a7b4f180a61cd29e2f2db53febac95deee3300519d4dd28ba08af297f29a5862653a314324e78e41fe2696ab25fb42aa80c63556eeb119d961157c0fb573d93953b7adc485e4cee5c3ecc5561acc5d45c2b1ccb5575a28763a877859d11c9f520d311a750314aebbd71e2459caa4d35a799aeee9f285934086f302d94f368ace46def566f6aac8884b5701914ff26f304b072931bbaeb697aa9d11a71d21767924c96ffe5793848aee50cf40d02dfe4f70f6d329cb83d380397f5f4081c1dcb39034458",
  "size": 14094
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.incident_id = incident.id
inputs.attachment_id = attachment.id

# If this is a "task attachment" then we will additionally have a task-id
if task is not None:
  inputs.task_id = task.id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.attachment_hash_result
file_name = str(results.get("filename", ""))
attachment_name = attachment.name

hash_types = {
    "sha256": "Malware SHA-256 Hash",
    "sha1": "Malware SHA-1 Hash",
    "md5": "Malware MD5 Hash"
}

success = False

for hash_key, artifact_type in hash_types.items():
    hash_value = results.get(hash_key)
    if hash_value:
        incident.addArtifact(artifact_type, hash_value, f"{hash_key.upper()} hash of '{attachment_name}'")
        note_text = f"<b>SOAR Utils: Attachment Hash - Example (PB)</b> File {file_name} converted to {hash_key.upper()} successfully."
        incident.addNote(note_text)
        success = True

if not success:
    note_text = f"<b>SOAR Utils: Attachment Hash - Example (PB)</b> Failed: {results.get('reason', 'Unknown reason')}"
    incident.addNote(note_text)


```

</p>
</details>

---
## Function - SOAR Utilities: Attachment to Base64
Reads a file attachment in the incident, and produces a base64-encoded string with the file attachment content. This content can then be used in combination with other workflow functions to create an artifact, a new file attachment, or to analyze the contents using various tools.

 ![screenshot: fn-soar-utilities-attachment-to-base64 ](./doc/screenshots/fn-soar-utilities-attachment-to-base64.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `artifact_id` | `number` | No | `-` | - |
| `attachment_id` | `number` | No | `-` | - |
| `incident_id` | `number` | Yes | `-` | - |
| `task_id` | `number` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": "Q3VycmVudCBQb2QgU3R*******RTdGF0dXMoY29uZGl0aW9ucz1bUG9kQ29uZGl0aW9uKGxhc3RQcm9iZVRpbWU9bnVsbCwgbGFzdFRyYW5zaXRpb25UaW1lPTIwMjItMDktMDlUMTU6NTE6MjRaLCBtZXNzYWdlPW51bGwsIHJlYXNvbj1udWxsLCBzdGF0dXM9VHJ1ZSwgdHlwZT1Jbml0aWFsaXplZCwgYWRkaXRpb25hbFByb3BlcnRpZXM9e30pLCBQb2RDb25kaXRpb24obGFzdFByb2JlVGltZT1udWxsLCBsYXN0VHJhbnNpdGlvblRpbWU9MjAyMi0wOS0wOVQxNTo1MTozNlosIG1lc3NhZ2U9bnVsbCwgcmVhc29uPW51bGwsIHN0YXR1cz1UcnVlLCB0eXBlPVJlYWR5LCBhZGRpdGlvbmFsUHJvcGVydGllcz17fSksIFBvZENvbmRpdGlvbihsYXN0UHJvYmVUaW1lPW51bGwsIGxhc3RUcmFuc2l0aW9uVGltZT0yMDIyLTA5LTA5VDE1OjUxOjM2WiwgbWVzc2FnZT1udWxsLCByZWFzb249bnVsbCwgc3RhdHVzPVRydWUsIHR5cGU9Q29udGFpbmVyc1JlYWR5LCBhZGRpdGlvbmFsUHJvcGVydGllcz17fSksIFBvZENvbmRpdGlvbihsYXN0UHJvYmVUaW1lPW51bGwsIGxhc3RUcmFuc2l0aW9uVGltZT0yMDIyLTA5LTA5VDE1OjUxOjI0WiwgbWVzc2FnZT1udWxsLCByZWFzb249bnVsbCwgc3RhdHVzPVRydWUsIHR5cGU9UG9kU2NoZWR1bGVkLCBhZGRpdGlvbmFsUHJvcGVydGllcz17fSldLCBjb250YWluZXJTdGF0dXNlcz1bQ29udGFpbmVyU3RhdHVzKGNvbnRhaW5lcklEPWNvbnRhaW5lcmQ6Ly9lMTVkYzJmZWEzYmViMGI5MGYxZTRiMmM5ZGJhZDlkMWExZjM3MzY5ZTMzNmU2MzA2NDU1NzE3Yjc0YWJmNmIxLCBpbWFnZT1zZWMtcmVzaWxpZW50LWRvY2tlci1sb2NhbC5hcnRpZmFjdG9yeS5zd2ctZGV2b3BzLmNvbS9pYm1yZXNpbGllbnQvZm5fdGltZXI6MS4wLjEzNTg5LCBpbWFnZUlEPXNlYy1yZXNpbGllbnQtZG9ja2VyLWxvY2FsLmFydGlmYWN0b3J5LnN3Zy1kZXZvcHMuY29tL2libXJlc2lsaWVudC9mbl90aW1lckBzaGEyNTY6ZGE5ZDliOGQ0NjIwYWQ2YTNjOTUzZGU0NDc3YzExYWE0NDY1NmRhOTA0MDdkZGRkMTkyOTc5ZGU1NmY2M2FhNCwgbGFzdFN0YXRlPUNvbnRhaW5lclN0YXRlKHJ1bm5pbmc9bnVsbCwgdGVybWluYXRlZD1udWxsLCB3YWl0aW5nPW51bGwsIGFkZGl0aW9uYWxQcm9wZXJ0aWVzPXt9KSwgbmFtZT03ZDAzMDE1Ni1iOWJlLTRhMTItYmMzZS0zOTY0N2E3NmY5MDAsIHJlYWR5PXRydWUsIHJlc3RhcnRDb3VudD0wLCBzdGFydGVkPXRydWUsIHN0YXRlPUNvbnRhaW5lclN0YXRlKHJ1bm5pbmc9Q29udGFpbmVyU3RhdGVSdW5uaW5nKHN0YXJ0ZWRBdD0yMDIyLTA5LTA5VDE1OjUxOjM1WiwgYWRkaXRpb25hbFByb3BlcnRpZXM9e30pLCB0ZXJtaW5hdGVkPW51bGwsIHdhaXRpbmc9bnVsbCwgYWRkaXRpb25hbFByb3BlcnRpZXM9e30pLCBhZGRpdGlvbmFsUHJvcGVydGllcz17fSldLCBlcGhlbWVyYWxDb250YWluZXJTdGF0dXNlcz1bXSwgaG9zdElQPTkuMzAuMTQxLjIxNCwgaW5pdENvbnRhaW5lclN0YXR1c2VzPVtdLCBtZXNzYWdlPW51bGwsIG5vbWluYXRlZE5vZGVOYW1lPW51bGwsIHBoYXNlPVJ1bm5pbmcsIHBvZElQPTEwLjQyLjEuMjE1LCBwb2RJUHM9W1BvZElQKGlwPTEwLjQyLjEuMjE1LCBhZGRpdGlvbmFsUHJvcGVydGllcz17fSldLCBxb3NDbGFzcz1CZXN0RWZmb3J0LCByZWFzb249bnVsbCwgc3RhcnRUaW1lPTIwMjItMDktMDlUMTU6NTE6MjRaLCBhZGRpdGlvbmFsUHJvcGVydGllcz17fSkKTG9nczoKCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQpFbnZpcm9ubWVudDoKUHl0aG9uIFZlcnNpb246IDMuOS43IChkZWZhdWx0LCBTZXAgMTMgMjAyMSwgMDg6MTg6MzkpIApbR0NDIDguNS4wIDIwMjEwNTE0IChSZWQgSGF0IDguNS4wLTMpXQoKSW5zdGFsbGVkIHBhY2thZ2VzOgoKYmVhdXRpZnVsc291cDQ6IDQuMTEuMQpjYWNoZXRvb2xzOiA1LjIuMApjZXJ0aWZpOiAyMDIyLjYuMTUuMQpjZmZpOiAxLjE1LjEKY2hhcnNldC1ub3JtYWxpemVyOiAyLjEuMQpjaXJjdWl0czogMy4yLjIKY3J5cHRvZ3JhcGh5OiAzOC4wLjEKZGVjb3JhdG9yOiA1LjEuMQpEZXByZWNhdGVkOiAxLjIuMTMKZmlsZWxvY2s6IDMuOC4wCmZuLXRpbWVyOiAxLjAuMTM1ODkKaWRuYTogMy4zCmltcG9ydGxpYi1tZXRhZGF0YTogNC4xMi4wCmphcmFjby5jbGFzc2VzOiAzLjIuMgpqZWVwbmV5OiAwLjguMApKaW5qYTI6IDMuMS4yCmtleXJpbmc6IDIzLjkuMQpNYXJrdXBTYWZlOiAyLjEuMQptb3JlLWl0ZXJ0b29sczogOC4xNC4wCnBpcDogMjIuMi4yCnB5OiAxLjExLjAKcHljcGFyc2VyOiAyLjIxClB5U29ja3M6IDEuNy4xCnB5dHo6IDIwMjIuMi4xCnJlcXVlc3RzOiAyLjI4LjEKcmVxdWVzdHMtdG9vbGJlbHQ6IDAuOS4xCnJlc2lsaWVudDogNDYuMC4zNDYxCnJlc2lsaWVudC1jaXJjdWl0czogNDYuMC4zNDYxCnJlc2lsaWVudC1saWI6IDQ2LjAuMzQ2MQpyZXRyeTI6IDAuOS40ClNlY3JldFN0b3JhZ2U6IDMuMy4zCnNldHVwdG9vbHM6IDYyLjYuMApzaXg6IDEuMTYuMApzb3Vwc2lldmU6IDIuMy4yLnBvc3QxCnN0b21wZXN0OiAyLjMuMAp1cmxsaWIzOiAxLjI2LjEyCndhdGNoZG9nOiAyLjEuOQp3cmFwdDogMS4xNC4xCnppcHA6IDMuOC4xCiMjIyMjIyMjIyMjIyMjIwoyMDIyLTA5LTA5IDE1OjUxOjM2LDQ5MyBJTkZPIFthcHBdIENvbmZpZ3VyYXRpb24gZmlsZTogL2V0Yy9yZXNjaXJjdWl0cy9hcHAuY29uZmlnCjIwMjItMDktMDkgMTU6NTE6MzYsNDk0IElORk8gW2FwcF0gUmVzaWxpZW50IHNlcnZlcjogOS4zMC40NC40NQoyMDIyLTA5LTA5IDE1OjUxOjM2LDQ5NCBJTkZPIFthcHBdIFJlc2lsaWVudCBhcGkga2V5IGlkOiBhMDI4ODI4OC1hYjkxLTRlMWMtOGM5ZS1mZjcyOThhNzlhNTIKMjAyMi0wOS0wOSAxNTo1MTozNiw0OTUgSU5GTyBbYXBwXSBSZXNpbGllbnQgb3JnOiBUZXN0IE9yZ2FuaXphdGlvbgoyMDIyLTA5LTA5IDE1OjUxOjM2LDQ5NSBJTkZPIFthcHBdIExvZ2dpbmcgTGV2ZWw6IElORk8KMjAyMi0wOS0wOSAxNTo1MTozNiw0OTYgV0FSTklORyBbY28zXSBVbnZlcmlmaWVkIEhUVFBTIHJlcXVlc3RzIChjYWZpbGU9ZmFsc2UpLgoyMDIyLTA5LTA5IDE1OjUxOjM2LDU4OSBJTkZPIFtjbzNiYXNlXSBVc2luZyBvcmcgbmFtZTogVGVzdCBPcmdhbml6YXRpb24KMjAyMi0wOS0wOSAxNTo1MTozNywwMjggSU5GTyBbYXBwXSBDb21wb25lbnRzIGF1dG8tbG9hZCBkaXJlY3Rvcnk6IChub25lKQoyMDIyLTA5LTA5IDE1OjUxOjM3LDA2MiBJTkZPIFtjb21wb25lbnRfbG9hZGVyXSBMb2FkaW5nIDEgY29tcG9uZW50cwoyMDIyLTA5LTA5IDE1OjUxOjM3LDA2MyBJTkZPIFtjb21wb25lbnRfbG9hZGVyXSAnZm5fdGltZXIuY29tcG9uZW50cy5mdW5jdF9mbl90aW1lci5GdW5jdGlvbkNvbXBvbmVudCcgbG9hZGluZwoyMDIyLTA5LTA5IDE1OjUxOjM3LDIxOSBXQVJOSU5HIFthY3Rpb25zX2NvbXBvbmVudF0gVW52ZXJpZmllZCBTVE9NUCBUTFMgY2VydGlmaWNhdGUgKGNhZmlsZT1mYWxzZSkKMjAyMi0wOS0wOSAxNTo1MTozNywyMjkgSU5GTyBbc3RvbXBfY29tcG9uZW50XSBDb25uZWN0IHRvIDkuMzAuNDQuNDU6NjUwMDEKMjAyMi0wOS0wOSAxNTo1MTozNywyMzAgSU5GTyBbYWN0aW9uc19jb21wb25lbnRdICdmbl90aW1lci5jb21wb25lbnRzLmZ1bmN0X2ZuX3RpbWVyLkZ1bmN0aW9uQ29tcG9uZW50JyBmdW5jdGlvbiAnZm5fdGltZXInIHJlZ2lzdGVyZWQgdG8gJ2ZuX3RpbWVyJwoyMDIyLTA5LTA5IDE1OjUxOjM3LDIzMCBJTkZPIFthcHBdIENvbXBvbmVudHMgbG9hZGVkCjIwMjItMDktMDkgMTU6NTE6MzcsMjMyIElORk8gW2FwcF0gQXBwIFN0YXJ0ZWQKMjAyMi0wOS0wOSAxNTo1MTozNywzMzUgSU5GTyBbYWN0aW9uc19jb21wb25lbnRdIFNUT01QIGF0dGVtcHRpbmcgdG8gY29ubmVjdAoyMDIyLTA5LTA5IDE1OjUxOjM3LDMzNiBJTkZPIFtzdG9tcF9jb21wb25lbnRdIENvbm5lY3QgdG8gU3RvbXAuLi4KMjAyMi0wOS0wOSAxNTo1MTozNywzMzYgSU5GTyBbY2xpZW50XSBDb25uZWN0aW5nIHRvIDkuMzAuNDQuNDU6NjUwMDEgLi4uCjIwMjItMDktMDkgMTU6NTE6MzcsMzkyIElORk8gW2NsaWVudF0gQ29ubmVjdGlvbiBlc3RhYmxpc2hlZAoyMDIyLTA5LTA5IDE1OjUxOjM3LDQ2NSBJTkZPIFtjbGllbnRdIENvbm5lY3RlZCB0byBzdG9tcCBicm9rZXIgW3Nlc3Npb249SUQ6dGhpc3RsZXMxLmZ5cmUuaWJtLmNvbS00NDYxMS0xNjYxNzgyNTAwODA1LTQ6ODQsIHZlcnNpb249MS4yXQoyMDIyLTA5LTA5IDE1OjUxOjM3LDQ2NSBJTkZPIFtzdG9tcF9jb21wb25lbnRdIENvbm5lY3RlZCB0byBmYWlsb3Zlcjooc3NsOi8vOS4zMC40NC40NTo2NTAwMSk/bWF4UmVjb25uZWN0QXR0ZW1wdHM9MyxzdGFydHVwTWF4UmVjb25uZWN0QXR0ZW1wdHM9MwoyMDIyLTA5LTA5IDE1OjUxOjM3LDQ2NiBJTkZPIFtzdG9tcF9jb21wb25lbnRdIENsaWVudCBIQjogMCAgU2VydmVyIEhCOiAxNTAwMAoyMDIyLTA5LTA5IDE1OjUxOjM3LDQ2NiBJTkZPIFtzdG9tcF9jb21wb25lbnRdIE5vIENsaWVudCBoZWFydGJlYXRzIHdpbGwgYmUgc2VudAoyMDIyLTA5LTA5IDE1OjUxOjM3LDQ2NiBJTkZPIFtzdG9tcF9jb21wb25lbnRdIFJlcXVlc3RlZCBoZWFydGJlYXRzIGZyb20gc2VydmVyLgoyMDIyLTA5LTA5IDE1OjUxOjM3LDQ2OCBJTkZPIFthY3Rpb25zX2NvbXBvbmVudF0gU1RPTVAgY29ubmVjdGVkLgoyMDIyLTA5LTA5IDE1OjUxOjM3LDU3MCBJTkZPIFthY3Rpb25zX2NvbXBvbmVudF0gcmVzaWxpZW50LWNpcmN1aXRzIGhhcyBzdGFydGVkIHN1Y2Nlc3NmdWxseSBhbmQgaXMgbm93IHJ1bm5pbmcuLi4KMjAyMi0wOS0wOSAxNTo1MTozNyw1NzAgSU5GTyBbYWN0aW9uc19jb21wb25lbnRdIFN1YnNjcmliZSB0byBtZXNzYWdlIGRlc3RpbmF0aW9uICdmbl90aW1lcicKMjAyMi0wOS0wOSAxNTo1MTozNyw1NzEgSU5GTyBbc3RvbXBfY29tcG9uZW50XSBTdWJzY3JpYmUgdG8gbWVzc2FnZSBkZXN0aW5hdGlvbiBhY3Rpb25zLjIwMS5mbl90aW1lcgoyMDIyLTA5LTA5IDE1OjUxOjM3LDk3NiBJTkZPIFthY3Rpb25zX2NvbXBvbmVudF0gRXZlbnQ6IDxmbl90aW1lcltdIChpZD00MSwgd29ya2Zsb3c9cGxheWJvb2tfNTdmNmM1NjlfNWUxZV80ZTM4XzgwNjJfM2MzZDg2OTY1OTU3LCB1c2VyPWFkbWluQGV4YW1wbGUuY29tKSAyMDIyLTA5LTA5IDE1OjQxOjMzLjg3MjAwMD4gQ2hhbm5lbDogZnVuY3Rpb25zLmZuX3RpbWVyCjIwMjItMDktMDkgMTU6NTE6MzgsMTc5IElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gVmFsaWRhdGVkIGZ1bmN0aW9uIGlucHV0cwoyMDIyLTA5LTA5IDE1OjUxOjM4LDE4MCBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IFN0YXJ0aW5nIEFwcCBGdW5jdGlvbjogJ2ZuX3RpbWVyJwoyMDIyLTA5LTA5IDE1OjUxOjM4LDE4MCBJTkZPIFtmdW5jdF9mbl90aW1lcl0gdGltZXJfdGltZTogCjIwMjItMDktMDkgMTU6NTE6MzgsMTgwIElORk8gW2Z1bmN0X2ZuX3RpbWVyXSB0aW1lcl9lcG9jaDogMTY2MjczODMwMDAwMAoyMDIyLTA5LTA5IDE1OjUxOjM4LDE4NCBFUlJPUiBbYWN0aW9uc19jb21wb25lbnRdIFRyYWNlYmFjayAobW9zdCByZWNlbnQgY2FsbCBsYXN0KToKRmlsZSAiL29wdC9hcHAtcm9vdC9saWI2NC9weXRob24zLjkvc2l0ZS1wYWNrYWdlcy9yZXNpbGllbnRfY2lyY3VpdHMvYWN0aW9uc19jb21wb25lbnQucHkiLCBsaW5lIDkwLCBpbiBfb25fdGFzawp5aWVsZCByZXN1bHQuZ2V0KCkKRmlsZSAiL3Vzci9saWI2NC9weXRob24zLjkvbXVsdGlwcm9jZXNzaW5nL3Bvb2wucHkiLCBsaW5lIDc3MSwgaW4gZ2V0CnJhaXNlIHNlbGYuX3ZhbHVlCkZpbGUgIi91c3IvbGliNjQvcHl0aG9uMy45L211bHRpcHJvY2Vzc2luZy9wb29sLnB5IiwgbGluZSAxMjUsIGluIHdvcmtlcgpyZXN1bHQgPSAoVHJ1ZSwgZnVuYygqYXJncywgKiprd2RzKSkKRmlsZSAiL29wdC9hcHAtcm9vdC9saWI2NC9weXRob24zLjkvc2l0ZS1wYWNrYWdlcy9yZXNpbGllbnRfY2lyY3VpdHMvZGVjb3JhdG9ycy5weSIsIGxpbmUgMjkwLCBpbiBfaW52b2tlX2FwcF9mdW5jdGlvbgpyYWlzZSByCnJlc2lsaWVudF9jaXJjdWl0cy5hY3Rpb25fbWVzc2FnZS5GdW5jdGlvbkV4Y2VwdGlvbl86IApUcmFjZWJhY2sgKG1vc3QgcmVjZW50IGNhbGwgbGFzdCk6CkZpbGUgIi9vcHQvYXBwLXJvb3QvbGliNjQvcHl0aG9uMy45L3NpdGUtcGFja2FnZXMvZm5fdGltZXIvY29tcG9uZW50cy9mdW5jdF9mbl90aW1lci5weSIsIGxpbmUgNzQsIGluIF90aW1lcl9mdW5jdGlvbgp0b3RhbF90aW1lX2luX3NlY29uZHMgPSBnZXRfc2xlZXBfdGltZV9mcm9tX2Vwb2NoKHRpbWVyX2Vwb2NoKQpGaWxlICIvb3B0L2FwcC1yb290L2xpYjY0L3B5dGhvbjMuOS9zaXRlLXBhY2thZ2VzL2ZuX3RpbWVyL2NvbXBvbmVudHMvZnVuY3RfZm5fdGltZXIucHkiLCBsaW5lIDE2NiwgaW4gZ2V0X3NsZWVwX3RpbWVfZnJvbV9lcG9jaApyYWlzZSBWYWx1ZUVycm9yKCJUaW1lciBlbmQgZGF0ZSBpcyBpbiB0aGUgcGFzdDogezB9Ii5mb3JtYXQoZW5kX2Vwb2NoKSkKVmFsdWVFcnJvcjogVGltZXIgZW5kIGRhdGUgaXMgaW4gdGhlIHBhc3Q6IDE2NjI3MzgzMDAwMDAKCgoyMDIyLTA5LTA5IDE1OjUxOjM4LDE4NiBFUlJPUiBbYWN0aW9uc19jb21wb25lbnRdIDx0YXNrW2Z1bmN0aW9ud29ya2VyXSAoPGZ1bmN0aW9uIGFwcF9mdW5jdGlvbi5fX2NhbGxfXy48bG9jYWxzPi5hcHBfZnVuY3Rpb25fZGVjb3JhdG9yLjxsb2NhbHM+Ll9pbnZva2VfYXBwX2Z1bmN0aW9uIGF0IDB4N2ZlYTU4MzUwZTUwPiwgPGZuX3RpbWVyW2Z1bmN0aW9ucy5mbl90aW1lcl0gKGlkPTQxLCB3b3JrZmxvdz1wbGF5Ym9va181N2Y2YzU2OV81ZTFlXzRlMzhfODA2Ml8zYzNkODY5NjU5NTcsIHVzZXI9YWRtaW5AZXhhbXBsZS5jb20pIDIwMjItMDktMDkgMTU6NDE6MzMuODcyMDAwPiB0aW1lcl90aW1lPScnLCB0aW1lcl9lcG9jaD0xNjYyNzM4MzAwMDAwKT4gKDxjbGFzcyAncmVzaWxpZW50X2NpcmN1aXRzLmFjdGlvbl9tZXNzYWdlLkZ1bmN0aW9uRXhjZXB0aW9uXyc+KTogClRyYWNlYmFjayAobW9zdCByZWNlbnQgY2FsbCBsYXN0KToKRmlsZSAiL29wdC9hcHAtcm9vdC9saWI2NC9weXRob24zLjkvc2l0ZS1wYWNrYWdlcy9mbl90aW1lci9jb21wb25lbnRzL2Z1bmN0X2ZuX3RpbWVyLnB5IiwgbGluZSA3NCwgaW4gX3RpbWVyX2Z1bmN0aW9uCnRvdGFsX3RpbWVfaW5fc2Vjb25kcyA9IGdldF9zbGVlcF90aW1lX2Zyb21fZXBvY2godGltZXJfZXBvY2gpCkZpbGUgIi9vcHQvYXBwLXJvb3QvbGliNjQvcHl0aG9uMy45L3NpdGUtcGFja2FnZXMvZm5fdGltZXIvY29tcG9uZW50cy9mdW5jdF9mbl90aW1lci5weSIsIGxpbmUgMTY2LCBpbiBnZXRfc2xlZXBfdGltZV9mcm9tX2Vwb2NoCnJhaXNlIFZhbHVlRXJyb3IoIlRpbWVyIGVuZCBkYXRlIGlzIGluIHRoZSBwYXN0OiB7MH0iLmZvcm1hdChlbmRfZXBvY2gpKQpWYWx1ZUVycm9yOiBUaW1lciBlbmQgZGF0ZSBpcyBpbiB0aGUgcGFzdDogMTY2MjczODMwMDAwMAoKMjAyMi0wOS0wOSAxNTo1MjozOSw4ODUgSU5GTyBbYWN0aW9uc19jb21wb25lbnRdIEV2ZW50OiA8Zm5fdGltZXJbXSAoaWQ9NDEsIHdvcmtmbG93PXBsYXlib29rXzU3ZjZjNTY5XzVlMWVfNGUzOF84MDYyXzNjM2Q4Njk2NTk1NywgdXNlcj1hZG1pbkBleGFtcGxlLmNvbSkgMjAyMi0wOS0wOSAxNTo1MjozOS42NTgwMDA+IENoYW5uZWw6IGZ1bmN0aW9ucy5mbl90aW1lcgoyMDIyLTA5LTA5IDE1OjUyOjQwLDA5MCBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFZhbGlkYXRlZCBmdW5jdGlvbiBpbnB1dHMKMjAyMi0wOS0wOSAxNTo1Mjo0MCwwOTEgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBTdGF0dXNNZXNzYWdlOiBTdGFydGluZyBBcHAgRnVuY3Rpb246ICdmbl90aW1lcicKMjAyMi0wOS0wOSAxNTo1Mjo0MCwwOTEgSU5GTyBbZnVuY3RfZm5fdGltZXJdIHRpbWVyX3RpbWU6IAoyMDIyLTA5LTA5IDE1OjUyOjQwLDA5MiBJTkZPIFtmdW5jdF9mbl90aW1lcl0gdGltZXJfZXBvY2g6IDE2NjI3Mzg5MDAwMDAKMjAyMi0wOS0wOSAxNTo1Mjo0MCwxNzUgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBTdGF0dXNNZXNzYWdlOiBTbGVlcGluZyBmb3IgMzRzLiAwLzEzOXMgY29tcGxldGUuCjIwMjItMDktMDkgMTU6NTM6MTQsMjg0IElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogU2xlZXBpbmcgZm9yIDM0cy4gMzQvMTM5cyBjb21wbGV0ZS4KMjAyMi0wOS0wOSAxNTo1Mzo0OCwzNjMgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBTdGF0dXNNZXNzYWdlOiBTbGVlcGluZyBmb3IgMzRzLiA2OC8xMzlzIGNvbXBsZXRlLgoyMDIyLTA5LTA5IDE1OjU0OjIyLDQ1OCBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IFNsZWVwaW5nIGZvciAzNHMuIDEwMi8xMzlzIGNvbXBsZXRlLgoyMDIyLTA5LTA5IDE1OjU0OjU2LDU3OCBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IFNsZWVwaW5nIGZvciAzcy4gMTM2LzEzOXMgY29tcGxldGUuCjIwMjItMDktMDkgMTU6NTQ6NTksNjQ2IElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogVG90YWwgc2xlZXAgdGltZSAxMzkgc2Vjb25kcyBjb21wbGV0ZS4KMjAyMi0wOS0wOSAxNTo1NDo1OSw2NDkgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBSZXR1cm5pbmcgcmVzdWx0cwoyMDIyLTA5LTA5IDE1OjU0OjU5LDY1MSBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IEZpbmlzaGVkIHJ1bm5pbmcgQXBwIEZ1bmN0aW9uOiAnZm5fdGltZXInCjIwMjItMDktMDkgMTU6NTc6NDEsOTk1IElORk8gW2FjdGlvbnNfY29tcG9uZW50XSBFdmVudDogPGZuX3RpbWVyW10gKGlkPTQxLCB3b3JrZmxvdz1wbGF5Ym9va181N2Y2YzU2OV81ZTFlXzRlMzhfODA2Ml8zYzNkODY5NjU5NTcsIHVzZXI9YWRtaW5AZXhhbXBsZS5jb20pIDIwMjItMDktMDkgMTU6NTc6NDEuNjg3MDAwPiBDaGFubmVsOiBmdW5jdGlvbnMuZm5fdGltZXIKMjAyMi0wOS0wOSAxNTo1Nzo0MiwxOTkgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBWYWxpZGF0ZWQgZnVuY3Rpb24gaW5wdXRzCjIwMjItMDktMDkgMTU6NTc6NDIsMjAxIElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogU3RhcnRpbmcgQXBwIEZ1bmN0aW9uOiAnZm5fdGltZXInCjIwMjItMDktMDkgMTU6NTc6NDIsMjAxIElORk8gW2Z1bmN0X2ZuX3RpbWVyXSB0aW1lcl90aW1lOiAyMHMKMjAyMi0wOS0wOSAxNTo1Nzo0MiwyMDEgSU5GTyBbZnVuY3RfZm5fdGltZXJdIHRpbWVyX2Vwb2NoOiBOb25lCjIwMjItMDktMDkgMTU6NTc6NDIsMjkxIElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogU2xlZXBpbmcgZm9yIDEwcy4gMC8yMHMgY29tcGxldGUuCjIwMjItMDktMDkgMTU6NTc6NTIsMzYyIElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogU2xlZXBpbmcgZm9yIDEwcy4gMTAvMjBzIGNvbXBsZXRlLgoyMDIyLTA5LTA5IDE1OjU4OjAyLDQzOSBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IFRvdGFsIHNsZWVwIHRpbWUgMjAgc2Vjb25kcyBjb21wbGV0ZS4KMjAyMi0wOS0wOSAxNTo1ODowMiw0NDIgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBSZXR1cm5pbmcgcmVzdWx0cwoyMDIyLTA5LTA5IDE1OjU4OjAyLDQ0MiBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IEZpbmlzaGVkIHJ1bm5pbmcgQXBwIEZ1bmN0aW9uOiAnZm5fdGltZXInCjIwMjItMDktMDkgMTg6MDg6MDQsODMzIElORk8gW2FjdGlvbnNfY29tcG9uZW50XSBFdmVudDogPGZuX3RpbWVyW10gKGlkPTQxLCB3b3JrZmxvdz1wbGF5Ym9va181N2Y2YzU2OV81ZTFlXzRlMzhfODA2Ml8zYzNkODY5NjU5NTcsIHVzZXI9YWRtaW5AZXhhbXBsZS5jb20pIDIwMjItMDktMDkgMTg6MDg6MDQuNTYyMDAwPiBDaGFubmVsOiBmdW5jdGlvbnMuZm5fdGltZXIKMjAyMi0wOS0wOSAxODowODowNSwwNDAgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBWYWxpZGF0ZWQgZnVuY3Rpb24gaW5wdXRzCjIwMjItMDktMDkgMTg6MDg6MDUsMDQyIElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogU3RhcnRpbmcgQXBwIEZ1bmN0aW9uOiAnZm5fdGltZXInCjIwMjItMDktMDkgMTg6MDg6MDUsMDQyIElORk8gW2Z1bmN0X2ZuX3RpbWVyXSB0aW1lcl90aW1lOiA2MHMKMjAyMi0wOS0wOSAxODowODowNSwwNDQgSU5GTyBbZnVuY3RfZm5fdGltZXJdIHRpbWVyX2Vwb2NoOiBOb25lCjIwMjItMDktMDkgMTg6MDg6MDUsMDQ1IFdBUk5JTkcgW2NvM10gVW52ZXJpZmllZCBIVFRQUyByZXF1ZXN0cyAoY2FmaWxlPWZhbHNlKS4KMjAyMi0wOS0wOSAxODowODowNSwxMzAgSU5GTyBbY28zYmFzZV0gVXNpbmcgb3JnIG5hbWU6IFRlc3QgT3JnYW5pemF0aW9uCjIwMjItMDktMDkgMTg6MDg6MDUsMzE1IElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogU2xlZXBpbmcgZm9yIDMwcy4gMC82MHMgY29tcGxldGUuCjIwMjItMDktMDkgMTg6MDg6MzUsNDE4IElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogV29ya2Zsb3cgd2FzIHRlcm1pbmF0ZWQuCjIwMjItMDktMDkgMTg6MDg6MzUsNDE5IElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogVG90YWwgc2xlZXAgdGltZSAzMCBzZWNvbmRzIGNvbXBsZXRlLgoyMDIyLTA5LTA5IDE4OjA4OjM1LDQyMSBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFJldHVybmluZyByZXN1bHRzCjIwMjItMDktMDkgMTg6MDg6MzUsNDIzIElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogRmluaXNoZWQgcnVubmluZyBBcHAgRnVuY3Rpb246ICdmbl90aW1lcicKMjAyMi0wOS0wOSAxODowODozNSw0MjIgSU5GTyBbYWN0aW9uc19jb21wb25lbnRdIEV2ZW50OiA8Zm5fdGltZXJbXSAoaWQ9NDEsIHdvcmtmbG93PXRpbWVyX2luX3BhcmFsbGVsLCB1c2VyPWFkbWluQGV4YW1wbGUuY29tKSAyMDIyLTA5LTA5IDE4OjA4OjM1LjE0MzAwMD4gQ2hhbm5lbDogZnVuY3Rpb25zLmZuX3RpbWVyCjIwMjItMDktMDkgMTg6MDg6MzUsNDI1IElORk8gW2FjdGlvbnNfY29tcG9uZW50XSBFdmVudDogPGZuX3RpbWVyW10gKGlkPTQxLCB3b3JrZmxvdz10aW1lcl9pbl9wYXJhbGxlbCwgdXNlcj1hZG1pbkBleGFtcGxlLmNvbSkgMjAyMi0wOS0wOSAxODowODozNS4xNDkwMDA+IENoYW5uZWw6IGZ1bmN0aW9ucy5mbl90aW1lcgoyMDIyLTA5LTA5IDE4OjA4OjM1LDQyOSBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFZhbGlkYXRlZCBmdW5jdGlvbiBpbnB1dHMKMjAyMi0wOS0wOSAxODowODozNSw0MzAgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBTdGF0dXNNZXNzYWdlOiBTdGFydGluZyBBcHAgRnVuY3Rpb246ICdmbl90aW1lcicKMjAyMi0wOS0wOSAxODowODozNSw0MzAgSU5GTyBbZnVuY3RfZm5fdGltZXJdIHRpbWVyX3RpbWU6IDJtCjIwMjItMDktMDkgMTg6MDg6MzUsNDMzIElORk8gW2Z1bmN0X2ZuX3RpbWVyXSB0aW1lcl9lcG9jaDogTm9uZQoyMDIyLTA5LTA5IDE4OjA4OjM1LDQzMiBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFZhbGlkYXRlZCBmdW5jdGlvbiBpbnB1dHMKMjAyMi0wOS0wOSAxODowODozNSw0MzUgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBTdGF0dXNNZXNzYWdlOiBTdGFydGluZyBBcHAgRnVuY3Rpb246ICdmbl90aW1lcicKMjAyMi0wOS0wOSAxODowODozNSw0MzYgSU5GTyBbZnVuY3RfZm5fdGltZXJdIHRpbWVyX3RpbWU6IDNtCjIwMjItMDktMDkgMTg6MDg6MzUsNDM2IElORk8gW2Z1bmN0X2ZuX3RpbWVyXSB0aW1lcl9lcG9jaDogTm9uZQoyMDIyLTA5LTA5IDE4OjA4OjM1LDUxNiBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IFNsZWVwaW5nIGZvciAzMHMuIDAvMTIwcyBjb21wbGV0ZS4KMjAyMi0wOS0wOSAxODowODozNSw1MjkgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBTdGF0dXNNZXNzYWdlOiBTbGVlcGluZyBmb3IgNDVzLiAwLzE4MHMgY29tcGxldGUuCjIwMjItMDktMDkgMTg6MDk6MDUsNjMwIElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogV29ya2Zsb3cgd2FzIHRlcm1pbmF0ZWQuCjIwMjItMDktMDkgMTg6MDk6MDUsNjMyIElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogVG90YWwgc2xlZXAgdGltZSAzMCBzZWNvbmRzIGNvbXBsZXRlLgoyMDIyLTA5LTA5IDE4OjA5OjA1LDYzMyBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFJldHVybmluZyByZXN1bHRzCjIwMjItMDktMDkgMTg6MDk6MDUsNjM2IElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogRmluaXNoZWQgcnVubmluZyBBcHAgRnVuY3Rpb246ICdmbl90aW1lcicKMjAyMi0wOS0wOSAxODowOToyMCw2MzUgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBTdGF0dXNNZXNzYWdlOiBXb3JrZmxvdyB3YXMgdGVybWluYXRlZC4KMjAyMi0wOS0wOSAxODowOToyMCw2MzYgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBTdGF0dXNNZXNzYWdlOiBUb3RhbCBzbGVlcCB0aW1lIDQ1IHNlY29uZHMgY29tcGxldGUuCjIwMjItMDktMDkgMTg6MDk6MjAsNjM5IElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gUmV0dXJuaW5nIHJlc3VsdHMKMjAyMi0wOS0wOSAxODowOToyMCw2NDAgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBTdGF0dXNNZXNzYWdlOiBGaW5pc2hlZCBydW5uaW5nIEFwcCBGdW5jdGlvbjogJ2ZuX3RpbWVyJwoyMDIyLTA5LTA5IDE4OjE5OjUxLDk3NCBJTkZPIFthY3Rpb25zX2NvbXBvbmVudF0gRXZlbnQ6IDxmbl90aW1lcltdIChpZD00MSwgd29ya2Zsb3c9cGxheWJvb2tfNTdmNmM1NjlfNWUxZV80ZTM4XzgwNjJfM2MzZDg2OTY1OTU3LCB1c2VyPWFkbWluQGV4YW1wbGUuY29tKSAyMDIyLTA5LTA5IDE4OjE5OjUxLjY5NzAwMD4gQ2hhbm5lbDogZnVuY3Rpb25zLmZuX3RpbWVyCjIwMjItMDktMDkgMTg6MTk6NTIsMTgwIElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gVmFsaWRhdGVkIGZ1bmN0aW9uIGlucHV0cwoyMDIyLTA5LTA5IDE4OjE5OjUyLDE4MSBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IFN0YXJ0aW5nIEFwcCBGdW5jdGlvbjogJ2ZuX3RpbWVyJwoyMDIyLTA5LTA5IDE4OjE5OjUyLDE4MiBJTkZPIFtmdW5jdF9mbl90aW1lcl0gdGltZXJfdGltZTogNW0KMjAyMi0wOS0wOSAxODoxOTo1MiwxODIgSU5GTyBbZnVuY3RfZm5fdGltZXJdIHRpbWVyX2Vwb2NoOiBOb25lCjIwMjItMDktMDkgMTg6MTk6NTIsMTgyIFdBUk5JTkcgW2NvM10gVW52ZXJpZmllZCBIVFRQUyByZXF1ZXN0cyAoY2FmaWxlPWZhbHNlKS4KMjAyMi0wOS0wOSAxODoxOTo1MiwyODcgSU5GTyBbY28zYmFzZV0gVXNpbmcgb3JnIG5hbWU6IFRlc3QgT3JnYW5pemF0aW9uCjIwMjItMDktMDkgMTg6MTk6NTIsNDY3IElORk8gW2RlY29yYXRvcnNdIFtmbl90aW1lcl0gU3RhdHVzTWVzc2FnZTogU2xlZXBpbmcgZm9yIDc1cy4gMC8zMDBzIGNvbXBsZXRlLgoyMDIyLTA5LTA5IDE4OjIxOjA3LDYxMSBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IFdvcmtmbG93IHdhcyB0ZXJtaW5hdGVkLgoyMDIyLTA5LTA5IDE4OjIxOjA3LDYxMiBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IFRvdGFsIHNsZWVwIHRpbWUgNzUgc2Vjb25kcyBjb21wbGV0ZS4KMjAyMi0wOS0wOSAxODoyMTowNyw2MTYgSU5GTyBbZGVjb3JhdG9yc10gW2ZuX3RpbWVyXSBSZXR1cm5pbmcgcmVzdWx0cwoyMDIyLTA5LTA5IDE4OjIxOjA3LDYxNiBJTkZPIFtkZWNvcmF0b3JzXSBbZm5fdGltZXJdIFN0YXR1c01lc3NhZ2U6IEZpbmlzaGVkIHJ1bm5pbmcgQXBwIEZ1bmN0aW9uOiAnZm5fdGltZXIn",
  "content_type": "application/octet-stream",
  "created": 1663177933110,
  "filename": "fn_timer.log",
  "size": 14094
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.incident_id = incident.id
inputs.artifact_id = artifact.id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.artifact_attachment_to_base64_result

if results.get("content") is not None:
    file_name = str(results.get("filename", ""))
    preview = results.get("content", "")[0:20]
    note_text = f"<b>SOAR Utils: (Artifact) Attachment to Base64 - Example (PB)</b> File {file_name} converted to base64 format: {preview}... successfully."
    incident.addNote(note_text)

```

</p>
</details>

---
## Function - SOAR Utilities: Attachment Zip Extract
Extracts a file from a ZIP file attachment, producing a base64 string.

That string can then be used as input to subsequent functions that might write it as a file attachment, as a malware sample artifact, or in other ways.

 ![screenshot: fn-soar-utilities-attachment-zip-extract ](./doc/screenshots/fn-soar-utilities-attachment-zip-extract.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `attachment_id` | `number` | No | `-` | - |
| `incident_id` | `number` | Yes | `-` | - |
| `soar_utils_file_path` | `text` | No | `-` | - |
| `soar_utils_zipfile_password` | `text` | No | `-` | - |
| `task_id` | `number` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": "eyJhY3Rpb25fb3JkZXIiO*******dGlvbnMiOiBbeyJhdXRvbWF0aW9ucyI6IFtdLCAiY29uZGl0aW9ucyI6IFtdLCAiZW5hYmxlZCI6IHRydWUsICJleHBvcnRfa2V5IjogIkV4YW1wbGU6IEFyY2hpdmUgSW5jaWRlbnQgU2xhY2sgQ2hhbm5lbCIsICJpZCI6IDM3LCAibG9naWNfdHlwZSI6ICJhbGwiLCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbXSwgIm5hbWUiOiAiRXhhbXBsZTogQXJjaGl2ZSBJbmNpZGVudCBTbGFjayBDaGFubmVsIiwgIm9iamVjdF90eXBlIjogImluY2lkZW50IiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ0eXBlIjogMSwgInV1aWQiOiAiMTgzNTI0OGQtY2I1OC00NWM2LThiYjYtZTMwYmUyNWZlNWUzIiwgInZpZXdfaXRlbXMiOiBbeyJjb250ZW50IjogIjdjYmJiZmRmLWYxYTAtNGUzMi05ZTVjLTYzMmExODM1ZGUxZSIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9XSwgIndvcmtmbG93cyI6IFsiYXJjaGl2ZV9zbGFja19jaGFubmVsIl19LCB7ImF1dG9tYXRpb25zIjogW10sICJjb25kaXRpb25zIjogW10sICJlbmFibGVkIjogdHJ1ZSwgImV4cG9ydF9rZXkiOiAiRXhhbXBsZTogQXJjaGl2ZSBUYXNrIFNsYWNrIENoYW5uZWwiLCAiaWQiOiAzOCwgImxvZ2ljX3R5cGUiOiAiYWxsIiwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW10sICJuYW1lIjogIkV4YW1wbGU6IEFyY2hpdmUgVGFzayBTbGFjayBDaGFubmVsIiwgIm9iamVjdF90eXBlIjogInRhc2siLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ0aW1lb3V0X3NlY29uZHMiOiA4NjQwMCwgInR5cGUiOiAxLCAidXVpZCI6ICIwY2U5OGNjZi0xOTdkLTQ1ZWQtOTU0My04YTlkNTlmMGU3NjciLCAidmlld19pdGVtcyI6IFt7ImNvbnRlbnQiOiAiN2NiYmJmZGYtZjFhMC00ZTMyLTllNWMtNjMyYTE4MzVkZTFlIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH1dLCAid29ya2Zsb3dzIjogWyJzbGFja19leGFtcGxlX2FyY2hpdmVfc2xhY2tfY2hhbm5lbF9fdGFzayJdfSwgeyJhdXRvbWF0aW9ucyI6IFtdLCAiY29uZGl0aW9ucyI6IFt7ImV2YWx1YXRpb25faWQiOiBudWxsLCAiZmllbGRfbmFtZSI6ICJhcnRpZmFjdC50eXBlIiwgIm1ldGhvZCI6ICJpbiIsICJ0eXBlIjogbnVsbCwgInZhbHVlIjogWyJSRkMgODIyIEVtYWlsIE1lc3NhZ2UgRmlsZSIsICJFbWFpbCBBdHRhY2htZW50IiwgIkxvZyBGaWxlIiwgIk90aGVyIEZpbGUiLCAiWDUwOSBDZXJ0aWZpY2F0ZSBGaWxlIl19XSwgImVuYWJsZWQiOiB0cnVlLCAiZXhwb3J0X2tleSI6ICJFeGFtcGxlOiBQb3N0IEFydGlmYWN0IEF0dGFjaG1lbnQgdG8gU2xhY2siLCAiaWQiOiAzOSwgImxvZ2ljX3R5cGUiOiAiYWxsIiwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW10sICJuYW1lIjogIkV4YW1wbGU6IFBvc3QgQXJ0aWZhY3QgQXR0YWNobWVudCB0byBTbGFjayIsICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInRpbWVvdXRfc2Vjb25kcyI6IDg2NDAwLCAidHlwZSI6IDEsICJ1dWlkIjogIjBhODU3MGJlLWM2YmEtNGYxZC04M2ExLTY3YmQ5NTY0Nzk3NSIsICJ2aWV3X2l0ZW1zIjogW3siY29udGVudCI6ICIyNGRmM2UxYy0yYzI4LTRlN2QtYWMyOC00ZmVhMGEzODc3YTIiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjNiMWE2NjI4LTVlZjAtNDk1Yy05NTVlLTEwYzNlNWY5ZjRlMiIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiN2NiYmJmZGYtZjFhMC00ZTMyLTllNWMtNjMyYTE4MzVkZTFlIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICJiMmRmNDRlMi01YWU2LTQzYWUtYjg2Yy05YzVmNDc1ZjljNzkiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjJmMGZjYWQzLTc5ZjEtNDEwYi1iN2YwLTZhNmZhMGVlMzk0NyIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9XSwgIndvcmtmbG93cyI6IFsiZXhhbXBsZV9wb3N0X2F0dGFjaG1lbnRfdG9fc2xhY2tfX2FydGlmYWN0Il19LCB7ImF1dG9tYXRpb25zIjogW10sICJjb25kaXRpb25zIjogW3siZXZhbHVhdGlvbl9pZCI6IG51bGwsICJmaWVsZF9uYW1lIjogImFydGlmYWN0LnR5cGUiLCAibWV0aG9kIjogIm5vdF9pbiIsICJ0eXBlIjogbnVsbCwgInZhbHVlIjogWyJSRkMgODIyIEVtYWlsIE1lc3NhZ2UgRmlsZSIsICJFbWFpbCBBdHRhY2htZW50IiwgIkxvZyBGaWxlIiwgIk90aGVyIEZpbGUiLCAiWDUwOSBDZXJ0aWZpY2F0ZSBGaWxlIl19XSwgImVuYWJsZWQiOiB0cnVlLCAiZXhwb3J0X2tleSI6ICJFeGFtcGxlOiBQb3N0IEFydGlmYWN0IHRvIFNsYWNrIiwgImlkIjogNDAsICJsb2dpY190eXBlIjogImFsbCIsICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFtdLCAibmFtZSI6ICJFeGFtcGxlOiBQb3N0IEFydGlmYWN0IHRvIFNsYWNrIiwgIm9iamVjdF90eXBlIjogImFydGlmYWN0IiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ0eXBlIjogMSwgInV1aWQiOiAiZGZkNzNiMjItNDQzOC00NmVhLTllMDEtODg4ZWRjMDE3NGU3IiwgInZpZXdfaXRlbXMiOiBbeyJjb250ZW50IjogIjI0ZGYzZTFjLTJjMjgtNGU3ZC1hYzI4LTRmZWEwYTM4NzdhMiIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiM2IxYTY2MjgtNWVmMC00OTVjLTk1NWUtMTBjM2U1ZjlmNGUyIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICJiMmRmNDRlMi01YWU2LTQzYWUtYjg2Yy05YzVmNDc1ZjljNzkiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjJmMGZjYWQzLTc5ZjEtNDEwYi1iN2YwLTZhNmZhMGVlMzk0NyIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiN2NiYmJmZGYtZjFhMC00ZTMyLTllNWMtNjMyYTE4MzVkZTFlIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH1dLCAid29ya2Zsb3dzIjogWyJzbGFja19leGFtcGxlX3Bvc3RfbWVzc2FnZV90b19zbGFja19fYXJ0aWZhY3QiXX0sIHsiYXV0b21hdGlvbnMiOiBbXSwgImNvbmRpdGlvbnMiOiBbXSwgImVuYWJsZWQiOiB0cnVlLCAiZXhwb3J0X2tleSI6ICJFeGFtcGxlOiBQb3N0IEluY2lkZW50IC8gVGFzayBBdHRhY2htZW50IHRvIFNsYWNrIiwgImlkIjogNDEsICJsb2dpY190eXBlIjogImFsbCIsICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFtdLCAibmFtZSI6ICJFeGFtcGxlOiBQb3N0IEluY2lkZW50IC8gVGFzayBBdHRhY2htZW50IHRvIFNsYWNrIiwgIm9iamVjdF90eXBlIjogImF0dGFjaG1lbnQiLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ0aW1lb3V0X3NlY29uZHMiOiA4NjQwMCwgInR5cGUiOiAxLCAidXVpZCI6ICI0YmQ0NzcxMi1iYzkyLTQwNWQtOTM2Ny0zOWFmZmU1NDRiOTEiLCAidmlld19pdGVtcyI6IFt7ImNvbnRlbnQiOiAiMjRkZjNlMWMtMmMyOC00ZTdkLWFjMjgtNGZlYTBhMzg3N2EyIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICIzYjFhNjYyOC01ZWYwLTQ5NWMtOTU1ZS0xMGMzZTVmOWY0ZTIiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjdjYmJiZmRmLWYxYTAtNGUzMi05ZTVjLTYzMmExODM1ZGUxZSIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiYjJkZjQ0ZTItNWFlNi00M2FlLWI4NmMtOWM1ZjQ3NWY5Yzc5IiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICIyZjBmY2FkMy03OWYxLTQxMGItYjdmMC02YTZmYTBlZTM5NDciLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfV0sICJ3b3JrZmxvd3MiOiBbInNsYWNrX2V4YW1wbGVfcG9zdF9hdHRhY2htZW50X3RvX3NsYWNrIl19LCB7ImF1dG9tYXRpb25zIjogW10sICJjb25kaXRpb25zIjogW10sICJlbmFibGVkIjogdHJ1ZSwgImV4cG9ydF9rZXkiOiAiRXhhbXBsZTogUG9zdCBJbmNpZGVudCB0byBTbGFjayIsICJpZCI6IDQyLCAibG9naWNfdHlwZSI6ICJhbGwiLCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbXSwgIm5hbWUiOiAiRXhhbXBsZTogUG9zdCBJbmNpZGVudCB0byBTbGFjayIsICJvYmplY3RfdHlwZSI6ICJpbmNpZGVudCIsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInRpbWVvdXRfc2Vjb25kcyI6IDg2NDAwLCAidHlwZSI6IDEsICJ1dWlkIjogImM5MTU2MTllLWNhMTEtNGZiMS1iYTlkLWEyZDk0MzljOTJmMiIsICJ2aWV3X2l0ZW1zIjogW3siY29udGVudCI6ICIyNGRmM2UxYy0yYzI4LTRlN2QtYWMyOC00ZmVhMGEzODc3YTIiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjNiMWE2NjI4LTVlZjAtNDk1Yy05NTVlLTEwYzNlNWY5ZjRlMiIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiN2NiYmJmZGYtZjFhMC00ZTMyLTllNWMtNjMyYTE4MzVkZTFlIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICJiMmRmNDRlMi01YWU2LTQzYWUtYjg2Yy05YzVmNDc1ZjljNzkiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjJmMGZjYWQzLTc5ZjEtNDEwYi1iN2YwLTZhNmZhMGVlMzk0NyIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9XSwgIndvcmtmbG93cyI6IFsiY3JlYXRlX3NsYWNrX21lc3NhZ2UiXX0sIHsiYXV0b21hdGlvbnMiOiBbXSwgImNvbmRpdGlvbnMiOiBbXSwgImVuYWJsZWQiOiB0cnVlLCAiZXhwb3J0X2tleSI6ICJFeGFtcGxlOiBQb3N0IE5vdGUgdG8gU2xhY2siLCAiaWQiOiA0MywgImxvZ2ljX3R5cGUiOiAiYWxsIiwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW10sICJuYW1lIjogIkV4YW1wbGU6IFBvc3QgTm90ZSB0byBTbGFjayIsICJvYmplY3RfdHlwZSI6ICJub3RlIiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ0eXBlIjogMSwgInV1aWQiOiAiYWM1MDY2ZTctMjY0NC00OGUzLTllY2ItODVlYzJjMTZiYjZkIiwgInZpZXdfaXRlbXMiOiBbeyJjb250ZW50IjogIjI0ZGYzZTFjLTJjMjgtNGU3ZC1hYzI4LTRmZWEwYTM4NzdhMiIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiM2IxYTY2MjgtNWVmMC00OTVjLTk1NWUtMTBjM2U1ZjlmNGUyIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICI3Y2JiYmZkZi1mMWEwLTRlMzItOWU1Yy02MzJhMTgzNWRlMWUiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogImIyZGY0NGUyLTVhZTYtNDNhZS1iODZjLTljNWY0NzVmOWM3OSIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiMmYwZmNhZDMtNzlmMS00MTBiLWI3ZjAtNmE2ZmEwZWUzOTQ3IiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH1dLCAid29ya2Zsb3dzIjogWyJjcmVhdGVfc2xhY2tfcmVwbHkiXX0sIHsiYXV0b21hdGlvbnMiOiBbXSwgImNvbmRpdGlvbnMiOiBbXSwgImVuYWJsZWQiOiB0cnVlLCAiZXhwb3J0X2tleSI6ICJFeGFtcGxlOiBQb3N0IFRhc2sgdG8gU2xhY2siLCAiaWQiOiA0NCwgImxvZ2ljX3R5cGUiOiAiYWxsIiwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW10sICJuYW1lIjogIkV4YW1wbGU6IFBvc3QgVGFzayB0byBTbGFjayIsICJvYmplY3RfdHlwZSI6ICJ0YXNrIiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ0eXBlIjogMSwgInV1aWQiOiAiMTU0MjIxY2QtZjFjMS00YzZjLWI0ZDItNjFmZjcwOWUyM2ZiIiwgInZpZXdfaXRlbXMiOiBbeyJjb250ZW50IjogIjI0ZGYzZTFjLTJjMjgtNGU3ZC1hYzI4LTRmZWEwYTM4NzdhMiIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiM2IxYTY2MjgtNWVmMC00OTVjLTk1NWUtMTBjM2U1ZjlmNGUyIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICI3Y2JiYmZkZi1mMWEwLTRlMzItOWU1Yy02MzJhMTgzNWRlMWUiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiYWN0aW9uaW52b2NhdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogImIyZGY0NGUyLTVhZTYtNDNhZS1iODZjLTljNWY0NzVmOWM3OSIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJhY3Rpb25pbnZvY2F0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiMmYwZmNhZDMtNzlmMS00MTBiLWI3ZjAtNmE2ZmEwZWUzOTQ3IiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogImFjdGlvbmludm9jYXRpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH1dLCAid29ya2Zsb3dzIjogWyJzbGFja19leGFtcGxlX3Bvc3RfbWVzc2FnZV90b19zbGFja19fdGFzayJdfV0sICJhcHBzIjogW10sICJhdXRvbWF0aWNfdGFza3MiOiBbXSwgImV4cG9ydF9kYXRlIjogMTY1OTU1NjcyMjcxMywgImV4cG9ydF9mb3JtYXRfdmVyc2lvbiI6IDIsICJleHBvcnRfdHlwZSI6IG51bGwsICJmaWVsZHMiOiBbeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9zbGFja190ZXh0IiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDMxMywgImlucHV0X3R5cGUiOiAidGV4dCIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6ICJzbGFja190ZXh0IiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6IG51bGwsICJyZWFkX29ubHkiOiBmYWxzZSwgInJlcXVpcmVkIjogImFsd2F5cyIsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogInNsYWNrX3RleHQiLCAidG9vbHRpcCI6ICJUZXh0IG1lc3NhZ2Ugb3IgYSBjb250YWluZXIgZmllbGQgdG8gcmV0YWluIEpTT04gZmllbGRzIHRvIHNlbmQgdG8gU2xhY2suIiwgInR5cGVfaWQiOiAxMSwgInV1aWQiOiAiODVkMjBiNzctNzM0Zi00OTMwLTljNGItYjVmOGQ5OGM1ODFjIiwgInZhbHVlcyI6IFtdfSwgeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi90YXNrX2lkIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDI5OCwgImlucHV0X3R5cGUiOiAibnVtYmVyIiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInRhc2tfaWQiLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJvcGVyYXRpb25zIjogW10sICJwbGFjZWhvbGRlciI6ICIiLCAicHJlZml4IjogbnVsbCwgInJlYWRfb25seSI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJ0YXNrX2lkIiwgInRvb2x0aXAiOiAiIiwgInR5cGVfaWQiOiAxMSwgInV1aWQiOiAiOTU4ZjA5NTMtOGI2Zi00NDcyLWI3ODYtYjlhZTQzNTFkZGZlIiwgInZhbHVlcyI6IFtdfSwgeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9zbGFja19jaGFubmVsX2lkIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDMxNiwgImlucHV0X3R5cGUiOiAidGV4dCIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6ICJzbGFja19jaGFubmVsX2lkIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiT3B0aW9uYWwiLCAicHJlZml4IjogbnVsbCwgInJlYWRfb25seSI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJzbGFja19jaGFubmVsX2lkIiwgInRvb2x0aXAiOiAiT3B0aW9uYWwuIEV4ZWN1dGluZyB3aXRob3V0IGNoYW5uZWwgSUQgYXJjaGl2ZXMgdGhlIGNoYW5uZWwgdGhhdCB0aGlzIGlzIGFzc29jaWF0ZWQgd2l0aC4iLCAidHlwZV9pZCI6IDExLCAidXVpZCI6ICI5ODQ2ZGYzMS01Yjc2LTQyOTktYjEyYi0xN2UwYzY1NTE3OTEiLCAidmFsdWVzIjogW119LCB7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL2F0dGFjaG1lbnRfaWQiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMjkxLCAiaW5wdXRfdHlwZSI6ICJudW1iZXIiLCAiaW50ZXJuYWwiOiBmYWxzZSwgImlzX3RyYWNrZWQiOiBmYWxzZSwgIm5hbWUiOiAiYXR0YWNobWVudF9pZCIsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgIm9wZXJhdGlvbnMiOiBbXSwgInBsYWNlaG9sZGVyIjogIiIsICJwcmVmaXgiOiBudWxsLCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogImF0dGFjaG1lbnRfaWQiLCAidG9vbHRpcCI6ICIiLCAidHlwZV9pZCI6IDExLCAidXVpZCI6ICI5OTk3ZTA0Yy1iZGJlLTRmN2MtOWI4Ny0yYmMwMzkwODI2ZmUiLCAidmFsdWVzIjogW119LCB7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL3NsYWNrX2NoYW5uZWwiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzEyLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInNsYWNrX2NoYW5uZWwiLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJvcGVyYXRpb25zIjogW10sICJwbGFjZWhvbGRlciI6ICIiLCAicHJlZml4IjogbnVsbCwgInJlYWRfb25seSI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJzbGFja19jaGFubmVsIiwgInRvb2x0aXAiOiAiTmFtZSBvZiB0aGUgZXhpc3Rpbmcgb3IgYSBuZXcgc2xhY2sgY2hhbm5lbCB1c2VkIHRvIHNlbmQgbWVzc2FnZSB0by4gQ2hhbm5lbCBuYW1lcyBjYW4gb25seSBjb250YWluIGxvd2VyY2FzZSBsZXR0ZXJzLCBudW1iZXJzLCBoeXBoZW5zLCBhbmQgdW5kZXJzY29yZXMsIGFuZCBtdXN0IGJlIDIxIGNoYXJhY3RlcnMgb3IgbGVzcy4iLCAidHlwZV9pZCI6IDExLCAidXVpZCI6ICI5Y2FhZGI4Ni0zY2IxLTQ0ZjgtODFmNC00ZGEzMGU2OGExMDYiLCAidmFsdWVzIjogW119LCB7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL3NsYWNrX3BhcnRpY2lwYW50X2VtYWlscyIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiaWQiOiAzMTQsICJpbnB1dF90eXBlIjogInRleHQiLCAiaW50ZXJuYWwiOiBmYWxzZSwgImlzX3RyYWNrZWQiOiBmYWxzZSwgIm5hbWUiOiAic2xhY2tfcGFydGljaXBhbnRfZW1haWxzIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6IG51bGwsICJyZWFkX29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ0ZW1wbGF0ZXMiOiBbXSwgInRleHQiOiAic2xhY2tfcGFydGljaXBhbnRfZW1haWxzIiwgInRvb2x0aXAiOiAiQ29tbWEgc2VwYXJhdGVkIGxpc3Qgb2YgZW1haWxzIGJlbG9uZ2luZyB0byBTbGFjayB1c2VycyBpbiB5b3VyIHdvcmtzcGFjZSB0aGF0IHdpbGwgYmUgYWRkZWQgdG8geW91ciBjaGFubmVsLiIsICJ0eXBlX2lkIjogMTEsICJ1dWlkIjogImFlODJhMjBhLWQ2YWUtNGY3Ny05OGQ4LTEzODhkZmE0YjJmNyIsICJ2YWx1ZXMiOiBbXX0sIHsiYWxsb3dfZGVmYXVsdF92YWx1ZSI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJkZXByZWNhdGVkIjogZmFsc2UsICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDMxNSwgImlucHV0X3R5cGUiOiAiYm9vbGVhbiIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6ICJzbGFja19pc19jaGFubmVsX3ByaXZhdGUiLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJvcGVyYXRpb25zIjogW10sICJwbGFjZWhvbGRlciI6ICIiLCAicHJlZml4IjogbnVsbCwgInJlYWRfb25seSI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJzbGFja19pc19jaGFubmVsX3ByaXZhdGUiLCAidG9vbHRpcCI6ICJJbmRpY2F0ZSBpZiB0aGUgY2hhbm5lbCB5b3UgYXJlIHBvc3RpbmcgdG8gc2hvdWxkIGJlIHByaXZhdGUuIiwgInR5cGVfaWQiOiAxMSwgInV1aWQiOiAiY2MyMzExMjYtNGY0OS00MjM3LTk5OGItZDk1NzA2NjRkNjYyIiwgInZhbHVlcyI6IFtdfSwgeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9hcnRpZmFjdF9pZCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiaWQiOiAyOTAsICJpbnB1dF90eXBlIjogIm51bWJlciIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6ICJhcnRpZmFjdF9pZCIsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgIm9wZXJhdGlvbnMiOiBbXSwgInBsYWNlaG9sZGVyIjogIiIsICJwcmVmaXgiOiBudWxsLCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogImFydGlmYWN0X2lkIiwgInRvb2x0aXAiOiAiIiwgInR5cGVfaWQiOiAxMSwgInV1aWQiOiAiZDYzZDE2YTEtYzViZC00MDE1LTk4NTAtMDUzMTZiMjI1NjRjIiwgInZhbHVlcyI6IFtdfSwgeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9zbGFja19tcmtkd24iLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzA5LCAiaW5wdXRfdHlwZSI6ICJib29sZWFuIiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInNsYWNrX21ya2R3biIsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgIm9wZXJhdGlvbnMiOiBbXSwgInBsYWNlaG9sZGVyIjogIiIsICJwcmVmaXgiOiBudWxsLCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogInNsYWNrX21ya2R3biIsICJ0b29sdGlwIjogIkRpc2FibGUgU2xhY2sgbWFya3VwIHBhcnNpbmcgYnkgc2V0dGluZyB0byBmYWxzZS4iLCAidHlwZV9pZCI6IDExLCAidXVpZCI6ICIyMzg4YmU0OS0yODNmLTRiNzctYmJlYi04NmEyZWUxZGNmMDgiLCAidmFsdWVzIjogW119LCB7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL2luY2lkZW50X2lkIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDI4OSwgImlucHV0X3R5cGUiOiAibnVtYmVyIiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogImluY2lkZW50X2lkIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6IG51bGwsICJyZWFkX29ubHkiOiBmYWxzZSwgInJlcXVpcmVkIjogImFsd2F5cyIsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogImluY2lkZW50X2lkIiwgInRvb2x0aXAiOiAiIiwgInR5cGVfaWQiOiAxMSwgInV1aWQiOiAiM2YzNWYxYTktZjVkNi00NDBhLWE4MjUtNjZhMzQwYWVhZWZlIiwgInZhbHVlcyI6IFtdfSwgeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9zbGFja19hc191c2VyIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDMxMCwgImlucHV0X3R5cGUiOiAiYm9vbGVhbiIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6ICJzbGFja19hc191c2VyIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6IG51bGwsICJyZWFkX29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ0ZW1wbGF0ZXMiOiBbXSwgInRleHQiOiAic2xhY2tfYXNfdXNlciIsICJ0b29sdGlwIjogIlNldCB0byB0cnVlIGFuZCB0aGUgYXV0aGVudGljYXRlZCB1c2VyIG9mIHRoZSBTbGFjayBBcHAgd2lsbCBhcHBlYXIgYXMgdGhlIGF1dGhvciBvZiB0aGUgbWVzc2FnZSwgaWdub3JpbmcgYW55IHZhbHVlcyBwcm92aWRlZCBmb3Igc2xhY2tfdXNlcm5hbWUuICIsICJ0eXBlX2lkIjogMTEsICJ1dWlkIjogIjQ4ZTU5M2Y0LTNjYzQtNGYzZS1hODA5LTM4ZTVmZWQ3MGYyMCIsICJ2YWx1ZXMiOiBbXX0sIHsiYWxsb3dfZGVmYXVsdF92YWx1ZSI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJkZXByZWNhdGVkIjogZmFsc2UsICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vc2xhY2tfdXNlcm5hbWUiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzExLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInNsYWNrX3VzZXJuYW1lIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6IG51bGwsICJyZWFkX29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ0ZW1wbGF0ZXMiOiBbXSwgInRleHQiOiAic2xhY2tfdXNlcm5hbWUiLCAidG9vbHRpcCI6ICJTZXQgeW91ciBTbGFjayBhcHAncyBuYW1lIHRoYXQgd2lsbCBhcHBlYXIgYXMgdGhlIGF1dGhvciBvZiB0aGUgbWVzc2FnZS4gTXVzdCBiZSB1c2VkIGluIGNvbmp1bmN0aW9uIHdpdGggc2xhY2tfYXNfdXNlciBzZXQgdG8gZmFsc2UsIG90aGVyd2lzZSBpZ25vcmVkLiIsICJ0eXBlX2lkIjogMTEsICJ1dWlkIjogIjc0MzY1ZWQyLTYzNWEtNDQ2YS1iYTM5LTY1YjI2NGI3YWQ1NCIsICJ2YWx1ZXMiOiBbXX0sIHsiYWxsb3dfZGVmYXVsdF92YWx1ZSI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJkZXByZWNhdGVkIjogZmFsc2UsICJleHBvcnRfa2V5IjogImFjdGlvbmludm9jYXRpb24vcnVsZV9zbGFja19wYXJ0aWNpcGFudF9lbWFpbHMiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzA3LCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInJ1bGVfc2xhY2tfcGFydGljaXBhbnRfZW1haWxzIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAic2xhY2sudXNlckBlbWFpbC5jb20sIHNsYWNrLnVzZXIyQGVtYWlsLmNvbSwgIiwgInByZWZpeCI6ICJwcm9wZXJ0aWVzIiwgInJlYWRfb25seSI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJTbGFjayB1c2VycyBlbWFpbHMiLCAidG9vbHRpcCI6ICJDb21tYSBzZXBhcmF0ZWQgbGlzdCBvZiBlbWFpbHMgYmVsb25naW5nIHRvIFNsYWNrIHVzZXJzIGluIHlvdXIgd29ya3NwYWNlIHRoYXQgd2lsbCBiZSBhZGRlZCB0byB0aGUgY2hhbm5lbCB5b3UgYXJlIHBvc3RpbmcgdG8uIiwgInR5cGVfaWQiOiA2LCAidXVpZCI6ICJiMmRmNDRlMi01YWU2LTQzYWUtYjg2Yy05YzVmNDc1ZjljNzkiLCAidmFsdWVzIjogW119LCB7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJhY3Rpb25pbnZvY2F0aW9uL3J1bGVfc2xhY2tfY2hhbm5lbCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiaWQiOiAzMDUsICJpbnB1dF90eXBlIjogInRleHQiLCAiaW50ZXJuYWwiOiBmYWxzZSwgImlzX3RyYWNrZWQiOiBmYWxzZSwgIm5hbWUiOiAicnVsZV9zbGFja19jaGFubmVsIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiRXhpc3Rpbmcgb3IgbmV3IFNsYWNrIGNoYW5uZWwgbmFtZSIsICJwcmVmaXgiOiAicHJvcGVydGllcyIsICJyZWFkX29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ0ZW1wbGF0ZXMiOiBbXSwgInRleHQiOiAiU2xhY2sgY2hhbm5lbCBuYW1lIiwgInRvb2x0aXAiOiAiTmFtZSBvZiB0aGUgZXhpc3RpbmcgU2xhY2sgY2hhbm5lbCBvciBhIG5ldyBTbGFjayBjaGFubmVsIHlvdSBhcmUgcG9zdGluZyB0by4gQ2hhbm5lbCBuYW1lcyBjYW4gb25seSBjb250YWluIGxvd2VyY2FzZSBsZXR0ZXJzLCBudW1iZXJzLCBoeXBoZW5zLCBhbmQgdW5kZXJzY29yZXMsIGFuZCBtdXN0IGJlIDIxIGNoYXJhY3RlcnMgb3IgbGVzcy4gSWYgeW91IGxlYXZlIHRoaXMgZmllbGQgZW1wdHksIGZ1bmN0aW9uIHdpbGwgdHJ5IHRvIHVzZSB0aGUgc2xhY2tfY2hhbm5lbCBhc3NvY2lhdGVkIHdpdGggdGhlIEluY2lkZW50IG9yIFRhc2sgZm91bmQgaW4gdGhlIFNsYWNrIENvbnZlcnNhdGlvbnMgZGF0YXRhYmxlLiBJZiB0aGVyZSBpc25cdTIwMTl0IG9uZSBkZWZpbmVkLCB0aGUgd29ya2Zsb3cgd2lsbCB0ZXJtaW5hdGUuIiwgInR5cGVfaWQiOiA2LCAidXVpZCI6ICIyNGRmM2UxYy0yYzI4LTRlN2QtYWMyOC00ZmVhMGEzODc3YTIiLCAidmFsdWVzIjogW119LCB7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJhY3Rpb25pbnZvY2F0aW9uL3J1bGVfc2xhY2tfdGV4dCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiaWQiOiAzMDYsICJpbnB1dF90eXBlIjogInRleHQiLCAiaW50ZXJuYWwiOiBmYWxzZSwgImlzX3RyYWNrZWQiOiBmYWxzZSwgIm5hbWUiOiAicnVsZV9zbGFja190ZXh0IiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiUGxlYXNlIHJldmlldyBwb3N0ZWQgUmVzaWxpZW50IERhdGEiLCAicHJlZml4IjogInByb3BlcnRpZXMiLCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogIkFkZGl0aW9uYWwgdGV4dCIsICJ0b29sdGlwIjogIkFkZGl0aW9uYWwgdGV4dCBtZXNzYWdlIHRvIGluY2x1ZGUgd2l0aCB0aGUgSW5jaWRlbnQsIE5vdGUsIEFydGlmYWN0LCBBdHRhY2htZW50IG9yIFRhc2sgZGF0YS4iLCAidHlwZV9pZCI6IDYsICJ1dWlkIjogIjJmMGZjYWQzLTc5ZjEtNDEwYi1iN2YwLTZhNmZhMGVlMzk0NyIsICJ2YWx1ZXMiOiBbXX0sIHsiYWxsb3dfZGVmYXVsdF92YWx1ZSI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJjYWxjdWxhdGVkIjogZmFsc2UsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJkZXByZWNhdGVkIjogZmFsc2UsICJleHBvcnRfa2V5IjogImFjdGlvbmludm9jYXRpb24vcnVsZV9zbGFja19pc19jaGFubmVsX3ByaXZhdGUiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzA4LCAiaW5wdXRfdHlwZSI6ICJib29sZWFuIiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInJ1bGVfc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6ICJwcm9wZXJ0aWVzIiwgInJlYWRfb25seSI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJTbGFjayBpcyBjaGFubmVsIHByaXZhdGUiLCAidG9vbHRpcCI6ICJJbmRpY2F0ZSBpZiB0aGUgY2hhbm5lbCB5b3UgYXJlIHBvc3RpbmcgdG8gc2hvdWxkIGJlIHByaXZhdGUuIiwgInR5cGVfaWQiOiA2LCAidXVpZCI6ICIzYjFhNjYyOC01ZWYwLTQ5NWMtOTU1ZS0xMGMzZTVmOWY0ZTIiLCAidmFsdWVzIjogW119LCB7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJhY3Rpb25pbnZvY2F0aW9uL3NsYWNrX2NoYW5uZWxfaWQiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzE3LCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInNsYWNrX2NoYW5uZWxfaWQiLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJvcGVyYXRpb25zIjogW10sICJwbGFjZWhvbGRlciI6ICJPcHRpb25hbCIsICJwcmVmaXgiOiAicHJvcGVydGllcyIsICJyZWFkX29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ0ZW1wbGF0ZXMiOiBbXSwgInRleHQiOiAiU2xhY2sgQ2hhbm5lbCBJRCIsICJ0b29sdGlwIjogIk9wdGlvbmFsLiBFeGVjdXRpbmcgd2l0aG91dCBjaGFubmVsIElEIGFyY2hpdmVzIHRoZSBjaGFubmVsIHRoYXQgdGhpcyBpcyBhc3NvY2lhdGVkIHdpdGguIiwgInR5cGVfaWQiOiA2LCAidXVpZCI6ICI3Y2JiYmZkZi1mMWEwLTRlMzItOWU1Yy02MzJhMTgzNWRlMWUiLCAidmFsdWVzIjogW119LCB7ImV4cG9ydF9rZXkiOiAiaW5jaWRlbnQvaW50ZXJuYWxfY3VzdG9taXphdGlvbnNfZmllbGQiLCAiaWQiOiAwLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjogdHJ1ZSwgIm5hbWUiOiAiaW50ZXJuYWxfY3VzdG9taXphdGlvbnNfZmllbGQiLCAicmVhZF9vbmx5IjogdHJ1ZSwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidGV4dCI6ICJDdXN0b21pemF0aW9ucyBGaWVsZCAoaW50ZXJuYWwpIiwgInR5cGVfaWQiOiAwLCAidXVpZCI6ICJiZmVlYzJkNC0zNzcwLTExZTgtYWQzOS00YTAwMDQwNDRhYTEifV0sICJmdW5jdGlvbnMiOiBbeyJjcmVhdGVkX2RhdGUiOiAxNjU2NTI0ODA4NDk5LCAiZGVzY3JpcHRpb24iOiB7ImNvbnRlbnQiOiAiRnVuY3Rpb24gZXhwb3J0cyBjb252ZXJzYXRpb24gaGlzdG9yeSBmcm9tIFNsYWNrIGNoYW5uZWwgdG8gYSB0ZXh0IGZpbGUsIHNhdmVzIHRoZSB0ZXh0IGZpbGUgYXMgYW4gQXR0YWNobWVudCBhbmQgYXJjaGl2ZXMgdGhlIFNsYWNrIGNoYW5uZWwuIiwgImZvcm1hdCI6ICJ0ZXh0In0sICJkZXN0aW5hdGlvbl9oYW5kbGUiOiAic2xhY2siLCAiZGlzcGxheV9uYW1lIjogIkFyY2hpdmUgU2xhY2sgQ2hhbm5lbCIsICJleHBvcnRfa2V5IjogInNsYWNrX2FyY2hpdmVfY2hhbm5lbCIsICJpZCI6IDE2LCAibGFzdF9tb2RpZmllZF9ieSI6IHsiZGlzcGxheV9uYW1lIjogIkFkbWluIFVzZXIiLCAiaWQiOiAxLCAibmFtZSI6ICJhZG1pbkBleGFtcGxlLmNvbSIsICJ0eXBlIjogInVzZXIifSwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE2NTg3Nzk0NTUzODgsICJuYW1lIjogInNsYWNrX2FyY2hpdmVfY2hhbm5lbCIsICJvdXRwdXRfanNvbl9leGFtcGxlIjogIntcImNoYW5uZWxcIjogXCJ0ZXN0djJcIn0iLCAib3V0cHV0X2pzb25fc2NoZW1hIjogIntcIiRzY2hlbWFcIjogXCJodHRwOi8vanNvbi1zY2hlbWEub3JnL2RyYWZ0LTA2L3NjaGVtYVwiLCBcInR5cGVcIjogXCJvYmplY3RcIiwgXCJwcm9wZXJ0aWVzXCI6IHtcImNoYW5uZWxcIjoge1widHlwZVwiOiBcInN0cmluZ1wifX19IiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXVpZCI6ICI4ZjNhOWQxZC04MTgyLTRjNWItYjQyMi1jZmVlZTMzZGUwZGMiLCAidmVyc2lvbiI6IDMsICJ2aWV3X2l0ZW1zIjogW3siY29udGVudCI6ICIzZjM1ZjFhOS1mNWQ2LTQ0MGEtYTgyNS02NmEzNDBhZWFlZmUiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjk4NDZkZjMxLTViNzYtNDI5OS1iMTJiLTE3ZTBjNjU1MTc5MSIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiOTU4ZjA5NTMtOGI2Zi00NDcyLWI3ODYtYjlhZTQzNTFkZGZlIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH1dLCAid29ya2Zsb3dzIjogW3siYWN0aW9ucyI6IFtdLCAiZGVzY3JpcHRpb24iOiBudWxsLCAibmFtZSI6ICJFeGFtcGxlOiBBcmNoaXZlIEluY2lkZW50IFNsYWNrIENoYW5uZWwiLCAib2JqZWN0X3R5cGUiOiAiaW5jaWRlbnQiLCAicHJvZ3JhbW1hdGljX25hbWUiOiAiYXJjaGl2ZV9zbGFja19jaGFubmVsIiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXVpZCI6IG51bGwsICJ3b3JrZmxvd19pZCI6IDM1fSwgeyJhY3Rpb25zIjogW10sICJkZXNjcmlwdGlvbiI6IG51bGwsICJuYW1lIjogIkV4YW1wbGU6IEFyY2hpdmUgVGFzayBTbGFjayBDaGFubmVsIiwgIm9iamVjdF90eXBlIjogInRhc2siLCAicHJvZ3JhbW1hdGljX25hbWUiOiAic2xhY2tfZXhhbXBsZV9hcmNoaXZlX3NsYWNrX2NoYW5uZWxfX3Rhc2siLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ1dWlkIjogbnVsbCwgIndvcmtmbG93X2lkIjogMzF9XX0sIHsiY3JlYXRlZF9kYXRlIjogMTY1NjUyNDgwODU4MSwgImRlc2NyaXB0aW9uIjogeyJjb250ZW50IjogIkZ1bmN0aW9uIHVwbG9hZHMgSW5jaWRlbnQsIFRhc2sgb3IgQXJ0aWZhY3QgQXR0YWNobWVudHMgdG8gU2xhY2sgY2hhbm5lbC4iLCAiZm9ybWF0IjogInRleHQifSwgImRlc3RpbmF0aW9uX2hhbmRsZSI6ICJzbGFjayIsICJkaXNwbGF5X25hbWUiOiAiUG9zdCBhdHRhY2htZW50IHRvIFNsYWNrIiwgImV4cG9ydF9rZXkiOiAic2xhY2tfcG9zdF9hdHRhY2htZW50IiwgImlkIjogMTcsICJsYXN0X21vZGlmaWVkX2J5IjogeyJkaXNwbGF5X25hbWUiOiAiQWRtaW4gVXNlciIsICJpZCI6IDEsICJuYW1lIjogImFkbWluQGV4YW1wbGUuY29tIiwgInR5cGUiOiAidXNlciJ9LCAibGFzdF9tb2RpZmllZF90aW1lIjogMTY1ODk1Mzc3Njg4NSwgIm5hbWUiOiAic2xhY2tfcG9zdF9hdHRhY2htZW50IiwgIm91dHB1dF9qc29uX2V4YW1wbGUiOiAie1wiY2hhbm5lbFwiOiBcInRlc3Rpbmd2MlwiLCBcInVybFwiOiBcImh0dHBzOi8vaWJtLXJlc2lsaWVudC10ZXN0LnNsYWNrLmNvbS9hcmNoaXZlcy9DMDNRWkdWMFlKVS9wMTY1ODMzMDY4ODI0MTEyOVwifSIsICJvdXRwdXRfanNvbl9zY2hlbWEiOiAie1wiJHNjaGVtYVwiOiBcImh0dHA6Ly9qc29uLXNjaGVtYS5vcmcvZHJhZnQtMDYvc2NoZW1hXCIsIFwidHlwZVwiOiBcIm9iamVjdFwiLCBcInByb3BlcnRpZXNcIjoge1wiY2hhbm5lbFwiOiB7XCJ0eXBlXCI6IFwic3RyaW5nXCJ9LCBcInVybFwiOiB7XCJ0eXBlXCI6IFwic3RyaW5nXCJ9fX0iLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ1dWlkIjogIjVmZWQ0ZGQ1LTljY2MtNDkyYS05MGUxLTRmMTdlNmE1YzVjOCIsICJ2ZXJzaW9uIjogMywgInZpZXdfaXRlbXMiOiBbeyJjb250ZW50IjogIjljYWFkYjg2LTNjYjEtNDRmOC04MWY0LTRkYTMwZTY4YTEwNiIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiY2MyMzExMjYtNGY0OS00MjM3LTk5OGItZDk1NzA2NjRkNjYyIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICJhZTgyYTIwYS1kNmFlLTRmNzctOThkOC0xMzg4ZGZhNGIyZjciLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjg1ZDIwYjc3LTczNGYtNDkzMC05YzRiLWI1ZjhkOThjNTgxYyIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiOTg0NmRmMzEtNWI3Ni00Mjk5LWIxMmItMTdlMGM2NTUxNzkxIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICIzZjM1ZjFhOS1mNWQ2LTQ0MGEtYTgyNS02NmEzNDBhZWFlZmUiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjk1OGYwOTUzLThiNmYtNDQ3Mi1iNzg2LWI5YWU0MzUxZGRmZSIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiZDYzZDE2YTEtYzViZC00MDE1LTk4NTAtMDUzMTZiMjI1NjRjIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICI5OTk3ZTA0Yy1iZGJlLTRmN2MtOWI4Ny0yYmMwMzkwODI2ZmUiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfV0sICJ3b3JrZmxvd3MiOiBbeyJhY3Rpb25zIjogW10sICJkZXNjcmlwdGlvbiI6IG51bGwsICJuYW1lIjogIkV4YW1wbGU6IFBvc3QgQXJ0aWZhY3QgQXR0YWNobWVudCB0byBTbGFjayIsICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJleGFtcGxlX3Bvc3RfYXR0YWNobWVudF90b19zbGFja19fYXJ0aWZhY3QiLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ1dWlkIjogbnVsbCwgIndvcmtmbG93X2lkIjogMzN9LCB7ImFjdGlvbnMiOiBbXSwgImRlc2NyaXB0aW9uIjogbnVsbCwgIm5hbWUiOiAiRXhhbXBsZTogUG9zdCBJbmNpZGVudCAvIFRhc2sgQXR0YWNobWVudCB0byBTbGFjayIsICJvYmplY3RfdHlwZSI6ICJhdHRhY2htZW50IiwgInByb2dyYW1tYXRpY19uYW1lIjogInNsYWNrX2V4YW1wbGVfcG9zdF9hdHRhY2htZW50X3RvX3NsYWNrIiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXVpZCI6IG51bGwsICJ3b3JrZmxvd19pZCI6IDM0fV19LCB7ImNyZWF0ZWRfZGF0ZSI6IDE2NTY1MjQ4MDg2NjEsICJkZXNjcmlwdGlvbiI6IHsiY29udGVudCI6ICJGdW5jdGlvbiBzZW5kcyBhIG1lc3NhZ2UgZnJvbSBhbiBJbmNpZGVudCwgVGFzaywgTm90ZSBvciBhbiBBcnRpZmFjdCB0byBhIFNsYWNrIGNoYW5uZWwuIiwgImZvcm1hdCI6ICJ0ZXh0In0sICJkZXN0aW5hdGlvbl9oYW5kbGUiOiAic2xhY2siLCAiZGlzcGxheV9uYW1lIjogIlBvc3QgbWVzc2FnZSB0byBTbGFjayIsICJleHBvcnRfa2V5IjogInNsYWNrX3Bvc3RfbWVzc2FnZSIsICJpZCI6IDE4LCAibGFzdF9tb2RpZmllZF9ieSI6IHsiZGlzcGxheV9uYW1lIjogIkFkbWluIFVzZXIiLCAiaWQiOiAxLCAibmFtZSI6ICJhZG1pbkBleGFtcGxlLmNvbSIsICJ0eXBlIjogInVzZXIifSwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE2NTg5NDQzNTcxMjgsICJuYW1lIjogInNsYWNrX3Bvc3RfbWVzc2FnZSIsICJvdXRwdXRfanNvbl9leGFtcGxlIjogIntcImNoYW5uZWxcIjogXCJ0ZXN0aW5ndjJcIiwgXCJ1cmxcIjogXCJodHRwczovL2libS1yZXNpbGllbnQtdGVzdC5zbGFjay5jb20vYXJjaGl2ZXMvQzAzUVpHVjBZSlUvcDE2NTgzMzA3NTE3NTI4MTlcIn0iLCAib3V0cHV0X2pzb25fc2NoZW1hIjogIntcIiRzY2hlbWFcIjogXCJodHRwOi8vanNvbi1zY2hlbWEub3JnL2RyYWZ0LTA2L3NjaGVtYVwiLCBcInR5cGVcIjogXCJvYmplY3RcIiwgXCJwcm9wZXJ0aWVzXCI6IHtcImNoYW5uZWxcIjoge1widHlwZVwiOiBcInN0cmluZ1wifSwgXCJ1cmxcIjoge1widHlwZVwiOiBcInN0cmluZ1wifX19IiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXVpZCI6ICJkZWQyODI2Yy02NTI4LTRhMjYtYjJjOC0wY2YyMTVkY2UzYzMiLCAidmVyc2lvbiI6IDMsICJ2aWV3X2l0ZW1zIjogW3siY29udGVudCI6ICI5Y2FhZGI4Ni0zY2IxLTQ0ZjgtODFmNC00ZGEzMGU2OGExMDYiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogImNjMjMxMTI2LTRmNDktNDIzNy05OThiLWQ5NTcwNjY0ZDY2MiIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiYWU4MmEyMGEtZDZhZS00Zjc3LTk4ZDgtMTM4OGRmYTRiMmY3IiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICI4NWQyMGI3Ny03MzRmLTQ5MzAtOWM0Yi1iNWY4ZDk4YzU4MWMiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjIzODhiZTQ5LTI4M2YtNGI3Ny1iYmViLTg2YTJlZTFkY2YwOCIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiNDhlNTkzZjQtM2NjNC00ZjNlLWE4MDktMzhlNWZlZDcwZjIwIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICI5ODQ2ZGYzMS01Yjc2LTQyOTktYjEyYi0xN2UwYzY1NTE3OTEiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJjb250ZW50IjogIjc0MzY1ZWQyLTYzNWEtNDQ2YS1iYTM5LTY1YjI2NGI3YWQ1NCIsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfaWYiOiBudWxsLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7ImNvbnRlbnQiOiAiM2YzNWYxYTktZjVkNi00NDBhLWE4MjUtNjZhMzQwYWVhZWZlIiwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19pZiI6IG51bGwsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsiY29udGVudCI6ICI5NThmMDk1My04YjZmLTQ0NzItYjc4Ni1iOWFlNDM1MWRkZmUiLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2lmIjogbnVsbCwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgInN0ZXBfbGFiZWwiOiBudWxsfV0sICJ3b3JrZmxvd3MiOiBbeyJhY3Rpb25zIjogW10sICJkZXNjcmlwdGlvbiI6IG51bGwsICJuYW1lIjogIkV4YW1wbGU6IFBvc3QgQXJ0aWZhY3QgdG8gU2xhY2siLCAib2JqZWN0X3R5cGUiOiAiYXJ0aWZhY3QiLCAicHJvZ3JhbW1hdGljX25hbWUiOiAic2xhY2tfZXhhbXBsZV9wb3N0X21lc3NhZ2VfdG9fc2xhY2tfX2FydGlmYWN0IiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXVpZCI6IG51bGwsICJ3b3JrZmxvd19pZCI6IDM3fSwgeyJhY3Rpb25zIjogW10sICJkZXNjcmlwdGlvbiI6IG51bGwsICJuYW1lIjogIkV4YW1wbGU6IFBvc3QgSW5jaWRlbnQgdG8gU2xhY2siLCAib2JqZWN0X3R5cGUiOiAiaW5jaWRlbnQiLCAicHJvZ3JhbW1hdGljX25hbWUiOiAiY3JlYXRlX3NsYWNrX21lc3NhZ2UiLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ1dWlkIjogbnVsbCwgIndvcmtmbG93X2lkIjogMzJ9LCB7ImFjdGlvbnMiOiBbXSwgImRlc2NyaXB0aW9uIjogbnVsbCwgIm5hbWUiOiAiRXhhbXBsZTogUG9zdCBOb3RlIHRvIFNsYWNrIiwgIm9iamVjdF90eXBlIjogIm5vdGUiLCAicHJvZ3JhbW1hdGljX25hbWUiOiAiY3JlYXRlX3NsYWNrX3JlcGx5IiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXVpZCI6IG51bGwsICJ3b3JrZmxvd19pZCI6IDM4fSwgeyJhY3Rpb25zIjogW10sICJkZXNjcmlwdGlvbiI6IG51bGwsICJuYW1lIjogIkV4YW1wbGU6IFBvc3QgVGFzayB0byBTbGFjayIsICJvYmplY3RfdHlwZSI6ICJ0YXNrIiwgInByb2dyYW1tYXRpY19uYW1lIjogInNsYWNrX2V4YW1wbGVfcG9zdF9tZXNzYWdlX3RvX3NsYWNrX190YXNrIiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXVpZCI6IG51bGwsICJ3b3JrZmxvd19pZCI6IDM2fV19XSwgImdlb3MiOiBudWxsLCAiZ3JvdXBzIjogbnVsbCwgImlkIjogMTE0LCAiaW5ib3VuZF9kZXN0aW5hdGlvbnMiOiBbXSwgImluYm91bmRfbWFpbGJveGVzIjogbnVsbCwgImluY2lkZW50X2FydGlmYWN0X3R5cGVzIjogW10sICJpbmNpZGVudF90eXBlcyI6IFt7ImNyZWF0ZV9kYXRlIjogMTY1OTU1NjcxODgzOCwgImRlc2NyaXB0aW9uIjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJlbmFibGVkIjogZmFsc2UsICJleHBvcnRfa2V5IjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJoaWRkZW4iOiBmYWxzZSwgImlkIjogMCwgIm5hbWUiOiAiQ3VzdG9taXphdGlvbiBQYWNrYWdlcyAoaW50ZXJuYWwpIiwgInBhcmVudF9pZCI6IG51bGwsICJzeXN0ZW0iOiBmYWxzZSwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXBkYXRlX2RhdGUiOiAxNjU5NTU2NzE4ODM4LCAidXVpZCI6ICJiZmVlYzJkNC0zNzcwLTExZTgtYWQzOS00YTAwMDQwNDRhYTAifV0sICJpbmR1c3RyaWVzIjogbnVsbCwgImxheW91dHMiOiBbXSwgImxvY2FsZSI6IG51bGwsICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFt7ImFwaV9rZXlzIjogWyIwMjI4ZTAwZS0yYzQ3LTQzZTYtYTczNi01NTBmMTA0Yzk0ZWEiLCAiYmVmMTk4YzUtY2M1NC00Mzc3LTk1YzUtZjk4YmYyY2NjZmQ4Il0sICJkZXN0aW5hdGlvbl90eXBlIjogMCwgImV4cGVjdF9hY2siOiB0cnVlLCAiZXhwb3J0X2tleSI6ICJzbGFjayIsICJuYW1lIjogInNsYWNrIiwgInByb2dyYW1tYXRpY19uYW1lIjogInNsYWNrIiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXNlcnMiOiBbXSwgInV1aWQiOiAiNjExZjEwZjctMWI3ZC00OWM1LTg2OTItM2I4MzgxNTZkNDJiIn1dLCAibm90aWZpY2F0aW9ucyI6IG51bGwsICJvdmVycmlkZXMiOiBbXSwgInBoYXNlcyI6IFtdLCAicGxheWJvb2tzIjogbnVsbCwgInJlZ3VsYXRvcnMiOiBudWxsLCAicm9sZXMiOiBbXSwgInNjcmlwdHMiOiBbXSwgInNlcnZlcl92ZXJzaW9uIjogeyJidWlsZF9udW1iZXIiOiA0OSwgIm1ham9yIjogNDMsICJtaW5vciI6IDEsICJ2ZXJzaW9uIjogIjQzLjEuNDkifSwgInRhZ3MiOiBbXSwgInRhc2tfb3JkZXIiOiBbXSwgInRpbWVmcmFtZXMiOiBudWxsLCAidHlwZXMiOiBbeyJhY3Rpb25zIjogW10sICJkaXNwbGF5X25hbWUiOiAiU2xhY2sgQ29udmVyc2F0aW9ucyIsICJleHBvcnRfa2V5IjogInNsYWNrX2NvbnZlcnNhdGlvbnNfZGIiLCAiZmllbGRzIjogeyJzbGFja19kYl9jaGFubmVsIjogeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAic2xhY2tfY29udmVyc2F0aW9uc19kYi9zbGFja19kYl9jaGFubmVsIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJpZCI6IDMwMCwgImlucHV0X3R5cGUiOiAidGV4dCIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6ICJzbGFja19kYl9jaGFubmVsIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAib3JkZXIiOiAyLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6IG51bGwsICJyZWFkX29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFtdLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogIlNsYWNrIGNoYW5uZWwgbmFtZSIsICJ0b29sdGlwIjogIiIsICJ0eXBlX2lkIjogMTAwMCwgInV1aWQiOiAiZGYwMTY1ZDQtNjM2Ny00OTE0LWI4MGMtYzg4NzdiMjBjMDExIiwgInZhbHVlcyI6IFtdLCAid2lkdGgiOiAxNjV9LCAic2xhY2tfZGJfY2hhbm5lbF90eXBlIjogeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAic2xhY2tfY29udmVyc2F0aW9uc19kYi9zbGFja19kYl9jaGFubmVsX3R5cGUiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzAxLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInNsYWNrX2RiX2NoYW5uZWxfdHlwZSIsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgIm9wZXJhdGlvbnMiOiBbXSwgIm9yZGVyIjogMywgInBsYWNlaG9sZGVyIjogIiIsICJwcmVmaXgiOiBudWxsLCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbXSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJTbGFjayBjaGFubmVsIHR5cGUiLCAidG9vbHRpcCI6ICIiLCAidHlwZV9pZCI6IDEwMDAsICJ1dWlkIjogImNlNGM4Mzk5LTA5ZTMtNDgxYS05NzZmLWIwNzZjOTg5NjVmNyIsICJ2YWx1ZXMiOiBbXSwgIndpZHRoIjogNjd9LCAic2xhY2tfZGJfcGVybWFsaW5rIjogeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAic2xhY2tfY29udmVyc2F0aW9uc19kYi9zbGFja19kYl9wZXJtYWxpbmsiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzAyLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0YXJlYSIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6ICJzbGFja19kYl9wZXJtYWxpbmsiLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJvcGVyYXRpb25zIjogW10sICJvcmRlciI6IDQsICJwbGFjZWhvbGRlciI6ICIiLCAicHJlZml4IjogbnVsbCwgInJlYWRfb25seSI6IGZhbHNlLCAicmljaF90ZXh0IjogdHJ1ZSwgInRhZ3MiOiBbXSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJTbGFjayBVUkwiLCAidG9vbHRpcCI6ICIiLCAidHlwZV9pZCI6IDEwMDAsICJ1dWlkIjogIjJmOTUzNjZiLWRkMzItNDAzNS04ODExLTU0OTY0NmMwYWY1YyIsICJ2YWx1ZXMiOiBbXSwgIndpZHRoIjogNzl9LCAic2xhY2tfZGJfcmVzX2lkIjogeyJhbGxvd19kZWZhdWx0X3ZhbHVlIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImNhbGN1bGF0ZWQiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAic2xhY2tfY29udmVyc2F0aW9uc19kYi9zbGFja19kYl9yZXNfaWQiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzAzLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgImludGVybmFsIjogZmFsc2UsICJpc190cmFja2VkIjogZmFsc2UsICJuYW1lIjogInNsYWNrX2RiX3Jlc19pZCIsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgIm9wZXJhdGlvbnMiOiBbXSwgIm9yZGVyIjogMSwgInBsYWNlaG9sZGVyIjogIiIsICJwcmVmaXgiOiBudWxsLCAicmVhZF9vbmx5IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRhZ3MiOiBbXSwgInRlbXBsYXRlcyI6IFtdLCAidGV4dCI6ICJSZXNpbGllbnQgSUQiLCAidG9vbHRpcCI6ICIiLCAidHlwZV9pZCI6IDEwMDAsICJ1dWlkIjogImNlM2M5YTFlLTI4MDAtNDdkYS1hNWI5LWMzNzgyNTc5MDk0MyIsICJ2YWx1ZXMiOiBbXSwgIndpZHRoIjogMjExfSwgInNsYWNrX2RiX3RpbWUiOiB7ImFsbG93X2RlZmF1bHRfdmFsdWUiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiY2FsY3VsYXRlZCI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJzbGFja19jb252ZXJzYXRpb25zX2RiL3NsYWNrX2RiX3RpbWUiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImlkIjogMzA0LCAiaW5wdXRfdHlwZSI6ICJkYXRldGltZXBpY2tlciIsICJpbnRlcm5hbCI6IGZhbHNlLCAiaXNfdHJhY2tlZCI6IGZhbHNlLCAibmFtZSI6ICJzbGFja19kYl90aW1lIiwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAib3BlcmF0aW9ucyI6IFtdLCAib3JkZXIiOiAwLCAicGxhY2Vob2xkZXIiOiAiIiwgInByZWZpeCI6IG51bGwsICJyZWFkX29ubHkiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGFncyI6IFtdLCAidGVtcGxhdGVzIjogW10sICJ0ZXh0IjogIlRpbWUiLCAidG9vbHRpcCI6ICIiLCAidHlwZV9pZCI6IDEwMDAsICJ1dWlkIjogIjY1NmE3ZGFmLWI2NGEtNDU1OS05ODdkLWI3ODlkMGVjNGM0YiIsICJ2YWx1ZXMiOiBbXSwgIndpZHRoIjogMTIzfX0sICJmb3JfYWN0aW9ucyI6IGZhbHNlLCAiZm9yX2N1c3RvbV9maWVsZHMiOiBmYWxzZSwgImZvcl9ub3RpZmljYXRpb25zIjogZmFsc2UsICJmb3Jfd29ya2Zsb3dzIjogZmFsc2UsICJpZCI6IG51bGwsICJwYXJlbnRfdHlwZXMiOiBbImluY2lkZW50Il0sICJwcm9wZXJ0aWVzIjogeyJjYW5fY3JlYXRlIjogZmFsc2UsICJjYW5fZGVzdHJveSI6IGZhbHNlLCAiZm9yX3dobyI6IFtdfSwgInNjcmlwdHMiOiBbXSwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidHlwZV9pZCI6IDgsICJ0eXBlX25hbWUiOiAic2xhY2tfY29udmVyc2F0aW9uc19kYiIsICJ1dWlkIjogImUyMDM2YmYzLTYxZWEtNDc1Mi04ZDZmLTJiNGVhMjYyYmIxYiJ9XSwgIndvcmtmbG93cyI6IFt7ImFjdGlvbnMiOiBbXSwgImNvbnRlbnQiOiB7InZlcnNpb24iOiA1LCAid29ya2Zsb3dfaWQiOiAiZXhhbXBsZV9wb3N0X2F0dGFjaG1lbnRfdG9fc2xhY2tfX2FydGlmYWN0IiwgInhtbCI6ICI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48ZGVmaW5pdGlvbnMgeG1sbnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L01PREVMXCIgeG1sbnM6YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9ESVwiIHhtbG5zOm9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRENcIiB4bWxuczpvbWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RJXCIgeG1sbnM6cmVzaWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5cIiB4bWxuczp4c2Q9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNwYWNlPVwiaHR0cDovL3d3dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJleGFtcGxlX3Bvc3RfYXR0YWNobWVudF90b19zbGFja19fYXJ0aWZhY3RcIiBpc0V4ZWN1dGFibGU9XCJ0cnVlXCIgbmFtZT1cIkV4YW1wbGU6IFBvc3QgQXJ0aWZhY3QgQXR0YWNobWVudCB0byBTbGFja1wiPjxkb2N1bWVudGF0aW9uPlVwbG9hZCBBcnRpZmFjdCBBdHRhY2htZW50IHRvIHlvdXIgU2xhY2sgY2hhbm5lbCB3aXRoIGFuIG9wdGlvbmFsIGN1c3RvbSB0ZXh0IG1lc3NhZ2UuPC9kb2N1bWVudGF0aW9uPjxzdGFydEV2ZW50IGlkPVwiU3RhcnRFdmVudF8xNTVhc3htXCI+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18wMmpzaHFmPC9vdXRnb2luZz48L3N0YXJ0RXZlbnQ+PHNlcnZpY2VUYXNrIGlkPVwiU2VydmljZVRhc2tfMGRneGFxa1wiIG5hbWU9XCJQb3N0IGF0dGFjaG1lbnQgdG8gU2xhY2tcIiByZXNpbGllbnQ6dHlwZT1cImZ1bmN0aW9uXCI+PGV4dGVuc2lvbkVsZW1lbnRzPjxyZXNpbGllbnQ6ZnVuY3Rpb24gdXVpZD1cIjVmZWQ0ZGQ1LTljY2MtNDkyYS05MGUxLTRmMTdlNmE1YzVjOFwiPntcImlucHV0c1wiOnt9LFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdFwiOlwidXNlcnMgPSBcXFwiXFxcIlxcbmZvciB1c2VyIGluIHJlc3VsdHMudXNlcl9pbmZvOlxcbiAgdXNlcnMgKz0gXFxcInt9IFxcXFxuXFxcIi5mb3JtYXQodXNlcilcXG4jIENyZWF0ZSBhIG5vdGVcXG5ub3RlVGV4dCA9IHVcXFwiXFxcIlxcXCJBcnRpZmFjdCBBdHRhY2htZW50IHdhcyBwb3N0ZWQgdG8gJmx0O2EgaHJlZj0ne30nJmd0O1NsYWNrIGNoYW5uZWwgI3t9Jmx0Oy9hJmd0Oy4gTWVtYmVycyBvZiB0aGlzIGNoYW5uZWwgYXJlOiBcXFxcbnt9XFxcIlxcXCJcXFwiLmZvcm1hdChyZXN1bHRzLnVybCwgcmVzdWx0cy5jaGFubmVsLCB1c2VycylcXG5pbmNpZGVudC5hZGROb3RlKGhlbHBlci5jcmVhdGVSaWNoVGV4dChub3RlVGV4dCkpXCIsXCJwb3N0X3Byb2Nlc3Npbmdfc2NyaXB0X2xhbmd1YWdlXCI6XCJweXRob25cIixcInByZV9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiIyMjIyMjIyMjIyMjIyMjIyMjIyMjXFxuIyBBdHRhY2htZW50IGRhdGEgICAjXFxuIyMjIyMjIyMjIyMjIyMjIyMjIyMjXFxuXFxuIyBSZXF1aXJlZCBpbnB1dHMgYXJlOiB0aGUgaW5jaWRlbnQgaWQgYW5kIGF0dGFjaG1lbnQgaWRcXG5pbnB1dHMuaW5jaWRlbnRfaWQgPSBpbmNpZGVudC5pZFxcbmlucHV0cy5hcnRpZmFjdF9pZCA9IGFydGlmYWN0LmlkXFxuXFxuIyBTbGFjayBjaGFubmVsIG5hbWVcXG4jIE5hbWUgb2YgdGhlIGV4aXN0aW5nIFNsYWNrIFdvcmtzcGFjZSBjaGFubmVsIG9yIGEgbmV3IFNsYWNrIGNoYW5uZWwgeW91IGFyZSBwb3N0aW5nIHRvLiBcXG4jIENoYW5uZWwgbmFtZXMgY2FuIG9ubHkgY29udGFpbiBsb3dlcmNhc2UgbGV0dGVycywgbnVtYmVycywgaHlwaGVucywgYW5kIHVuZGVyc2NvcmVzLCBhbmQgbXVzdCBiZSAyMSBjaGFyYWN0ZXJzIG9yIGxlc3MuIFxcbiMgSWYgeW91IGxlYXZlIHRoaXMgZmllbGQgZW1wdHksIGZ1bmN0aW9uIHdpbGwgdHJ5IHRvIHVzZSB0aGUgc2xhY2tfY2hhbm5lbCBhc3NvY2lhdGVkIHdpdGggdGhlIEluY2lkZW50IG9yIFRhc2sgZm91bmQgaW4gdGhlIFNsYWNrIENvbnZlcnNhdGlvbnMgZGF0YXRhYmxlLiBcXG4jIElmIHRoZXJlIGlzblx1MjAxOXQgb25lIGRlZmluZWQsIHRoZSB3b3JrZmxvdyB3aWxsIHRlcm1pbmF0ZS5cXG5pbnB1dHMuc2xhY2tfY2hhbm5lbCA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2NoYW5uZWwgaWYgcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfY2hhbm5lbCBpcyBub3QgTm9uZSBlbHNlIGlucHV0cy5zbGFja19jaGFubmVsXFxuXFxuIyBJcyBjaGFubmVsIHByaXZhdGVcXG4jIEluZGljYXRlIGlmIHRoZSBjaGFubmVsIHlvdSBhcmUgcG9zdGluZyB0byBzaG91bGQgYmUgcHJpdmF0ZS5cXG5pbnB1dHMuc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlID0gcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlIGlmIHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2lzX2NoYW5uZWxfcHJpdmF0ZSBpcyBub3QgTm9uZSBlbHNlIGlucHV0cy5zbGFja19pc19jaGFubmVsX3ByaXZhdGVcXG5cXG4jIFNsYWNrIHVzZXIgZW1haWxzXFxuIyBDb21tYSBzZXBhcmF0ZWQgbGlzdCBvZiBlbWFpbHMgYmVsb25naW5nIHRvIFNsYWNrIHVzZXJzIGluIHlvdXIgd29ya3NwYWNlIHRoYXQgd2lsbCBiZSBhZGRlZCB0byB5b3VyIGNoYW5uZWwuXFxuaW5wdXRzLnNsYWNrX3BhcnRpY2lwYW50X2VtYWlscyA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX3BhcnRpY2lwYW50X2VtYWlscyBpZiBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19wYXJ0aWNpcGFudF9lbWFpbHMgaXMgbm90IE5vbmUgZWxzZSBpbnB1dHMuc2xhY2tfcGFydGljaXBhbnRfZW1haWxzXFxuXFxuIyBTbGFjayBhZGRpdGlvbmFsIHRleHQgbWVzc2FnZVxcbiMgQWRkaXRpb25hbCB0ZXh0IG1lc3NhZ2UgdG8gaW5jbHVkZSB3aXRoIHRoZSBJbmNpZGVudCwgTm90ZSwgQXJ0aWZhY3QsIEF0dGFjaG1lbnQgb3IgVGFzayBkYXRhLlxcbmlucHV0cy5zbGFja190ZXh0ID0gcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfdGV4dCBpZiBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja190ZXh0IGlzIG5vdCBOb25lIGVsc2UgJydcXG5cXG4jIFNsYWNrIENoYW5uZWwgSUQsIGZhc3RlciB0aGFuIGZpbmRpbmcgdmlhIGNoYW5uZWwgbmFtZVxcbmlucHV0cy5zbGFja19jaGFubmVsX2lkID0gcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgaWYgcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgZWxzZSBpbnB1dHMuc2xhY2tfY2hhbm5lbF9pZFxcblwiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0X2xhbmd1YWdlXCI6XCJweXRob25cIixcInJlc3VsdF9uYW1lXCI6XCJcIn08L3Jlc2lsaWVudDpmdW5jdGlvbj48L2V4dGVuc2lvbkVsZW1lbnRzPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMDJqc2hxZjwvaW5jb21pbmc+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18wcDA4YnllPC9vdXRnb2luZz48L3NlcnZpY2VUYXNrPjxlbmRFdmVudCBpZD1cIkVuZEV2ZW50XzB4dWxsMGpcIj48aW5jb21pbmc+U2VxdWVuY2VGbG93XzBwMDhieWU8L2luY29taW5nPjwvZW5kRXZlbnQ+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18wMmpzaHFmXCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tfMGRneGFxa1wiLz48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzBwMDhieWVcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18wZGd4YXFrXCIgdGFyZ2V0UmVmPVwiRW5kRXZlbnRfMHh1bGwwalwiLz48dGV4dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCI+PHRleHQ+U3RhcnQgeW91ciB3b3JrZmxvdyBoZXJlPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMXUwd3NtdVwiPjx0ZXh0PjwhW0NEQVRBW1Bvc3QgdGhlIEFydGlmYWN0IGF0dGFjaG1lbnQgdG8gc2xhY2tfY2hhbm5lbCBhc3NvY2lhdGVkIHdpdGggdGhlIEluY2lkZW50XG5dXT48L3RleHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlvbl8xOTltODlsXCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tfMGRneGFxa1wiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzF1MHdzbXVcIi8+PC9wcm9jZXNzPjxicG1uZGk6QlBNTkRpYWdyYW0gaWQ9XCJCUE1ORGlhZ3JhbV8xXCI+PGJwbW5kaTpCUE1OUGxhbmUgYnBtbkVsZW1lbnQ9XCJ1bmRlZmluZWRcIiBpZD1cIkJQTU5QbGFuZV8xXCI+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bV9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjE2MlwiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIwXCIgd2lkdGg9XCI5MFwiIHg9XCIxNTdcIiB5PVwiMjIzXCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzMFwiIHdpZHRoPVwiMTAwXCIgeD1cIjk5XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzFzZXVqNDhcIiBpZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjE2OVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjIwXCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMTUzXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyNTRcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTZXJ2aWNlVGFza18wZGd4YXFrXCIgaWQ9XCJTZXJ2aWNlVGFza18wZGd4YXFrX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCI4MFwiIHdpZHRoPVwiMTAwXCIgeD1cIjM0MFwiIHk9XCIxNjZcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiRW5kRXZlbnRfMHh1bGwwalwiIGlkPVwiRW5kRXZlbnRfMHh1bGwwal9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjU3MVwiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI1ODlcIiB5PVwiMjI3XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18wMmpzaHFmXCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMDJqc2hxZl9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTk4XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIzNDBcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjI2OVwiIHk9XCIxODRcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJTZXF1ZW5jZUZsb3dfMHAwOGJ5ZVwiIGlkPVwiU2VxdWVuY2VGbG93XzBwMDhieWVfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjQ0MFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiNTcxXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI1MDUuNVwiIHk9XCIxODQuNVwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8xdTB3c211XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8xdTB3c211X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzMFwiIHdpZHRoPVwiMjMzXCIgeD1cIjIyN1wiIHk9XCIzOVwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzE5OW04OWxcIiBpZD1cIkFzc29jaWF0aW9uXzE5OW04OWxfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjM3OFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMTY2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMzQ5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCI2OVwiLz48L2JwbW5kaTpCUE1ORWRnZT48L2JwbW5kaTpCUE1OUGxhbmU+PC9icG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZpbml0aW9ucz4ifSwgImNvbnRlbnRfdmVyc2lvbiI6IDUsICJkZXNjcmlwdGlvbiI6ICJVcGxvYWQgQXJ0aWZhY3QgQXR0YWNobWVudCB0byB5b3VyIFNsYWNrIGNoYW5uZWwgd2l0aCBhbiBvcHRpb25hbCBjdXN0b20gdGV4dCBtZXNzYWdlLiIsICJleHBvcnRfa2V5IjogImV4YW1wbGVfcG9zdF9hdHRhY2htZW50X3RvX3NsYWNrX19hcnRpZmFjdCIsICJsYXN0X21vZGlmaWVkX2J5IjogImFkbWluQGV4YW1wbGUuY29tIiwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE2NTk1NTQwMDU4MTksICJuYW1lIjogIkV4YW1wbGU6IFBvc3QgQXJ0aWZhY3QgQXR0YWNobWVudCB0byBTbGFjayIsICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJleGFtcGxlX3Bvc3RfYXR0YWNobWVudF90b19zbGFja19fYXJ0aWZhY3QiLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ1dWlkIjogIjI3MjU0ZjIyLThlYmItNDc5MC1hNTU3LTBhODNjYjgwMjE5NiIsICJ3b3JrZmxvd19pZCI6IDMzfSwgeyJhY3Rpb25zIjogW10sICJjb250ZW50IjogeyJ2ZXJzaW9uIjogNSwgIndvcmtmbG93X2lkIjogImNyZWF0ZV9zbGFja19yZXBseSIsICJ4bWwiOiAiPD94bWwgdmVyc2lvbj1cIjEuMFwiIGVuY29kaW5nPVwiVVRGLThcIj8+PGRlZmluaXRpb25zIHhtbG5zPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9NT0RFTFwiIHhtbG5zOmJwbW5kaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQvRElcIiB4bWxuczpvbWdkYz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RDXCIgeG1sbnM6b21nZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEwMDUyNC9ESVwiIHhtbG5zOnJlc2lsaWVudD1cImh0dHA6Ly9yZXNpbGllbnQuaWJtLmNvbS9icG1uXCIgeG1sbnM6eHNkPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWFcIiB4bWxuczp4c2k9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZVwiIHRhcmdldE5hbWVzcGFjZT1cImh0dHA6Ly93d3cuY2FtdW5kYS5vcmcvdGVzdFwiPjxwcm9jZXNzIGlkPVwiY3JlYXRlX3NsYWNrX3JlcGx5XCIgaXNFeGVjdXRhYmxlPVwidHJ1ZVwiIG5hbWU9XCJFeGFtcGxlOiBQb3N0IE5vdGUgdG8gU2xhY2tcIj48ZG9jdW1lbnRhdGlvbj5Qb3N0IGEgbWVzc2FnZSBmcm9tIHRoZSBOb3RlIHRvIHlvdXIgU2xhY2sgY2hhbm5lbC4gU2VuZCBzcGVjaWZpY3MgYWJvdXQgdGhlIEluY2lkZW50IG9yIFRhc2sgTm90ZSB3aXRoIGFuIG9wdGlvbmFsIGN1c3RvbSB0ZXh0IG1lc3NhZ2UuPC9kb2N1bWVudGF0aW9uPjxzdGFydEV2ZW50IGlkPVwiU3RhcnRFdmVudF8xNTVhc3htXCI+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18xNGZvODFlPC9vdXRnb2luZz48L3N0YXJ0RXZlbnQ+PHNlcnZpY2VUYXNrIGlkPVwiU2VydmljZVRhc2tfMXJiMjh5cFwiIG5hbWU9XCJQb3N0IG1lc3NhZ2UgdG8gU2xhY2tcIiByZXNpbGllbnQ6dHlwZT1cImZ1bmN0aW9uXCI+PGV4dGVuc2lvbkVsZW1lbnRzPjxyZXNpbGllbnQ6ZnVuY3Rpb24gdXVpZD1cImRlZDI4MjZjLTY1MjgtNGEyNi1iMmM4LTBjZjIxNWRjZTNjM1wiPntcImlucHV0c1wiOnt9LFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdFwiOlwidXNlcnMgPSBcXFwiXFxcIlxcbmZvciB1c2VyIGluIHJlc3VsdHMudXNlcl9pbmZvOlxcbiAgdXNlcnMgKz0gXFxcInt9IFxcXFxuXFxcIi5mb3JtYXQodXNlcilcXG4jIENyZWF0ZSBhIG5vdGVcXG5ub3RlVGV4dCA9IHVcXFwiXFxcIlxcXCJOb3RlIHdhcyBwb3N0ZWQgdG8gJmx0O2EgaHJlZj0ne30nJmd0O1NsYWNrIGNoYW5uZWwgI3t9Jmx0Oy9hJmd0Oy4gTWVtYmVycyBvZiB0aGlzIGNoYW5uZWwgYXJlOiBcXFxcbnt9XFxcIlxcXCJcXFwiLmZvcm1hdChyZXN1bHRzLnVybCwgcmVzdWx0cy5jaGFubmVsLCB1c2VycylcXG5pZiBub3QgdGFzazpcXG4gIGluY2lkZW50LmFkZE5vdGUoaGVscGVyLmNyZWF0ZVJpY2hUZXh0KG5vdGVUZXh0KSlcXG5lbHNlOlxcbiAgdGFzay5hZGROb3RlKGhlbHBlci5jcmVhdGVSaWNoVGV4dChub3RlVGV4dCkpXCIsXCJwb3N0X3Byb2Nlc3Npbmdfc2NyaXB0X2xhbmd1YWdlXCI6XCJweXRob25cIixcInByZV9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiIyMjIyMjIyMjIyMjIyMjIyMjIyMjXFxuIyBOb3RlIGRhdGEgICAgICAgICAjXFxuIyMjIyMjIyMjIyMjIyMjIyMjIyMjXFxuXFxuIyBTbGFjayBhZGRpdGlvbmFsIHRleHQgbWVzc2FnZVxcbiMgQWRkaXRpb25hbCB0ZXh0IG1lc3NhZ2UgdG8gaW5jbHVkZSB3aXRoIHRoZSBJbmNpZGVudCwgTm90ZSwgQXJ0aWZhY3QsIEF0dGFjaG1lbnQgb3IgVGFzayBkYXRhLlxcbnJ1bGVfYWRkaXRpb25hbF90ZXh0ID0gcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfdGV4dCBpZiBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja190ZXh0IGlzIG5vdCBOb25lIGVsc2UgJydcXG5cXG4jIEluY2lkZW50IGlkIGZvciB0aGUgVVJMXFxuaW5jaWRlbnRfaWQgPSBzdHIoaW5jaWRlbnQuaWQpXFxudHlwZV9kYXRhID0gXFxcIkluY2lkZW50IE5vdGVcXFwiXFxuaWYgdGFzazpcXG4gIGluY2lkZW50X2lkICs9IFxcXCI/dGFza19pZD1cXFwiK3N0cih0YXNrLmlkKVxcbiAgdHlwZV9kYXRhID0gXFxcIlRhc2sgTm90ZVxcXCJcXG5cXG4jIFNsYWNrIHRleHQgbWVzc2FnZSBpbiBKU09OIGZvcm1hdFxcbiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXFxuIyBEbyBub3QgcmVtb3ZlIGZpcnN0IDMgZWxlbWVudHMgXFxcIkFkZGl0aW9uYWwgVGV4dFxcXCIsIFxcXCJSZXNpbGllbnQgVVJMXFxcIiBhbmQgXFxcIlR5cGUgb2YgZGF0YVxcXCIsXFxuIyB0aGUgaW5mb3JtYXRpb24gaXMgdXNlZCB0byBnZW5lcmF0ZSB0aGUgdGl0bGUgb2YgdGhlIG1lc3NhZ2UuXFxuI1xcbiMgQWRkL3JlbW92ZSBpbmZvcm1hdGlvbiB1c2luZyB0aGUgc3ludGF4OlxcbiMgXFxcImxhYmVsXFxcIjoge3sgXFxcInR5cGVcXFwiOiBcXFwiW3N0cmluZ3xyaWNodGV4dHxib29sZWFufGRhdGV0aW1lXFxcIiwgXFxcImRhdGFcXFwiOiBcXFwicmVzaWxpZW50IGZpZWxkIGRhdGFcXFwiIH19XFxuI1xcbiMgTWFrZSBzdXJlIHRvIHNlbmQgXFxcImRhdGV0aW1lXFxcIiB0eXBlcyBhcyBpbnRlZ2VycyBhbmQgbm90IHN0cmluZ3M6XFxuIyB3aXRob3V0IGRvdWJsZSBxdW90ZXM6IHsgXFxcInR5cGVcXFwiOiBcXFwiZGF0ZXRpbWVcXFwiLCBcXFwiZGF0YVxcXCI6IHJlc2lsaWVudCBkYXRldGltZSBkYXRhfSBcXG4jXFxuIyBUZXh0IGZpZWxkcyBsaWtlICdub3RlLnRleHQuY29udGVudCcsICd0YXNrLm5hbWUnIG9yICdTbGFjayBhZGRpdGlvbmFsIHRleHQgbWVzc2FnZScgY2FuIGluY2x1ZGUgZG91YmxlIHF1b3Rlcy5cXG4jIFdhdGNoIG91dCBmb3IgZW1iZWRkZWQgZG91YmxlIHF1b3RlcyBpbiB0aGVzZSB0ZXh0IGZpZWxkcyBhbmQgZXNjYXBlIHdpdGggZmllbGQucmVwbGFjZSh1J1xcXCInLCB1J1xcXFxcXFxcXFxcIicpIG90aGVyd2lzZSBqc29uLmxvYWRzIHdpbGwgZmFpbC5cXG5zbGFja190ZXh0ID0gdVxcXCJcXFwiXFxcInt7XFxuICBcXFwiQWRkaXRpb25hbCBUZXh0XFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJzdHJpbmdcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7MH1cXFwiIH19LFxcbiAgXFxcIlJlc2lsaWVudCBVUkxcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcImluY2lkZW50XFxcIiwgXFxcImRhdGFcXFwiOiBcXFwiezF9XFxcIiB9fSxcXG4gIFxcXCJUeXBlIG9mIGRhdGFcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcInN0cmluZ1xcXCIsIFxcXCJkYXRhXFxcIjogXFxcInsyfVxcXCIgfX0sXFxuICBcXFwiSW5jaWRlbnQgSURcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcInN0cmluZ1xcXCIsIFxcXCJkYXRhXFxcIjogXFxcInszfVxcXCIgfX0sXFxuICBcXFwiVGFza1xcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwic3RyaW5nXFxcIiwgXFxcImRhdGFcXFwiOiBcXFwiezR9XFxcIiB9fSxcXG4gIFxcXCJOb3RlXFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJyaWNodGV4dFxcXCIsIFxcXCJkYXRhXFxcIjogXFxcIns1fVxcXCIgfX1cXG59fVxcXCJcXFwiXFxcIi5mb3JtYXQoXFxuICBydWxlX2FkZGl0aW9uYWxfdGV4dC5yZXBsYWNlKHUnXFxcIicsIHUnXFxcXFxcXFxcXFwiJyksXFxuICBpbmNpZGVudF9pZCxcXG4gIHR5cGVfZGF0YSxcXG4gIHN0cihpbmNpZGVudC5pZCksXFxuICB0YXNrLm5hbWUucmVwbGFjZSh1J1xcXCInLCB1J1xcXFxcXFxcXFxcIicpIGlmIHRhc2sgZWxzZSBcXFwiXFxcIiwgXFxuICBub3RlLnRleHQuY29udGVudC5yZXBsYWNlKHUnXFxcIicsIHUnXFxcXFxcXFxcXFwiJykgaWYgbm90ZS50ZXh0IGlzIG5vdCBOb25lIGVsc2UgJycpXFxuXFxuIyBTbGFjayB1c2VybmFtZSAtIG9wdGlvbmFsIHNldHRpbmdcXG4jIFNldCB0byB0cnVlIGFuZCB0aGUgYXV0aGVudGljYXRlZCB1c2VyIG9mIHRoZSBTbGFjayBBcHAgd2lsbCBhcHBlYXIgYXMgdGhlIGF1dGhvciBvZiB0aGUgbWVzc2FnZSwgaWdub3JpbmcgYW55IHZhbHVlcyBwcm92aWRlZCBmb3Igc2xhY2tfdXNlcm5hbWUuIFxcbiMgU2V0IHlvdXIgYm90J3MgbmFtZSB0byBOb3RlJ3MgY3JlYXRvciB0byBhcHBlYXIgYXMgdGhlIGF1dGhvciBvZiB0aGUgbWVzc2FnZS4gTXVzdCBiZSB1c2VkIGluIGNvbmp1bmN0aW9uIHdpdGggc2xhY2tfYXNfdXNlciBzZXQgdG8gZmFsc2UsIG90aGVyd2lzZSBpZ25vcmVkLlxcbiNpbnB1dHMuc2xhY2tfYXNfdXNlciA9IEZhbHNlXFxuI2lucHV0cy5zbGFja191c2VybmFtZSA9IG5vdGUudXNlcl9pZFxcblxcbiMgSUQgb2YgdGhpcyBpbmNpZGVudFxcbmlucHV0cy5pbmNpZGVudF9pZCA9IGluY2lkZW50LmlkXFxuXFxuIyBJRCBvZiB0aGlzIFRhc2tcXG5pZiB0YXNrOlxcbiAgaW5wdXRzLnRhc2tfaWQgPSB0YXNrLmlkXFxuXFxuIyBTbGFjayBjaGFubmVsIG5hbWVcXG4jIE5hbWUgb2YgdGhlIGV4aXN0aW5nIFNsYWNrIFdvcmtzcGFjZSBjaGFubmVsIG9yIGEgbmV3IFNsYWNrIGNoYW5uZWwgeW91IGFyZSBwb3N0aW5nIHRvLiBcXG4jIENoYW5uZWwgbmFtZXMgY2FuIG9ubHkgY29udGFpbiBsb3dlcmNhc2UgbGV0dGVycywgbnVtYmVycywgaHlwaGVucywgYW5kIHVuZGVyc2NvcmVzLCBhbmQgbXVzdCBiZSAyMSBjaGFyYWN0ZXJzIG9yIGxlc3MuIFxcbiMgSWYgeW91IGxlYXZlIHRoaXMgZmllbGQgZW1wdHksIGZ1bmN0aW9uIHdpbGwgdHJ5IHRvIHVzZSB0aGUgc2xhY2tfY2hhbm5lbCBhc3NvY2lhdGVkIHdpdGggdGhlIEluY2lkZW50IG9yIFRhc2sgZm91bmQgaW4gdGhlIFNsYWNrIENvbnZlcnNhdGlvbnMgZGF0YXRhYmxlLiBcXG4jIElmIHRoZXJlIGlzblx1MjAxOXQgb25lIGRlZmluZWQsIHRoZSB3b3JrZmxvdyB3aWxsIHRlcm1pbmF0ZS5cXG5pbnB1dHMuc2xhY2tfY2hhbm5lbCA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2NoYW5uZWwgaWYgcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfY2hhbm5lbCBpcyBub3QgTm9uZSBlbHNlIGlucHV0cy5zbGFja19jaGFubmVsXFxuXFxuIyBJcyBjaGFubmVsIHByaXZhdGVcXG4jIEluZGljYXRlIGlmIHRoZSBjaGFubmVsIHlvdSBhcmUgcG9zdGluZyB0byBzaG91bGQgYmUgcHJpdmF0ZS5cXG5pbnB1dHMuc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlID0gcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlIGlmIHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2lzX2NoYW5uZWxfcHJpdmF0ZSBpcyBub3QgTm9uZSBlbHNlIGlucHV0cy5zbGFja19pc19jaGFubmVsX3ByaXZhdGVcXG5cXG4jIFNsYWNrIHVzZXIgZW1haWxzXFxuIyBDb21tYSBzZXBhcmF0ZWQgbGlzdCBvZiBlbWFpbHMgYmVsb25naW5nIHRvIFNsYWNrIHVzZXJzIGluIHlvdXIgd29ya3NwYWNlIHRoYXQgd2lsbCBiZSBhZGRlZCB0byB5b3VyIGNoYW5uZWwuXFxuaW5wdXRzLnNsYWNrX3BhcnRpY2lwYW50X2VtYWlscyA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX3BhcnRpY2lwYW50X2VtYWlscyBpZiBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19wYXJ0aWNpcGFudF9lbWFpbHMgaXMgbm90IE5vbmUgZWxzZSBpbnB1dHMuc2xhY2tfcGFydGljaXBhbnRfZW1haWxzXFxuXFxuIyBTbGFjayB0ZXh0IG1lc3NhZ2VcXG4jIENvbnRhaW5lciBmaWVsZCB0byByZXRhaW4gSlNPTiBmaWVsZHMgdG8gc2VuZCB0byBTbGFjay5cXG5pbnB1dHMuc2xhY2tfdGV4dCA9IHNsYWNrX3RleHRcXG5cXG4jIFNsYWNrIENoYW5uZWwgSUQsIGZhc3RlciB0aGFuIGZpbmRpbmcgdmlhIGNoYW5uZWwgbmFtZVxcbmlucHV0cy5zbGFja19jaGFubmVsX2lkID0gcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgaWYgcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgZWxzZSBpbnB1dHMuc2xhY2tfY2hhbm5lbF9pZFxcblwiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0X2xhbmd1YWdlXCI6XCJweXRob25cIixcInJlc3VsdF9uYW1lXCI6XCJcIn08L3Jlc2lsaWVudDpmdW5jdGlvbj48L2V4dGVuc2lvbkVsZW1lbnRzPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMTRmbzgxZTwvaW5jb21pbmc+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18xaDQzZmdnPC9vdXRnb2luZz48L3NlcnZpY2VUYXNrPjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMTRmbzgxZVwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlNlcnZpY2VUYXNrXzFyYjI4eXBcIi8+PGVuZEV2ZW50IGlkPVwiRW5kRXZlbnRfMGd2YjBodFwiPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMWg0M2ZnZzwvaW5jb21pbmc+PC9lbmRFdmVudD48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzFoNDNmZ2dcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18xcmIyOHlwXCIgdGFyZ2V0UmVmPVwiRW5kRXZlbnRfMGd2YjBodFwiLz48dGV4dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCI+PHRleHQ+U3RhcnQgeW91ciB3b3JrZmxvdyBoZXJlPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMG0xZXM3a1wiPjx0ZXh0PjwhW0NEQVRBW1NlbGVjdCB0aGUgc2xhY2tfY2hhbm5lbCB0byBwb3N0IGluIGFuZCBhZGp1c3QgdGhlIHBvc3RpbmcgcGFyYW1ldGVycyBhcyBuZWVkZWQuXG5dXT48L3RleHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlvbl8wZHg2dWFnXCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tfMXJiMjh5cFwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzBtMWVzN2tcIi8+PC9wcm9jZXNzPjxicG1uZGk6QlBNTkRpYWdyYW0gaWQ9XCJCUE1ORGlhZ3JhbV8xXCI+PGJwbW5kaTpCUE1OUGxhbmUgYnBtbkVsZW1lbnQ9XCJ1bmRlZmluZWRcIiBpZD1cIkJQTU5QbGFuZV8xXCI+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bV9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjE2MlwiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIwXCIgd2lkdGg9XCI5MFwiIHg9XCIxNTdcIiB5PVwiMjIzXCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzMFwiIHdpZHRoPVwiMTAwXCIgeD1cIjk5XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzFzZXVqNDhcIiBpZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjE2OVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjIwXCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMTUzXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyNTRcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTZXJ2aWNlVGFza18xcmIyOHlwXCIgaWQ9XCJTZXJ2aWNlVGFza18xcmIyOHlwX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCI4MFwiIHdpZHRoPVwiMTAwXCIgeD1cIjI4OVwiIHk9XCIxNjZcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJTZXF1ZW5jZUZsb3dfMTRmbzgxZVwiIGlkPVwiU2VxdWVuY2VGbG93XzE0Zm84MWVfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjE5OFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMjg5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCIyNDMuNVwiIHk9XCIxODRcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiRW5kRXZlbnRfMGd2YjBodFwiIGlkPVwiRW5kRXZlbnRfMGd2YjBodF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjQ5MVwiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI1MDlcIiB5PVwiMjI3XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18xaDQzZmdnXCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMWg0M2ZnZ19kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMzg5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCI0OTFcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjQ0MFwiIHk9XCIxODRcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiVGV4dEFubm90YXRpb25fMG0xZXM3a1wiIGlkPVwiVGV4dEFubm90YXRpb25fMG0xZXM3a19kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiNzVcIiB3aWR0aD1cIjQzOVwiIHg9XCIxMzBcIiB5PVwiNDZcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8wZHg2dWFnXCIgaWQ9XCJBc3NvY2lhdGlvbl8wZHg2dWFnX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIzNDNcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjE2NlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjM0OFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMTIxXCIvPjwvYnBtbmRpOkJQTU5FZGdlPjwvYnBtbmRpOkJQTU5QbGFuZT48L2JwbW5kaTpCUE1ORGlhZ3JhbT48L2RlZmluaXRpb25zPiJ9LCAiY29udGVudF92ZXJzaW9uIjogNSwgImRlc2NyaXB0aW9uIjogIlBvc3QgYSBtZXNzYWdlIGZyb20gdGhlIE5vdGUgdG8geW91ciBTbGFjayBjaGFubmVsLiBTZW5kIHNwZWNpZmljcyBhYm91dCB0aGUgSW5jaWRlbnQgb3IgVGFzayBOb3RlIHdpdGggYW4gb3B0aW9uYWwgY3VzdG9tIHRleHQgbWVzc2FnZS4iLCAiZXhwb3J0X2tleSI6ICJjcmVhdGVfc2xhY2tfcmVwbHkiLCAibGFzdF9tb2RpZmllZF9ieSI6ICJhZG1pbkBleGFtcGxlLmNvbSIsICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNjU5NTU0MjY0Mzg3LCAibmFtZSI6ICJFeGFtcGxlOiBQb3N0IE5vdGUgdG8gU2xhY2siLCAib2JqZWN0X3R5cGUiOiAibm90ZSIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJjcmVhdGVfc2xhY2tfcmVwbHkiLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ1dWlkIjogImQ5ZWRhYTM4LTIwZGYtNGMwZS1hMDE3LTlmZTcyMTM2ODAyNSIsICJ3b3JrZmxvd19pZCI6IDM4fSwgeyJhY3Rpb25zIjogW10sICJjb250ZW50IjogeyJ2ZXJzaW9uIjogNSwgIndvcmtmbG93X2lkIjogImNyZWF0ZV9zbGFja19tZXNzYWdlIiwgInhtbCI6ICI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48ZGVmaW5pdGlvbnMgeG1sbnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L01PREVMXCIgeG1sbnM6YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9ESVwiIHhtbG5zOm9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRENcIiB4bWxuczpvbWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RJXCIgeG1sbnM6cmVzaWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5cIiB4bWxuczp4c2Q9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNwYWNlPVwiaHR0cDovL3d3dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJjcmVhdGVfc2xhY2tfbWVzc2FnZVwiIGlzRXhlY3V0YWJsZT1cInRydWVcIiBuYW1lPVwiRXhhbXBsZTogUG9zdCBJbmNpZGVudCB0byBTbGFja1wiPjxkb2N1bWVudGF0aW9uPlBvc3QgYSBtZXNzYWdlIGZyb20gdGhlIEluY2lkZW50IHRvIHlvdXIgU2xhY2sgY2hhbm5lbC4gU2VuZCBzcGVjaWZpY3MgYWJvdXQgdGhlIEluY2lkZW50IHdpdGggYW4gb3B0aW9uYWwgY3VzdG9tIHRleHQgbWVzc2FnZS48L2RvY3VtZW50YXRpb24+PHN0YXJ0RXZlbnQgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIj48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzFncXMyN3E8L291dGdvaW5nPjwvc3RhcnRFdmVudD48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzFncXMyN3FcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiB0YXJnZXRSZWY9XCJTZXJ2aWNlVGFza18xOThyMjF0XCIvPjxlbmRFdmVudCBpZD1cIkVuZEV2ZW50XzFxb3d0ODdcIj48aW5jb21pbmc+U2VxdWVuY2VGbG93XzF4NmlhZDg8L2luY29taW5nPjwvZW5kRXZlbnQ+PHNlcnZpY2VUYXNrIGlkPVwiU2VydmljZVRhc2tfMTk4cjIxdFwiIG5hbWU9XCJQb3N0IG1lc3NhZ2UgdG8gU2xhY2tcIiByZXNpbGllbnQ6dHlwZT1cImZ1bmN0aW9uXCI+PGV4dGVuc2lvbkVsZW1lbnRzPjxyZXNpbGllbnQ6ZnVuY3Rpb24gdXVpZD1cImRlZDI4MjZjLTY1MjgtNGEyNi1iMmM4LTBjZjIxNWRjZTNjM1wiPntcImlucHV0c1wiOnt9LFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdFwiOlwidXNlcnMgPSBcXFwiXFxcIlxcbmZvciB1c2VyIGluIHJlc3VsdHMudXNlcl9pbmZvOlxcbiAgdXNlcnMgKz0gXFxcInt9IFxcXFxuXFxcIi5mb3JtYXQodXNlcilcXG4jIENyZWF0ZSBhIG5vdGVcXG5ub3RlVGV4dCA9IHVcXFwiXFxcIlxcXCJJbmNpZGVudCB3YXMgcG9zdGVkIHRvICZsdDthIGhyZWY9J3t9JyZndDtTbGFjayBjaGFubmVsICN7fSZsdDsvYSZndDsuIE1lbWJlcnMgb2YgdGhpcyBjaGFubmVsIGFyZTogXFxcXG57fVxcXCJcXFwiXFxcIi5mb3JtYXQocmVzdWx0cy51cmwsIHJlc3VsdHMuY2hhbm5lbCwgdXNlcnMpXFxuaW5jaWRlbnQuYWRkTm90ZShoZWxwZXIuY3JlYXRlUmljaFRleHQobm90ZVRleHQpKVwiLFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdF9sYW5ndWFnZVwiOlwicHl0aG9uXCIsXCJwcmVfcHJvY2Vzc2luZ19zY3JpcHRcIjpcIiMjIyMjIyMjIyMjIyMjIyMjIyMjI1xcbiMgSW5jaWRlbnQgZGF0YSAgICAgI1xcbiMjIyMjIyMjIyMjIyMjIyMjIyMjI1xcblxcbiMgU2xhY2sgYWRkaXRpb25hbCB0ZXh0IG1lc3NhZ2VcXG4jIEFkZGl0aW9uYWwgdGV4dCBtZXNzYWdlIHRvIGluY2x1ZGUgd2l0aCB0aGUgSW5jaWRlbnQsIE5vdGUsIEFydGlmYWN0LCBBdHRhY2htZW50IG9yIFRhc2sgZGF0YS5cXG5ydWxlX2FkZGl0aW9uYWxfdGV4dCA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX3RleHQgaWYgcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfdGV4dCBpcyBub3QgTm9uZSBlbHNlICcnXFxuXFxuIyBcXFwiZGF0ZXRpbWVcXFwiIGZpZWxkczogQXNzaWduIDAgaWYgaXQncyBOb25lXFxuZGF0ZV9vY2N1cmVkID0gaW5jaWRlbnQuc3RhcnRfZGF0ZSBpZiBpbmNpZGVudC5zdGFydF9kYXRlIGVsc2UgMFxcbmRhdGVfZGlzY292ZXJlZCA9IGluY2lkZW50LmRpc2NvdmVyZWRfZGF0ZSBpZiBpbmNpZGVudC5kaXNjb3ZlcmVkX2RhdGUgZWxzZSAwXFxuXFxuIyBJbmNpZGVudCBpZCBmb3IgdGhlIFVSTFxcbmluY2lkZW50X2lkX3N0ciA9IHN0cihpbmNpZGVudC5pZClcXG5cXG4jIFNsYWNrIHRleHQgbWVzc2FnZSBpbiBKU09OIGZvcm1hdFxcbiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXFxuIyBEbyBub3QgcmVtb3ZlIGZpcnN0IDMgZWxlbWVudHMgXFxcIkFkZGl0aW9uYWwgVGV4dFxcXCIsIFxcXCJSZXNpbGllbnQgVVJMXFxcIiBhbmQgXFxcIlR5cGUgb2YgZGF0YVxcXCIsXFxuIyB0aGUgaW5mb3JtYXRpb24gaXMgdXNlZCB0byBnZW5lcmF0ZSB0aGUgdGl0bGUgb2YgdGhlIG1lc3NhZ2UuXFxuI1xcbiMgQWRkL3JlbW92ZSBpbmZvcm1hdGlvbiB1c2luZyB0aGUgc3ludGF4OlxcbiMgXFxcImxhYmVsXFxcIjoge3sgXFxcInR5cGVcXFwiOiBcXFwiW3N0cmluZ3xyaWNodGV4dHxib29sZWFufGRhdGV0aW1lXFxcIiwgXFxcImRhdGFcXFwiOiBcXFwicmVzaWxpZW50IGZpZWxkIGRhdGFcXFwiIH19XFxuI1xcbiMgTWFrZSBzdXJlIHRvIHNlbmQgXFxcImRhdGV0aW1lXFxcIiB0eXBlcyBhcyBpbnRlZ2VycyBhbmQgbm90IHN0cmluZ3M6XFxuIyB3aXRob3V0IGRvdWJsZSBxdW90ZXM6IHsgXFxcInR5cGVcXFwiOiBcXFwiZGF0ZXRpbWVcXFwiLCBcXFwiZGF0YVxcXCI6IHJlc2lsaWVudCBkYXRldGltZSBkYXRhfSAgXFxuI1xcbiMgVGV4dCBmaWVsZHMgbGlrZSAnaW5jaWRlbnQgbmFtZScsICdkZXNjcmlwdGlvbicgb3IgJ1NsYWNrIGFkZGl0aW9uYWwgdGV4dCBtZXNzYWdlJyBjYW4gaW5jbHVkZSBkb3VibGUgcXVvdGVzLlxcbiMgV2F0Y2ggb3V0IGZvciBlbWJlZGRlZCBkb3VibGUgcXVvdGVzIGluIHRoZXNlIHRleHQgZmllbGRzIGFuZCBlc2NhcGUgd2l0aCBmaWVsZC5yZXBsYWNlKHUnXFxcIicsIHUnXFxcXFxcXFxcXFwiJykgb3RoZXJ3aXNlIGpzb24ubG9hZHMgd2lsbCBmYWlsLlxcbnNsYWNrX3RleHQgPSB1XFxcIlxcXCJcXFwie3tcXG4gIFxcXCJBZGRpdGlvbmFsIFRleHRcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcInN0cmluZ1xcXCIsIFxcXCJkYXRhXFxcIjogXFxcInswfVxcXCIgfX0sXFxuICBcXFwiUmVzaWxpZW50IFVSTFxcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwiaW5jaWRlbnRcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7MX1cXFwiIH19LFxcbiAgXFxcIlR5cGUgb2YgZGF0YVxcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwic3RyaW5nXFxcIiwgXFxcImRhdGFcXFwiOiBcXFwiezJ9XFxcIiB9fSxcXG4gIFxcXCJJbmNpZGVudCBJRFxcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwic3RyaW5nXFxcIiwgXFxcImRhdGFcXFwiOiBcXFwiezN9XFxcIiB9fSxcXG4gIFxcXCJJbmNpZGVudCBuYW1lXFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJzdHJpbmdcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7NH1cXFwiIH19LFxcbiAgXFxcIkRlc2NyaXB0aW9uXFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJyaWNodGV4dFxcXCIsIFxcXCJkYXRhXFxcIjogXFxcIns1fVxcXCIgfX0sXFxuICBcXFwiSW5jaWRlbnQgVHlwZXNcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcInN0cmluZ1xcXCIsIFxcXCJkYXRhXFxcIjogXFxcIns2fVxcXCIgfX0sXFxuICBcXFwiTklTVCBBdHRhY2sgVmVjdG9yc1xcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwic3RyaW5nXFxcIiwgXFxcImRhdGFcXFwiOiBcXFwiezd9XFxcIiB9fSxcXG4gIFxcXCJDb25maXJtZWRcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcImJvb2xlYW5cXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7OH1cXFwiIH19LFxcbiAgXFxcIkRhdGUgQ3JlYXRlZFxcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwiZGF0ZXRpbWVcXFwiLCBcXFwiZGF0YVxcXCI6IHs5fSB9fSxcXG4gIFxcXCJEYXRlIE9jY3VycmVkXFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJkYXRldGltZVxcXCIsIFxcXCJkYXRhXFxcIjogezEwfSB9fSxcXG4gIFxcXCJEYXRlIERpc2NvdmVyZWRcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcImRhdGV0aW1lXFxcIiwgXFxcImRhdGFcXFwiOiB7MTF9IH19LFxcbiAgXFxcIlNldmVyaXR5XFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJzdHJpbmdcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7MTJ9XFxcIiB9fVxcbn19XFxcIlxcXCJcXFwiLmZvcm1hdChcXG4gIHJ1bGVfYWRkaXRpb25hbF90ZXh0LnJlcGxhY2UodSdcXFwiJywgdSdcXFxcXFxcXFxcXCInKSxcXG4gIGluY2lkZW50X2lkX3N0cixcXG4gIFxcXCJJbmNpZGVudFxcXCIsXFxuICBpbmNpZGVudF9pZF9zdHIsXFxuICBpbmNpZGVudC5uYW1lLnJlcGxhY2UodSdcXFwiJywgdSdcXFxcXFxcXFxcXCInKSxcXG4gIGluY2lkZW50LmRlc2NyaXB0aW9uLmNvbnRlbnQucmVwbGFjZSh1J1xcXCInLCB1J1xcXFxcXFxcXFxcIicpIGlmIGluY2lkZW50LmRlc2NyaXB0aW9uIGlzIG5vdCBOb25lIGVsc2UgJycsXFxuICBpbmNpZGVudC5pbmNpZGVudF90eXBlX2lkcyxcXG4gIGluY2lkZW50Lm5pc3RfYXR0YWNrX3ZlY3RvcnMsXFxuICBpbmNpZGVudC5jb25maXJtZWQsXFxuICBpbmNpZGVudC5jcmVhdGVfZGF0ZSxcXG4gIGRhdGVfb2NjdXJlZCxcXG4gIGRhdGVfZGlzY292ZXJlZCxcXG4gIGluY2lkZW50LnNldmVyaXR5X2NvZGUpXFxuXFxuIyBJRCBvZiB0aGlzIGluY2lkZW50XFxuaW5wdXRzLmluY2lkZW50X2lkID0gaW5jaWRlbnQuaWRcXG5cXG4jIFNsYWNrIGNoYW5uZWwgbmFtZVxcbiMgTmFtZSBvZiB0aGUgZXhpc3RpbmcgU2xhY2sgV29ya3NwYWNlIGNoYW5uZWwgb3IgYSBuZXcgU2xhY2sgY2hhbm5lbCB5b3UgYXJlIHBvc3RpbmcgdG8uIFxcbiMgQ2hhbm5lbCBuYW1lcyBjYW4gb25seSBjb250YWluIGxvd2VyY2FzZSBsZXR0ZXJzLCBudW1iZXJzLCBoeXBoZW5zLCBhbmQgdW5kZXJzY29yZXMsIGFuZCBtdXN0IGJlIDIxIGNoYXJhY3RlcnMgb3IgbGVzcy4gXFxuIyBJZiB5b3UgbGVhdmUgdGhpcyBmaWVsZCBlbXB0eSwgZnVuY3Rpb24gd2lsbCB0cnkgdG8gdXNlIHRoZSBzbGFja19jaGFubmVsIGFzc29jaWF0ZWQgd2l0aCB0aGUgSW5jaWRlbnQgb3IgVGFzayBmb3VuZCBpbiB0aGUgU2xhY2sgQ29udmVyc2F0aW9ucyBkYXRhdGFibGUuIFxcbiMgSWYgdGhlcmUgaXNuXHUyMDE5dCBvbmUgZGVmaW5lZCwgdGhlIHdvcmtmbG93IHdpbGwgdGVybWluYXRlLlxcbmlucHV0cy5zbGFja19jaGFubmVsID0gcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfY2hhbm5lbCBpZiBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19jaGFubmVsIGlzIG5vdCBOb25lIGVsc2UgaW5wdXRzLnNsYWNrX2NoYW5uZWxcXG5cXG4jIElzIGNoYW5uZWwgcHJpdmF0ZVxcbiMgSW5kaWNhdGUgaWYgdGhlIGNoYW5uZWwgeW91IGFyZSBwb3N0aW5nIHRvIHNob3VsZCBiZSBwcml2YXRlLlxcbmlucHV0cy5zbGFja19pc19jaGFubmVsX3ByaXZhdGUgPSBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19pc19jaGFubmVsX3ByaXZhdGUgaWYgcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlIGlzIG5vdCBOb25lIGVsc2UgaW5wdXRzLnNsYWNrX2lzX2NoYW5uZWxfcHJpdmF0ZVxcblxcbiMgU2xhY2sgdXNlciBlbWFpbHNcXG4jIENvbW1hIHNlcGFyYXRlZCBsaXN0IG9mIGVtYWlscyBiZWxvbmdpbmcgdG8gU2xhY2sgdXNlcnMgaW4geW91ciB3b3Jrc3BhY2UgdGhhdCB3aWxsIGJlIGFkZGVkIHRvIHRoZSBjaGFubmVsIHlvdSBhcmUgcG9zdGluZyB0by5cXG5pbnB1dHMuc2xhY2tfcGFydGljaXBhbnRfZW1haWxzID0gcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfcGFydGljaXBhbnRfZW1haWxzIGlmIHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX3BhcnRpY2lwYW50X2VtYWlscyBpcyBub3QgTm9uZSBlbHNlIGlucHV0cy5zbGFja19wYXJ0aWNpcGFudF9lbWFpbHNcXG5cXG4jIFNsYWNrIHRleHQgbWVzc2FnZVxcbiMgQ29udGFpbmVyIGZpZWxkIHRvIHJldGFpbiBKU09OIGZpZWxkcyB0byBzZW5kIHRvIFNsYWNrLlxcbmlucHV0cy5zbGFja190ZXh0ID0gc2xhY2tfdGV4dFxcblxcbiMgU2xhY2sgQ2hhbm5lbCBJRCwgZmFzdGVyIHRoYW4gZmluZGluZyB2aWEgY2hhbm5lbCBuYW1lXFxuaW5wdXRzLnNsYWNrX2NoYW5uZWxfaWQgPSBydWxlLnByb3BlcnRpZXMuc2xhY2tfY2hhbm5lbF9pZCBpZiBydWxlLnByb3BlcnRpZXMuc2xhY2tfY2hhbm5lbF9pZCBlbHNlIGlucHV0cy5zbGFja19jaGFubmVsX2lkXFxuXCIsXCJwcmVfcHJvY2Vzc2luZ19zY3JpcHRfbGFuZ3VhZ2VcIjpcInB5dGhvblwiLFwicmVzdWx0X25hbWVcIjpcIlwifTwvcmVzaWxpZW50OmZ1bmN0aW9uPjwvZXh0ZW5zaW9uRWxlbWVudHM+PGluY29taW5nPlNlcXVlbmNlRmxvd18xZ3FzMjdxPC9pbmNvbWluZz48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzF4NmlhZDg8L291dGdvaW5nPjwvc2VydmljZVRhc2s+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18xeDZpYWQ4XCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tfMTk4cjIxdFwiIHRhcmdldFJlZj1cIkVuZEV2ZW50XzFxb3d0ODdcIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiPjx0ZXh0PlN0YXJ0IHlvdXIgd29ya2Zsb3cgaGVyZTwvdGV4dD48L3RleHRBbm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBpZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiB0YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRleHRBbm5vdGF0aW9uXzF4ejJpcjVcIj48dGV4dD5TZWxlY3QgdGhlIHNsYWNrX2NoYW5uZWwgdG8gcG9zdCBpbiBhbmQgYWRqdXN0IHRoZSBwb3N0aW5nIHBhcmFtZXRlcnMgYXMgbmVlZGVkLjwvdGV4dD48L3RleHRBbm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBpZD1cIkFzc29jaWF0aW9uXzBpamZpd25cIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18xOThyMjF0XCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90YXRpb25fMXh6MmlyNVwiLz48L3Byb2Nlc3M+PGJwbW5kaTpCUE1ORGlhZ3JhbSBpZD1cIkJQTU5EaWFncmFtXzFcIj48YnBtbmRpOkJQTU5QbGFuZSBicG1uRWxlbWVudD1cInVuZGVmaW5lZFwiIGlkPVwiQlBNTlBsYW5lXzFcIj48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIGlkPVwiU3RhcnRFdmVudF8xNTVhc3htX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiMTYyXCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBcIiB3aWR0aD1cIjkwXCIgeD1cIjE1N1wiIHk9XCIyMjNcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIiBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjMwXCIgd2lkdGg9XCIxMDBcIiB4PVwiOTlcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTY5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMjBcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIxNTNcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzFncXMyN3FcIiBpZD1cIlNlcXVlbmNlRmxvd18xZ3FzMjdxX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIxOThcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjI4M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjkwXCIgeD1cIjE5NS41XCIgeT1cIjE4NC41XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIkVuZEV2ZW50XzFxb3d0ODdcIiBpZD1cIkVuZEV2ZW50XzFxb3d0ODdfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9XCI0NDVcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjkwXCIgeD1cIjQxOFwiIHk9XCIyMjdcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzE5OHIyMXRcIiBpZD1cIlNlcnZpY2VUYXNrXzE5OHIyMXRfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBcIiB4PVwiMjgzXCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18xeDZpYWQ4XCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMXg2aWFkOF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMzgzXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCI0NDVcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjQxNFwiIHk9XCIxODQuNVwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8xeHoyaXI1XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8xeHoyaXI1X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCI1NlwiIHdpZHRoPVwiMjQ1XCIgeD1cIjE2MVwiIHk9XCIzNFwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzBpamZpd25cIiBpZD1cIkFzc29jaWF0aW9uXzBpamZpd25fZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjMyMFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMTY2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMjk0XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCI5MFwiLz48L2JwbW5kaTpCUE1ORWRnZT48L2JwbW5kaTpCUE1OUGxhbmU+PC9icG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZpbml0aW9ucz4ifSwgImNvbnRlbnRfdmVyc2lvbiI6IDUsICJkZXNjcmlwdGlvbiI6ICJQb3N0IGEgbWVzc2FnZSBmcm9tIHRoZSBJbmNpZGVudCB0byB5b3VyIFNsYWNrIGNoYW5uZWwuIFNlbmQgc3BlY2lmaWNzIGFib3V0IHRoZSBJbmNpZGVudCB3aXRoIGFuIG9wdGlvbmFsIGN1c3RvbSB0ZXh0IG1lc3NhZ2UuIiwgImV4cG9ydF9rZXkiOiAiY3JlYXRlX3NsYWNrX21lc3NhZ2UiLCAibGFzdF9tb2RpZmllZF9ieSI6ICJhZG1pbkBleGFtcGxlLmNvbSIsICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNjU5NTU0MTQyOTgwLCAibmFtZSI6ICJFeGFtcGxlOiBQb3N0IEluY2lkZW50IHRvIFNsYWNrIiwgIm9iamVjdF90eXBlIjogImluY2lkZW50IiwgInByb2dyYW1tYXRpY19uYW1lIjogImNyZWF0ZV9zbGFja19tZXNzYWdlIiwgInRhZ3MiOiBbeyJ0YWdfaGFuZGxlIjogImZuX3NsYWNrIiwgInZhbHVlIjogbnVsbH1dLCAidXVpZCI6ICI4ZGY2ZjMzMy00NDIzLTRlOWQtOTU1NC1kY2VhY2QzMTFjYmEiLCAid29ya2Zsb3dfaWQiOiAzMn0sIHsiYWN0aW9ucyI6IFtdLCAiY29udGVudCI6IHsidmVyc2lvbiI6IDQsICJ3b3JrZmxvd19pZCI6ICJzbGFja19leGFtcGxlX2FyY2hpdmVfc2xhY2tfY2hhbm5lbF9fdGFzayIsICJ4bWwiOiAiPD94bWwgdmVyc2lvbj1cIjEuMFwiIGVuY29kaW5nPVwiVVRGLThcIj8+PGRlZmluaXRpb25zIHhtbG5zPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9NT0RFTFwiIHhtbG5zOmJwbW5kaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQvRElcIiB4bWxuczpvbWdkYz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RDXCIgeG1sbnM6b21nZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEwMDUyNC9ESVwiIHhtbG5zOnJlc2lsaWVudD1cImh0dHA6Ly9yZXNpbGllbnQuaWJtLmNvbS9icG1uXCIgeG1sbnM6eHNkPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWFcIiB4bWxuczp4c2k9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZVwiIHRhcmdldE5hbWVzcGFjZT1cImh0dHA6Ly93d3cuY2FtdW5kYS5vcmcvdGVzdFwiPjxwcm9jZXNzIGlkPVwic2xhY2tfZXhhbXBsZV9hcmNoaXZlX3NsYWNrX2NoYW5uZWxfX3Rhc2tcIiBpc0V4ZWN1dGFibGU9XCJ0cnVlXCIgbmFtZT1cIkV4YW1wbGU6IEFyY2hpdmUgVGFzayBTbGFjayBDaGFubmVsXCI+PGRvY3VtZW50YXRpb24+RXhwb3J0cyBjb252ZXJzYXRpb24gaGlzdG9yeSBmcm9tIFRhc2sgYXNzb2NpYXRlZCBTbGFjayBjaGFubmVsIHRvIGEgdGV4dCBmaWxlLCBzYXZlcyB0aGUgdGV4dCBmaWxlIGFzIGFuIEF0dGFjaG1lbnQgYW5kIGFyY2hpdmVzIHRoZSBTbGFjayBjaGFubmVsLjwvZG9jdW1lbnRhdGlvbj48c3RhcnRFdmVudCBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMGtobHlncTwvb3V0Z29pbmc+PC9zdGFydEV2ZW50PjxzZXJ2aWNlVGFzayBpZD1cIlNlcnZpY2VUYXNrXzB1dmRoanNcIiBuYW1lPVwiQXJjaGl2ZSBTbGFjayBDaGFubmVsXCIgcmVzaWxpZW50OnR5cGU9XCJmdW5jdGlvblwiPjxleHRlbnNpb25FbGVtZW50cz48cmVzaWxpZW50OmZ1bmN0aW9uIHV1aWQ9XCI4ZjNhOWQxZC04MTgyLTRjNWItYjQyMi1jZmVlZTMzZGUwZGNcIj57XCJpbnB1dHNcIjp7fSxcInBvc3RfcHJvY2Vzc2luZ19zY3JpcHRcIjpcIm5vdGVUZXh0ID0gdVxcXCJcXFwiXFxcIlNsYWNrIGNoYW5uZWwge30gaGFzIGJlZW4gYXJjaGl2ZWQuIFRoZSBjb252ZXJzYXRpb24gaGlzdG9yeSBoYXMgYmVlbiBzYXZlZCBhcyBhbiBhdHRhY2htZW50LlxcXCJcXFwiXFxcIi5mb3JtYXQocmVzdWx0cy5jaGFubmVsKVxcbnRhc2suYWRkTm90ZShoZWxwZXIuY3JlYXRlUmljaFRleHQobm90ZVRleHQpKVwiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCIjIElEIG9mIHRoaXMgaW5jaWRlbnRcXG5pbnB1dHMuaW5jaWRlbnRfaWQgPSBpbmNpZGVudC5pZFxcblxcbiMgSUQgb2YgdGhpcyBUYXNrXFxuaW5wdXRzLnRhc2tfaWQgPSB0YXNrLmlkXFxuXFxuIyBTbGFjayBDaGFubmVsIElELCBmYXN0ZXIgdGhhbiBmaW5kaW5nIHZpYSBjaGFubmVsIG5hbWVcXG5pbnB1dHMuc2xhY2tfY2hhbm5lbF9pZCA9IHJ1bGUucHJvcGVydGllcy5zbGFja19jaGFubmVsX2lkIGlmIHJ1bGUucHJvcGVydGllcy5zbGFja19jaGFubmVsX2lkIGVsc2UgaW5wdXRzLnNsYWNrX2NoYW5uZWxfaWRcXG5cIixcInByZV9wcm9jZXNzaW5nX3NjcmlwdF9sYW5ndWFnZVwiOlwicHl0aG9uXCJ9PC9yZXNpbGllbnQ6ZnVuY3Rpb24+PC9leHRlbnNpb25FbGVtZW50cz48aW5jb21pbmc+U2VxdWVuY2VGbG93XzBraGx5Z3E8L2luY29taW5nPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMGp3ZXdrazwvb3V0Z29pbmc+PC9zZXJ2aWNlVGFzaz48ZW5kRXZlbnQgaWQ9XCJFbmRFdmVudF8xNDhmcWNzXCI+PGluY29taW5nPlNlcXVlbmNlRmxvd18wandld2trPC9pbmNvbWluZz48L2VuZEV2ZW50PjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMGtobHlncVwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlNlcnZpY2VUYXNrXzB1dmRoanNcIi8+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18wandld2trXCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tfMHV2ZGhqc1wiIHRhcmdldFJlZj1cIkVuZEV2ZW50XzE0OGZxY3NcIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiPjx0ZXh0PlN0YXJ0IHlvdXIgd29ya2Zsb3cgaGVyZTwvdGV4dD48L3RleHRBbm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBpZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiB0YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRleHRBbm5vdGF0aW9uXzBmc2ZkYXdcIj48dGV4dD5BdXRvbWF0aWMgcnVsZSBhcmNoaXZlcyBzbGFja19jaGFubmVsIGFzc29jaWF0ZWQgd2l0aCB0aGUgVGFzazwvdGV4dD48L3RleHRBbm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBpZD1cIkFzc29jaWF0aW9uXzFncXIzd2pcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18wdXZkaGpzXCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90YXRpb25fMGZzZmRhd1wiLz48L3Byb2Nlc3M+PGJwbW5kaTpCUE1ORGlhZ3JhbSBpZD1cIkJQTU5EaWFncmFtXzFcIj48YnBtbmRpOkJQTU5QbGFuZSBicG1uRWxlbWVudD1cInVuZGVmaW5lZFwiIGlkPVwiQlBNTlBsYW5lXzFcIj48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIGlkPVwiU3RhcnRFdmVudF8xNTVhc3htX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiMTYyXCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBcIiB3aWR0aD1cIjkwXCIgeD1cIjE1N1wiIHk9XCIyMjNcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIiBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjMwXCIgd2lkdGg9XCIxMDBcIiB4PVwiOTlcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTY5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMjBcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIxNTNcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzB1dmRoanNcIiBpZD1cIlNlcnZpY2VUYXNrXzB1dmRoanNfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBcIiB4PVwiMzYzXCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJFbmRFdmVudF8xNDhmcWNzXCIgaWQ9XCJFbmRFdmVudF8xNDhmcWNzX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiNjMxXCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjY0OVwiIHk9XCIyMjdcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzBraGx5Z3FcIiBpZD1cIlNlcXVlbmNlRmxvd18wa2hseWdxX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIxOThcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjM2M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiMjgwLjVcIiB5PVwiMTg0XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzBqd2V3a2tcIiBpZD1cIlNlcXVlbmNlRmxvd18wandld2trX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0NjNcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjYzMVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNTQ3XCIgeT1cIjE4NFwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8wZnNmZGF3XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8wZnNmZGF3X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCI0M1wiIHdpZHRoPVwiMjM3XCIgeD1cIjIyNFwiIHk9XCI2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzFncXIzd2pcIiBpZD1cIkFzc29jaWF0aW9uXzFncXIzd2pfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjM4OVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMTY2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMzU1XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIxMDlcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PC9icG1uZGk6QlBNTlBsYW5lPjwvYnBtbmRpOkJQTU5EaWFncmFtPjwvZGVmaW5pdGlvbnM+In0sICJjb250ZW50X3ZlcnNpb24iOiA0LCAiZGVzY3JpcHRpb24iOiAiRXhwb3J0cyBjb252ZXJzYXRpb24gaGlzdG9yeSBmcm9tIFRhc2sgYXNzb2NpYXRlZCBTbGFjayBjaGFubmVsIHRvIGEgdGV4dCBmaWxlLCBzYXZlcyB0aGUgdGV4dCBmaWxlIGFzIGFuIEF0dGFjaG1lbnQgYW5kIGFyY2hpdmVzIHRoZSBTbGFjayBjaGFubmVsLiIsICJleHBvcnRfa2V5IjogInNsYWNrX2V4YW1wbGVfYXJjaGl2ZV9zbGFja19jaGFubmVsX190YXNrIiwgImxhc3RfbW9kaWZpZWRfYnkiOiAiYWRtaW5AZXhhbXBsZS5jb20iLCAibGFzdF9tb2RpZmllZF90aW1lIjogMTY1OTM4MTY1ODQyNCwgIm5hbWUiOiAiRXhhbXBsZTogQXJjaGl2ZSBUYXNrIFNsYWNrIENoYW5uZWwiLCAib2JqZWN0X3R5cGUiOiAidGFzayIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJzbGFja19leGFtcGxlX2FyY2hpdmVfc2xhY2tfY2hhbm5lbF9fdGFzayIsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInV1aWQiOiAiZmNjOTQ4MjgtY2I5MS00NzgxLWI3MDYtZjNhNmFlMDFlODA1IiwgIndvcmtmbG93X2lkIjogMzF9LCB7ImFjdGlvbnMiOiBbXSwgImNvbnRlbnQiOiB7InZlcnNpb24iOiAxNCwgIndvcmtmbG93X2lkIjogInNsYWNrX2V4YW1wbGVfcG9zdF9tZXNzYWdlX3RvX3NsYWNrX19hcnRpZmFjdCIsICJ4bWwiOiAiPD94bWwgdmVyc2lvbj1cIjEuMFwiIGVuY29kaW5nPVwiVVRGLThcIj8+PGRlZmluaXRpb25zIHhtbG5zPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9NT0RFTFwiIHhtbG5zOmJwbW5kaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQvRElcIiB4bWxuczpvbWdkYz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RDXCIgeG1sbnM6b21nZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEwMDUyNC9ESVwiIHhtbG5zOnJlc2lsaWVudD1cImh0dHA6Ly9yZXNpbGllbnQuaWJtLmNvbS9icG1uXCIgeG1sbnM6eHNkPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWFcIiB4bWxuczp4c2k9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZVwiIHRhcmdldE5hbWVzcGFjZT1cImh0dHA6Ly93d3cuY2FtdW5kYS5vcmcvdGVzdFwiPjxwcm9jZXNzIGlkPVwic2xhY2tfZXhhbXBsZV9wb3N0X21lc3NhZ2VfdG9fc2xhY2tfX2FydGlmYWN0XCIgaXNFeGVjdXRhYmxlPVwidHJ1ZVwiIG5hbWU9XCJFeGFtcGxlOiBQb3N0IEFydGlmYWN0IHRvIFNsYWNrXCI+PGRvY3VtZW50YXRpb24+UG9zdCBhIG1lc3NhZ2UgZnJvbSB0aGUgQXJ0aWZhY3QgdG8geW91ciBTbGFjayBjaGFubmVsLiBTZW5kIHNwZWNpZmljcyBhYm91dCB0aGUgQXJ0aWZhY3Qgd2l0aCBhbiBvcHRpb25hbCBjdXN0b20gdGV4dCBtZXNzYWdlLjwvZG9jdW1lbnRhdGlvbj48c3RhcnRFdmVudCBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMDhnMjk0OTwvb3V0Z29pbmc+PC9zdGFydEV2ZW50PjxzZXJ2aWNlVGFzayBpZD1cIlNlcnZpY2VUYXNrXzB4eXlhcXRcIiBuYW1lPVwiUG9zdCBtZXNzYWdlIHRvIFNsYWNrXCIgcmVzaWxpZW50OnR5cGU9XCJmdW5jdGlvblwiPjxleHRlbnNpb25FbGVtZW50cz48cmVzaWxpZW50OmZ1bmN0aW9uIHV1aWQ9XCJkZWQyODI2Yy02NTI4LTRhMjYtYjJjOC0wY2YyMTVkY2UzYzNcIj57XCJpbnB1dHNcIjp7fSxcInBvc3RfcHJvY2Vzc2luZ19zY3JpcHRcIjpcInVzZXJzID0gXFxcIlxcXCJcXG5mb3IgdXNlciBpbiByZXN1bHRzLnVzZXJfaW5mbzpcXG4gIHVzZXJzICs9IFxcXCJ7fSBcXFxcblxcXCIuZm9ybWF0KHVzZXIpXFxuIyBDcmVhdGUgYSBub3RlXFxubm90ZVRleHQgPSB1XFxcIlxcXCJcXFwiQXJ0aWZhY3Qgd2FzIHBvc3RlZCB0byAmbHQ7YSBocmVmPSd7fScmZ3Q7U2xhY2sgY2hhbm5lbCAje30mbHQ7L2EmZ3Q7LiBNZW1iZXJzIG9mIHRoaXMgY2hhbm5lbCBhcmU6IFxcXFxue31cXFwiXFxcIlxcXCIuZm9ybWF0KHJlc3VsdHMudXJsLCByZXN1bHRzLmNoYW5uZWwsIHVzZXJzKVxcbmluY2lkZW50LmFkZE5vdGUoaGVscGVyLmNyZWF0ZVJpY2hUZXh0KG5vdGVUZXh0KSlcIixcInBvc3RfcHJvY2Vzc2luZ19zY3JpcHRfbGFuZ3VhZ2VcIjpcInB5dGhvblwiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCIjIyMjIyMjIyMjIyMjIyMjIyMjIyNcXG4jIEFydGlmYWN0IGRhdGEgICAgICNcXG4jIyMjIyMjIyMjIyMjIyMjIyMjIyNcXG5cXG4jIFNsYWNrIGFkZGl0aW9uYWwgdGV4dCBtZXNzYWdlXFxuIyBBZGRpdGlvbmFsIHRleHQgbWVzc2FnZSB0byBpbmNsdWRlIHdpdGggdGhlIEluY2lkZW50LCBOb3RlLCBBcnRpZmFjdCwgQXR0YWNobWVudCBvciBUYXNrIGRhdGEuXFxucnVsZV9hZGRpdGlvbmFsX3RleHQgPSBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja190ZXh0IGlmIHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX3RleHQgaXMgbm90IE5vbmUgZWxzZSAnJ1xcblxcbiMgSW5jaWRlbnQgaWQgZm9yIHRoZSBVUkxcXG5pbmNpZGVudF9pZF9zdHIgPSBzdHIoaW5jaWRlbnQuaWQpXFxuXFxuIyBTbGFjayB0ZXh0IG1lc3NhZ2UgaW4gSlNPTiBmb3JtYXRcXG4jIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxcbiMgRG8gbm90IHJlbW92ZSBmaXJzdCAzIGVsZW1lbnRzIFxcXCJBZGRpdGlvbmFsIFRleHRcXFwiLCBcXFwiUmVzaWxpZW50IFVSTFxcXCIgYW5kIFxcXCJUeXBlIG9mIGRhdGFcXFwiLFxcbiMgdGhlIGluZm9ybWF0aW9uIGlzIHVzZWQgdG8gZ2VuZXJhdGUgdGhlIHRpdGxlIG9mIHRoZSBtZXNzYWdlLlxcbiNcXG4jIEFkZC9yZW1vdmUgaW5mb3JtYXRpb24gdXNpbmcgdGhlIHN5bnRheDpcXG4jIFxcXCJsYWJlbFxcXCI6IHt7IFxcXCJ0eXBlXFxcIjogXFxcIltzdHJpbmd8cmljaHRleHR8Ym9vbGVhbnxkYXRldGltZVxcXCIsIFxcXCJkYXRhXFxcIjogXFxcInJlc2lsaWVudCBmaWVsZCBkYXRhXFxcIiB9fVxcbiNcXG4jIE1ha2Ugc3VyZSB0byBzZW5kIFxcXCJkYXRldGltZVxcXCIgdHlwZXMgYXMgaW50ZWdlcnMgYW5kIG5vdCBzdHJpbmdzOlxcbiMgd2l0aG91dCBkb3VibGUgcXVvdGVzOiB7IFxcXCJ0eXBlXFxcIjogXFxcImRhdGV0aW1lXFxcIiwgXFxcImRhdGFcXFwiOiByZXNpbGllbnQgZGF0ZXRpbWUgZGF0YX0gIFxcbiNcXG4jIFRleHQgZmllbGRzIGxpa2UgJ2FydGlmYWN0LnZhbHVlJywgb3IgJ1NsYWNrIGFkZGl0aW9uYWwgdGV4dCBtZXNzYWdlJyBjYW4gaW5jbHVkZSBkb3VibGUgcXVvdGVzLlxcbiMgV2F0Y2ggb3V0IGZvciBlbWJlZGRlZCBkb3VibGUgcXVvdGVzIGluIHRoZXNlIHRleHQgZmllbGRzIGFuZCBlc2NhcGUgd2l0aCBmaWVsZC5yZXBsYWNlKHUnXFxcIicsIHUnXFxcXFxcXFxcXFwiJykgb3RoZXJ3aXNlIGpzb24ubG9hZHMgd2lsbCBmYWlsLlxcbnNsYWNrX3RleHQgPSB1XFxcIlxcXCJcXFwie3tcXG4gIFxcXCJBZGRpdGlvbmFsIFRleHRcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcInN0cmluZ1xcXCIsIFxcXCJkYXRhXFxcIjogXFxcInswfVxcXCIgfX0sXFxuICBcXFwiUmVzaWxpZW50IFVSTFxcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwiaW5jaWRlbnRcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7MX1cXFwiIH19LFxcbiAgXFxcIlR5cGUgb2YgZGF0YVxcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwic3RyaW5nXFxcIiwgXFxcImRhdGFcXFwiOiBcXFwiezJ9XFxcIiB9fSxcXG4gIFxcXCJJbmNpZGVudCBJRFxcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwic3RyaW5nXFxcIiwgXFxcImRhdGFcXFwiOiBcXFwiezN9XFxcIiB9fSxcXG4gIFxcXCJBcnRpZmFjdCBUeXBlXFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJzdHJpbmdcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7NH1cXFwiIH19LFxcbiAgXFxcIkFydGlmYWN0IFZhbHVlXFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJzdHJpbmdcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7NX1cXFwiIH19LFxcbiAgXFxcIkFydGlmYWN0IENyZWF0ZWQgQnlcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcInN0cmluZ1xcXCIsIFxcXCJkYXRhXFxcIjogXFxcIns2fVxcXCIgfX0sXFxuICBcXFwiQXJ0aWZhY3QgQ3JlYXRlZCBvblxcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwiZGF0ZXRpbWVcXFwiLCBcXFwiZGF0YVxcXCI6IHs3fSB9fVxcbn19XFxcIlxcXCJcXFwiLmZvcm1hdChcXG4gIHJ1bGVfYWRkaXRpb25hbF90ZXh0LnJlcGxhY2UodSdcXFwiJywgdSdcXFxcXFxcXFxcXCInKSxcXG4gIGluY2lkZW50X2lkX3N0cixcXG4gIFxcXCJBcnRpZmFjdFxcXCIsXFxuICBpbmNpZGVudF9pZF9zdHIsXFxuICBhcnRpZmFjdC50eXBlLFxcbiAgYXJ0aWZhY3QudmFsdWUucmVwbGFjZSh1J1xcXCInLCB1J1xcXFxcXFxcXFxcIicpLFxcbiAgYXJ0aWZhY3QuY3JlYXRvci5kaXNwbGF5X25hbWUsXFxuICBhcnRpZmFjdC5jcmVhdGVkKVxcblxcbiMgSUQgb2YgdGhpcyBpbmNpZGVudFxcbmlucHV0cy5pbmNpZGVudF9pZCA9IGluY2lkZW50LmlkXFxuXFxuIyBTbGFjayBjaGFubmVsIG5hbWVcXG4jIE5hbWUgb2YgdGhlIGV4aXN0aW5nIFNsYWNrIFdvcmtzcGFjZSBjaGFubmVsIG9yIGEgbmV3IFNsYWNrIGNoYW5uZWwgeW91IGFyZSBwb3N0aW5nIHRvLiBcXG4jIENoYW5uZWwgbmFtZXMgY2FuIG9ubHkgY29udGFpbiBsb3dlcmNhc2UgbGV0dGVycywgbnVtYmVycywgaHlwaGVucywgYW5kIHVuZGVyc2NvcmVzLCBhbmQgbXVzdCBiZSAyMSBjaGFyYWN0ZXJzIG9yIGxlc3MuIFxcbiMgSWYgeW91IGxlYXZlIHRoaXMgZmllbGQgZW1wdHksIGZ1bmN0aW9uIHdpbGwgdHJ5IHRvIHVzZSB0aGUgc2xhY2tfY2hhbm5lbCBhc3NvY2lhdGVkIHdpdGggdGhlIEluY2lkZW50IG9yIFRhc2sgZm91bmQgaW4gdGhlIFNsYWNrIENvbnZlcnNhdGlvbnMgZGF0YXRhYmxlLiBcXG4jIElmIHRoZXJlIGlzblx1MjAxOXQgb25lIGRlZmluZWQsIHRoZSB3b3JrZmxvdyB3aWxsIHRlcm1pbmF0ZS5cXG5pbnB1dHMuc2xhY2tfY2hhbm5lbCA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2NoYW5uZWwgaWYgcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfY2hhbm5lbCBpcyBub3QgTm9uZSBlbHNlIGlucHV0cy5zbGFja19jaGFubmVsXFxuXFxuIyBJcyBjaGFubmVsIHByaXZhdGVcXG4jIEluZGljYXRlIGlmIHRoZSBjaGFubmVsIHlvdSBhcmUgcG9zdGluZyB0byBzaG91bGQgYmUgcHJpdmF0ZS5cXG5pbnB1dHMuc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlID0gcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlIGlmIHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2lzX2NoYW5uZWxfcHJpdmF0ZSBpcyBub3QgTm9uZSBlbHNlIGlucHV0cy5zbGFja19pc19jaGFubmVsX3ByaXZhdGVcXG5cXG4jIFNsYWNrIHVzZXIgZW1haWxzXFxuIyBDb21tYSBzZXBhcmF0ZWQgbGlzdCBvZiBlbWFpbHMgYmVsb25naW5nIHRvIFNsYWNrIHVzZXJzIGluIHlvdXIgd29ya3NwYWNlIHRoYXQgd2lsbCBiZSBhZGRlZCB0byB5b3VyIGNoYW5uZWwuXFxuaW5wdXRzLnNsYWNrX3BhcnRpY2lwYW50X2VtYWlscyA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX3BhcnRpY2lwYW50X2VtYWlscyBpZiBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19wYXJ0aWNpcGFudF9lbWFpbHMgaXMgbm90IE5vbmUgZWxzZSBpbnB1dHMuc2xhY2tfcGFydGljaXBhbnRfZW1haWxzXFxuXFxuIyBTbGFjayB0ZXh0IG1lc3NhZ2VcXG4jIENvbnRhaW5lciBmaWVsZCB0byByZXRhaW4gSlNPTiBmaWVsZHMgdG8gc2VuZCB0byBTbGFjay5cXG5pbnB1dHMuc2xhY2tfdGV4dCA9IHNsYWNrX3RleHRcXG5cXG4jIFNsYWNrIENoYW5uZWwgSUQsIGZhc3RlciB0aGFuIGZpbmRpbmcgdmlhIGNoYW5uZWwgbmFtZVxcbmlucHV0cy5zbGFja19jaGFubmVsX2lkID0gcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgaWYgcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgZWxzZSBpbnB1dHMuc2xhY2tfY2hhbm5lbF9pZFxcblwiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0X2xhbmd1YWdlXCI6XCJweXRob25cIn08L3Jlc2lsaWVudDpmdW5jdGlvbj48L2V4dGVuc2lvbkVsZW1lbnRzPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMDhnMjk0OTwvaW5jb21pbmc+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18wd2hxc2t5PC9vdXRnb2luZz48L3NlcnZpY2VUYXNrPjxlbmRFdmVudCBpZD1cIkVuZEV2ZW50XzA3ODNnMG1cIj48aW5jb21pbmc+U2VxdWVuY2VGbG93XzB3aHFza3k8L2luY29taW5nPjwvZW5kRXZlbnQ+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18wOGcyOTQ5XCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tfMHh5eWFxdFwiLz48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzB3aHFza3lcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18weHl5YXF0XCIgdGFyZ2V0UmVmPVwiRW5kRXZlbnRfMDc4M2cwbVwiLz48dGV4dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCI+PHRleHQ+U3RhcnQgeW91ciB3b3JrZmxvdyBoZXJlPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMXhvaXZsZFwiPjx0ZXh0PlNlbGVjdCB0aGUgc2xhY2tfY2hhbm5lbCB0byBwb3N0IGluIGFuZCBhZGp1c3QgdGhlIHBvc3RpbmcgcGFyYW1ldGVycyBhcyBuZWVkZWQuPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMW56ZHhhelwiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNrXzB4eXlhcXRcIiB0YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8xeG9pdmxkXCIvPjwvcHJvY2Vzcz48YnBtbmRpOkJQTU5EaWFncmFtIGlkPVwiQlBNTkRpYWdyYW1fMVwiPjxicG1uZGk6QlBNTlBsYW5lIGJwbW5FbGVtZW50PVwidW5kZWZpbmVkXCIgaWQ9XCJCUE1OUGxhbmVfMVwiPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU3RhcnRFdmVudF8xNTVhc3htXCIgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1fZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9XCIxNjJcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMFwiIHdpZHRoPVwiOTBcIiB4PVwiMTU3XCIgeT1cIjIyM1wiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzBcIiB3aWR0aD1cIjEwMFwiIHg9XCI5OVwiIHk9XCIyNTRcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIgaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIxNjlcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIyMFwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjE1M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU2VydmljZVRhc2tfMHh5eWFxdFwiIGlkPVwiU2VydmljZVRhc2tfMHh5eWFxdF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiODBcIiB3aWR0aD1cIjEwMFwiIHg9XCIzNTVcIiB5PVwiMTY2XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIkVuZEV2ZW50XzA3ODNnMG1cIiBpZD1cIkVuZEV2ZW50XzA3ODNnMG1fZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9XCI2MTdcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNjM1XCIgeT1cIjIyN1wiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJTZXF1ZW5jZUZsb3dfMDhnMjk0OVwiIGlkPVwiU2VxdWVuY2VGbG93XzA4ZzI5NDlfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjE5OFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMzU1XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCIyNzYuNVwiIHk9XCIxODRcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJTZXF1ZW5jZUZsb3dfMHdocXNreVwiIGlkPVwiU2VxdWVuY2VGbG93XzB3aHFza3lfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjQ1NVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiNjE3XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI1MzZcIiB5PVwiMTg0LjVcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiVGV4dEFubm90YXRpb25fMXhvaXZsZFwiIGlkPVwiVGV4dEFubm90YXRpb25fMXhvaXZsZF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzNcIiB3aWR0aD1cIjMzMFwiIHg9XCIyMzhcIiB5PVwiMzlcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8xbnpkeGF6XCIgaWQ9XCJBc3NvY2lhdGlvbl8xbnpkeGF6X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0MDRcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjE2NlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjQwM1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiNzJcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PC9icG1uZGk6QlBNTlBsYW5lPjwvYnBtbmRpOkJQTU5EaWFncmFtPjwvZGVmaW5pdGlvbnM+In0sICJjb250ZW50X3ZlcnNpb24iOiAxNCwgImRlc2NyaXB0aW9uIjogIlBvc3QgYSBtZXNzYWdlIGZyb20gdGhlIEFydGlmYWN0IHRvIHlvdXIgU2xhY2sgY2hhbm5lbC4gU2VuZCBzcGVjaWZpY3MgYWJvdXQgdGhlIEFydGlmYWN0IHdpdGggYW4gb3B0aW9uYWwgY3VzdG9tIHRleHQgbWVzc2FnZS4iLCAiZXhwb3J0X2tleSI6ICJzbGFja19leGFtcGxlX3Bvc3RfbWVzc2FnZV90b19zbGFja19fYXJ0aWZhY3QiLCAibGFzdF9tb2RpZmllZF9ieSI6ICJhZG1pbkBleGFtcGxlLmNvbSIsICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNjU5NTU0MzMzNzM0LCAibmFtZSI6ICJFeGFtcGxlOiBQb3N0IEFydGlmYWN0IHRvIFNsYWNrIiwgIm9iamVjdF90eXBlIjogImFydGlmYWN0IiwgInByb2dyYW1tYXRpY19uYW1lIjogInNsYWNrX2V4YW1wbGVfcG9zdF9tZXNzYWdlX3RvX3NsYWNrX19hcnRpZmFjdCIsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInV1aWQiOiAiYjM4NDZlMDItZTFmOS00MjBlLTg2YWMtNWJmMGI4Zjk1YTlmIiwgIndvcmtmbG93X2lkIjogMzd9LCB7ImFjdGlvbnMiOiBbXSwgImNvbnRlbnQiOiB7InZlcnNpb24iOiA0LCAid29ya2Zsb3dfaWQiOiAiYXJjaGl2ZV9zbGFja19jaGFubmVsIiwgInhtbCI6ICI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48ZGVmaW5pdGlvbnMgeG1sbnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L01PREVMXCIgeG1sbnM6YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9ESVwiIHhtbG5zOm9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRENcIiB4bWxuczpvbWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RJXCIgeG1sbnM6cmVzaWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5cIiB4bWxuczp4c2Q9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNwYWNlPVwiaHR0cDovL3d3dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJhcmNoaXZlX3NsYWNrX2NoYW5uZWxcIiBpc0V4ZWN1dGFibGU9XCJ0cnVlXCIgbmFtZT1cIkV4YW1wbGU6IEFyY2hpdmUgSW5jaWRlbnQgU2xhY2sgQ2hhbm5lbFwiPjxkb2N1bWVudGF0aW9uPkV4cG9ydHMgY29udmVyc2F0aW9uIGhpc3RvcnkgZnJvbSBJbmNpZGVudCBhc3NvY2lhdGVkIFNsYWNrIGNoYW5uZWwgdG8gYSB0ZXh0IGZpbGUsIHNhdmVzIHRoZSB0ZXh0IGZpbGUgYXMgYW4gQXR0YWNobWVudCBhbmQgYXJjaGl2ZXMgdGhlIFNsYWNrIGNoYW5uZWwuPC9kb2N1bWVudGF0aW9uPjxzdGFydEV2ZW50IGlkPVwiU3RhcnRFdmVudF8xNTVhc3htXCI+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18xM3JkZ3p0PC9vdXRnb2luZz48L3N0YXJ0RXZlbnQ+PHNlcnZpY2VUYXNrIGlkPVwiU2VydmljZVRhc2tfMXgyNGM0MFwiIG5hbWU9XCJBcmNoaXZlIFNsYWNrIENoYW5uZWxcIiByZXNpbGllbnQ6dHlwZT1cImZ1bmN0aW9uXCI+PGV4dGVuc2lvbkVsZW1lbnRzPjxyZXNpbGllbnQ6ZnVuY3Rpb24gdXVpZD1cIjhmM2E5ZDFkLTgxODItNGM1Yi1iNDIyLWNmZWVlMzNkZTBkY1wiPntcImlucHV0c1wiOnt9LFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdFwiOlwibm90ZVRleHQgPSB1XFxcIlxcXCJcXFwiU2xhY2sgY2hhbm5lbCB7fSBoYXMgYmVlbiBhcmNoaXZlZC4gVGhlIGNvbnZlcnNhdGlvbiBoaXN0b3J5IGhhcyBiZWVuIHNhdmVkIGFzIGFuIGF0dGFjaG1lbnQuXFxcIlxcXCJcXFwiLmZvcm1hdChyZXN1bHRzLmNoYW5uZWwpXFxuaW5jaWRlbnQuYWRkTm90ZShoZWxwZXIuY3JlYXRlUmljaFRleHQobm90ZVRleHQpKVwiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCIjIElEIG9mIHRoaXMgaW5jaWRlbnRcXG5pbnB1dHMuaW5jaWRlbnRfaWQgPSBpbmNpZGVudC5pZFxcbmlucHV0cy5zbGFja19jaGFubmVsX2lkID0gcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgaWYgcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgZWxzZSBpbnB1dHMuc2xhY2tfY2hhbm5lbF9pZFxcblwiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0X2xhbmd1YWdlXCI6XCJweXRob25cIixcInJlc3VsdF9uYW1lXCI6XCJcIn08L3Jlc2lsaWVudDpmdW5jdGlvbj48L2V4dGVuc2lvbkVsZW1lbnRzPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMTNyZGd6dDwvaW5jb21pbmc+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18wcXBoMXBsPC9vdXRnb2luZz48L3NlcnZpY2VUYXNrPjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMTNyZGd6dFwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlNlcnZpY2VUYXNrXzF4MjRjNDBcIi8+PGVuZEV2ZW50IGlkPVwiRW5kRXZlbnRfMHdnenE1dFwiPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMHFwaDFwbDwvaW5jb21pbmc+PC9lbmRFdmVudD48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzBxcGgxcGxcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18xeDI0YzQwXCIgdGFyZ2V0UmVmPVwiRW5kRXZlbnRfMHdnenE1dFwiLz48dGV4dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCI+PHRleHQ+U3RhcnQgeW91ciB3b3JrZmxvdyBoZXJlPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMDU4YnZhMVwiPjx0ZXh0PjwhW0NEQVRBW0F1dG9tYXRpYyBydWxlIGFyY2hpdmVzIHNsYWNrX2NoYW5uZWwgYXNzb2NpYXRlZCB3aXRoIHRoZSBJbmNpZGVudFxuXV0+PC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMGl1MGoxNFwiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNrXzF4MjRjNDBcIiB0YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8wNThidmExXCIvPjwvcHJvY2Vzcz48YnBtbmRpOkJQTU5EaWFncmFtIGlkPVwiQlBNTkRpYWdyYW1fMVwiPjxicG1uZGk6QlBNTlBsYW5lIGJwbW5FbGVtZW50PVwidW5kZWZpbmVkXCIgaWQ9XCJCUE1OUGxhbmVfMVwiPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU3RhcnRFdmVudF8xNTVhc3htXCIgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1fZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9XCIxNjJcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMFwiIHdpZHRoPVwiOTBcIiB4PVwiMTU3XCIgeT1cIjIyM1wiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzBcIiB3aWR0aD1cIjEwMFwiIHg9XCI5OVwiIHk9XCIyNTRcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIgaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIxNjlcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIyMFwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjE1M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU2VydmljZVRhc2tfMXgyNGM0MFwiIGlkPVwiU2VydmljZVRhc2tfMXgyNGM0MF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiODBcIiB3aWR0aD1cIjEwMFwiIHg9XCIzNzZcIiB5PVwiMTY2XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzEzcmRnenRcIiBpZD1cIlNlcXVlbmNlRmxvd18xM3JkZ3p0X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIxOThcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjM3NlwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiMjg3XCIgeT1cIjE4NFwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJFbmRFdmVudF8wd2d6cTV0XCIgaWQ9XCJFbmRFdmVudF8wd2d6cTV0X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiNjc2XCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjY5NFwiIHk9XCIyMjdcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzBxcGgxcGxcIiBpZD1cIlNlcXVlbmNlRmxvd18wcXBoMXBsX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0NzZcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjY3NlwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNTc2XCIgeT1cIjE4NC41XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9uXzA1OGJ2YTFcIiBpZD1cIlRleHRBbm5vdGF0aW9uXzA1OGJ2YTFfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjYwXCIgd2lkdGg9XCIyMjhcIiB4PVwiMjE5XCIgeT1cIjM3XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMGl1MGoxNFwiIGlkPVwiQXNzb2NpYXRpb25fMGl1MGoxNF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMzk5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIxNjZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIzNTJcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjk3XCIvPjwvYnBtbmRpOkJQTU5FZGdlPjwvYnBtbmRpOkJQTU5QbGFuZT48L2JwbW5kaTpCUE1ORGlhZ3JhbT48L2RlZmluaXRpb25zPiJ9LCAiY29udGVudF92ZXJzaW9uIjogNCwgImRlc2NyaXB0aW9uIjogIkV4cG9ydHMgY29udmVyc2F0aW9uIGhpc3RvcnkgZnJvbSBJbmNpZGVudCBhc3NvY2lhdGVkIFNsYWNrIGNoYW5uZWwgdG8gYSB0ZXh0IGZpbGUsIHNhdmVzIHRoZSB0ZXh0IGZpbGUgYXMgYW4gQXR0YWNobWVudCBhbmQgYXJjaGl2ZXMgdGhlIFNsYWNrIGNoYW5uZWwuIiwgImV4cG9ydF9rZXkiOiAiYXJjaGl2ZV9zbGFja19jaGFubmVsIiwgImxhc3RfbW9kaWZpZWRfYnkiOiAiYWRtaW5AZXhhbXBsZS5jb20iLCAibGFzdF9tb2RpZmllZF90aW1lIjogMTY1OTM4MTYyMzQzOCwgIm5hbWUiOiAiRXhhbXBsZTogQXJjaGl2ZSBJbmNpZGVudCBTbGFjayBDaGFubmVsIiwgIm9iamVjdF90eXBlIjogImluY2lkZW50IiwgInByb2dyYW1tYXRpY19uYW1lIjogImFyY2hpdmVfc2xhY2tfY2hhbm5lbCIsICJ0YWdzIjogW3sidGFnX2hhbmRsZSI6ICJmbl9zbGFjayIsICJ2YWx1ZSI6IG51bGx9XSwgInV1aWQiOiAiMzkwNDI1YzEtMWNlNi00ZjMxLWE1MjItMzcyYzE5YmEyMzcwIiwgIndvcmtmbG93X2lkIjogMzV9LCB7ImFjdGlvbnMiOiBbXSwgImNvbnRlbnQiOiB7InZlcnNpb24iOiA2LCAid29ya2Zsb3dfaWQiOiAic2xhY2tfZXhhbXBsZV9wb3N0X2F0dGFjaG1lbnRfdG9fc2xhY2siLCAieG1sIjogIjw/eG1sIHZlcnNpb249XCIxLjBcIiBlbmNvZGluZz1cIlVURi04XCI/PjxkZWZpbml0aW9ucyB4bWxucz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQvTU9ERUxcIiB4bWxuczpicG1uZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L0RJXCIgeG1sbnM6b21nZGM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEwMDUyNC9EQ1wiIHhtbG5zOm9tZ2RpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRElcIiB4bWxuczpyZXNpbGllbnQ9XCJodHRwOi8vcmVzaWxpZW50LmlibS5jb20vYnBtblwiIHhtbG5zOnhzZD1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hXCIgeG1sbnM6eHNpPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2VcIiB0YXJnZXROYW1lc3BhY2U9XCJodHRwOi8vd3d3LmNhbXVuZGEub3JnL3Rlc3RcIj48cHJvY2VzcyBpZD1cInNsYWNrX2V4YW1wbGVfcG9zdF9hdHRhY2htZW50X3RvX3NsYWNrXCIgaXNFeGVjdXRhYmxlPVwidHJ1ZVwiIG5hbWU9XCJFeGFtcGxlOiBQb3N0IEluY2lkZW50IC8gVGFzayBBdHRhY2htZW50IHRvIFNsYWNrXCI+PGRvY3VtZW50YXRpb24+VXBsb2FkIEluY2lkZW50IG9yIFRhc2sgQXR0YWNobWVudCB0byB5b3VyIFNsYWNrIGNoYW5uZWwgd2l0aCBhbiBvcHRpb25hbCBjdXN0b20gdGV4dCBtZXNzYWdlLjwvZG9jdW1lbnRhdGlvbj48c3RhcnRFdmVudCBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMXBwMGp0dzwvb3V0Z29pbmc+PC9zdGFydEV2ZW50PjxzZXJ2aWNlVGFzayBpZD1cIlNlcnZpY2VUYXNrXzBua2I1bnVcIiBuYW1lPVwiUG9zdCBhdHRhY2htZW50IHRvIFNsYWNrXCIgcmVzaWxpZW50OnR5cGU9XCJmdW5jdGlvblwiPjxleHRlbnNpb25FbGVtZW50cz48cmVzaWxpZW50OmZ1bmN0aW9uIHV1aWQ9XCI1ZmVkNGRkNS05Y2NjLTQ5MmEtOTBlMS00ZjE3ZTZhNWM1YzhcIj57XCJpbnB1dHNcIjp7fSxcInBvc3RfcHJvY2Vzc2luZ19zY3JpcHRcIjpcInVzZXJzID0gXFxcIlxcXCJcXG5mb3IgdXNlciBpbiByZXN1bHRzLnVzZXJfaW5mbzpcXG4gIHVzZXJzICs9IFxcXCJ7fSBcXFxcblxcXCIuZm9ybWF0KHVzZXIpXFxuIyBDcmVhdGUgYSBub3RlXFxubm90ZVRleHQgPSB1XFxcIlxcXCJcXFwiQXR0YWNobWVudCB3YXMgcG9zdGVkIHRvICZsdDthIGhyZWY9J3t9JyZndDtTbGFjayBjaGFubmVsICN7fSZsdDsvYSZndDsuIE1lbWJlcnMgb2YgdGhpcyBjaGFubmVsIGFyZTogXFxcXG57fVxcXCJcXFwiXFxcIi5mb3JtYXQocmVzdWx0cy51cmwsIHJlc3VsdHMuY2hhbm5lbCwgdXNlcnMpXFxuaWYgbm90IHRhc2s6XFxuICBpbmNpZGVudC5hZGROb3RlKGhlbHBlci5jcmVhdGVSaWNoVGV4dChub3RlVGV4dCkpXFxuZWxzZTpcXG4gIHRhc2suYWRkTm90ZShoZWxwZXIuY3JlYXRlUmljaFRleHQobm90ZVRleHQpKVwiLFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdF9sYW5ndWFnZVwiOlwicHl0aG9uXCIsXCJwcmVfcHJvY2Vzc2luZ19zY3JpcHRcIjpcIiMjIyMjIyMjIyMjIyMjIyMjIyMjI1xcbiMgQXR0YWNobWVudCBkYXRhICAgI1xcbiMjIyMjIyMjIyMjIyMjIyMjIyMjI1xcblxcbiMgUmVxdWlyZWQgaW5wdXRzIGFyZTogdGhlIGluY2lkZW50IGlkIGFuZCBhdHRhY2htZW50IGlkXFxuaW5wdXRzLmluY2lkZW50X2lkID0gaW5jaWRlbnQuaWRcXG5pbnB1dHMuYXR0YWNobWVudF9pZCA9IGF0dGFjaG1lbnQuaWRcXG5cXG4jIElmIHRoaXMgaXMgYSBcXFwidGFzayBhdHRhY2htZW50XFxcIiB0aGVuIHdlIHdpbGwgYWRkaXRpb25hbGx5IGhhdmUgYSB0YXNrLWlkXFxuaWYgdGFzayBpcyBub3QgTm9uZTpcXG4gIGlucHV0cy50YXNrX2lkID0gdGFzay5pZFxcblxcbiMgU2xhY2sgY2hhbm5lbCBuYW1lXFxuIyBOYW1lIG9mIHRoZSBleGlzdGluZyBTbGFjayBXb3Jrc3BhY2UgY2hhbm5lbCBvciBhIG5ldyBTbGFjayBjaGFubmVsIHlvdSBhcmUgcG9zdGluZyB0by4gXFxuIyBDaGFubmVsIG5hbWVzIGNhbiBvbmx5IGNvbnRhaW4gbG93ZXJjYXNlIGxldHRlcnMsIG51bWJlcnMsIGh5cGhlbnMsIGFuZCB1bmRlcnNjb3JlcywgYW5kIG11c3QgYmUgMjEgY2hhcmFjdGVycyBvciBsZXNzLiBcXG4jIElmIHlvdSBsZWF2ZSB0aGlzIGZpZWxkIGVtcHR5LCBmdW5jdGlvbiB3aWxsIHRyeSB0byB1c2UgdGhlIHNsYWNrX2NoYW5uZWwgYXNzb2NpYXRlZCB3aXRoIHRoZSBJbmNpZGVudCBvciBUYXNrIGZvdW5kIGluIHRoZSBTbGFjayBDb252ZXJzYXRpb25zIGRhdGF0YWJsZS4gXFxuIyBJZiB0aGVyZSBpc25cdTIwMTl0IG9uZSBkZWZpbmVkLCB0aGUgd29ya2Zsb3cgd2lsbCB0ZXJtaW5hdGUuXFxuaW5wdXRzLnNsYWNrX2NoYW5uZWwgPSBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19jaGFubmVsIGlmIHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2NoYW5uZWwgaXMgbm90IE5vbmUgZWxzZSBpbnB1dHMuc2xhY2tfY2hhbm5lbFxcblxcbiMgSXMgY2hhbm5lbCBwcml2YXRlXFxuIyBJbmRpY2F0ZSBpZiB0aGUgY2hhbm5lbCB5b3UgYXJlIHBvc3RpbmcgdG8gc2hvdWxkIGJlIHByaXZhdGUuXFxuaW5wdXRzLnNsYWNrX2lzX2NoYW5uZWxfcHJpdmF0ZSA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2lzX2NoYW5uZWxfcHJpdmF0ZSBpZiBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19pc19jaGFubmVsX3ByaXZhdGUgaXMgbm90IE5vbmUgZWxzZSBpbnB1dHMuc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlXFxuXFxuIyBTbGFjayB1c2VyIGVtYWlsc1xcbiMgQ29tbWEgc2VwYXJhdGVkIGxpc3Qgb2YgZW1haWxzIGJlbG9uZ2luZyB0byBTbGFjayB1c2VycyBpbiB5b3VyIHdvcmtzcGFjZSB0aGF0IHdpbGwgYmUgYWRkZWQgdG8geW91ciBjaGFubmVsLlxcbmlucHV0cy5zbGFja19wYXJ0aWNpcGFudF9lbWFpbHMgPSBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19wYXJ0aWNpcGFudF9lbWFpbHMgaWYgcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfcGFydGljaXBhbnRfZW1haWxzIGlzIG5vdCBOb25lIGVsc2UgaW5wdXRzLnNsYWNrX3BhcnRpY2lwYW50X2VtYWlsc1xcblxcbiMgU2xhY2sgYWRkaXRpb25hbCB0ZXh0IG1lc3NhZ2VcXG4jIEFkZGl0aW9uYWwgdGV4dCBtZXNzYWdlIHRvIGluY2x1ZGUgd2l0aCB0aGUgSW5jaWRlbnQsIE5vdGUsIEFydGlmYWN0LCBBdHRhY2htZW50IG9yIFRhc2sgZGF0YS5cXG5pbnB1dHMuc2xhY2tfdGV4dCA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX3RleHQgaWYgcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfdGV4dCBpcyBub3QgTm9uZSBlbHNlICcnXFxuXFxuIyBTbGFjayBDaGFubmVsIElELCBmYXN0ZXIgdGhhbiBmaW5kaW5nIHZpYSBjaGFubmVsIG5hbWVcXG5pbnB1dHMuc2xhY2tfY2hhbm5lbF9pZCA9IHJ1bGUucHJvcGVydGllcy5zbGFja19jaGFubmVsX2lkIGlmIHJ1bGUucHJvcGVydGllcy5zbGFja19jaGFubmVsX2lkIGVsc2UgaW5wdXRzLnNsYWNrX2NoYW5uZWxfaWRcXG5cIixcInByZV9wcm9jZXNzaW5nX3NjcmlwdF9sYW5ndWFnZVwiOlwicHl0aG9uXCJ9PC9yZXNpbGllbnQ6ZnVuY3Rpb24+PC9leHRlbnNpb25FbGVtZW50cz48aW5jb21pbmc+U2VxdWVuY2VGbG93XzFwcDBqdHc8L2luY29taW5nPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMTR3bWNsczwvb3V0Z29pbmc+PC9zZXJ2aWNlVGFzaz48ZW5kRXZlbnQgaWQ9XCJFbmRFdmVudF8wYTRzNW50XCI+PGluY29taW5nPlNlcXVlbmNlRmxvd18xNHdtY2xzPC9pbmNvbWluZz48L2VuZEV2ZW50PjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMXBwMGp0d1wiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlNlcnZpY2VUYXNrXzBua2I1bnVcIi8+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18xNHdtY2xzXCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tfMG5rYjVudVwiIHRhcmdldFJlZj1cIkVuZEV2ZW50XzBhNHM1bnRcIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiPjx0ZXh0PlN0YXJ0IHlvdXIgd29ya2Zsb3cgaGVyZTwvdGV4dD48L3RleHRBbm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBpZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiB0YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRleHRBbm5vdGF0aW9uXzAzYzg1dWpcIj48dGV4dD48IVtDREFUQVtQb3N0IHRoZSBhdHRhY2htZW50IHRvIHNsYWNrX2NoYW5uZWwgYXNzb2NpYXRlZCB3aXRoIHRoZSBJbmNpZGVudCBvciBUYXNrXG5dXT48L3RleHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlvbl8wMm93amtqXCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tfMG5rYjVudVwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzAzYzg1dWpcIi8+PC9wcm9jZXNzPjxicG1uZGk6QlBNTkRpYWdyYW0gaWQ9XCJCUE1ORGlhZ3JhbV8xXCI+PGJwbW5kaTpCUE1OUGxhbmUgYnBtbkVsZW1lbnQ9XCJ1bmRlZmluZWRcIiBpZD1cIkJQTU5QbGFuZV8xXCI+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bV9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjE2MlwiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIwXCIgd2lkdGg9XCI5MFwiIHg9XCIxNTdcIiB5PVwiMjIzXCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzMFwiIHdpZHRoPVwiMTAwXCIgeD1cIjk5XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzFzZXVqNDhcIiBpZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjE2OVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjIwXCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMTUzXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyNTRcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTZXJ2aWNlVGFza18wbmtiNW51XCIgaWQ9XCJTZXJ2aWNlVGFza18wbmtiNW51X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCI4MFwiIHdpZHRoPVwiMTAwXCIgeD1cIjMyMVwiIHk9XCIxNjZcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiRW5kRXZlbnRfMGE0czVudFwiIGlkPVwiRW5kRXZlbnRfMGE0czVudF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjU3MFwiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI1ODhcIiB5PVwiMjI3XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18xcHAwanR3XCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMXBwMGp0d19kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTk4XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIzMjFcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjI1OS41XCIgeT1cIjE4NFwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18xNHdtY2xzXCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMTR3bWNsc19kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiNDIxXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCI1NzBcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjQ5NS41XCIgeT1cIjE4NFwiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8wM2M4NXVqXCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8wM2M4NXVqX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzMFwiIHdpZHRoPVwiMzI3XCIgeD1cIjIyN1wiIHk9XCI0OFwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzAyb3dqa2pcIiBpZD1cIkFzc29jaWF0aW9uXzAyb3dqa2pfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjM3N1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMTY2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMzg5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCI3OFwiLz48L2JwbW5kaTpCUE1ORWRnZT48L2JwbW5kaTpCUE1OUGxhbmU+PC9icG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZpbml0aW9ucz4ifSwgImNvbnRlbnRfdmVyc2lvbiI6IDYsICJkZXNjcmlwdGlvbiI6ICJVcGxvYWQgSW5jaWRlbnQgb3IgVGFzayBBdHRhY2htZW50IHRvIHlvdXIgU2xhY2sgY2hhbm5lbCB3aXRoIGFuIG9wdGlvbmFsIGN1c3RvbSB0ZXh0IG1lc3NhZ2UuIiwgImV4cG9ydF9rZXkiOiAic2xhY2tfZXhhbXBsZV9wb3N0X2F0dGFjaG1lbnRfdG9fc2xhY2siLCAibGFzdF9tb2RpZmllZF9ieSI6ICJhZG1pbkBleGFtcGxlLmNvbSIsICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNjU5NTU0MDgxMTk2LCAibmFtZSI6ICJFeGFtcGxlOiBQb3N0IEluY2lkZW50IC8gVGFzayBBdHRhY2htZW50IHRvIFNsYWNrIiwgIm9iamVjdF90eXBlIjogImF0dGFjaG1lbnQiLCAicHJvZ3JhbW1hdGljX25hbWUiOiAic2xhY2tfZXhhbXBsZV9wb3N0X2F0dGFjaG1lbnRfdG9fc2xhY2siLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ1dWlkIjogImRjNGM4MzFjLWE0NDQtNGFhYy1hYTFjLWM3NDg5OWVmOWE1MCIsICJ3b3JrZmxvd19pZCI6IDM0fSwgeyJhY3Rpb25zIjogW10sICJjb250ZW50IjogeyJ2ZXJzaW9uIjogNSwgIndvcmtmbG93X2lkIjogInNsYWNrX2V4YW1wbGVfcG9zdF9tZXNzYWdlX3RvX3NsYWNrX190YXNrIiwgInhtbCI6ICI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48ZGVmaW5pdGlvbnMgeG1sbnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L01PREVMXCIgeG1sbnM6YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9ESVwiIHhtbG5zOm9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRENcIiB4bWxuczpvbWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RJXCIgeG1sbnM6cmVzaWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5cIiB4bWxuczp4c2Q9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNwYWNlPVwiaHR0cDovL3d3dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJzbGFja19leGFtcGxlX3Bvc3RfbWVzc2FnZV90b19zbGFja19fdGFza1wiIGlzRXhlY3V0YWJsZT1cInRydWVcIiBuYW1lPVwiRXhhbXBsZTogUG9zdCBUYXNrIHRvIFNsYWNrXCI+PGRvY3VtZW50YXRpb24+UG9zdCBtZXNzYWdlIGZyb20gYSBUYXNrIHRvIHlvdXIgU2xhY2sgY2hhbm5lbC4gU2VuZCBzcGVjaWZpY3MgYWJvdXQgdGhlIFRhc2sgd2l0aCBhbiBvcHRpb25hbCBjdXN0b20gdGV4dCBtZXNzYWdlLjwvZG9jdW1lbnRhdGlvbj48c3RhcnRFdmVudCBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3dfMTl4cmdyeTwvb3V0Z29pbmc+PC9zdGFydEV2ZW50PjxzZXJ2aWNlVGFzayBpZD1cIlNlcnZpY2VUYXNrXzFyOWpyMTJcIiBuYW1lPVwiUG9zdCBtZXNzYWdlIHRvIFNsYWNrXCIgcmVzaWxpZW50OnR5cGU9XCJmdW5jdGlvblwiPjxleHRlbnNpb25FbGVtZW50cz48cmVzaWxpZW50OmZ1bmN0aW9uIHV1aWQ9XCJkZWQyODI2Yy02NTI4LTRhMjYtYjJjOC0wY2YyMTVkY2UzYzNcIj57XCJpbnB1dHNcIjp7fSxcInBvc3RfcHJvY2Vzc2luZ19zY3JpcHRcIjpcInVzZXJzID0gXFxcIlxcXCJcXG5mb3IgdXNlciBpbiByZXN1bHRzLnVzZXJfaW5mbzpcXG4gIHVzZXJzICs9IFxcXCJ7fSBcXFxcblxcXCIuZm9ybWF0KHVzZXIpXFxuIyBDcmVhdGUgYSBub3RlXFxubm90ZVRleHQgPSB1XFxcIlxcXCJcXFwiVGFzayB3YXMgcG9zdGVkIHRvICZsdDthIGhyZWY9J3t9JyZndDtTbGFjayBjaGFubmVsICN7fSZsdDsvYSZndDsuIE1lbWJlcnMgb2YgdGhpcyBjaGFubmVsIGFyZTogXFxcXG57fVxcXCJcXFwiXFxcIi5mb3JtYXQocmVzdWx0cy51cmwsIHJlc3VsdHMuY2hhbm5lbCwgdXNlcnMpXFxudGFzay5hZGROb3RlKGhlbHBlci5jcmVhdGVSaWNoVGV4dChub3RlVGV4dCkpXCIsXCJwb3N0X3Byb2Nlc3Npbmdfc2NyaXB0X2xhbmd1YWdlXCI6XCJweXRob25cIixcInByZV9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiIyMjIyMjIyMjIyMjIyMjIyMjIyMjXFxuIyBUYXNrIGRhdGEgICAgICAgICAjXFxuIyMjIyMjIyMjIyMjIyMjIyMjIyMjXFxuXFxuIyBJbmNpZGVudCBpZCBmb3IgdGhlIFVSTFxcbmluY2lkZW50X2lkX3N0ciA9IHN0cihpbmNpZGVudC5pZClcXG5pZiB0YXNrOlxcbiAgaW5jaWRlbnRfaWRfc3RyICs9IFxcXCI/dGFza19pZD1cXFwiK3N0cih0YXNrLmlkKVxcblxcbiMgVGFzayBkdWUgZGF0ZSwgc2VuZCAwIGlmIGl0J3MgTm9uZVxcbnRhc2tfZHVlX2RhdGUgPSB0YXNrLmR1ZV9kYXRlIGlmIHRhc2suZHVlX2RhdGUgZWxzZSAwXFxuXFxuIyBUYXNrIFN0YXR1c1xcbnRhc2tfc3RhdHVzID0gXFxcIk9wZW5cXFwiIGlmIHRhc2suc3RhdHVzID09IFxcXCJPXFxcIiBlbHNlIFxcXCJDbG9zZWRcXFwiXFxuXFxuIyBTbGFjayBhZGRpdGlvbmFsIHRleHQgbWVzc2FnZVxcbiMgQWRkaXRpb25hbCB0ZXh0IG1lc3NhZ2UgdG8gaW5jbHVkZSB3aXRoIHRoZSBJbmNpZGVudCwgTm90ZSwgQXJ0aWZhY3QsIEF0dGFjaG1lbnQgb3IgVGFzayBkYXRhLlxcbnJ1bGVfYWRkaXRpb25hbF90ZXh0ID0gcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfdGV4dCBpZiBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja190ZXh0IGlzIG5vdCBOb25lIGVsc2UgJydcXG5cXG4jIFNsYWNrIHRleHQgbWVzc2FnZSBpbiBKU09OIGZvcm1hdFxcbiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXFxuIyBEbyBub3QgcmVtb3ZlIGZpcnN0IDMgZWxlbWVudHMgXFxcIkFkZGl0aW9uYWwgVGV4dFxcXCIsIFxcXCJSZXNpbGllbnQgVVJMXFxcIiBhbmQgXFxcIlR5cGUgb2YgZGF0YVxcXCIsXFxuIyB0aGUgaW5mb3JtYXRpb24gaXMgdXNlZCB0byBnZW5lcmF0ZSB0aGUgdGl0bGUgb2YgdGhlIG1lc3NhZ2UuXFxuI1xcbiMgQWRkL3JlbW92ZSBpbmZvcm1hdGlvbiB1c2luZyB0aGUgc3ludGF4OlxcbiMgXFxcImxhYmVsXFxcIjoge3sgXFxcInR5cGVcXFwiOiBcXFwiW3N0cmluZ3xyaWNodGV4dHxib29sZWFufGRhdGV0aW1lXFxcIiwgXFxcImRhdGFcXFwiOiBcXFwicmVzaWxpZW50IGZpZWxkIGRhdGFcXFwiIH19XFxuI1xcbiMgTWFrZSBzdXJlIHRvIHNlbmQgXFxcImRhdGV0aW1lXFxcIiB0eXBlcyBhcyBpbnRlZ2VycyBhbmQgbm90IHN0cmluZ3M6XFxuIyB3aXRob3V0IGRvdWJsZSBxdW90ZXM6IHsgXFxcInR5cGVcXFwiOiBcXFwiZGF0ZXRpbWVcXFwiLCBcXFwiZGF0YVxcXCI6IHJlc2lsaWVudCBkYXRldGltZSBkYXRhfSBcXG4jXFxuIyBUZXh0IGZpZWxkcyBsaWtlICd0YXNrIG5hbWUnIG9yICdTbGFjayBhZGRpdGlvbmFsIHRleHQgbWVzc2FnZScgY2FuIGluY2x1ZGUgZG91YmxlIHF1b3Rlcy5cXG4jIFdhdGNoIG91dCBmb3IgZW1iZWRkZWQgZG91YmxlIHF1b3RlcyBpbiB0aGVzZSB0ZXh0IGZpZWxkcyBhbmQgZXNjYXBlIHdpdGggZmllbGQucmVwbGFjZSh1J1xcXCInLCB1J1xcXFxcXFxcXFxcIicpIG90aGVyd2lzZSBqc29uLmxvYWRzIHdpbGwgZmFpbC5cXG5zbGFja190ZXh0ID0gdVxcXCJcXFwiXFxcInt7XFxuICBcXFwiQWRkaXRpb25hbCBUZXh0XFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJzdHJpbmdcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7MH1cXFwiIH19LFxcbiAgXFxcIlJlc2lsaWVudCBVUkxcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcImluY2lkZW50XFxcIiwgXFxcImRhdGFcXFwiOiBcXFwiezF9XFxcIiB9fSxcXG4gIFxcXCJUeXBlIG9mIGRhdGFcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcInN0cmluZ1xcXCIsIFxcXCJkYXRhXFxcIjogXFxcInsyfVxcXCIgfX0sXFxuICBcXFwiSW5jaWRlbnQgSURcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcInN0cmluZ1xcXCIsIFxcXCJkYXRhXFxcIjogXFxcInszfVxcXCIgfX0sXFxuICBcXFwiVGFzayBOYW1lXFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJzdHJpbmdcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7NH1cXFwiIH19LFxcbiAgXFxcIlRhc2sgU3RhdHVzXFxcIjoge3tcXFwidHlwZVxcXCI6IFxcXCJzdHJpbmdcXFwiLCBcXFwiZGF0YVxcXCI6IFxcXCJ7NX1cXFwiIH19LFxcbiAgXFxcIlRhc2sgT3duZXJcXFwiOiB7e1xcXCJ0eXBlXFxcIjogXFxcInN0cmluZ1xcXCIsIFxcXCJkYXRhXFxcIjogXFxcIns2fVxcXCIgfX0sXFxuICBcXFwiVGFzayBEdWUgRGF0ZVxcXCI6IHt7XFxcInR5cGVcXFwiOiBcXFwiZGF0ZXRpbWVcXFwiLCBcXFwiZGF0YVxcXCI6IHs3fSB9fVxcbn19XFxcIlxcXCJcXFwiLmZvcm1hdChcXG4gIHJ1bGVfYWRkaXRpb25hbF90ZXh0LnJlcGxhY2UodSdcXFwiJywgdSdcXFxcXFxcXFxcXCInKSxcXG4gIGluY2lkZW50X2lkX3N0cixcXG4gIFxcXCJUYXNrXFxcIixcXG4gIHN0cihpbmNpZGVudC5pZCksXFxuICB0YXNrLm5hbWUucmVwbGFjZSh1J1xcXCInLCB1J1xcXFxcXFxcXFxcIicpLFxcbiAgdGFza19zdGF0dXMsXFxuICB0YXNrLm93bmVyX2lkLFxcbiAgdGFza19kdWVfZGF0ZSlcXG5cXG4jIFNsYWNrIHVzZXJuYW1lIC0gb3B0aW9uYWwgc2V0dGluZ1xcbiMgU2V0IHRvIHRydWUgYW5kIHRoZSBhdXRoZW50aWNhdGVkIHVzZXIgb2YgdGhlIFNsYWNrIEFwcCB3aWxsIGFwcGVhciBhcyB0aGUgYXV0aG9yIG9mIHRoZSBtZXNzYWdlLCBpZ25vcmluZyBhbnkgdmFsdWVzIHByb3ZpZGVkIGZvciBzbGFja191c2VybmFtZS4gXFxuIyBTZXQgeW91ciBib3QncyBuYW1lIHRvIFRhc2sncyBjcmVhdG9yIHRvIGFwcGVhciBhcyB0aGUgYXV0aG9yIG9mIHRoZSBtZXNzYWdlLiBNdXN0IGJlIHVzZWQgaW4gY29uanVuY3Rpb24gd2l0aCBzbGFja19hc191c2VyIHNldCB0byBmYWxzZSwgb3RoZXJ3aXNlIGlnbm9yZWQuXFxuI2lucHV0cy5zbGFja19hc191c2VyID0gRmFsc2VcXG4jaW5wdXRzLnNsYWNrX3VzZXJuYW1lID0gdGFzay5jcmVhdG9yX2lkXFxuXFxuIyBJRCBvZiB0aGlzIGluY2lkZW50XFxuaW5wdXRzLmluY2lkZW50X2lkID0gaW5jaWRlbnQuaWRcXG5cXG4jIElEIG9mIHRoaXMgVGFza1xcbmlucHV0cy50YXNrX2lkID0gdGFzay5pZFxcblxcbiMgU2xhY2sgY2hhbm5lbCBuYW1lXFxuIyBOYW1lIG9mIHRoZSBleGlzdGluZyBTbGFjayBXb3Jrc3BhY2UgY2hhbm5lbCBvciBhIG5ldyBTbGFjayBjaGFubmVsIHlvdSBhcmUgcG9zdGluZyB0by4gXFxuIyBDaGFubmVsIG5hbWVzIGNhbiBvbmx5IGNvbnRhaW4gbG93ZXJjYXNlIGxldHRlcnMsIG51bWJlcnMsIGh5cGhlbnMsIGFuZCB1bmRlcnNjb3JlcywgYW5kIG11c3QgYmUgMjEgY2hhcmFjdGVycyBvciBsZXNzLiBcXG4jIElmIHlvdSBsZWF2ZSB0aGlzIGZpZWxkIGVtcHR5LCBmdW5jdGlvbiB3aWxsIHRyeSB0byB1c2UgdGhlIHNsYWNrX2NoYW5uZWwgYXNzb2NpYXRlZCB3aXRoIHRoZSBJbmNpZGVudCBvciBUYXNrIGZvdW5kIGluIHRoZSBTbGFjayBDb252ZXJzYXRpb25zIGRhdGF0YWJsZS4gXFxuIyBJZiB0aGVyZSBpc25cdTIwMTl0IG9uZSBkZWZpbmVkLCB0aGUgd29ya2Zsb3cgd2lsbCB0ZXJtaW5hdGUuXFxuaW5wdXRzLnNsYWNrX2NoYW5uZWwgPSBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19jaGFubmVsIGlmIHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2NoYW5uZWwgaXMgbm90IE5vbmUgZWxzZSBpbnB1dHMuc2xhY2tfY2hhbm5lbFxcblxcbiMgSXMgY2hhbm5lbCBwcml2YXRlXFxuIyBJbmRpY2F0ZSBpZiB0aGUgY2hhbm5lbCB5b3UgYXJlIHBvc3RpbmcgdG8gc2hvdWxkIGJlIHByaXZhdGUuXFxuaW5wdXRzLnNsYWNrX2lzX2NoYW5uZWxfcHJpdmF0ZSA9IHJ1bGUucHJvcGVydGllcy5ydWxlX3NsYWNrX2lzX2NoYW5uZWxfcHJpdmF0ZSBpZiBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19pc19jaGFubmVsX3ByaXZhdGUgaXMgbm90IE5vbmUgZWxzZSBpbnB1dHMuc2xhY2tfaXNfY2hhbm5lbF9wcml2YXRlXFxuXFxuIyBTbGFjayB1c2VyIGVtYWlsc1xcbiMgQ29tbWEgc2VwYXJhdGVkIGxpc3Qgb2YgZW1haWxzIGJlbG9uZ2luZyB0byBTbGFjayB1c2VycyBpbiB5b3VyIHdvcmtzcGFjZSB0aGF0IHdpbGwgYmUgYWRkZWQgdG8geW91ciBjaGFubmVsLlxcbmlucHV0cy5zbGFja19wYXJ0aWNpcGFudF9lbWFpbHMgPSBydWxlLnByb3BlcnRpZXMucnVsZV9zbGFja19wYXJ0aWNpcGFudF9lbWFpbHMgaWYgcnVsZS5wcm9wZXJ0aWVzLnJ1bGVfc2xhY2tfcGFydGljaXBhbnRfZW1haWxzIGlzIG5vdCBOb25lIGVsc2UgaW5wdXRzLnNsYWNrX3BhcnRpY2lwYW50X2VtYWlsc1xcblxcbiMgU2xhY2sgdGV4dCBtZXNzYWdlXFxuIyBDb250YWluZXIgZmllbGQgdG8gcmV0YWluIEpTT04gZmllbGRzIHRvIHNlbmQgdG8gU2xhY2tcXG5pbnB1dHMuc2xhY2tfdGV4dCA9IHNsYWNrX3RleHRcXG5cXG4jIFNsYWNrIENoYW5uZWwgSUQsIGZhc3RlciB0aGFuIGZpbmRpbmcgdmlhIGNoYW5uZWwgbmFtZVxcbmlucHV0cy5zbGFja19jaGFubmVsX2lkID0gcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgaWYgcnVsZS5wcm9wZXJ0aWVzLnNsYWNrX2NoYW5uZWxfaWQgZWxzZSBpbnB1dHMuc2xhY2tfY2hhbm5lbF9pZFxcblwiLFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0X2xhbmd1YWdlXCI6XCJweXRob25cIn08L3Jlc2lsaWVudDpmdW5jdGlvbj48L2V4dGVuc2lvbkVsZW1lbnRzPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMTl4cmdyeTwvaW5jb21pbmc+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18wZTAxcWkwPC9vdXRnb2luZz48L3NlcnZpY2VUYXNrPjxlbmRFdmVudCBpZD1cIkVuZEV2ZW50XzBwMzNlN3NcIj48aW5jb21pbmc+U2VxdWVuY2VGbG93XzBlMDFxaTA8L2luY29taW5nPjwvZW5kRXZlbnQ+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18xOXhyZ3J5XCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tfMXI5anIxMlwiLz48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzBlMDFxaTBcIiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18xcjlqcjEyXCIgdGFyZ2V0UmVmPVwiRW5kRXZlbnRfMHAzM2U3c1wiLz48dGV4dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCI+PHRleHQ+U3RhcnQgeW91ciB3b3JrZmxvdyBoZXJlPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMHBmcjY4N1wiPjx0ZXh0PlNlbGVjdCB0aGUgc2xhY2tfY2hhbm5lbCB0byBwb3N0IGluIGFuZCBhZGp1c3QgdGhlIHBvc3RpbmcgcGFyYW1ldGVycyBhcyBuZWVkZWQuPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMXN3MzlsbVwiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNrXzFyOWpyMTJcIiB0YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8wcGZyNjg3XCIvPjwvcHJvY2Vzcz48YnBtbmRpOkJQTU5EaWFncmFtIGlkPVwiQlBNTkRpYWdyYW1fMVwiPjxicG1uZGk6QlBNTlBsYW5lIGJwbW5FbGVtZW50PVwidW5kZWZpbmVkXCIgaWQ9XCJCUE1OUGxhbmVfMVwiPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU3RhcnRFdmVudF8xNTVhc3htXCIgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1fZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9XCIxNjJcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMFwiIHdpZHRoPVwiOTBcIiB4PVwiMTU3XCIgeT1cIjIyM1wiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzBcIiB3aWR0aD1cIjEwMFwiIHg9XCI5OVwiIHk9XCIyNTRcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIgaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIxNjlcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIyMFwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjE1M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU2VydmljZVRhc2tfMXI5anIxMlwiIGlkPVwiU2VydmljZVRhc2tfMXI5anIxMl9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiODBcIiB3aWR0aD1cIjEwMFwiIHg9XCIzMzJcIiB5PVwiMTY2XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIkVuZEV2ZW50XzBwMzNlN3NcIiBpZD1cIkVuZEV2ZW50XzBwMzNlN3NfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9XCI1ODNcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNjAxXCIgeT1cIjIyN1wiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJTZXF1ZW5jZUZsb3dfMTl4cmdyeVwiIGlkPVwiU2VxdWVuY2VGbG93XzE5eHJncnlfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjE5OFwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMzMyXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCIyNjVcIiB5PVwiMTg0XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzBlMDFxaTBcIiBpZD1cIlNlcXVlbmNlRmxvd18wZTAxcWkwX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0MzJcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjU4M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNTA3LjVcIiB5PVwiMTg0LjVcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiVGV4dEFubm90YXRpb25fMHBmcjY4N1wiIGlkPVwiVGV4dEFubm90YXRpb25fMHBmcjY4N19kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzBcIiB3aWR0aD1cIjI4NlwiIHg9XCIxOTdcIiB5PVwiNTFcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJBc3NvY2lhdGlvbl8xc3czOWxtXCIgaWQ9XCJBc3NvY2lhdGlvbl8xc3czOWxtX2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIzNzBcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjE2NlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjM0NVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiODFcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PC9icG1uZGk6QlBNTlBsYW5lPjwvYnBtbmRpOkJQTU5EaWFncmFtPjwvZGVmaW5pdGlvbnM+In0sICJjb250ZW50X3ZlcnNpb24iOiA1LCAiZGVzY3JpcHRpb24iOiAiUG9zdCBtZXNzYWdlIGZyb20gYSBUYXNrIHRvIHlvdXIgU2xhY2sgY2hhbm5lbC4gU2VuZCBzcGVjaWZpY3MgYWJvdXQgdGhlIFRhc2sgd2l0aCBhbiBvcHRpb25hbCBjdXN0b20gdGV4dCBtZXNzYWdlLiIsICJleHBvcnRfa2V5IjogInNsYWNrX2V4YW1wbGVfcG9zdF9tZXNzYWdlX3RvX3NsYWNrX190YXNrIiwgImxhc3RfbW9kaWZpZWRfYnkiOiAiYWRtaW5AZXhhbXBsZS5jb20iLCAibGFzdF9tb2RpZmllZF90aW1lIjogMTY1OTU1NDMxNzI0MSwgIm5hbWUiOiAiRXhhbXBsZTogUG9zdCBUYXNrIHRvIFNsYWNrIiwgIm9iamVjdF90eXBlIjogInRhc2siLCAicHJvZ3JhbW1hdGljX25hbWUiOiAic2xhY2tfZXhhbXBsZV9wb3N0X21lc3NhZ2VfdG9fc2xhY2tfX3Rhc2siLCAidGFncyI6IFt7InRhZ19oYW5kbGUiOiAiZm5fc2xhY2siLCAidmFsdWUiOiBudWxsfV0sICJ1dWlkIjogImViYThmMjcwLTJkMDMtNGRhOC1hODEyLTJjODc4Mzc0MjQ1NCIsICJ3b3JrZmxvd19pZCI6IDM2fV0sICJ3b3Jrc3BhY2VzIjogW119",
  "info": {
    "CRC": 1492648105,
    "comment": "",
    "compress_size": 10780,
    "compress_type": 8,
    "create_system": 3,
    "create_version": 20,
    "date_time": 1661452332000,
    "external_attr": 2175008768,
    "extract_version": 20,
    "file_size": 101541,
    "filename": "export.res",
    "flag_bits": 0,
    "header_offset": 588360,
    "internal_attr": 0,
    "volume": 0
  }
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
# Required inputs are: the incident id and attachment id
inputs.incident_id = incident.id
inputs.attachment_id = attachment.id

# If this is a "task attachment" then we will additionally have a task-id
if task is not None:
  inputs.task_id = task.id

# The path within the zip that we want to extract
inputs.soar_utils_file_path = playbook.inputs.soar_utils_extract_file_path

# If the zipfile is password protected, specify here
# inputs.zipfile_password = 
if playbook.inputs.soar_utils_zip_password:
  inputs.soar_utils_zipfile_password = playbook.inputs.soar_utils_zip_password
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
None
```

</p>
</details>

---
## Function - SOAR Utilities: Attachment Zip List
Reads a ZIP file and produces a list of the file paths, and a list with detailed information about each file.

 ![screenshot: fn-soar-utilities-attachment-zip-list ](./doc/screenshots/fn-soar-utilities-attachment-zip-list.png) 

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `attachment_id` | `number` | No | `-` | - |
| `incident_id` | `number` | Yes | `-` | - |
| `task_id` | `number` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "infolist": [
    {
      "CRC": 2624755629,
      "comment": "",
      "compress_size": 563006,
      "compress_type": 8,
      "create_system": 3,
      "create_version": 20,
      "date_time": 1661452332000,
      "external_attr": 2175008768,
      "extract_version": 20,
      "file_size": 562852,
      "filename": "fn_slack-2.0.0.tar.gz",
      "flag_bits": 0,
      "header_offset": 0,
      "internal_attr": 0,
      "volume": 0
    },
    {
      "CRC": 3145654620,
      "comment": "",
      "compress_size": 25265,
      "compress_type": 8,
      "create_system": 3,
      "create_version": 20,
      "date_time": 1661452332000,
      "external_attr": 2175008768,
      "extract_version": 20,
      "file_size": 33851,
      "filename": "app.json",
      "flag_bits": 0,
      "header_offset": 563057,
      "internal_attr": 0,
      "volume": 0
    },
    {
      "CRC": 1492648105,
      "comment": "",
      "compress_size": 10780,
      "compress_type": 8,
      "create_system": 3,
      "create_version": 20,
      "date_time": 1661452332000,
      "external_attr": 2175008768,
      "extract_version": 20,
      "file_size": 101541,
      "filename": "export.res",
      "flag_bits": 0,
      "header_offset": 588360,
      "internal_attr": 0,
      "volume": 0
    }
  ],
  "namelist": [
    "fn_slack-2.0.0.tar.gz",
    "app.json",
    "export.res"
  ]
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.incident_id = incident.id
inputs.attachment_id = attachment.id

# If this is a "task attachment" then we will additionally have a task-id
if task is not None:
  inputs.task_id = task.id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.zip_list_result

# Note with the list of filenames in the ZIP
namelist_html = (
    f"<div><p><b>SOAR Utils: Zip List - Example (PB):</b></p>"
    f"<p><b>Contents of {attachment.name}:</b></p>"
)
namelist_html += "".join(f"{filename}<br>" for filename in results.namelist)
namelist_html += "</div>"

incident.addNote(namelist_html)

# Note with detailed information for each file in the ZIP
infolist_html = (
    f"<div><p><b>SOAR Utils: Zip List - Example (PB):</b></p>"
    f"<p><b>Detailed contents of {attachment.name}:</b></p>"
)
for fileinfo in results.infolist:
    filename = fileinfo.get("filename", "Unknown")
    file_size = fileinfo.get("file_size", "N/A")
    compress_size = fileinfo.get("compress_size", "N/A")
    comment = fileinfo.get("comment", "")
    
    infolist_html += (
        f"{filename} ({file_size} bytes, {compress_size} compressed) {comment}<br>"
    )
infolist_html += "</div>"

incident.addNote(infolist_html)

```

</p>
</details>

---
## Function - SOAR Utilities: Base64 to Artifact
Creates a new artifact from a Base64 string. You can  specify the artifact type and description.

 ![screenshot: fn-soar-utilities-base64-to-artifact ](./doc/screenshots/fn-soar-utilities-base64-to-artifact.png) 

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `incident_id` | `number` | Yes | `-` | - |
| `soar_utils_artifact_file_type` | `select` | No | `-` | - |
| `soar_utils_base64content` | `text` | No | `-` | - |
| `soar_utils_content_type` | `text` | No | `-` | - |
| `soar_utils_description` | `textarea` | No | `-` | - |
| `soar_utils_file_name` | `text` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "actions": [],
  "attachment": {
    "actions": [
      {
        "enabled": true,
        "id": 33,
        "name": "Example: Virus Total for Attachments"
      },
      {
        "enabled": true,
        "id": 34,
        "name": "Example: Google Cloud - Inspect Attachment for PII"
      },
      {
        "enabled": true,
        "id": 35,
        "name": "Example: Google Cloud - Remove PII from Attachment"
      },
      {
        "enabled": true,
        "id": 47,
        "name": "Example: Attachment Hash"
      },
      {
        "enabled": true,
        "id": 48,
        "name": "Example: Attachment to Base64"
      },
      {
        "enabled": true,
        "id": 52,
        "name": "Example: Email Parsing (Attachment)"
      },
      {
        "enabled": true,
        "id": 41,
        "name": "Example: Post Incident / Task Attachment to Slack"
      },
      {
        "enabled": true,
        "id": 85,
        "name": "Example: SOAR Utilities Attachment Hash"
      },
      {
        "enabled": true,
        "id": 87,
        "name": "Example: SOAR Utilities Attachment to Base64"
      },
      {
        "enabled": true,
        "id": 59,
        "name": "Example: PDFiD"
      },
      {
        "enabled": true,
        "id": 60,
        "name": "Example: Resilient Search"
      },
      {
        "enabled": true,
        "id": 90,
        "name": "Example: SOAR Utilities SOAR Search"
      },
      {
        "enabled": false,
        "id": 65,
        "name": "Example: Use Excel Data"
      },
      {
        "enabled": false,
        "id": 67,
        "name": "Example: Zip Extract"
      },
      {
        "enabled": false,
        "id": 68,
        "name": "Example: Zip List"
      },
      {
        "enabled": false,
        "id": 96,
        "name": "Example: SOAR Utilities Zip List"
      },
      {
        "enabled": false,
        "id": 95,
        "name": "Example: SOAR Utilities Zip Extract"
      },
      {
        "enabled": false,
        "id": 97,
        "name": "Example: SOAR Utilities Zip Extract to Artifact"
      }
    ],
    "content_type": "image/jpeg",
    "created": 1663775473887,
    "creator_id": 6,
    "id": 71,
    "inc_id": 2112,
    "inc_name": "SOAR Utilities",
    "inc_owner": 1,
    "name": "tmppe_6ed00",
    "playbooks": [],
    "size": 180520,
    "task_at_id": null,
    "task_custom": null,
    "task_id": null,
    "task_members": null,
    "task_name": null,
    "type": "artifact",
    "uuid": "b2fb5c8f-92f8-46a8-a2a8-8b9342a1bb64",
    "vers": 12
  },
  "created": 1663775473530,
  "creator_principal": {
    "display_name": "Integration Server v43",
    "id": 6,
    "name": "0228e00e-2c47-43e6-a736-550f104c94ea",
    "type": "apikey"
  },
  "description": null,
  "global_artifact": [],
  "global_info": null,
  "hash": "c670630c6c19434*******800bffd4cf5d5c361d64c8c92c628f1aba368ee",
  "hits": [],
  "id": 547,
  "inc_id": 2112,
  "inc_name": "SOAR Utilities",
  "inc_owner": 1,
  "ip": {
    "destination": null,
    "source": null
  },
  "last_modified_by": {
    "display_name": "Integration Server v43",
    "id": 6,
    "name": "0228e00e-2c47-43e6-a736-550f104c94ea",
    "type": "apikey"
  },
  "last_modified_time": 1663775473899,
  "parent_id": null,
  "pending_scan_result": false,
  "pending_sources": [],
  "perms": null,
  "playbooks": [],
  "properties": null,
  "related_incident_count": null,
  "relating": true,
  "type": 7,
  "value": "export.res.b64"
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.soar_utils_base64content = playbook.functions.results.zip_extract_result.content
file_name = playbook.inputs.soar_utils_extract_file_path.split('/')[-1]

inputs.incident_id = incident.id
inputs.soar_utils_file_name = file_name + ".b64"
inputs.soar_utils_content_type = "image/jpeg"
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.zip_extract_to_artifact_result
if results:
  note_text = f"<b> SOAR Utils: Zip Extract to Artifact - Example (PB) </b> File {results.get('value',None)} saved successfully in the artifact."
else:
  note_text = f"<b>SOAR Utils: Zip Extract to Artifact - Example (PB)</b> Failed: {results.reason}"

incident.addNote(note_text)

```

</p>
</details>

---
## Function - SOAR Utilities: Base64 to Attachment
Creates a new attachment from a base64 string.

 ![screenshot: fn-soar-utilities-base64-to-attachment ](./doc/screenshots/fn-soar-utilities-base64-to-attachment.png) 

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `incident_id` | `number` | Yes | `-` | - |
| `soar_utils_base64content` | `text` | No | `-` | - |
| `soar_utils_content_type` | `text` | No | `-` | - |
| `soar_utils_file_name` | `text` | No | `-` | - |
| `task_id` | `number` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "actions": [
    {
      "enabled": true,
      "id": 33,
      "name": "Example: Virus Total for Attachments"
    },
    {
      "enabled": true,
      "id": 34,
      "name": "Example: Google Cloud - Inspect Attachment for PII"
    },
    {
      "enabled": true,
      "id": 35,
      "name": "Example: Google Cloud - Remove PII from Attachment"
    },
    {
      "enabled": true,
      "id": 47,
      "name": "Example: Attachment Hash"
    },
    {
      "enabled": true,
      "id": 48,
      "name": "Example: Attachment to Base64"
    },
    {
      "enabled": true,
      "id": 52,
      "name": "Example: Email Parsing (Attachment)"
    },
    {
      "enabled": true,
      "id": 41,
      "name": "Example: Post Incident / Task Attachment to Slack"
    },
    {
      "enabled": true,
      "id": 85,
      "name": "Example: SOAR Utilities Attachment Hash"
    },
    {
      "enabled": true,
      "id": 87,
      "name": "Example: SOAR Utilities Attachment to Base64"
    },
    {
      "enabled": true,
      "id": 59,
      "name": "Example: PDFiD"
    },
    {
      "enabled": true,
      "id": 60,
      "name": "Example: Resilient Search"
    },
    {
      "enabled": true,
      "id": 90,
      "name": "Example: SOAR Utilities SOAR Search"
    },
    {
      "enabled": false,
      "id": 65,
      "name": "Example: Use Excel Data"
    },
    {
      "enabled": false,
      "id": 67,
      "name": "Example: Zip Extract"
    },
    {
      "enabled": false,
      "id": 68,
      "name": "Example: Zip List"
    },
    {
      "enabled": false,
      "id": 96,
      "name": "Example: SOAR Utilities Zip List"
    },
    {
      "enabled": false,
      "id": 95,
      "name": "Example: SOAR Utilities Zip Extract"
    }
  ],
  "content_type": "image/jpeg",
  "created": 1663772427768,
  "creator_id": 6,
  "id": 70,
  "inc_id": 2112,
  "inc_name": "SOAR Utilities",
  "inc_owner": 1,
  "name": "export.res.b64",
  "playbooks": [],
  "size": 101541,
  "task_at_id": null,
  "task_custom": null,
  "task_id": null,
  "task_members": null,
  "task_name": null,
  "type": "incident",
  "uuid": "999c463c-4382-4435-9b3e-663f166080a8",
  "vers": 11
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.soar_utils_base64content = playbook.functions.results.zip_extract_result.content
file_name = playbook.inputs.soar_utils_extract_file_path.split('/')[-1]

inputs.incident_id = incident.id
inputs.soar_utils_file_name = file_name + ".b64"
inputs.soar_utils_content_type = "image/jpeg"
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.zip_extract_to_base64_result

if results:
  note_text = f'<b> SOAR Utils: Zip Extract - Example (PB) </b> File {results.get("name", None)} saved successfully in the attachment.'
else:
  note_text = f"<b>SOAR Utils: Zip Extract - Example (PB)</b> Failed: {results.reason}"

incident.addNote(note_text)

```

</p>
</details>

---
## Function - SOAR Utilities: Close Incident
Function that takes an incident_id and a JSON String of field_name and field_value pairs to close an Incident.

 ![screenshot: fn-soar-utilities-close-incident ](./doc/screenshots/fn-soar-utilities-close-incident.png) 

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `incident_id` | `number` | Yes | `-` | - |
| `soar_utils_close_fields` | `text` | Yes | `-` | A JSON String of the fields required to close an Incident e.g.: {'resolution_id':'Resolved','resolution_summary':'closing'} |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "hints": [],
    "message": null,
    "success": true,
    "title": null
  },
  "inputs": {
    "incident_id": 2114,
    "soar_utils_close_fields": "{\"resolution_id\":\"Resolved\",\"resolution_summary\":\"closing\"}"
  },
  "metrics": {
    "execution_time_ms": 1781,
    "host": "Christophers-MacBook-Pro-2.local",
    "package": "fn-soar-utils",
    "package_version": "1.0.0",
    "timestamp": "2022-09-19 14:00:50",
    "version": "1.0"
  },
  "raw": "{\"success\": true, \"title\": null, \"message\": null, \"hints\": []}",
  "reason": null,
  "success": true,
  "version": "1.0"
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
from json import dumps
close_fields = {"resolution_id": playbook.inputs.soar_utils_resolution_id,
                "resolution_summary": playbook.inputs.soar_utils_resolution_summary}

inputs.incident_id = incident.id
inputs.soar_utils_close_fields = dumps(close_fields)
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.close_incident_result

if results.get("success"):
  note_text = f"<b>SOAR Utils: Close Incident - Example (PB)</b> incident {results.inputs.incident_id} successfully closed."
else:
  note_text = f"<b>SOAR Utils: Close Incident - Example (PB)</b> Failed: {results.reason}"
incident.addNote(note_text)

```

</p>
</details>

---
## Function - SOAR Utilities: Create Incident
Create an incident from a function

 ![screenshot: fn-soar-utilities-create-incident ](./doc/screenshots/fn-soar-utilities-create-incident.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `soar_utils_create_fields` | `text` | Yes | `-` | json string fields to create an incident |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "actions": [
      {
        "enabled": true,
        "id": 69,
        "name": "Timer Epoch"
      },
      {
        "enabled": true,
        "id": 70,
        "name": "Timer in Parallel"
      },
      {
        "enabled": false,
        "id": 72,
        "name": "Symantec DLP: Get DLP Notes"
      },
      {
        "enabled": true,
        "id": 37,
        "name": "Example: Archive Incident Slack Channel"
      },
      {
        "enabled": true,
        "id": 42,
        "name": "Example: Post Incident to Slack"
      },
      {
        "enabled": false,
        "id": 75,
        "name": "Symantec DLP: Update DLP Incident"
      },
      {
        "enabled": false,
        "id": 78,
        "name": "Symantec DLP: Upload Binaries as Artifact"
      },
      {
        "enabled": false,
        "id": 79,
        "name": "Symantec DLP: Write DLP Incident Details to Note"
      },
      {
        "enabled": true,
        "id": 81,
        "name": "Example: Close Incident"
      },
      {
        "enabled": true,
        "id": 82,
        "name": "Example: Create Incident"
      },
      {
        "enabled": true,
        "id": 83,
        "name": "Example: Search Incidents"
      },
      {
        "enabled": true,
        "id": 55,
        "name": "Example: Get Incident Contact Info"
      },
      {
        "enabled": true,
        "id": 88,
        "name": "Example: SOAR Utilities Close Incident"
      },
      {
        "enabled": true,
        "id": 89,
        "name": "Example: SOAR Utilities Create Incident"
      },
      {
        "enabled": true,
        "id": 91,
        "name": "Example: SOAR Utilities Get Incident Contact Info"
      },
      {
        "enabled": true,
        "id": 63,
        "name": "Example: Timer Epoch"
      },
      {
        "enabled": true,
        "id": 64,
        "name": "Example: Timers in Parallel"
      },
      {
        "enabled": true,
        "id": 93,
        "name": "Example: SOAR Utilities Search Incidents"
      }
    ],
    "addr": null,
    "admin_id": null,
    "artifacts": null,
    "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
    "city": null,
    "cm": {
      "geo_counts": {},
      "total": 0,
      "unassigneds": []
    },
    "comments": null,
    "confirmed": false,
    "country": null,
    "create_date": 1663297952673,
    "creator": null,
    "creator_id": 6,
    "creator_principal": {
      "display_name": "Chris\u0027 Integration Server v43",
      "id": 6,
      "name": "0228e00e-2c47-43e6-a736-550f104c94ea",
      "type": "apikey"
    },
    "crimestatus_id": 1,
    "data_compromised": null,
    "description": "Testing",
    "discovered_date": 1621110044000,
    "draft": false,
    "dtm": {},
    "due_date": null,
    "employee_involved": null,
    "end_date": null,
    "exposure": 0,
    "exposure_dept_id": null,
    "exposure_individual_name": null,
    "exposure_type_id": 1,
    "exposure_vendor_id": null,
    "gdpr": {
      "gdpr_breach_circumstances": [],
      "gdpr_breach_type": null,
      "gdpr_breach_type_comment": null,
      "gdpr_consequences": null,
      "gdpr_consequences_comment": null,
      "gdpr_final_assessment": null,
      "gdpr_final_assessment_comment": null,
      "gdpr_identification": null,
      "gdpr_identification_comment": null,
      "gdpr_personal_data": null,
      "gdpr_personal_data_comment": null,
      "gdpr_subsequent_notification": null
    },
    "hard_liability": 0,
    "hipaa": {
      "hipaa_acquired": null,
      "hipaa_acquired_comment": null,
      "hipaa_additional_misuse": null,
      "hipaa_additional_misuse_comment": null,
      "hipaa_adverse": null,
      "hipaa_adverse_comment": null,
      "hipaa_breach": null,
      "hipaa_breach_comment": null,
      "hipaa_misused": null,
      "hipaa_misused_comment": null
    },
    "id": 2114,
    "inc_last_modified_date": 1663297953098,
    "inc_start": null,
    "inc_training": false,
    "incident_type_ids": [],
    "is_scenario": false,
    "jurisdiction_name": null,
    "jurisdiction_reg_id": null,
    "members": [],
    "name": "Create Incident",
    "negative_pr_likely": null,
    "nist_attack_vectors": [],
    "org_handle": 201,
    "org_id": 201,
    "owner_id": 3,
    "perms": {
      "assign": true,
      "attach_file": true,
      "change_members": true,
      "change_workspace": true,
      "close": true,
      "comment": true,
      "create_artifacts": true,
      "create_milestones": true,
      "delete": true,
      "delete_attachments": true,
      "list_artifacts": true,
      "list_milestones": true,
      "read": true,
      "read_attachments": true,
      "write": true
    },
    "phase_id": 1000,
    "pii": {
      "alberta_health_risk_assessment": null,
      "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
      "california_health_risk_assessment": null,
      "data_compromised": null,
      "data_contained": null,
      "data_encrypted": null,
      "data_format": null,
      "data_source_ids": [],
      "dc_impact_likely": null,
      "determined_date": 1621110044000,
      "exposure": 0,
      "gdpr_harm_risk": null,
      "gdpr_lawful_data_processing_categories": [],
      "harmstatus_id": 2,
      "impact_likely": null,
      "new_zealand_risk_assessment": null,
      "ny_impact_likely": null,
      "or_impact_likely": null,
      "singapore_risk_assessment": null,
      "wa_impact_likely": null
    },
    "plan_status": "A",
    "playbooks": [
      {
        "display_name": "TImer",
        "playbook_handle": 1
      }
    ],
    "properties": {
      "internal_customizations_field": null,
      "sdlp_incident_id": null,
      "sdlp_incident_status": null,
      "sdlp_incident_url": null,
      "sdlp_policy_group_id": null,
      "sdlp_policy_group_name": null,
      "sdlp_policy_id": null,
      "sdlp_policy_name": null
    },
    "regulator_risk": {},
    "regulators": {
      "ids": []
    },
    "reporter": null,
    "resolution_id": null,
    "resolution_summary": null,
    "sequence_code": null,
    "severity_code": null,
    "start_date": null,
    "state": null,
    "task_changes": {
      "added": [],
      "removed": []
    },
    "tasks": null,
    "timer_field_summarized_incident_data": [],
    "vers": 2,
    "workspace": 1,
    "zip": null
  },
  "inputs": {
    "soar_utils_create_fields": "{\"name\":\"Create Incident\",\"description\":\"Testing\",\"discovered_date\":1621110044000}"
  },
  "metrics": {
    "execution_time_ms": 1705,
    "host": "Christophers-MacBook-Pro-2.local",
    "package": "fn-soar-utils",
    "package_version": "1.0.0",
    "timestamp": "2022-09-15 23:12:33",
    "version": "1.0"
  },
  "raw": "{\"dtm\": {}, \"cm\": {\"unassigneds\": [], \"total\": 0, \"geo_counts\": {}}, \"regulators\": {\"ids\": []}, \"hipaa\": {\"hipaa_adverse\": null, \"hipaa_misused\": null, \"hipaa_acquired\": null, \"hipaa_additional_misuse\": null, \"hipaa_breach\": null, \"hipaa_adverse_comment\": null, \"hipaa_misused_comment\": null, \"hipaa_acquired_comment\": null, \"hipaa_additional_misuse_comment\": null, \"hipaa_breach_comment\": null}, \"tasks\": null, \"artifacts\": null, \"name\": \"Create Incident\", \"description\": \"Testing\", \"phase_id\": 1000, \"inc_training\": false, \"vers\": 2, \"addr\": null, \"city\": null, \"creator\": null, \"creator_principal\": {\"id\": 6, \"type\": \"apikey\", \"name\": \"0228e00e-2c47-43e6-a736-550f104c94ea\", \"display_name\": \"Chris\u0027 Integration Server v43\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": false, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_incident_id\": null, \"sdlp_policy_group_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1621110044000, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1663297953098, \"comments\": null, \"actions\": [{\"id\": 69, \"name\": \"Timer Epoch\", \"enabled\": true}, {\"id\": 70, \"name\": \"Timer in Parallel\", \"enabled\": true}, {\"id\": 72, \"name\": \"Symantec DLP: Get DLP Notes\", \"enabled\": false}, {\"id\": 37, \"name\": \"Example: Archive Incident Slack Channel\", \"enabled\": true}, {\"id\": 42, \"name\": \"Example: Post Incident to Slack\", \"enabled\": true}, {\"id\": 75, \"name\": \"Symantec DLP: Update DLP Incident\", \"enabled\": false}, {\"id\": 78, \"name\": \"Symantec DLP: Upload Binaries as Artifact\", \"enabled\": false}, {\"id\": 79, \"name\": \"Symantec DLP: Write DLP Incident Details to Note\", \"enabled\": false}, {\"id\": 81, \"name\": \"Example: Close Incident\", \"enabled\": true}, {\"id\": 82, \"name\": \"Example: Create Incident\", \"enabled\": true}, {\"id\": 83, \"name\": \"Example: Search Incidents\", \"enabled\": true}, {\"id\": 55, \"name\": \"Example: Get Incident Contact Info\", \"enabled\": true}, {\"id\": 88, \"name\": \"Example: SOAR Utilities Close Incident\", \"enabled\": true}, {\"id\": 89, \"name\": \"Example: SOAR Utilities Create Incident\", \"enabled\": true}, {\"id\": 91, \"name\": \"Example: SOAR Utilities Get Incident Contact Info\", \"enabled\": true}, {\"id\": 63, \"name\": \"Example: Timer Epoch\", \"enabled\": true}, {\"id\": 64, \"name\": \"Example: Timers in Parallel\", \"enabled\": true}, {\"id\": 93, \"name\": \"Example: SOAR Utilities Search Incidents\", \"enabled\": true}], \"playbooks\": [{\"playbook_handle\": 1, \"display_name\": \"TImer\"}], \"timer_field_summarized_incident_data\": [], \"admin_id\": null, \"creator_id\": 6, \"crimestatus_id\": 1, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2114, \"sequence_code\": null, \"discovered_date\": 1621110044000, \"due_date\": null, \"create_date\": 1663297952673, \"owner_id\": 3, \"severity_code\": null, \"plan_status\": \"A\"}",
  "reason": null,
  "success": true,
  "version": "1.0"
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
from json import dumps
create_fields = {"name": playbook.inputs.soar_utils_name,
                "description": playbook.inputs.soar_utils_description.content,
                "discovered_date": playbook.inputs.soar_utils_discovered_date}
                
inputs.soar_utils_create_fields = dumps(create_fields)
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.create_incident_result

if results.get("success"):
  note_text = f"<b>SOAR Utils: Create Incident - Example (PB):</b> Incident <b>{results.content.id}: {results.content.name}</b> successfully created"
else:
  note_text = f"<b>SOAR Utils: Create Incident - Example (PB)</b> Failed: {results.reason}"
incident.addNote(note_text)
```

</p>
</details>

---
## Function - SOAR Utilities: Get Contact Info
Retrieves contact information for the owner and members of an incident or task.
Version 1.1.0 Update: Enhanced to support group ownership by identifying group owners and listing their individual members.


 ![screenshot: fn-soar-utilities-get-contact-info ](./doc/screenshots/fn-soar-utilities-get-contact-info.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `incident_id` | `number` | Yes | `-` | - |
| `task_id` | `number` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "owner": {
    "owner_type": "individual",
    "owner_info": {
      "fname": "admin",
      "lname": "example",
      "title": null,
      "display_name": "admin example",
      "email": "admin@example.com",
      "phone": null,
      "cell": null
    }
  },
  "members": [
    {
      "fname": "admin2",
      "lname": "example",
      "title": null,
      "display_name": "admin2 example",
      "email": "admin2@example.com",
      "phone": null,
      "cell": null
    },
    {
      "fname": "admin3",
      "lname": "example",
      "title": null,
      "display_name": "admin3 example",
      "email": "admin3@example.com",
      "phone": null,
      "cell": null
    }
  ]
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.incident_id = incident.id
inputs.task_id = task.id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.get_incident_contact_info_result

owner_data = results.get('owner', {})
owner_type = owner_data.get('owner_type')

if owner_type == "individual":
    owner_info = owner_data.get('owner_info', {})
    owner_name = owner_info.get('display_name', 'Unknown')
    owner_email = owner_info.get('email', 'N/A')
    owner = f"{owner_name} ({owner_email})"
elif owner_type == "group":
    group_name = owner_data.get('group_name', 'Unnamed Group')
    member_names = ", ".join(owner_data.get('members', []))
    owner = f"{group_name} (Group Owner: {member_names})"

else:
    owner = "Unassigned"

# Format members list
members = "\n".join(
    f"{member.get('display_name', 'Unknown')} ({member.get('email', 'N/A')})"
    for member in results.get('members', [])
)

note_text = (
    f"<b>SOAR Utils: Get Incident Contact Info - Example (PB):</b>\n"
    f"Owner: {owner}\nMembers:\n{members}"
)

incident.addNote(note_text)

```

</p>
</details>

---
## Function - SOAR Utilities: Search Incidents
Search for incidents based on filter criteria. Sorting field are optional

 ![screenshot: fn-soar-utilities-search-incidents ](./doc/screenshots/fn-soar-utilities-search-incidents.png) 

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `soar_utils_filter_conditions` | `text` | No | `[{"field_name":"name", "method":"contains", "value":"sample"}]` | json fields to filter incident records to return |
| `soar_utils_sort_fields` | `text` | No | `-` | json string fields to order result set |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": {
    "data": [
      {
        "addr": null,
        "admin_id": null,
        "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
        "city": null,
        "confirmed": true,
        "country": null,
        "create_date": 1643922148213,
        "creator": {
          "cell": "",
          "display_name": "Admin User",
          "email": "admin@example.com",
          "fname": "Admin",
          "id": 1,
          "is_external": false,
          "is_ldap": false,
          "is_saml": false,
          "lname": "User",
          "locked": false,
          "password_changed": false,
          "phone": "",
          "status": "A",
          "title": "",
          "ui_theme": "verydarkmode"
        },
        "creator_id": 1,
        "creator_principal": {
          "display_name": "Admin User",
          "id": 1,
          "name": "admin@example.com",
          "type": "user"
        },
        "crimestatus_id": 5,
        "data_compromised": null,
        "description": null,
        "discovered_date": 1643922138662,
        "draft": false,
        "due_date": null,
        "employee_involved": null,
        "end_date": null,
        "exposure": 0,
        "exposure_dept_id": null,
        "exposure_individual_name": null,
        "exposure_type_id": 1,
        "exposure_vendor_id": null,
        "gdpr": {
          "gdpr_breach_circumstances": [],
          "gdpr_breach_type": null,
          "gdpr_breach_type_comment": null,
          "gdpr_consequences": null,
          "gdpr_consequences_comment": null,
          "gdpr_final_assessment": null,
          "gdpr_final_assessment_comment": null,
          "gdpr_identification": null,
          "gdpr_identification_comment": null,
          "gdpr_personal_data": null,
          "gdpr_personal_data_comment": null,
          "gdpr_subsequent_notification": null
        },
        "hard_liability": 0,
        "id": 2095,
        "inc_last_modified_date": 1647529122634,
        "inc_start": null,
        "inc_training": false,
        "incident_type_ids": [],
        "is_scenario": false,
        "jurisdiction_name": null,
        "jurisdiction_reg_id": null,
        "members": [],
        "name": "AbuseIPDB",
        "negative_pr_likely": null,
        "nist_attack_vectors": [],
        "org_handle": 201,
        "org_id": 201,
        "owner_id": 1,
        "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "change_workspace": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
        },
        "phase_id": 1000,
        "pii": {
          "alberta_health_risk_assessment": null,
          "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
          "california_health_risk_assessment": null,
          "data_compromised": null,
          "data_contained": null,
          "data_encrypted": null,
          "data_format": null,
          "data_source_ids": [],
          "dc_impact_likely": null,
          "determined_date": 1643922138662,
          "exposure": 0,
          "gdpr_harm_risk": null,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2,
          "impact_likely": null,
          "new_zealand_risk_assessment": null,
          "ny_impact_likely": null,
          "or_impact_likely": null,
          "singapore_risk_assessment": null,
          "wa_impact_likely": null
        },
        "plan_status": "A",
        "properties": {
          "internal_customizations_field": null,
          "sdlp_incident_id": null,
          "sdlp_incident_status": null,
          "sdlp_incident_url": null,
          "sdlp_policy_group_id": null,
          "sdlp_policy_group_name": null,
          "sdlp_policy_id": null,
          "sdlp_policy_name": null
        },
        "regulator_risk": {},
        "reporter": null,
        "resolution_id": null,
        "resolution_summary": null,
        "sequence_code": "E2E5-1",
        "severity_code": 4,
        "start_date": null,
        "state": null,
        "task_changes": {
          "added": [],
          "removed": []
        },
        "vers": 2,
        "workspace": 1,
        "zip": null
      },
      {
        "addr": null,
        "admin_id": null,
        "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
        "city": null,
        "confirmed": true,
        "country": null,
        "create_date": 1645039847583,
        "creator": {
          "cell": "",
          "display_name": "Admin User",
          "email": "admin@example.com",
          "fname": "Admin",
          "id": 1,
          "is_external": false,
          "is_ldap": false,
          "is_saml": false,
          "lname": "User",
          "locked": false,
          "password_changed": false,
          "phone": "",
          "status": "A",
          "title": "",
          "ui_theme": "verydarkmode"
        },
        "creator_id": 1,
        "creator_principal": {
          "display_name": "Admin User",
          "id": 1,
          "name": "admin@example.com",
          "type": "user"
        },
        "crimestatus_id": 5,
        "data_compromised": null,
        "description": null,
        "discovered_date": 1645039833651,
        "draft": false,
        "due_date": null,
        "employee_involved": null,
        "end_date": null,
        "exposure": 0,
        "exposure_dept_id": null,
        "exposure_individual_name": null,
        "exposure_type_id": 1,
        "exposure_vendor_id": null,
        "gdpr": {
          "gdpr_breach_circumstances": [],
          "gdpr_breach_type": null,
          "gdpr_breach_type_comment": null,
          "gdpr_consequences": null,
          "gdpr_consequences_comment": null,
          "gdpr_final_assessment": null,
          "gdpr_final_assessment_comment": null,
          "gdpr_identification": null,
          "gdpr_identification_comment": null,
          "gdpr_personal_data": null,
          "gdpr_personal_data_comment": null,
          "gdpr_subsequent_notification": null
        },
        "hard_liability": 0,
        "id": 2096,
        "inc_last_modified_date": 1647461667230,
        "inc_start": null,
        "inc_training": false,
        "incident_type_ids": [],
        "is_scenario": false,
        "jurisdiction_name": null,
        "jurisdiction_reg_id": null,
        "members": [],
        "name": "GoogleSafeBrowsing",
        "negative_pr_likely": null,
        "nist_attack_vectors": [],
        "org_handle": 201,
        "org_id": 201,
        "owner_id": 1,
        "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "change_workspace": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
        },
        "phase_id": 1000,
        "pii": {
          "alberta_health_risk_assessment": null,
          "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
          "california_health_risk_assessment": null,
          "data_compromised": null,
          "data_contained": null,
          "data_encrypted": null,
          "data_format": null,
          "data_source_ids": [],
          "dc_impact_likely": null,
          "determined_date": 1645039833651,
          "exposure": 0,
          "gdpr_harm_risk": null,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2,
          "impact_likely": null,
          "new_zealand_risk_assessment": null,
          "ny_impact_likely": null,
          "or_impact_likely": null,
          "singapore_risk_assessment": null,
          "wa_impact_likely": null
        },
        "plan_status": "A",
        "properties": {
          "internal_customizations_field": null,
          "sdlp_incident_id": null,
          "sdlp_incident_status": null,
          "sdlp_incident_url": null,
          "sdlp_policy_group_id": null,
          "sdlp_policy_group_name": null,
          "sdlp_policy_id": null,
          "sdlp_policy_name": null
        },
        "regulator_risk": {},
        "reporter": null,
        "resolution_id": null,
        "resolution_summary": null,
        "sequence_code": "E2E5-2",
        "severity_code": 4,
        "start_date": null,
        "state": null,
        "task_changes": {
          "added": [],
          "removed": []
        },
        "vers": 2,
        "workspace": 1,
        "zip": null
      },
      {
        "addr": null,
        "admin_id": null,
        "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
        "city": null,
        "confirmed": true,
        "country": null,
        "create_date": 1646142354974,
        "creator": {
          "cell": "",
          "display_name": "Admin User",
          "email": "admin@example.com",
          "fname": "Admin",
          "id": 1,
          "is_external": false,
          "is_ldap": false,
          "is_saml": false,
          "lname": "User",
          "locked": false,
          "password_changed": false,
          "phone": "",
          "status": "A",
          "title": "",
          "ui_theme": "verydarkmode"
        },
        "creator_id": 1,
        "creator_principal": {
          "display_name": "Admin User",
          "id": 1,
          "name": "admin@example.com",
          "type": "user"
        },
        "crimestatus_id": 5,
        "data_compromised": null,
        "description": null,
        "discovered_date": 1646103998739,
        "draft": false,
        "due_date": null,
        "employee_involved": null,
        "end_date": null,
        "exposure": 0,
        "exposure_dept_id": null,
        "exposure_individual_name": null,
        "exposure_type_id": 1,
        "exposure_vendor_id": null,
        "gdpr": {
          "gdpr_breach_circumstances": [],
          "gdpr_breach_type": null,
          "gdpr_breach_type_comment": null,
          "gdpr_consequences": null,
          "gdpr_consequences_comment": null,
          "gdpr_final_assessment": null,
          "gdpr_final_assessment_comment": null,
          "gdpr_identification": null,
          "gdpr_identification_comment": null,
          "gdpr_personal_data": null,
          "gdpr_personal_data_comment": null,
          "gdpr_subsequent_notification": null
        },
        "hard_liability": 0,
        "id": 2097,
        "inc_last_modified_date": 1647974941312,
        "inc_start": null,
        "inc_training": false,
        "incident_type_ids": [],
        "is_scenario": false,
        "jurisdiction_name": null,
        "jurisdiction_reg_id": null,
        "members": [],
        "name": "PassiveTotal",
        "negative_pr_likely": null,
        "nist_attack_vectors": [],
        "org_handle": 201,
        "org_id": 201,
        "owner_id": 1,
        "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "change_workspace": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
        },
        "phase_id": 1000,
        "pii": {
          "alberta_health_risk_assessment": null,
          "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
          "california_health_risk_assessment": null,
          "data_compromised": null,
          "data_contained": null,
          "data_encrypted": null,
          "data_format": null,
          "data_source_ids": [],
          "dc_impact_likely": null,
          "determined_date": 1646103998739,
          "exposure": 0,
          "gdpr_harm_risk": null,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2,
          "impact_likely": null,
          "new_zealand_risk_assessment": null,
          "ny_impact_likely": null,
          "or_impact_likely": null,
          "singapore_risk_assessment": null,
          "wa_impact_likely": null
        },
        "plan_status": "A",
        "properties": {
          "internal_customizations_field": null,
          "sdlp_incident_id": null,
          "sdlp_incident_status": null,
          "sdlp_incident_url": null,
          "sdlp_policy_group_id": null,
          "sdlp_policy_group_name": null,
          "sdlp_policy_id": null,
          "sdlp_policy_name": null
        },
        "regulator_risk": {},
        "reporter": null,
        "resolution_id": null,
        "resolution_summary": null,
        "sequence_code": "E2E5-3",
        "severity_code": 4,
        "start_date": null,
        "state": null,
        "task_changes": {
          "added": [],
          "removed": []
        },
        "vers": 2,
        "workspace": 1,
        "zip": null
      },
      {
        "addr": null,
        "admin_id": null,
        "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
        "city": null,
        "confirmed": true,
        "country": null,
        "create_date": 1647975111873,
        "creator": {
          "cell": "",
          "display_name": "Admin User",
          "email": "admin@example.com",
          "fname": "Admin",
          "id": 1,
          "is_external": false,
          "is_ldap": false,
          "is_saml": false,
          "lname": "User",
          "locked": false,
          "password_changed": false,
          "phone": "",
          "status": "A",
          "title": "",
          "ui_theme": "verydarkmode"
        },
        "creator_id": 1,
        "creator_principal": {
          "display_name": "Admin User",
          "id": 1,
          "name": "admin@example.com",
          "type": "user"
        },
        "crimestatus_id": 5,
        "data_compromised": null,
        "description": null,
        "discovered_date": 1647975098216,
        "draft": false,
        "due_date": null,
        "employee_involved": null,
        "end_date": null,
        "exposure": 0,
        "exposure_dept_id": null,
        "exposure_individual_name": null,
        "exposure_type_id": 1,
        "exposure_vendor_id": null,
        "gdpr": {
          "gdpr_breach_circumstances": [],
          "gdpr_breach_type": null,
          "gdpr_breach_type_comment": null,
          "gdpr_consequences": null,
          "gdpr_consequences_comment": null,
          "gdpr_final_assessment": null,
          "gdpr_final_assessment_comment": null,
          "gdpr_identification": null,
          "gdpr_identification_comment": null,
          "gdpr_personal_data": null,
          "gdpr_personal_data_comment": null,
          "gdpr_subsequent_notification": null
        },
        "hard_liability": 0,
        "id": 2098,
        "inc_last_modified_date": 1653512178112,
        "inc_start": null,
        "inc_training": false,
        "incident_type_ids": [],
        "is_scenario": false,
        "jurisdiction_name": null,
        "jurisdiction_reg_id": null,
        "members": [],
        "name": "ShadowServer",
        "negative_pr_likely": null,
        "nist_attack_vectors": [],
        "org_handle": 201,
        "org_id": 201,
        "owner_id": 1,
        "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "change_workspace": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
        },
        "phase_id": 1000,
        "pii": {
          "alberta_health_risk_assessment": null,
          "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
          "california_health_risk_assessment": null,
          "data_compromised": null,
          "data_contained": null,
          "data_encrypted": null,
          "data_format": null,
          "data_source_ids": [],
          "dc_impact_likely": null,
          "determined_date": 1647975098216,
          "exposure": 0,
          "gdpr_harm_risk": null,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2,
          "impact_likely": null,
          "new_zealand_risk_assessment": null,
          "ny_impact_likely": null,
          "or_impact_likely": null,
          "singapore_risk_assessment": null,
          "wa_impact_likely": null
        },
        "plan_status": "A",
        "properties": {
          "internal_customizations_field": null,
          "sdlp_incident_id": null,
          "sdlp_incident_status": null,
          "sdlp_incident_url": null,
          "sdlp_policy_group_id": null,
          "sdlp_policy_group_name": null,
          "sdlp_policy_id": null,
          "sdlp_policy_name": null
        },
        "regulator_risk": {},
        "reporter": null,
        "resolution_id": null,
        "resolution_summary": null,
        "sequence_code": "E2E5-4",
        "severity_code": 4,
        "start_date": null,
        "state": null,
        "task_changes": {
          "added": [],
          "removed": []
        },
        "vers": 2,
        "workspace": 1,
        "zip": null
      },
      {
        "addr": null,
        "admin_id": null,
        "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
        "city": null,
        "confirmed": true,
        "country": null,
        "create_date": 1648839806477,
        "creator": {
          "cell": "",
          "display_name": "Admin User",
          "email": "admin@example.com",
          "fname": "Admin",
          "id": 1,
          "is_external": false,
          "is_ldap": false,
          "is_saml": false,
          "lname": "User",
          "locked": false,
          "password_changed": false,
          "phone": "",
          "status": "A",
          "title": "",
          "ui_theme": "verydarkmode"
        },
        "creator_id": 1,
        "creator_principal": {
          "display_name": "Admin User",
          "id": 1,
          "name": "admin@example.com",
          "type": "user"
        },
        "crimestatus_id": 5,
        "data_compromised": null,
        "description": null,
        "discovered_date": 1648839797719,
        "draft": false,
        "due_date": null,
        "employee_involved": null,
        "end_date": null,
        "exposure": 0,
        "exposure_dept_id": null,
        "exposure_individual_name": null,
        "exposure_type_id": 1,
        "exposure_vendor_id": null,
        "gdpr": {
          "gdpr_breach_circumstances": [],
          "gdpr_breach_type": null,
          "gdpr_breach_type_comment": null,
          "gdpr_consequences": null,
          "gdpr_consequences_comment": null,
          "gdpr_final_assessment": null,
          "gdpr_final_assessment_comment": null,
          "gdpr_identification": null,
          "gdpr_identification_comment": null,
          "gdpr_personal_data": null,
          "gdpr_personal_data_comment": null,
          "gdpr_subsequent_notification": null
        },
        "hard_liability": 0,
        "id": 2099,
        "inc_last_modified_date": 1649700668706,
        "inc_start": null,
        "inc_training": false,
        "incident_type_ids": [],
        "is_scenario": false,
        "jurisdiction_name": null,
        "jurisdiction_reg_id": null,
        "members": [],
        "name": "Yeti",
        "negative_pr_likely": null,
        "nist_attack_vectors": [],
        "org_handle": 201,
        "org_id": 201,
        "owner_id": 1,
        "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "change_workspace": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
        },
        "phase_id": 1000,
        "pii": {
          "alberta_health_risk_assessment": null,
          "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
          "california_health_risk_assessment": null,
          "data_compromised": null,
          "data_contained": null,
          "data_encrypted": null,
          "data_format": null,
          "data_source_ids": [],
          "dc_impact_likely": null,
          "determined_date": 1648839797719,
          "exposure": 0,
          "gdpr_harm_risk": null,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2,
          "impact_likely": null,
          "new_zealand_risk_assessment": null,
          "ny_impact_likely": null,
          "or_impact_likely": null,
          "singapore_risk_assessment": null,
          "wa_impact_likely": null
        },
        "plan_status": "A",
        "properties": {
          "internal_customizations_field": null,
          "sdlp_incident_id": null,
          "sdlp_incident_status": null,
          "sdlp_incident_url": null,
          "sdlp_policy_group_id": null,
          "sdlp_policy_group_name": null,
          "sdlp_policy_id": null,
          "sdlp_policy_name": null
        },
        "regulator_risk": {},
        "reporter": null,
        "resolution_id": null,
        "resolution_summary": null,
        "sequence_code": "E2E5-5",
        "severity_code": 4,
        "start_date": null,
        "state": null,
        "task_changes": {
          "added": [],
          "removed": []
        },
        "vers": 2,
        "workspace": 1,
        "zip": null
      },
      {
        "addr": null,
        "admin_id": null,
        "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
        "city": null,
        "confirmed": true,
        "country": null,
        "create_date": 1649858943997,
        "creator": {
          "cell": "",
          "display_name": "Admin User",
          "email": "admin@example.com",
          "fname": "Admin",
          "id": 1,
          "is_external": false,
          "is_ldap": false,
          "is_saml": false,
          "lname": "User",
          "locked": false,
          "password_changed": false,
          "phone": "",
          "status": "A",
          "title": "",
          "ui_theme": "verydarkmode"
        },
        "creator_id": 1,
        "creator_principal": {
          "display_name": "Admin User",
          "id": 1,
          "name": "admin@example.com",
          "type": "user"
        },
        "crimestatus_id": 5,
        "data_compromised": null,
        "description": null,
        "discovered_date": 1649858935196,
        "draft": false,
        "due_date": null,
        "employee_involved": null,
        "end_date": null,
        "exposure": 0,
        "exposure_dept_id": null,
        "exposure_individual_name": null,
        "exposure_type_id": 1,
        "exposure_vendor_id": null,
        "gdpr": {
          "gdpr_breach_circumstances": [],
          "gdpr_breach_type": null,
          "gdpr_breach_type_comment": null,
          "gdpr_consequences": null,
          "gdpr_consequences_comment": null,
          "gdpr_final_assessment": null,
          "gdpr_final_assessment_comment": null,
          "gdpr_identification": null,
          "gdpr_identification_comment": null,
          "gdpr_personal_data": null,
          "gdpr_personal_data_comment": null,
          "gdpr_subsequent_notification": null
        },
        "hard_liability": 0,
        "id": 2100,
        "inc_last_modified_date": 1651092229697,
        "inc_start": null,
        "inc_training": false,
        "incident_type_ids": [],
        "is_scenario": false,
        "jurisdiction_name": null,
        "jurisdiction_reg_id": null,
        "members": [],
        "name": "hibp",
        "negative_pr_likely": null,
        "nist_attack_vectors": [],
        "org_handle": 201,
        "org_id": 201,
        "owner_id": 1,
        "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "change_workspace": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
        },
        "phase_id": 1000,
        "pii": {
          "alberta_health_risk_assessment": null,
          "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
          "california_health_risk_assessment": null,
          "data_compromised": null,
          "data_contained": null,
          "data_encrypted": null,
          "data_format": null,
          "data_source_ids": [],
          "dc_impact_likely": null,
          "determined_date": 1649858935196,
          "exposure": 0,
          "gdpr_harm_risk": null,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2,
          "impact_likely": null,
          "new_zealand_risk_assessment": null,
          "ny_impact_likely": null,
          "or_impact_likely": null,
          "singapore_risk_assessment": null,
          "wa_impact_likely": null
        },
        "plan_status": "A",
        "properties": {
          "internal_customizations_field": null,
          "sdlp_incident_id": null,
          "sdlp_incident_status": null,
          "sdlp_incident_url": null,
          "sdlp_policy_group_id": null,
          "sdlp_policy_group_name": null,
          "sdlp_policy_id": null,
          "sdlp_policy_name": null
        },
        "regulator_risk": {},
        "reporter": null,
        "resolution_id": null,
        "resolution_summary": null,
        "sequence_code": "E2E5-6",
        "severity_code": 4,
        "start_date": null,
        "state": null,
        "task_changes": {
          "added": [],
          "removed": []
        },
        "vers": 2,
        "workspace": 1,
        "zip": null
      },
      {
        "addr": null,
        "admin_id": null,
        "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
        "city": null,
        "confirmed": true,
        "country": null,
        "create_date": 1651000737927,
        "creator": {
          "cell": "",
          "display_name": "Admin User",
          "email": "admin@example.com",
          "fname": "Admin",
          "id": 1,
          "is_external": false,
          "is_ldap": false,
          "is_saml": false,
          "lname": "User",
          "locked": false,
          "password_changed": false,
          "phone": "",
          "status": "A",
          "title": "",
          "ui_theme": "verydarkmode"
        },
        "creator_id": 1,
        "creator_principal": {
          "display_name": "Admin User",
          "id": 1,
          "name": "admin@example.com",
          "type": "user"
        },
        "crimestatus_id": 5,
        "data_compromised": null,
        "description": null,
        "discovered_date": 1651000728764,
        "draft": false,
        "due_date": null,
        "employee_involved": null,
        "end_date": null,
        "exposure": 0,
        "exposure_dept_id": null,
        "exposure_individual_name": null,
        "exposure_type_id": 1,
        "exposure_vendor_id": null,
        "gdpr": {
          "gdpr_breach_circumstances": [],
          "gdpr_breach_type": null,
          "gdpr_breach_type_comment": null,
          "gdpr_consequences": null,
          "gdpr_consequences_comment": null,
          "gdpr_final_assessment": null,
          "gdpr_final_assessment_comment": null,
          "gdpr_identification": null,
          "gdpr_identification_comment": null,
          "gdpr_personal_data": null,
          "gdpr_personal_data_comment": null,
          "gdpr_subsequent_notification": null
        },
        "hard_liability": 0,
        "id": 2101,
        "inc_last_modified_date": 1653580063528,
        "inc_start": null,
        "inc_training": false,
        "incident_type_ids": [],
        "is_scenario": false,
        "jurisdiction_name": null,
        "jurisdiction_reg_id": null,
        "members": [],
        "name": "VirusTotal",
        "negative_pr_likely": null,
        "nist_attack_vectors": [],
        "org_handle": 201,
        "org_id": 201,
        "owner_id": 1,
        "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "change_workspace": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
        },
        "phase_id": 1000,
        "pii": {
          "alberta_health_risk_assessment": null,
          "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
          "california_health_risk_assessment": null,
          "data_compromised": null,
          "data_contained": null,
          "data_encrypted": null,
          "data_format": null,
          "data_source_ids": [],
          "dc_impact_likely": null,
          "determined_date": 1651000728764,
          "exposure": 0,
          "gdpr_harm_risk": null,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2,
          "impact_likely": null,
          "new_zealand_risk_assessment": null,
          "ny_impact_likely": null,
          "or_impact_likely": null,
          "singapore_risk_assessment": null,
          "wa_impact_likely": null
        },
        "plan_status": "A",
        "properties": {
          "internal_customizations_field": null,
          "sdlp_incident_id": null,
          "sdlp_incident_status": null,
          "sdlp_incident_url": null,
          "sdlp_policy_group_id": null,
          "sdlp_policy_group_name": null,
          "sdlp_policy_id": null,
          "sdlp_policy_name": null
        },
        "regulator_risk": {},
        "reporter": null,
        "resolution_id": null,
        "resolution_summary": null,
        "sequence_code": "E2E5-7",
        "severity_code": 4,
        "start_date": null,
        "state": null,
        "task_changes": {
          "added": [],
          "removed": []
        },
        "vers": 4,
        "workspace": 1,
        "zip": null
      },
      {
        "addr": null,
        "admin_id": null,
        "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
        "city": null,
        "confirmed": true,
        "country": null,
        "create_date": 1651264273600,
        "creator": {
          "cell": "",
          "display_name": "Admin User",
          "email": "admin@example.com",
          "fname": "Admin",
          "id": 1,
          "is_external": false,
          "is_ldap": false,
          "is_saml": false,
          "lname": "User",
          "locked": false,
          "password_changed": false,
          "phone": "",
          "status": "A",
          "title": "",
          "ui_theme": "verydarkmode"
        },
        "creator_id": 1,
        "creator_principal": {
          "display_name": "Admin User",
          "id": 1,
          "name": "admin@example.com",
          "type": "user"
        },
        "crimestatus_id": 5,
        "data_compromised": null,
        "description": null,
        "discovered_date": 1651264262077,
        "draft": false,
        "due_date": null,
        "employee_involved": null,
        "end_date": null,
        "exposure": 0,
        "exposure_dept_id": null,
        "exposure_individual_name": null,
        "exposure_type_id": 1,
        "exposure_vendor_id": null,
        "gdpr": {
          "gdpr_breach_circumstances": [],
          "gdpr_breach_type": null,
          "gdpr_breach_type_comment": null,
          "gdpr_consequences": null,
          "gdpr_consequences_comment": null,
          "gdpr_final_assessment": null,
          "gdpr_final_assessment_comment": null,
          "gdpr_identification": null,
          "gdpr_identification_comment": null,
          "gdpr_personal_data": null,
          "gdpr_personal_data_comment": null,
          "gdpr_subsequent_notification": null
        },
        "hard_liability": 0,
        "id": 2102,
        "inc_last_modified_date": 1652814527143,
        "inc_start": null,
        "inc_training": false,
        "incident_type_ids": [],
        "is_scenario": false,
        "jurisdiction_name": null,
        "jurisdiction_reg_id": null,
        "members": [],
        "name": "URLScan.io",
        "negative_pr_likely": null,
        "nist_attack_vectors": [],
        "org_handle": 201,
        "org_id": 201,
        "owner_id": 1,
        "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "change_workspace": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
        },
        "phase_id": 1000,
        "pii": {
          "alberta_health_risk_assessment": null,
          "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
          "california_health_risk_assessment": null,
          "data_compromised": null,
          "data_contained": null,
          "data_encrypted": null,
          "data_format": null,
          "data_source_ids": [],
          "dc_impact_likely": null,
          "determined_date": 1651264262077,
          "exposure": 0,
          "gdpr_harm_risk": null,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2,
          "impact_likely": null,
          "new_zealand_risk_assessment": null,
          "ny_impact_likely": null,
          "or_impact_likely": null,
          "singapore_risk_assessment": null,
          "wa_impact_likely": null
        },
        "plan_status": "A",
        "properties": {
          "internal_customizations_field": null,
          "sdlp_incident_id": null,
          "sdlp_incident_status": null,
          "sdlp_incident_url": null,
          "sdlp_policy_group_id": null,
          "sdlp_policy_group_name": null,
          "sdlp_policy_id": null,
          "sdlp_policy_name": null
        },
        "regulator_risk": {},
        "reporter": null,
        "resolution_id": null,
        "resolution_summary": null,
        "sequence_code": "E2E5-8",
        "severity_code": 4,
        "start_date": null,
        "state": null,
        "task_changes": {
          "added": [],
          "removed": []
        },
        "vers": 74,
        "workspace": 1,
        "zip": null
      },
      {
        "addr": null,
        "admin_id": null,
        "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
        "city": null,
        "confirmed": true,
        "country": null,
        "create_date": 1655912245009,
        "creator": {
          "cell": "",
          "display_name": "Admin User",
          "email": "admin@example.com",
          "fname": "Admin",
          "id": 1,
          "is_external": false,
          "is_ldap": false,
          "is_saml": false,
          "lname": "User",
          "locked": false,
          "password_changed": false,
          "phone": "",
          "status": "A",
          "title": "",
          "ui_theme": "verydarkmode"
        },
        "creator_id": 1,
        "creator_principal": {
          "display_name": "Admin User",
          "id": 1,
          "name": "admin@example.com",
          "type": "user"
        },
        "crimestatus_id": 5,
        "data_compromised": null,
        "description": null,
        "discovered_date": 1655912228120,
        "draft": false,
        "due_date": null,
        "employee_involved": null,
        "end_date": null,
        "exposure": 0,
        "exposure_dept_id": null,
        "exposure_individual_name": null,
        "exposure_type_id": 1,
        "exposure_vendor_id": null,
        "gdpr": {
          "gdpr_breach_circumstances": [],
          "gdpr_breach_type": null,
          "gdpr_breach_type_comment": null,
          "gdpr_consequences": null,
          "gdpr_consequences_comment": null,
          "gdpr_final_assessment": null,
          "gdpr_final_assessment_comment": null,
          "gdpr_identification": null,
          "gdpr_identification_comment": null,
          "gdpr_personal_data": null,
          "gdpr_personal_data_comment": null,
          "gdpr_subsequent_notification": null
        },
        "hard_liability": 0,
        "id": 2103,
        "inc_last_modified_date": 1655924984252,
        "inc_start": null,
        "inc_training": false,
        "incident_type_ids": [],
        "is_scenario": false,
        "jurisdiction_name": null,
        "jurisdiction_reg_id": null,
        "members": [],
        "name": "Google Cloud DLP",
        "negative_pr_likely": null,
        "nist_attack_vectors": [],
        "org_handle": 201,
        "org_id": 201,
        "owner_id": 1,
        "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "change_workspace": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
        },
        "phase_id": 1000,
        "pii": {
          "alberta_health_risk_assessment": null,
          "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
          "california_health_risk_assessment": null,
          "data_compromised": null,
          "data_contained": null,
          "data_encrypted": null,
          "data_format": null,
          "data_source_ids": [],
          "dc_impact_likely": null,
          "determined_date": 1655912228120,
          "exposure": 0,
          "gdpr_harm_risk": null,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2,
          "impact_likely": null,
          "new_zealand_risk_assessment": null,
          "ny_impact_likely": null,
          "or_impact_likely": null,
          "singapore_risk_assessment": null,
          "wa_impact_likely": null
        },
        "plan_status": "A",
        "properties": {
          "internal_customizations_field": null,
          "sdlp_incident_id": null,
          "sdlp_incident_status": null,
          "sdlp_incident_url": null,
          "sdlp_policy_group_id": null,
          "sdlp_policy_group_name": null,
          "sdlp_policy_id": null,
          "sdlp_policy_name": null
        },
        "regulator_risk": {},
        "reporter": null,
        "resolution_id": null,
        "resolution_summary": null,
        "sequence_code": "E2E5-9",
        "severity_code": 4,
        "start_date": null,
        "state": null,
        "task_changes": {
          "added": [],
          "removed": []
        },
        "vers": 12,
        "workspace": 1,
        "zip": null
      },
      {
        "addr": null,
        "admin_id": null,
        "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
        "city": null,
        "confirmed": true,
        "country": null,
        "create_date": 1656527541659,
        "creator": {
          "cell": "",
          "display_name": "Admin User",
          "email": "admin@example.com",
          "fname": "Admin",
          "id": 1,
          "is_external": false,
          "is_ldap": false,
          "is_saml": false,
          "lname": "User",
          "locked": false,
          "password_changed": false,
          "phone": "",
          "status": "A",
          "title": "",
          "ui_theme": "verydarkmode"
        },
        "creator_id": 1,
        "creator_principal": {
          "display_name": "Admin User",
          "id": 1,
          "name": "admin@example.com",
          "type": "user"
        },
        "crimestatus_id": 5,
        "data_compromised": null,
        "description": null,
        "discovered_date": 1656527528505,
        "draft": false,
        "due_date": null,
        "employee_involved": null,
        "end_date": null,
        "exposure": 0,
        "exposure_dept_id": null,
        "exposure_individual_name": null,
        "exposure_type_id": 1,
        "exposure_vendor_id": null,
        "gdpr": {
          "gdpr_breach_circumstances": [],
          "gdpr_breach_type": null,
          "gdpr_breach_type_comment": null,
          "gdpr_consequences": null,
          "gdpr_consequences_comment": null,
          "gdpr_final_assessment": null,
          "gdpr_final_assessment_comment": null,
          "gdpr_identification": null,
          "gdpr_identification_comment": null,
          "gdpr_personal_data": null,
          "gdpr_personal_data_comment": null,
          "gdpr_subsequent_notification": null
        },
        "hard_liability": 0,
        "id": 2104,
        "inc_last_modified_date": 1661269393325,
        "inc_start": null,
        "inc_training": false,
        "incident_type_ids": [],
        "is_scenario": false,
        "jurisdiction_name": null,
        "jurisdiction_reg_id": null,
        "members": [],
        "name": "Slack",
        "negative_pr_likely": null,
        "nist_attack_vectors": [],
        "org_handle": 201,
        "org_id": 201,
        "owner_id": 1,
        "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "change_workspace": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
        },
        "phase_id": 1000,
        "pii": {
          "alberta_health_risk_assessment": null,
          "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
          "california_health_risk_assessment": null,
          "data_compromised": null,
          "data_contained": null,
          "data_encrypted": null,
          "data_format": null,
          "data_source_ids": [],
          "dc_impact_likely": null,
          "determined_date": 1656527528505,
          "exposure": 0,
          "gdpr_harm_risk": null,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2,
          "impact_likely": null,
          "new_zealand_risk_assessment": null,
          "ny_impact_likely": null,
          "or_impact_likely": null,
          "singapore_risk_assessment": null,
          "wa_impact_likely": null
        },
        "plan_status": "A",
        "properties": {
          "internal_customizations_field": null,
          "sdlp_incident_id": null,
          "sdlp_incident_status": null,
          "sdlp_incident_url": null,
          "sdlp_policy_group_id": null,
          "sdlp_policy_group_name": null,
          "sdlp_policy_id": null,
          "sdlp_policy_name": null
        },
        "regulator_risk": {},
        "reporter": null,
        "resolution_id": null,
        "resolution_summary": null,
        "sequence_code": "E2E5-10",
        "severity_code": 4,
        "start_date": null,
        "state": null,
        "task_changes": {
          "added": [],
          "removed": []
        },
        "vers": 16,
        "workspace": 1,
        "zip": null
      },
      {
        "addr": null,
        "admin_id": null,
        "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
        "city": null,
        "confirmed": true,
        "country": null,
        "create_date": 1660155971260,
        "creator": {
          "cell": "",
          "display_name": "Admin User",
          "email": "admin@example.com",
          "fname": "Admin",
          "id": 1,
          "is_external": false,
          "is_ldap": false,
          "is_saml": false,
          "lname": "User",
          "locked": false,
          "password_changed": false,
          "phone": "",
          "status": "A",
          "title": "",
          "ui_theme": "verydarkmode"
        },
        "creator_id": 1,
        "creator_principal": {
          "display_name": "Admin User",
          "id": 1,
          "name": "admin@example.com",
          "type": "user"
        },
        "crimestatus_id": 5,
        "data_compromised": null,
        "description": null,
        "discovered_date": 1660155959409,
        "draft": false,
        "due_date": null,
        "employee_involved": null,
        "end_date": null,
        "exposure": 0,
        "exposure_dept_id": null,
        "exposure_individual_name": null,
        "exposure_type_id": 1,
        "exposure_vendor_id": null,
        "gdpr": {
          "gdpr_breach_circumstances": [],
          "gdpr_breach_type": null,
          "gdpr_breach_type_comment": null,
          "gdpr_consequences": null,
          "gdpr_consequences_comment": null,
          "gdpr_final_assessment": null,
          "gdpr_final_assessment_comment": null,
          "gdpr_identification": null,
          "gdpr_identification_comment": null,
          "gdpr_personal_data": null,
          "gdpr_personal_data_comment": null,
          "gdpr_subsequent_notification": null
        },
        "hard_liability": 0,
        "id": 2107,
        "inc_last_modified_date": 1661281207911,
        "inc_start": null,
        "inc_training": false,
        "incident_type_ids": [],
        "is_scenario": false,
        "jurisdiction_name": null,
        "jurisdiction_reg_id": null,
        "members": [],
        "name": "New Slack",
        "negative_pr_likely": null,
        "nist_attack_vectors": [],
        "org_handle": 201,
        "org_id": 201,
        "owner_id": 1,
        "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "change_workspace": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
        },
        "phase_id": 1000,
        "pii": {
          "alberta_health_risk_assessment": null,
          "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
          "california_health_risk_assessment": null,
          "data_compromised": null,
          "data_contained": null,
          "data_encrypted": null,
          "data_format": null,
          "data_source_ids": [],
          "dc_impact_likely": null,
          "determined_date": 1660155959409,
          "exposure": 0,
          "gdpr_harm_risk": null,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2,
          "impact_likely": null,
          "new_zealand_risk_assessment": null,
          "ny_impact_likely": null,
          "or_impact_likely": null,
          "singapore_risk_assessment": null,
          "wa_impact_likely": null
        },
        "plan_status": "A",
        "properties": {
          "internal_customizations_field": null,
          "sdlp_incident_id": null,
          "sdlp_incident_status": null,
          "sdlp_incident_url": null,
          "sdlp_policy_group_id": null,
          "sdlp_policy_group_name": null,
          "sdlp_policy_id": null,
          "sdlp_policy_name": null
        },
        "regulator_risk": {},
        "reporter": null,
        "resolution_id": null,
        "resolution_summary": null,
        "sequence_code": "E2E5-13",
        "severity_code": 4,
        "start_date": null,
        "state": null,
        "task_changes": {
          "added": [],
          "removed": []
        },
        "vers": 4,
        "workspace": 1,
        "zip": null
      },
      {
        "addr": null,
        "admin_id": null,
        "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
        "city": null,
        "confirmed": true,
        "country": null,
        "create_date": 1660245680733,
        "creator": {
          "cell": "",
          "display_name": "Admin User",
          "email": "admin@example.com",
          "fname": "Admin",
          "id": 1,
          "is_external": false,
          "is_ldap": false,
          "is_saml": false,
          "lname": "User",
          "locked": false,
          "password_changed": false,
          "phone": "",
          "status": "A",
          "title": "",
          "ui_theme": "verydarkmode"
        },
        "creator_id": 1,
        "creator_principal": {
          "display_name": "Admin User",
          "id": 1,
          "name": "admin@example.com",
          "type": "user"
        },
        "crimestatus_id": 5,
        "data_compromised": null,
        "description": null,
        "discovered_date": 1660245674318,
        "draft": false,
        "due_date": null,
        "employee_involved": null,
        "end_date": null,
        "exposure": 0,
        "exposure_dept_id": null,
        "exposure_individual_name": null,
        "exposure_type_id": 1,
        "exposure_vendor_id": null,
        "gdpr": {
          "gdpr_breach_circumstances": [],
          "gdpr_breach_type": null,
          "gdpr_breach_type_comment": null,
          "gdpr_consequences": null,
          "gdpr_consequences_comment": null,
          "gdpr_final_assessment": null,
          "gdpr_final_assessment_comment": null,
          "gdpr_identification": null,
          "gdpr_identification_comment": null,
          "gdpr_personal_data": null,
          "gdpr_personal_data_comment": null,
          "gdpr_subsequent_notification": null
        },
        "hard_liability": 0,
        "id": 2108,
        "inc_last_modified_date": 1661280682539,
        "inc_start": null,
        "inc_training": false,
        "incident_type_ids": [],
        "is_scenario": false,
        "jurisdiction_name": null,
        "jurisdiction_reg_id": null,
        "members": [],
        "name": "Slack2",
        "negative_pr_likely": null,
        "nist_attack_vectors": [],
        "org_handle": 201,
        "org_id": 201,
        "owner_id": 1,
        "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "change_workspace": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
        },
        "phase_id": 1000,
        "pii": {
          "alberta_health_risk_assessment": null,
          "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
          "california_health_risk_assessment": null,
          "data_compromised": null,
          "data_contained": null,
          "data_encrypted": null,
          "data_format": null,
          "data_source_ids": [],
          "dc_impact_likely": null,
          "determined_date": 1660245674318,
          "exposure": 0,
          "gdpr_harm_risk": null,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2,
          "impact_likely": null,
          "new_zealand_risk_assessment": null,
          "ny_impact_likely": null,
          "or_impact_likely": null,
          "singapore_risk_assessment": null,
          "wa_impact_likely": null
        },
        "plan_status": "A",
        "properties": {
          "internal_customizations_field": null,
          "sdlp_incident_id": null,
          "sdlp_incident_status": null,
          "sdlp_incident_url": null,
          "sdlp_policy_group_id": null,
          "sdlp_policy_group_name": null,
          "sdlp_policy_id": null,
          "sdlp_policy_name": null
        },
        "regulator_risk": {},
        "reporter": null,
        "resolution_id": null,
        "resolution_summary": null,
        "sequence_code": "E2E5-14",
        "severity_code": 4,
        "start_date": null,
        "state": null,
        "task_changes": {
          "added": [],
          "removed": []
        },
        "vers": 6,
        "workspace": 1,
        "zip": null
      },
      {
        "addr": null,
        "admin_id": null,
        "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
        "city": null,
        "confirmed": true,
        "country": null,
        "create_date": 1661346206429,
        "creator": {
          "cell": "",
          "display_name": "Admin User",
          "email": "admin@example.com",
          "fname": "Admin",
          "id": 1,
          "is_external": false,
          "is_ldap": false,
          "is_saml": false,
          "lname": "User",
          "locked": false,
          "password_changed": false,
          "phone": "",
          "status": "A",
          "title": "",
          "ui_theme": "verydarkmode"
        },
        "creator_id": 1,
        "creator_principal": {
          "display_name": "Admin User",
          "id": 1,
          "name": "admin@example.com",
          "type": "user"
        },
        "crimestatus_id": 5,
        "data_compromised": null,
        "description": null,
        "discovered_date": 1661346194202,
        "draft": false,
        "due_date": null,
        "employee_involved": null,
        "end_date": null,
        "exposure": 0,
        "exposure_dept_id": null,
        "exposure_individual_name": null,
        "exposure_type_id": 1,
        "exposure_vendor_id": null,
        "gdpr": {
          "gdpr_breach_circumstances": [],
          "gdpr_breach_type": null,
          "gdpr_breach_type_comment": null,
          "gdpr_consequences": null,
          "gdpr_consequences_comment": null,
          "gdpr_final_assessment": null,
          "gdpr_final_assessment_comment": null,
          "gdpr_identification": null,
          "gdpr_identification_comment": null,
          "gdpr_personal_data": null,
          "gdpr_personal_data_comment": null,
          "gdpr_subsequent_notification": null
        },
        "hard_liability": 0,
        "id": 2110,
        "inc_last_modified_date": 1661447571753,
        "inc_start": null,
        "inc_training": false,
        "incident_type_ids": [],
        "is_scenario": false,
        "jurisdiction_name": null,
        "jurisdiction_reg_id": null,
        "members": [],
        "name": "debug incident",
        "negative_pr_likely": null,
        "nist_attack_vectors": [],
        "org_handle": 201,
        "org_id": 201,
        "owner_id": 1,
        "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "change_workspace": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
        },
        "phase_id": 1000,
        "pii": {
          "alberta_health_risk_assessment": null,
          "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
          "california_health_risk_assessment": null,
          "data_compromised": null,
          "data_contained": null,
          "data_encrypted": null,
          "data_format": null,
          "data_source_ids": [],
          "dc_impact_likely": null,
          "determined_date": 1661346194202,
          "exposure": 0,
          "gdpr_harm_risk": null,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2,
          "impact_likely": null,
          "new_zealand_risk_assessment": null,
          "ny_impact_likely": null,
          "or_impact_likely": null,
          "singapore_risk_assessment": null,
          "wa_impact_likely": null
        },
        "plan_status": "A",
        "properties": {
          "internal_customizations_field": null,
          "sdlp_incident_id": null,
          "sdlp_incident_status": null,
          "sdlp_incident_url": null,
          "sdlp_policy_group_id": null,
          "sdlp_policy_group_name": null,
          "sdlp_policy_id": null,
          "sdlp_policy_name": null
        },
        "regulator_risk": {},
        "reporter": null,
        "resolution_id": null,
        "resolution_summary": null,
        "sequence_code": "E2E5-16",
        "severity_code": 4,
        "start_date": null,
        "state": null,
        "task_changes": {
          "added": [],
          "removed": []
        },
        "vers": 13,
        "workspace": 1,
        "zip": null
      },
      {
        "addr": null,
        "admin_id": null,
        "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
        "city": null,
        "confirmed": true,
        "country": null,
        "create_date": 1661800169751,
        "creator": {
          "cell": "",
          "display_name": "Admin User",
          "email": "admin@example.com",
          "fname": "Admin",
          "id": 1,
          "is_external": false,
          "is_ldap": false,
          "is_saml": false,
          "lname": "User",
          "locked": false,
          "password_changed": false,
          "phone": "",
          "status": "A",
          "title": "",
          "ui_theme": "verydarkmode"
        },
        "creator_id": 1,
        "creator_principal": {
          "display_name": "Admin User",
          "id": 1,
          "name": "admin@example.com",
          "type": "user"
        },
        "crimestatus_id": 5,
        "data_compromised": null,
        "description": null,
        "discovered_date": 1661800148708,
        "draft": false,
        "due_date": null,
        "employee_involved": null,
        "end_date": null,
        "exposure": 0,
        "exposure_dept_id": null,
        "exposure_individual_name": null,
        "exposure_type_id": 1,
        "exposure_vendor_id": null,
        "gdpr": {
          "gdpr_breach_circumstances": [],
          "gdpr_breach_type": null,
          "gdpr_breach_type_comment": null,
          "gdpr_consequences": null,
          "gdpr_consequences_comment": null,
          "gdpr_final_assessment": null,
          "gdpr_final_assessment_comment": null,
          "gdpr_identification": null,
          "gdpr_identification_comment": null,
          "gdpr_personal_data": null,
          "gdpr_personal_data_comment": null,
          "gdpr_subsequent_notification": null
        },
        "hard_liability": 0,
        "id": 2111,
        "inc_last_modified_date": 1662747629777,
        "inc_start": null,
        "inc_training": false,
        "incident_type_ids": [],
        "is_scenario": false,
        "jurisdiction_name": null,
        "jurisdiction_reg_id": null,
        "members": [],
        "name": "Timer",
        "negative_pr_likely": null,
        "nist_attack_vectors": [],
        "org_handle": 201,
        "org_id": 201,
        "owner_id": 1,
        "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "change_workspace": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
        },
        "phase_id": 1000,
        "pii": {
          "alberta_health_risk_assessment": null,
          "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
          "california_health_risk_assessment": null,
          "data_compromised": null,
          "data_contained": null,
          "data_encrypted": null,
          "data_format": null,
          "data_source_ids": [],
          "dc_impact_likely": null,
          "determined_date": 1661800148708,
          "exposure": 0,
          "gdpr_harm_risk": null,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2,
          "impact_likely": null,
          "new_zealand_risk_assessment": null,
          "ny_impact_likely": null,
          "or_impact_likely": null,
          "singapore_risk_assessment": null,
          "wa_impact_likely": null
        },
        "plan_status": "A",
        "properties": {
          "internal_customizations_field": null,
          "sdlp_incident_id": null,
          "sdlp_incident_status": null,
          "sdlp_incident_url": null,
          "sdlp_policy_group_id": null,
          "sdlp_policy_group_name": null,
          "sdlp_policy_id": null,
          "sdlp_policy_name": null
        },
        "regulator_risk": {},
        "reporter": null,
        "resolution_id": null,
        "resolution_summary": null,
        "sequence_code": "E2E5-17",
        "severity_code": 4,
        "start_date": null,
        "state": null,
        "task_changes": {
          "added": [],
          "removed": []
        },
        "vers": 2,
        "workspace": 1,
        "zip": null
      },
      {
        "addr": null,
        "admin_id": null,
        "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
        "city": null,
        "confirmed": true,
        "country": null,
        "create_date": 1663093296645,
        "creator": {
          "cell": "",
          "display_name": "Admin User",
          "email": "admin@example.com",
          "fname": "Admin",
          "id": 1,
          "is_external": false,
          "is_ldap": false,
          "is_saml": false,
          "lname": "User",
          "locked": false,
          "password_changed": false,
          "phone": "",
          "status": "A",
          "title": "",
          "ui_theme": "verydarkmode"
        },
        "creator_id": 1,
        "creator_principal": {
          "display_name": "Admin User",
          "id": 1,
          "name": "admin@example.com",
          "type": "user"
        },
        "crimestatus_id": 5,
        "data_compromised": null,
        "description": null,
        "discovered_date": 1663093285999,
        "draft": false,
        "due_date": null,
        "employee_involved": null,
        "end_date": null,
        "exposure": 0,
        "exposure_dept_id": null,
        "exposure_individual_name": null,
        "exposure_type_id": 1,
        "exposure_vendor_id": null,
        "gdpr": {
          "gdpr_breach_circumstances": [],
          "gdpr_breach_type": null,
          "gdpr_breach_type_comment": null,
          "gdpr_consequences": null,
          "gdpr_consequences_comment": null,
          "gdpr_final_assessment": null,
          "gdpr_final_assessment_comment": null,
          "gdpr_identification": null,
          "gdpr_identification_comment": null,
          "gdpr_personal_data": null,
          "gdpr_personal_data_comment": null,
          "gdpr_subsequent_notification": null
        },
        "hard_liability": 0,
        "id": 2112,
        "inc_last_modified_date": 1663699613661,
        "inc_start": null,
        "inc_training": false,
        "incident_type_ids": [],
        "is_scenario": false,
        "jurisdiction_name": null,
        "jurisdiction_reg_id": null,
        "members": [],
        "name": "SOAR Utilities",
        "negative_pr_likely": null,
        "nist_attack_vectors": [],
        "org_handle": 201,
        "org_id": 201,
        "owner_id": 1,
        "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "change_workspace": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
        },
        "phase_id": 1000,
        "pii": {
          "alberta_health_risk_assessment": null,
          "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
          "california_health_risk_assessment": null,
          "data_compromised": null,
          "data_contained": null,
          "data_encrypted": null,
          "data_format": null,
          "data_source_ids": [],
          "dc_impact_likely": null,
          "determined_date": 1663093285999,
          "exposure": 0,
          "gdpr_harm_risk": null,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2,
          "impact_likely": null,
          "new_zealand_risk_assessment": null,
          "ny_impact_likely": null,
          "or_impact_likely": null,
          "singapore_risk_assessment": null,
          "wa_impact_likely": null
        },
        "plan_status": "A",
        "properties": {
          "internal_customizations_field": null,
          "sdlp_incident_id": null,
          "sdlp_incident_status": null,
          "sdlp_incident_url": null,
          "sdlp_policy_group_id": null,
          "sdlp_policy_group_name": null,
          "sdlp_policy_id": null,
          "sdlp_policy_name": null
        },
        "regulator_risk": {},
        "reporter": null,
        "resolution_id": null,
        "resolution_summary": null,
        "sequence_code": "E2E5-18",
        "severity_code": 4,
        "start_date": null,
        "state": null,
        "task_changes": {
          "added": [],
          "removed": []
        },
        "vers": 7,
        "workspace": 1,
        "zip": null
      },
      {
        "addr": null,
        "admin_id": null,
        "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
        "city": null,
        "confirmed": false,
        "country": null,
        "create_date": 1663188001122,
        "creator": null,
        "creator_id": 6,
        "creator_principal": {
          "display_name": "Chris\u0027 Integration Server v43",
          "id": 6,
          "name": "0228e00e-2c47-43e6-a736-550f104c94ea",
          "type": "apikey"
        },
        "crimestatus_id": 1,
        "data_compromised": null,
        "description": "Test",
        "discovered_date": 1621110044000,
        "draft": false,
        "due_date": null,
        "employee_involved": null,
        "end_date": null,
        "exposure": 0,
        "exposure_dept_id": null,
        "exposure_individual_name": null,
        "exposure_type_id": 1,
        "exposure_vendor_id": null,
        "gdpr": {
          "gdpr_breach_circumstances": [],
          "gdpr_breach_type": null,
          "gdpr_breach_type_comment": null,
          "gdpr_consequences": null,
          "gdpr_consequences_comment": null,
          "gdpr_final_assessment": null,
          "gdpr_final_assessment_comment": null,
          "gdpr_identification": null,
          "gdpr_identification_comment": null,
          "gdpr_personal_data": null,
          "gdpr_personal_data_comment": null,
          "gdpr_subsequent_notification": null
        },
        "hard_liability": 0,
        "id": 2113,
        "inc_last_modified_date": 1663613729686,
        "inc_start": null,
        "inc_training": false,
        "incident_type_ids": [],
        "is_scenario": false,
        "jurisdiction_name": null,
        "jurisdiction_reg_id": null,
        "members": [],
        "name": "SOAR Utils",
        "negative_pr_likely": null,
        "nist_attack_vectors": [],
        "org_handle": 201,
        "org_id": 201,
        "owner_id": 3,
        "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "change_workspace": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
        },
        "phase_id": 1000,
        "pii": {
          "alberta_health_risk_assessment": null,
          "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
          "california_health_risk_assessment": null,
          "data_compromised": null,
          "data_contained": null,
          "data_encrypted": null,
          "data_format": null,
          "data_source_ids": [],
          "dc_impact_likely": null,
          "determined_date": 1621110044000,
          "exposure": 0,
          "gdpr_harm_risk": null,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2,
          "impact_likely": null,
          "new_zealand_risk_assessment": null,
          "ny_impact_likely": null,
          "or_impact_likely": null,
          "singapore_risk_assessment": null,
          "wa_impact_likely": null
        },
        "plan_status": "A",
        "properties": {
          "internal_customizations_field": null,
          "sdlp_incident_id": null,
          "sdlp_incident_status": null,
          "sdlp_incident_url": null,
          "sdlp_policy_group_id": null,
          "sdlp_policy_group_name": null,
          "sdlp_policy_id": null,
          "sdlp_policy_name": null
        },
        "regulator_risk": {},
        "reporter": null,
        "resolution_id": null,
        "resolution_summary": null,
        "sequence_code": "E2E5-19",
        "severity_code": null,
        "start_date": null,
        "state": null,
        "task_changes": {
          "added": [],
          "removed": []
        },
        "vers": 2,
        "workspace": 1,
        "zip": null
      },
      {
        "addr": null,
        "admin_id": null,
        "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
        "city": null,
        "confirmed": false,
        "country": null,
        "create_date": 1663297952673,
        "creator": null,
        "creator_id": 6,
        "creator_principal": {
          "display_name": "Chris\u0027 Integration Server v43",
          "id": 6,
          "name": "0228e00e-2c47-43e6-a736-550f104c94ea",
          "type": "apikey"
        },
        "crimestatus_id": 1,
        "data_compromised": null,
        "description": "Testing",
        "discovered_date": 1621110044000,
        "draft": false,
        "due_date": null,
        "employee_involved": null,
        "end_date": 1663610449718,
        "exposure": 0,
        "exposure_dept_id": null,
        "exposure_individual_name": null,
        "exposure_type_id": 1,
        "exposure_vendor_id": null,
        "gdpr": {
          "gdpr_breach_circumstances": [],
          "gdpr_breach_type": null,
          "gdpr_breach_type_comment": null,
          "gdpr_consequences": null,
          "gdpr_consequences_comment": null,
          "gdpr_final_assessment": null,
          "gdpr_final_assessment_comment": null,
          "gdpr_identification": null,
          "gdpr_identification_comment": null,
          "gdpr_personal_data": null,
          "gdpr_personal_data_comment": null,
          "gdpr_subsequent_notification": null
        },
        "hard_liability": 0,
        "id": 2114,
        "inc_last_modified_date": 1663610451616,
        "inc_start": null,
        "inc_training": false,
        "incident_type_ids": [],
        "is_scenario": false,
        "jurisdiction_name": null,
        "jurisdiction_reg_id": null,
        "members": [],
        "name": "Create Incident",
        "negative_pr_likely": null,
        "nist_attack_vectors": [],
        "org_handle": 201,
        "org_id": 201,
        "owner_id": 3,
        "perms": {
          "assign": true,
          "attach_file": true,
          "change_members": true,
          "change_workspace": true,
          "close": true,
          "comment": true,
          "create_artifacts": true,
          "create_milestones": true,
          "delete": true,
          "delete_attachments": true,
          "list_artifacts": true,
          "list_milestones": true,
          "read": true,
          "read_attachments": true,
          "write": true
        },
        "phase_id": 1000,
        "pii": {
          "alberta_health_risk_assessment": null,
          "assessment": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?\u003e\n\u003cassessment\u003e\n    \u003crollups/\u003e\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\n\u003c/assessment\u003e\n",
          "california_health_risk_assessment": null,
          "data_compromised": null,
          "data_contained": null,
          "data_encrypted": null,
          "data_format": null,
          "data_source_ids": [],
          "dc_impact_likely": null,
          "determined_date": 1621110044000,
          "exposure": 0,
          "gdpr_harm_risk": null,
          "gdpr_lawful_data_processing_categories": [],
          "harmstatus_id": 2,
          "impact_likely": null,
          "new_zealand_risk_assessment": null,
          "ny_impact_likely": null,
          "or_impact_likely": null,
          "singapore_risk_assessment": null,
          "wa_impact_likely": null
        },
        "plan_status": "C",
        "properties": {
          "internal_customizations_field": null,
          "sdlp_incident_id": null,
          "sdlp_incident_status": null,
          "sdlp_incident_url": null,
          "sdlp_policy_group_id": null,
          "sdlp_policy_group_name": null,
          "sdlp_policy_id": null,
          "sdlp_policy_name": null
        },
        "regulator_risk": {},
        "reporter": null,
        "resolution_id": 10,
        "resolution_summary": "closing",
        "sequence_code": "E2E5-20",
        "severity_code": null,
        "start_date": null,
        "state": null,
        "task_changes": {
          "added": [],
          "removed": []
        },
        "vers": 3,
        "workspace": 1,
        "zip": null
      }
    ],
    "recordsFiltered": 17,
    "recordsTotal": 17
  },
  "inputs": {
    "soar_utils_filter_conditions": null,
    "soar_utils_sort_fields": "[{\"field_name\":\"id\",\"type\":\"asc\"}]"
  },
  "metrics": {
    "execution_time_ms": 276,
    "host": "Christophers-MacBook-Pro-2.local",
    "package": "fn-soar-utils",
    "package_version": "1.0.0",
    "timestamp": "2022-09-20 14:46:54",
    "version": "1.0"
  },
  "raw": "{\"recordsTotal\": 17, \"recordsFiltered\": 17, \"data\": [{\"name\": \"AbuseIPDB\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 2, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1643922138662, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1647529122634, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2095, \"sequence_code\": \"E2E5-1\", \"discovered_date\": 1643922138662, \"due_date\": null, \"create_date\": 1643922148213, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"GoogleSafeBrowsing\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 2, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1645039833651, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1647461667230, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2096, \"sequence_code\": \"E2E5-2\", \"discovered_date\": 1645039833651, \"due_date\": null, \"create_date\": 1645039847583, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"PassiveTotal\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 2, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1646103998739, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1647974941312, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2097, \"sequence_code\": \"E2E5-3\", \"discovered_date\": 1646103998739, \"due_date\": null, \"create_date\": 1646142354974, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"ShadowServer\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 2, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1647975098216, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1653512178112, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2098, \"sequence_code\": \"E2E5-4\", \"discovered_date\": 1647975098216, \"due_date\": null, \"create_date\": 1647975111873, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"Yeti\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 2, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1648839797719, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1649700668706, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2099, \"sequence_code\": \"E2E5-5\", \"discovered_date\": 1648839797719, \"due_date\": null, \"create_date\": 1648839806477, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"hibp\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 2, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1649858935196, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1651092229697, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2100, \"sequence_code\": \"E2E5-6\", \"discovered_date\": 1649858935196, \"due_date\": null, \"create_date\": 1649858943997, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"VirusTotal\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 4, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1651000728764, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1653580063528, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2101, \"sequence_code\": \"E2E5-7\", \"discovered_date\": 1651000728764, \"due_date\": null, \"create_date\": 1651000737927, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"URLScan.io\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 74, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1651264262077, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1652814527143, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2102, \"sequence_code\": \"E2E5-8\", \"discovered_date\": 1651264262077, \"due_date\": null, \"create_date\": 1651264273600, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"Google Cloud DLP\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 12, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1655912228120, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1655924984252, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2103, \"sequence_code\": \"E2E5-9\", \"discovered_date\": 1655912228120, \"due_date\": null, \"create_date\": 1655912245009, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"Slack\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 16, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1656527528505, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1661269393325, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2104, \"sequence_code\": \"E2E5-10\", \"discovered_date\": 1656527528505, \"due_date\": null, \"create_date\": 1656527541659, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"New Slack\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 4, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1660155959409, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1661281207911, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2107, \"sequence_code\": \"E2E5-13\", \"discovered_date\": 1660155959409, \"due_date\": null, \"create_date\": 1660155971260, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"Slack2\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 6, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1660245674318, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1661280682539, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2108, \"sequence_code\": \"E2E5-14\", \"discovered_date\": 1660245674318, \"due_date\": null, \"create_date\": 1660245680733, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"debug incident\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 13, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1661346194202, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1661447571753, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2110, \"sequence_code\": \"E2E5-16\", \"discovered_date\": 1661346194202, \"due_date\": null, \"create_date\": 1661346206429, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"Timer\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 2, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1661800148708, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1662747629777, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2111, \"sequence_code\": \"E2E5-17\", \"discovered_date\": 1661800148708, \"due_date\": null, \"create_date\": 1661800169751, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"SOAR Utilities\", \"description\": null, \"phase_id\": 1000, \"inc_training\": false, \"vers\": 7, \"addr\": null, \"city\": null, \"creator\": {\"id\": 1, \"fname\": \"Admin\", \"lname\": \"User\", \"display_name\": \"Admin User\", \"status\": \"A\", \"email\": \"admin@example.com\", \"phone\": \"\", \"cell\": \"\", \"title\": \"\", \"locked\": false, \"password_changed\": false, \"is_external\": false, \"ui_theme\": \"verydarkmode\", \"is_ldap\": false, \"is_saml\": false}, \"creator_principal\": {\"id\": 1, \"type\": \"user\", \"name\": \"admin@example.com\", \"display_name\": \"Admin User\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": true, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1663093285999, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1663699613661, \"admin_id\": null, \"creator_id\": 1, \"crimestatus_id\": 5, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2112, \"sequence_code\": \"E2E5-18\", \"discovered_date\": 1663093285999, \"due_date\": null, \"create_date\": 1663093296645, \"owner_id\": 1, \"severity_code\": 4, \"plan_status\": \"A\"}, {\"name\": \"SOAR Utils\", \"description\": \"Test\", \"phase_id\": 1000, \"inc_training\": false, \"vers\": 2, \"addr\": null, \"city\": null, \"creator\": null, \"creator_principal\": {\"id\": 6, \"type\": \"apikey\", \"name\": \"0228e00e-2c47-43e6-a736-550f104c94ea\", \"display_name\": \"Chris\u0027 Integration Server v43\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": false, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_policy_group_id\": null, \"sdlp_incident_id\": null}, \"resolution_id\": null, \"resolution_summary\": null, \"pii\": {\"data_compromised\": null, \"determined_date\": 1621110044000, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1663613729686, \"admin_id\": null, \"creator_id\": 6, \"crimestatus_id\": 1, \"employee_involved\": null, \"end_date\": null, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2113, \"sequence_code\": \"E2E5-19\", \"discovered_date\": 1621110044000, \"due_date\": null, \"create_date\": 1663188001122, \"owner_id\": 3, \"severity_code\": null, \"plan_status\": \"A\"}, {\"name\": \"Create Incident\", \"description\": \"Testing\", \"phase_id\": 1000, \"inc_training\": false, \"vers\": 3, \"addr\": null, \"city\": null, \"creator\": null, \"creator_principal\": {\"id\": 6, \"type\": \"apikey\", \"name\": \"0228e00e-2c47-43e6-a736-550f104c94ea\", \"display_name\": \"Chris\u0027 Integration Server v43\"}, \"exposure_type_id\": 1, \"incident_type_ids\": [], \"reporter\": null, \"state\": null, \"country\": null, \"zip\": null, \"workspace\": 1, \"exposure\": 0, \"org_handle\": 201, \"members\": [], \"negative_pr_likely\": null, \"perms\": {\"read\": true, \"write\": true, \"comment\": true, \"assign\": true, \"close\": true, \"change_members\": true, \"attach_file\": true, \"read_attachments\": true, \"delete_attachments\": true, \"create_milestones\": true, \"list_milestones\": true, \"create_artifacts\": true, \"list_artifacts\": true, \"delete\": true, \"change_workspace\": true}, \"confirmed\": false, \"task_changes\": {\"added\": [], \"removed\": []}, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"data_compromised\": null, \"draft\": false, \"properties\": {\"sdlp_policy_name\": null, \"sdlp_policy_group_name\": null, \"sdlp_policy_id\": null, \"sdlp_incident_status\": null, \"sdlp_incident_url\": null, \"internal_customizations_field\": null, \"sdlp_incident_id\": null, \"sdlp_policy_group_id\": null}, \"resolution_id\": 10, \"resolution_summary\": \"closing\", \"pii\": {\"data_compromised\": null, \"determined_date\": 1621110044000, \"harmstatus_id\": 2, \"data_encrypted\": null, \"data_contained\": null, \"impact_likely\": null, \"ny_impact_likely\": null, \"or_impact_likely\": null, \"wa_impact_likely\": null, \"dc_impact_likely\": null, \"data_source_ids\": [], \"data_format\": null, \"assessment\": \"\u003c?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\" standalone=\\\"yes\\\"?\u003e\\n\u003cassessment\u003e\\n    \u003crollups/\u003e\\n    \u003coptional\u003eThere are 1 required and 0 optional tasks from 1 regulators.\u003c/optional\u003e\\n\u003c/assessment\u003e\\n\", \"exposure\": 0, \"gdpr_harm_risk\": null, \"gdpr_lawful_data_processing_categories\": [], \"alberta_health_risk_assessment\": null, \"california_health_risk_assessment\": null, \"new_zealand_risk_assessment\": null, \"singapore_risk_assessment\": null}, \"gdpr\": {\"gdpr_breach_circumstances\": [], \"gdpr_breach_type\": null, \"gdpr_personal_data\": null, \"gdpr_identification\": null, \"gdpr_consequences\": null, \"gdpr_final_assessment\": null, \"gdpr_breach_type_comment\": null, \"gdpr_personal_data_comment\": null, \"gdpr_identification_comment\": null, \"gdpr_consequences_comment\": null, \"gdpr_final_assessment_comment\": null, \"gdpr_subsequent_notification\": null}, \"regulator_risk\": {}, \"inc_last_modified_date\": 1663610451616, \"admin_id\": null, \"creator_id\": 6, \"crimestatus_id\": 1, \"employee_involved\": null, \"end_date\": 1663610449718, \"exposure_dept_id\": null, \"exposure_individual_name\": null, \"exposure_vendor_id\": null, \"jurisdiction_name\": null, \"jurisdiction_reg_id\": null, \"start_date\": null, \"inc_start\": null, \"org_id\": 201, \"is_scenario\": false, \"hard_liability\": 0, \"nist_attack_vectors\": [], \"id\": 2114, \"sequence_code\": \"E2E5-20\", \"discovered_date\": 1621110044000, \"due_date\": null, \"create_date\": 1663297952673, \"owner_id\": 3, \"severity_code\": null, \"plan_status\": \"C\"}]}",
  "reason": null,
  "success": true,
  "version": "1.0"
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
inputs.soar_utils_filter_conditions = playbook.inputs.soar_utils_filter_conditions.content
inputs.soar_utils_sort_fields = playbook.inputs.soar_utils_sort_fields.content
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.search_incidents_result

filter_conditions = results.inputs.get('soar_utils_filter_conditions', '')
msgs = [f"Filter conditions: {filter_conditions}"]

if results.success:
    for inc in results.content['data']:
        inc_id = inc['id']
        inc_name = inc['name']
        msgs.append(f"id: <a target='blank' href='/#incidents/{inc_id}'>{inc_id}</a> Name: {inc_name}")

    total = results.content.get('recordsTotal', 0)
    note_text = (
        f"<b>SOAR Utils: Search Incident - Example (PB)</b><br>"
        f"Found {total} incidents<br>{'<br>'.join(msgs)}"
    )
    incident.addNote(note_text)

else:
    reason = results.get('reason', 'Unknown error')
    sort_fields = results.inputs.get('soar_utils_sort_fields', '')
    note_text = (
        f"<b>SOAR Utils: Search Incident - Example (PB)</b><br>"
        f"Search error found: {reason}<br>"
        f"Filter conditions: {filter_conditions}<br>"
        f"Sort Fields conditions: {sort_fields}"
    )
    incident.addNote(note_text)

```

</p>
</details>

---
## Function - SOAR Utilities: SOAR Search
This function searches the SOAR platform for incident data according to the criteria specified, and returns the results to your workflow. It can be used to find incidents containing data that matches any string, or incidents currently assigned to a given user, or a very wide range of other search conditions.

 ![screenshot: fn-soar-utilities-soar-search ](./doc/screenshots/fn-soar-utilities-soar-search.png) 

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `soar_search_query` | `text` | No | `-` | - |
| `soar_search_template` | `textarea` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "results": [
    {
      "inc_id": 2112,
      "inc_name": "SOAR Utilities",
      "inc_owner_id": 1,
      "match_field_name": "Content Type",
      "match_field_value": "application/\u003cResilientHighlight\u003ezip\u003c/ResilientHighlight\u003e",
      "match_highlights": [
        {
          "match_field_name": "Content Type",
          "match_field_value": "application/\u003cResilientHighlight\u003ezip\u003c/ResilientHighlight\u003e"
        },
        {
          "match_field_name": "Name",
          "match_field_value": "\u003cResilientHighlight\u003eapp\u003c/ResilientHighlight\u003e-\u003cResilientHighlight\u003efn_slack\u003c/ResilientHighlight\u003e-\u003cResilientHighlight\u003e2.0.0\u003c/ResilientHighlight\u003e-\u003cResilientHighlight\u003e13477\u003c/ResilientHighlight\u003e.\u003cResilientHighlight\u003ezip\u003c/ResilientHighlight\u003e"
        }
      ],
      "obj_create_date": 1663640024209,
      "obj_creator_id": 1,
      "obj_id": 68,
      "obj_name": "app-fn_slack-2.0.0-13477.zip",
      "org_id": 201,
      "result": {
        "actions": [],
        "content_type": "application/zip",
        "created": 1663640024209,
        "creator_id": {
          "display_name": "Admin User",
          "id": 1,
          "name": "admin@example.com",
          "type": "user"
        },
        "id": 68,
        "inc_id": 2112,
        "inc_name": "SOAR Utilities",
        "inc_owner": {
          "display_name": "Admin User",
          "id": 1,
          "name": "admin@example.com",
          "type": "user"
        },
        "name": "app-fn_slack-2.0.0-13477.zip",
        "playbooks": [],
        "size": 599379,
        "task_at_id": null,
        "task_custom": null,
        "task_id": null,
        "task_members": null,
        "task_name": null,
        "type": "incident",
        "uuid": "e5868c93-581b-4543-8113-358becb2c9cc",
        "vers": 7
      },
      "score": 18.473476,
      "task_id": null,
      "task_name": null,
      "type_id": "attachment"
    }
  ]
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
from json import dumps

# Search for other occurrences of the same file attachment in Resilient.

# The search template determines the type(s) of object to search, and the filter conditions.
# This can be used to search within a specific incident field, or to search only incidents that meet other criteria.
# Refer to SearchExInputDTO in the REST API documentation for additional details of this data structure.

# Example search template
json_template = {
  "types": ["attachment"],
  "filters": {
    "incident": [{
        "conditions": [{"field_name": "plan_status", "method": "in", "value": ["A"]}]
      }]
  }
}

inputs.soar_search_template = dumps(json_template)
# The search query can be a simple string.
inputs.soar_search_query = attachment.name
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.soar_search_result

# Build the list of result links
result_info = []
for result in results.results:
    inc_id = result["result"].get("inc_id", "Unknown ID")
    inc_name = result["result"].get("inc_name", "Unnamed Incident")
    obj_name = result.get("obj_name", "Unknown Object")
    
    link = f"<a href='#incidents/{inc_id}'>{inc_name}</a>"
    result_info.append(f"<p>{link} - {obj_name}</p>")

# Construct the final HTML note
if not result_info:
    html = "<div><b>SOAR Utils: SOAR Search - Example (PB):</b><br>No results found.</div>"
else:
    html = (
        "<div>"
        "<p><b>SOAR Utils: SOAR search - Example (PB):</b></p>"
        + "".join(result_info) +
        "</div>"
    )

incident.addNote(html)

```

</p>
</details>

---
## Function - SOAR Utilities: String to Attachment
Creates a new file (.txt) attachment in the incident or task from a string that your workflow provides as input.

 ![screenshot: fn-soar-utilities-string-to-attachment ](./doc/screenshots/fn-soar-utilities-string-to-attachment.png) 

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `attachment_name` | `text` | Yes | `-` | - |
| `incident_id` | `number` | Yes | `-` | - |
| `soar_utils_string_to_convert_to_attachment` | `text` | Yes | `-` | - |
| `task_id` | `number` | No | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "attachment_id": 72
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
# Required inputs are: the string to convert, the incident id and the attachment name
inputs.soar_utils_string_to_convert_to_attachment = artifact.value
inputs.incident_id = incident.id
inputs.attachment_name = "A Test Attachment Name"
# If this is a "task attachment" then we will additionally have a task-id
if task is not None:
  inputs.task_id = task.id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
results = playbook.functions.results.string_to_attachment_result


if results:
  note_text = f"<b>SOAR Utils: String to Attachment - Example (PB):</b> Attachment ID: <b>{results.attachment_id}</b> successfully created"
else:
  note_text = f"<b>SOAR Utils: String to Attachment - Example (PB)</b> Failed: {results.reason}"
incident.addNote(note_text)

```

</p>
</details>

---


## Playbooks
| Playbook Name | Description | Activation Type | Object | Status | Condition | 
| ------------- | ----------- | --------------- | ------ | ------ | --------- | 
| SOAR Utils: (Artifact) Attachment to Base64- Example (PB) | An example playbook converting an Artifact of type File to a Base64 Encoded string. | Manual | artifact | `enabled` | `artifact.attachment has_a_value` | 
| SOAR Utils: Artifact Hash- Example (PB) | An example playbook that calculates hash from an artifact attachment. | Manual | artifact | `enabled` | `artifact.attachment has_a_value` | 
| SOAR Utils: Attachment Hash- Example (PB) | An example playbook that calculates hash from an attachment. | Manual | attachment | `enabled` | `-` | 
| SOAR Utils: Attachment to Base64- Example (PB) | An example playbook converting File attachment to a Base64 Encoded string. | Manual | attachment | `enabled` | `-` | 
| SOAR Utils: Close Incident - Example (PB) | Example playbook to show how to SOAR Utils close incident function from a playbook. | Manual | incident | `enabled` | `-` | 
| SOAR Utils: Create Incident - Example (PB) | Example playbook to show how to use SOAR Utils create incident function from a playbook. | Manual | incident | `enabled` | `-` | 
| SOAR Utils: Get Incident contact Info- Example (PB) | Get owner and member contact information for an Incident. | Manual | incident | `enabled` | `-` | 
| SOAR Utils: Get Task contact Info- Example (PB) | Get owner and member contact information for a task in an Incident. | Manual | task | `enabled` | `-` | 
| SOAR Utils: Search Incidents - Example (PB) | Example playbook for Search incidents based on filtering fields. Sort field are optional | Manual | incident | `enabled` | `-` | 
| SOAR Utils: SOAR Search - Example (PB) | This function searches the SOAR platform for incident data according to the criteria specified, and returns the results to your playbook. It can be used to find incidents containing data that matches any string, incidents currently assigned to a given user, or a very wide range of other search conditions.  NOTE: The search results may include data from incidents that the current SOAR user (the person who triggered the workflow) cannot access. Often your SOAR users have the Default role that allows them to only see incidents where they are members. This function runs with the permissions of your app account, which typically may have much wider access privileges. Use with caution, to avoid information disclosure. | Manual | attachment | `enabled` | `-` | 
| SOAR Utils: String to Attachment - Example (PB) | An example playbook of creating an attachment from an input string. | Manual | artifact | `enabled` | `artifact.type equals String` | 
| SOAR Utils: Zip Extract - Example (PB) | An example playbook showing how to extract a file from a ZIP file attachment and create a new attachment. | Manual | attachment | `enabled` | `attachment.name contains .zip` | 
| SOAR Utils: Zip Extract to Artifact- Example (PB) | An example playbook showing how to extract a file from a ZIP file attachment and create a new artifact. | Manual | attachment | `enabled` | `attachment.name contains .zip` | 
| SOAR Utils: Zip List - Example (PB) | An example playbook showing how to list the contents of a ZIP file attachment. | Manual | attachment | `enabled` | `attachment.name contains .zip` | 

---







## Troubleshooting & Support
Refer to the documentation listed in the Requirements section for troubleshooting information.
 
### For Support
This is a IBM Community provided app. Please search the Community [ibm.biz/soarcommunity](https://ibm.biz/soarcommunity) for assistance.
