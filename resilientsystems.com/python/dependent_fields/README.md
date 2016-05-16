Make a field in resilient dependent on the result of two other fields
===================================


Use Case:  Given the value of a two custom fields in the resilient
platform, add them together, and populate the value in a third custom field.
These fields could represent many values, such as number of records or time
change. 


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


### Message Destination

Create a Queue message destination with programmatic name `timedelta`.
Select Yes for "expect acknowledgement", and add the integration user
to its users list.


### Custom Fields

Create two custom fields called 'custom3' and 'custom4', both of type
'Text'.  Add the new fields to the incident details so that you can
view them. Do the same for a third field called 'custom5'. 
These field names are arbitrary; if those fields already exist in your 
environment, you can name these fields differently than described here.
If so, make sure to change the appropriate field values in the app.config
file.


### Automatic Action

Create an automatic action named 'Time Delta', associated with object type
"Incident".  Choose `timedelta` as the message destination. Add condition
"custom4 is changed".

