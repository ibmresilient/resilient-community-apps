# Generated with resilient-sdk v51.0.8.3
# docker build -t ibmresilient/fn_outbound_email:2.1.6 .
ARG BASE_IMAGE_REPO=quay.io
# BASE_IMAGE_TAG options: latest, python-312. See https://quay.io/repository/ibmresilient/soarapps-base-docker-image?tab=tags for all options
# use --build-arg BASE_IMAGE_TAG=<tag> to set base image to be built from
ARG BASE_IMAGE_TAG=latest

FROM ${BASE_IMAGE_REPO}/ibmresilient/soarapps-base-docker-image:${BASE_IMAGE_TAG}

ARG APPLICATION=fn_outbound_email

COPY ./dist /tmp/packages
USER 0
RUN yum -y update && yum clean all
# pip is bootstrapped via ensurepip and removed after install
RUN python3 -m ensurepip --upgrade && \
    python3 -m pip install /tmp/packages/${APPLICATION}-*.tar.gz && \
    python3 -m pip uninstall -y pip setuptools
USER 1001
