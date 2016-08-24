Assign Tasks to Me
==================

This implements a custom Manual Action named "Assign Tasks To Me",
which takes all the unassigned tasks in the current phase
or in a use-selected phase of the incident, and assigns them
to the current user.


## Environment and Installation

This integration is provided as
* A component for a "resilient circuits" framework
* A fragment of a configuration file.

Copy the .py file into your `components` directory, where it will be
loaded automatically when your Resilient Circuits application starts.

Copy the configuration file fragment into your application's configuration
file and edit the settings appropriately.


## Resilient server setup

You must configure the following customizations to the Resilient server.
Open the Administrator Settings --> Actions, then:


### Message Destination

Create a Queue message destination with programmatic name `assigntasks`.
Select Yes for "expect acknowledgement", and add the integration user
to its users list.

Note: you can use any message destination; its name is specified in the
config file as 'queue' in the "[assigntasks]" section.

### Manual Action

Create a manual action named 'Assign Tasks To Me', associated with
object type "Incident".  Choose `assigntasks` as the message
destination. 



