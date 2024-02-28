# Ansible
## Table of Contents
  - [About This Package](#about-this-package)
  - [Features](#features)
  - [Package Components](#package-components)
  - [App Host Installation](#app-host-installation)
  - [Integration Server Installation](#integration-server-installation)
  - [Function Inputs](#function-inputs)
  - [Function Output](#function-output)
  - [Considerations](#considerations)
  - [App Host sshPass Support](#app-host-sshpass-support)
---

## About This Package:
This package contains functions that integrate with Ansible to run playbooks and modules for remote host execution.

## History

| Version| Comment |
| ------- | ------ |
| 1.2 | Support for App Host |
| 1.1 | Change result payload format to JSON returned to Resilient |
 * For customers upgrading from 1.0, the example workflows will use different post-processing script logic, based on the json results returned.

## Features:
* Run pre-written Ansible Playbooks from the Resilient platform, using parameter substitution.
* Run Ansible Modules for ad-hoc command execution.
* Run Resilient Rules at the Incident and Artifact levels.

Additional documentation on Ansible can be found at [the Ansible website](https://docs.ansible.com/).

### Package Components
* Functions:
  - fn_ansible
  - fn_ansible_module
* Workflows:
  - Example: Ansible - Run a Module
  - Example: Ansible - Run a Playbook from an Incident
  - Example: Ansible - Run a Playbook on an Artifact
* Rules:
  - Example: Ansible - Run a Module
  - Example: Ansible - Run a Playbook
  - Example: Ansible - Run a Playbook from an Artifact


## App Host Installation
All the components for running Ansible in a container already exist when using the App Host app. The remainder of this section details the Ansible configuration file changes.

Under the Configuration Tab for an App, build out the ansible-runner files needed per the [ansible-runner convention](https://docs.ansible.com/ansible/latest/installation_guide/intro_configuration.html). The necessary files are the `hosts` file, ssh_key and your yml playbooks. Build these files under `/var/rescircuits/ansible` and ensure that the app.config file contains the same reference:

```
[fn_ansible]
runner_dir=/var/rescircuits/ansible
artifact_dir=/tmp
```

### Playbooks
When adding playbooks through the Configuration tab of an App, ensure the File Path is `/var/rescircuits/ansible/project`.

Note: Playbooks and modules cannot be run within the container environment.

The minimum Ansible files needed are:
* hosts, and
* playbooks

Your environment may require more configuration files, such as ssh_key and envvars.

This is an example of the configuration files used including
several yaml files.
![screenshot](./screenshots/ansible_config_files.png)

If you require additional ansible modules, additional effort is needed to include them as files in the Configuration tab.

### Limitations
Presently, there are limitations in the use of containers when playbook parameters sent from Resilient
are used with any file defined in `/var/rescircuits/ansible/env`.

## Integration Server Installation
### Prerequisites:
This integration relies on the installation of the ansible solution on the integration server. The process of installing ansible can be followed [here](https://docs.ansible.com/ansible/latest/installation_guide/).

* ansible >= 2.8.1
* ansible-runner >= 1.3.4
* Resilient platform >= v31.0.0
* Integrations Server Resilient Circuits >= v30.0.0
* Ansible config directory per the [ansible-runner convention](https://docs.ansible.com/ansible/latest/installation_guide/intro_configuration.html)

* Ansible relies on a system library `sshpass`. Depending on your Integration Server operation system, different procedures are required to install this system library.

* For RHEL servers, the [Red Hat Developer Toolset](https://access.redhat.com/documentation/en-us/red_hat_developer_toolset/8/html/user_guide/chap-red_hat_developer_toolset) is needed to build the ansible runtime environment. This may also require a registered subscription manager to install.

This package requires that it is installed on a RHEL or CentOS platform and uses the Resilient Circuits framework.

* Unzip the package downloaded from the IBM App Exchange
```
    $ unzip app-fn_ansible-<version>.zip
```
* To install the package, run:

    ```
    $ [sudo] pip install fn_ansible-<version>.tar.gz
    ```

* To import the function, example rules and workflows into your Resilient platform, run:

    ```
    $ resilient-circuits customize -l fn-ansible
    ```
* To update your `app.config` file with the required Ansible configurations, run:

    ```
    $ resilient-circuits config -u -l fn-ansible
    ```

* Within the `app.config` file, edit the following configuration data:

    ```
    [fn_ansible]
    runner_dir=</full/path/to/your/ansible/directory>
    # temporary files collected when running a module or a playbook
    artifact_dir=</full/path/to/artifacts/directory>
    # change this value to trim the collection of previous process runs
    artifact_retention_num=0
    ```

* To uninstall:

    ```
    $ [sudo] pip uninstall fn-ansible
    ```

* Run Resilient Circuits:

    ```
    $ resilient-circuits run
    ```

### Sample Workflow:
 ![screenshot](./screenshots/sample_workflow.png)

## Function Inputs:
| Input Name | Type | Required | Example | Info |
| ------------- | :--: | :-------:| ------- | ---- |
| ansible_playbook_name | String | Yes | "my_playbook" or "my_playbook.yml" | Identifies target playbook to run |
| ansible_parameters | String | No | "host_names=192.168.1.4" | Substitution variables for a Playbook at runtime. For example, a Playbook containing `hosts: "{{host_names}}"` will be replaced using the example value of 196.168.1.4. Use semi-colons (;) to separate different parameters. |

Some parameters can contain more than one value. In these cases, use a comma (,) to separate the values. Example: `host_names=192.168.56.1,192.168.56.2`.

When using playbooks run against artifacts, an additional parameter is sent specifying the artifact value to the playbook as `artifact_value=<artifact_value>`. Therefore, in your playbook, ensure to add `{{artifact_value}}` for value substitution.

 ![screenshot](./screenshots/2.png)
## Function Output:
Results returned to the Resilient platform from an Ansible function are in the following payload pattern:

```
{
  'version': '1.0',
  'success': True,
  'reason': None,
  'inputs': {
    u'ansible_playbook_name': u'find_files2',
    u'ansible_parameters': u'age=-2d; host_names=192.168.56.3,192.168.56.4; path=/usr/local/bin/'
  },
  'metrics': {
    'package': 'fn-ansible',
    'timestamp': '2019-06-19 11:06:39',
    'package_version': '1.0.0',
    'host': 'xxx.cambridge.ibm.com',
    'version': '1.0',
    'execution_time_ms': 12549
  },
  'content': {
    u'192.168.56.4': {
      'detail': 'fatal: [192.168.56.4]: UNREACHABLE! => {"changed": false, "msg": "timed out", "unreachable": true}',
      'summary': 'failed'
    },
    u'192.168.56.3': {
      'detail': '',
      'summary': 'failed'
    }
  },
  'raw': '{"192.168.56.4": {"detail": "fatal: [192.168.56.4]: UNREACHABLE! => {\\"changed\\": false, \\"msg\\": \\"timed out\\", \\"unreachable\\": true}", "summary": "failed"}, "192.168.56.3": {"detail": "", "summary": "failed"}'
}
```

The following Post-Processing Script cleans up the payload and adds it as an incident note:

```
if len(results['content'].keys()) == 0:
  note = u"No results returned on parameters: {}".format(results['inputs'])
else:
  for item in results['content']:
    note = u"{} - {}\n{}".format(item, results['inputs'], str(results['content'][item]['detail']))

incident.addNote(helper.createPlainText(note))
```

For very large data results, it may not be practical to save the results as a Note. Instead, the fn_utilities function `Utilities: String to Attachment` can be added to your workflow to send your Ansible results to an attachment. In this case, workflow properties are used to retain the results of this function for use by downstream functions.

## Considerations
* Only the ansible-runner `synchronous` capability is supported.
* Playbook and artifact names must not contain unicode characters. This is a limitation in the ansible-runner package ( <= 2.8.1) which should be resolved in a future release.
* The app.config setting `artifact_retention_num` is available to clean up previous execution files older than the specified days. Use a value of 0 to specify no deletion.
* Consider using Rule Activity Field select lists for Ansible module name and parameter restrictions. This ensures that only specific commands are used for ad-hoc executions.
* Also consider using Rule Activity Field select lists for Ansible playbook names for similar reasons to ensure only specific playbooks are supported through Resilient.
* The workflow associated with a module or playbook function will remain blocked until all host executions are complete and the results are returned. The ansible-runner `Asynchronous` operation corrects this restriction but remains a future enhancement.
* Playbooks should use the `debug` statement to return findings back to Resilient. The example below runs the `find` module, returning the file found using the debug statement.

```yaml
- hosts: "{{host_names}}"
  tasks:
  - name: Recursively find files
    find:
      paths: "{{path}}"
      age: "{{age}}"
      recurse: yes
      pattern: '*'
    register: files_matched

  - debug:
      msg: "{{ files_matched.files }}"
```

## App Host sshPass Support
You may find that you require the sshPass package for your use of Ansible. This package uses the [GPLv2 license](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html) and
this license restricts IBM from building and distributing a container under our [International License Agreement](https://www-03.ibm.com/software/sla/sladb.nsf/pdf/ilan/$file/ilan_en.pdf).

If you require sshPass, you can build your own container by modifying the `Dockerfile` in the fn_ansible-x.x.x.tar.gz archive and uncomment the following
RUN command. See the documentation on [hosting your own container registry for App Host](https://www.ibm.com/support/knowledgecenter/SSBRUQ_37.0.0/doc/container_apps.html)
for the use of a private registry with App Host.

```
## ---- section for changes ----
# uncomment to support sshpass in your container
#RUN wget http://mirror.pit.teraswitch.com/fedora/epel/epel-release-latest-8.noarch.rpm && \
#    rpm -ivh epel-release-latest-8.noarch.rpm && \
#    yum --enablerepo=epel -y install sshpass
```