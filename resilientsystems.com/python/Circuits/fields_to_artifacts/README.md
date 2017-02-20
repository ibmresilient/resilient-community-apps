Fields to Artifacts
===================

Artifacts are used to track key indicators, assets and observations
related to the security incident.  For some key indicators, such as
the IP address or hostname of a primary machine involved, it is often
useful to track the indicator with a field in the incident Details.
But custom fields don't have the data validation, threat intelligence
services and Related Incidents functions that artifacts provide.

To assist with this, instead of requiring the analyst to enter
the same information twice, this custom action processor copies
values from incident fields into artifacts.

Configuration has two parts:

* A tooltip to the field(s) in question.  This action processor
  looks for a particular format of the tooltip:

    `[Artifact: <artifact type>]`

  for example,

    `[Artifact: IP Address]`

* An automatic rule that triggers when the incident is
  modified.  If you have only a single field, or a small number of
  fields, that are tracked in this way, then rules with specific
  conditions should be created to trigger when those fields are
  changed.

When the action triggers, this processor examines each field that has
a tooltip in this format.  For each of these fields, it ensures that
an artifact exists having the field's value.


## Environment and Installation

This integration is provided as
* A component for a "resilient circuits" framework
* A fragment of a configuration file.

Copy the .py file into your `components` directory, where it will be
loaded automatically when your Resilient Circuits application starts.

If you want to use a different message destination than the default
("fields_to_artifacts"), copy the configuration file fragment into your
application's configuration file and edit the settings appropriately.


## Resilient server setup

You must configure the following customizations to the Resilient server.
Open the Customization Settings menu, then:

### Field Tooltips
Open the Layouts tab.
As described above, set the Tooltip for each field
that you want to be reflected in an artifact.  Be sure that the
Artifact Type you specify in the tooltip is valid, and that the
field's values will be valid for that artifact type.  For example,
you could specify Tooltip: `[Artifact: IP Address]`, and an
"IP Address" artifact will be created with the value of this field,
but if the field's value is not a valid IP Address then artifact
creation will fail.

### Message Destination

Open the Message Destinations tab.
Create a Queue message destination with programmatic name `fields_to_artifacts`.
Select Yes for "expect acknowledgement", and add the integration user
to its users list.

Note: you can use any message destination; its name is specified in the
config file as 'queue' in the "[fields_to_artifacts]" section.

### Rule

Open the Rules tab.
Create an automatic rule (the name is not important), associated with
object type "Incident".  Choose `fields_to_artifacts` as the message
destination.
 
If you want the rule to trigger only when a particular field is
changed, add that condition as appropriate.



