Add Group
=========


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


## Environment and Installation

This integration is provided as
* A component for a "resilient circuits" framework
* A fragment of a configuration file.

Copy the .py file into your `components` directory, where it will be
loaded automatically when your application starts.

Copy the confiruration file fragment into your application's configuration
file and edit the settings appropriately.


## Resilient server setup

You must configure the following customizations to the Resilient server.
Open the Administrator Settings --> Actions, then:


### Message Destination

Create a Queue message destination with programmatic name `addgroup`.
Select Yes for "expect acknowledgement", and add the integration user
to its users list.


### Automatic Action

Create an automatic action named 'Add Group', associated with object type
"Incident".  Choose `addgroup` as the message destination. Add condition
"Severity is changed".



