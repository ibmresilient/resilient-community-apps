#/bin/bash
# This script creates a self-extracting .run file in order to install resilient-circuits and other
# community apps on linux base systems. The intent is to support air-gapped environments and to use
# virtualenv so as not to effect system level pyton libraries.
# Several steps are performed in the creation of this .run file based on the need to collect
# architecture specific libraries and account for some libraries which are not on pypi.org
# Ex. makedotrun.sh build/ template/

# print an optional message and a usage statement when the program parameter list is incorrect
function usage {
  if [ "$1" != "" ]; then
    echo $1
  fi
  echo "usage: $0 <directory to build> <template directory> <result directory>"
  exit 1
}

# some libraries are not on pypi and need to be loaded directly from github
function buildFromGithub {
  for pkg in "$@"
  do
    echo ">>> ${pkg}"
    pip download git+git://github.com/${pkg}.git ${LINKS_INFO}
  done
}

# some libraries are best loaded from whl files but then specific OS and hardware
# architectures need to be specified. This function will attempt to load the library
# list covering the environments needed for specific libraries which are problematic
# if loaded from a tar.gz source distribution
function loadManyLinux {
  # add the specific linux wheels
  for pkg in "$@"
  do
    echo ">>> ${pkg}"
    for abi in 'cp27m' 'cp27mu'
    do
      # suppress errors associated with not finding 'pycparser'
      pip download ${pkg} ${LINKS_INFO} --platform=manylinux1_x86_64 --abi=${abi} --python-version=27 --only-binary=:all:  2>&1  | grep -v pycparser
    done
    for abi in 34 36
    do
      # suppress errors associated with not finding 'pycparser'
      pip download ${pkg} ${LINKS_INFO} --platform=manylinux1_x86_64 --abi=cp${abi}m --python-version=${abi} --only-binary=:all:  2>&1  | grep -v pycparser
    done
    # get the tar.gz file too
    pip download ${pkg} ${LINKS_INFO} --no-binary=:all:
  done

}

# load libraries into our lib directory and follow any dependencies for dependent libraries as well
function loadGeneral {
  # add the environment specific libraries
  for pkg in "$@"
  do
    echo ">>> ${pkg}"
    pip download ${pkg} ${LINKS_INFO}
  done
}

# load libraries specific to the python versions we support
function loadVersion {
  # add the environment specific libraries
  for pkg in "$@"
  do
    echo ">>> ${pkg}"

    for version in 27 36
    do
      # suppress errors associated with not finding 'future'
      pip download ${pkg} ${LINKS_INFO} --only-binary=:all: --python-version=${version} 2>&1 | grep -v future
    done
    # get the tar.gz file too
    pip download ${pkg} ${LINKS_INFO} --no-binary=:all:
  done
}

# collect all the public facing community apps and package as source distributions (tar.gz files)
function buildCommApps {
  RC_APPS="${TMP_DIR}/resilient-community-apps"
  #
  if [ -d ${RC_APPS} ]; then
    rm -Rf ${RC_APPS}
  fi
  #
  git clone -b ${2} ${1} ${RC_APPS}
  # find all packages with a setup.py file to build
  setup_files=(`find ${RC_APPS} -depth 2 -type f -name 'setup.py'`);

  for setup in ${setup_files[@]};
  do
    pkg_dir=$(dirname "${setup}")
    echo ">>> $pkg_dir";
    (cd $pkg_dir && python setup.py -q sdist --dist-dir ${BUILD_DIR});
  done;
}

# B E G I N
if [ $# -ne 3 ]; then
  usage
fi

if [ ! -d "$2" ]; then
  usage "template directory is missing"
fi

if [ ! -d "$3" ]; then
  usage "result directory is missing"
fi

TEMPLATE_DIR=$2
TMP_DIR=/tmp
MANYLINUX1="cryptography cffi lxml MarkupSafe"
ENV_LIBS="pip SecretStorage setuptools setuptools_scm watchdog wheel keyring==7.3 virtualenv"
# needed for VERSION_LIBS
EARLY_LIBS="pycparser future configobj"
VERSION_LIBS="enum34 circuits investigate pymisp beautifulsoup4 pyodbc"
# on pypi
RESILIENT_LIBS="rc-webserver rc-cts resilient-circuits"
GIT_LIBS="williballenthin/vivisect fireeye/flare-floss yeti-platform/pyeti"
# ex. "github.com/ibmresilient/resilient-community-apps.git"
MAKESELF=~/Downloads/makeself-2.4.0/makeself.sh
RESILIENT_COMM_APPS=git@github.ibm.com:Resilient/resilient-community-apps.git
REPO_BRANCH=public

# expand any directory references to path shortcuts such as ~
if [ "`command -v greadlink`" != "" ]; then
  BUILD_DIR=`greadlink -f $1`
  RESULT_DIR=`greadlink -f $2`
else
  BUILD_DIR=`readlink -f $1`
  RESULT_DIR=`readlink -f $2`
fi
# complete path into with ${BUILD_DIR}
LINKS_INFO="--find-links ${BUILD_DIR} --find-links ${BUILD_DIR}/lib -d ${BUILD_DIR}/lib/"

# S T A R T I N G
# start with a fresh directory
if [ -d ${BUILD_DIR} ]; then
  rm -Rf ${BUILD_DIR}
fi

cp -r ${TEMPLATE_DIR} ${BUILD_DIR}

cd ${BUILD_DIR}

# add the environment specific libraries
loadGeneral ${ENV_LIBS}
loadGeneral ${EARLY_LIBS}
# add the specific linux wheels
loadManyLinux ${MANYLINUX1}
# these libraries are only on git
buildFromGithub ${GIT_LIBS}
# add community apps
buildCommApps ${RESILIENT_COMM_APPS} ${REPO_BRANCH}
# get resilient-circuits
loadGeneral ${RESILIENT_LIBS}
# run all tar.gz files and get their dependencies
loadGeneral `ls *.tar.gz`
# add the libraries which are python version specific
loadVersion ${VERSION_LIBS}
#
# append the README file with the contents of the directory
ls -1 ${BUILD_DIR} >>${BUILD_DIR}/README
#
# end with makeself
/bin/bash ${MAKESELF} --target resilient-circuits ${BUILD_DIR} ${RESULT_DIR}/resilient-circuits.run "Resilient-Circuits" ./setup
