# Base image using Red Hat's universal base image (rhel 8) for python
FROM registry.access.redhat.com/ubi8/python-36:latest

ARG APPLICATION=fn_test_app_one
ARG RESILIENT_CIRCUITS_VERSION=37
ARG PATH_RESILIENT_CIRCUITS=rescircuits

# Environment variable for any app to check if running in a container
ARG APP_HOST_CONTAINER=1
ENV APP_HOST_CONTAINER=${APP_HOST_CONTAINER}

# Update to latest packages, user 0 for root privilege
USER 0

# Update to latest pip
RUN pip install --upgrade pip

# install resilient-circuits
RUN pip install "resilient-circuits>=${RESILIENT_CIRCUITS_VERSION}"

## ---- section for changes ----
# uncomment and replicate if additional os libraries are needed
#RUN yum -y update && yum clean all
#RUN yum -y install <package>

# install the base package
COPY ./dist /tmp/packages
RUN pip install /tmp/packages/${APPLICATION}-*.tar.gz
