

# Validation Report for Microsoft Security Graph Integration for SOAR

| SDK Version       | Generation Time          | Command Line Arguments Provided |
| :---------------- | ------------------------ | ------------------------------- |
| 44.0.2810 | 2022/04/25 08:39:11 | `cmd`: validate, `package`: . |

## App Details
| Attribute | Value |
| --------- | ----- |
| `display_name` | Microsoft Security Graph Integration for SOAR |
| `name` | fn_microsoft_security_graph |
| `version` | 1.2.0 |
| `author` | IBM SOAR |
| `install_requires` | ['resilient_circuits>=40.0.0', 'resilient-lib>=40.0.0'] |
| `description` | Sync alerts from MS Security Graph with IBM SOAR |
| `long_description` | The package contains a polling component and 3 functions.                    The poller queries for alerts to be brought into the SOAR platform as new incidents,                     while the functions allow SOAR users to search the graph, get alert details and update alerts. |
| `url` | https://ibm.com/mysupport |
| `entry_points` | {'resilient.circuits.configsection': '/Users/richardswierk/dev/resilient-community-apps/fn_microsoft_security_graph/fn_microsoft_security_graph/util/config.py',<br> 'resilient.circuits.customize': '/Users/richardswierk/dev/resilient-community-apps/fn_microsoft_security_graph/fn_microsoft_security_graph/util/customize.py',<br> 'resilient.circuits.selftest': '/Users/richardswierk/dev/resilient-community-apps/fn_microsoft_security_graph/fn_microsoft_security_graph/util/selftest.py'} |
| `python_requires` | >=3.6 |
| `SOAR version` | 41.0.6783 |
| `Proxy support` | Proxies not fully supported unless running on AppHost>=1.6 and resilient-circuits>=42.0.0 |

---


## `setup.py` file validation
| Severity | Name | Description | Solution |
| --- | --- | --- | --- |

<span style="color:green">Success</span>


---


## Package files validation

### `app_logo.png`
<span style="color:teal">INFO</span>: `app_logo.png` is the default icon. Consider using your own logo

Icons appear in SOAR when your app is installed with App Host


### `company_logo.png`
<span style="color:teal">INFO</span>: `company_logo.png` is the default icon. Consider using your own logo

Icons appear in SOAR when your app is installed with App Host


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


### LICENSE
<span style="color:green">Pass</span>

 
---
 

## Payload samples validation

### `payload_samples/microsoft_security_graph_alert_search`
<span style="color:green">Pass</span>


### `payload_samples/microsoft_security_graph_get_alert_details`
<span style="color:green">Pass</span>


### `payload_samples/microsoft_security_graph_update_alert`
<span style="color:green">Pass</span>

 
---
 

## `resilient-circuits` selftest

<span style="color:green">Success</span>


---
 

## tox tests
<span style="color:teal">INFO</span>: 4 tests passed!





---
 

## Pylint Scan
<span style="color:teal">INFO</span>: Pylint scan passed with no errors

Run with `-v` to see the full pylint output



---
 

## Bandit Scan
<span style="color:teal">INFO</span>: Bandit scan passed with no issues

Run again with `-v` to see the full bandit output



---
 