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
COPY . /opt/app-root/src

USER 0

RUN yum -y update

RUN yum -vy install https://mirror.stream.centos.org/9-stream/AppStream/x86_64/os/Packages/tesseract-tessdata-doc-4.1.0-3.el9.noarch.rpm # tesseract dependency
RUN yum -vy install https://mirror.stream.centos.org/9-stream/AppStream/x86_64/os/Packages/leptonica-1.80.0-4.el9.1.x86_64.rpm # tesseract dependency
RUN yum -vy install https://mirror.stream.centos.org/9-stream/AppStream/x86_64/os/Packages/tesseract-langpack-eng-4.1.0-3.el9.noarch.rpm \
                    https://mirror.stream.centos.org/9-stream/AppStream/x86_64/os/Packages/tesseract-4.1.1-7.el9.x86_64.rpm

RUN yum clean all

RUN yum -vy install java-11-openjdk

RUN pip install /tmp/packages/${APPLICATION}-*.tar.gz

RUN mkdir -p /opt/tika
RUN curl -o /opt/tika/tika-server.jar https://dlcdn.apache.org/tika/2.9.3/tika-server-standard-2.9.3.jar
RUN chmod +x /opt/tika/tika-server.jar

RUN mkdir -p /var/log/tika
RUN chown 1001:1001 /var/log/tika # allow app to write logs


ENV export TIKA_SERVER_ENDPOINT=http://localhost:9998
ENV export TIKA_CLIENT_ONLY=True

RUN mkdir -p /opt/${APPLICATION}
COPY entrypoint.sh /opt/${APPLICATION}/entrypoint.sh

USER 1001

ENTRYPOINT sh /opt/$APPLICATION/entrypoint.sh
