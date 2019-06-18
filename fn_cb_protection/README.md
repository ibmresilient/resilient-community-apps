# Resilient Functions for CarbonBlack Protection

This Resilient Function package can be used to interact with Carbon Black CbProtection.
When a CbProtection user sends an approval request to allow execution of a file,
this request can be used to create a Resilient incident.  This integration includes
workflows for the analyst to approve or deny the approval request.

Prerequisites:

	resilient version 30 or later
	resilient_circuits version 30 or later

## Environment

This package requires that it is installed on a RHEL platform and that the resilient-circuits application is installed.
Install this package with 'pip', or `python setup.py install`.
To set the config values in the app.config file with a new resilient instance run `resilient-circuits config -c`.
To set the config values in the app.config file with an existing resilient instance run `resilient-circuits config -u`.

Config values example:

	[fn_cb_protection]
	
	# Name or IP address of your CbProtect server
	server=10.200.1.1
	
	# Access token issued by the CbProtect administrator
	token=XXXXX-XXXX-XXXXX-XXXX
	
	# If your CbProtect server has a self-signed TLS certificate, you cannot verify it:
	# verify_cert=false
	
	# Interval (seconds) for automatic escalation of approval requests, set 0 to disable
	# Suggest 300 as a starting point, which will check CbProtect every 5 minutes
	escalation_interval=0
	
	# Optional: query for which requests to escalate; default is to escalate all open approval requests
	# escalation_query=resolution:0
	
	# Optional: path to a custom template file for the escalated incident
	# template_file=/usr/integration/bit9_escalation.jinja
	
	# Optional: set this to only escalate a single request ID, e.g. when testing a custom template
	# test_single_request=999


Run with: `resilient-circuits run`.

## Resilient Functions for CbProtection - FIXME! - rename functions
```
CbProtect Approval Request Get
CbProtect Approval Request Query
CbProtect Approval Request Update
CbProtect File Catalog Get
CbProtect File Catalog Query
CbProtect File Instance Query
CbProtect File Instance Update
CbProtect File Rule Delete
CbProtect File Rule Get
CbProtect File Rule Query
CbProtect File Rule Update
CbProtect File Delete
```
## Rules and workflows have been provided: FIXME! - rename rules and workflows
```
(Example) CbProtection: Get Approval Request
(Example) CbProtection: Approve File Globally and Close Request
(Example) CbProtection: Approve File Locally and Close Request
(Example) CbProtection: Ban File Globally and Close Request
(Example) CbProtect Delete File
(Example) CbProtection Delete File Rule
(Example) CbProtection File Rule Get
(Example) CbProtection Query Approval Request
(Example) CbProtection Query File Catalog
(Example) CbProtection Query File Rule
```
> Use these as reference to create your own from.

