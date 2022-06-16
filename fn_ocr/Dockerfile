# docker build -t ibmresilient/fn_ocr:1.0.0 -t ibmresilient/fn_ocr:latest .

# Base image using Red Hat's universal base image (rhel 8) for python
FROM registry.access.redhat.com/ubi8/python-39:latest

ARG APPLICATION=fn_ocr
ARG RESILIENT_CIRCUITS_VERSION=45.0.0
ARG PATH_RESILIENT_CIRCUITS=rescircuits

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
# install tools required to build tesseract and leptonica
RUN yum -y install libstdc++ autoconf automake libtool autoconf-archive pkg-config gcc gcc-c++ make cmake libjpeg-devel libpng-devel libtiff-devel libtiff zlib-devel wget libarchive 
# install image shared libraries
RUN yum -y install libpng libjpeg libtiff zlib 
# make a temp dir we can delete after building and installing
RUN mkdir $HOME/temp_installers
WORKDIR $HOME/temp_installers

RUN wget https://download.sourceforge.net/libpng/libpng-1.6.37.tar.gz & \ 
wget https://sourceforge.net/projects/libjpeg-turbo/files/2.1.3/libjpeg-turbo-2.1.3.tar.gz & \
wget http://download.osgeo.org/libtiff/tiff-4.4.0.tar.gz & \ 
wget https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-1.2.2.tar.gz & \
wget http://www.leptonica.org/source/leptonica-1.82.0.tar.gz &\
wget https://github.com/tesseract-ocr/tesseract/archive/refs/tags/5.0.1.tar.gz & wait

RUN tar -xvzf libpng-1.6.37.tar.gz & tar -xvzf libjpeg-turbo-2.1.3.tar.gz & tar -xvzf tiff-4.4.0.tar.gz &\
 tar -xvzf leptonica-1.82.0.tar.gz & tar -xvzf 5.0.1.tar.gz & tar -xvzf libwebp-1.2.2.tar.gz & wait
# download and build libpng
WORKDIR $HOME/temp_installers/libpng-1.6.37
RUN ./configure && make -j5 && make install

# download and build libjpeg
# RUN mkdir -p /usr/local/man/man1
RUN mkdir $HOME/temp_installers/libjpeg-turbo-2.1.3/build
WORKDIR $HOME/temp_installers/libjpeg-turbo-2.1.3/build
# RUN ./configure --prefix=/usr/local --libdir=/usr/local/lib && make -j5 && make install
RUN cmake -G"Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr/local .. && make -j5 && make install

# download and build libtiff
# WORKDIR $HOME/temp_installers/tiff-4.4.0
# RUN ./configure --prefix=/usr/local --libdir=/usr/local/lib && make -j5 && make install

# build webp
WORKDIR $HOME/temp_installers/libwebp-1.2.2
RUN ./configure --prefix=/usr/local --libdir=/usr/local/lib && make -j5 && make install

# download and build leptonica
WORKDIR $HOME/temp_installers/leptonica-1.82.0
RUN ./autogen.sh && ./configure && make -j5 && make install

# download and build tesseract
WORKDIR $HOME/temp_installers/tesseract-5.0.1
RUN ./autogen.sh
RUN PKG_CONFIG_PATH=/usr/local/lib/pkgconfig LIBLEPT_HEADERSDIR=/usr/local/include ./configure --with-extra-includes=/usr/local/include --with-extra-libraries=/usr/local/lib
RUN LDFLAGS="-L/usr/local/lib" CFLAGS="-I/usr/local/include" make -j5 && make install && ldconfig

# download langauge files
WORKDIR $HOME/temp_installers
RUN wget https://github.com/tesseract-ocr/tessdata_fast/blob/main/ara.traineddata;\
wget https://github.com/tesseract-ocr/tessdata_fast/blob/main/eng.traineddata;\
wget https://github.com/tesseract-ocr/tessdata_fast/blob/main/rus.traineddata;\
wget https://github.com/tesseract-ocr/tessdata_fast/blob/main/spa.traineddata;\
wget https://github.com/tesseract-ocr/tessdata_fast/blob/main/chi_sim.traineddata;\
wget https://github.com/tesseract-ocr/tessdata_fast/blob/main/chi_sim_vert.traineddata;\
wget https://github.com/tesseract-ocr/tessdata_fast/blob/main/chi_tra.traineddata;\
wget https://github.com/tesseract-ocr/tessdata_fast/blob/main/chi_tra_vert.traineddata;
# move language files to the shared library
RUN mv *.traineddata /usr/local/share/tessdata
WORKDIR $HOME
RUN rm -rf $HOME/temp_installers
# remove build tools + wget because they pose security risk
RUN yum -y remove gcc gcc-c++ make wget automake autoconf pkg-config 


# install the base package
COPY ./dist /tmp/packages
RUN pip install /tmp/packages/${APPLICATION}-*.tar.gz

# uncomment and replicate if additional pypi packages are needed
# RUN pip install pytesseract=0.3.9 numpy=1.22.4 opencv-python-headless=4.5.5.64 

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

# remove temporary python files
RUN rm -rf /tmp/packages /tmp/lib

# arbitrary user, support running as non-root. Required on OpenShift. Generally a good practice.
USER 1001
ENTRYPOINT [ "sh", "/opt/rescircuits/entrypoint.sh" ]
