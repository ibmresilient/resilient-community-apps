# Resilient Function Integration for Cisco AMP for Endpoints

This Resilient function package can be used to perform the following actions from a workflow using the Functions feature of the Resilient
Circuits integration framework.

* Retrieve list of all computers with agents deployed on them, in a Cisco AMP for endpoints environment.
* Get information about a specific computer by guid
* Get list of all activities associated with a particular computer, search by guid.
* Search all computers for any events or activities associated with a file or network operation


##Prerequisites:
```
Resilient version 31 or later
resilient_circuits version 30 or later
```
* For more info about Cisco AMP for Endpoints, please visit https://www.cisco.com/c/en/us/products/security/amp-for-endpoints/index.html
* For more info about Cisco AMP for Endpoints Rest API, please visit https://api-docs.amp.cisco.com/


## Environment

This package requires that it is installed on a RHEL or CentOS platform and that the resilient-circuits application is running.
Install this package with 'pip', or `python setup.py install`.
To set the config values in the app.config file with a new resilient instance run `resilient-circuits config -c`.
To set the config values in the app.config file with an existing resilient instance run `resilient-circuits config -u`.

Config values example:
(Note: The api token will be supplied by Cisco and will be in uuid format)
```
[fn_cisco_amp4ep]
base_url=https://api.amp.cisco.com/
# Version of api to use.
api_version=v1
# The client id will be generated on the Cisco AMP for endpoints dashboard.
client_id=01234abcde56789efedc
# The api_token will be generated on the Cisco AMP for endpoints dashboard and will be will be in uuid format.
api_token=abcd1234-a123-123a-123a-123456abcdef
# Settings for access to cisco AMP website via a proxy
#http_proxy=http':'http://proxy:80
#https_proxy=https':'http://proxy:80
# Query results global limit override for the integration global default which is set to 1000.
#query_limit=1000
# Max number of retry attempts on Rate Limit exception
max_retries=3
```

Run with: `resilient-circuits run`.

## Supported functions:
```
fn_amp_get_computer
fn_amp_get_computers
fn_amp_get_computer_trajectory
fn_amp_get_activity
fn_amp_get_file_lists
fn_amp_get_file_list_files
fn_amp_set_file_list_files
fn_amp_delete_file_list_files
fn_amp_get_event_types
fn_amp_get_events
fn_amp_get_groups
fn_amp_move_computer
```
## Sample workflows provided:
```
Example: AMP add artifact from activity
Example: AMP Add artifact from event
Example: AMP add artifact from trajectory
Example: AMP delete file from list
Example: AMP get computer by guid
Example: AMP get computer by name
Example: AMP get computers with activity
Example: AMP get computer trajectory
Example: AMP get computer trajectory by activity
Example: AMP get events
Example: AMP get events by type
Example: AMP get event types
Example: AMP get file lists
Example: AMP get files from list
Example: AMP get group name by guid
Example: AMP get groups
Example: AMP move computer
Example: AMP set file in list
```
## Sample rules provided:
```
Example: AMP add artifact from activity
Example: AMP add artifact from event
Example: AMP add artifact from trajectory
Example: AMP delete file from list
Example: AMP get computer by guid
Example: AMP get computer by name
Example: AMP get computers with activity
Example: AMP get computer trajectory
Example: AMP get computer trajectory by activity
Example: AMP get events
Example: AMP get events by type
Example: AMP get event types
Example: AMP get file lists
Example: AMP get files from list
Example: AMP get group name by guid
Example: AMP get groups
Example: AMP move computer
Example: AMP set file in list
```
## Get Computer Example

The fn_amp_get_computer function requires one input parameter: amp_conn_guid. 
The following example shows the configuration of the parameter using a simple workflow pre-processing script:

```
inputs.amp_conn_guid = artifact.value
```
For example, if artifact.value is set to guid 00da1a57-b833-43ba-8ea2-79a5ab21908f, the results
returned to will be in JSON format similar to the following:
```
{
  "response": {
    "version": "v1.2.0",
    "data": {
      "operating_system": "Windows 7, SP 1.0",
      "connector_guid": "00da1a57-b833-43ba-8ea2-79a5ab21908f",
      "links": {
        "trajectory": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f/trajectory",
        "computer": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f",
        "group": "https://api.amp.cisco.com/v1/groups/9d55c259-c960-488b-9b2d-06478fa19ee4"
      },
      "external_ip": "145.1.91.176",
      "group_guid": "9d55c259-c960-488b-9b2d-06478fa19ee4",
      "hostname": "Demo_AMP",
      "install_date": "2018-05-22T16:53:27Z",
      "network_addresses": [
        {
          "ip": "255.240.221.92",
          "mac": "a0:28:f5:c3:71:d5"
        }
      ],
      "connector_version": "6.0.9.10685",
      "internal_ips": [
        "255.240.221.92"
      ],
      "policy": {
        "guid": "a98a0f97-4d54-4175-9eef-b8dee9c8e74b",
        "name": "Audit"
      },
      "active": true,
      "last_seen": "2018-05-22T16:53:27Z"
    },
    "metadata": {
      "links": {
        "self": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f"
      }
    }
  },
  "query_execution_time": "2018-08-09 11:56:02"
}
```
