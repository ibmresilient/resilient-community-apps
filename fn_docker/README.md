# IBM Resilient Integration with Docker

The Resilient Integration with Docker provides tools to integrate Docker into your Incident Response Plan. The integration brings Automation and Orchestration capabilities for Dockerised tools that can be used for Malware Research and Incident Response.

**This package contains 1 Function, 3 Workflows, 3 Rules and 1 Data Table that help you integrate with Docker**

 ![screenshot](./screenshots/1.png)
## Table of Contents
- [Integration app.config settings:](#integration-appconfig-settings)
- [Image specific app.config sections](#image-specific-appconfig-sections)
- [Function: Run Docker Container](#1-run-docker-container)
- [Workflow: Send Artifact To Docker Container](#1-send-artifact-to-docker-container)
- [Workflow: Send Attachment To Docker Container](#2-send-attachment-to-docker-container)
- [Rules:](#rules)
- [Datatable:](#datatable)
    - [Docker External Ticket Status Datatable](#docker-external-ticket-status-datatable)
    - [API Name:](#api-name)
    - [Columns:](#columns)
    - [Display the Datatable in an Incident](#display-the-datatable-in-an-incident)

# Connection options and installation:  

This integration requires access to a Docker daemon, in order to run containers and get output. Typically the Docker daemon would be on the same machine that you intend to run the containers from so this would mean installing Docker on your integration server itself.
To install Docker on your Integration Server see [this link](https://docs.docker.com/install/linux/docker-ee/rhel/). 

Alternatively, if you have an exposed Docker daemon that you can connect to and use, you may instead opt to connect to and run containers using this daemon instead of installing Docker on your integration server. This is done by specifying the `docker_remote_url` value in the app.config section which will specify the location of the Docker daemon and also which remote connection option to use, of which there are two: TCP and SSH.

# app.config settings:
There are two ways to configure settings for this Integration. You can choose to configure general settings for the Integration itself such as which method to use for connections. 
Additionally, each image you intend to create containers from can have its own app.config section.

## Integration app.config settings:
The Integration has a number of app.config settings which manage how a connection to a Docker daemon is performed and also which images are approved to be run by the integration. The approved images list includes only the shortname of the docker image e.g remnux/volatility -> volatility is the shortname.

```bash
docker_approved_images=<imagename>,<imagename> # Which images are approved to be run e.g volatility,nsrl
docker_use_remote_conn=<True/False>
docker_remote_url=<URL>
```

## Image specific app.config sections 
Each Docker image has the opportunity to use its own app.config section for getting options which are specific to that image only. This includes the images full name, volume bindings if that container requires volumes and the command which will be sent to the built container.

Image specific app.config sections are found by searching for the image shortname postfixed to `fn_docker_`. This means that to enable image specific options that you need your section should be named this way e.g `fn_docker_volatility`. 
```bash
[fn_docker_volatility]
docker_image=remnux/volatility
primary_output_dir=/tmp/bind_folder
primary_internal_dir=/home/nonroot/memdumps
docker_extra_<arguement>=<string> # Allows you to pass an extra arguement used for docker container creation. See documentation
cmd_operation=pslist
cmd=vol.py -f {{internal_vol}}/{{attachment_input}} {{operation}}

```

Each image app.config section has the opportunity to include a number of extra arguements which will be used during container creation/invocation. This brings you, the designer, flexibility to configure different aspects of how the container will be run. For a list of which arguements you can modify this way [see here](). 

There are a number of arguements which you cannot modify as they are explicity set by the integration, these are :

+ Image -- The image is set in the app.config
+ Command -- The command is set in the app.config
+ Detach -- This is set to `True`. 
+ Remove -- This is set to `False`, the container is removed after logs and stats are gathered.

## Functions:

## **1: Run Docker Container**

### Function Inputs:

| Input Name | Type | Required | Example | Info |
| ------------- | :--: | :-------:| ------- | ------- |
| `incident_id` | `Number` | Yes | `2105`  | ------- |
| `task_id` | `Number` | No | `None` | ------- |
| `artifact_id` | `Number` | No | `None` | ------- |
| `attachment_id` | `Number` | No | `None` | ------- |
| `docker_image` | `Select` | Yes | `nsrl` | `Which image will be used by the function` |
| `docker_input` | `String` | No | `60B7C0FEAD45F2066E5B805A91F4F0FC` | `The input being fed to the container, only used for artifact level workflwos ` |

### Function Output:

```python
results = {
    'content': {
        'container_exit_status': {
            'Error': None,
            'StatusCode': 0
        },
        'container_id': '0ce1ece10633d13ea159a2b013ae0256f0e2ae29e247492c811b8525d560b30c',
        'container_stats': {
            'blkio_stats': {
                'io_merged_recursive': None,
                'io_queue_recursive': None,
                'io_service_bytes_recursive': None,
                'io_service_time_recursive': None,
                'io_serviced_recursive': None,
                'io_time_recursive': None,
                'io_wait_time_recursive': None,
                'sectors_recursive': None
            },
            'cpu_stats': {
                'cpu_usage': {
                    'total_usage': 0,
                    'usage_in_kernelmode': 0,
                    'usage_in_usermode': 0
                },
                'throttling_data': {
                    'periods': 0,
                    'throttled_periods': 0,
                    'throttled_time': 0
                }
            },
            'id': '0ce1ece10633d13ea159a2b013ae0256f0e2ae29e247492c811b8525d560b30c',
            'memory_stats': {},
            'name': '/tender_goldwasser',
            'num_procs': 0,
            'pids_stats': {},
            'precpu_stats': {
                'cpu_usage': {
                    'total_usage': 0,
                    'usage_in_kernelmode': 0,
                    'usage_in_usermode': 0
                },
                'throttling_data': {
                    'periods': 0,
                    'throttled_periods': 0,
                    'throttled_time': 0
                }
            },
            'preread': '0001-01-01T00:00:00Z',
            'read': '0001-01-01T00:00:00Z',
            'storage_stats': {}
        },
        'logs': 'Hash 0252d45ca21c8e43c9742285c48e91ad was NOT found in '
        'NSRL Database.\n'
    },
    'inputs': {
        'docker_image': {
            'id': 1801,
            'name': 'nsrl'
        },
        'docker_input': '0252d45ca21c8e43c9742285c48e91ad',
        'incident_id': 2095
    },
    'metrics': {
        'execution_time_ms': 7414,
        'host': 'Ryans-MacBook-Pro.local',
        'package': 'fn-docker',
        'package_version': '1.0.0',
        'timestamp': '2019-02-15 14:06:11',
        'version': '1.0'
    },
    'raw': '<the raw output of the function payload>',
    'reason': None,
    'success': True,
    'version': '1.0'
}

```

## Workflows

### **1: Send Artifact To Docker Container**

An example workflow scoped for Artifacts which will, when invoked, send the artifact to a Docker container, perform some operation on the input and returns information to Resilient.

### Pre-Process Script:

```python
inputs.docker_input = artifact.value
inputs.incident_id = incident.id
```

### Post-Process Script:

```python
noteText = u"""Container exit code : <b>{0}</b>
              <br> Container Stats : <b>{1}</b>
              <br> Container Logs has been saved as an attachment""".format(results.content["container_exit_status"], results.content["container_stats"])

incident.addNote(helper.createRichText(noteText))

try:
    des = artifact.description.content
except Exception:
  des = None
  
if des is None:
  artifact.description = u"""Results from Docker Integration: \n{}""".format(results.content["logs"])
else:
  artifact.description = des + u"""\nResults from Docker Integration: \n{}""".format(results.content["logs"])
  
  
row = incident.addRow("docker_integration_invocations")
row["docker_links"] = u"""<a href="{}">{}</a>""".format(results.content["res_links"]["res_object"], "Task Link" if "task" in results.content["res_links"]["res_object"] else "Incident Link")
row["docker_timestamp"] = results["metrics"]["timestamp_epoch"] or 0
row["docker_container_id"] = results.content["container_id"]
row["docker_image"] = results.inputs["docker_image"]["name"]
row["docker_exit_status"] = u"""<b style="color:{}">{}</b>""".format("green" if not results.content["container_exit_status"]["StatusCode"] else "red",results.content["container_exit_status"]["StatusCode"])
```


### **2: Send Attachment To Docker Container**

An example workflow scoped for Attachments which will, when invoked, send the attachment to a Docker container, perform some operation on the input and returns information to Resilient.

### 2: Pre-Process Script:

```python
inputs.incident_id = incident.id 

# If this workflow has the task_id available, gather it incase we need it.
if task:
  inputs.task_id = task.id
# If this workflow has the attachment_id available, gather it incase we need it.
if attachment:
  inputs.attachment_id = attachment.id

# If this workflow has the artifact_id available, gather it incase we need it.
try: 
  if artifact:
    inputs.artifact_id = artifact.id
except:
  pass
```

### 2: Post-Process Script:

```python
noteText = u"""Container exit code : <b>{0}</b>
              <br> Container Stats : <b>{1}</b>
              <br> Container Logs has been saved as an attachment""".format(results.content["container_exit_status"], results.content["container_stats"])

incident.addNote(helper.createRichText(noteText))

row = incident.addRow("docker_integration_invocations")
row["docker_links"] = u"""<a href="{}">{}</a>""".format(results.content["res_links"]["res_object"], "Task Link" if "task" in results.content["res_links"]["res_object"] else "Incident Link")
row["docker_timestamp"] = results["metrics"]["timestamp_epoch"] or 0
row["docker_container_id"] = results.content["container_id"]
row["docker_image"] = results.inputs["docker_image"]["name"]
row["docker_exit_status"] = u"""<b style="color:{}">{}</b>""".format("green" if not results.content["container_exit_status"]["StatusCode"] else "red",results.content["container_exit_status"]["StatusCode"])

```

## Rules:
| Rule Name | Object Type | Workflow Triggered | Conditions |
| --------- | :---------: | ------------------ | ---------- |
| Analyze Memory Sample with Volatility | `Attachment` | `Docker: Send Attachment To Docker Container` | None |
| Validate MD5 is in NSRL Whitelist | `Attachment` | `Docker: Send Artifact To Docker Container` | None |
| Analyze Memory Sample with Volatility | `Attachment` | `Send Attachment To Docker Container` | None |
| Analyze Memory Sample with Volatility | `Attachment` | `Send Attachment To Docker Container` | None |


## Datatable:


### **Docker Integration Invocations**
 ![screenshot](./screenshots/dtdocker.png)

### API Name:
docker_integration_invocations

#### Columns:
| Column Name | API Access Name | Type | Info |
| ----------- | --------------- | ---- | ---- |
| Timestamp | `timestamp` | `DateTime` | Timestamp when this entry was added |
| Device ID | `device_id` | `Text` | Unique CrowdStrike ID for the Device |
| Hostname | `hostname` | `Text` | Hostname of the Device |
| IP | `ip` | `Text` | Local IP Address of the Device |
| MAC | `mac` | `Text` | MAC Address of the Device |
| Last Seen | `last_seen` | `DateTime` | Datetime the Device was Last Seen |
| Status | `status` | `Text` | The Containment Status of the Device |
| Latest Action | `latest_action` | `Text` | Name of the latest CrowdStrike action to run on this device |

### Display a Data Table in an Incident
* In order to **display** the Test Data Table in your Incident, you must **modify your Layout Settings**

1. Go to **Customization Settings** > **Layouts** > **Incident Tabs** > **+ Add Tab**
   
 ![screenshot](./screenshots/dt_1.png)

2. Enter **Tab Text**: `My Test Tab` and click **Add**
 
 ![screenshot](./screenshots/dt_2.png)

3. **Drag** the Data table into the middle and click **Save**
 
 ![screenshot](./screenshots/dt_3.png)

4. Create a new Incident and you will now see the **My Test Tab** with the **Test Data Table**
