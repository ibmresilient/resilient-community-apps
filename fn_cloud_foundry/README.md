# Resilient Function Cloud Foundry

This function interfaces with Cloud Foundry platform to allow the user to manage deployed applications, their instances, and deploy new applications. Managing the applications includes starting/stopping, updating, restaging, deleting, and getting various types of information about it. This package implements these actions in 3 functions, 3 example workflows and 3 example rules.
This package is a wrapper around Cloud Foundry’s API with possibilities to be adjusted for different platform providers. On the time of release the latest stable version is: https://apidocs.cloudfoundry.org/3.1.0/. 


You must edit the `setup.py` before distribution;
it should contain your actual contact and license information.

## To install in *development mode*:

    pip install -e ./fn_cloud_foundry/

After installation, the package will be loaded by `resilient-circuits run`.


## To uninstall:

    pip uninstall fn_cloud_foundry


## To package for distribution:

    python ./fn_cloud_foundry/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz

## Add Cloud Foundry configuration details to the config file:

    resilient-circuits config -u

Set the following values in the config file (`~/.resilient/app.config`) under the `[fn_cloud_foundry]` section:

```
[fn_cloud_foundry]
#Base url endpoint of your CF platform
#For example, for IBM’s BlueMix it is: https://api.ng.bluemix.net/
cf_api_base=https://api.ng.bluemix.net/
#
#Enter only what’s required by your authenticator.
#For example, the default BlueMixCF authenticator only requires apikey.
#
cf_api_apikey=
##Enter username and password if needed for access to DockerHub for Create Application function
cf_api_username=
cf_api_password=
```

## How to use the function

1. Import the necessary customization data into the Resilient platform:

		resilient-circuits customize
		
    This import data contains:
	* Function inputs:
         `fn_cloud_foundry_action,
         fn_cloud_foundry_additional_parameters_json,
         fn_cloud_foundry_applications,
         fn_cloud_foundry_instance_action,
         fn_cloud_foundry_instances,
         fn_cloud_foundry_space_guid`
    * Message Destination: `cloud_foundry`
	* Functions: `fn_cloud_foundry_create_app,
         fn_cloud_foundry_instance_command,
         fn_cloud_foundry_manage_applications`
 	* Workflows: `cloud_foundry_create_an_application,
         cloud_foundry_instance_command,
         cloud_foundry_stop_application`
 	* Rules: `Example: Cloud Foundry Create Application,
         Example: Cloud Foundry Instance Command,
         Example: Cloud Foundry Stop Application`
		
2. Update and edit `app.config`:

		resilient-circuits configure -u

3. Start Resilient Circuits:
   
         resilient-circuits run
    

4. Trigger the rule.
