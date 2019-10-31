# Resilient Function - Jira Integration

This Resilient Functions package provides integration with JIRA for:
* Issue Creation
* Issue Transitions
* Comment Creation

Prerequisites
```
resilient-circuits >=v30.0.0
resilient-lib >= 32.0.186
```

## Environment
To install in "development mode", run 
    `pip install -e ./fn_jira/`
    
The distribution file can be installed using
    `pip install fn_jira-<version>.tar.gz`
    
Import the package into Resilient by running `resilient-circuits customize`

To configure the Jira parameters, run `resilient-circuits config [-u | -c]`. 
Then edit the `[jira]` template with the JIRA URL and basic authentication settings.

Run with: `resilient-circuits run`.

To uninstall, run: `pip uninstall fn_jira`
    
## Resilient Configuration
Follow the steps to add a jira section to your `app.config` file by running `resilient-circuits config [-u | -c]` and updating the fields:

```
[jira]
url=https://<jira url>
user=<jira user>
password=<jira user password>
# use verify_cert to disable untrusted certificate verification
verify_cert=True
```

Sample workflows have been provided. They include: 
* Name: Jira Create Issue
  * Manual
  * Object type: Incident
* Name: Jira Create Issue (Task)
  * Manual
  * Object type: Task
* Name: Jira Close Issue
  * Automatic
  * Object type: Incident
  * Conditions: When an Incident Resolution Summary is changed
* Name: Jira Close Issue (Task)
  * Manual
  * Object type: Task
* Name: Jira Create Comment
  * Automatic
  * Object type: Incident Note
  * Conditions: When a Note is created
 
  




