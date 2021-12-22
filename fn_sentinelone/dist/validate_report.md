

# Validation Report for SentinelOne

| SDK Version       | Generation Time          | Command Line Arguments Provided |
| :---------------- | ------------------------ | ------------------------------- |
| 43.1.2571 | 2021/12/22 11:59:23 | `cmd`: validate, `package`: fn_sentinelone |

## App Details
| Attribute | Value |
| --------- | ----- |
| `display_name` | SentinelOne |
| `name` | fn_sentinelone |
| `version` | 1.0.0 |
| `author` | IBM Resilient |
| `install_requires` | ['resilient-circuits>=40.0.0', 'resilient-lib', 'jinja2'] |
| `description` | IBM Security SOAR app for SentinelOne |
| `long_description` | This app allows bi-directional synchronization between IBM SOAR and SentinelOne.    SentinelOne threats are escalated to IBM SOAR as cases with the creation of artifacts and notes in SOAR from the threat. |
| `url` | https://github.com/ibmresilient/fn_sentinelone |
| `entry_points` | {'resilient.circuits.configsection': '/Users/annmarienorcross/resilient-community-apps/fn_sentinelone/fn_sentinelone/util/config.py',<br> 'resilient.circuits.customize': '/Users/annmarienorcross/resilient-community-apps/fn_sentinelone/fn_sentinelone/util/customize.py',<br> 'resilient.circuits.selftest': '/Users/annmarienorcross/resilient-community-apps/fn_sentinelone/fn_sentinelone/util/selftest.py'} |
| `python_requires` | >=3.6 |
| `SOAR version` | 40.2.81 |
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

### `payload_samples/sentinelone_abort_disk_scan`
<span style="color:green">Pass</span>


### `payload_samples/sentinelone_connect_to_network`
<span style="color:green">Pass</span>


### `payload_samples/sentinelone_disconnect_from_network`
<span style="color:green">Pass</span>


### `payload_samples/sentinelone_get_agent_details`
<span style="color:green">Pass</span>


### `payload_samples/sentinelone_get_hash_reputation`
<span style="color:green">Pass</span>


### `payload_samples/sentinelone_get_threat_details`
<span style="color:green">Pass</span>


### `payload_samples/sentinelone_initiate_disk_scan`
<span style="color:green">Pass</span>


### `payload_samples/sentinelone_resolve_threat_in_sentinelone`
<span style="color:green">Pass</span>


### `payload_samples/sentinelone_restart_agent`
<span style="color:green">Pass</span>


### `payload_samples/sentinelone_send_soar_note_to_sentinelone`
<span style="color:green">Pass</span>


### `payload_samples/sentinelone_shutdown_agent`
<span style="color:green">Pass</span>


### `payload_samples/sentinelone_update_notes_from_sentinelone`
<span style="color:green">Pass</span>


### `payload_samples/sentinelone_update_threat_status`
<span style="color:green">Pass</span>

 
---
 

## `resilient-circuits` selftest

<span style="color:green">Success</span>


---
 

## tox tests
<span style="color:teal">INFO</span>: `tox` is not installed in your Python environment

(OPTIONAL) If you want to verify any tests you have written, install `tox` by running ```pip install -U tox```



---
 

## Pylint Scan
<span style="color:teal">INFO</span>: Pylint scan passed with no errors

Run with `-v` to see full pylint output



---
 

## Bandit Scan
<span style="color:teal">INFO</span>: Bandit scan passed with no issues

Run again with `-v` to see full bandit output



---
 