
if [ $# -eq 0 ]
    then 
        destination_folder="./"
else
    destination_folder=$1
fi
echo $destination_folder
tar -czvf $destination_folder/res_qraw_mitre.tar.gz qraw_mitre.res README.md screenshots

