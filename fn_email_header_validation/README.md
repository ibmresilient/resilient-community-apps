# Email Header Validation

This IBM QRadar SOAR Function package can be used to analyze DKIM and ARC headers on a RFC822 formatted email.
This email can be provide via a **SOAR Attachment**, **SOAR Artifact**, or string.
Once the analysis is complete, the user is informed if the headers authenticate or not through a **SOAR Note**.

## Table of Contents
- [Release Notes](#release-notes)
- [Installation](#installation)
	- [Install](#to-install-in-development-mode)
	- [Uninstall](#to-uninstall)
	- [Distribution](#to-package-for-distribution)
	- [Functions](#how-to-use-the-function)

## Release Notes
| Version | Date | Notes |
| ------- | ---- | ----- |
| 1.0.2 | 05/2025 | Converted example workflows to python3 |
| 1.0.1 | 04/2020 | AppHost Support Added | 
| 1.0.0 | 02/2019 | Initial Release |

## Installation
### To install in *development mode*:

    pip install -e ./fn_email_header_validation/

### To uninstall:

    pip uninstall fn_email_header_validation


### To package for distribution:

    python ./fn_email_header_validation/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz

### How to use the function

1. Import the necessary customization data into the SOAR platform:

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