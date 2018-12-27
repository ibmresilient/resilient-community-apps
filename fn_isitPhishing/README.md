# Resilient Integration with IsItPhishing
**This package contains two functions that call the Vade Secure IsItPhishing Webservice API to analyze a URL or to analyze an HTML document.  Also included are 3 example workflows and rules to demonstrate how to invoke and use the functions.**

 ![screenshot](./screenshots/isitPhishing-url-function.png)
 ![screenshot](./screenshots/isitPhishing-url-preprocess.png)
 ![screenshot](./screenshots/isitPhishing-url-postprocess.png)
 ![screenshot](./screenshots/isitPhishing-url-rule.png)
 ![screenshot](./screenshots/isitPhishing-doc-function.png)
 ![screenshot](./screenshots/isitPhishing-doc-preprocess.png)
 ![screenshot](./screenshots/isitPhishing-doc-postprocess.png)
 ![screenshot](./screenshots/isitPhishing-doc-rule.png)
## app.config settings:
```
[fn_isitPhishing]
# Define the Vade Secure IsItPhishing Webservice API endpoint
#
isitPhishing_api_url=https://ws.isitphishing.org/api/v2
#
# You need a license key to use the Vade Secure IsItPhishing API. 
# This key will be provided to you by Vade Secure, and has the following format:
# <NAME>:<LICENSE>
isitPhishing_name=xxxx
isitPhishing_license=xxxx
```

## Function: isitPhishing_url

###Function Inputs: 

| Function Parameter | Type | Required | Example | Info |
| ------------- | :--: | :-------:| ------- | ---- |
| `isitPhishing_url`| `String` | Yes | `"http://www.thisisaphishingurl.com "` | N/A |


### Function Output:
```python

results = {
  analysis: {
    status: "PHISHING"
  },
  inputs: {
    URL: "URL_to_analyze"
  }
}

```

### Pre-Process Script: 
```python
# Get the URL from the artifact value
inputs.isitphishing_url = artifact.value

```

### Post-Process Script: Example: IsItPhishing Analyze URL:

```python
# Get the results and post to an incident note.
content = u'IsItPhishing analysis of URL {0} : {1}\n'.format(results['inputs']['URL'], results['analysis']['status'])
note = helper.createPlainText(content)
incident.addNote(note)

```

### Rules: Example: isitPhishing Analyze URL:
| Rule Name | Object Type | Workflow Triggered | Conditions |
| --------- | :---------: | ------------------ | ---------- |
| Example: IsItPhishing Analyze URL | `Artifact` | `Example: IsItPhishing Analyze URL` | Artifact type is URL |


##Function: isitPhishing__html__document

### Function Inputs:
| Function Parameter | Type | Required |
| ------------- | :--: | :-------:|
| `incident_id`| `Number` | Yes |  |
| `task_id`| `Number` | No |  |
| `attachment_id`| `Number` | No |  |
| `artifact_id`| `Number` | No |  |

### Function Output:
```python

results = {
  analysis: {
    result : "PHISHING"
  },
  inputs: {
    incident_id": incident_id,
    "task_id": task_id,
    "attachment_id": attachment_id,
    "artifact_id": artifact_id
  }
}

```

### Pre-Process Script for Attachment:

```python
# Required inputs are: incident id and attachment id
inputs.incident_id = incident.id
inputs.attachment_id = attachment.id

if task is not None:
  inputs.task_id = task.id

```

### Post-Process Script for Attachment:

```python
# Get the results and post to an incident note.
content = u"IsItPhishing analysis of attachment document {0} : {1}".format(results["inputs"]["filename"],results['content']['result'])
note = helper.createPlainText(content)
incident.addNote(note)

```

### Rule for Attachment:
| Rule Name | Object Type | Workflow Triggered |
| --------- | :---------: | ------------------ | 
| Example: IsItPhishing Analyze HTML Document: Attachment | `Attachment` | `Example: IsItPhishing Analyze HTML document: Attachment` |

### Pre-Process Script for Artifact:

```python
# Required inputs are: incident id and attachment id
inputs.incident_id = incident.id
inputs.artifact_id = artifact.id

```

### Post-Process Script for Artifact:

```python
# Get the results and post to an incident note.
content = u"IsItPhishing analysis of artifact document {0} : {1}".format(results["inputs"]["filename"],results['content']['result'])

note = helper.createPlainText(content)

incident.addNote(note)

```

### Rule for Artifact:
| Rule Name | Object Type | Workflow Triggered |
| --------- | :---------: | ------------------ | 
| Example: IsItPhishing Analyze HTML Document: Artifact | `Artifact` | `Example: IsItPhishing Analyze HTML document: Artifact` |

## Install and run
To package for distribution,

`python ./fn_isitPhishing/setup.py sdist`

The resulting .tar.gz file can be installed using

`pip install <filename>.tar.gz`

To run the integration:

`resilient-circuits run`

##