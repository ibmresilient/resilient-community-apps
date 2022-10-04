# URLScan.io Function 

[https://urlscan.io](urlscan.io) is a service to scan and analyse websites. When a URL is submitted to urlscan.io,
an automated process will browse to the URL like a regular user and record the activity that this page navigation
creates. This includes the domains and IPs contacted, the resources (JavaScript, CSS, etc) requested from those
domains, as well as additional information about the page itself. urlscan.io will take a screenshot of the page,
record the DOM content, JavaScript global variables, cookies created by the page, and a myriad of other observations.

This integration is a Resilient function that can be called from workflows, to submit a URL for analysis by urlscan.io.
It returns the report metadata, report URL, and base64-encoded screenshot that is attached to the incident.


## Installation
### App Host Setup
All the components for running this integration in a container already exist when using the App Host app.

To install,

* Navigate to Administrative Settings and then the Apps tab.
* Click the Install button and select the downloaded file: app-fn_urlscanio-x.x.x.zip.
* Go to the Configuration tab and edit the app.config file, editing the API key for URLScanIO and making any additional setting changes.


  | Config | Required | Example | Description |
  | ------ | :------: | ------- | ----------- |
  | **urlscanio_report_url** | Yes | `https://urlscan.io/api/v1` | *URL to retrieve scan reports* |
  | **urlscanio_screenshot_url** | Yes | `https://urlscan.io/screenshots` | *URL for website screenshots* |
  | **urlscanio_api_key** | Yes | 1790000-0000-0000-0000-a1b2c3d4597 / *Provide your URLScanIO API key* |
  | **timeout** | No | 300 / *Seconds to timeout reports which take a long time to complete. Default 5 minutes* |
  | **http_proxy** | No | `http://your_proxy.com` | *Optional http proxy URL* |
  | **https_proxy** | No | `https://your_proxy.com` | *Optional https proxy URL* |

### Integration Server Setup

Unzip file from AppExchange:

    unzip app-fn_urlscanio-1.1.5.zip

The resulting .tar.gz file can be installed using

    pip install fn_urlscanio-x.x.x.tar.gz

After installation, before running, you must import the customizations into your Resilient platform,

    resilient-circuits customize -l fn-urlscanio

<br/>

## app.config settings

The following block is automatically added to your app.config file when running `resilient-circuits config -u -l fn-urlscanio`. 
You will need to add your API key and have the flexibility to adjust the URL parameters if required.

```
[urlscanio]
urlscanio_report_url=https://urlscan.io/api/v1
urlscanio_screenshot_url=https://urlscan.io/screenshots
# your API key for urlscan.io
urlscanio_api_key=xxx

# Optional timeout (seconds)
# timeout=300
# Optional proxy settings
#http_proxy=http://your_proxy.com
#https_proxy=https://your_proxy.com
```

## Pre-Processing Script

```
# This is an artifact workflow; 
# The URL to scan is the artifact value
inputs.urlscanio_url = artifact.value

# Set the incident id
inputs.incident_id = incident.id
```

## Post-Processing Script

No action is performed after the workflow is complete, so we simply outline the result format in the results for ease of use.

```
# The result contains,
# {
#   "png_url": the URL of the screenshot image
#   "png_base64content": the base64-encoded screenshot (PNG)
#   "report_url": the URL of the JSON report_url
#   "report": the JSON report, which will contain lots of detail of the page analysis (see urlscan.io for details).
# }
#
# In this case, the file is already attached to the incident.  Nothing to do here.
workflow.addProperty('convert_json_to_rich_text', { 
    "version": 1.0,
    "header": "Artifact scan results for {}".format(artifact.value),
    "padding": 10,
    "separator": u"<br>",
    "sort": True,
    "json": results,
    "json_omit_list": ['png_base64content'],
    "incident_field": None
  })
```

## Other notes

To regenerate the customization blob,
`resilient-sdk codegen -p fn_urlscanio -m urlscanio --workflow example_urlscanio --rule "Example: urlscan.io"`

<br/>

## Changelog

| Version | Description |
| ------- | ----------- |
| 1.0.0   | Initial Release |
| 1.1.0   | Removed workflow dependency on fn_utilities <br> Added incident_id parameter to workflow inputs |
| 1.1.1 | Pinned version of resilient-lib to work with write_file_attachment <br> Updated customize.py so minimum required version of Resilient is v35.0 |
| 1.1.2 | Support added for App Host |
| 1.1.3 | Compatibility with older versions of resilient-circuits |
| 1.1.4 | Proxy support added |
| 1.1.5 | Bug fix error for non existing url |

When upgrading from a previous version. Add these lines to your existing app.config [urlscanio] settings

```
# Optional proxy settings
#http_proxy=http://your_proxy.com
#https_proxy=https://your_proxy.com
```