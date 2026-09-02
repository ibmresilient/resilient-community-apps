# docker build -t resilient/{ext} .
# rc-data-feeder will build plugins from a base image
FROM quay.io/ibmresilient/rc_data_feed:3.3.0

ARG APPLICATION=rc_data_feed_plugin_splunkfeed

# update to latest packages, user 0 for root privilege
USER 0

# Update to latest pip
RUN pip install --upgrade pip
RUN yum -y update && yum clean all

# install the base package
COPY ./dist /tmp/packages
RUN pip install /tmp/packages/${APPLICATION}-*.tar.gz

RUN rm -rf /tmp/packages