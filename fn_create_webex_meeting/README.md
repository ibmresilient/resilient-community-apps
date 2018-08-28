# Resilient Function - Create Webex Meeting

This Resilient Function package can be used to create a Cisco WebEx meeting from a workflow using the Functions feature of the Resilient Circuits integration framework.

Prerequisites:
```
resilient version 30 or later
resilient_circuits version 30 or later
pytz
requests
```
* Can be used in a Resilient workflow to add a note or update another resource.

## Environment

This package requires that it is installed on a RHEL platform and that the resilient-circuits application is running.
Install this package with 'pip', or `python setup.py install`.
To set the config values in the app.config file with a new resilient instance run `resilient-circuits config -c`.
To set the config values in the app.config file with an existing resilient instance run `resilient-circuits config -u`.

Config values example:
(Note: The email and password should be for a user that is able to create meetings)
```
[create_webex_meeting]
webex_email=abc@abc.com
webex_password=abc123
webex_site=abc.webex.com
webex_site_url=abc
webex_timezone=GMT-04:00
```

Run with: `resilient-circuits run`.

## Supported Resilient Functions for Create WebEx Meeting
```
fn_create_webex_meeting
```
## Sample workflows have been provided:
```
Example: Create WebEx Meeting: Incident
```
## fn_create_webex_meeting Example

The fn_create_webex_meeting Function takes 3 input parameters. The parameters are setup from a Resilient systems workflow on the Resilient console.
The following are examples of setup of each parameter using a simple workflow pre-processing script.
```
inputs.webex_meeting_name = incident.name
inputs.webex_meeting_agenda = incident.description.content
inputs.webex_meeting_password = "resilient"
```
The results returned to Resilient will be in JSON format and will be similar to the following format.
Note: Each Resilient Function will return a different result.
```
{
"status":"SUCCESS",
"host_url":"https://sitename.my.webex.com/sitename/j.php?MTID=x",
"attendee_url":"https://sitename.my.webex.com/sitename/j.php?MTID=x"
}
```