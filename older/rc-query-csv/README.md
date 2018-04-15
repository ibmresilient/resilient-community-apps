Query CSV Files From Resilient
==============================

Use Case:  Search a CSV file for rows that match a column value, or a regular expression.

This integration can be run on the Resilient appliance or anywhere else.  
The code is written in Python, and can be extended for your own purposes.

Requires: Python version 2.7.9+ or 3.4+  
Requires: rc-query-runner

## Resilient server setup

You must configure the following customizations to the Resilient server.
Open the Administrator Settings --> Actions, then:

### Message Destination

Create a Queue message destination with programmatic name `query_csv`.
Select Yes for "expect acknowledgement", and add the integration user
to its users list.

### Rules

Create automatic or manual rules with names corresponding to your query definition files.


## Tests
Tests are **destructive**.  They remove all configuration (message destinations, rules, etc) and replace with the required test configuration.
These tests should *ONLY* be run against an organization with nothing you want to save!   

Install the `pytest_resilient_circuits` package.

To run the included tests, cd to the parent directory of your project, then:
```
  pytest -s --resilient_email <resilient account email> --resilient_host <IP or hostname> --resilient_password <resilient account password> --resilient_org <org name>
``` 

