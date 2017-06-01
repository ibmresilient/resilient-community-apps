Simple Circuits Web Example
==================

This component utilizes circuits.web to server up examples of 
a REST endpoint for a Webhook and also a Webform for incident 
creation.

## Environment and Installation

The following Python packages should be installed on your system:
co3
resilient_circuits
rc-webserver

In your Resilient Circuits app.config file, in the "resilient" section, 
set a value for "componentsdir" to be a directory on your system.  
Copy the web_example.py file into the directory specified.

If you have not already created an app.config file, do so with:
`resilient-circuits config -c`

## Running the Examples

Start up the integration with:
`resilient-circuits run`

Point your browser to http://localhost:9000/example
Enter an incident name and description and click Submit.  If successful, you should see the ID of an incident that was created.
*Note that if your appliance is configured with additional mandatory fields, you will need to update this example to account for them*

You can try out the note creation endpoint from the command line with curl:
"""
`curl -H "Content-Type: application/json" -X POST -d '{"text": "This is a great note"}' http://localhost:9000/example/incident/2661/note `
{"status": "Note ID [223] posted to incident [2661]"}
"""
