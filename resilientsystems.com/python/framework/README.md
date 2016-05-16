Framework
=========


Use Case: This is a template for a `resilient_circuits`-based component,
for easy prototyping.


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

Create a Queue message destination with programmatic name `framework_queue`.
Select Yes for "expect acknowledgement", and add the integration user
to its users list.

Note: 'framework_queue' must match the queue field in the config file.

## Automatic Action

Create an automatic action named 'Framework Action Title', associated with  
object type "Incident".  Choose `framework_queue` as the message destination.  
Add condition "Severity is changed".

