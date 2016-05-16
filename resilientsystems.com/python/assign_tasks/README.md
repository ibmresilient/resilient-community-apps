Programmatically assign users to tasks in Resilient
===================================================

Use Case: In many cases, a user of Resilient would like to manually or
automatically assign tasks to a user or set of users. This circuits
script demonstrates how to assign those tasks to users programmatically.
It will assign each task in a given incident to a random users from the
current Resilient environment.


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


## Message Destination

Create a Queue message destination with programmatic name `assigntasks`.
Select Yes for "expect acknowledgement", and add the integration user
to its users list.


## Manual Action

Create an manual action named 'Assign Tasks', associated with object type
"Incident".  Choose `assigntasks` as the message destination. 


