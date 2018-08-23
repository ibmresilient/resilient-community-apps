# Resilient Function - Create Zoom Meeting

This Resilient Function package can be used to create a Zoom meeting from a workflow using the Functions feature of the Resilient Circuits integration framework.

Prerequisites:
```
resilient-circuits >=v30.0.0
```
Can be used in a Resilient workflow to add a note or update another resource.

## Environment
To install in "development mode"
    `pip install -e ./fn_create_zoom_meeting/`
    
The distribution file can be installed using
    `pip install fn_create_zoom_meeting-<version>.tar.gz`
    
Import the package into Resilient by running `resilient-circuits customize`

To configure the Create Zoom Meeting Function parameters, run `resilient-circuits config [-u | -c]`. 
Then edit the `[create_zoom_meeting]` template.

After installation, the package will be loaded by: `resilient-circuits run`.

To uninstall,
    `pip uninstall fn_create_zoom_meeting`

## Resilient Configuration
Follow the steps to add a create_zoom_meeting section to your `app.config` file by running `resilient-circuits config [-u | -c]` and updating the fields:

Note: The email and password should be for a user that is able to create meetings
```
[create_zoom_meeting]
zoom_api_url=https://api.zoom.us/v2
zoom_api_key=<api key>
zoom_api_secret=<api secret>
zoom_api_timezone=<timezone, i.e America/New_York>
```

## Supported Resilient Functions for Create Zoom Meeting
```
fn_create_zoom_meeting
```
## Sample workflows have been provided:
```
Example: Create Zoom Meeting: Incident
```
## fn_create_zoom_meeting Example

The fn_create_zoom_meeting Function takes 5 input parameters. The parameters are set up from a Resilient systems workflow on the Resilient console.
The following are examples of setup of each parameter using a simple workflow pre-processing script.
```
inputs.zoom_host_email = "email@email.com"
inputs.zoom_topic = incident.name
inputs.zoom_agenda = incident.description.content
inputs.zoom_record_meeting = False
inputs.zoom_password = "password"
```
The results returned to Resilient will be in JSON format and will be similar to the following format.
Note: Each Resilient Function will return a different result.
```
{
"host_url": "https://zoom.us/s/x?zak=x", 
"attendee_url": "https://zoom.us/j/x", 
"date_created": "01/01/1971 12:00:00"
}
```