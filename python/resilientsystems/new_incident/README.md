Lookup in Local File from Resilient
===================================

Use Case: In many cases, a company will have multiple divisions involved
in the handling of an incident. In Resilient, this often means one instance
will consist of several orgs. 

This script demonstrates the ability to escalate incidents between orgs. 

This integration can be run on the Resilient appliance or anywhere else.
The code is written in Python, and can be extended for your own purposes.

Requires: Python version 2.7.x or 3.4.x or later.
Requires: Resilient Server or hosted Application, version 23 or later.

## Resilient server setup

You must configure the following customizations to the Resilient server.
Open the Administrator Settings --> Actions, then:

### Message Destination

Create a Queue message destination with programmatic name `addincident`.
Select Yes for "expect acknowledgement", and add the integration user
to its users list.

![Custom message destination](documentation/messagedestination.png)

### Custom Fields

Create a custom text field called "resilient_org_id". This will be where
the script puts the original incident ID. For example, if we use incident
number 4242 in org1 to create a new incident in org2, the new incident in
org2 will have a resilient_org_id field of 4242. This field can 
be modified or removed as necessary and is not vital to the execution of the
script.

### Automatic Action

Create an manual action named 'Add Incident', associated with object type
"Incident".  Choose `addincident` as the message destination. 

![Custom Automatic Action](documentation/automaticaction.png)

## Python setup

The Resilient REST API is accessed with a helper module 'co3' that should be
used for all Python client applications.  The 'co3' module is a part of the
Resilient REST API utilities 'co3-api'.  Download and install that first,
following its instructions.

This application is built using the circuits library.  The 'resilient-circuits'
framework should be downloaded and installed, following its instructions.

## Installing the Integration

Unpack the integration's files into the location where you will run them.

## Configuring the Integration

The script reads configuration parameters from a file.
The configuration file is named `app.config`, in the same
directory as the scripts.  Edit this file to provide appropriate values
appropriate for your environment (server URL and authentication credentials).
Verify that the logging directory has been created.

### Certificates

If your Resilient server uses a self-signed TLS certificate, or some
other certificate that is not automatically trusted by your machine,
you need to tell the Python scripts that it should be trusted.
To do this, download the server's TLS certificate into a file,
e.g. from 'resilient.example.com' to a file 'cert.cer':

    mkdir -p ~/resilient/
    openssl s_client -connect resilient.example.com:443 -showcerts < /dev/null 2> /dev/null | openssl x509 -outform PEM > ~/resilient/cert.cer

Then specify the path to this certificate in the config file.


## Running the example

In the script directory, run the custom action application with:

    python run.py

The script will start running, and wait for messages.  When users in Resilient
click on the manual action, it will add a new incident to the second org
specified by the credentials in the config file. This new incident will
have the name "New Incident From Manual Action". Furthermore, the new  
incident description will be "Incident created from incident (incidentnumber)",   
the new incident discovered date will be "Sun, 24 Apr 2016 16:52:45 GMT".   
All of these fields can be customized in the script.  

![Search Results](documentation/results.png)

To stop the script running, interrupt it with `Ctrl+C`.

## Extending the example

This module could be easily extended by customizing the fields ported over
to the new incident. This could scale up to the point where the new incident
is a carbon copy of the first, although extensive field-mapping is needed 
to achieve this result.

### More
For more extensive integrations with stored data files, contact
[success@resilientsystems.com](success@resilientsystems.com).
