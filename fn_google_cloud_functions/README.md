# Resilient Integration with Google Cloud Functions
**This package contains functions which invoke or interact with Google Cloud Functions.**  
 
 ![screenshot](./screenshots/1.png)

Do you have a use-case or a need to get data / perform an operation from a service without exposing your IP? 
Why not build out a cloud function which does that work for you under a different network configuration and target that instead.

Note: This Package depends on the fn_utilities package. fn_utilities must be installed for the function to work as expected.

The output of the Google Cloud Function is fed downstream into a Utility function called Base64ToAttachment.
This function takes the base64 result from the previous function and saves it in the Resilient Platform as an attachment.
## app.config settings:
```python
[fn_google_cloud_functions]
gcp_region = <GCP_REGION_ID>
gcp_project_id = <GCP_PROJECT_ID>
gcp_function_name = <NAME_OF_CLOUD_FUNCTION>
# Optional Config values
gcp_http_proxy = None
gcp_https_proxy = None

```

## Function Inputs:
**gcp_url:**
* The URL to send to the GCP Cloud Function
* E.g. https://www.ibm.com

## Pre-Processing Scripts 
The workflow `Example: GCP Cloud Functions: Sandbox and Screenshot Webpage` includes 2 functions.

### Function : GCP Cloud Functions: Sandbox and Screenshot Webpage
```python
inputs.gcp_url = artifact.value
```

### Function : Utilities: Base64 to Attachment
```python
url = workflow.properties.sandbox_screenshot["input_url"]
attachment_desc = "GCP Sandbox Screenshot of {0}".format(url)

inputs.incident_id = incident.id 
inputs.file_name = attachment_desc
inputs.base64content = workflow.properties.sandbox_screenshot["base64Screenshot"]
```


## Function Output:
* The function returns the results as a Python Dictionary. Here is an example ouput:
```
{
    "success": True/False,
    "base64Screenshot": <base64 string>
    "input_url": <string>
}
```

## Rules
| Rule Name | Object Type | Workflow Triggered |
| --------- | :---------: | ------------------ |
| Send URL to Google Cloud function for Sandboxing | `Artifact` | `Example: GCP Cloud Functions: Sandbox and Screenshot Webpage` |

