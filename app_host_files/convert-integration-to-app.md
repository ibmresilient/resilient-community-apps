Steps: 
## Download and Install integration code. 
When preparing to convert an integration into an app; ideally start from the master branch of the resilient-community-apps repo and branch off to have your own workspace for conversion.

## Initial Test with Integration Server
In order to prevent a duplication of testing efforts and being blocked by an issue which may appear to be AppHost related but is not, consider first testing the integration using the traditional architecture. In particular with vendor submissions this should be the first step followed as some apps submitted by vendors depending on submission time may have issues with Python3 our now standard version for integrations. 

## Performing an initial test using an integration server:

+ Run `setuptools` to generate a sdist zip/tar.gz file. `python setup.py sdist`
+ Create a new virtual environment to house just this integration; this is particularly important to ensure the testing/verification is performed in what can be considered a 'clean room' environment.
+ Install the integration package into the newly created and activated virtual environment
+ run resilient-circuits customize -l fn-integration-name to bring in the UI elements associated with this integration package. 

The extent of the testing here should at a minimum confirm that the integration does not have compatibility issues with Python 3. An end 2 end test can be performed where appropriate. After following the steps, provided there are no issues we can progress to AppHost testing. 

## Preparing an AppHost package for the App Exchange

After confirming the basic functionality of the integration and its compatibility with python 3 the next step is to prepare an App Package to verify the AppHost portion of the test and ultimately upload the new AppHost package. 

If the code is in master an app package will be prepared for you and should be available in the releases tab or resilient-community-apps

To prepare a package you will need resilient-sdk. A good practice here would be to reuse the same virtual environment that was created for the previous verification. 

### Prepare AppHost package

#### Community/Supported App
A number of integrations in resilient-community-apps already have a Dockerfile ready for you.
Alternatively a number of placeholder/starter files are available in this directory for the AppHost conversion.
These files can be used with the `resilient-sdk package` command to prepare an App.

To copy over the changes from the dockerfile branch to whatever branch you want to do the conversion on a script is provided in the `app_host_files` directory. 

> Ensure to review the Dockerfile you are using during the conversion of an App. In most cases no extra changes will be needed for the Dockerfile however depending on the integration there may be dependency issue or extra steps needed. An example of this is the ODBC integration which requires additional packages to be specified in the Dockerfile.

`resilient-sdk package -p <path to your integration>`
The resilient-sdk `package` command is used to convert an existing integration package into an AppHost compatible package. The command is used to modify the Dockerfile which will be used to run the App as a container as well as confirm the existence of files such as an `apikey_permissions.txt` file which will be used to limit the types of things the App can do to only what it should be able to do. Additionally package will create a .tar.gz/.zip file.

The SDK package command used the setup.py file to gather needed values for the Dockerfile and updates the Dockerfile with them.
In order for the SDK package command to work fully; a number of files need to brought into the directory of the integration you are planning to convert into an app. 
The package command will then modify values as appropriate in these files.

+ Deployment of the image file to quay 
+ App-fn_integration-version.zip verification on AppHost before publish
+ publication of app update with new tag and app host zip 
+ Final smoke check on the thing that was uploaded 

After this, the newly created App is almost ready for AppHost testing. The remaining piece is understanding and building out the required permissions

#### API Key Permissions 
Using the AppHost involves having an App which can make use of API keys and have permissions limited to what is needed for that given App. 
A convenience given by app host is by providing a `apikey_permissions.txt` file, the provision of API keys with the needed permissions can be handled by the AppHost itself. 

##### Figuring out the permissions
Understanding what permissions a given App needs is a bit of trial and error but it can be made easier by searching for any API calls made with the resilient_circuits client. Gathering these API calls could speed up the process of identifying what permissions are needed.

### Install the AppHost package and test
Most of the testing for a given integration/app will have been done by this stage and the remaining things to test are that : 
+ The newly created App package works with an AppHost
+ The provided API Key permissions allow the app to work with its generated API Key
+ There are no issues brought about with the containerization of the package

To install the App into AppHost head to Administrator Settings > Apps and click the Install button.
This will present a modal where you can upload the App package.

### Downloaded newly published app from AppExchange and perform final sanity check
As a final just incase, once the app is approved for AppX a final check of it by downloading and again installing it could be done.