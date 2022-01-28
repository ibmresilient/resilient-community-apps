# docker build -t resilient/{ext} .
# Base image using Red Hat's universal base image (rhel 8) for python
#FROM registry.access.redhat.com/ubi8/python-36:latest
# rc-data-feeder will build plugins from a base image
FROM quay.io/ibmresilient/rc_data_feed:2.2.1

ARG APPLICATION=rc_data_feed_plugin_odbcfeed
ARG RES_CIRCUITS_VERSION="40.0"

# update to latest packages, user 0 for root privilege
USER 0
# Update to latest pip
RUN pip install --upgrade pip

# install resilient-circuits
RUN pip install resilient-circuits>=${RES_CIRCUITS_VERSION}

## ---- section for changes ----
# uncomment and replicate if additional os libraries are needed
RUN yum -y update && yum clean all

# link libnsl2 to libnsl
RUN ln -s /usr/lib64/libnsl.so.2.0.0 /usr/lib64/libnsl.so.1

# install MS SQL driver
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
RUN yum -y install freetds

# copy the driver configurations to the container
COPY ./drivers/drivers.ini /etc/odbc-drivers.ini
COPY ./drivers/drivers/ /tmp/lib/

# install Oracle DB driver
RUN yum -y install /tmp/lib/oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm
RUN yum -y install /tmp/lib/oracle-instantclient-odbc-linuxx64.rpm
#RUN rpm -i /tmp/lib/libnsl-2.28-72.el8_1.1.x86_64.rpm
ENV TNS_ADMIN /var/rescircuits

# add yum repo with unixODBC and install
RUN yum -y install unixODBC-devel
RUN curl https://packages.microsoft.com/config/rhel/8/prod.repo > /etc/yum.repos.d/mssql-release.repo

# configure unixODBC with the driver information in the .ini file
RUN odbcinst -i -d -f /etc/odbc-drivers.ini

# install psqlodbc driver
RUN tar -zxvf /tmp/lib/psqlodbc-12.01.0000.tar.gz
RUN ./psqlodbc-12.01.0000/configure
RUN make
RUN make install

# install mariadb (mysql) driver
RUN git clone https://github.com/MariaDB/mariadb-connector-odbc.git
WORKDIR mariadb-connector-odbc
RUN cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCONC_WITH_UNIT_TESTS=Off -DCONC_WITH_MSI=OFF -DCMAKE_INSTALL_PREFIX=/usr/local .
RUN cmake --build . --config RelWithDebInfo
RUN make install
WORKDIR /opt/app-root/src


# install the base package
COPY ./dist /tmp/packages
RUN pip install /tmp/packages/${APPLICATION}-*.tar.gz

# uncomment and replicate if additional pypi packages are needed
#RUN pip install <package>

# uncomment and replicate if additional local packages are needed
#COPY /path/to/extra_package /tmp/packages/.
#RUN pip install /tmp/packages/<extra_package>*.tar.gz

# uncomment to expose port only if a custom threat feed
# EXPOSE 9000
## ---- end section for changes ----

# set up configuration and log locations using /etc and /var/log, the conventional locations for config and logs
# RUN mkdir /etc/rescircuits
ENV APP_CONFIG_FILE /etc/rescircuits/app.config

# create directory for logs and set to be root group to allow access by non root processes
# See https://docs.openshift.com/container-platform/4.2/openshift_images/create-images.html#images-create-guide-openshift_create-images
# RUN mkdir /var/log/rescircuits && \
#    chgrp -R 0 /var/log/rescircuits && \
#    chmod -R g=u /var/log/rescircuits
ENV APP_LOG_DIR /var/log/rescircuits

# setup entrypoint for read-only enterprise data used by integration, if needed
#RUN mkdir /var/rescircuits

# entrypoint for resilient-circuits.  Use /opt, the conventional location for optional software on Linux
# RUN mkdir /opt/rescircuits
COPY entrypoint.sh /opt/rescircuits/entrypoint.sh
# arbitrary user, support running as non-root.  Required on OpenShift.
# Generally a good practice.
USER 1001
ENTRYPOINT [ "sh", "/opt/rescircuits/entrypoint.sh" ]
