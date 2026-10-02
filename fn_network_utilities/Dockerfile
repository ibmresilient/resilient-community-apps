# Generated with resilient-sdk v51.0.2.2.1096
# docker build -t ibmresilient/fn_network_utilities:1.2.1 .
ARG BASE_IMAGE_REPO=quay.io
# BASE_IMAGE_TAG options: latest, python-39, python-311. See https://quay.io/repository/ibmresilient/soarapps-base-docker-image?tab=tags for all options
# use --build-arg BASE_IMAGE_TAG=<tag> to set base image to be built from
ARG BASE_IMAGE_TAG=latest

FROM ${BASE_IMAGE_REPO}/ibmresilient/soarapps-base-docker-image:${BASE_IMAGE_TAG}

ARG APPLICATION=fn_network_utilities

COPY ./dist /tmp/packages
USER 0
RUN yum -y update && yum clean all
# dig and nsloookup
RUN yum install -y bind-utils net-tools
RUN yum install -y https://mirror.stream.centos.org/9-stream/AppStream/x86_64/os/Packages/whois-nls-5.5.9-3.el9.noarch.rpm
RUN yum install -y https://mirror.stream.centos.org/9-stream/AppStream/x86_64/os/Packages/whois-5.5.9-3.el9.x86_64.rpm

RUN pip install /tmp/packages/${APPLICATION}-*.tar.gz
USER 1001
