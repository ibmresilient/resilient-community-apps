# Build centos env with python 2.7.13


FROM library/centos:7.4.1708

RUN yum -y update
RUN yum install -y epel-release && yum groupinstall -y 'development tools'
RUN yum install -y zlib-dev openssl-devel sqlite-devel bzip2-devel xz-libs wget gcc java makeself
RUN wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tar.xz
RUN tar xvfJ Python-2.7.13.tar.xz
WORKDIR Python-2.7.13
RUN ./configure --prefix=/usr/local && make && make altinstall
RUN curl https://bootstrap.pypa.io/get-pip.py | python2.7

RUN yum install -y python-pip
RUN python -m pip install --upgrade pip setuptools

# Install twine
RUN pip2.7 install twine boxsdk


ENTRYPOINT /bin/bash
