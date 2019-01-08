#!/bin/bash

set -e

dir=build/py2
srcdir=$dir/rc_data_feed

mkdir -p $srcdir

find rc_data_feed -name '*.py' -exec cp {} $srcdir \;
cp setup.py $dir

3to2 -n --no-diffs -w $(find $srcdir -name '*.py')

cd $dir
python setup.py sdist

