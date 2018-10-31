# Resilient Integration with Google Cloud Functions
** This package contains one function which targets the Twitter Search API. Takes in an input of a multiple possible hashtags and a number of Tweets to be returned and contacts the Twitter Search API to return the results. Requires Twitter Access Key and Secret to obtain a OAuth2 read-only token. **  
 
 ![screenshot](./screenshots/1.png)


Note: This Package depends on the fn_utilities package. fn_utilities must be installed for the function to work as expected.

The output of the Google Cloud Function is fed downstream into a Utility function called Base64ToAttachment.
This function takes the base64 result from the previous function and saves it in the Resilient Platform as an attachment.
## app.config settings:
```python
[fn_gcp]
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

