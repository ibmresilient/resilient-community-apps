# Resilient Function - fn_bigfix

This Resilient Function package can be used to perform the following actions from a workflow using the Functions feature of the Resilient
Circuits integration framework.
```
Run Bigfix query for Resilient artifacts to determine if there are any hits.
Retrieve properties of an endpoint, with hits, from Bigfix.
Remediate hits in Bigfix environment.
Update status of a Bigfix remediating action.
```

Prerequisites:
```
resilient version 30 or later
resilient_circuits version 30 or later
```
* For more info about BigFix, please visit https://www.ibm.com/support/knowledgecenter/en/SSQL82_9.5.0/com.ibm.bigfix.doc/welcome/BigFix_Platform_welcome.html


## Environment

This package requires that it is installed on a RHEL platform and that the resilient-circuits application is running.
Install this package with 'pip', or `python setup.py install`.
To set the config values in the app.config file run `resilient-circuits config -u`.

Config values example:
```
[fn_bigfix]
bigfix_int_auto_configure=False
bigfix_url=https://bigfix-url.com
bigfix_port=12345
bigfix_user=BigFixAdmin
bigfix_pass=MyPassword
bigfix_polling_interval=30
bigfix_polling_timeout=1800
hunt_results_limit=200
```

Run with: `resilient-circuits run`.

## fn_bigfix Example

The fn_bigfix function fn_bigfix_artifact requires 7 input parameters. The parameters are setup from a
Resilient systems workflow on the Resilient console.
The following are examples of setup of each parameter using a simple workflow pre-processing script.

```
inputs.bigfix_artifact_id =  120
inputs.bigfix_artifact_value = "HKLM\SOFTWARE\TEST\TEST\com.tst.browsercore"
inputs.bigfix_artifact_type = "Registry Key"
inputs.bigfix_artifact_properties_name = "TESTKEY"
inputs.bigfix_artifact_properties_value = "TESTVAL"
inputs.bigfix_incident_id = 2095
inputs.bigfix_incident_plan_status = "A"
```
The results returned to Resilient will be in JSON format and will consist of a list of
endpoints where hits for the artifact have been found.
```
{'hits_count': 1,
 'endpoint_hits': [{u'computer_id': 13550086, u'failure': False, u'resp_time': 0, u'query_id': 1,
                    u'result': u'True', u'computer_name': u'DESKTOP-TUKM3HF'}]
 'query_execution_date': '07-17-2018 17:44:21'
}
```
