# Generated with resilient-sdk v51.0.5.0.1475
# docker build -t ibmresilient/fn_snapshot_url:1.1.0 .
ARG BASE_IMAGE_REPO=quay.io
# BASE_IMAGE_TAG options: latest, python-311, python-312. See https://quay.io/repository/ibmresilient/soarapps-base-docker-image?tab=tags for all options
# use --build-arg BASE_IMAGE_TAG=<tag> to set base image to be built from
ARG BASE_IMAGE_TAG=latest
ARG PHANTOM_JS="phantomjs-2.1.1-linux-i686"

FROM ${BASE_IMAGE_REPO}/ibmresilient/soarapps-base-docker-image:${BASE_IMAGE_TAG}

ARG APPLICATION=fn_snapshot_url

COPY ./dist /tmp/packages
USER 0
RUN yum -y update && yum clean all
RUN pip install /tmp/packages/${APPLICATION}-*.tar.gz

#=========
# Firefox
#=========
RUN wget "https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=en-US" -O /tmp/firefox.tar.gz \
  && tar -xf /tmp/firefox.tar.gz -C /usr/local/
RUN ln -s /usr/local/firefox/firefox  /usr/bin/firefox

#============
# GeckoDriver
#============
ARG GECKODRIVER_VERSION=latest
RUN GK_VERSION=$(if [ ${GECKODRIVER_VERSION:-latest} = "latest" ]; then echo "0.33.0"; else echo $GECKODRIVER_VERSION; fi) \
  && echo "Using GeckoDriver version: "$GK_VERSION \
  && wget --no-verbose -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v$GK_VERSION/geckodriver-v$GK_VERSION-linux64.tar.gz \
  && rm -rf /opt/geckodriver \
  && tar -C /opt -zxf /tmp/geckodriver.tar.gz \
  && rm /tmp/geckodriver.tar.gz \
  && mv /opt/geckodriver /opt/geckodriver-$GK_VERSION \
  && chmod 755 /opt/geckodriver-$GK_VERSION \
  && ln -fs /opt/geckodriver-$GK_VERSION /usr/bin/geckodriver

RUN yum install -y gtk3 glib* pango
RUN yum install -y alsa-lib

#============================================
# Dumping Browser information for config
#============================================
RUN mkdir /opt/selenium && echo "firefox" > /opt/selenium/browser_name
# firefox cannot be run as root
USER 1001
RUN firefox --version | awk '{print $3}' > /tmp/browser_version
USER 0
RUN mv /tmp/browser_version /opt/selenium/browser_version
RUN echo "\"moz:firefoxOptions\": {\"binary\": \"/usr/bin/firefox\"}" > /opt/selenium/browser_binary_location

RUN rm -R /tmp/packages /tmp/firefox.tar.gz
USER 1001
