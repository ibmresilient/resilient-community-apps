<!--
  This README.md is generated by running:
  "resilient-sdk docgen -p fn_shadowserver"

  It is best edited using a Text Editor with a Markdown Previewer. VS Code
  is a good example. Checkout https://guides.github.com/features/mastering-markdown/
  for tips on writing with Markdown

  All fields followed by "::CHANGE_ME::"" should be manually edited

  If you make manual edits and run docgen again, a .bak file will be created

  Store any screenshots in the "doc/screenshots" directory and reference them like:
  ![screenshot: screenshot_1](./screenshots/screenshot_1.png)

  NOTE: If your app is available in the container-format only, there is no need to mention the integration server in this readme.
-->

# Shadowserver

## Table of Contents
- [Shadowserver](#shadowserver)
  - [Table of Contents](#table-of-contents)
  - [Release Notes](#release-notes)
  - [Overview](#overview)
    - [Key Features](#key-features)
  - [Requirements](#requirements)
    - [SOAR platform](#soar-platform)
    - [Cloud Pak for Security](#cloud-pak-for-security)
    - [Proxy Server](#proxy-server)
    - [Python Environment](#python-environment)
    - [Endpoint Developed With](#endpoint-developed-with)
  - [Installation](#installation)
    - [Install](#install)
    - [App Configuration](#app-configuration)
  - [Function - Shadowserver](#function---shadowserver)
  - [Rules](#rules)
  - [Troubleshooting \& Support](#troubleshooting--support)
    - [For Support](#for-support)
---

## Release Notes
<!--
  Specify all changes in this release. Do not remove the release 
  notes of a previous release
-->
| Version | Date | Notes |
| ------- | ---- | ----- |
| 1.0.0 | 04/2022 | Initial Release |

---

## Overview
<!--
  Provide a high-level description of the function itself and its remote software or application.
  The text below is parsed from the "description" and "long_description" attributes in the setup.py file
-->
**IBM Security SOAR app for Shadowserver**

 ![screenshot: main](./doc/screenshots/main.png) 

Queries Shadowserver to check if the hash provided matches an entry in our database. Returns details on the data source if there is a match.

### Key Features
<!--
  List the Key Features of the Integration
-->
* The workflow checks if the hash provided checks an entry in the Shadowserver database and will then create a hit in the post-processing script with all the information returned from Shadowserver. 

---

## Requirements
<!--
  List any Requirements 
--> 
This app supports the IBM Security QRadar SOAR Platform and the IBM Security QRadar SOAR for IBM Cloud Pak for Security.

### SOAR platform
The SOAR platform supports two app deployment mechanisms, App Host and integration server.

If deploying to a SOAR platform with an App Host, the requirements are:
* SOAR platform >= `43.1.49`.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

If deploying to a SOAR platform with an integration server, the requirements are:
* SOAR platform >= `43.1.49`.
* The app is in the older integration format (available from the AppExchange as a `zip` file which contains a `tar.gz` file).
* Integration server is running `resilient-circuits>=44.0.0`.
* If using an API key account, make sure the account provides the following minimum permissions: 
  | Name | Permissions |
  | ---- | ----------- |
  | Org Data | Read |
  | Function | Read |

The following SOAR platform guides provide additional information: 
* _App Host Deployment Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings. 
* _Integration Server Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings.
* _System Administrator Guide_: provides the procedure to install, configure and deploy apps. 

The above guides are available on the IBM Documentation website at [ibm.biz/soar-docs](https://ibm.biz/soar-docs). On this web page, select your SOAR platform version. On the follow-on page, you can find the _App Host Deployment Guide_ or _Integration Server Guide_ by expanding **Apps** in the Table of Contents pane. The System Administrator Guide is available by expanding **System Administrator**.

### Cloud Pak for Security
If you are deploying to IBM Cloud Pak for Security, the requirements are:
* IBM Cloud Pak for Security >= 1.4.
* Cloud Pak is configured with an App Host.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

The following Cloud Pak guides provide additional information: 
* _App Host Deployment Guide_: provides installation, configuration, and troubleshooting information, including proxy server settings. From the Table of Contents, select Case Management and Orchestration & Automation > **Orchestration and Automation Apps**.
* _System Administrator Guide_: provides information to install, configure, and deploy apps. From the IBM Cloud Pak for Security IBM Documentation table of contents, select Case Management and Orchestration & Automation > **System administrator**.

These guides are available on the IBM Documentation website at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs). From this web page, select your IBM Cloud Pak for Security version. From the version-specific IBM Documentation page, select Case Management and Orchestration & Automation.

### Proxy Server
The app does support a proxy server.

### Python Environment
Python 3.6 is supported.
Additional package dependencies may exist for each of these packages:
* resilient-circuits>=44.0.0

### Endpoint Developed With

This app has been implemented using:
| Product Name | Product Version | API URL | API Version |
| ------------ | --------------- | ------- | ----------- |
| Shadowserver | -- | https://api.shadowserver.org/malware/info | -- |

---

## Installation

### Install
* To install or uninstall an App or Integration on the _SOAR platform_, see the documentation at [ibm.biz/soar-docs](https://ibm.biz/soar-docs).
* To install or uninstall an App on _IBM Cloud Pak for Security_, see the documentation at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs) and follow the instructions above to navigate to Orchestration and Automation.

### App Configuration
The following table provides the settings you need to configure the app. These settings are made in the app.config file. See the documentation discussed in the Requirements section for the procedure.

| Config | Required | Example | Description |
| ------ | :------: | ------- | ----------- |
| **shadowserver_url** | Yes | `https://api.shadowserver.org/malware/info?sample=` | -- |

---

## Function - Shadowserver
Queries Shadowserver to check if the hash provided matches an entry in the Shadowserver database. Returns details on the data source if there is a match.

 ![screenshot: fn-shadowserver ](./doc/screenshots/fn-shadowserver.png)

<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `shadowserver_artifact_type` | `text` | Yes | `-` | - |
| `shadowserver_artifact_value` | `text` | Yes | `-` | - |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "content": [
    {
      "adobe_malware_classifier": "malicious",
      "anti_virus": [
        {
          "signature": "Troj/Agent-APCU",
          "vendor": "Sophos"
        },
        {
          "signature": "W32/Lamer.CQ",
          "vendor": "Fortinet"
        },
        {
          "signature": "PUA.Win.Packer.Purebasic-2",
          "vendor": "Clam"
        },
        {
          "signature": "Win32.Generic.VC",
          "vendor": "AVG"
        },
        {
          "signature": "Gen:Win32.FileInfector.uwZ@a4T!Kcmi",
          "vendor": "MicroWorld"
        },
        {
          "signature": "Virus ( 004d554e1 )",
          "vendor": "K7GW"
        },
        {
          "signature": "W32.Sivis.A5",
          "vendor": "QuickHeal"
        },
        {
          "signature": "Trojan/Win32.FileInfector",
          "vendor": "AhnLab"
        },
        {
          "signature": "Win32:Malware-gen",
          "vendor": "Avast"
        },
        {
          "signature": "Trojan.PWS.Onlinegames.KEGA",
          "vendor": "BitDefender"
        },
        {
          "signature": "Trojan.GenericKD.40542465",
          "vendor": "BitDefender"
        },
        {
          "signature": "Gen.Win32.FileInfector",
          "vendor": "Ikarus"
        },
        {
          "signature": "Virus.Win32.sivis.a",
          "vendor": "Sunbelt"
        },
        {
          "signature": "Gen:Win32.FileInfector.uwZ@a4T!Kcmi",
          "vendor": "BitDefender"
        },
        {
          "signature": "PUA.Win.Packer.Purebasic-2",
          "vendor": "Clam"
        },
        {
          "signature": "Gen:Win32.Backdoor.ozZbauKWKdpb",
          "vendor": "BitDefender"
        },
        {
          "signature": "Win32.Generic.VC",
          "vendor": "AVG"
        },
        {
          "signature": "Virus ( 004d554e1 )",
          "vendor": "K7GW"
        },
        {
          "signature": "Win32.HLLW.Siggen.4657",
          "vendor": "DrWeb"
        },
        {
          "signature": "TR/Dropper.Gen8",
          "vendor": "Avira"
        },
        {
          "signature": "Win32/Zatoxp.C",
          "vendor": "Eset"
        },
        {
          "signature": "Win32:Malware-gen",
          "vendor": "Avast"
        },
        {
          "signature": "Virus ( 004d554e1 )",
          "vendor": "K7"
        },
        {
          "signature": "Trojan/Win32.FileInfector",
          "vendor": "AhnLab"
        },
        {
          "signature": "Win32:Lamer-A",
          "vendor": "Avast"
        },
        {
          "signature": "Gen:Win32.FileInfector.uwZ@a4T!Kcmi",
          "vendor": "BitDefender"
        }
      ],
      "entropic": "5.952427",
      "filesize": "2438340",
      "first_seen": "2016-08-25 02:44:39",
      "import_hash": "33f98db5bdb6a7013d52f0120248df35",
      "last_seen": "2016-08-25 02:44:39",
      "magic": "PE32 executable (GUI) Intel 80386, for MS Windows",
      "md5": "dfe1832e02888422f48d6896dc8e8f73",
      "pehash": "243c359*******829f30b30c45839cbf6",
      "sha1": "c56ba4*******7be3c1eb5588cec27c413eb208",
      "sha256": "d8d395f87443*******0a4308e7b380a0aca86bfc8939ded9f4c8c5cb1e838a",
      "sha512": "7ca1fdfe537913b8*******efc1f11b00d405f2d21e416e7023c4ebed2bfa887d2bc4d4d553ce41667c99def47ea05e6ce4a773c4ee7173927f1d263e724c16c2",
      "timestamp": "2016-08-25 02:44:39",
      "tlsh": "c1b52a5273fa0*******f75a8b7a3944939fea11d22e08e1164314d88b6f808e75bb7",
      "type": "exe"
    }
  ],
  "inputs": {
    "shadowserver_artifact_type": "Malware SHA-1 Hash",
    "shadowserver_artifact_value": "c56ba498d41caa7be3c1eb5588cec27c413eb208"
  },
  "metrics": {
    "execution_time_ms": 386,
    "host": "My Host",
    "package": "fn-shadowserver",
    "package_version": "1.0.0",
    "timestamp": "2022-03-30 11:34:35",
    "version": "1.0"
  },
  "raw": null,
  "reason": null,
  "success": true,
  "version": 2.0
}
```

</p>
</details>

<details><summary>Example Pre-Process Script:</summary>
<p>

```python
inputs.shadowserver_artifact_type = artifact.type
inputs.shadowserver_artifact_value = artifact.value
```

</p>
</details>

<details><summary>Example Post-Process Script:</summary>
<p>

```python

if results.success:
  if results.content:
    resp = results.content
    hit_list = []
    for attribute, attribute_value in resp.items():
      hit = {
        "name": attribute,
        "type": "string",
        "value": "{}".format(attribute_value)
      }
      hit_list.append(hit)
    artifact.addHit("ShadowServer Function", hit_list)
else:
  incident.addNote("ShadowServer Hash check failed: {}".format(results.reason))
    
```

</p>
</details>

---





## Rules
| Rule Name | Object | Workflow Triggered |
| --------- | ------ | ------------------ |
| Shadowserver Hash Query | artifact | `shadowserver_hash_query` |

---


## Troubleshooting & Support
Refer to the documentation listed in the Requirements section for troubleshooting information.

### For Support
This is a IBM Community provided App. Please search the Community [ibm.biz/soarcommunity](https://ibm.biz/soarcommunity) for assistance.
