# Generated with resilient-sdk v51.0.2.2.1096
# docker build -t ibmresilient/fn_watsonx_analyst:1.0.2 .
ARG BASE_IMAGE_REPO=quay.io
# BASE_IMAGE_TAG options: latest, python-39, python-311. See https://quay.io/repository/ibmresilient/soarapps-base-docker-image?tab=tags for all options
# use --build-arg BASE_IMAGE_TAG=<tag> to set base image to be built from
ARG BASE_IMAGE_TAG=latest

FROM ${BASE_IMAGE_REPO}/ibmresilient/soarapps-base-docker-image:${BASE_IMAGE_TAG}

ARG APPLICATION=fn_watsonx_analyst

COPY ./dist /tmp/packages
COPY . /opt/app-root/src
USER 0
RUN pip install /tmp/packages/${APPLICATION}-*.tar.gz
RUN yum -y update && yum clean all
USER 1001