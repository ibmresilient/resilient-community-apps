# AppHost Conversion Files

## Introduction

Starting with a Beta release in Resilient 36.2, IBM Resilient now supports container-based
deployment of Apps (Integrations) using a VMWare image, called AppHost, that pairs with your
Resilient appliance.

In order to deploy to AppHost, you will need to create an image of your App using Docker
(or the container tool of your choice), push that image to a registry, and utilize the
Resilient SDK to create a `.zip` file for your app in the standard format.


## Files

There are 3 files present to help you successfully package your App to deploy on AppHost.
Most of the content can remain the same, and you will only need to make a few manual edits.

### Dockerfile

The Dockerfile contains all the commands used to build the container image for a given App.
We use the Red Hat Enterprise Linux Universal Base Image (UBI) with a Python3.6 environment and build a circuits
environment on top of that. For more information on Red Hat UBI, please see their [documentation](https://developers.redhat.com/products/rhel/ubi/).

#### Required Changes

For all Apps, you will need to change `ARG APPLICATION=<app_name>` to match the name of your
App. If left unchaged, the build process will mount the `dist/` directory into the container
and attempt a `pip install` on a file matching the format `${APPLICATION}-*.tar.gz`, where
`${APPLICATION}` is the `<app_name>` you just provided. If your directory structure or naming
convention for Apps is different, you may need to slightly alter this process.

It is also recommended that for all Apps, change `ARG RES_CIRCUITS_VERSION=36.2` to match
the latest version of `resilient-circuits` found on [PyPI](https://pypi.org/project/resilient-circuits/).
At the time of writing this documentation, the latest version of `resilient-circuits` is 36.2.

#### Advanced Changes

In certain cases, you may need to further alter the Dockerfile in order to install additional OS-level
packages, install additional Python packages, or expose a port in order for your App to run properly.

If you find that you need to install addtional OS-level packages, edit this section:
```
# uncomment and replicate if additional os libraries are needed
#RUN yum -y update && yum clean all
#RUN yum -y install <package>
```

To install additional Python packages, edit this section:
```
# uncomment and replicate if additional pypi packages are needed
#RUN pip install <package>

# uncomment and replicate if additional local packages are needed
#COPY /path/to/extra_package /tmp/packages/.
#RUN pip install /tmp/packages/<extra_package>*.tar.gz
```

To expose a port, use this section:
```
# uncomment to expose port only if a custom threat feed
#EXPOSE 9000
```

### apikey_permissions.txt

This file contains a list of all API key permissions available to you in Resilient. By default, only
`read_data` and `read_function` are enabled, which allow for communication over the message destination.
Many Apps, however may require additional permissions in order to function properly. Uncomment those
permissions accordingly before invoking the Resilient SDK command to package your App. At the time of
packing, the SDK will read in the permissions you enabled so that AppHost can generate an API key with
the appropriate permissions for your App.

### entrypoint.sh

In almost all cases, this file can be left unchaged. The `entrypoint.sh` file serves as a means to watch
for changes in the `app.config` file utilized by your App's container and will kill circuits if changes
are detected. This is useful in a Kubernetes environment to enable a new container to start in the Pod
using the new configuration.

## Resilient SDK

Introduced with Resilient 36.2 is the [Resilient SDK](https://pypi.org/project/resilient-sdk/). This
tool is needed to produce a `.zip` file that AppHost will leverage to install your App. To do this,
install the SDK from PyPI and run `resilient-sdk package -p /path/to/your/app` in the command line.

## Wrapping Up

That's it! Now that you have created a container image and `.zip` file for your App, you are ready
to install it and deploy onto your Resilient appliance through the UI using AppHost.