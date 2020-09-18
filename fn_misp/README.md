# MISP Functions

_Craig @ Resilient Labs_

The MISP functions allows integration with MISP Threat Intelligence Platform from Resilient.

## New for v3.0.0

There have been significant changes to the app for version 3, the community built a python3 compatible version of the app. This meant there was 2 different version in circulation.

This version of the app is designed to reunify the fn-misp apps. To support both python2 and python3 automatically - using the latest recommended libraries from the MISP community.

MISP are very clear they will be depreciating python2 support, so it is recommended if you want to continue using fn-misp you upgrade to python3 but in the meantime, this app is fully tested with python2. You will receive errors in logs referencing the depreciation.

Finally, the Lookup Att&ck function has been removed, as MISP now stores Att&ck information as Tags - this is returned via the search attribute function, so no special function is required. The example of how to parse out Technique IDs has been updated.

The old separate apps are packaged inside the app directory, marked as ARCHIVE. They are unsupported and just for code documentation purposes.

## Use Cases

The following 6 use cases are supported;

+ Create a MISP "Event" from a Resilient incident
+ Add attributes to the incident "Event" in MISP from incident artifacts incident
+ Mark any artifact in Resilient as "Sighted" if they exist in MISP
+ Search all MISP events for a match on a given attribute, this will also return tags for an attribute
+ Return all MISP sightings for a given event
+ Create Tag on an event or attribute in MISP - such as TLP, Att&ck or threat actor.

![Misp Functions](./doc/screen_0.png)

## Installation 

This function is packaged as a zip, so you do not need to extract the zip to install it.

```bash
pip install fn_misp-<version>.zip
```

You will then need to add the configuration section to your `app.config` file.

```bash
resilient-circuits config -u
```

This will add the MISP key and url properties. Update the URL for your instance of MISP and add the API key found in "Event Actions -> Automation". Set the verify cert to false if you do not want to verify the certificate. 

```bash
[fn_misp]
misp_url=http://localhost
misp_key=<your key>
# used to bypass cerification validation for self signed instances of MISP
verify_cert=true
```

To add all the configuration settings for functions, workflows, runs, etc. to Resilient,  run the following command:

```bash
resilient-circuits customize -l fn-misp
```

## Configuration

Sample workflows are included to demonstrate how to execute a function and how to parse the returned results.

For each workflow, edit each function (see the pencil icon) and visit the Post-Process Script for processing hints. Your use of the functions may need different data formatting or different feedback such as notes etc.

![screenshot](./doc/screen_1.png)

An incident field `misp_event_id` is used to track event creation. This field can remain hidden or added to your layout through the `Customization Settings` section. You can pair this with a rich text field and in-product script to give a direct Resilient UI link to the event in MISP.

## Rules

This app is not packaged with rules to prevent adding needed configuration to your system.

Some recommended rules are below:

+ Auto - Create MISP Event if incident is created
+ Auto - Create MISP Attribute if artifact is created and incident.misp_event_id has a value
+ Auto - Search MISP Attribute if artifact us created and incident.misp_event_id has a value
+ Menu Item - Create TLP Tag on an artifact when misp_event_id has a value

## Using MISP for Att&ck

The following assumes you have installed the Resilient Att&ck function.

When you run a search for an attribute with event or attribute level artifacts. The response includes Technique IDs from MITRE Att&ck.

You will see this is in the default search workflow, the Att&ck information comes back in the tags field in the artifact description.

![screenshot](./doc/screen_2.png)

We can use our postprocessing script to extract these to use in the Techniques DataTable for Att&ck.

Clone the example workflow to customize it.

>`resilient-circuits clone --workflow example_misp_search_attribute misp_search_attack`

Now we can edit the post process script of the cloned workflow.

First we need to loop through the tags and check they have `mitre-attack` in, add to the bottom of the existing post processing script.

```python
for tag in results.tags:
  if "mitre-attack" in tag:
```

Next we need to parse out the Technique ID to put in our MITRE Att&ck table (from the MITRE function).

```python
for tag in results.tags:
  if "mitre-attack" in tag:
    tag.split("=")
```

This will give us a list now where the second (position 1) item is "Bootkit - T1067", we can now use simple regex to pull this out.

```python
import re

regex_pattern = "(T\d+)"

for tag in results.tags:
  if "mitre-attack" in tag:
    split_tag = tag.split("=")
    technique = split_tag[1]
    technique_id = re.findall(regex_pattern, technique)
    dt = incident.addRow("mitre_attack_techniques")
    dt.technique_id = technique_id[0]
```

Now create a rule and run the workflow to check it pulls out the Technique ID into the table.

Now this is all working you can chain with the MITRE Lookup function to lookup the Technique ID when a row is added to the datatable. Remember you can also use the "Create Tag" function to tag artifacts with Att&ck.
