# URL ScanIO


## Table of Contents
- [Table of Contents](#table-of-contents)
- [Release Notes](#release-notes)
- [Overview](#overview)
- [Requirements](#requirements)
  - [SOAR platform](#soar-platform)
  - [Cloud Pak for Security](#cloud-pak-for-security)
  - [Proxy Server](#proxy-server)
  - [Python Environment](#python-environment)
- [Installation](#installation)
  - [Install](#install)
  - [App Configuration](#app-configuration)
- [Function - Scan with urlscan.io](#function---scan-with-urlscan.io)
- [Troubleshooting \& Support](#troubleshooting--support)
  - [For Support](#for-support)


---

## Release Notes
| Version | Date | Notes |
| ------- | ---- | ----- |
| 1.2.0 | 05/2026 | Add playbook with aim to replace workflow in future release. Add auth headers to all GET requests in line with API usage changes with urlscan.io. |
| 1.1.6 | 04/2025 | Converted example workflows to python3 |
| 1.1.5 | 06/2021 | Bug fix error for non existing url |
| 1.1.4 | 09/2020 | Proxy support added |
| 1.1.3 | 05/2020 | Compatibility with older versions of resilient-circuits |
| 1.1.2 | 04/2020 | Support added for App Host |
| 1.1.1 | 04/2020 | Pinned version of resilient-lib to work with write_file_attachment <br> Updated customize.py so minimum required version of Resilient is v35.0 |
| 1.1.0 | 03/2020 | Removed workflow dependency on fn_utilities <br> Added incident_id parameter to workflow inputs |
| 1.0.0 | 12/2018 | Initial Release |

---

## Overview
**Resilient Circuits Components for 'fn_urlscanio'**

 ![screenshot: main](./doc/screenshots/main.png)

[https://urlscan.io](urlscan.io) is a service to scan and analyse websites. When a URL is submitted to urlscan.io,
an automated process will browse to the URL like a regular user and record the activity that this page navigation
creates. This includes the domains and IPs contacted, the resources (JavaScript, CSS, etc) requested from those
domains, as well as additional information about the page itself. urlscan.io will take a screenshot of the page,
record the DOM content, JavaScript global variables, cookies created by the page, and a myriad of other observations.

This integration is a Resilient function that can be called from workflows, to submit a URL for analysis by urlscan.io.
It returns the report metadata, report URL, and base64-encoded screenshot that is attached to the incident.

---

## Requirements
This app supports the IBM Security QRadar SOAR Platform and the IBM Security QRadar SOAR for IBM Cloud Pak for Security.

### SOAR platform
The SOAR platform supports two app deployment mechanisms, Edge Gateway (also known as App Host) and integration server.

If deploying to a SOAR platform with an App Host, the requirements are:
* SOAR platform >= `51.0.8.0.20726
`.
* The app is in a container-based format (available from the AppExchange as a `zip` file).

If deploying to a SOAR platform with an integration server, the requirements are:
* SOAR platform >= `51.0.8.0.20726
`.
* The app is in the older integration format (available from the AppExchange as a `zip` file which contains a `tar.gz` file).
* Integration server is running `resilient_circuits>=51.0.0`.
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
The app **does** support a proxy server.

### Python Environment
Python 3.11 and 3.12 are officially supported. When deployed as an app, the app runs on Python 3.11.
Additional package dependencies may exist for each of these packages:
* resilient_circuits>=51.0.0
* resilient_lib>=51.0.0


---

## Installation

### Install
* To install or uninstall an App or Integration on the _SOAR platform_, see the documentation at [ibm.biz/soar-docs](https://ibm.biz/soar-docs).
* To install or uninstall an App on _IBM Cloud Pak for Security_, see the documentation at [ibm.biz/cp4s-docs](https://ibm.biz/cp4s-docs) and follow the instructions above to navigate to Orchestration and Automation.

### App Configuration
The following table provides the settings you need to configure the app. These settings are made in the app.config file. See the documentation discussed in the Requirements section for the procedure.

| Config | Required | Example | Description |
| ------ | :------: | ------- | ----------- |
| **urlscanio_report_url** | Yes | `https://urlscan.io/api/v1` | *URL to retrieve scan reports* |
| **urlscanio_screenshot_url** | Yes | `https://urlscan.io/screenshots` | *URL for website screenshots* |
| **urlscanio_api_key** | Yes | 1790000-0000-0000-0000-a1b2c3d4597 / *Provide your URLScanIO API key* |
| **timeout** | No | 300 / *Seconds to timeout reports which take a long time to complete. Default 5 minutes* |
| **http_proxy** | No | `http://your_proxy.com` | *Optional http proxy URL* |
| **https_proxy** | No | `https://your_proxy.com` | *Optional https proxy URL* |

 ---

## Function - Scan with urlscan.io
Analyze a URL with urlscan.io


<details><summary>Inputs:</summary>
<p>

| Name | Type | Required | Example | Tooltip |
| ---- | :--: | :------: | ------- | ------- |
| `incident_id` | `number` | Yes | `-` | the id of the incident |
| `urlscanio_public` | `boolean` | No | `-` | Should the scan be posted as public? |
| `urlscanio_referer` | `text` | No | `-` | Custom referer URL for this scan |
| `urlscanio_url` | `text` | No | `-` | - |
| `urlscanio_useragent` | `text` | No | `-` | Override User-Agent for this scan |

</p>
</details>

<details><summary>Outputs:</summary>
<p>

> **NOTE:** This example might be in JSON format, but `results` is a Python Dictionary on the SOAR platform.

```python
results = {
  "png_base64content": "b\u0027iVBORw0KGgoAAAANS******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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD8Sv8fPv3XOmgnQlgAAAAASUVORK5CYII=\u0027",
  "png_url": "https://urlscan.io/screenshots/0195fbfa-84aa-706a-9c7d-e84cfadf0199.png",
  "report": {
    "data": {
      "console": [
        {
          "message": {
            "level": "error",
            "source": "network",
            "text": "Failed to load resource: the server responded with a status of 404 ()",
            "timestamp": 1743689255168.243,
            "url": "https://www.example.com/page.html"
          }
        },
        {
          "message": {
            "level": "error",
            "source": "network",
            "text": "Failed to load resource: the server responded with a status of 404 ()",
            "timestamp": 1743689255240.546,
            "url": "https://www.example.com/favicon.ico"
          }
        }
      ],
      "cookies": [],
      "globals": [],
      "links": [
        {
          "href": "https://www.iana.org/domains/example",
          "text": "More information..."
        }
      ],
      "requests": [
        {
          "request": {
            "documentURL": "https://www.example.com/page.html",
            "frameId": "CD9E4F30FBDA2CCFD5017B733804ECC4",
            "hasUserGesture": false,
            "initiator": {
              "type": "other"
            },
            "loaderId": "62201A5A3D1FD1CC81A23D76F51DA8FC",
            "primaryRequest": true,
            "redirectHasExtraInfo": false,
            "request": {
              "headers": {
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
              },
              "initialPriority": "VeryHigh",
              "isSameSite": true,
              "method": "GET",
              "mixedContentType": "none",
              "referrerPolicy": "strict-origin-when-cross-origin",
              "url": "https://www.example.com/page.html"
            },
            "requestId": "62201A5A3D1FD1CC81A23D76F51DA8FC",
            "timestamp": 10821428.508261,
            "type": "Document",
            "wallTime": 1743689254.10678
          },
          "response": {
            "asn": {
              "asn": "20940",
              "country": "NL",
              "description": "AKAMAI-ASN1 Akamai International B.V., NL",
              "ip": "2a02:26f0:2780:6::214:f58b",
              "name": "AKAMAI-ASN1 Akamai International B.V.",
              "route": "2a02:26f0:2000::/37"
            },
            "dataLength": 1256,
            "encodedDataLength": 1538,
            "geoip": {
              "city": "",
              "country": "NL",
              "country_name": "Netherlands",
              "ll": [
                52.3824,
                4.8995
              ],
              "metro": 0,
              "region": "",
              "timezone": "Europe/Amsterdam"
            },
            "hasExtraInfo": true,
            "hash": "ea8fac7c65fb589b0d53560f5251f74f9e9b243478dcb6b3ea79b5e36449c8d9",
            "requestId": "62201A5A3D1FD1CC81A23D76F51DA8FC",
            "response": {
              "alternateProtocolUsage": "unspecifiedReason",
              "charset": "",
              "encodedDataLength": 1538,
              "headers": {
                "accept-ranges": "bytes",
                "alt-svc": "h3=\":443\"; ma=93600,h3-29=\":443\"; ma=93600,quic=\":443\"; ma=93600; v=\"43\"",
                "cache-control": "max-age=0, no-cache, no-store",
                "content-length": "1256",
                "content-type": "text/html",
                "date": "Thu, 03 Apr 2025 14:07:35 GMT",
                "etag": "\"84238dfc8092e5d9c0dac8ef93371a07:1736799080.121134\"",
                "expires": "Thu, 03 Apr 2025 14:07:35 GMT",
                "last-modified": "Mon, 13 Jan 2025 20:11:20 GMT",
                "pragma": "no-cache",
                "server": "AkamaiNetStorage"
              },
              "mimeType": "text/html",
              "protocol": "h2",
              "remoteIPAddress": "2a02:26f0:2780:6::214:f58b",
              "remotePort": 443,
              "responseTime": 1743689255162.935,
              "securityDetails": {
                "certificateId": 0,
                "certificateTransparencyCompliance": "compliant",
                "cipher": "AES_256_GCM",
                "encryptedClientHello": false,
                "issuer": "DigiCert Global G3 TLS ECC SHA384 2020 CA1",
                "keyExchange": "***",
                "keyExchangeGroup": "***",
                "protocol": "TLS 1.3",
                "sanList": [
                  "*.example.com",
                  "example.com"
                ],
                "serverSignatureAlgorithm": 1027,
                "signedCertificateTimestampList": [
                  {
                    "hashAlgorithm": "SHA-256",
                    "logDescription": "Google \u0027Argon2026h1\u0027 log",
                    "logId": "0E5794BCF3AEA93E331B2C9907B3F790DF9BC23D713225DD21A925AC61C54E21",
                    "origin": "Embedded in certificate",
                    "signatureAlgorithm": "ECDSA",
                    "signatureData": "3043021F24170F5A4C7CD2293BB8B616E8E1AF358BC9E0D98E47645773DBAF8853C7E9022052DBAE51E9C7213E5435625F7C1051AB7D6D5068BB6434D2AEB3347F8CF555AE",
                    "status": "Verified",
                    "timestamp": 1736902885319
                  },
                  {
                    "hashAlgorithm": "SHA-256",
                    "logDescription": "DigiCert \u0027Wyvern2026h1\u0027",
                    "logId": "6411C46CA412ECA7891CA2022E00BCAB4F2807D41E3527ABEAFED503C97DCDF0",
                    "origin": "Embedded in certificate",
                    "signatureAlgorithm": "ECDSA",
                    "signatureData": "3044022070AEE8D807855D50BE27FF1BB047ABB7223061FC8DD721FF1CB82F3AD895EB1702207230532F0E11A0E2C626D4CB2B0C655E75CC2913878DD11B997051A65B1C0972",
                    "status": "Verified",
                    "timestamp": 1736902885381
                  },
                  {
                    "hashAlgorithm": "SHA-256",
                    "logDescription": "DigiCert \u0027Sphinx2026h1\u0027",
                    "logId": "499C9B69DE1D7CECFC36DECD8764A6B85BAF0A878019D15552FBE9EB29DDF8C3",
                    "origin": "Embedded in certificate",
                    "signatureAlgorithm": "ECDSA",
                    "signatureData": "3045022068587AEF2110DA5C209B75F5EA7DA25A31101482366F67E938DB415626D9556C022100F9A6CAA35C362C2046F58728744BC6C13773B8BB6B00F738AC2889588D983CC2",
                    "status": "Verified",
                    "timestamp": 1736902885401
                  }
                ],
                "subjectName": "*.example.com",
                "validFrom": 1736899200,
                "validTo": 1768521599
              },
              "securityState": "secure",
              "status": 404,
              "statusText": "",
              "timing": {
                "connectEnd": 202.03,
                "connectStart": 156.441,
                "dnsEnd": 156.383,
                "dnsStart": 0,
                "proxyEnd": -1,
                "proxyStart": -1,
                "pushEnd": 0,
                "pushStart": 0,
                "receiveHeadersEnd": 1056.926,
                "receiveHeadersStart": 1055.764,
                "requestTime": 10821428.508643,
                "sendEnd": 202.184,
                "sendStart": 202.131,
                "sslEnd": 202.025,
                "sslStart": 175.182,
                "workerFetchStart": -1,
                "workerReady": -1,
                "workerRespondWithSettled": -1,
                "workerStart": -1
              },
              "url": "https://www.example.com/page.html"
            },
            "size": 1256,
            "type": "Document"
          }
        },
        {
          "request": {
            "documentURL": "https://www.example.com/page.html",
            "frameId": "CD9E4F30FBDA2******17B733804ECC4",
            "hasUserGesture": false,
            "initiator": {
              "type": "other"
            },
            "loaderId": "62201A5A3D1F******A23D76F51DA8FC",
            "redirectHasExtraInfo": false,
            "request": {
              "headers": {
                "Referer": "https://www.example.com/page.html",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
              },
              "initialPriority": "High",
              "isSameSite": true,
              "method": "GET",
              "mixedContentType": "none",
              "referrerPolicy": "strict-origin-when-cross-origin",
              "url": "https://www.example.com/favicon.ico"
            },
            "requestId": "237764.2",
            "timestamp": 10821429.58155,
            "type": "Other",
            "wallTime": 1743689255.180086
          },
          "response": {
            "asn": {
              "asn": "20940",
              "country": "NL",
              "description": "AKAMAI-ASN1 Akamai International B.V., NL",
              "ip": "2a02:26f0:2780:6::214:f58b",
              "name": "AKAMAI-ASN1 Akamai International B.V.",
              "route": "2a02:26f0:2000::/37"
            },
            "dataLength": 1256,
            "encodedDataLength": 1471,
            "geoip": {
              "city": "",
              "country": "NL",
              "country_name": "Netherlands",
              "ll": [
                52.3824,
                4.8995
              ],
              "metro": 0,
              "region": "",
              "timezone": "Europe/Amsterdam"
            },
            "hasExtraInfo": true,
            "hash": "ea8fac7c65fb589b0d53560f******4f9e9b243478dcb6b3ea79b5e36449c8d9",
            "requestId": "237764.2",
            "response": {
              "alternateProtocolUsage": "mainJobWonRace",
              "charset": "",
              "encodedDataLength": 1471,
              "headers": {
                "accept-ranges": "bytes",
                "cache-control": "max-age=0, no-cache, no-store",
                "content-length": "1256",
                "content-type": "text/html",
                "date": "Thu, 03 Apr 2025 14:07:35 GMT",
                "etag": "\"84238dfc8092e5d9c0dac8ef93371a07:1736799080.121134\"",
                "expires": "Thu, 03 Apr 2025 14:07:35 GMT",
                "last-modified": "Mon, 13 Jan 2025 20:11:20 GMT",
                "pragma": "no-cache",
                "server": "AkamaiNetStorage"
              },
              "mimeType": "text/html",
              "protocol": "h2",
              "remoteIPAddress": "2a02:26f0:2780:6::214:f58b",
              "remotePort": 443,
              "responseTime": 1743689255239.839,
              "securityDetails": {
                "certificateId": 0,
                "certificateTransparencyCompliance": "compliant",
                "cipher": "AES_256_GCM",
                "encryptedClientHello": false,
                "issuer": "DigiCert Global G3 TLS ECC SHA384 2020 CA1",
                "keyExchange": "***",
                "keyExchangeGroup": "***",
                "protocol": "TLS 1.3",
                "sanList": [
                  "*.example.com",
                  "example.com"
                ],
                "serverSignatureAlgorithm": 1027,
                "signedCertificateTimestampList": [
                  {
                    "hashAlgorithm": "SHA-256",
                    "logDescription": "Google \u0027Argon2026h1\u0027 log",
                    "logId": "0E5794BCF3AEA93E331B2C9907******DF9BC23D713225DD21A925AC61C54E21",
                    "origin": "Embedded in certificate",
                    "signatureAlgorithm": "ECDSA",
                    "signatureData": "3043021F24170F5A4C7CD2293BB8B616E8E1AF******E0D98E47645773DBAF8853C7E9022052DBAE51E9C7213E54356******051AB7D6D5068BB6434D2AEB3347F8CF555AE",
                    "status": "Verified",
                    "timestamp": 1736902885319
                  },
                  {
                    "hashAlgorithm": "SHA-256",
                    "logDescription": "DigiCert \u0027Wyvern2026h1\u0027",
                    "logId": "6411C46CA412ECA7891CA2022******B4F2807D41E3527ABEAFED503C97DCDF0",
                    "origin": "Embedded in certificate",
                    "signatureAlgorithm": "ECDSA",
                    "signatureData": "3044022070AEE8D80******0BE27FF1BB047ABB7223061FC8DD721FF1CB82F3AD895EB1702207230532F0E1******626D4CB2B0C655E75CC2913878DD11B997051A65B1C0972",
                    "status": "Verified",
                    "timestamp": 1736902885381
                  },
                  {
                    "hashAlgorithm": "SHA-256",
                    "logDescription": "DigiCert \u0027Sphinx2026h1\u0027",
                    "logId": "499C9B69DE******FC36DECD8764A6B85BAF0A878019D15552FBE9EB29DDF8C3",
                    "origin": "Embedded in certificate",
                    "signatureAlgorithm": "ECDSA",
                    "signatureData": "3045022068587******DA5C209B75F5EA7DA25A31101482366F67E938DB415626D9556C022100F9A6CAA35C362C2046F58728744BC6C13773B8BB6B00F738AC2889588D983CC2",
                    "status": "Verified",
                    "timestamp": 1736902885401
                  }
                ],
                "subjectName": "*.example.com",
                "validFrom": 1736899200,
                "validTo": 1768521599
              },
              "securityState": "secure",
              "status": 404,
              "statusText": "",
              "timing": {
                "connectEnd": -1,
                "connectStart": -1,
                "dnsEnd": -1,
                "dnsStart": -1,
                "proxyEnd": -1,
                "proxyStart": -1,
                "pushEnd": 0,
                "pushStart": 0,
                "receiveHeadersEnd": 59.597,
                "receiveHeadersStart": 59.411,
                "requestTime": 10821429.581904,
                "sendEnd": 0.469,
                "sendStart": 0.413,
                "sslEnd": -1,
                "sslStart": -1,
                "workerFetchStart": -1,
                "workerReady": -1,
                "workerRespondWithSettled": -1,
                "workerStart": -1
              },
              "url": "https://www.example.com/favicon.ico"
            },
            "size": 1256,
            "type": "Other"
          }
        }
      ],
      "timing": {
        "beginNavigation": "2025-04-03T14:07:34.104Z",
        "domContentEventFired": "2025-04-03T14:07:35.177Z",
        "frameNavigated": "2025-04-03T14:07:35.168Z",
        "frameStartedLoading": "2025-04-03T14:07:34.106Z",
        "frameStoppedLoading": "2025-04-03T14:07:35.180Z"
      }
    },
    "lists": {
      "asns": [
        "20940"
      ],
      "certificates": [
        {
          "issuer": "DigiCert Global G3 TLS ECC SHA384 2020 CA1",
          "subjectName": "*.example.com",
          "validFrom": 1736899200,
          "validTo": 1768521599
        }
      ],
      "countries": [
        "NL"
      ],
      "domains": [
        "www.example.com"
      ],
      "hashes": [
        "ea8fac7c65fb589b0d5356******f74f9e9b243478dcb6b3ea79b5e36449c8d9"
      ],
      "ips": [
        "2a02:26f0:2780:6::214:f58b"
      ],
      "linkDomains": [
        "www.iana.org"
      ],
      "servers": [
        "AkamaiNetStorage"
      ],
      "urls": [
        "https://www.example.com/page.html",
        "https://www.example.com/favicon.ico"
      ]
    },
    "meta": {
      "processors": {
        "asn": {
          "data": [
            {
              "asn": "20940",
              "country": "NL",
              "description": "AKAMAI-ASN1 Akamai International B.V., NL",
              "ip": "2a02:26f0:2780:6::214:f58b",
              "name": "AKAMAI-ASN1 Akamai International B.V.",
              "route": "2a02:26f0:2000::/37"
            }
          ]
        },
        "geoip": {
          "data": [
            {
              "geoip": {
                "city": "",
                "country": "NL",
                "country_name": "Netherlands",
                "ll": [
                  52.3824,
                  4.8995
                ],
                "metro": 0,
                "region": "",
                "timezone": "Europe/Amsterdam"
              },
              "ip": "2a02:26f0:2780:6::214:f58b"
            }
          ]
        },
        "rdns": {
          "data": []
        },
        "umbrella": {
          "data": [
            {
              "hostname": "www.example.com",
              "rank": 28218
            }
          ]
        },
        "wappa": {
          "data": []
        }
      }
    },
    "page": {
      "apexDomain": "example.com",
      "asn": "AS20940",
      "asnname": "AKAMAI-ASN1 Akamai International B.V., NL",
      "city": "",
      "country": "NL",
      "domain": "www.example.com",
      "ip": "2a02:26f0:2780:6::214:f58b",
      "mimeType": "text/html",
      "server": "AkamaiNetStorage",
      "status": "404",
      "title": "Example Domain",
      "tlsAgeDays": 78,
      "tlsIssuer": "DigiCert Global G3 TLS ECC SHA384 2020 CA1",
      "tlsValidDays": 365,
      "tlsValidFrom": "2025-01-15T00:00:00.000Z",
      "umbrellaRank": 28218,
      "url": "https://www.example.com/page.html"
    },
    "scanner": {
      "country": "nl"
    },
    "stats": {
      "IPv6Percentage": 100,
      "adBlocked": 0,
      "domainStats": [
        {
          "count": 2,
          "countries": [
            "NL"
          ],
          "domain": "www.example.com",
          "encodedSize": 3009,
          "index": 0,
          "initiators": [],
          "ips": [
            "2a02:26f0:2780:6::214:f58b"
          ],
          "redirects": 0,
          "size": 2512
        }
      ],
      "ipStats": [
        {
          "asn": {
            "asn": "20940",
            "country": "NL",
            "description": "AKAMAI-ASN1 Akamai International B.V., NL",
            "ip": "2a02:26f0:2780:6::214:f58b",
            "name": "AKAMAI-ASN1 Akamai International B.V.",
            "route": "2a02:26f0:2000::/37"
          },
          "count": null,
          "countries": [
            "NL"
          ],
          "dns": {},
          "domains": [
            "www.example.com"
          ],
          "encodedSize": 3009,
          "geoip": {
            "city": "",
            "country": "NL",
            "country_name": "Netherlands",
            "ll": [
              52.3824,
              4.8995
            ],
            "metro": 0,
            "region": "",
            "timezone": "Europe/Amsterdam"
          },
          "index": 0,
          "ip": "2a02:26f0:2780:6::214:f58b",
          "ipv6": true,
          "redirects": 0,
          "requests": 2,
          "size": 2512
        }
      ],
      "malicious": 0,
      "protocolStats": [
        {
          "count": 2,
          "countries": [
            "NL"
          ],
          "encodedSize": 3009,
          "ips": [
            "2a02:26f0:2780:6::214:f58b"
          ],
          "protocol": "h2",
          "securityState": {},
          "size": 2512
        }
      ],
      "regDomainStats": [
        {
          "count": 2,
          "countries": [],
          "encodedSize": 3009,
          "index": 0,
          "ips": [
            "2a02:26f0:2780:6::214:f58b"
          ],
          "redirects": 0,
          "regDomain": "example.com",
          "size": 2512,
          "subDomains": [
            {
              "country": "NL",
              "domain": "www"
            }
          ]
        }
      ],
      "resourceStats": [
        {
          "compression": "0.9",
          "count": 1,
          "countries": [
            "NL"
          ],
          "encodedSize": 1471,
          "ips": [
            "2a02:26f0:2780:6::214:f58b"
          ],
          "latency": 0,
          "percentage": 50,
          "size": 1256,
          "type": "Other"
        },
        {
          "compression": "0.8",
          "count": 1,
          "countries": [
            "NL"
          ],
          "encodedSize": 1538,
          "ips": [
            "2a02:26f0:2780:6::214:f58b"
          ],
          "latency": 0,
          "percentage": 50,
          "size": 1256,
          "type": "Document"
        }
      ],
      "securePercentage": 100,
      "secureRequests": 2,
      "serverStats": [
        {
          "count": 2,
          "countries": [
            "NL"
          ],
          "encodedSize": 3009,
          "ips": [
            "2a02:26f0:2780:6::214:f58b"
          ],
          "server": "AkamaiNetStorage",
          "size": 2512
        }
      ],
      "tlsStats": [
        {
          "count": 2,
          "countries": [
            "NL"
          ],
          "encodedSize": 3009,
          "ips": [
            "2a02:26f0:2780:6::214:f58b"
          ],
          "protocols": {
            "TLS 1.3 /  / AES_256_GCM": 2
          },
          "securityState": "secure",
          "size": 2512
        }
      ],
      "totalLinks": 1,
      "uniqCountries": 1
    },
    "submitter": {
      "country": "NL"
    },
    "task": {
      "apexDomain": "example.com",
      "domURL": "https://urlscan.io/dom/0195fbfa-84aa-706a-9c7d-e84cfadf0199/",
      "domain": "www.example.com",
      "method": "api",
      "reportURL": "https://urlscan.io/result/0195fbfa-84aa-706a-9c7d-e84cfadf0199/",
      "screenshotURL": "https://urlscan.io/screenshots/0195fbfa-84aa-706a-9c7d-e84cfadf0199.png",
      "source": "7675118b",
      "tags": [],
      "time": "2025-04-03T14:07:40.445Z",
      "url": "https://www.example.com/page.html",
      "uuid": "0195fbfa-84aa-706a-9c7d-e84cfadf0199",
      "visibility": "private"
    },
    "verdicts": {
      "community": {
        "brands": [],
        "categories": [],
        "hasVerdicts": false,
        "malicious": false,
        "score": 0,
        "votesBenign": 0,
        "votesMalicious": 0,
        "votesTotal": 0
      },
      "engines": {
        "benignTotal": 0,
        "benignVerdicts": [],
        "categories": [],
        "enginesTotal": 0,
        "malicious": false,
        "maliciousTotal": 0,
        "maliciousVerdicts": [],
        "score": 0
      },
      "overall": {
        "brands": [],
        "categories": [],
        "hasVerdicts": false,
        "malicious": false,
        "score": 0,
        "tags": []
      },
      "urlscan": {
        "brands": [],
        "categories": [],
        "hasVerdicts": false,
        "malicious": false,
        "score": 0,
        "tags": []
      }
    }
  },
  "report_url": "https://urlscan.io/api/v1/result/0195fbfa-84aa-706a-9c7d-e84cfadf0199/"
}
```

</p>
</details>

<details><summary>Example Function Input Script:</summary>
<p>

```python
# This is an artifact workflow; 
# The URL to scan is the artifact value
inputs.urlscanio_url = artifact.value

# Set the incident id
inputs.incident_id = incident.id
```

</p>
</details>

<details><summary>Example Function Post Process Script:</summary>
<p>

```python
# The result contains,
# {
#   "png_url": the URL of the screenshot image
#   "png_base64content": the base64-encoded screenshot (PNG)
#   "report_url": the URL of the JSON report_url
#   "report": the JSON report, which will contain lots of detail of the page analysis (see urlscan.io for details).
# }
#
# In this case, the file is already attached to the incident.  Nothing to do here.
```

</p>
</details>

---


## Troubleshooting & Support
Refer to the documentation listed in the Requirements section for troubleshooting information.
 
### For Support
This is a IBM Community provided app. Please search the Community [ibm.biz/soarcommunity](https://ibm.biz/soarcommunity) for assistance.
