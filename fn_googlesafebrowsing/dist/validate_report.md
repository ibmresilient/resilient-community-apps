

# Validation Report for Google Safe Browsing Function for IBM SOAR

| SDK Version       | Generation Time          | Command Line Arguments Provided |
| :---------------- | ------------------------ | ------------------------------- |
| 44.0.2686 | 2022/02/18 16:32:09 | `verbose`: True, `cmd`: validate, `package`: . |

## App Details
| Attribute | Value |
| --------- | ----- |
| `display_name` | Google Safe Browsing Function for IBM SOAR |
| `name` | fn_googlesafebrowsing |
| `version` | 1.0.0 |
| `author` | '' |
| `install_requires` | ['resilient-circuits>=43.0.0'] |
| `description` | IBM Security SOAR app for 'fn_googlesafebrowsing' |
| `long_description` | This app uses Google Safe Browsing to check artifacts with a URL type and adds a hit if the site is potentially unsafe. The hits contains a link to Google Transparency Report that gives information on the potentially unsafe url.' |
| `url` | `https://github.com/resilient/resilient-community-apps` |
| `entry_points` | {'resilient.circuits.configsection': '/Users/MyUser/resilient-community-apps/fn_googlesafebrowsing/fn_googlesafebrowsing/util/config.py',<br> 'resilient.circuits.customize': '/Users/MyUser/resilient-community-apps/fn_googlesafebrowsing/fn_googlesafebrowsing/util/customize.py',<br> 'resilient.circuits.selftest': '/Users/MyUser/resilient-community-apps/fn_googlesafebrowsing/fn_googlesafebrowsing/util/selftest.py'} |
| `python_requires` | >=3.6 |
| `SOAR version` | 43.1.49 |
| `Proxy support` | Proxies supported if running on AppHost>=1.6 |

---


## `setup.py` file validation
| Severity | Name | Description | Solution |
| --- | --- | --- | --- |
| <span style="color:orange">WARNING</span> | invalid value in `setup.py` | `<<your company url>>` is not a valid `url` | Include a valid URL for your organization |


---


## Package files validation

### `README.md`
<span style="color:red">CRITICAL</span>: `README.md` still has at least one instance of `<!-- ::CHANGE_ME:: -->`

Edit the README and make sure to remove all `<!-- ::CHANGE_ME:: -->` comments


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


### LICENSE
<span style="color:green">Pass</span>

 
---
 

## Payload samples validation

### `payload_samples/fn_googlesafebrowsing`
<span style="color:green">Pass</span>

 
---
 

## `resilient-circuits` selftest

<span style="color:green">Success</span>


---
 

## tox tests
<span style="color:teal">INFO</span>: 3 tests passed!





---
 

## Pylint Scan
<span style="color:orange">WARNING</span>: The Pylint score was 7.80/10. Details:

	************* Module fn_googlesafebrowsing.util.selftest
	convention fn_googlesafebrowsing.util.selftest:57:97: Trailing whitespace
	warning fn_googlesafebrowsing.util.selftest:61:11: Catching too general exception Exception
	convention fn_googlesafebrowsing.util.selftest:56:28: Formatting a regular string which could be a f-string
	************* Module fn_googlesafebrowsing
	convention fn_googlesafebrowsing:1:0: Missing module docstring
	************* Module fn_googlesafebrowsing.components.funct_fn_googlesafebrowsing
	convention fn_googlesafebrowsing.components.funct_fn_googlesafebrowsing:70:0: Line too long (128/100)
	refactor fn_googlesafebrowsing.components.funct_fn_googlesafebrowsing:22:8: Consider using Python 3 style super() without arguments
	convention fn_googlesafebrowsing.components.funct_fn_googlesafebrowsing:28:34: Formatting a regular string which could be a f-string
	convention fn_googlesafebrowsing.components.funct_fn_googlesafebrowsing:64:43: Formatting a regular string which could be a f-string
	convention fn_googlesafebrowsing.components.funct_fn_googlesafebrowsing:70:34: Formatting a regular string which could be a f-string
	warning fn_googlesafebrowsing.components.funct_fn_googlesafebrowsing:8:0: Unused IntegrationError imported from resilient_lib
	refactor fn_googlesafebrowsing.components.funct_fn_googlesafebrowsing:1:0: Similar lines in 2 files
	==fn_googlesafebrowsing.components.funct_fn_googlesafebrowsing:[44:57]
	==fn_googlesafebrowsing.util.selftest:[37:50]
	    reqbody = {
	            `client`: {
	                 `clientId`: SB_CLIENT_ID,
	                 `clientVersion`: SB_CLIENT_VER
	            },
	            `threatInfo`: {
	                `threatTypes`: [`THREAT_TYPE_UNSPECIFIED`,
	                             `MALWARE`,
	                             `SOCIAL_ENGINEERING`,
	                             `UNWANTED_SOFTWARE`,
	                             `POTENTIALLY_HARMFUL_APPLICATION`],
	                `platformTypes`: [`ANY_PLATFORM`],
	                `threatEntryTypes`: [`URL`],
	
	------------------------------------------------------------------
	Your code has been rated at 7.80/10 (previous run: 7.60/10, +0.20)
	
	





---
 

## Bandit Scan
<span style="color:teal">INFO</span>: Bandit scan passed with no issues

Run again with `-v` to see the full bandit output



---
 