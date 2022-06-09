

# Validation Report for fn_utilities

| SDK Version       | Generation Time          | Command Line Arguments Provided |
| :---------------- | ------------------------ | ------------------------------- |
| 43.1.1.dev63+g4c39febb | 2022/01/11 11:29:27 | `verbose`: True, `cmd`: validate, `settings`: /Users/bobleckel/.resilient/.sdk_settings.json, `package`: fn_utilities, `validate`: True |

## App Details
| Attribute | Value |
| --------- | ----- |
| `display_name` | **NOT FOUND** |
| `name` | fn_utilities |
| `version` | 2.0.6 |
| `author` | IBM Resilient |
| `author_email` | support@resilientsystems.com |
| `install_requires` | ['six==1.14.0', 'resilient_circuits>=30.0.0', 'resilient-lib>=34.0.0', 'openpyxl>=2.5.3', 'pyOpenSSL>=18.0.0', 'cryptography>=2.3', 'pywinrm>=0.3.0', 'json2html', 'lxml', 'mail-parser>=3.9.3', 'paramiko', 'defusedxml>=0.7.1', 'pdfid>=1.0.4', 'chardet==4.0.0'] |
| `description` | Useful workflow functions for common automation and integration activities in the Resilient platform. |
| `long_description` | Resilient functions simplify development of integrations by wrapping each external activity    into an individual workflow component. These components can be easily installed, then used and combined in Resilient    workflows. The Resilient platform sends data to the function component that performs an activity then returns the results    to the workflow. The results can be acted upon by scripts, rules, and workflow decision points to dynamically orchestrate    the security incident response activities. |
| `url` | http://ibm.biz/resilientcommunity |
| `entry_points` | {'resilient.circuits.configsection': '/Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities/fn_utilities/util/config.py',<br> 'resilient.circuits.customize': '/Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities/fn_utilities/util/customize.py',<br> 'resilient.circuits.selftest': '/Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities/fn_utilities/util/selftest.py'} |
| `python_requires` | >=3 |
| `SOAR version` | 35.2.32 |
| `Proxy support` | Proxies not fully supported unless running on AppHost>=1.6 and resilient-circuits>=42.0.0 |

---


## `setup.py` file validation
| Severity | Name | Description | Solution |
| --- | --- | --- | --- |
| <span style="color:orange">WARNING</span> | display_name not found | `setup.py` file is missing attribute `display_name` or missing the value for the attribute | Set `display_name` to an appropriate value. This value is displayed when the app is installed |
| <span style="color:orange">WARNING</span> | invalid value in `setup.py` | `python_requires` version `3.0` is not supported | Suggested value is `python_requires>=3.6` |


---


## Package files validation

### `MANIFEST.in`
<span style="color:orange">WARNING</span>: `MANIFEST.in` is missing the following lines: [`recursive-include fn_utilities/util *`, `include icons/*.png`, `recursive-include payload_samples/*/ *.json`, `include tox.ini`, `recursive-include tests/ *`, `global-exclude *.bak`]

The `MANIFEST.in` file is the list of files to be included during packaging. Be sure it is up to date


### `Dockerfile`
<span style="color:orange">WARNING</span>: `Dockerfile` does not match the template file (77% match). Difference from template:

```diff
--- Dockerfile template
+++ Dockerfile
@@ -1,2 +1 @@
-# docker build -t ibmresilient/fn_utilities:2.0.6 -t ibmresilient/fn_utilities:latest .
-
+# docker build -t resilient/{ext} .
@@ -4,0 +4,2 @@
+# rc-data-feeder will build plugins from a base image
+#FROM resilient/rc-data-feeder-base
@@ -7 +8 @@
-ARG RESILIENT_CIRCUITS_VERSION=43.0.0
+ARG RES_CIRCUITS_VERSION=40.0
@@ -14 +15 @@
-# Update to latest packages, user 0 for root privilege
+# update to latest packages, user 0 for root privilege
@@ -16 +16,0 @@
-
@@ -21 +21,6 @@
-RUN pip install "resilient-circuits>=${RESILIENT_CIRCUITS_VERSION}"
+RUN pip install resilient-circuits>=${RES_CIRCUITS_VERSION}
+
+# install and upgrade six to satisfy fn_utilities requirement
+RUN pip install six==1.14.0
+# install and upgrade cryptography to satisfy fn_utilities requirement
+RUN pip install --upgrade cryptography
@@ -25,2 +30,9 @@
-#RUN yum -y update && yum clean all
-#RUN yum -y install <package>
+RUN yum -y update && yum clean all
+# whois, traceroute, dig and nsloookup
+RUN yum install -y bind-utils net-tools
+RUN yum install -y http://mirror.centos.org/centos/8/AppStream/x86_64/os/Packages/whois-nls-5.5.1-2.el8.noarch.rpm
+RUN yum install -y http://mirror.centos.org/centos/8/AppStream/x86_64/os/Packages/whois-5.5.1-2.el8.x86_64.rpm
+RUN yum install -y http://mirror.centos.org/centos/8/BaseOS/x86_64/os/Packages/traceroute-2.1.0-6.el8.x86_64.rpm
+# changes for mail parsing of Outlook emails
+RUN yum install -y perl cpan
+RUN cpan -fTi Email::Outlook::Message
@@ -31,0 +44,2 @@
+# install and upgrade cryptography to satisfy fn_utilities requirement
+RUN pip install --upgrade cryptography
@@ -64 +78,2 @@
-# arbitrary user, support running as non-root. Required on OpenShift. Generally a good practice.
+# arbitrary user, support running as non-root.  Required on OpenShift.
+# Generally a good practice.
@@ -66,0 +82 @@
+
```

Ensure that the `Dockerfile` was generated with the latest version of the resilient-sdk...


### LICENSE
<span style="color:teal">INFO</span>: `LICENSE` file is valid

It is recommended to manually validate the license. Suggested formats: MIT, Apache, and BSD


### `apikey_permissions.txt`
<span style="color:green">Pass</span>


### `entrypoint.sh`
<span style="color:green">Pass</span>


### ``config.py``
<span style="color:green">Pass</span>


### ``customize.py``
<span style="color:green">Pass</span>


### `README.md`
<span style="color:green">Pass</span>


### `app_logo.png`
<span style="color:green">Pass</span>


### `company_logo.png`
<span style="color:green">Pass</span>


### LICENSE
<span style="color:green">Pass</span>

 
---
 

## Payload samples validation

### `payload_samples/utilities_attachment_hash`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_attachment_hash` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_attachment_to_base64`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_attachment_to_base64` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_attachment_zip_extract`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_attachment_zip_extract` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_attachment_zip_list`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_attachment_zip_list` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_base64_to_artifact`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_base64_to_artifact` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_base64_to_attachment`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_base64_to_attachment` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_call_rest_api`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_call_rest_api` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_domain_distance`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_domain_distance` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_email_parse`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_email_parse` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_excel_query`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_excel_query` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_expand_url`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_expand_url` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_extract_ssl_cert_from_url`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_extract_ssl_cert_from_url` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_get_contact_info`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_get_contact_info` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_json2html`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_json2html` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_parse_ssl_certificate`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_parse_ssl_certificate` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_pdfid`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_pdfid` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_resilient_search`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_resilient_search` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_shell_command`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_shell_command` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_string_to_attachment`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_string_to_attachment` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_timer`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_timer` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```


### `payload_samples/utilities_xml_transformation`
<span style="color:red">CRITICAL</span>: `output_json_example.json` and `output_json_schema.json` for `utilities_xml_transformation` not found

Reload code using ```resilient-sdk codegen -p /Users/bobleckel/soar/resilient-community-apps-worktrees/resilient-community-apps/fn_utilities --reload```

 
---
 

 

 

 

 