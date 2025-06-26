# Generated with resilient-sdk v51.0.5.0.1475
# docker build -t ibmresilient/fn_parse_utilities:1.1.1 .
ARG BASE_IMAGE_REPO=quay.io
# BASE_IMAGE_TAG options: latest, python-311, python-312. See https://quay.io/repository/ibmresilient/soarapps-base-docker-image?tab=tags for all options
# use --build-arg BASE_IMAGE_TAG=<tag> to set base image to be built from
ARG BASE_IMAGE_TAG=latest

FROM ${BASE_IMAGE_REPO}/ibmresilient/soarapps-base-docker-image:${BASE_IMAGE_TAG}

ARG APPLICATION=fn_parse_utilities

COPY ./dist /tmp/packages
USER 0
RUN yum -y update && yum clean all
RUN yum install -y perl cpan
RUN cpan -fTi Email::Outlook::Message
RUN pip install /tmp/packages/${APPLICATION}-*.tar.gz
USER 1001
