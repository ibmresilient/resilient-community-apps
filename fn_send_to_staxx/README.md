# Send to Staxx

*Craig @ Resilient Labs*

This function sends indicators from Resilient across to an Anomali Staxx Threat Intelligence Platform.

Staxx is a free Threat Intelligence and STIX/TAXII Solution available from [https://www.anomali.com/community/staxx](https://www.anomali.com/community/staxx)

The function gives options of user input or predefined tags, indicator types, TLP and Severity and whether the report is auto-approved or not. All of this can be customized from the workflow to keep inline with the intelligence procedures for your organization.

## Installation

Installation of the function requires the setup of an integration server - see the following guide for more information.

It can be installed via the following commands

```
pip install fn-send-to-staxx-1.0.0.tar.gz
```

Next, add the configuration (in this case, it doesn't require any)

```
resilient-circuits config -u
```

Finally add the example datatable, workflow and function to the system


```
resilient-circuits customize
```

You can now restart resilient-circuits to load the new function.
