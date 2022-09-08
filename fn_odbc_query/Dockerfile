# Base image using Red Hat's universal base image (rhel 8) for python
FROM registry.access.redhat.com/ubi8/python-39:latest

ARG APPLICATION=fn_odbc_query
ARG RES_CIRCUITS_VERSION=37.0
ARG PATH_RESILIENT_CIRCUITS=rescircuits

# update to latest packages, user 0 for root privilege
USER 0
# Update to latest pip
RUN pip install --upgrade pip

# install resilient-circuits
RUN pip install "resilient-circuits>=${RES_CIRCUITS_VERSION}"

## ---- section for changes ----
# uncomment and replicate if additional os libraries are needed
#RUN yum -y update && yum clean all
#RUN yum -y install <package>

# install the base package
RUN yum -y update && yum clean all

# add yum repo with unixODBC and install
RUN curl https://packages.microsoft.com/config/rhel/8/prod.repo > /etc/yum.repos.d/mssql-release.repo
RUN yum -y install unixODBC-devel

# copy the driver configurations to the container
COPY ./.drivers/drivers.ini /etc/odbc-drivers.ini
COPY ./.drivers/drivers /tmp/lib/

# configure unixODBC with the driver information in the .ini file
RUN odbcinst -i -d -f /etc/odbc-drivers.ini

# install psqlodbc driver
RUN tar -zxvf /tmp/lib/psqlodbc-12.01.0000.tar.gz
RUN ./psqlodbc-12.01.0000/configure
RUN make
RUN make install

# install mariadb (mysql) driver
RUN mkdir /usr/local/lib64/mariadb
RUN mkdir /usr/local/lib64/mariadb/plugin
RUN tar -xvzf /tmp/lib/mariadb-connector-odbc-3.1.9-centos8-amd64.tar.gz
WORKDIR mariadb-connector-odbc-3.1.9-centos8-amd64
RUN install lib/mariadb/libmaodbc.so /usr/lib64/
RUN install -d /usr/lib64/mariadb/
RUN install -d /usr/lib64/mariadb/plugin/
RUN install lib64/mariadb/plugin/auth_gssapi_client.so /usr/local/lib64/mariadb/plugin/
RUN install lib64/mariadb/plugin/caching_sha2_password.so /usr/local/lib64/mariadb/plugin/
RUN install lib64/mariadb/plugin/client_ed25519.so /usr/local/lib64/mariadb/plugin/
RUN install lib64/mariadb/plugin/dialog.so /usr/local/lib64/mariadb/plugin/
RUN install lib64/mariadb/plugin/mysql_clear_password.so /usr/local/lib64/mariadb/plugin/
RUN install lib64/mariadb/plugin/sha256_password.so /usr/local/lib64/mariadb/plugin/
WORKDIR /opt/app-root/src

# install MS SQL driver
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
RUN yum -y install freetds

##########################
# At the time of writing this integration, oracle DB was not supported
# If we do decide to support, uncomment the run commands below to enable apphost support
##########################
## install Oracle DB driver
#RUN yum -y install /tmp/lib/oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm
#RUN yum -y install /tmp/lib/oracle-instantclient-odbc-linuxx64.rpm
#RUN yum -y install /tmp/lib/libnsl-2.28-101.el8.x86_64.rpm

# install the base package
COPY ./dist /tmp/packages
RUN pip install /tmp/packages/${APPLICATION}-*.tar.gz

# uncomment and replicate if additional pypi packages are needed
#RUN pip install <package>

# uncomment and replicate if additional local packages are needed
#COPY /path/to/extra_package /tmp/packages/.
#RUN pip install /tmp/packages/<extra_package>*.tar.gz

# uncomment to expose port only if a custom threat feed
#EXPOSE 9000
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

# remove temporary python files and temporary driver files
RUN rm -rf /tmp/packages /tmp/lib

# arbitrary user, support running as non-root. Required on OpenShift. Generally a good practice.
USER 1001
ENTRYPOINT [ "sh", "/opt/rescircuits/entrypoint.sh" ]
