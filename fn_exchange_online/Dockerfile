# Generated with resilient-sdk v51.0.1.1.824
# docker build -t ibmresilient/fn_exchange_online:1.4.1 .
ARG BASE_IMAGE_REPO=quay.io
# BASE_IMAGE_TAG options: latest, python-39, python-311. See https://quay.io/repository/ibmresilient/soarapps-base-docker-image?tab=tags for all options
# use --build-arg BASE_IMAGE_TAG=<tag> to set base image to be built from
ARG BASE_IMAGE_TAG=latest

FROM ${BASE_IMAGE_REPO}/ibmresilient/soarapps-base-docker-image:${BASE_IMAGE_TAG}

ARG APPLICATION=fn_exchange_online

COPY ./dist /tmp/packages
USER 0
RUN pip install /tmp/packages/${APPLICATION}-*.tar.gz
USER 1001
