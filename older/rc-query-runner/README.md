Query-Runner Component
======================

This is a resilient-circuits component providing a query execution framework.

This component itself doesn't execute any queries.  Instead, it installs a base set of functionality for other query integrations to use.
Any query-runner action, triggered by a Resilient rule, can be defined by a "query definition file" that tells Query Runner:
- How to construct a query, using a template file named by the action,
- How to map the query results onto Resilient incident fields, data tables, artifacts and other objects.

To implement your own query component, 
* Create a Python class that inherits from QueryRunner,
* Give it a callback function - this will be called when a query runs.
* The result of your callback is then mapped onto Resilient data using the query definition file.

Query components provided in this repository can query a variety of systems including LDAP, Splunk, and QRadar.

Refer to the [Query Runner Integration Guide](https://github.com/ibmresilient/resilient-community-apps/blob/master/rc-query-runner/docs/Query%20Runner%20Integration%20Guide.pdf)
for additional details.
 
