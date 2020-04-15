# App Host Conversion Files

## Introduction

Starting with a Beta release in Resilient 36.2, IBM Resilient now supports container-based
deployment of apps (integrations) using an environment called App Host that pairs with your
Resilient appliance.

In order to deploy to App Host, you will need to create an image of your app using Docker
(or the container tool of your choice), push that image to a registry, and utilize
`resilient-sdk` to create a `.zip` file for your app in the standard format.


## Files

There are 3 files in this directory that will enable you to successfully package your app to deploy on App Host.
Most of the content can remain the same - you will only need to make a few manual edits.

### Dockerfile

The Dockerfile contains all the commands used to build the container image for a given app.
We use the Red Hat Enterprise Linux Universal Base Image (UBI) with a Python3.6 environment and build a circuits
environment on top of that. For more information on Red Hat UBI, please see their [documentation](https://developers.redhat.com/products/rhel/ubi/).

#### Required Changes

For all apps, you will need to change `ARG APPLICATION=<app_name>` to match the name of your
app. Note that if the build process is left unchaged, the `dist/` directory will mount into the container as `/tmp/packages`.
A `pip` command will attempt to install file matching the format `tmp/packages/${APPLICATION}-*.tar.gz`, where
`${APPLICATION}` is the `<app_name>` you just provided. If your directory structure or naming
convention for apps is different, you may need to slightly alter this process.

It is also recommended that for all apps, change `ARG RES_CIRCUITS_VERSION=36.2` to match
the latest version of `resilient-circuits` found on [PyPI](https://pypi.org/project/resilient-circuits/).
At the time of writing this documentation, the latest version of `resilient-circuits` is 36.2.

#### Advanced Changes

In certain cases, you may need to further alter the Dockerfile in order to install additional OS-level
packages, install additional Python packages, or expose a port in order for your app to run properly.

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

#### Building Your Container

Once the Dockerfile is updated according to the needs of the app, it is now time to build an image.
To do this, invoke a build command, e.g. `docker build -t resilient/your_custom_app:1.0.0 /path/to/dockerfile/directory`.

In the above command, we use docker (you could use podman) to build the image according to the Dockerfile.
The `-t` or `--tag` flag assigns the `resilient/your_custom_app` tag to the image with a version tag of `1.0.0`.
Finally, we specify the path to the directory containing the target Dockerfile with `/path/to/dockerfile/directory`.

Once the image is built, it is relatively easy to spin up a container on your local machine, provided you have access
to a Resilient instance and a valid `app.config` file for that instance. Run the command below:
```
docker run -v /path/to/your/local/app.config:/etc/rescircuits/app.config resilient/your_custom_app
```
Here, we have just started the a container running `resilient/your_custom_app` and performed a volume mount
with a local app config file, so that the container will use the configuration present in that file. Using the
command as stated above will output the logs from the container so you can verify that `resilient-circuits`
starts correctly. If you would prefer the logs not be output to the terminal, pass a `-d` flag to run the
container in detached mode.

### apikey_permissions.txt

This file contains a list of all API key permissions available to you in Resilient. By default, only
`read_data` and `read_function` are enabled, which allow for communication over the message destination.
Some apps, however, may require additional permissions in order to function properly. Uncomment those
permissions accordingly before invoking the `resilient-sdk package` command to package your app. At the time of
packing, the SDK will read in the permissions you enabled so that App Host can generate an API key with
the appropriate permissions for your app.

### entrypoint.sh

In almost all cases, this file can be left unchaged. The `entrypoint.sh` file serves as a means to monitor
the `app.config` file utilized by the app container for changes. If changes are detected, the container will be killed.
This is useful in a Kubernetes environment to enable a new container to start in the Pod using the new configuration.

## resilient-sdk

Introduced with Resilient 36.2 is [resilient-sdk](https://pypi.org/project/resilient-sdk/). This
tool is needed to produce a `.zip` file that App Host will leverage to install your app. To do this,
install the SDK from PyPI and run `resilient-sdk package -p /path/to/your/app` in the command line.
The resulting .zip file is placed in the dist/ folder. Import this file into Resilient. Your accompanying
docker image will need to be placed in a container repository for use with AppHost.

## Wrapping Up

Now that you have created a container image and `.zip` file for your app, you are ready
to install it and deploy onto your Resilient appliance through the UI using App Host.