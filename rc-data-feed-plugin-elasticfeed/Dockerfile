# docker build -t resilient/{ext} .
# Base image using Red Hat's universal base image (rhel 8) for python
#FROM registry.access.redhat.com/ubi8/python-36:latest
# rc-data-feeder will build plugins from a base image
FROM quay.io/ibmresilient/rc_data_feed:2.0.0

ARG APPLICATION=rc_data_feed_plugin_elasticfeed
ARG RES_CIRCUITS_VERSION=37.2

# Environment variable for any app to check if running in a container
ARG APP_HOST_CONTAINER=1
ENV APP_HOST_CONTAINER=${APP_HOST_CONTAINER}

# update to latest packages, user 0 for root privilege
USER 0
# Update to latest pip
RUN pip install --upgrade pip

# install resilient-circuits
RUN pip install resilient-circuits>=${RES_CIRCUITS_VERSION}

## ---- section for changes ----
# uncomment and replicate if additional os libraries are needed
#RUN yum -y update && yum clean all
#RUN yum -y install <package>

# install the base package
COPY ./dist /tmp/packages
RUN pip install /tmp/packages/${APPLICATION}-*.tar.gz

# uncomment and replicate if additional pypi packages are needed
#RUN pip install <package>

# uncomment and replicate if additional local packages are needed
#COPY /path/to/extra_package /tmp/packages/.
#RUN pip install /tmp/packages/<extra_package>*.tar.gz

# uncomment to expose port only if a custom threat feed
# EXPOSE 9000
## ---- end section for changes ----

# set up configuration and log locations using /etc and /var/log, the conventional locations for config and logs
# RUN mkdir /etc/rescircuits
ENV APP_CONFIG_FILE /etc/rescircuits/app.config

# create directory for logs and set to be root group to allow access by non root processes
# See https://docs.openshift.com/container-platform/4.2/openshift_images/create-images.html#images-create-guide-openshift_create-images
# RUN mkdir /var/log/rescircuits && \
#    chgrp -R 0 /var/log/rescircuits && \
#    chmod -R g=u /var/log/rescircuits
ENV APP_LOG_DIR /var/log/rescircuits

# setup entrypoint for read-only enterprise data used by integration, if needed
#RUN mkdir /var/rescircuits

# entrypoint for resilient-circuits.  Use /opt, the conventional location for optional software on Linux
# RUN mkdir /opt/rescircuits
COPY entrypoint.sh /opt/rescircuits/entrypoint.sh
# arbitrary user, support running as non-root.  Required on OpenShift.
# Generally a good practice.
USER 1001
ENTRYPOINT [ "sh", "/opt/rescircuits/entrypoint.sh" ]

