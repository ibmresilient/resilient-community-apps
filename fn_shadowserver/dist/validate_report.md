

# Validation Report for Shadow Server Function for IBM SOAR

| SDK Version       | Generation Time          | Command Line Arguments Provided |
| :---------------- | ------------------------ | ------------------------------- |
| 44.0.2810 | 2022/03/25 14:09:18 | `cmd`: validate, `package`: . |

## App Details
| Attribute | Value |
| --------- | ----- |
| `display_name` | Shadow Server Function for IBM SOAR |
| `name` | fn_shadowserver |
| `version` | 1.0.0 |
| `author` | IBM SOAR |
| `install_requires` | ['resilient-circuits>=44.0.0'] |
| `description` | IBM Security SOAR app for ShadowServer |
| `long_description` | Queries ShadowServer to check if the hash provided matches an entry in our database. Returns details on the data source if there is a match. |
| `url` | https://github.com/ibmresilient/fn_shadowserver |
| `entry_points` | {'resilient.circuits.configsection': '/Users/christopherchang/resilient-community-apps/fn_shadowserver/fn_shadowserver/util/config.py',<br> 'resilient.circuits.customize': '/Users/christopherchang/resilient-community-apps/fn_shadowserver/fn_shadowserver/util/customize.py',<br> 'resilient.circuits.selftest': '/Users/christopherchang/resilient-community-apps/fn_shadowserver/fn_shadowserver/util/selftest.py'} |
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


### `app_logo.png`
<span style="color:green">Pass</span>


### LICENSE
<span style="color:green">Pass</span>

 
---
 

## Payload samples validation

### `payload_samples/fn_shadowserver`
<span style="color:green">Pass</span>

 
---
 

## `resilient-circuits` selftest

<span style="color:green">Success</span>


---
 

## tox tests
<span style="color:teal">INFO</span>: 3 tests passed!





---
 

## Pylint Scan
<span style="color:teal">INFO</span>: Pylint scan passed with no errors

Run with `-v` to see the full pylint output



---
 

## Bandit Scan
<span style="color:teal">INFO</span>: Bandit scan passed with no issues

Run again with `-v` to see the full bandit output



---
 