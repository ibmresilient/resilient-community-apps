

# Validation Report for Symantec DLP

| SDK Version       | Generation Time          | Command Line Arguments Provided |
| :---------------- | ------------------------ | ------------------------------- |
| 44.0.2810 | 2022/03/31 12:54:14 | `cmd`: validate, `package`: fn_symantec_dlp |

## App Details
| Attribute | Value |
| --------- | ----- |
| `display_name` | Symantec DLP |
| `name` | fn_symantec_dlp |
| `version` | 2.0.0 |
| `author` | IBM SOAR |
| `install_requires` | ['resilient_circuits>=43.0.0'] |
| `description` | IBM QRadar SOAR app for Symantec DLP |
| `long_description` | This app allows bi-directional synchronization between IBM SOAR and Symantec DLP.    Symantec DLP incidents are escalated to IBM SOAR as cases with the creation of artifacts and notes in SOAR from the incident. |
| `url` | https://ibm.com/mysupport |
| `entry_points` | {'resilient.circuits.configsection': '/Users/annmarienorcross/resilient-community-apps/fn_symantec_dlp/fn_symantec_dlp/util/config.py',<br> 'resilient.circuits.customize': '/Users/annmarienorcross/resilient-community-apps/fn_symantec_dlp/fn_symantec_dlp/util/customize.py',<br> 'resilient.circuits.selftest': '/Users/annmarienorcross/resilient-community-apps/fn_symantec_dlp/fn_symantec_dlp/util/selftest.py'} |
| `SOAR version` | 42.0.7058 |
| `Proxy support` | Proxies supported if running on AppHost>=1.6 |

---


## `setup.py` file validation
| Severity | Name | Description | Solution |
| --- | --- | --- | --- |

<span style="color:green">Success</span>


---


## Package files validation

### `Dockerfile`
<span style="color:orange">WARNING</span>: `Dockerfile` does not match the template file (97% match). Difference from template:

```diff
--- Dockerfile template
+++ Dockerfile
@@ -4 +4 @@
-FROM registry.access.redhat.com/ubi8/python-39:latest
+FROM registry.access.redhat.com/ubi8/python-36:latest
@@ -7 +7 @@
-ARG RESILIENT_CIRCUITS_VERSION=44.0.0
+ARG RESILIENT_CIRCUITS_VERSION=43.0.0
```

Ensure that the `Dockerfile` was generated with the latest version of the resilient-sdk...


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

### `payload_samples/symantec_dlp_close_dlp_case`
<span style="color:green">Pass</span>


### `payload_samples/symantec_dlp_get_incident_details`
<span style="color:green">Pass</span>


### `payload_samples/symantec_dlp_get_notes`
<span style="color:green">Pass</span>


### `payload_samples/symantec_dlp_send_note_to_dlp_incident`
<span style="color:green">Pass</span>


### `payload_samples/symantec_dlp_update_incident_status`
<span style="color:green">Pass</span>


### `payload_samples/symantec_dlp_upload_binaries`
<span style="color:green">Pass</span>

 
---
 

## `resilient-circuits` selftest

<span style="color:green">Success</span>


---
 

## tox tests
<span style="color:teal">INFO</span>: 1 tests passed!





---
 

## Pylint Scan
<span style="color:red">CRITICAL</span>: The Pylint score was 9.85/10. Details:

	************* Module fn_symantec_dlp.lib.dlp_common
	error fn_symantec_dlp.lib.dlp_common:456:19: Using variable `path_tmp_dir` before assignment
	************* Module fn_symantec_dlp.components.dlp_poller
	error fn_symantec_dlp.components.dlp_poller:52:39: Using variable `poller_start` before assignment
	
	------------------------------------------------------------------
	Your code has been rated at 9.85/10 (previous run: 9.85/10, +0.00)
	
	

Run with `-v` to see the full pylint output



---
 

## Bandit Scan
<span style="color:teal">INFO</span>: Bandit scan passed with no issues

Run again with `-v` to see the full bandit output



---
 