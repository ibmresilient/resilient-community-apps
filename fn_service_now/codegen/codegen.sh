
echo "Removing old"

package_name="fn_service_now"

echo $package_name

rm -rf $package_name

echo "Running codegen"
resilient-circuits codegen -p $package_name -m $package_name \
--datatable "sn_records_dt" \
--rule \
"SNOW: Update Data Table on Status Change [Incident]" \
"SNOW: Update Data Table on Status Change [Task]" \
"SNOW: Add Attachment to Record" \
"SNOW: Close Record [Incident]" \
"SNOW: Close Record [Task]" \
"SNOW: Create Record [Incident]" \
"SNOW: Create Record [Task]" \
"SNOW: Send as Additional Comment" \
"SNOW: Send as Work Note" \
"SNOW: Close Record from Data Table" \
--field \
"sn_snow_record_id" \
"sn_snow_record_link" \

echo "Copying new customize.py"
cp $package_name/$package_name/util/customize.py ../$package_name/util/customize.py

# echo "Copying new setup.py"
# cp $package_name/setup.py ../setup.py

rm -rf $package_name

echo "Complete"