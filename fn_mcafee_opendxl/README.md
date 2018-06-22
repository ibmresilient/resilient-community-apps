## Function McAfee Publish to DXL
#### This function is designed to publish an event or invoke a service on the DXL framework.


To install in "development mode":

    pip install -e ./fn_mcafee_opendxl/

After installation, the package will be loaded by `resilient-circuits run`.


To uninstall:

    pip uninstall fn_mcafee_opendxl


To package for distribution:

    python ./fn_mcafee_opendxl/setup.py sdist

The resulting .tar.gz file can be installed using:

    pip install <filename>.tar.gz

Set the following value in the config file under the `[fn_mcafee_opendxl]` section:

    dxlclient_config=<path_to_dxlclient.config_file>
    
Deploy to the Resilient Platform:

    resilient-circuits customize

Creates the following items in the Resilient Platform:

    Function: McAfee Publish to DXL
    Function inputs: mcafee_topic_name, mcafee_dxl_payload, mcafee_publish_method, mcafee_return_response
    Message Destination: McAfee DXL Message Destination
    Workflows: (Example) McAfee Publish to DXL (Set TIE Reputation), (Example) McAfee Publish to DXL (Tag System)
    Rules: (Example) McAfee Publish to DXL (Set TIE Reputation), (Example) McAfee Publish to DXL (Tag System)

### How to use the function
1. Import the necessary customization data into the Resilient Platform:

		resilient-circuits customize
		
	This will create the following customization components:
	* Function inputs: `mcafee_dxl_payload, mcafee_publish_method, mcafee_return_response, mcafee_topic_name`
	* Message Destinations: `mcafee_dxl_message_destination`
	* Functions: `mcafee_publish_to_dxl`
	* Workflows: `example_mcafee_publish_to_dxl_set_tie_reputation, example_mcafee_publish_to_dxl_tag_system`
	* Rules: `(Example) McAfee Publish to DXL (Tag System), (Example) McAfee Publish to DXL (Set TIE Reputation)`

2. Update and edit `app.config`:

		resilient-circuits configure -u

3. Start Resilient Circuits with: `resilient-circuits run`
4. Trigger either rule.



## Integration McAfee DXL Listener
#### This integration is designed to listen on a DXL topic and map the data into an Incident DTO and sent to Resilient to create Incidents and Artifacts

It is included in the same package and installed/uninstalled in the same manor as above.

The following values will need to be set in the config file under the `[fn_mcafee_opendxl]` section:

    topic_name=<this_is_the_topic_the_integration_will_listen_on>
    topic_listener_on=[True|False]  #Turns the listener on or off
    incident_template=<Resilient incident DTO template>
    incident_template_mapping=<Incident mapping template>

### How to use the integration
1. Update and edit `app.config`:

		resilient-circuits configure -u

2. Start Resilient Circuits with: `resilient-circuits run`