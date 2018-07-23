# Function Joe Sandbox Analysis

This IBM Resilient Function package can be used to execute a **Joe Sandbox Analysis** of a file or URL. 

Once the analysis is complete, the user is informed if the file or URL is **clean** or **malicious** via a **Resilient Note**. The related Joe Sandbox Analysis report is then uploaded to the Resilient platform as an attachment. The function has the following capabilities:

* Supports an attachment or artifact that is a file, or where the artifact's value contains a URL.
* Allows users to select the type of report, PDF, HTML, or JSON, which is returned from Joe Sandbox.
* Supports a proxy. Just add your proxy details to the `app.config` file.
* •	Is dependent on **Joe Security's python module, jbxapi**.See [here](https://github.com/joesecurity/joesandboxcloudapi) for more details


## To install in *development mode*:

    pip install -e ./fn_joe_sandbox_analysis/

## To uninstall:

    pip uninstall fn_joe_sandbox_analysis


## To package for distribution:

    python ./fn_joe_sandbox_analysis/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz

## Add Joe Sandbox configuration details to the config file:

    resilient-circuits config -u

Set the following values in the config file (`~/.resilient/app.config`) under the `[fn_joe_sandbox_analysis]` section:

```
jsb_accept_tac=True
jsb_api_key=
jsb_analysis_url=
jsb_analysis_report_default_ping_delay=120
jsb_analysis_report_request_timeout=1800
#jsb_http_proxy=http://user:pass@10.10.1.10:3128
#jsb_https_proxy=http://user:pass@10.10.1.10:1080
```

## How to use the function

1. Import the necessary customization data into the Resilient platform:

		resilient-circuits customize

	This creates the following customization components:
	* Function input: `jsb_report_type, ping_delay`
	* Message Destination: `fn_joe_sandbox_analysis`
	* Function: `fn_joe_sandbox_analysis`
	* Workflows: `example_joe_sandbox_analysis_attachment, example_joe_sandbox_artifact`
	* Rules: `Example: Joe Sandbox Analysis [Artifact], Example: Joe Sandbox Analysis [Attachment]`

2. Update and edit `app.config`:

		resilient-circuits configure -u

3. Start Resilient Circuits:
    ```
    resilient-circuits run
    ```

4. Trigger the rule.
