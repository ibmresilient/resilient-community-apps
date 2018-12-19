# Resilient Function - Twilio Send SMS

This Resilient Function package can be used to send an SMS via Twilio from a workflow using the Functions feature of the Resilient Circuits integration framework.

Prerequisites:
```
resilient version 30 or later
resilient_circuits version 30 or later
twilio version 6.21.0 or later
```

## Environment
This package requires that it is installed on a RHEL platform and that the resilient-circuits application is running.
Install this package with 'pip', or `python setup.py install`.
To set the config values in the app.config file with a new resilient instance run `resilient-circuits config -c`.
To set the config values in the app.config file with an existing resilient instance run `resilient-circuits config -u`.

Config values example:
The parameters twilio_account_sid and twilio_auth_token are as defined in your Twilio account.
The parameter twilio_src_address should be set to the Twilio number you wish to use.
```
[fn_twilio_send_sms]
twilio_account_sid=
twilio_auth_token=
twilio_src_address=
```

Run with: `resilient-circuits run`.

## Supported Resilient Functions for Twilio Send SMS
```
fn_twilio_send_sms
```
## Sample workflows have been provided:
```
Example: Send Twilio SMS
```
## fn_twilio_send_sms Example

The fn_twilio_send_sms Function takes 2 input parameters. The parameters are setup from a Resilient systems workflow on the Resilient console.
- twilio_sms_destnation - a comma delimited (CSV) list of destination numbers
- twilio_sms_message - the message you wish to send

The following are examples of setup of each parameter using a simple workflow pre-processing script.
The message can be customised to suit your own use case.
```
inputs.twilio_sms_destination = rule.properties.twilio_sms_destination
inputs.twilio_sms_message = 'An incident ' + incident.name + ' (' + `incident.id` + ') with ' + incident.severity_code + ' priority may require your attention'
```
The results returned to Resilient can be used to determine the status for each destination.
Below is a post process script which adds a note for each destination.
```
for entry in results["twilio_status"]:
  if(entry.success == True):
    note_text = """<b>Twilio SMS Message:</b> {0}
              </br><b>sent to:</b> {1}""".format(results.twilio_sms_message,
                                            entry.phone_number)
                                          
    incident.addNote(helper.createRichText(note_text))
  else: 
    note_text = """<b>Unable to send Twilio SMS Message:</b> {0}
              </br><b> to:</b> {1} ({2})""".format(results.twilio_sms_message,
                                            entry.phone_number, entry.error_message)
                                          
    incident.addNote(helper.createRichText(note_text))
```
