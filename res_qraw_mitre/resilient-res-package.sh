#
#   Note this is a script used by jenkins to auto-build this package.
#   The ../.script/build_packages.sh searches for all
#   resilient-res-package.sh files in all folders, and call them
#   one by  one. It will pass the destination folder as the first
#   parameter.
#
if [ $# -eq 0 ]
    then 
        destination_folder="./"
else
    destination_folder=$1
fi
echo $destination_folder
tar -czvf $destination_folder/res_qraw_mitre.tar.gz qraw_mitre.res README.pdf README.md screenshots

