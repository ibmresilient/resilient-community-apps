Add Group
=========


Use Case:  Upon changing the Severity of an incident, change the owner
and add members as appropriate.

An automatic rule triggers when the severity is changed.  The action processor,
implemented in the 'add_group.py' component, responds to this event.  It finds
the intended owner and membership from settings in the configuration file,
and applies them to the incident.


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
Open the Customization Settings menu, then:


## Message Destination

Open the Message Destinations tab.
Create a Queue message destination with programmatic name `addgroup`.
Select Yes for "expect acknowledgement", and add the integration user
to its users list.


## Automatic Rule

Open the Rules tab.  Create an automatic rule named 'Add Group',
associated with object type "Incident".  Choose `addgroup` as the message destination. 
Add condition "Severity is changed".

