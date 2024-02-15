# App Host Conversion Files

## Introduction

Starting with Resilient v37, IBM Resilient now supports container-based
deployment of apps using an environment called App Host that pairs with your
Resilient organization to run apps.

A Resilient app is a collection of Resilient playbook components, 
Python-based external code executables or both that represent an 
end-to-end function that can be easily installed and deployed 
within the Resilient platform. A Resilient app is the next 
generation of the Resilient extension or integration. 
The main difference between a Resilient app and Resilient extension 
is that apps use containers for improved usability, manageability, 
and security.

In order to deploy containers to App Host, you will need to 

* create a container image of your app using Docker, Podman
or the container tool of your choice, 
* push that image to a container registry, and 
* utilize
`resilient-sdk package` to create a `.zip` file to import your application into the 
Resilient organization.


## Files

This directory contains three files and a directory of icons that will enable you to successfully package your app to deploy on App Host.
Most of the content can remain the same - you will only need to make a few manual edits.

* [Dockerfile](#Dockerfile)
* [apikey_permissions.txt](#apikey_permissions.txt)
* [entrypoint.sh](#entrypoint.sh)
* [icons](#icons)


### Dockerfile

The Dockerfile contains all the commands used to build the container image for a given app.
We use the Red Hat Enterprise Linux Universal Base Image (UBI) with a Python3.6 environment and build a resilient-circuits
environment on top of that. For more information on Red Hat UBI, please see their [documentation](https://developers.redhat.com/products/rhel/ubi/).

#### Required Changes

For all apps, you will need to change the line `ARG APPLICATION=<app_name>` to match the name of your
app. Note that the build process will use the `dist/<app_name>-<version>.tar.gz` source distribution produced by `python setup.py sdist`.


It is also recommended that for all apps, change `ARG RES_CIRCUITS_VERSION=37` to match
the latest version of `resilient-circuits` found on [PyPI](https://pypi.org/project/resilient-circuits/).


#### Advanced Changes

In certain cases, you may need to further alter the Dockerfile in order to install additional OS-level
packages, install additional Python packages, or expose port(s) in order for your app to run properly.

If you find that you need to install additional OS-level packages, edit this section:
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
To do this, invoke a build command in the directory where the Dockerfile is found, e.g., `docker build . -t your_company/your_custom_app:1.0.0`.

In the above command, we use docker to build the image according to the Dockerfile. Other tools such as podman can also be used.

The `-t` or `--tag` flag assigns the `your_company/your_custom_app` tag to the image with a version of `1.0.0`.
Finally, we specify the path to the directory containing the target Dockerfile with current directory (.). The container version must match the version specified in your `setup.py` file.

Once the image is built, it is relatively easy to spin up a container on your local machine for testing, provided you have access
to a Resilient organization and a valid `app.config` file for that organization. Run the command below:
```
docker run -v /path/to/your/local/app.config:/etc/rescircuits/app.config your_company/your_custom_app:1.0.0
```
In this example, we have just started the   `your_company/your_custom_app` container with a volume mount
using a local app.config file, so that the container will use the configuration present in that file. Using the
command as stated above will output the log entries to your console from the container so you can verify that `resilient-circuits`
starts correctly. If you would prefer the logs not be output to the terminal, pass a `-d` flag to run the
container in detached mode.

### apikey_permissions.txt

This file contains a list of all Resilient API key account permissions. By default, only
`read_data` and `read_function` are enabled, which allow for communication over the message destination.
Some apps, however, may require additional permissions in order to function properly, such as the use of different Resilient API calls. Uncomment those
permissions accordingly before invoking the `resilient-sdk package` command to package your app. At the time of
packing, the SDK will read the permissions you enabled so that App Host can generate an API key with
the appropriate permissions for your app.

### entrypoint.sh

In almost all cases, this file should be left unchanged. The `entrypoint.sh` file serves as a means to execute resilient-circuits and monitor
changes to the `app.config` file. If changes are detected, the container will be killed and restarted by Kubernetes.

### icons
Two icons are provided to allow you to use or modify for your application. 
Add this directory to your application so that the `resilient-sdk package` process
can bundle them together for display within the Resilient organization. 

* company_logo.png - this icon must be 100x100px and by default displays the IBM Shield. It can be replaced to represent your companies' logo.
* app_logo.png - this icon must be 200x72px and by default displays the IBM Shield.  It can be replaced to represent a visual representation of our application. 
See the [IBM AppExchange](https://exchange.xforce.ibmcloud.com/hub?br=Resilient) for examples. 

## resilient-sdk

Introduced with Resilient v37 is [resilient-sdk](https://pypi.org/project/resilient-sdk/). This
tool is needed to build and package a `.zip` file that App Host will leverage to install your app. To do this,
install the SDK from PyPi and run `resilient-sdk package -p /path/to/your/app` at the command line.
The resulting .zip file is placed in the app's `dist/` folder. Import this file into Resilient. Your accompanying
docker image will need to be placed in a container repository to complete the deployment to App Host.

## Wrapping Up

Now that you have created a container image and `.zip` file for your app, you are ready
to install it and deploy to your Resilient organization through the UI using App Host.