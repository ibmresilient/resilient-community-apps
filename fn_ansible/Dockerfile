# Generated with resilient-sdk v51.0.1.0.695
# docker build -t ibmresilient/fn_ansible:1.3.0 .
ARG BASE_IMAGE_REPO=quay.io
# BASE_IMAGE_TAG options: latest, python-39, python-311. See https://quay.io/repository/ibmresilient/soarapps-base-docker-image?tab=tags for all options
# use --build-arg BASE_IMAGE_TAG=<tag> to set base image to be built from
ARG BASE_IMAGE_TAG=latest

FROM ${BASE_IMAGE_REPO}/ibmresilient/soarapps-base-docker-image:${BASE_IMAGE_TAG}

ARG APPLICATION=fn_ansible

COPY ./dist /tmp/packages
USER 0

RUN yum -y update && yum clean all
# uncomment to support sshpass in your privately built container
#RUN yum install -y sshpass

RUN pip install /tmp/packages/${APPLICATION}-*.tar.gz

# ansible artifacts
RUN mkdir /tmp/artifacts

USER 1001
