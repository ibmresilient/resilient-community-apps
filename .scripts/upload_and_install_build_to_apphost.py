import resilient
import json
import os,sys
import time
from requests_toolbelt import MultipartEncoder
from resilient.co3base import BasicHTTPException, ensure_unicode

ZIP_PATH = sys.argv[1]
CONFIG_PATH = sys.argv[2]
PACKAGE_NAME = sys.argv[3]

def main():
    res_client = setup()
    
    if res_client is None:
        print("FAILURE!")
        sys.exit()

    upload_all_apps(res_client, app_path=ZIP_PATH)
    install_all_apps(res_client)
    deploy_all_apps(res_client)
    upload_all_app_configurations(res_client)
    
    os.remove('{}/complete_app.config'.format(CONFIG_PATH))

########################################
### basic setup + helper functions
########################################            
#  sets up and returns our SOAR client

def setup():
    soar_config_file = '{}/app.config'.format(CONFIG_PATH)
    integration_config_file = '/home/travis/build/Resilient/{}.config'.format(PACKAGE_NAME)

    if not os.path.exists(soar_config_file):
        print("The app.config with the SOAR credentials is missing. Exiting now")
        sys.exit()

    if not os.path.exists(integration_config_file):
        print("The app.config with the integration information is missing. Exiting now")
        sys.exit()

    config_file_path='{}/complete_app.config'.format(CONFIG_PATH)

    # combines the two app configs into a complete usable one
    filenames = [integration_config_file, soar_config_file]
    with open(config_file_path, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                outfile.write(infile.read())
            outfile.write("\n")

    resilient_parser = resilient.ArgumentParser(config_file=config_file_path)
    opts = resilient_parser.parse_known_args()[0]

    # creates variables for the opts.keys()
    # check to see if we are using env variables and change the format to be usable here
    if "email" in opts.keys():
        email = opts["email"]
        if email[:2] == "{{" and email[-2:] == "}}":
            email = email.replace("{", "")
            email = email.replace("}", "") 
            email = os.environ.get(email)
    if "password" in opts.keys():
        password = opts["password"]
        if password[:2] == "{{" and password[-2:] == "}}":
            password = password.replace("{", "")
            password = password.replace("}", "") 
            password = os.environ.get(password)
    if "api_key_id" in opts.keys():
        if opts["api_key_id"] is not None: 
            api_key_id = opts["api_key_id"]
            if api_key_id[:2] == "{{" and api_key_id[-2:] == "}}":
                api_key_id = api_key_id.replace("{", "")
                api_key_id = api_key_id.replace("}", "") 
                api_key_id = os.environ.get(api_key_id)
        else:
            api_key_id = None
    if "api_key_secret" in opts.keys(): 
        if opts["api_key_secret"] is not None:
            api_key_secret = opts["api_key_secret"]
            if api_key_secret[:2] == "{{" and api_key_secret[-2:] == "}}":
                api_key_secret = api_key_secret.replace("{", "")
                api_key_secret = api_key_secret.replace("}", "") 
                api_key_secret = os.environ.get(api_key_secret) 
        else:
            api_key_secret = None
    if "host" in opts.keys():
        host = opts["host"]
        if host[:2] == "{{" and host[-2:] == "}}":
            host = host.replace("{", "")
            host = host.replace("}", "") 
            host = os.environ.get(host) 
    if "org" in opts.keys():
        org = opts["org"]
    if "cafile" in opts.keys():
        cafile = opts["cafile"]

    verify = True
    if cafile is not None and cafile == "false":
        verify = False

    if "port" in opts.keys():
        port = opts["port"]
    else:
        # default ssl port
        port = 443
    url = "https://{}:{}".format(host,port)


    login_args = {"base_url": url,
            "verify": verify,
            "org_name": org}

    res_client = resilient.SimpleClient(**login_args)
    
    # we will need platform information further down (to select platform specific URLs) 
    # and prevent the "/apps" API endpoint from being called (since it is not accessible)
    res_client.platform = "SOAR"

    if email is not None and password is not None:
        session = res_client.connect(email, password)
    elif api_key_id is not None and api_key_secret is not None:
        session = res_client.set_api_key(api_key_id=opts["api_key_id"], 
                                        api_key_secret=opts["api_key_secret"])
    else: 
        print("Neither email/password nor API key id/secret was supplied!")
        print("Provide via app.config. Aborting!")
        return None

    set_tenant_id(res_client,session)
    return res_client

# helper method for setting the tenant id. session_info is the return of the /session API endpoint
def set_tenant_id(res_client, session_info):
    # The session info contains all organizations the user is a member of
    # The res_client has a field, which specifies the ID of the
    # chosen organization, so we can extract the correct one.
    # After that, we can choose the correct tenant_id
    # (TenantID == UUID of choosen organization)
    for org in session_info["orgs"]:
        if res_client.org_id == org["id"]:
            res_client.tenant_id = org["uuid"]

    res_client.session_return = session_info
    if res_client.tenant_id is None:
        print("Tenant ID was not extracted")

# helper method to initiate GET requests to the Resilient servers.
# this is needed, because the standard get method goes to
# https://{url}/rest/orgs/{orgID}
# but we sometimes need to go just to the url + something
def base_get(res_client, uri, co3_context_token=None, timeout=None):
    if res_client is None:
        return "No res_client supplied!"

    url = u"{0}{1}".format(res_client.base_url, ensure_unicode(uri))

    response = res_client._execute_request(res_client.session.get,
                                        url,
                                        proxies=res_client.proxies,
                                        cookies=res_client.cookies,
                                        headers=res_client.make_headers(co3_context_token,{"X-ORG-ID": "{}".format(res_client.org_id)   }),
                                        verify=res_client.verify,
                                        timeout=timeout)
    BasicHTTPException.raise_if_error(response)
    return json.loads(response.content)

# helper method to initiate PUT requests to the Resilient servers
# this is needed, because the standard get method goes to
# https://{url}/rest/orgs/{orgID}
# but we sometimes need to go just to the url + something
def base_put(res_client, uri, payload, co3_context_token=None, timeout=None):
    if res_client is None:
        return "No res_client supplied!"

    
    url = u"{0}{1}".format(res_client.base_url, ensure_unicode(uri))
    
    payload_json = json.dumps(payload)
    response = res_client._execute_request(res_client.session.put,
                                        url,
                                        data=payload_json,
                                        proxies=res_client.proxies,
                                        cookies=res_client.cookies,
                                        headers=res_client.make_headers(co3_context_token,{"X-ORG-ID": "{}".format(res_client.org_id)   }),
                                        verify=res_client.verify,
                                        timeout=timeout)
    BasicHTTPException.raise_if_error(response)
    return json.loads(response.text)   

# helper method to initiate POST requests to the Resilient servers
# this is needed, because the standard get method goes to
# https://{url}/rest/orgs/{orgID}
# but we sometimes need to go just to the url + something
def base_post(res_client, uri, payload, co3_context_token=None, timeout=None):
    if res_client is None:
        return "No res_client supplied!"
    
    url = u"{0}{1}".format(res_client.base_url, ensure_unicode(uri))

    payload_json = json.dumps(payload)
    response = res_client._execute_request(res_client.session.post,
                                        url,
                                        data=payload_json,
                                        proxies=res_client.proxies,
                                        cookies=res_client.cookies,
                                        headers=res_client.make_headers(co3_context_token,{"X-ORG-ID": "{}".format(res_client.org_id)   }),
                                        verify=res_client.verify,
                                        timeout=timeout)
    BasicHTTPException.raise_if_error(response)
    return json.loads(response.text)     

# For some officially unsupported API calls we have to upload XML files
# The server expects multipart encoded data, therefore we have to package
# it ourselves. 
def base_put_multipart_xml(res_client, uri, payload, co3_context_token=None, timeout=None):
    workflow_fields = {}
    workflow_fields["csrf"] = res_client.headers["X-sess-id"]
    workflow_fields["file"] = payload
    # Not sure what this does, this may be changed later
    workflow_fields["object_type"] = '0'

    encoder = MultipartEncoder(fields=workflow_fields)

    url = u"{0}{1}".format(res_client.base_url, ensure_unicode(uri))

    headers = res_client.make_headers(co3_context_token,
                                additional_headers={'content-type': encoder.content_type, "X-ORG-ID": "{}".format(res_client.org_id) })

    response = res_client._execute_request(res_client.session.put,
                                        url,
                                        data=encoder,
                                        proxies=res_client.proxies,
                                        cookies=res_client.cookies,
                                        headers=headers,
                                        verify=res_client.verify,
                                        timeout=timeout)
    BasicHTTPException.raise_if_error(response)
    return json.loads(response.text)

# For some officially unsupported API calls we have to upload XML files
# The server expects multipart encoded data, therefore we have to package
# it ourselves. 
def base_post_export_config(res_client, uri, co3_context_token=None, timeout=None):
    fields = {}
    fields["csrf"] = res_client.headers["X-sess-id"]

    encoder = MultipartEncoder(fields=fields)

    url = u"{0}{1}".format(res_client.base_url, ensure_unicode(uri))

    headers = res_client.make_headers(co3_context_token,
                                additional_headers={'content-type': encoder.content_type, "X-ORG-ID": "{}".format(res_client.org_id) })

    response = res_client._execute_request(res_client.session.post,
                                        url,
                                        data=encoder,
                                        proxies=res_client.proxies,
                                        cookies=res_client.cookies,
                                        headers=headers,
                                        verify=res_client.verify,
                                        timeout=timeout)
    BasicHTTPException.raise_if_error(response)

    return response

########################################
### create the secret information for 
### AppHost setup
########################################
# Not curently used since we are using one designated app host and SOAR

def create_AppHost_pairing(res_client,appHost_name="new Host", appHost_description= "new Description", toFile = None):
    payload = {}
    payload["tenant_id"] = res_client.tenant_id
    payload["name"] = appHost_name
    payload["description"] = {"format": "text", "content": appHost_description}

    r = base_post(res_client = res_client, uri = "/services_proxy/manager/controllers", payload = payload)
    

    # for consistency with clipboard information in the GUI remove some items
    r.pop("status")
    r.pop("version")

    clipboard_information = {}

    # base url includes the port number, we remove it for consistency with clipboard information in the GUI
    base_url_parts = res_client.base_url.split(":")
    base_url_without_port = ":".join(base_url_parts[:-1]) + "/services_proxy/manager"

    clipboard_information["manager_url"] = base_url_without_port
    clipboard_information["controller"] = r

    if toFile:
        with open(toFile,"w") as f:
            f.write(json.dumps(clipboard_information, indent= 4))
    else: 
        print(json.dumps(clipboard_information))

########################################
### upload, install and deploy apps
########################################
def upload_all_apps(res_client, app_path):
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
        print("The app {} is already uploaded!".format(extracted_name))

    print("Begin upload: {}".format(app_path))

    try: 
        app = res_client.post_attachment(uri="/apps", filepath=app_path)           
    except resilient.co3.SimpleHTTPException as e:
        print(e)

def install_all_apps(res_client):
    if res_client.use_api_key is True:
        print("The client is authenticated via API keys. The requested function uses the '/apps' API endpoint, which is not enabled with this authentication method!")
        return
    apps = res_client.get("/apps")

    for app in apps["entities"]:
        # check if app is in 'pending' state and extract all values needed for installation
        if app["current_installation"]["status"] == 'pending':
            print("Begin installation: {}".format(app["name"]))

            app_handle = app["id"]
            installation_ID = app["current_installation"]["id"]
            
            # set status to installing, this triggers installation
            app["current_installation"]["status"] = 'installing'

            # type(r) == AppInstallationDTO
            r = res_client.put(uri="/apps/{}/installations/{}".format(app_handle,installation_ID),
                                payload = app["current_installation"])
            

            # check result
            if r["status"] == 'installed':
                print("Installation successfull: {}".format(app["name"]))
            else:
                print("Error in installation: {}".format(app["name"]))
                print(r)

def deploy_all_apps(res_client, controller_id=None):
    if res_client.use_api_key is True:
        print("The client is authenticated via API keys. The requested function uses the '/apps' API endpoint, which is not enabled with this authentication method!")
        return

    controller_found = False

    
    controllers = base_get(res_client, "/services_proxy/manager/tenants/{}/controllers".format(res_client.tenant_id))
    
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
        print("The supplied controller_id {} could not be resolved to a paired AppHost!".format(controller_id))
        print("Exiting...")
        return

    apps = res_client.get("/apps")

    # we gather the list of apps that will be deployed, so we can keep track of their status
    deployment_list = []

    for app in apps["entities"]:
        
        id = app["current_installation"]["executables"][0]["uuid"]
        name = app["current_installation"]["executables"][0]["name"]

        app_information = base_get(res_client,"/services_proxy/manager/tenants/{}/apps/{}".format(res_client.tenant_id,name))

        if "deployment" not in app_information:           
            deploy_body = app_information

            deployment = {
                "controller_id" : controller_id,
                "status" : "deploying"
            }

            deploy_body["deployment"] = deployment

            deployment_list.append(name)

            print("Deployement started: {}".format(name))

            base_put(res_client,uri= "/services_proxy/manager/apps/{0}".format(id),
                                    payload = deploy_body)
            
    # we now have set all apps to the deployment state, track their deployment status
    track_deployment(res_client, deployment_list)


def track_deployment(res_client, deployment_list):
    # default cutoff time for is 10 minutes
    # other values can be supplied via the "--deployment_cutoff_seconds" argument
    deployment_cutoff_seconds = 10*60

    # if args.deployment_cutoff_seconds is not None:
    #     deployment_cutoff_seconds = args.deployment_cutoff_seconds

    deployment_status = {}
    print("Started deployment of the following apps:", deployment_list)
    start_time = time.time()
    while (len(deployment_list)>0):
        for name in deployment_list:

            
            r = base_get(res_client,"/services_proxy/manager/tenants/{}/apps/{}".format(res_client.tenant_id,name))
            
            deployment_status[name] = r["deployment"]["status"]

            if deployment_status[name] == "ready":
                deployment_list.remove(name)

        # wait period between app installation status checks
        time.sleep(2)

        if time.time()-start_time > deployment_cutoff_seconds:
            print("Cufoff time was reached! Deployment may still be going on, please check in the GUI.")
            break

    print("This operation was running for {:.2f} seconds.".format(time.time()-start_time))
    if len(deployment_list) > 0: 
        print("The deployment of the following apps was not completed in time:", deployment_list)
    else:
        print("SUCCESS!")

########################################
### set config files for apps
########################################

def upload_all_app_configurations(res_client, config_dir = CONFIG_PATH):
    if res_client.use_api_key is True:
        print("The client is authenticated via API keys. The requested function uses the '/apps' API endpoint, which is not enabled with this authentication method!")
        return
    config_dict = {}
    
    # collect files to upload
    
    if not config_dir.endswith("/"):
        config_dir = config_dir + "/"
    config_file = '{}/complete_app.config'.format(CONFIG_PATH)

    with open(config_file) as f:
        config_string = f.read()
        app_name = PACKAGE_NAME
        config_dict[app_name] = config_string

    print("We have found the following configuration files:")
    print(json.dumps(config_dict, indent=4))

    # get all installment IDs
    apps = res_client.get("/apps")
    changed_apps = []

    for app in apps["entities"]:
        name = app["current_installation"]["executables"][0]["name"]

        if name in config_dict:
            app_installment = base_get(res_client, "/services_proxy/manager/tenants/{}/apps/{}".format(res_client.tenant_id,name))
            
            # we only want to upload configurations to already deployed apps!
            if "deployment" not in app_installment:
                print("{} is not yet deployed, we will not upload the configuration!".format(name))
                continue

            # Add app name to list, that will be tracked for deployment status
            changed_apps.append(name)

            # gather list of files for every installment
            # and then look for "app.config"
            file_ids = app_installment["file_ids"]

            for file_id in file_ids:
                f = base_get(res_client, "/services_proxy/manager/app_files/{}".format(file_id))
                
                if f["name"] != "app.config":
                    continue
                else:
                    f["content"] = config_dict[name]

                    base_put(res_client, uri="/services_proxy/manager/app_files/{}".format(file_id),
                                            payload=f)
                    break
    track_deployment(res_client, changed_apps)

if __name__ == "__main__":
    main()
    