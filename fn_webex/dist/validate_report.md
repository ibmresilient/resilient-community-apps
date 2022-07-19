

# Validation Report for Cisco Webex

| SDK Version       | Generation Time          | Command Line Arguments Provided |
| :---------------- | ------------------------ | ------------------------------- |
| 45.0.3150 | 2022/07/19 13:27:33 | `cmd`: validate, `package`: fn_webex |

## App Details
| Attribute | Value |
| --------- | ----- |
| `display_name` | Cisco Webex |
| `name` | fn_webex |
| `version` | 2.0.0 |
| `author` | IBM SOAR |
| `install_requires` | ['resilient-circuits>=45.0.0'] |
| `description` | Resilient Circuits Components for 'fn_webex' |
| `long_description` | Resilient Circuits Components for 'fn_webex' |
| `url` | http://ibm.biz/soarcommunity |
| `entry_points` | {'resilient.circuits.configsection': '/Users/calvinwynne/Development/resilient-community-apps/fn_webex/fn_webex/util/config.py',<br> 'resilient.circuits.customize': '/Users/calvinwynne/Development/resilient-community-apps/fn_webex/fn_webex/util/customize.py',<br> 'resilient.circuits.selftest': '/Users/calvinwynne/Development/resilient-community-apps/fn_webex/fn_webex/util/selftest.py'} |
| `python_requires` | >=3.6 |
| `SOAR version` | 43.1.49 |
| `Proxy support` | Proxies supported if running on AppHost>=1.6 |

---


## `setup.py` file validation
| Severity | Name | Description | Solution |
| --- | --- | --- | --- |
| <span style="color:orange">WARNING</span> | invalid value in `setup.py` | `setup.py` attribute `description` remains unchanged from the default value `Resilient Circuits Components...` | Enter text that describes the app in `description`. This will be displayed when the app is installed |
| <span style="color:orange">WARNING</span> | invalid value in `setup.py` | `setup.py` attribute `long_description` remains unchanged from the default value `Resilient Circuits Components...` | Enter text that describes the app in `long_description`. This will be displayed when the app is installed |


---


## Package files validation

### `README.md`
<span style="color:red">CRITICAL</span>: `README.md` still has at least one instance of `<!-- ::CHANGE_ME:: -->`

Edit the README and make sure to remove all `<!-- ::CHANGE_ME:: -->` comments


### `README.md`
<span style="color:red">CRITICAL</span>: Cannot find one or more screenshots referenced in the README: [`./doc/screenshots/fn-create-webex-meeting.png`]

Make sure all screenshots referenced in the README are placed in the /doc/screenshots folder


### `Dockerfile`
<span style="color:orange">WARNING</span>: `Dockerfile` does not match the template file (99% match). Difference from template:

```diff
--- Dockerfile template
+++ Dockerfile
@@ -1 +1 @@
-# docker build -t ibmresilient/fn_webex:2.0.0 -t ibmresilient/fn_webex:latest .
+# docker build -t ibmresilient/fn_webex:1.0.0 -t ibmresilient/fn_webex:latest .
```

Ensure that the `Dockerfile` was generated with the latest version of the resilient-sdk...


### ``config.py``
<span style="color:teal">INFO</span>: `config.py` does not return a string value

The `config.py` file defines the contents of the app.config settings for your app


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


### ``customize.py``
<span style="color:green">Pass</span>


### LICENSE
<span style="color:green">Pass</span>

 
---
 

## Payload samples validation

### `payload_samples/fn_create_meeting`
<span style="color:green">Pass</span>

 
---
 

## `resilient-circuits` selftest
<span style="color:red">CRITICAL</span>: While running selftest.py, `resilient-circuits` failed to connect to server. Details:

	...
	
	- WARNING: No certificate file specified. Only allows the connections that are trusted by operating system.
	- Checking if we can authenticate a REST connection with `e14b8f3e-6652-408c-8abf-448093f7f4ea` to `doctor1.fyre.ibm.com`
	Unverified HTTPS requests (cafile=false).
	
	ERROR: could not connect to SOAR at `doctor1.fyre.ibm.com`.
	Reason: HTTPSConnectionPool(host=`doctor1.fyre.ibm.com`, port=443): Max retries exceeded with url: /rest/session (Caused by NewConnectionError(`<urllib3.connection.HTTPSConnection object at 0x104bb7630>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known`,))
	Error Code: 20




---
 

## tox tests
<span style="color:teal">INFO</span>: 11 tests passed!





---
 

## Pylint Scan
<span style="color:teal">INFO</span>: Pylint scan passed with no errors

Run with `-v` to see the full pylint output



---
 

## Bandit Scan
<span style="color:teal">INFO</span>: Bandit scan passed with no issues

Run again with `-v` to see the full bandit output



---
 