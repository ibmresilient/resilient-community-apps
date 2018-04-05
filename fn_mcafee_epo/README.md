
## Function McAfee Tagging ePO Asset

To install in development mode:

    pip install -e ./fn_mcafee_epo/

After installation, you can load the package with:
    `resilient-circuits run`.

To uninstall:

    pip uninstall fn_mcafee_epo

To package for distribution:

    python ./fn_mcafee_epo/setup.py sdist

The resulting .tar.gz file can be installed using:

    pip install <filename>.tar.gz

Add ePO configuration details to the config file:

    resilient-circuits configure -u

Set the following values in the config file under the `[fn_mcafee_epo]` section:
    
    epo_url=https://<your_epo_server>:<port>
    epo_username=<your_epo_username>
    epo_password=<your_epo_password>
    epo_trust_cert=true/false
    
### How to use the function

1. Import the necessary customization data into the Resilient Platform:

		resilient-circuits customize

	This will create the following customization components:
	* Function inputs: `mcafee_epo_systems, mcafee_epo_tag`
	* Message Destinations: `mcafee_epo_message_destination`
	* Functions: `mcafee_tag_an_epo_asset`
	* Workflows: `mcafee_tag_epo_asset_workflow`
	* Rules: `(Example) McAfee Tag ePO Asset`
2. Update and edit `add.config`:

		resilient-circuits configure -u

3. Start Resilient Circuits with:
    `resilient-circuits run`

4. Trigger the rule.
