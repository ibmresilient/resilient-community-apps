# Resilient Function - ldap_search

This Resilient Function package can be used to execute an an LDAP search/query from a workflow using the Functions feature of the Resilient
Circuits integration framework.

Prerequisites:
```
resilient
resilient_circuits
ldap3
```
* Can be used in a Resilient workflow to populate/update a datatable.
* For more info about the python ldap3 module, please visit http://ldap3.readthedocs.io/


## Environment

This package requires that it is installed on a RHEL platform and that the resilient-circuits application is running.
Install this package with 'pip', or `python setup.py install`.
To set the config values in the app.config file run `resilient-circuits config -u`.

Config values example 1:
```
[fn_ldap_search]
server=localhost
port=389
user=cn=admin,dc=example,dc=com
password=admin
auth=SIMPLE
use_ssl=False
connect_timeout=10
```

Config values example 2 (Active Directory):
```
[fn_ldap_search]
server=adserver
port=389
user=mydomain\myuser
password=mypass
auth=SIMPLE
use_ssl=False
connect_timeout=10
```

Config values example 3 (Active Directory):
```
[fn_ldap_search]
server=adserver
port=389
domain=mydomain
user=myuser
password=mypass
auth=NTLM
use_ssl=False
connect_timeout=10
```

Run with: `resilient-circuits run`.

## ldap_search Example

The LDAP search requires 4 input parameters. The parameters are setup from a Resilient systems workflow on the Resilient console.
The following are examples of setup of each parameter using a simple workflow pre-processing script. The %param% token
will be replaced by the actual inputs.param value at time of execution.

```
inputs.ldap_search_base = "dc=example,dc=com"
inputs.ldap_search_filter = "(&(objectClass=person)(uid=%ldap_param%))"
inputs.ldap_search_attributes = "cn,sn,mail,telephoneNumber"
inputs.ldap_param =  artifact.value
```
The results returned to Resilient will be in JSON format and will consist of a list of
entries where each entry has a 'dn' entry and a set of attributes
```
{
  "entries": [
    {"dn': "entry1_dn1_value", "entry1_attribute2", "entry1_attribute3", ... },
    {"dn": "entry2_dn2_value", "entry2_attribute2", "entry2_attribute3", ... }
    ...
  ]
}
```
