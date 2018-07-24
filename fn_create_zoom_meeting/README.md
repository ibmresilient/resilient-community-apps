# Resilient Function - Create Zoom Meeting

This Resilient Function package can be used to create a Zoom meeting from a workflow using the Functions feature of the Resilient Circuits integration framework.

Prerequisites:
```
resilient version 30 or later
resilient_circuits version 30 or later
pyjwt
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
[create_zoom_meeting]
[create_zoom_meeting]
zoom_api_url=https://api.zoom.us/v2
zoom_api_key=<api key>
zoom_api_secret=<api secret>
```

Run with: `resilient-circuits run`.

## Supported Resilient Functions for Create Zoom Meeting
```
fn_create_zoom_meeting
```
## Sample workflows have been provided:
```
Example: Create Zoom Meeting: Incident
```
## fn_create_zoom_meeting Example

The fn_create_zoom_meeting Function takes 5 input parameters. The parameters are setup from a Resilient systems workflow on the Resilient console.
The following are examples of setup of each parameter using a simple workflow pre-processing script.
```
inputs.zoom_host_email = incident.creator_id
inputs.zoom_topic = incident.name
inputs.zoom_agenda = incident.description.content
inputs.zoom_record_meeting = False
inputs.zoom_password = "resilient"
```
The results returned to Resilient will be in JSON format and will be similar to the following format.
Note: Each Resilient Function will return a different result.
```
{
"host_url": "https://zoom.us/s/x?zak=x", 
"attendee_url": "https://zoom.us/j/x?pwd=x", 
"date_created": "01/01/1971 12:00:00"
}
```