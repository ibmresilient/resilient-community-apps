# Generated with resilient-sdk v51.0.2.2.1096
# docker build -t ibmresilient/fn_watsonx_analyst:1.0.2 .
ARG BASE_IMAGE_REPO=quay.io
# BASE_IMAGE_TAG options: latest, python-39, python-311. See https://quay.io/repository/ibmresilient/soarapps-base-docker-image?tab=tags for all options
# use --build-arg BASE_IMAGE_TAG=<tag> to set base image to be built from
ARG BASE_IMAGE_TAG=latest

FROM ${BASE_IMAGE_REPO}/ibmresilient/soarapps-base-docker-image:${BASE_IMAGE_TAG}

ARG APPLICATION=fn_watsonx_analyst
ENV APPLICATION=$APPLICATION

COPY ./dist /tmp/packages

# Copy in the config files
RUN mkdir -p /opt/app-root/src/fn_watsonx_analyst
COPY ./fn_watsonx_analyst/config/ /opt/app-root/src/fn_watsonx_analyst/config/

USER 0

RUN dnf -y remove httpd httpd-core httpd-devel httpd-filesystem httpd mod_md

# Update system
RUN yum -y update

RUN yum clean all && rm -rf /var/cache/yum

# Install the CPU version of pytorch
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

# Install Python package for the application
RUN pip install /tmp/packages/${APPLICATION}-*.tar.gz

# Set up the application directory and copy entrypoint script
RUN mkdir -p /opt/${APPLICATION}
COPY entrypoint.sh /opt/${APPLICATION}/entrypoint.sh

USER 1001

ENTRYPOINT sh /opt/$APPLICATION/entrypoint.sh
