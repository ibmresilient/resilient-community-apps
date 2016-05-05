Lookup in Local File from Resilient
===================================

Use Case:  Upon changing the Severity of an incident, change the owner
and add members as appropriate. This currently is specific to my
(ztaira@resilientsystems.com) local instance, because it uses user ID's
rather than names. However, the code can be easily modified to fit any
case of assigning users based on a change in severity.
Currently, you can get the user names and ID's with Python as follows:
users = resilient_client.get("/users/")
for user in users:
	print user['id'], user['fname'], user['lname']
groups = resilient_client.get("/groups")
for group in groups:
	print group['id'], group['name']

This integration can be run on the Resilient appliance or anywhere else.
The code is written in Python, and can be extended for your own purposes.

Requires: Python version 2.7.x or 3.4.x or later.
Requires: Resilient Server or hosted Application, version 23 or later.

## Resilient server setup

You must configure the following customizations to the Resilient server.
Open the Administrator Settings --> Actions, then:

### Message Destination

Create a Queue message destination with programmatic name `addgroup`.
Select Yes for "expect acknowledgement", and add the integration user
to its users list.

![Custom message destination](documentation/messagedestination.png)

### Custom Fields

No Custom Fields are needed for this action.

### Automatic Action

Create an automatic action named 'Add Group', associated with object type
"Incident".  Choose `addgroup` as the message destination. Add condition
"Severity is changed".

![Custom Automatic Action](documentation/automaticaction.png)

## Python setup

The Resilient REST API is accessed with a helper module 'co3' that should be
used for all Python client applications.  The 'co3' module is a part of the
Resilient REST API utilities 'co3-api'.  Download and install that first,
following its instructions.

This application is built using the circuits library.  The 'resilient-circuits'
framework should be downloaded and installed, following its instructions.

## Installing the Integration

Unpack the integration's files into the location where you will run them.

## Configuring the Integration

The script reads configuration parameters from a file.
The configuration file is named `app.config`, in the same
directory as the scripts.  Edit this file to provide appropriate values
appropriate for your environment (server URL and authentication credentials).
Verify that the logging directory has been created.

### Certificates

If your Resilient server uses a self-signed TLS certificate, or some
other certificate that is not automatically trusted by your machine,
you need to tell the Python scripts that it should be trusted.
To do this, download the server's TLS certificate into a file,
e.g. from 'resilient.example.com' to a file 'cert.cer':

    mkdir -p ~/resilient/
    openssl s_client -connect resilient.example.com:443 -showcerts < /dev/null 2> /dev/null | openssl x509 -outform PEM > ~/resilient/cert.cer

Then specify the path to this certificate in the config file.


## Running the example

In the script directory, run the custom action application with:

    python run.py

The script will start running, and wait for messages.  When users in Resilient
update the incident severity, it will add or remove users based on what the
final severity level is changed to.

![Search Results](documentation/results.png)

To stop the script running, interrupt it with `Ctrl+C`.

## Extending the example

This example can be easily extended by getting the group/user models off of
resilient using the REST API's GET method and then customizing which members
are added to which severity. These can be mapped together in the config
file to improve readability and modularity of the circuits component.
In addition, this script can be triggered by fields other than Severity
by swapping out 'severity_code' for another field in Resilient.

### More
For more extensive integrations with stored data files, contact
[success@resilientsystems.com](success@resilientsystems.com).
