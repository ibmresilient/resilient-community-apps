# docker build -t resilient/{ext} .
# Base image using Red Hat's universal base image (rhel 7) for python
#FROM registry.access.redhat.com/ubi8/python-36:latest
# rc-data-feeder will build plugins from a base image
FROM quay.io/ibmresilient/rc_data_feed:3.1.0

ARG APPLICATION=rc_data_feed_plugin_resilientfeed

# update to latest packages, user 0 for root privilege
USER 0

# Update to latest pip
RUN pip install --upgrade pip
RUN yum -y update && yum clean all

# copy the driver configurations to the container
COPY ./.drivers/drivers.ini /etc/odbc-drivers.ini
COPY ./.drivers/drivers/ /tmp/lib/

# unixodbc driver 
RUN yum -y install https://mirror.stream.centos.org/9-stream/CRB/x86_64/os/Packages/unixODBC-devel-2.3.9-4.el9.x86_64.rpm

# install psqlodbc driver
RUN tar -zxvf /tmp/lib/psqlodbc-16.00.0000.tar.gz
RUN ./psqlodbc-16.00.0000/configure && \
    make && \
    make install
RUN ln -s /usr/local/lib/psqlodbca.so /usr/lib64/psqlodbca.so && \
    ln -s /usr/local/lib/psqlodbcw.so /usr/lib64/psqlodbcw.so

# install the base package
COPY ./dist /tmp/packages
RUN app_file=`ls -1 /tmp/packages/${APPLICATION}-*.tar.gz` && pip install ${app_file}[postgres]

RUN rm -rf /tmp/packages /tmp/lib