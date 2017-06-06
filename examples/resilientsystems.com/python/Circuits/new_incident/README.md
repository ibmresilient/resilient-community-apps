Create New Incident in Another Org
===================================


Use Case: In some cases, a company will have multiple divisions involved
in the handling of an incident. In Resilient, this often means one instance
of Resilient will contain several Organizations (orgs).

This script demonstrates the ability to escalate incidents between orgs.

The action messages arrive from one org.  The resilient_circuits library gives
you a ready-authenticated 'SimpleClient' for REST API functions in that org.
But orgs are independent; each has a distinct set of users.  So, to access
another org, we need to construct a new SimpleClient for the purpose.

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

Create a Queue message destination with programmatic name `addincident`.
Select Yes for "expect acknowledgement", and add the integration user
to its users list.


## Manual Action

Create an manual action named 'Escalate Incident Between Orgs', 
associated with object type "Incident". Choose `addincident` as the message 
destination. 


