

# Validation Report for Splunk Integration for SOAR

| SDK Version       | Generation Time          | Command Line Arguments Provided |
| :---------------- | ------------------------ | ------------------------------- |
| 44.1.2953 | 2022/05/10 10:48:32 | `cmd`: validate, `package`: . |

## App Details
| Attribute | Value |
| --------- | ----- |
| `display_name` | Splunk Integration for SOAR |
| `name` | fn_splunk_integration |
| `version` | 1.2.0 |
| `author` | IBM SOAR |
| `install_requires` | ['resilient_circuits>=40.0.0', 'resilient_lib', 'splunk-sdk'] |
| `description` | Add, Search and Delete artifacts to Splunk ES |
| `long_description` | Several functions to operate with Splunk ES intel collections, including updates to SplunkES notable events and add, search and delete operations to intel collections based on artifact type values. |
| `url` | https://github.com/ibmresilient/resilient-community-apps |
| `entry_points` | {'resilient.circuits.configsection': '/Users/richardswierk/dev/resilient-community-apps/fn_splunk_integration/fn_splunk_integration/util/config.py',<br> 'resilient.circuits.customize': '/Users/richardswierk/dev/resilient-community-apps/fn_splunk_integration/fn_splunk_integration/util/customize.py',<br> 'resilient.circuits.selftest': '/Users/richardswierk/dev/resilient-community-apps/fn_splunk_integration/fn_splunk_integration/util/selftest.py'} |
| `python_requires` | >=3.6 |
| `SOAR version` | 42.0.7058 |
| `Proxy support` | Proxies not fully supported unless running on AppHost>=1.6 and resilient-circuits>=42.0.0 |

---


## `setup.py` file validation
| Severity | Name | Description | Solution |
| --- | --- | --- | --- |

<span style="color:green">Success</span>


---


## Package files validation

### LICENSE
<span style="color:teal">INFO</span>: `LICENSE` file is valid

It is recommended to manually validate the license. Suggested formats: MIT, Apache, and BSD


### `MANIFEST.in`
<span style="color:green">Pass</span>


### `apikey_permissions.txt`
<span style="color:green">Pass</span>


### `Dockerfile`
<span style="color:green">Pass</span>


### `entrypoint.sh`
<span style="color:green">Pass</span>


### ``config.py``
<span style="color:green">Pass</span>


### ``customize.py``
<span style="color:green">Pass</span>


### `README.md`
<span style="color:green">Pass</span>


### `app_logo.png`
<span style="color:green">Pass</span>


### `company_logo.png`
<span style="color:green">Pass</span>


### LICENSE
<span style="color:green">Pass</span>

 
---
 

## Payload samples validation

### `payload_samples/splunk_add_intel_item`
<span style="color:green">Pass</span>


### `payload_samples/splunk_delete_threat_intel_item`
<span style="color:green">Pass</span>


### `payload_samples/splunk_search`
<span style="color:green">Pass</span>


### `payload_samples/splunk_update_notable`
<span style="color:green">Pass</span>

 
---
 

## `resilient-circuits` selftest

<span style="color:green">Success</span>


---
 

## tox tests
<span style="color:teal">INFO</span>: 20 tests passed!





---
 

## Pylint Scan
<span style="color:teal">INFO</span>: Pylint scan passed with no errors

Run with `-v` to see the full pylint output



---
 

## Bandit Scan
<span style="color:teal">INFO</span>: Bandit scan passed with no issues

Run again with `-v` to see the full bandit output



---
 