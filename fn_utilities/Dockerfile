# docker build -t resilient/{ext} .
# Base image using Red Hat's universal base image (rhel 8) for python
FROM registry.access.redhat.com/ubi8/python-39:latest
# rc-data-feeder will build plugins from a base image
#FROM resilient/rc-data-feeder-base

ARG APPLICATION=fn_utilities
ARG RES_CIRCUITS_VERSION=40.0
ARG PATH_RESILIENT_CIRCUITS=rescircuits

# Environment variable for any app to check if running in a container
ARG APP_HOST_CONTAINER=1
ENV APP_HOST_CONTAINER=${APP_HOST_CONTAINER}

# update to latest packages, user 0 for root privilege
USER 0
# Update to latest pip
RUN pip install --upgrade pip

# install resilient-circuits
RUN pip install resilient-circuits>=${RES_CIRCUITS_VERSION}

# install and upgrade six to satisfy fn_utilities requirement
RUN pip install six==1.14.0
# install and upgrade cryptography to satisfy fn_utilities requirement
RUN pip install --upgrade cryptography

## ---- section for changes ----
# uncomment and replicate if additional os libraries are needed
RUN yum -y update && yum clean all
# dig and nsloookup
RUN yum install -y bind-utils net-tools
RUN yum install -y http://mirror.centos.org/centos/8-stream/AppStream/x86_64/os/Packages/whois-nls-5.5.1-2.el8.noarch.rpm
RUN yum install -y http://mirror.centos.org/centos/8-stream/AppStream/x86_64/os/Packages/whois-5.5.1-2.el8.x86_64.rpm
RUN yum install -y http://mirror.centos.org/centos/8-stream/BaseOS/x86_64/os/Packages/traceroute-2.1.0-6.el8.x86_64.rpm
# changes for mail parsing of Outlook emails
RUN yum install -y perl cpan
RUN cpan -fTi Email::Outlook::Message

# install the base package
COPY ./dist /tmp/packages
RUN pip install /tmp/packages/${APPLICATION}-*.tar.gz

# install and upgrade cryptography to satisfy fn_utilities requirement
RUN pip install --upgrade cryptography
# uncomment and replicate if additional pypi packages are needed
#RUN pip install <package>

# uncomment and replicate if additional local packages are needed
#COPY /path/to/extra_package /tmp/packages/.
#RUN pip install /tmp/packages/<extra_package>*.tar.gz

# uncomment to expose port only if a custom threat feed
#EXPOSE 9000
## ---- end section for changes ----

# set up configuration and log locations using /etc and /var/log, the conventional locations for config and logs
RUN mkdir /etc/${PATH_RESILIENT_CIRCUITS}
ENV APP_CONFIG_FILE /etc/${PATH_RESILIENT_CIRCUITS}/app.config

# create arbitrary group for user 1001
RUN groupadd -g 1001 default && usermod -g 1001 default

# create directory for logs and set to be root group to allow access by non root processes
# See https://docs.openshift.com/container-platform/4.2/openshift_images/create-images.html#images-create-guide-openshift_create-images
RUN mkdir /var/log/${PATH_RESILIENT_CIRCUITS} && \
    chgrp -R 1001 /var/log/${PATH_RESILIENT_CIRCUITS} && \
    chmod -R g=u /var/log/${PATH_RESILIENT_CIRCUITS}
ENV APP_LOG_DIR /var/log/${PATH_RESILIENT_CIRCUITS}

# setup entrypoint for read-only enterprise data used by integration, if needed
RUN mkdir /var/${PATH_RESILIENT_CIRCUITS}

# entrypoint for resilient-circuits.  Use /opt, the conventional location for optional software on Linux
RUN mkdir /opt/${PATH_RESILIENT_CIRCUITS}
COPY entrypoint.sh /opt/${PATH_RESILIENT_CIRCUITS}/entrypoint.sh

# remove temporary python files
RUN rm -rf /tmp/packages /tmp/lib

# arbitrary user, support running as non-root.  Required on OpenShift.
# Generally a good practice.
USER 1001
ENTRYPOINT [ "sh", "/opt/rescircuits/entrypoint.sh" ]
