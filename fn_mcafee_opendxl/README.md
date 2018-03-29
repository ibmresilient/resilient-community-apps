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
1. Start Resilient Circuits with: `resilient-circuits run`
2. There are two sets of example Workflows and Rules which trigger the function:
    ```
    Workflow: (Example) McAfee Publish to DXL (Tag System); Rule: (Example) McAfee Publish to DXL (Tag System)
    Workflow: (Example) McAfee Publish to DXL (Set TIE Reputation); Rule: (Example) McAfee Publish to DXL (Set TIE Reputation)
    ```
Triggering either of the the manual rules will cause the function to be called.
