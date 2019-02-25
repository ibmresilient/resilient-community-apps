
echo "Removing old"

package_name="fn_docker"

echo $package_name

rm -rf $package_name

echo "Running codegen"
resilient-circuits codegen -p $package_name -m $package_name \
--datatable \
"docker_integration_invocations" \
--rule \
"Validate MD5 is in NSRL Whitelist" \
"Search for Subdomains using Amass" \
"Analyze Memory Sample with Volatility" \


echo "Copying new customize.py"
cp $package_name/$package_name/util/customize.py ../$package_name/util/customize.py

# echo "Copying new setup.py"
# cp $package_name/setup.py ../setup.py

rm -rf $package_name

echo "Complete"