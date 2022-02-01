# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2022. All Rights Reserved.

"""
    Script to upload, install, and deploy a zip file to app host
    Takes 3 parameters:
        1: ZIP_PATH
        2: CONFIG_PATH
        3: PACKAGE_NAME
"""

import json
import os
import sys
import time
import re
import resilient
from resilient.co3base import BasicHTTPException, ensure_unicode

if len(sys.argv) != 4:
    sys.exit()

ZIP_PATH = sys.argv[1]
CONFIG_PATH = sys.argv[2]
PACKAGE_NAME = sys.argv[3]

CONFIG_FILE = f'/home/travis/build/Resilient/{PACKAGE_NAME}.config'
DEPLOYMENT_CUTOFF_SECONDS = 10*60

def main():
    """runs all the necessary functions"""
    res_client = setup()

    if res_client is None:
        print("******************* FAILURE! Wasn't able to connect to SOAR! *******************")
        sys.exit()

    upload_all_apps(res_client, app_path=ZIP_PATH)
    install_all_apps(res_client)
    deploy_all_apps(res_client)
    upload_all_app_configurations(res_client)

########################################
### basic setup + helper functions
########################################
def setup():
    """sets up and returns our SOAR client"""

    soar_config_file = f'{CONFIG_PATH}/app.config'

    if not os.path.exists(soar_config_file):
        print("The app.config with the SOAR credentials is missing. Exiting now")
        sys.exit()

    resilient_parser = resilient.ArgumentParser(config_file=soar_config_file)
    opts = resilient_parser.parse_known_args()[0]

   # removes the brackets from the app config to get the Travis env variable values
    results = {}
    for item in ["email", "password", "api_key_id", "api_key_secret", "host"]:
        if item in opts.keys() and opts[item] is not None:
            results[item] = re.sub(r"[{}]", "", opts[item]).strip()
            results[item] = os.environ.get(results[item])

    if "org" in opts.keys():
        org = opts["org"]
    if "cafile" in opts.keys():
        cafile = opts["cafile"]

    verify = True
    if cafile is not None and cafile == "false":
        verify = False

    # 443 is the default ssl port
    port = opts["port"] if opts.get("port") else 443

    url = f'https://{results["host"]}:{port}'


    login_args = {
            "base_url": url,
            "verify": verify,
            "org_name": org
            }

    res_client = resilient.SimpleClient(**login_args)

    # we will need platform information further down (to select platform specific URLs)
    # and prevent the "/apps" API endpoint from being called (since it is not accessible)
    res_client.platform = "SOAR"

    if results["email"] and results["password"]:
        session = res_client.connect(results["email"], results["password"])
    elif results["api_key_id"] and results["api_key_secret"]:
        session = res_client.set_api_key(api_key_id=results["api_key_id"],
                                        api_key_secret=results["api_key_secret"])
    else:
        print("Neither email/password nor API key id/secret was supplied!")
        print("Provide via app.config. Aborting!")
        return None

    set_tenant_id(res_client,session)
    return res_client

# helper method for setting the tenant id. session_info is the return of the /session API endpoint
def set_tenant_id(res_client, session_info):
    """The session info contains all organizations the user is a member of
    The res_client has a field, which specifies the ID of the
    chosen organization, so we can extract the correct one.
    After that, we can choose the correct tenant_id
    (TenantID == UUID of choosen organization)"""
    for org in session_info["orgs"]:
        if res_client.org_id == org["id"]:
            res_client.tenant_id = org["uuid"]

    res_client.session_return = session_info
    if res_client.tenant_id is None:
        print("Tenant ID was not extracted")


def base_get(res_client, uri, co3_context_token=None, timeout=None):
    """helper method to initiate GET requests to the Resilient servers.
    this is needed, because the standard get method goes to
    https://{url}/rest/orgs/{orgID}
    but we sometimes need to go just to the url + something"""
    if res_client is None:
        return "No res_client supplied!"

    url = f'{res_client.base_url}{ensure_unicode(uri)}'

    response = res_client._execute_request(res_client.session.get,
                                            url,
                                            proxies=res_client.proxies,
                                            cookies=res_client.cookies,
                                            headers=res_client.make_headers(co3_context_token,{"X-ORG-ID": f'{res_client.org_id}'}),
                                            verify=res_client.verify,
                                            timeout=timeout)
    BasicHTTPException.raise_if_error(response)
    return json.loads(response.content)


def base_put(res_client, uri, payload, co3_context_token=None, timeout=None):
    """helper method to initiate PUT requests to the Resilient servers
    this is needed, because the standard put method goes to
    https://{url}/rest/orgs/{orgID}
    but we sometimes need to go just to the url + something"""
    if res_client is None:
        return "No res_client supplied!"

    url = f'{res_client.base_url}{ensure_unicode(uri)}'

    payload_json = json.dumps(payload)
    response = res_client._execute_request(res_client.session.put,
                                            url,
                                            data=payload_json,
                                            proxies=res_client.proxies,
                                            cookies=res_client.cookies,
                                            headers=res_client.make_headers(co3_context_token,{"X-ORG-ID": f'{res_client.org_id}'}),
                                            verify=res_client.verify,
                                            timeout=timeout)
    BasicHTTPException.raise_if_error(response)
    return json.loads(response.text)


def base_post(res_client, uri, payload, co3_context_token=None, timeout=None):
    """helper method to initiate POST requests to the Resilient servers
    this is needed, because the standard post method goes to
    https://{url}/rest/orgs/{orgID}
    but we sometimes need to go just to the url + something"""
    if res_client is None:
        return "No res_client supplied!"

    url = f'{res_client.base_url}{ensure_unicode(uri)}'

    payload_json = json.dumps(payload)
    response = res_client._execute_request(res_client.session.post,
                                            url,
                                            data=payload_json,
                                            proxies=res_client.proxies,
                                            cookies=res_client.cookies,
                                            headers=res_client.make_headers(co3_context_token,{"X-ORG-ID": f'{res_client.org_id}'}),
                                            verify=res_client.verify,
                                            timeout=timeout)
    BasicHTTPException.raise_if_error(response)
    return json.loads(response.text)

########################################
### upload, install and deploy apps
########################################
def upload_all_apps(res_client, app_path):
    """uploads the zip file to apphost"""

    if app_path is None:
        print("Problem getting the app file path.")
        return

    if res_client.use_api_key is True:
        print("The client is authenticated via API keys. The requested function uses the '/apps' API endpoint, which is not enabled with this authentication method!")
        return

    apps = res_client.get("/apps")
    installed_app_names = []
    for app in apps["entities"]:
        installed_app_names.append(app["name"])

    # app downloaded from the X-Force Exchange have the following naming convention:
    # app-#NAME#-#VERSION#.zip e.g.: app-fn_outbound_email-1.1.0.zip
    # we try to extract the #NAME# and check if this app is already installed.
    # If we don't succeed, the upload will softfail later with a bad request.
    parts = app_path.split("-")
    # if there are more than 3 elements in parts, the app name includes hyphens
    # we therefore concat all but the first and the last element
    if len(parts)>=3:
        extracted_name = "-".join(parts[1:-1])
    elif len(parts)<3:
        # the file name contains less than 2 hyphens, just continue
        extracted_name = ""

    if extracted_name in installed_app_names:
        print(f'The app {extracted_name} is already uploaded!')

    print(f'Begin upload: {app_path}')

    try:
        app = res_client.post_attachment(uri="/apps", filepath=app_path)
    except resilient.co3.SimpleHTTPException as exception:
        print(exception)

def install_all_apps(res_client):
    """installs pending uploaded app to apphost"""

    if res_client.use_api_key is True:
        print("The client is authenticated via API keys. The requested function uses the '/apps' API endpoint, which is not enabled with this authentication method!")
        return
    apps = res_client.get("/apps")

    for app in apps["entities"]:
        # check if app is in 'pending' state and extract all values needed for installation
        if app["current_installation"]["status"] == 'pending':
            print(f'Begin installation: {app["name"]}')

            app_handle = app["id"]
            installation_id = app["current_installation"]["id"]

            # set status to installing, this triggers installation
            app["current_installation"]["status"] = 'installing'

            # type(r) == AppInstallationDTO
            res = res_client.put(uri=f'/apps/{app_handle}/installations/{installation_id}',
                                 payload = app["current_installation"])


            # check result
            if res["status"] == 'installed':
                print(f'Installation successfull: {app["name"]}')
            else:
                print(f'Error in installation: {app["name"]}')
                print(res)

def deploy_all_apps(res_client, controller_id=None):
    """deploys app in apphost"""

    if res_client.use_api_key is True:
        print("The client is authenticated via API keys. The requested function uses the '/apps' API endpoint, which is not enabled with this authentication method!")
        return

    controller_found = False
    controllers = base_get(res_client, f'/services_proxy/manager/tenants/{res_client.tenant_id}/controllers')

    # if no controller_id is supplied, pick the first running controller
    if controller_id is None:
        for controller in controllers["controllers"]:
            if controller["status"] == "paired":
                controller_id = controller["id"]
                controller_found = True
                break

        # No paired controller found
        if not controller_found:
            print("There is no paired controller!\nPlease set up an AppHost!\n")
            return
    else:
        # it is easier to supply the controller host name
        # we have to check what was supplied, and then search for the correct ID

        for controller in controllers["controllers"]:
            # supplied id was found and runnning
            if controller["id"] == controller_id and controller["status"] == "paired":
                controller_found = True
                break

            # the supplied id was actually the name and it is running
            if controller["name"] == controller_id and controller["status"] == "paired":
                controller_id = controller["id"]
                controller_found = True
                break

    if not controller_found:
        print(f'The supplied controller_id {controller_id} could not be resolved to a paired AppHost!')
        print("Exiting...")
        return

    apps = res_client.get("/apps")

    # we gather the list of apps that will be deployed, so we can keep track of their status
    deployment_list = []

    for app in apps["entities"]:
        app_id = app["current_installation"]["executables"][0]["uuid"]
        name = app["current_installation"]["executables"][0]["name"]

        app_information = base_get(res_client, f'/services_proxy/manager/tenants/{res_client.tenant_id}/apps/{name}')

        if "deployment" not in app_information:
            deploy_body = app_information

            deployment = {
                "controller_id" : controller_id,
                "status" : "deploying"
            }

            deploy_body["deployment"] = deployment

            deployment_list.append(name)

            print(f'Deployement started: {name}')

            base_put(res_client,uri= f'/services_proxy/manager/apps/{app_id}',
                     payload = deploy_body)

    # we now have set all apps to the deployment state, track their deployment status
    track_deployment(res_client, deployment_list)

def track_deployment(res_client, deployment_list):
    """tracks the deployment of the app
    default cutoff time for is 10 minutes
    other values can be supplied via the "--deployment_cutoff_seconds" argument"""
    deployment_cutoff_seconds = DEPLOYMENT_CUTOFF_SECONDS

    # if args.deployment_cutoff_seconds is not None:
    #     deployment_cutoff_seconds = args.deployment_cutoff_seconds

    deployment_status = {}
    print("Started deployment of the following apps:", deployment_list)
    start_time = time.time()
    while len(deployment_list) > 0:
        for name in deployment_list:

            res = base_get(res_client, f'/services_proxy/manager/tenants/{res_client.tenant_id}/apps/{name}')

            deployment_status[name] = res["deployment"]["status"]

            if deployment_status[name] == "ready":
                deployment_list.remove(name)

        # wait period between app installation status checks
        time.sleep(2)

        if time.time()-start_time > deployment_cutoff_seconds:
            print("Cutoff time was reached! Deployment may still be going on, please check in the GUI.")
            break

    print(f'This operation was running for {time.time()-start_time:.2f} seconds.')
    if len(deployment_list) > 0:
        print("The deployment of the following apps was not completed in time:", deployment_list)
    else:
        print("******************* SUCCESS! The app was deployed! *******************")

########################################
### set config files for apps
########################################

def upload_all_app_configurations(res_client):
    """Uploads  and fills out the app config"""
    if res_client.use_api_key is True:
        print("The client is authenticated via API keys. The requested function uses the '/apps' API endpoint, which is not enabled with this authentication method!")
        return
    config_dict = {}

    if not os.path.exists(CONFIG_FILE):
        print("The app.config with the integration information is missing. The app has been deployed but the app.config is not filled out in SOAR. Exiting now.")
        sys.exit()

    with open(CONFIG_FILE, encoding="utf-8") as file:
        config_dict[PACKAGE_NAME] = file.read()

    # get all installment IDs
    apps = res_client.get("/apps")
    changed_apps = []

    for app in apps["entities"]:
        name = app["current_installation"]["executables"][0]["name"]

        if name in config_dict:
            app_installment = base_get(res_client, f'/services_proxy/manager/tenants/{res_client.tenant_id}/apps/{name}')

            # we only want to upload configurations to already deployed apps!
            if "deployment" not in app_installment:
                print(f'{name} is not yet deployed, we will not upload the configuration!')
                continue

            # Add app name to list, that will be tracked for deployment status
            changed_apps.append(name)

            # gather list of files for every installment
            # and then look for "app.config"
            file_ids = app_installment["file_ids"]

            for file_id in file_ids:
                service_proxy_url = f'/services_proxy/manager/app_files/{file_id}'
                file = base_get(res_client, service_proxy_url)

                if file["name"] == "app.config":
                    # fill out app.config while retaining the Resilient variables
                    content_string = file["content"]
                    substring = content_string.find("[resilient]")
                    end_substring = content_string.find("cafile")
                    final_string = f'\n{content_string[substring:end_substring]}cafile=false\n'
                    substring = content_string.find("host")
                    final_string = f'{final_string}{content_string[substring:]}'
                    config_dict[name] = config_dict[name] + final_string

                    file["content"] = config_dict[name]

                    base_put(res_client, uri=service_proxy_url, payload=file)
                    print("*******************SUCCESS! The app.config was filled out! *******************")
                    break
    track_deployment(res_client, changed_apps)

if __name__ == "__main__":
    main()
