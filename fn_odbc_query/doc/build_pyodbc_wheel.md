# How To Set Up RHEL to Build pyodbc wheel

* update yum and enable EPEL repository, log in as root
```
$ yum -y update
$ yum install epel-release
```
* install Python 2.7
```
$ yum install gcc gcc-c++ openssl-devel bzip2-devel
$ cd /usr/src
$ wget https://www.python.org/ftp/python/2.7.15/Python-2.7.15.tgz
$ tar xzf Python-2.7.15.tgz
$ cd Python-2.7.15
$ ./configure --enable-optimizations
$ make altinstall
(Important: make altinstall is used to prevent replacing the default python binary file /usr/bin/python therefore not removing older versions of Python and breaking your system)
$ /usr/local/bin/python2.7 -V
Python 2.7.15
```
* install Python 3.6
```
$ cd /usr/src
$ wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8rc1.tgz
$ tar xzf Python-3.6.8rc1.tgz
$ cd Python-3.6.8rc1
$ ./configure --enable-optimizations
$ make altinstall
$ /usr/local/bin/python3.6 -V
Python 3.6.8rc1
```
* install pip
```
$ curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
$ python2.7 get-pip.py
$ python3.6 get-pip.py
```
* check your installed packages, you need setuptools and wheel
```
$ pip list
Package    Version
---------- -------
pip        18.1   
setuptools 40.6.2
virtualenv 16.2.0
wheel      0.32.3
```
* install git
```
$ yum install git
```
(Important: Installing Git from default repositories will give you older version. If you looking to have a most recent version of Git, consider compiling from source)

* download pyodbc - clone github repo, you'll need it's tagging to successfully create pyodbc's wheel version
```
$ git clone https://github.com/mkleehammer/pyodbc.git
```
* create a setup.cfg file in pyodbc folder (see example here https://github.com/pypa/sampleproject)
```
$ cd pyodbc
$ vi setup.cfg
```
Add to setup.cfg:

```
[metadata]
# This includes the license file(s) in the wheel.
# https://wheel.readthedocs.io/en/stable/user_guide.html#including-license-files-in-the-generated-wheel-file
license_files = LICENSE.txt

[bdist_wheel]
# This flag says to generate wheels that support both Python 2 and Python
# 3. If your code will not run unchanged on both Python 2 and 3, you will
# need to generate separate wheels for each Python version that you
# support. Removing this line (or setting universal to 0) will prevent
# bdist_wheel from trying to make a universal wheel. For more see:
# https://packaging.python.org/guides/distributing-packages-using-setuptools/#wheels
universal=1
```
* get required ODBC header files
```
$ yum install unixODBC-devel
```
* create virtualenv for both Python versions
```
$ pip install virtualenv
$ cd ~/
$ mkdir venv
$ virtualenv --python=python2.7 ~/venv/pyodbc2.7
$ virtualenv --python=python3.6 ~/venv/pyodbc3.6
```
* activate your Py2 virtual env
```
$ source ~/venv/pyodbc2.7/bin/activate
```
* go back to Pyodbc folder, where setup.py is and build the wheel
```
$ python setup.py bdist_wheel
```
* deactivate your Py2 virtual env
```
$ deactivate
```
* activate your Py3 virtual env
```
$ source ~/venv/pyodbc3.6/bin/activate
```
* go back to Pyodbc folder, where setup.py is and build the wheel
```
$ python setup.py bdist_wheel
```
* deactivate your Py3 virtual env
```
$ deactivate
```
* look for your wheels in dist folder
```
pyodbc/dist/pyodbc-4.0.25-cp27-cp27m-linux_x86_64.whl
pyodbc/dist/pyodbc-4.0.25-cp36-cp36m-linux_x86_64.whl
```