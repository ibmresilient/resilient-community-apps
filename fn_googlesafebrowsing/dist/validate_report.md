

# Validation Report for `<<display name of your app here>>`

| SDK Version       | Generation Time          | Command Line Arguments Provided |
| :---------------- | ------------------------ | ------------------------------- |
| 44.0.2686 | 2022/02/16 14:19:34 | `cmd`: validate, `package`: . |

## App Details
| Attribute | Value |
| --------- | ----- |
| `display_name` | `<<display name of your app here>>` |
| `name` | fn_googlesafebrowsing |
| `version` | 1.0.0 |
| `author` | `<<your name here>>` |
| `author_email` | you@example.com |
| `install_requires` | ['resilient-circuits>=43.0.0'] |
| `description` | Resilient Circuits Components for 'fn_googlesafebrowsing' |
| `long_description` | Resilient Circuits Components for 'fn_googlesafebrowsing' |
| `url` | `<<your company url>>` |
| `entry_points` | {'resilient.circuits.configsection': '/Users/christopherchang/resilient-community-apps/fn_googlesafebrowsing/fn_googlesafebrowsing/util/config.py',<br> 'resilient.circuits.customize': '/Users/christopherchang/resilient-community-apps/fn_googlesafebrowsing/fn_googlesafebrowsing/util/customize.py',<br> 'resilient.circuits.selftest': '/Users/christopherchang/resilient-community-apps/fn_googlesafebrowsing/fn_googlesafebrowsing/util/selftest.py'} |
| `python_requires` | >=3.6 |
| `SOAR version` | 43.1.49 |
| `Proxy support` | Proxies supported if running on AppHost>=1.6 |

---


## `setup.py` file validation
| Severity | Name | Description | Solution |
| --- | --- | --- | --- |
| <span style="color:red">CRITICAL</span> | invalid value in `setup.py` | `setup.py` attribute `license` remains unchanged from the default value `<<insert here>>` | Set `license` to an valid license. |
| <span style="color:red">CRITICAL</span> | invalid value in `setup.py` | `setup.py` attribute `author` remains unchanged from the default value `<<your name here>>` | Set `author` to the name of the author |
| <span style="color:red">CRITICAL</span> | invalid value in `setup.py` | `setup.py` attribute `author_email` remains unchanged from the default value `you@example.com` | Set `author_email` to the author`s contact email |
| <span style="color:orange">WARNING</span> | invalid value in `setup.py` | `setup.py` attribute `display_name` remains unchanged from the default value `<<display name of your app here>>` | Set `display_name` to an appropriate value. This value is displayed when the app is installed |
| <span style="color:orange">WARNING</span> | invalid value in `setup.py` | `<<your company url>>` is not a valid `url` | Include a valid URL for your organization |
| <span style="color:orange">WARNING</span> | invalid value in `setup.py` | `setup.py` attribute `description` remains unchanged from the default value `Resilient Circuits Components...` | Enter text that describes the app in `description`. This will be displayed when the app is installed |
| <span style="color:orange">WARNING</span> | invalid value in `setup.py` | `setup.py` attribute `long_description` remains unchanged from the default value `Resilient Circuits Components...` | Enter text that describes the app in `long_description`. This will be displayed when the app is installed |


---


## Package files validation

### `README.md`
<span style="color:red">CRITICAL</span>: `README.md` is still the `codegen` template

Be sure that you run ```resilient-sdk docgen -p /Users/christopherchang/resilient-community-apps/fn_googlesafebrowsing``` when you are done developing


### LICENSE
<span style="color:red">CRITICAL</span>: `LICENSE` is the default license file

Provide a `LICENSE` file in your package directory. Suggested formats: MIT, Apache, and BSD


### `app_logo.png`
<span style="color:teal">INFO</span>: `app_logo.png` is the default icon. Consider using your own logo

Icons appear in SOAR when your app is installed with App Host


### `company_logo.png`
<span style="color:teal">INFO</span>: `company_logo.png` is the default icon. Consider using your own logo

Icons appear in SOAR when your app is installed with App Host


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

 
---
 

## Payload samples validation

### `payload_samples/fn_googlesafebrowsing`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `fn_googlesafebrowsing` empty

Fill in values manually or by using ```resilient-sdk codegen -p /Users/christopherchang/resilient-community-apps/fn_googlesafebrowsing --gather-samples```

 
---
 

## `resilient-circuits` selftest
<span style="color:red">CRITICAL</span>: While running selftest.py, `resilient-circuits` failed to connect to server. Details:

	...
	2022-02-16 14:19:09,888 DEBUG [actions_component] num_workers set to 10
	2022-02-16 14:19:09,892 INFO [app] Components auto-load directory: (none)
	2022-02-16 14:19:10,044 DEBUG [decorators] @function <function FunctionComponent._clamav_scan_stream_function at 0x10c3032f0>
	2022-02-16 14:19:10,050 ERROR [component_loader] Failed to load `FunctFnAbuseipdbFunctionComponent = fn_abuseipdb.components.funct_fn_abuseipdb:FunctionComponent` from `fn-abuseipdb 1.0.0`
	
	ERROR: could not connect to SOAR at `9.30.44.45`.
	Reason: Unknown STOMP Error: No module named `fn_abuseipdb.components.funct_fn_abuseipdb`
	Error Code: 30




---
 

## tox tests
<span style="color:red">CRITICAL</span>: 2 tests failed. Details:

	self = <test_funct_fn_googlesafebrowsing.TestFnGooglesafebrowsing object at 0x10b076f28>
	circuits_app = <pytest_resilient_circuits.resilient_circuits_fixtures.ResilientCircuits object at 0x10bedc898>
	mock_inputs = {}, expected_results = {`value`: `xyz`}
	
	    @pytest.mark.parametrize("mock_inputs, expected_results", [
	        (mock_inputs_1, expected_results_1),
	        (mock_inputs_2, expected_results_2)
	    ])
	    def test_success(self, circuits_app, mock_inputs, expected_results):
	        """ Test calling with sample values for the parameters """
	    
	>       results = call_fn_googlesafebrowsing_function(circuits_app, mock_inputs)
	
	tests/test_funct_fn_googlesafebrowsing.py:67: 
	_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
	tests/test_funct_fn_googlesafebrowsing.py:31: in call_fn_googlesafebrowsing_function
	    raise exception
	.tox/py36/lib/python3.6/site-packages/circuits/core/manager.py:874: in processTask
	    raise value.extract()
	.tox/py36/lib/python3.6/site-packages/resilient_circuits/actions_component.py:80: in _on_task
	    yield result.get()
	../../.pyenv/versions/3.6.12/lib/python3.6/multiprocessing/pool.py:644: in get
	    raise self._value
	../../.pyenv/versions/3.6.12/lib/python3.6/multiprocessing/pool.py:119: in worker
	    result = (True, func(*args, **kwds))
	.tox/py36/lib/python3.6/site-packages/resilient_circuits/decorators.py:274: in _invoke_app_function
	    for r in fn_results:
	_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
	
	self = <FunctionComponent/* 6001:MainThread (queued=0) [S]>
	fn_inputs = fn_inputs()
	
	    @app_function(FN_NAME)
	    def lookup_urls(self, fn_inputs):
	        """
	        Utility class to access the Google Safe Browsing Lookup API
	        https://developers.google.com/safe-browsing/v4/get-started
	        >>> sb = SafeBrowsingAPI(os.environ.get("SAFEBROWSING_API_KEY"))
	        # {u`matches`: [{u`threatType`: u`SOCIAL_ENGINEERING`, u`threatEntryType`: u`URL`, u`platformType`: u`ANY_PLATFORM`, u`threat`: {u`url`: u`ihaveaproblem.info`}, u`cacheDuration`: u`300s`}]}
	        >>> result = sb.lookup_urls("ihaveaproblem.info")
	        >>> len(result["matches"]) > 0
	        True
	        """
	    
	        yield self.status_message("Starting App Function: `{0}`".format(FN_NAME))
	    
	>       artifact_type = fn_inputs.abuseipdb_artifact_type
	E       AttributeError: `fn_inputs` object has no attribute `abuseipdb_artifact_type`
	
	.tox/py36/lib/python3.6/site-packages/fn_googlesafebrowsing/components/funct_fn_googlesafebrowsing.py:42: AttributeError
	
	---
	
	self = <test_funct_fn_googlesafebrowsing.TestFnGooglesafebrowsing object at 0x10c9d2c18>
	circuits_app = <pytest_resilient_circuits.resilient_circuits_fixtures.ResilientCircuits object at 0x10bedc898>
	mock_inputs = {}, expected_results = {`value`: `xyz`}
	
	    @pytest.mark.parametrize("mock_inputs, expected_results", [
	        (mock_inputs_1, expected_results_1),
	        (mock_inputs_2, expected_results_2)
	    ])
	    def test_success(self, circuits_app, mock_inputs, expected_results):
	        """ Test calling with sample values for the parameters """
	    
	>       results = call_fn_googlesafebrowsing_function(circuits_app, mock_inputs)
	
	tests/test_funct_fn_googlesafebrowsing.py:67: 
	_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
	tests/test_funct_fn_googlesafebrowsing.py:31: in call_fn_googlesafebrowsing_function
	    raise exception
	.tox/py36/lib/python3.6/site-packages/circuits/core/manager.py:874: in processTask
	    raise value.extract()
	.tox/py36/lib/python3.6/site-packages/resilient_circuits/actions_component.py:80: in _on_task
	    yield result.get()
	../../.pyenv/versions/3.6.12/lib/python3.6/multiprocessing/pool.py:644: in get
	    raise self._value
	../../.pyenv/versions/3.6.12/lib/python3.6/multiprocessing/pool.py:119: in worker
	    result = (True, func(*args, **kwds))
	.tox/py36/lib/python3.6/site-packages/resilient_circuits/decorators.py:274: in _invoke_app_function
	    for r in fn_results:
	_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
	
	self = <FunctionComponent/* 6001:MainThread (queued=0) [S]>
	fn_inputs = fn_inputs()
	
	    @app_function(FN_NAME)
	    def lookup_urls(self, fn_inputs):
	        """
	        Utility class to access the Google Safe Browsing Lookup API
	        https://developers.google.com/safe-browsing/v4/get-started
	        >>> sb = SafeBrowsingAPI(os.environ.get("SAFEBROWSING_API_KEY"))
	        # {u`matches`: [{u`threatType`: u`SOCIAL_ENGINEERING`, u`threatEntryType`: u`URL`, u`platformType`: u`ANY_PLATFORM`, u`threat`: {u`url`: u`ihaveaproblem.info`}, u`cacheDuration`: u`300s`}]}
	        >>> result = sb.lookup_urls("ihaveaproblem.info")
	        >>> len(result["matches"]) > 0
	        True
	        """
	    
	        yield self.status_message("Starting App Function: `{0}`".format(FN_NAME))
	    
	>       artifact_type = fn_inputs.abuseipdb_artifact_type
	E       AttributeError: `fn_inputs` object has no attribute `abuseipdb_artifact_type`
	
	.tox/py36/lib/python3.6/site-packages/fn_googlesafebrowsing/components/funct_fn_googlesafebrowsing.py:42: AttributeError
	
	---
	
	


Run with the `-v` flag to see more information



---
 

## Pylint Scan
<span style="color:red">CRITICAL</span>: The Pylint score was 8.96/10. Details:

	************* Module fn_googlesafebrowsing.components.funct_fn_googlesafebrowsing
	error fn_googlesafebrowsing.components.funct_fn_googlesafebrowsing:80:19: Instance of `RequestsCommon` has no `execture` member
	
	-----------------------------------
	Your code has been rated at 8.96/10
	
	

Run with `-v` to see the full pylint output



---
 

## Bandit Scan
<span style="color:teal">INFO</span>: Bandit scan passed with no issues

Run again with `-v` to see the full bandit output



---
 