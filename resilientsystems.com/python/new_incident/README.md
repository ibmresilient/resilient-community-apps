Create New Incident in Another Org
===================================


Use Case: In many cases, a company will have multiple divisions involved
in the handling of an incident. In Resilient, this often means one instance
of Resilient will contain several orgs. 

This script demonstrates the ability to escalate incidents between orgs. 


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

Create a Queue message destination with programmatic name `newincident`.
Select Yes for "expect acknowledgement", and add the integration user
to its users list.


### Manual Action

Create an manual action named 'Escalate Incident between Orgs', 
associated with object type "Incident". Choose `newincident` as the message 
destination. 


