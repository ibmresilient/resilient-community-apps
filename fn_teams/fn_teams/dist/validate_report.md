

# Validation Report for Microsoft Teams

| SDK Version       | Generation Time          | Command Line Arguments Provided |
| :---------------- | ------------------------ | ------------------------------- |
| 45.0.3150 | 2022/11/01 11:51:42 | `cmd`: validate, `settings`: /Users/calvinwynne/.resilient/.sdk_settings.json, `package`: fn_teams |

## App Details
| Attribute | Value |
| --------- | ----- |
| `display_name` | Microsoft Teams |
| `name` | fn_teams |
| `version` | 2.0.0 |
| `author` | IBM SOAR |
| `install_requires` | ['resilient_circuits>=45.0.0', "pymsteams ~= 0.2.1;python_version>='3.6'", "msal ~= 1.19;python_version>='3.6'"] |
| `description` | This app extends the collaboration functionality of Microsoft Teams to IBM Security QRadar SOAR Platform |
| `long_description` | This app provides SOAR platform with the ability to interface with Microsoft Teams and create groups and channels.    Included are example workflows and rules for pushing incident and task information to a Teams channel and to create a group and channel from    within an incident or task |
| `url` | https://ibm.biz/soarcommunity |
| `entry_points` | {'resilient.circuits.configsection': '/Users/calvinwynne/Development/resilient-community-apps/fn_teams/fn_teams/util/config.py',<br> 'resilient.circuits.customize': '/Users/calvinwynne/Development/resilient-community-apps/fn_teams/fn_teams/util/customize.py',<br> 'resilient.circuits.selftest': '/Users/calvinwynne/Development/resilient-community-apps/fn_teams/fn_teams/util/selftest.py'} |
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

### `payload_samples/teams_post_message`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `teams_post_message` empty

Fill in values manually or by using ```resilient-sdk codegen -p /Users/calvinwynne/Development/resilient-community-apps/fn_teams --gather-results```


### `payload_samples/ms_teams_create_group`
<span style="color:green">Pass</span>

 
---
 

## `resilient-circuits` selftest

<span style="color:green">Success</span>


---
 

## tox tests
<span style="color:teal">INFO</span>: 14 tests passed!





---
 

## Pylint Scan
<span style="color:teal">INFO</span>: Pylint scan passed with no errors

Run with `-v` to see the full pylint output



---
 

## Bandit Scan
<span style="color:teal">INFO</span>: Bandit scan passed with no issues

Run again with `-v` to see the full bandit output



---
 