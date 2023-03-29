#!/bin/bash
# perform changes to a package to prepare it for publication
# files updated:
#  LICENSE - replaced with MIT license
#  setup.py - changes to author, author_email, url, license based on community or supported publication
#  *.py - added copyright statement
#
TEMPLATE_DIR=`dirname $0`
#
if [ $# = 2 ]
then
  package_dir=$2
else
  echo "Usage: prep_package.sh c[ommunity]|s[upported] package_dir"
  exit 1
fi

# two different scripts for community apps vs supported apps
if [ $1 = 'community' ] || [ $1 = 'c' ]; then
  sed_file=setup_community.sed
elif [ $1 = 'supported' ] || [ $1 = 's' ]; then
  sed_file=setup_supported.sed
else
  echo "Usage: prep_package.sh c[ommunity]|s[upported] package_dir"
  exit 1
fi

# start making changes to files
echo Updating license file
find ${package_dir} -name LICENSE -exec cp ${TEMPLATE_DIR}/LICENSE {} \;
#
echo Fixing setup.py
sed -i .bak -f ${TEMPLATE_DIR}/${sed_file} ${package_dir}/setup.py
#
echo Adding copyright statement
find ${package_dir} \( -name \*.py -and -not -name __init__.py -and -not -name setup.py \) -print -exec \
sed -i .bak -f ${TEMPLATE_DIR}/copyright.sed {} \;
