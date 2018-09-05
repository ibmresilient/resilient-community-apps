# Function Email Header Avalidation

This IBM Resilient Function package can be used to analyze DKIM and ARC headers on a RFC822 formatted email.
This email can be provide via a **Resilient Attachment**, **Resilient Artifact**, or string.
Once the analysis is complete, the user is informed if the headers authenticate or not through a **Resilient Note**.


## To install in *development mode*:

    pip install -e ./fn_email_header_validation/

## To uninstall:

    pip uninstall fn_email_header_validation


## To package for distribution:

    python ./fn_email_header_validation/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz

## How to use the function

1. Import the necessary customization data into the Resilient platform:

		resilient-circuits customize

	This creates the following customization components:
	* Function inputs:
	    * `email_header_validation_target_email`
	    * `artifact_id`
	    * `attachment_id`
	    * `optional_incident_id`
	* Message Destination: `fn_email_header_validation`
	* Function: `email_header_validation_using_dkimarc`
	* Workflows:
	    * `example_of_email_header_validation_using_dkimarc_artifact`
	    * `example_of_email_header_validation_using_dkimarc_attachment`
	* Rule: `Email Header Avalidation Using DKIM/ARC`

2. Start Resilient Circuits:
    ```
    resilient-circuits run
    ```

3. Trigger the rule.