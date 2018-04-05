# McAfee TIE Searcher Function

This function uses the Python OpenDXL TIE Client to communicate with your TIE server, which is located at 
[GitHit: opendxl-tie-client-python](https://github.com/opendxl/opendxl-tie-client-python).

### Prerequisites
* System must have an OpenSSL version used by Python that supports TLSv1.2 (Version 1.0.1 or greater)
* ePO-managed environments must have 4.0 (or newer) version of DXL ePO extension installed

To install in "development mode"

    pip install -e ./fn_mcafee_tie/

To package for distribution,

    python ./fn_mcafee_tie/setup.py sdist
    
The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz

To uninstall:

    pip uninstall fn_mcafee_tie

Once installed the client must be provisioned. Click [here](https://opendxl.github.io/opendxl-client-python/pydoc/provisioningoverview.html) for more info on provisioning

Add values to the config file
    
    resilient-circuits configure -u

Set the following value in the config file under the `[fn_mcafee_tie]` section
    
    dxlclient_config=<path_dxl_config_file>

### How to use the function

1. Import the necessary customization data into the Resilient Platform:

		resilient-circuits customize

	This will create the following customization components:
	* Function inputs: `mcafee_tie_hash, mcafee_tie_hash_type`
	* Message Destinations: `mcafee_tie_md`
	* Functions: `mcafee_tie_search_hash`
	* Workflows: `mcafee_tie_hash_search_workflow`
	* Rules: `(Example) McAfee artifact hash search`

2. Update and edit `add.config`:

		resilient-circuits configure -u

3. Start Resilient Circuits with:
	`resilient-circuits run`
4. Trigger the rule