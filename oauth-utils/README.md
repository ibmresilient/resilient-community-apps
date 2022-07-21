<!--

  It is best edited using a Text Editor with a Markdown Previewer. VS Code
  is a good example. Checkout https://guides.github.com/features/mastering-markdown/
  for tips on writing with Markdown

  All fields followed by "::CHANGE_ME::"" should be manually edited

  If you make manual edits and run docgen again, a .bak file will be created

  Store any screenshots in the "doc/screenshots" directory and reference them like:
  ![screenshot: screenshot_1](./screenshots/screenshot_1.png)

  NOTE: If your app is available in the container-format only, there is no need to mention the integration server in this readme.
-->

# OAuth utilities for IBM SOAR apps

## Table of Contents
- [Release Notes](#release-notes)
- [Overview](#overview)
  - [Key Features](#key-features)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Install](#install)
  - [Configuration](#configuration)
  - [Usage](#usage)
- [Troubleshooting & Support](#troubleshooting--support)
---

## Release Notes
<!--
  Specify all changes in this release. Do not remove the release 
  notes of a previous release
-->
| Version | Date | Notes |
| ------- | ---- | ----- |
| 1.0.0 | 07/2022 | Initial Release |

---

## Overview
<!--
  Provide a high-level description of the function itself and its remote software or application.
  The text below is parsed from the "description" and "long_description" attributes in the setup.py file
-->
**OAuth utilities**

The OAuth Utilities package provides tools and utilities to support OAuth for IBM SOAR apps.

### Key Features
<!--
  List the Key Features of the package
-->
* A utility to generate an OAuth 2.0 authorization code flow refresh token for an IBM SOAR app.

---

## Requirements
<!--
  List any Requirements 
-->
### Python Environment
Both Python 3.6 and python 3.9 are supported.
Additional package dependencies may exist for each of these packages:
* Jinja2>=30.0.0
* six>=39.0.0
* urllib3>=0.18.2
* requests>=0.18.2
* flask>=2.0.3
* pyOpenssl>=0.18.2
* click>=8.0.4

#### Prerequisites
* Utility `oauth2_generate_refresh_token`: An OAuth 2.0 identity provider service with an app or project configured to allow user access to a 3rd party application.
#### Configuration
* Utility `oauth2_generate_refresh_token`: The following settings must be available for the OAuth 2.0 service.
```
client_id 
client_secret 
scope 
token_url 
auth_url
```
#### Permission
* Utility `oauth2_generate_refresh_token`: The provider OAuth 2.0 configuration settings must have required access to the 3rd party app.

---
## Installation

### Install

You can download the oauth-utils app packages from the [IBM Resilient Community](https://github.com/ibmresilient/resilient-community-apps)  or [IBM X-Force App Exchange](https://exchange.xforce.ibmcloud.com).

Complete the following steps to install the `oauth-utils` Python package:
1. Ensure that your python environment is up to date, as follows:
```
pip install --upgrade pip
pip install --upgrade setuptools
```
2. Go to the folder where the downloaded app is located and unzip. For example:
```
unzip oauth-utils-1.0.0-00001.zip
``` 
3. The app zip file contains a python package. Install the package using the following command:
```
pip install --upgrade oauth-utils-1.0.0-00001.tar.gz
```
4. If running in browser mode, install optional python modules using the following command:
```
pip install --upgrade oauth-utils-1.0.0-00001.tar.gz[browser]
```
### Package Configuration

#### Utility: oauth2_generate_refresh_token

#### Required Settings

The following table provides the settings required to execute this utility. These settings are either read from an app.config file or provided as command-line arguments.

| Setting/Argument | Required | Example | Cli usage| Description |
| ------ | :------: | ------- | ----------- | ----------- |
| client_id | Yes  | `1234567a-abc8-90d1-2efa3-123456789abcd` | `-ci or --client_id <CLIENT_ID>` | *OAuth 2.0 application or project client ID.* |
| client_secret | Yes | `ABCDEF-123456789abcd123456789a_aWX4` | `-ci or --client_secret <CLIENT_SECRET>` | *OAuth 2.0 application or project client Secret.* |
| scope | Yes | `https://mail.myservice.com/` | `-sc or --scope <SCOPE>` |  *OAuth 2.0 application or project scope.* |
| token_url | Yes | `https://myservice.com/o/oauth2/token` | `-tu or --token_url <TOKEN_URL>` | *OAuth 2.0 application or project token url.* |
| auth_url | Yes  | `https://myservice.com/o/oauth2/auth` | `-au or --auth_url <AUTH_URL>` | *OAuth 2.0 application or project authorization url.* |

**_NOTE:_** The settings are read from an app.config file if one is located in the environment. Alternative app.config files can be selected using the -c or --config_file option.

**_NOTE:_** The settings are all read either from an app.config file or as command-line arguments. These operations are mutually exclusive.

#### Arguments
The following table provides additional optional command-line arguments which can be used to execute this utility.

| Argument | Required | Example | Description |
| ------ | :------: | ------- | ----------- |
| browser | No  | `-b or --browser` | *Browser mode. Use a browser to control the flow and run a callback listener.* |
| config_file | No | `-c or --config_file <path_to_config_file>/app.config` | *Location of app.config file to override default.* |
| port | No | `-p or --port 4000` |  *TCP port used for callback url and listener (default is 8080).* |
| timeout | No | `-t or --timeout 90` | *Timeout callback listener after timeout (seconds).* |
| app_name | No  | `-a or --app_name fn_outbound_email` | *The app name to read if more than one app is defined in an app.config file.* |

---
### Usage
The OAuth Utilities for SOAR app supplies various subcommands to help with OAuth support for apps in a SOAR environment.
```
$ oauth-utils
usage: 
    $ oauth-utils <subcommand> ...
    $ oauth-utils -v <subcommand> ...
    $ oauth-utils oauth2_generate_refresh_token
    $ oauth-utils oauth2_generate_refresh_token -b
    $ oauth-utils oauth2_generate_refresh_token -c <path_to_config_file>/app.config -a <app_name>
    $ oauth-utils -h
    

Tools to manage OAuth for IBM SOAR apps

optional arguments:
  -h, --help                       show this help message and exit
  -v, --verbose                    Set the log level to DEBUG
``` 

#### Utility: oauth2_generate_refresh_token

A utility to generate a refresh token for an OAuth 2.0 service (to be used with an IBM SOAR app).
``` 
usage: $ oauth-utils <subcommand> ...
    $ oauth-utils -v <subcommand> ...
    $ oauth-utils oauth2_generate_refresh_token
    $ oauth-utils oauth2_generate_refresh_token -b
    $ oauth-utils oauth2_generate_refresh_token -c <path_to_config_file>/app.config -a <app_name>
    $ oauth-utils -h oauth2_generate_refresh_token
       [-h] [-c CONFIG_FILE] [-t TIMEOUT] [-b] [-a APP_NAME] [-p PORT]
       [-ci CLIENT_ID] [-cs CLIENT_SECRET] [-sc SCOPE] [-tu TOKEN_URL]
       [-au AUTH_URL]

A utility to generate a refresh token for an OAuth 2.0 service (to be used with an IBM SOAR app).
The parameters used for the OAuth 2.0 service can be taken either from an app.config file or manually from the command line.
(For further information please refer to the auth_utils documentation.)

optional arguments:
  -h, --help                       show this help message and exit
  -c CONFIG_FILE, --config_file CONFIG_FILE
                                   Location of app.config file
  -t TIMEOUT, --timeout TIMEOUT    Timeout callback listener after timeout (seconds)
  -b, --browser                    Use browser and listener
  -a APP_NAME, --app_name APP_NAME
                                   Specify the app name
  -p PORT, --port PORT             Specify port for callback url and listener
  -ci CLIENT_ID, --client_id CLIENT_ID
                                   Specify OAuth 2.0 application client ID
  -cs CLIENT_SECRET, --client_secret CLIENT_SECRET
                                   Specify OAuth 2.0 application client secret
  -sc SCOPE, --scope SCOPE         Specify OAuth 2.0 application scope
  -tu TOKEN_URL, --token_url TOKEN_URL
                                   Specify OAuth 2.0 application token url
  -au AUTH_URL, --auth_url AUTH_URL
                                   Specify OAuth 2.0 application authorization url
```

---

## Setup of OAuth 2.0 credentials for 3rd party providers

To use the oauth2_generate_refresh_token utility, set up an app or project for an OAuth 2.0 identity provider service from which you can get the required configuration settings, such as:
```
client_id 
client_secret 
scope 
token_url 
auth_url
```
The setup procedure varies depending on the provider. This document provides examples for 2 well known services `Google Gmail` and `Microsoft Outlook 365`. These examples can be used to send email using SMTP.

### Creating OAuth 2.0 credentials for Gmail
#### Endpoints
Google Authorization endpoint - used by client to obtain authorization from the resource owner.
```
auth_url=https://accounts.google.com/o/oauth2/auth
```
Google Token endpoint - used by client to exchange an authorization grant or refresh token for an access token.
```
token_url=https://accounts.google.com/o/oauth2/token
```
#### Create the new project.
* As the SMTP email user, log in to [Google cloud](https://console.cloud.google.com/) and create a Google cloud project.
* Give your project a name, change the project ID if needed, and click the `Create` button.

    ![screenshot: oauth-utils-goog-create-project](./doc/screenshots/oauth-utils-goog-create-project.png)

    ![screenshot: oauth-utils-goog-create-project_2](./doc/screenshots/oauth-utils-goog-create-project_2.png)

#### Configure OAuth Consent Screen.
* In the APIs and Services section, click on OAuth Consent Screen and set the user type to `External`. Click on `Create`.

    ![screenshot: oauth-utils-goog-user-external](./doc/screenshots/oauth-utils-goog-user-external.png)

* Enter a name for your application and provide an email address where Google may contact you.

    ![screenshot: oauth-utils-goog-oc-app-info](./doc/screenshots/oauth-utils-goog-oc-app-info.png)

    ![screenshot: oauth-utils-goog-oc-dev-info](./doc/screenshots/oauth-utils-goog-oc-dev-info.png)


*  Provide one or more Scopes for Google APIs. Click the `Add Or Remove Scopes` button and add https://mail.google.com/ to the list of scopes. Click `Save` and `Continue`.

    ![screenshot: oauth-utils-goog-oc-dev-scopes](./doc/screenshots/oauth-utils-goog-oc-dev-scopes.png)

    ![screenshot: oauth-utils-goog-oc-dev-scopes_2](./doc/screenshots/oauth-utils-goog-oc-dev-scopes_2.png)
 
*  Since a User Type of `External` is used, you need to add a user who has access to the app. In this example, the test user is the same as the app user. Click `Add Users`, and  add the user. Click `Save` and `Continue`.

    ![screenshot: oauth-utils-goog-oc-dev-test-user](./doc/screenshots/oauth-utils-goog-oc-dev-test-user.png)
   
#### Configure Credentials.

* In the APIs & Services section, click on `Credentials` and then click on `Create credentials`.

    ![screenshot: oauth-utils-goog-creds-create](./doc/screenshots/oauth-utils-goog-creds-create.png)

* Select `OAuth Client ID` to create a new client ID then select `Desktop app`. The client ID is used verify application identify to Google’s OAuth servers.

    ![screenshot: oauth-utils-goog-creds-desktop](./doc/screenshots/oauth-utils-goog-creds-desktop.png)
    ![screenshot: oauth-utils-goog-creds-desktop_2](./doc/screenshots/oauth-utils-goog-creds-desktop_2.png)  

* When the OAuth client is created you are presented with a screen showing your client ID and secret.

  ![screenshot: oauth-utils-goog-creds-created](./doc/screenshots/oauth-utils-goog-creds-created.png)  

You can now add these credentials and scope to an app.config file or alternatively use as command-line arguments for the `oauth2_generate_refresh_token` utility.
```
client_id=337895628616-h4epvvbqv5946aun1u9qg7kqp6tu5c1j.apps.googleusercontent.com
client_secret=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
scope=https://mail.google.com/
token_url=https://accounts.google.com/o/oauth2/token
auth_url=https://accounts.google.com/o/oauth2/auth
```
* Execute the `oauth2_generate_refresh_token` utility using the new credentials as command-line arguments.
```
$ oauth-utils oauth2_generate_refresh_token -ci=337895628616-h4epvvbqv5946aun1u9qg7kqp6tu5c1j.apps.googleusercontent.com -cs=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 -sc=https://mail.google.com/ -tu=https://accounts.google.com/o/oauth2/token -au=https://accounts.google.com/o/oauth2/auth
Running from command line.
Using OAuth2 discrete settings from command-line arguments.

To authorize a token, copy the following URL into a browser and follow the directions then enter the generated callback URL below:

https://accounts.google.com/o/oauth2/auth?state=6a3290f368de76e0dc83d7a380ca91e8950a57ff2aabc94c706b3418743e2743&scope=https%3A%2F%2Fmail.google.com%2F&client_id=337895628616-h4epvvbqv5946aun1u9qg7kqp6tu5c1j.apps.googleusercontent.com&response_type=code&response_mode=query&redirect_uri=https%3A%2F%2Flocalhost%3A8080%2Fcallback

Enter callback URL: 
```
* Enter the URL in a browser login and follow the directions by clicking `Continue` in each presented screen.

  ![screenshot: oauth-utils-goog-web ](./doc/screenshots/oauth-utils-goog-web.png)
  
  ![screenshot: oauth-utils-goog-web_2 ](./doc/screenshots/oauth-utils-goog-web_2.png) 

* Eventually the user is presented with an `Unable to connect` message in the browser and a callback URL in the browser location window.

  ![screenshot: oauth-utils-goog-web-callback ](./doc/screenshots/oauth-utils-goog-web-callback.png) 

* Enter the callback address from the browser location window on the command line.
```
Enter callback URL: https://localhost:8080/callback?state=6c98b3f1dcc03245a5f9e525ad6ac11983dc26dadebeb497492462aa166e19f0&code=4/0AdQt8qjMgTnOh42tSkJRafz_uNmJIvOLsanTp9NUoj1YDBRr7oW94nqXADDHD1BIe6Bz6g&scope=https://mail.google.com/


refresh_token=1//07JEwfJ_7KNbWCgYIARAAGAcSNwF-L9IrH71Z4sT_VsmL4kO3rSaW4fEKKTpetFVhf6dfxDBuPxqB-KkE2DJEo_8Xo1hOkfP_RyY

```
* Add the resultant `refresh_token` to the app.config file for the required app.

**_NOTE:_** In the example we used a test user with User Type of `External`. Selecting User Type `Internal` will allow the application to access the Google api without having to go through the verification process.

See: [Setting up OAuth 2.0 with Google Cloud](https://support.google.com/cloud/answer/6158849?hl=en)

### Creating up OAuth 2.0 credentials for Microsoft Outlook
#### Endpoints
Microsoft Authorization endpoint - used by client to obtain authorization from the resource owner.
```
https://login.microsoftonline.com/<tenant_id>/oauth2/v2.0/authorize
```
Microsoft Token endpoint - used by client to exchange an authorization grant or refresh token for an access token.
```
https://login.microsoftonline.com/<tenant_id>/oauth2/v2.0/token
```
#### App Registration
* As the SMTP email user log in to the [Microsoft Azure Portal](https://portal.azure.com/) and authenticate.
* Under `Azure services`, click  on `Azure Active Directory`.
  
  ![screenshot: oauth-utils-ms-azure ](./doc/screenshots/oauth-utils-ms-azure.png)

* Click on `App Registrations` >`New Registration`.

  ![screenshot: oauth-utils-ms-new-reg ](./doc/screenshots/oauth-utils-ms-new-reg.png)

* Give your application a name. For `Redirect URI` select `Web` and enter `https://localhost:8080/callback`. Click `Register`.

  ![screenshot: oauth-utils-ms-register ](./doc/screenshots/oauth-utils-ms-register.png)

* Copy and save the Application (client) ID and Directory (tenant) ID locally.

  ![screenshot: oauth-utils-ms-cli-id ](./doc/screenshots/oauth-utils-ms-cli-id.png)

#### Authentication
* Under `Manage` on the left-hand menu, select `Authentication`.

   ![screenshot: oauth-utils-ms-auth ](./doc/screenshots/oauth-utils-ms-auth.png) 
  
* Select `Yes` for `Enable the following mobile and desktop flows` then click `Save`.
  
   ![screenshot: oauth-utils-ms-auth_2 ](./doc/screenshots/oauth-utils-ms-auth_2.png) 

#### API Permissions
* On the left-hand side under `Manage`, select `API Permissions`.
* Click `Add a permission`.
  
  ![screenshot: oauth-utils-ms-perms ](./doc/screenshots/oauth-utils-ms-perms.png) 
  
* On the Request API permission screen, select Microsoft Graph.
* In Graph API, choose Delegated permissions.
* Add the following permissions.
```
offline_access
SMTP.Send
``` 

  ![screenshot: oauth-utils-ms-perms_2 ](./doc/screenshots/oauth-utils-ms-perms_2.png) 
  
* You need an admin user account to `Grant admin consent for <user>` to enable these permissions.

  ![screenshot: oauth-utils-ms-grant ](./doc/screenshots/oauth-utils-ms-grant.png) 
  
  ![screenshot: oauth-utils-ms-grant_2 ](./doc/screenshots/oauth-utils-ms-grant_2.png) 

#### Create client secret
* On the left-hand side under `Manage`, select `Certificate and secrets`.
* Click `New client secret`.
* Enter a name for the client secret.
  ![screenshot: oauth-utils-ms-sec ](./doc/screenshots/oauth-utils-ms-sec.png) 
  
  ![screenshot: oauth-utils-ms-sec_2 ](./doc/screenshots/oauth-utils-ms-sec_2.png) 

  ![screenshot: oauth-utils-ms-sec_3 ](./doc/screenshots/oauth-utils-ms-sec_3.png) 

* Save the secret `Value` locally. This will be used as the value for the `client_secret` setting/argument.

#### Authenticated SMTP
* Log in to [Microsoft 365 admin center](https://admin.microsoft.com) as an admin user and go to `Users` > `Active users`.
* Select the SMTP user, and click `Mail`.
* In the Email apps section, click Manage email apps.
* Verify the `Authenticated SMTP` setting is checked.
* Click `Save changes`.
  
  ![screenshot: oauth-utils-ms-admin-smtp ](./doc/screenshots/oauth-utils-ms-admin-smtp.png)

You can now add credentials and scope obtained above to an app.config file or alternatively use as command line arguments for the `oauth2_generate_refresh_token` utility.

```
client_id=1c22e8d1-daf0-407e-b576-0778cc3cd812
client_secret=OT48Q~enmvy5HpCpub2maQxCVdhvEgowkT1WBbGc
scope=offline_access https://outlook.office365.com/SMTP.Send
token_url=https://login.microsoftonline.com/c06fa6c3-5dd0-48c9-9a4b-7edbf1904269/oauth2/v2.0/token
auth_url=https://login.microsoftonline.com/c06fa6c3-5dd0-48c9-9a4b-7edbf1904269/oauth2/v2.0/authorize
```
* Using the browser mode option, execute the `oauth2_generate_refresh_token` utility using the new credentials in the app.config file.
```
$ oauth-utils oauth2_generate_refresh_token -b
Running with callback listener and web browser.
Reading OAuth2 settings from app.config file /Users/johnpren/.resilient/app.config.
/Users/johnpren/ws/venv_3.6.8_oauth-utils/lib/python3.6/site-packages/werkzeug/serving.py:469: CryptographyDeprecationWarning: Python 3.6 is no longer supported by the Python core team. Therefore, support for it is deprecated in cryptography and will be removed in a future release.
  from cryptography import x509
Starting callback listener on port 8080.
Starting browser.
```
A web browser is launched, and the rest of the process will be completed using the browser.

* In the browser, sign in as the SMTP email user.

 ![screenshot: oauth-utils-ms-brow-sign-in ](./doc/screenshots/oauth-utils-ms-brow-sign-in.png)

* Follow the directions by clicking `Accept`.

 ![screenshot: oauth-utils-ms-brow-accept ](./doc/screenshots/oauth-utils-ms-brow-accept.png)

* The browser is redirected to the callback URL (default port 8080) and will be processed by a local listener.

* If you are satisfied that it is redirected to the correct location, click `Accept the Risk and Continue`.

 ![screenshot: oauth-utils-ms-brow-accept-risk ](./doc/screenshots/oauth-utils-ms-brow-accept-risk.png)

A refresh token is displayed in the browser.

 ![screenshot: oauth-utils-ms-brow-refresh-tok ](./doc/screenshots/oauth-utils-ms-brow-refresh-tok.png)

* Add the resultant `refresh_token` to the app.config file for the required app.

See: [Using OAuth 2.0 with Microsoft for Office 365 users](https://docs.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth)

---

## Troubleshooting & Support
Refer to the documentation listed in the Requirements section for troubleshooting information.

### For Support
This is a IBM Community provided package. Please search the Community [ibm.biz/soarcommunity](https://ibm.biz/soarcommunity) for assistance.
