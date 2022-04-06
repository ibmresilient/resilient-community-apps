

# Validation Report for Jira App for IBM SOAR

| SDK Version       | Generation Time          | Command Line Arguments Provided |
| :---------------- | ------------------------ | ------------------------------- |
| 44.0.2810 | 2022/03/31 14:56:25 | `cmd`: validate, `settings`: /Users/bobleckel/.resilient/.sdk_settings.json, `package`: fn_jira, `validate`: True |

## App Details
| Attribute | Value |
| --------- | ----- |
| `display_name` | Jira App for IBM SOAR |
| `name` | fn_jira |
| `version` | 2.1.0 |
| `author` | IBM SOAR |
| `install_requires` | ['resilient_circuits>=44.0.0', 'jira~=2.0', 'pyjwt~=2.3; python_version>="3.0"', 'pyjwt~=1.7; python_version<"3.0"'] |
| `description` | Provides integration with JIRA for Issue Creation, Issue Transition and Comment Creation |
| `long_description` | This app allows for the tracking of SOAR Incidents and Tasks as Jira Issues. Bidirectional links are saved to allow for easy navigation between the applications.It also allows for the transitioning of Jira issues when the corresponding incident is closed and adds comments to the Jira issue when a Note is created in SOAR.Example rules and workflows can used used or modified to meet your business processes. |
| `url` | https://ibm.com/mysupport |
| `entry_points` | {'resilient.circuits.configsection': '/Users/bobleckel/soar/resilient-community-apps-worktrees/story/INT-3098/fn_jira/include_attachments_in_comments/fn_jira/fn_jira/util/config.py',<br> 'resilient.circuits.customize': '/Users/bobleckel/soar/resilient-community-apps-worktrees/story/INT-3098/fn_jira/include_attachments_in_comments/fn_jira/fn_jira/util/customize.py',<br> 'resilient.circuits.selftest': '/Users/bobleckel/soar/resilient-community-apps-worktrees/story/INT-3098/fn_jira/include_attachments_in_comments/fn_jira/fn_jira/util/selftest.py'} |
| `SOAR version` | 42.2.41 |
| `Proxy support` | Proxies supported if running on AppHost>=1.6 |

---


## `setup.py` file validation
| Severity | Name | Description | Solution |
| --- | --- | --- | --- |

<span style="color:green">Success</span>


---


## Package files validation

### `Dockerfile`
<span style="color:orange">WARNING</span>: `Dockerfile` does not match the template file (94% match). Difference from template:

```diff
--- Dockerfile template
+++ Dockerfile
@@ -7 +7 @@
-ARG RESILIENT_CIRCUITS_VERSION=44.0.0
+ARG RESILIENT_CIRCUITS_VERSION=44
@@ -9,4 +8,0 @@
-
-# Environment variable for any app to check if running in a container
-ARG APP_HOST_CONTAINER=1
-ENV APP_HOST_CONTAINER=${APP_HOST_CONTAINER}
@@ -38,0 +35,2 @@
+# uncomment to expose port only if a custom threat feed
+#EXPOSE 9000
```

Ensure that the `Dockerfile` was generated with the latest version of the resilient-sdk...


### LICENSE
<span style="color:teal">INFO</span>: `LICENSE` file is valid

It is recommended to manually validate the license. Suggested formats: MIT, Apache, and BSD


### `MANIFEST.in`
<span style="color:green">Pass</span>


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

### `payload_samples/jira_create_comment`
<span style="color:green">Pass</span>


### `payload_samples/jira_open_issue`
<span style="color:green">Pass</span>


### `payload_samples/jira_transition_issue`
<span style="color:green">Pass</span>

 
---
 

 

 

 

 