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
#### This integration is designed to listen on a DXL topic, map the data into an Incident DTO, and send it to the Resilient platform to create incidents and artifacts.

It is included in the same package as the Function McAfee Publish to DXL function and installed/uninstalled in described above.

After installing it, set the following values in the config file under the `[fn_mcafee_opendxl]` section

    dxlclient_config=<path_to_dxlclient.config_file>
    topic_listener_on=[True|False]  #Turns the listener on or off
    custom_template_dir=<Optional value to absolute path of custom directory if one exists>

### How to use the integration
1. Update and edit `app.config`:

		resilient-circuits configure -u

2. Set the `topic_listener` to `True`
3. Start Resilient Circuits with: `resilient-circuits run`

The Subscriber listens on the default topic, /mcafee/event/epo/threat/response,
and uses the default template. To customize the behavior of the integration,
please refer to the included documentation