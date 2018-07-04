# Resilient Function - fn_bigfix_integration

This Resilient Function package can be used to perform the following actions from a workflow using the Functions feature of the Resilient
Circuits integration framework.
```
Run Bigfix query for Resilinet artifacts to determine if there are any hits.
Remediate hits in  Bigfix environment.
Retrieve resource details from Bigfix
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
[fn_bigfix_integration]
bigfix_int_auto_configure=False
bigfix_url=https://bigfix-url.com
bigfix_port=12345
bigfix_user=BigFixAdmin
bigfix_pass=MyPassword
hunt_results_limit=200
polling_period=120
```

Run with: `resilient-circuits run`.

## fn_bigfix_integration Example

The fn_bigfix_integration  function fn_bigfix_artifact requires 4 input parameters. The parameters are setup from a
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
endpoints where hits for the artifact 'hits' have been found.
```
{'endpoint_hits': [{u'computer_id': 13550086, u'failure': False, u'resp_time': 1000,
                    u'query_id': 1, u'result': u'True', u'computer_name': u'DESKTOP-TUKM3HF'
                   }
                  ]
}
```
