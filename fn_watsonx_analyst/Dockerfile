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

# Update system
RUN yum -y update

# Install tesseract and its dependencies and clean cache
RUN yum -vy install \
      https://mirror.stream.centos.org/9-stream/AppStream/x86_64/os/Packages/tesseract-tessdata-doc-4.1.0-3.el9.noarch.rpm && \
    yum -vy install \
      https://mirror.stream.centos.org/9-stream/AppStream/x86_64/os/Packages/leptonica-1.80.0-4.el9.1.x86_64.rpm && \
    yum -vy install \
      https://mirror.stream.centos.org/9-stream/AppStream/x86_64/os/Packages/tesseract-langpack-eng-4.1.0-3.el9.noarch.rpm \
      https://mirror.stream.centos.org/9-stream/AppStream/x86_64/os/Packages/tesseract-4.1.1-7.el9.x86_64.rpm


# Install LibreOffice and LibreOffice Impress while ignoring broken dependencies,
# then clean cache. (Consider using rpm --nodeps if you really want to ignore dependencies.)
RUN yum -vy install \
      https://mirror.stream.centos.org/9-stream/AppStream/x86_64/os/Packages/libreoffice-7.1.8.1-14.el9.x86_64.rpm \
      https://mirror.stream.centos.org/9-stream/AppStream/x86_64/os/Packages/libreoffice-impress-7.1.8.1-14.el9.x86_64.rpm \
      --skip-broken

# Install Poppler tools here
RUN yum -vy install poppler poppler-utils

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

