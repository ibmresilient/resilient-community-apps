# Resilient Function - Jira Integration

This Resilient Functions package provides integration with JIRA for:
* Issue Creation
* Issue Transitions
* Comment Creation

Prerequisites
```
resilient-circuits >=v30.0.0
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
# use verifyFlag to disable untrusted certificate verification
verifyFlag=True
```

Sample workflows have been provided. They include: 
* Name: Jira Create Issue
  * Automatic
  * Object type: Incident
  * Conditions: When an Incident is created
* Name: Jira Close Issue
  * Automatic
  * Object type: Incident
  * Conditions: When an Incident Resolution Summary is changed
* Name: Jira Create Comment
  * Automatic
  * Object type: Note
  * Conditions: When a Note is created
  




