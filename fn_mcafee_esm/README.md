# McAfee ESM functions and polling integration

These functions are designed to access different api endpoints and
the polling integration is designed to bring new cases into Resilient as incidents.


To install in "development mode"

    pip install -e ./fn_mcafee_esm/

After installation, the package will be loaded by `resilient-circuits run`.


To uninstall:

    pip uninstall fn_mcafee_esm


To package for distribution:

    python ./fn_mcafee_esm/setup.py sdist

The resulting .tar.gz file can be installed using:

    pip install <filename>.tar.gz


Set the following values in the config file under the `[fn_mcafee_esm]` section:

    # url example: https://127.0.0.1
    esm_url=<your_esm_url>
    esm_username=<your_esm_username>
    esm_password=<your_esm_password>

    # If your ESM server uses a cert which is not automatically trusted by your machine, set trust_cert=False.
    verify_cert=[True|False]

    ## ESM Polling settings
    # How often polling should happen. Value is in seconds. To disable polling, set this to zero.
    esm_polling_interval=0
    incident_template=<location_of_incident_template_file>  # If not set uses default template.

Deploy to the Resilient platform:

    resilient-circuits customize

Creates the following items in the Resilient platform:

    #   Incident fields:
    #     mcafee_esm_case_id
    #   Function inputs:
    #     mcafee_esm_alarm_triggered_end_time
    #     mcafee_esm_alarm_triggered_start_time
    #     mcafee_esm_alarm_triggered_time_range
    #     mcafee_esm_case_id
    #     mcafee_esm_edit_case_json
    #     mcafee_esm_qry_config
    #     mcafee_esm_qry_event_type
    #     mcafee_event_ids_list
    #   DataTables:
    #     mcafee_esm_event_list
    #     mcafee_esm_triggered_alarms
    #   Message Destinations:
    #     mcafee_esm_message_destination
    #   Functions:
    #     mcafee_esm_edit_case
    #     mcafee_esm_get_case_detail
    #     mcafee_esm_get_case_events_detail
    #     mcafee_esm_get_list_of_cases
    #     mcafee_esm_get_triggered_alarms
    #     mcafee_esm_query
    #   Workflows:
    #     mcafee_esm_close_case
    #     mcafee_esm_get_case_details
    #     mcafee_esm_get_case_events_detail
    #     mcafee_esm_get_triggered_alarms
    #     mcafee_esm_query
    #     mcafee_get_case_list
    #   Rules:
    #     Close McAfee ESM Case
    #     McAfee ESM Get Case Details
    #     McAfee ESM Get Case Events Detail
    #     McAfee ESM Get Case List
    #     McAfee ESM Get Triggered Alarms
    #     Run McAfee ESM Query

#### How to use the ESM polling integration
1. Create a incident template file based on the default packaged file.
2. Set the location of this file in the app.config to `incident_template=<location to template file>`
3. In the app.config, set `esm_polling=True`
4. Start Resilient Circuits.

This starts the ESM polling integration. ESM will create a corresponding
incident in the Resilient platform, based on the open cases assigned to
the logged-in ESM user.


#### How to use the ESM Functions
1. Import necessary customization data into the Resilient Platform:

        resilient-circuits customize

2. Update and edit app.config:

        resilient-circuits config -u

3. Start Reslient Circuits:

        resilient-circuits run

4. Trigger a rule.