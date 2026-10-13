# docker build -t resilient/{ext} .
# Base image using Red Hat's universal base image (rhel 8) for python
#FROM registry.access.redhat.com/ubi8/python-36:latest
# rc-data-feeder will build plugins from a base image
FROM quay.io/ibmresilient/rc_data_feed:3.3.3

ARG APPLICATION=rc_data_feed_plugin_odbcfeed

# update to latest packages, user 0 for root privilege
COPY ./dist /tmp/packages
USER 0

# Update to latest pip
RUN yum -y update && yum clean all

# libnsl2 not part of base rhel9 environment
RUN yum -y install libnsl2
RUN ln -s /usr/lib64/libnsl.so.3.0.0 /usr/lib64/libnsl.so.1

# install MS SQL driver
# base image is ubi9-minimal: yum is a symlink to microdnf, which cannot install from a URL
# and there is no dnf. Use rpm (with the EPEL signing key imported) to add the EPEL repo.
RUN yum -y install nettle
RUN rpm --import https://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-9 && \
    rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
RUN yum -y install freetds

# copy the driver configurations to the container
COPY ./.drivers/drivers.ini /etc/odbc-drivers.ini
COPY ./.drivers/drivers/ /tmp/lib/

# unixodbc driver (available from ubi-9-codeready-builder-rpms, enabled in the base image)
# installed before the vendor RPMs below, which depend on libodbcinst
RUN yum -y install unixODBC-devel

# The vendor RPMs are installed with rpm because microdnf (yum) is unreliable with local RPM files.
# Their dependencies are installed from the UBI repos first.
# install Oracle DB driver (requires libaio)
RUN yum -y install libaio
RUN rpm -ivh /tmp/lib/oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm && \
    rpm -ivh /tmp/lib/oracle-instantclient-odbc-linuxx64.rpm
ENV TNS_ADMIN /var/rescircuits

# install mariadb (mysql) driver (requires libmariadb.so.3 and libodbcinst.so.2)
RUN yum -y install mariadb-connector-c
RUN rpm -ivh /tmp/lib/mariadb-connector-odbc-3.1.20-rhel9-amd64.rpm

# configure unixODBC with the driver information in the .ini file
RUN odbcinst -i -d -f /etc/odbc-drivers.ini

# install psqlodbc driver
# ubi9-minimal has no build toolchain: tar/gzip/make from BaseOS; gcc, libpq (runtime) and
# libpq-devel (pg_config + headers) from AppStream. unixODBC-devel is installed above.
RUN yum -y install tar gzip make gcc libpq libpq-devel
RUN tar -zxvf /tmp/lib/psqlodbc-16.00.0000.tar.gz
RUN ./psqlodbc-16.00.0000/configure && \
    make && \
    make install
RUN ln -s /usr/local/lib/psqlodbca.so /usr/lib64/psqlodbca.so && \
    ln -s /usr/local/lib/psqlodbcw.so /usr/lib64/psqlodbcw.so

# install the base package
RUN python3 -m ensurepip --upgrade && \
    python3 -m pip install /tmp/packages/${APPLICATION}-*.tar.gz && \
    python3 -m pip uninstall -y pip
    
RUN rpm -e python3-pip python3-wheel 2>/dev/null || true

RUN rm -rf /tmp/packages /tmp/lib
USER 1001