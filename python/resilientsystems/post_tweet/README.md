Post to Twitter from Resilient
===================================

Use Case: Given a twitter account defined in the config file and a message
specified when executing a manual action, post the message to twitter. This
would be useful if one is managing the social media accounts of a company.  

This integration can be run on the Resilient appliance or anywhere else.
The code is written in Python, and can be extended for your own purposes.

Requires: Python version 2.7.x or 3.4.x or later.
Requires: Resilient Server or hosted Application, version 23 or later.
Requires: A twitter account and OAuth login credentials

## Resilient server setup

You must configure the following customizations to the Resilient server.
Open the Administrator Settings --> Actions, then:

### Message Destination

Create a Queue message destination with programmatic name `twitterpost`.
Select Yes for "expect acknowledgement", and add the integration user
to its users list.

### Manual Action

Create an manual action named 'Post Tweet', associated with object type
"Incident".  Choose `twitterpost` as the message destination.

### Custom Fields

Create a custom text field called "Tweet Body" and make it required upon 
execution of the manual action. You can do this from the Manual Action
creation window. 

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
click the "Post Tweet" action and enter a message, said message will be posted
to the twitter account specified by the login credentials.

To stop the script running, interrupt it with `Ctrl+C`.

## Extending the example

This example can be extended by specifying a time in addition to a message,
so that the users can specify when they want a tweet posted in addition to
what they want posted. Furthermore, one can automate the posting of tweets
so that no human needs to be directly involved.

### More
For more extensive integrations, contact
[success@resilientsystems.com](success@resilientsystems.com).
