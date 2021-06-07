# Repository Mirror Scripts for IBM Resilient App Host
## Table of Contents
  - [About this Package](#about-this-package)
  - [mirror-all-images.sh](#mirror-all-imagessh)
  - [mirror-images.sh](#mirror-imagessh)
  - [App Host Configuration](#app-host-configuration)
---

## History
7/20 -  Initial Documentation

## About this Package:
This branch contains scripts which can be used to mirror App Host container images
for local registry use. This is necessary when customers need to maintain their own
apps for use in App Host along with those officially published on the App Exchange 
or to replicate containers for air-gapped environments.

Two scripts are provided:
* [mirror-all-images.sh](#mirror-all-images.sh)
* [mirror-images.sh](#mirror-images.sh)

### Initialization
* Ensure that the local container tool, docker or podman, is accessible. If root permissions
are needed to run these commands, use `sudo` or `su` to access that login account in advance.
* Login to each registry using the `docker login` orr `podman login` commands.
* Add insecure_registry as an argument if working with HTTP registry with podman, docker may require you edit /.docker/config.json or an environment variable
* Add latest_tag to only retrieve the most the most recent version of each app, instead of all the unique versions, that exist on quay.io

## mirror-all-images.sh
This script is used to copy all container images from the IBM official registry, quay.io,
to a customer's private registry. It uses local container tools such as `docker` or `podman` to 
pull containers down from quay.io and then push them to the private registry.

### Usage
/bin/bash mirror-all-images fqdn.registry.io [docker | podman]

* fqdn.registry.io - name or ip address of the replication registry
* [docker | podman] - optional reference to the tool to perform the container transfer. 
If missing, the script will attempt to determine which tool exists.

### Examples
/bin/bash mirror-all-images 834299573936.dkr.ecr.us-east-2.amazonaws.com podman

/bin/bash mirror-all-images localhost:5000 podman insecure_registry latest_tag

## mirror-images.sh
This script is used to copy a select number of container images from the IBM official registry, quay.io,
to a customer's private registry. It uses local container tools such as `docker` or `podman` to 
pull containers down from quay.io and then push them to the private registry.
Two additional files are used to control the behavior of the script:
* repo_quay.conf - a list of container names and versions, one per line, to replicate. The format of a line is:
   `container_name:x.x.x` where `x.x.x` is the tagged version.
* preserved_images.conf - a list of container names and versions, one per line, to retain in the local docker or podman image 
container environment. Format of a line is the same as used in the `repo_quay.conf` file: `container_name:x.x.x`.

### Usage
/bin/bash mirror-all-images fqdn.registry.io [docker | podman]

* fqdn.registry.io - name or ip address of the replication registry
* [docker | podman] - optional reference to the tool to perform the container transfer. 
If missing, the script will attempt to determine which tool exists.

### Example
/bin/bash mirror-images 192.168.12.186:5000

repo_quay.conf
```
fn_utilities:1.14.0
fn_xforce:1.0.0
```

preserved_images.conf
```
fn_utilities:1.14.0
```

## App Host Configuration
Refer to the [Configuring a private repository](https://www-03preprod.ibm.com/support/knowledgecenter/SSBRUQ_37.0.0/doc/apps/private_repo_config.html) document on how to
develop Apps and configure App Host for your private registry.
Also, it will be necessary to secure your local registry currently for it to be paired correctly with App Host e.g.
https://www.redhat.com/sysadmin/simple-container-registry
