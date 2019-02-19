# Resilient Integration with Docker

The Resilient Integration with Docker provides tools which brings you to opportunity to integrate Docker into your Incident Response Plan. The integration brings Automation and Orchestration capabilities for Dockerised tools that can be used for Malware Research and Incident Response.

## Table of Contents
[Resilient Integration with Docker](#resilient-integration-with-docker)

- [Table of Contents](#table-of-contents)
- [Connection options and installation:](#connection-options-and-installation)
- [app.config settings:](#appconfig-settings)
- [Integration app.config settings:](#integration-appconfig-settings)
- [Image specific app.config sections](#image-specific-appconfig-sections)
- [Functions:](#functions)
- [**Docker: Run Docker Container**](#1-run-docker-container)
- [Function Inputs:](#function-inputs)
- [Function Output:](#function-output)
- [Workflows](#workflows)
- [**Workflow 1: Send Artifact To Docker Container**](#1-send-artifact-to-docker-container)
- [Workflow 1: Pre-Process Script:](#1-pre-process-script)
- [Workflow 1: Post-Process Script:](#1-post-process-script)
- [**Workflow 2: Send Attachment To Docker Container**](#2-send-attachment-to-docker-container)
- [Workflow 2: Pre-Process Script:](#2-pre-process-script)
- [Workflow 2: Post-Process Script:](#2-post-process-script)
- [Rules:](#rules)
- [Datatable:](#datatable)
- [**Docker External Ticket Status Datatable**](#docker-external-ticket-status-datatable)
- [API Name:](#api-name)
- [Columns:](#columns)
- [Display the Datatable in an Incident](#display-the-datatable-in-an-incident)

# Connection options and installation:  

This integration requires access to a Docker daemon, in order to run containers and get output. Typically the Docker daemon would be on the same machine that you intend to run the containers from so this would mean installing Docker on your integration server itself.
To install Docker on your Integration Server see [this link](). 

Alternatively, if you have an exposed Docker daemon that you can connect to and use, you may instead opt to connect to and run containers using this daemon instead of installing Docker on your integration server. This is done by providing a URL in the app.config section which will specify the location of the Docker daemon and also which remote connection option to use, of which there are two: TCP and SSH.

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

| Input Name | Type | Required | Example |
| ------------- | :--: | :-------:| ------- |
| `incident_id` | `Number` | Yes | `2105` |
| `task_id` | `Number` | No | `None` |
| `artifact_id` | `Number` | No | `None` |
| `attachment_id` | `Number` | No | `None` |
| `docker_image` | `Select` | Yes | `nsrl` |
| `docker_input` | `String` | No | `60B7C0FEAD45F2066E5B805A91F4F0FC` |

### Function Output:

```python
{'content': {'container_exit_status': {'Error': None, 'StatusCode': 0},
             'container_id': '0ce1ece10633d13ea159a2b013ae0256f0e2ae29e247492c811b8525d560b30c',
             'container_stats': {'blkio_stats': {'io_merged_recursive': None,
                                                 'io_queue_recursive': None,
                                                 'io_service_bytes_recursive': None,
                                                 'io_service_time_recursive': None,
                                                 'io_serviced_recursive': None,
                                                 'io_time_recursive': None,
                                                 'io_wait_time_recursive': None,
                                                 'sectors_recursive': None},
                                 'cpu_stats': {'cpu_usage': {'total_usage': 0,
                                                             'usage_in_kernelmode': 0,
                                                             'usage_in_usermode': 0},
                                               'throttling_data': {'periods': 0,
                                                                   'throttled_periods': 0,
                                                                   'throttled_time': 0}},
                                 'id': '0ce1ece10633d13ea159a2b013ae0256f0e2ae29e247492c811b8525d560b30c',
                                 'memory_stats': {},
                                 'name': '/tender_goldwasser',
                                 'num_procs': 0,
                                 'pids_stats': {},
                                 'precpu_stats': {'cpu_usage': {'total_usage': 0,
                                                                'usage_in_kernelmode': 0,
                                                                'usage_in_usermode': 0},
                                                  'throttling_data': {'periods': 0,
                                                                      'throttled_periods': 0,
                                                                      'throttled_time': 0}},
                                 'preread': '0001-01-01T00:00:00Z',
                                 'read': '0001-01-01T00:00:00Z',
                                 'storage_stats': {}},
             'logs': 'Hash 0252d45ca21c8e43c9742285c48e91ad was NOT found in '
                     'NSRL Database.\n'},
 'inputs': {'docker_image': {'id': 1801, 'name': 'nsrl'},
            'docker_input': '0252d45ca21c8e43c9742285c48e91ad',
            'incident_id': 2095},
 'metrics': {'execution_time_ms': 7414,
             'host': 'Ryans-MacBook-Pro.local',
             'package': 'fn-docker',
             'package_version': '1.0.0',
             'timestamp': '2019-02-15 14:06:11',
             'version': '1.0'},
 'raw': '<the raw output of the function payload>',
 'reason': None,
 'success': True,
 'version': '1.0'}

```

## Workflows

## **1: Send Artifact To Docker Container**

An example workflow scoped for Artifacts which will, when invoked, send the artifact to a Docker container, perform some operation on the input and returns information to Resilient.

### 1: Pre-Process Script:

```python
inputs.docker_input = artifact.value
inputs.incident_id = incident.id
```

### 1: Post-Process Script:

```python
noteText = u"""Container exit code : <b>{0}</b>
              <br> Container Logs : <b>{1}</b>
              <br> Container Stats : <b>{2}</b>""".format(results.content["container_exit_status"],results.content["logs"], results.content["container_stats"])
incident.addNote(helper.createRichText(noteText))

try:
    des = artifact.description.content
except Exception, e:
  des = None
  
if des is None:
  artifact.description = "Results from Docker Integration: \n{}".format(results.content["logs"])
else:
  artifact.description = des + "\nResults from Docker Integration: \n{}".format(results.content["logs"])
```


## **2: Send Attachment To Docker Container**

An example workflow scoped for Attachments which will, when invoked, send the attachment to a Docker container, perform some operation on the input and returns information to Resilient.

### 2: Pre-Process Script:

```python
inputs.incident_id = incident.id 

if task:
  inputs.task_id = task.id
if attachment:
  inputs.attachment_id = attachment.id
  
try: 
  if artifact:
    inputs.artifact_id = artifact.id
except:
  pass
```

### 2: Post-Process Script:

```python
noteText = u"""Container exit code : <b>{0}</b>
              <br> Container Logs : <br><b>{1}<b>
              <br> Container Stats : <b>{2}</b>""".format(results.content["container_exit_status"], unicode(results.content["logs"]), results.content["container_stats"])

#incident.addNote(helper.createRichText(noteText))
incident.addNote("{}".format(results.content["logs"]))
```

## Rules:
| Rule Name | Object Type | Workflow Triggered | Conditions |
| --------- | :---------: | ------------------ | ---------- |
| Analyze Memory Sample with Volatility | `Attachment` | `Docker: Send Attachment To Docker Container` | None |
| Validate MD5 is in NSRL Whitelist | `Attachment` | `Docker: Send Artifact To Docker Container` | None |
| Analyze Memory Sample with Volatility | `Attachment` | `Send Attachment To Docker Container` | None |
| Analyze Memory Sample with Volatility | `Attachment` | `Send Attachment To Docker Container` | None |


## Datatable:


### **Docker External Ticket Status Datatable**
 ![screenshot](./screenshots/3.png)

### API Name:
docker_integration_invocations

### Columns:

### Display the Datatable in an Incident
