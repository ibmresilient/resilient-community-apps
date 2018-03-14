# Resilient Function - Jira Integration

This Resilient Functions package provides integration with JIRA for:
* Issue Creation
* Issue Transitions
* Comment Creation

Prerequisites
```$xslt
resilient-circuits
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
Incident
* Create a new tab to display the Jira fields:
  * jira_url
  * jira_url
  
Create workflows for the functions 
* Jira Create Issue
  * function: Jira Create Issue
  * pre-processing script can be set as:
  ```desc = ''
     if incident.description is not None:
        desc = incident.description.content
     
     inputs.incidentID = incident.id
     inputs.jira_description = "Incident types: {}\nNist Attack Vectors: {}\n\nAdditional Information: {}".format(incident.incident_type_ids, incident.nist_attack_vectors, desc)
     inputs.jira_summary = "Resilient: {}".format(incident.name)
  ```
  * post-processing script can be set as:
  ```
     incident.properties.jiraid = results.issue['key']
     incident.properties.jiraurl = results.issue['self']
  ```
     
  * configure the `jira_project` and `jira_issuetype` input fields with the appropriate values for your use of Jira
* Jira Create Comment
  * function: Jira Create Issue
  * pre-processing script can be set as:
  ```
  inputs.jira_url = incident.properties.jiraurl
  inputs.jira_comment = note.text.content
  ```
  * no post processing script necessary
* Jira Transition Issue
  * function: Jira Create Issue
  * pre-processing script can be set as:
  ```
  inputs.jira_url = incident.properties.jiraurl
  inputs.jira_comment = "Resolution: {}\n{}".format(incident.resolution_id, incident.resolution_summary.content)
  ```
  
  * configure the `jira_transition_id` input field for the appropriate value 
  * no post processing script necessary

Create rules for the workflows. Example rules are: 
* Jira Create Issue
  * Automatic
  * Object type: Incident
  * Conditions: When an Incident is created
* Jira Close Issue
  * Automatic
  * Object type: Incident
  * Conditions: When an Incident Resolution Summary is changed
* Jira Create Comment
  * Automatic
  * Object type: Note
  * Conditions: When a Note is created
