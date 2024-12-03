# docker build -t ibmresilient/fn_snapshot_url:1.0.0 -t ibmresilient/fn_snapshot_url:latest .

# Base image using Red Hat's universal base image (rhel 8) for python
FROM registry.access.redhat.com/ubi8/python-39:latest

ARG APPLICATION=fn_snapshot_url
ARG RESILIENT_CIRCUITS_VERSION=46.0.0
ARG PATH_RESILIENT_CIRCUITS=rescircuits
ARG PHANTOM_JS="phantomjs-2.1.1-linux-i686"

# Environment variable for any app to check if running in a container
ARG APP_HOST_CONTAINER=1
ENV APP_HOST_CONTAINER=${APP_HOST_CONTAINER}

# Update to latest packages, user 0 for root privilege
USER 0

# Update to latest pip
RUN pip install --upgrade pip

# install resilient-circuits
RUN pip install "resilient-circuits>=${RESILIENT_CIRCUITS_VERSION}"

## ---- section for changes ----
# uncomment and replicate if additional os libraries are needed
RUN yum -y update && yum clean all

#=========
# Firefox
#=========
RUN wget -O- "https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=en-US" | tar -jx -C /usr/local/
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

# install the base package
COPY ./dist /tmp/packages
RUN pip install /tmp/packages/${APPLICATION}-*.tar.gz

# uncomment and replicate if additional pypi packages are needed
#RUN pip install extra-package

# uncomment and replicate if additional local packages are needed
#COPY /path/to/extra_package /tmp/packages/.
#RUN pip install /tmp/packages/<extra_package>*.tar.gz

## ---- end section for changes ----

# set up configuration and log locations using /etc and /var/log, the conventional locations for config and logs
RUN mkdir /etc/${PATH_RESILIENT_CIRCUITS}
ENV APP_CONFIG_FILE /etc/${PATH_RESILIENT_CIRCUITS}/app.config

# create arbitrary group for user 1001
RUN groupadd -g 1001 default && usermod -g 1001 default

# create directory for logs and set to be root group to allow access by non root processes
# See https://docs.openshift.com/container-platform/4.2/openshift_images/create-images.html#images-create-guide-openshift_create-images
RUN mkdir /var/log/${PATH_RESILIENT_CIRCUITS} && \
    chgrp -R 1001 /var/log/${PATH_RESILIENT_CIRCUITS} && \
    chmod -R g=u /var/log/${PATH_RESILIENT_CIRCUITS}
ENV APP_LOG_DIR /var/log/${PATH_RESILIENT_CIRCUITS}

# setup entrypoint for read-only enterprise data used by integration, if needed
RUN mkdir /var/${PATH_RESILIENT_CIRCUITS}

# entrypoint for resilient-circuits.  Use /opt, the conventional location for optional software on Linux
RUN mkdir /opt/${PATH_RESILIENT_CIRCUITS}
COPY entrypoint.sh /opt/${PATH_RESILIENT_CIRCUITS}/entrypoint.sh

# arbitrary user, support running as non-root. Required on OpenShift. Generally a good practice.
USER 1001
ENTRYPOINT [ "sh", "/opt/rescircuits/entrypoint.sh" ]
