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

# install tools required to build tesseract and leptonica
RUN yum -y install libstdc++ autoconf automake libtool autoconf-archive pkg-config gcc gcc-c++ make cmake zlib-devel wget libarchive 

# make a temp dir we can delete after building and installing
RUN mkdir $HOME/temp_installers
WORKDIR $HOME/temp_installers

# ! Note: many lines are written in ways that that minimize layers in the docker file
# !       most importantly, `&` is used to run download and unpack commands async
# !       if you choose to edit this docker file, please keep that in mind

# use wget to download tar.gz of libraries that are not available through yum
# libpng, libjpeg, and libwebp are for handling those respective files
# leptonica is required for tesseract

RUN wget https://download.sourceforge.net/libpng/libpng-1.6.37.tar.gz & \ 
wget https://sourceforge.net/projects/libjpeg-turbo/files/2.1.3/libjpeg-turbo-2.1.3.tar.gz & \
wget https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-1.2.2.tar.gz & \
wget http://www.leptonica.org/source/leptonica-1.82.0.tar.gz & \
wget https://github.com/tesseract-ocr/tesseract/archive/refs/tags/5.0.1.tar.gz & wait

# extract all of the source code
RUN tar -xvzf libpng-1.6.37.tar.gz & tar -xvzf libjpeg-turbo-2.1.3.tar.gz &\
 tar -xvzf leptonica-1.82.0.tar.gz & tar -xvzf 5.0.1.tar.gz & tar -xvzf libwebp-1.2.2.tar.gz & wait

# ! Note: when building, it is crucial to use `-j5` or however many jobs your environment can handle.
# !       running a single job is too slow - for IBM SOAR developers, it will time-out in Travis

# download and build libpng
WORKDIR $HOME/temp_installers/libpng-1.6.37
RUN ./configure && make -j5 && make install

# download and build libjpeg
RUN mkdir $HOME/temp_installers/libjpeg-turbo-2.1.3/build
WORKDIR $HOME/temp_installers/libjpeg-turbo-2.1.3/build
RUN cmake -G"Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr/local .. && make -j5 && make install

# build webp
WORKDIR $HOME/temp_installers/libwebp-1.2.2
RUN ./configure --prefix=/usr/local --libdir=/usr/local/lib && make -j5 && make install

# download and build leptonica
WORKDIR $HOME/temp_installers/leptonica-1.82.0
RUN ./autogen.sh && ./configure --prefix=/usr/local/ --libdir=/usr/local/lib && make -j5 && make install

# download and build tesseract
WORKDIR $HOME/temp_installers/tesseract-5.0.1
RUN ./autogen.sh
RUN PKG_CONFIG_PATH=/usr/local/lib/pkgconfig LIBLEPT_HEADERSDIR=/usr/local/include ./configure --with-extra-includes=/usr/local/include --with-extra-libraries=/usr/local/lib --with-extra-libraries=/usr/local/lib64 
RUN LDFLAGS="-L/usr/local/lib" CFLAGS="-I/usr/local/include" make -j5 && make install && ldconfig
RUN ldd $(which tesseract)

# ! Note: the below lines download tesseract lanuage files and places them into the right folder
# !       these files can be got from both the main tesseract github as well as github.com/tesseract-ocr/tessdata_fast
# !       please note that when you `wget` from github, it needs to be tessdata_fast/raw/main/{lang_file} NOT tessdata_fast/blob/main/{lang_file} 
# !       if you would like to add your own languages, simply find the right lang code from the link below, and download it from github
# !       https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html

WORKDIR $HOME/temp_installers
RUN wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/ara.traineddata &\
wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/eng.traineddata &\
wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/rus.traineddata &\
wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/spa.traineddata &\
wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/chi_sim.traineddata &\
wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/chi_sim_vert.traineddata &\
wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/chi_tra.traineddata &\
wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/chi_tra_vert.traineddata &\
wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/oci.traineddata & \
wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/ori.traineddata & \
wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/osd.traineddata & wait

# move language files to the shared library
RUN mv *.traineddata /usr/local/share/tessdata
WORKDIR $HOME
RUN rm -rf $HOME/temp_installers

# remove build tools + wget 
RUN yum -y remove gcc gcc-c++ make wget
RUN yum -y install libtiff libjpeg libpng

# install the base package
COPY ./dist /tmp/packages
RUN pip install /tmp/packages/${APPLICATION}-*.tar.gz

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
