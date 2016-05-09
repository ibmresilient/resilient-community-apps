Send an Email from Resilient
===================================

Use Case: Send an custom email message from resilient with the click of a
button. This is useful if you want to send one-off emails with custom messages.


## Environment and Installation

This integration is provided as
* A component for a "resilient circuits" framework
* A fragment of a configuration file.

Copy the .py file into your `components` directory, where it will be
loaded automatically when your application starts.

Copy the configuration file fragment into your application's configuration
file and edit the settings appropriately.


## Resilient server setup

You must configure the following customizations to the Resilient server.
Open the Administrator Settings --> Actions, then:


## Message Destination

Create a Queue message destination with programmatic name `outboundmail`.
Select Yes for "expect acknowledgement", and add the integration user
to its users list.


## Manual Action

Create an manual action named 'Send Email', associated with object type
"Incident". Choose `outboundmail` as the message destination.


## Custom fields

Create three custom text fields to represent the email body, address, and
subject. Put their API access names under the address, subject, and body 
fields in the config file. Also, whatever message you include in the default
message field in the [sendmail] section of the config file will be included
in all of the messages you send out by default. 


## Gmail Configuration

This incident assumes you have a working gmail account with valid login
credentials. Once you have your gmail, credentials, put them in the associated
fields in the [sendmail] section of the app.config file.
