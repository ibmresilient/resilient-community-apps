# Resilient Function - PagerDuty Integration

This Resilient Functions package provides integration with PagerDuty for:
* Incident Creation
* Incident Transitions
* Note Creation

Prerequisites
```
resilient-circuits >=v30.0.0
```

## Environment
To install in "development mode", run 
    `pip install -e ./fn_pagerduty/`
    
The distribution file can be installed using
    `pip install fn_pagerduty-<version>.tar.gz`
    
Import the package into Resilient by running `resilient-circuits customize`

To configure the PagerDuty parameters, run `resilient-circuits config [-u | -c]`. 
Then edit the `[pagerduty]` template with the PagerDuty API_Token.

Run with: `resilient-circuits run`.

To uninstall, run: `pip uninstall fn_pagerduty`
    
## Resilient Configuration
Follow the steps to add a pagerduty section to your `app.config` file by running `resilient-circuits config [-u | -c]` and updating the fields:

```
[pagerduty]
api_token=<api_token>
# bypass https certificate validation (only set to False for testing purposes)
verifyFlag=False
```

Sample workflows have been provided. They include: 
* Name: Trigger PagerDuty
  * Manual
  * Object type: Incident
* Name: Update PagerDuty Incident
  * Automatic
  * Object type: Incident
  * Conditions: When an Incident severity changes or when the Incident is closed
* Name: Create PagerDuty Note
  * Automatic
  * Object type: Note
  * Conditions: When a Note is created
  




