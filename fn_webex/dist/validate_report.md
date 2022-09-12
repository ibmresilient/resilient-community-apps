

# Validation Report for Cisco Webex

| SDK Version       | Generation Time          | Command Line Arguments Provided |
| :---------------- | ------------------------ | ------------------------------- |
| 45.0.3150 | 2022/09/12 13:59:08 | `cmd`: validate, `package`: fn_webex |

## App Details
| Attribute | Value |
| --------- | ----- |
| `display_name` | Cisco Webex |
| `name` | fn_webex |
| `version` | 2.0.0 |
| `author` | IBM SOAR |
| `install_requires` | ['resilient-circuits>=45.0.0'] |
| `description` | This package extends the meeting and collaboration functionality of Webex to IBM Security QRadar SOAR Platform  |
| `long_description` | This package provides SOAR platform with the ability to interface with Cisco Webex and create rooms teams and meetings.    The user now can create Meeitngs, Rooms and teams from within a SOAR incident and assign its members to it. |
| `url` | http://ibm.biz/soarcommunity |
| `entry_points` | {'resilient.circuits.configsection': '/Users/calvinwynne/Development/resilient-community-apps/fn_webex/fn_webex/util/config.py',<br> 'resilient.circuits.customize': '/Users/calvinwynne/Development/resilient-community-apps/fn_webex/fn_webex/util/customize.py',<br> 'resilient.circuits.selftest': '/Users/calvinwynne/Development/resilient-community-apps/fn_webex/fn_webex/util/selftest.py'} |
| `python_requires` | >=3.6 |
| `SOAR version` | 43.1.49 |
| `Proxy support` | Proxies supported if running on AppHost>=1.6 |

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

### `payload_samples/webex_delete_teamsrooms`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `webex_delete_teamsrooms` empty

Fill in values manually or by using ```resilient-sdk codegen -p /Users/calvinwynne/Development/resilient-community-apps/fn_webex --gather-results```


### `payload_samples/webex_create_meeting`
<span style="color:green">Pass</span>


### `payload_samples/webex_create_room`
<span style="color:green">Pass</span>


### `payload_samples/webex_create_team`
<span style="color:green">Pass</span>

 
---
 

## `resilient-circuits` selftest

<span style="color:green">Success</span>


---
 

## tox tests
<span style="color:teal">INFO</span>: 17 tests passed!





---
 

## Pylint Scan
<span style="color:teal">INFO</span>: Pylint scan passed with no errors

Run with `-v` to see the full pylint output



---
 

## Bandit Scan
<span style="color:teal">INFO</span>: Bandit scan passed with no issues

Run again with `-v` to see the full bandit output



---
 