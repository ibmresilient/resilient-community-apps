# docker build -t resilient/{ext} .
# Base image using Red Hat's universal base image (rhel 8) for python
#FROM registry.access.redhat.com/ubi8/python-36:latest
# rc-data-feeder will build plugins from a base image
FROM quay.io/ibmresilient/rc_data_feed:3.3.1

ARG APPLICATION=rc_data_feed_plugin_odbcfeed

# update to latest packages, user 0 for root privilege
USER 0

# Update to latest pip
RUN pip install --upgrade pip
RUN yum -y update && yum clean all

# libnsl2 not part of base rhel9 environment
RUN dnf -y install libnsl2
RUN ln -s /usr/lib64/libnsl.so.3.0.0 /usr/lib64/libnsl.so.1

# install MS SQL driver
RUN yum -y install nettle
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
RUN yum -y install freetds

# copy the driver configurations to the container
COPY ./.drivers/drivers.ini /etc/odbc-drivers.ini
COPY ./.drivers/drivers/ /tmp/lib/

# install Oracle DB driver
RUN yum -y install /tmp/lib/oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm
RUN yum -y install /tmp/lib/oracle-instantclient-odbc-linuxx64.rpm
ENV TNS_ADMIN /var/rescircuits

# install mariadb (mysql) driver
RUN yum -y install /tmp/lib/mariadb-connector-odbc-3.1.20-rhel9-amd64.rpm

# unixodbc driver 
RUN yum -y install https://mirror.stream.centos.org/9-stream/CRB/x86_64/os/Packages/unixODBC-devel-2.3.9-4.el9.x86_64.rpm

# configure unixODBC with the driver information in the .ini file
RUN odbcinst -i -d -f /etc/odbc-drivers.ini

# install psqlodbc driver
RUN tar -zxvf /tmp/lib/psqlodbc-16.00.0000.tar.gz
RUN ./psqlodbc-16.00.0000/configure && \
    make && \
    make install
RUN ln -s /usr/local/lib/psqlodbca.so /usr/lib64/psqlodbca.so && \
    ln -s /usr/local/lib/psqlodbcw.so /usr/lib64/psqlodbcw.so

# install the base package
COPY ./dist /tmp/packages
RUN pip install /tmp/packages/${APPLICATION}-*.tar.gz

RUN rm -rf /tmp/packages /tmp/lib
