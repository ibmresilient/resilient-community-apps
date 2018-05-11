# Resilient Functions Integration to McAfee ATD

This function uploads a file or URL to McAfee to be analyzed and returns the report to the function's post-processer or adding the pdf/html attachment to the incident. The function will work on all artifacts that support an attachment, incident and task attachments, in addition to artifacts which support URLs.

## Installation

To install in "development mode"

    pip install -e ./fn_mcafee_atd/

After installation, the package will be accessible to `resilient-circuits run`.

To uninstall,

    pip uninstall fn-mcafee-atd

To package for distribution,

    python ./fn_mcafeee_atd/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install dist/<filename>.tar.gz
    
See the accompanying documentation for how to install to Resilient and configure.

## Configuration

1. Import the package's customization data into the Resilient Platform through the command:

    `resilient-circuits customize`

	This will create the following custom components:
	* Message Destinations: `McAfee ATD Message Destination`
	* Functions: `McAfee ATD Analyze URL`, `McAfee ATD Analyze File`
	* Custom Fields: `incident_id`, `artifact_id`, `attachment_id`, `task_id`, `mcafee_atd_report_type`, `mcafee_atd_url_submit_type`
	* Workflows: `(Example) McAfee ATD Analyze Artifact File`, `(Example) McAfee ATD Analyze Attachment`, `(Example) McAfee ATD Analyze URL`
	* Rules: `(Example) McAfee ATD Analyze Artifact File`, `(Example) McAfee ATD Analyze Attachment`, `(Example) McAfee ATD Analyze URL`

2. Update and edit `app.config` by first running:

		resilient-circuits configure -c, to start a new configuration file or
		resilient-circuits configure -u, to update an existing configuration

   Edit
```
    [fn_mcafee_atd]
    atd_url=https://127.0.0.1:8888
    atd_username=
    atd_password=
    # Amount of time in minutes before the function quits and throws an error
    timeout=30

    # Interval in seconds to wait to check if the file has finished being analyzed
    polling_interval=60

    # Value '0' indicates no user interaction is needed during sample analysis. Value '1' indicates user interaction
    # is needed during sample analysis.
    xMode=

    # Analyzer profile ID. The profile ID number can be found in the UI Policy/Analyzer Profile page.
    vm_profile_list=

    # parameter with values either 'run_now' or 'add_to_q', defaults to 'add_to_q'
    filePriority=add_to_q

    trust_cert=[True|False]
```
## Customization

1. For each of the workflows, review the inputs and the post-process scripts to ensure expected behavior is set to occur.

## Use

1. Start Resilient Circuits with:
    `resilient-circuits run`

2. From within Resilient and a given incident, run the manual Action `McAfee ATD Analyze Artifact File` to upload the file to ATD for analysis.

3. After it has been analyzed a report will be returned to Resilient