

# Validation Report for SOAR LDAP Utilities

| SDK Version       | Generation Time          | Command Line Arguments Provided |
| :---------------- | ------------------------ | ------------------------------- |
| 44.1.2953 | 2022/04/22 10:50:05 | `cmd`: validate, `package`: . |

## App Details
| Attribute | Value |
| --------- | ----- |
| `display_name` | SOAR LDAP Utilities |
| `name` | fn_ldap_utilities |
| `version` | 1.2.0 |
| `author` | IBM SOAR |
| `install_requires` | ['resilient_circuits>=42.0.0', 'ldap3>=2.0.0'] |
| `description` | SOAR LDAP Utilities' |
| `long_description` | SOAR components to allow reading and manipulation of your LDAP Server' |
| `url` | https://github.com/ibmresilient/resilient-community-apps |
| `entry_points` | {'resilient.circuits.configsection': '/Users/richardswierk/dev/resilient-community-apps/fn_ldap_utilities/fn_ldap_utilities/util/config.py',<br> 'resilient.circuits.customize': '/Users/richardswierk/dev/resilient-community-apps/fn_ldap_utilities/fn_ldap_utilities/util/customize.py',<br> 'resilient.circuits.selftest': '/Users/richardswierk/dev/resilient-community-apps/fn_ldap_utilities/fn_ldap_utilities/util/selftest.py'} |
| `python_requires` | >=3.6 |
| `SOAR version` | 41.0.6783 |
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

### `payload_samples/ldap_utilities_add_to_groups`
<span style="color:green">Pass</span>


### `payload_samples/ldap_utilities_remove_from_groups`
<span style="color:green">Pass</span>


### `payload_samples/ldap_utilities_search`
<span style="color:green">Pass</span>


### `payload_samples/ldap_utilities_set_password`
<span style="color:green">Pass</span>


### `payload_samples/ldap_utilities_toggle_access`
<span style="color:green">Pass</span>


### `payload_samples/ldap_utilities_update`
<span style="color:green">Pass</span>

 
---
 

## `resilient-circuits` selftest

<span style="color:green">Success</span>


---
 

## tox tests
<span style="color:teal">INFO</span>: 15 tests passed!





---
 

## Pylint Scan
<span style="color:teal">INFO</span>: Pylint scan passed with no errors

Run with `-v` to see the full pylint output



---
 

## Bandit Scan
<span style="color:teal">INFO</span>: Bandit scan passed with no issues

Run again with `-v` to see the full bandit output



---
 