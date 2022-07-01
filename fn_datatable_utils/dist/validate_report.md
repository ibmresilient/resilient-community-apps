

# Validation Report for Datatable Utilities

| SDK Version       | Generation Time          | Command Line Arguments Provided |
| :---------------- | ------------------------ | ------------------------------- |
| 44.1.2953 | 2022/05/31 14:09:06 | `cmd`: validate, `package`: . |

## App Details
| Attribute | Value |
| --------- | ----- |
| `display_name` | Datatable Utilities |
| `name` | fn_datatable_utils |
| `version` | 2.0.0 |
| `author` | IBM SOAR |
| `install_requires` | ['resilient_circuits>=41.0.0', 'resilient-lib>=41.0.0'] |
| `description` | Functions manipulate data in a Datatable |
| `long_description` | This package contains 6 functions that help you manipulate IBM SOAR Data Tables: Get Row,  Get Rows, Update Row, Delete Row, Delete Rows and Convert CSV Data to a datatable. |
| `url` | http://ibm.biz/soarcommunity |
| `entry_points` | {'resilient.circuits.configsection': '/Users/richardswierk/dev/resilient-community-apps/fn_datatable_utils/fn_datatable_utils/util/config.py',<br> 'resilient.circuits.customize': '/Users/richardswierk/dev/resilient-community-apps/fn_datatable_utils/fn_datatable_utils/util/customize.py',<br> 'resilient.circuits.selftest': '/Users/richardswierk/dev/resilient-community-apps/fn_datatable_utils/fn_datatable_utils/util/selftest.py'} |
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

### ``config.py``
<span style="color:teal">INFO</span>: `config.py` does not return a string value

The `config.py` file defines the contents of the app.config settings for your app


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

### `payload_samples/dt_utils_add_row`
<span style="color:green">Pass</span>


### `payload_samples/dt_utils_clear_datatable`
<span style="color:green">Pass</span>


### `payload_samples/dt_utils_create_csv_table`
<span style="color:green">Pass</span>


### `payload_samples/dt_utils_delete_row`
<span style="color:green">Pass</span>


### `payload_samples/dt_utils_delete_rows`
<span style="color:green">Pass</span>


### `payload_samples/dt_utils_get_all_data_table_rows`
<span style="color:green">Pass</span>


### `payload_samples/dt_utils_get_row`
<span style="color:green">Pass</span>


### `payload_samples/dt_utils_get_rows`
<span style="color:green">Pass</span>


### `payload_samples/dt_utils_update_row`
<span style="color:green">Pass</span>

 
---
 

## `resilient-circuits` selftest

<span style="color:green">Success</span>


---
 

## tox tests
<span style="color:teal">INFO</span>: 38 tests passed!





---
 

## Pylint Scan
<span style="color:teal">INFO</span>: Pylint scan passed with no errors

Run with `-v` to see the full pylint output



---
 

## Bandit Scan
<span style="color:teal">INFO</span>: Bandit scan passed with no issues

Run again with `-v` to see the full bandit output



---
 