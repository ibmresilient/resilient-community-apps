"""
objective: this is a user-prompted tool to query scripts, workflows and playbooks to detect python2
pre-requisites:
    - python v3.6+ with the following python packages installed: resilient, requests, getpass
    - API key will permissions to read scripts, workflows and playbooks
usage:
    - python <name of this file>.py "https://<host>" "<org>" "<API key ID>"

"""
install_failures = False
try:
    from resilient import SimpleClient
except:
    print("install 'resilient' python package")
    install_failures = True
try:
    import requests
except:
    print("install 'requests' python package")
    install_failures = True

from getpass import getpass
import sys

if install_failures:
    exit(1)

# turn off warnings about certs
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def query_scripts(client):
    """list scripts by id, name, programmatic_name"""
    print("Querying for Python2 Scripts")
    script_json = client.get('/scripts')['entities']

    script_list = []

    for script in script_json:
        if script['language'] == "python":
            script_list.append(script)
    return script_list


def query_workflows(client):
    """list workflow by id, name, programmatic_name"""
    print("Querying for Python2 Workflows")
    definite_workflow = []
    potential_workflow = []
    workflow_json = client.get('/workflows')['entities']

    for workflow in workflow_json:
        xml = workflow['content']['xml']
        # If "python" is in xml then python 2
        if '"python"' in xml:
            definite_workflow.append(workflow)
        # else if there are processing scripts without language set, its likely python 2
        elif ((('"pre_processing_script":"' in xml) and ("pre_processing_script_language" not in xml)) or
              (('"post_processing_script":"' in xml) and ("post_processing_script_language" not in xml))):
            potential_workflow.append(workflow)
    return [definite_workflow, potential_workflow]


def query_playbooks(client):
    """list workflow by id, name, programmatic_name"""
    print("Querying for Python2 Playbooks")
    playbooks = []
    playbook_json = client.post('/playbooks/query_paged?return_level=full', {})['data']

    for playbook in playbook_json:
        if 'content' in playbook:
            if '"python"' in playbook['content']['xml']:
                playbooks.append(playbook)

    return playbooks


def printResults(scripts=None, workflows_definite=None, workflows_propable=None, playbooks=None):
    if scripts:
        print("Scripts Using Python 2")
        for script in scripts:
            print("Script ID: {}, name: {}".format(script["id"], script["name"]))
        print("total # of scripts using Python 2 = ", len(scripts))
        print("\n\n")

    if workflows_definite or workflows_propable:
        print("Workflows currently using Python 2")
        for workflow in workflows_definite:
            print("Workflow ID: {}, name: {}".format(workflow["workflow_id"], workflow["name"]))
        print("Total # of workflows currently using Python 2 = ", len(workflows_definite))
        print("\n\n")


        print("Workflows could be using Python 2")
        for workflow in workflows_propable:
            print("Workflow ID: {}, name: {}".format(workflow["workflow_id"], workflow["name"]))
        print("Total # of workflows could be using Python 2 = ", len(workflows_propable))
        print("\n\n")



    if playbooks:
        print("Playbooks Using Python 2")
        for playbook in playbooks:
            print("{} ID: {}, name: {}".format("Subplaybook" if playbook["type"] == "subplaybook" else "Playbook",
                                               playbook["id"], playbook["display_name"]))
        print("Total # of playbooks using Python 2 = ", len(playbooks))
        print("\n\n")



def main(argv):
    if (len(argv) != 4):
        print('Incorrect number of arguments')
        print('Usage: "https://<host>" "<org>" "<API key ID>" ')
        return

    base_url = argv[1]
    org = argv[2]
    user = argv[3]


    pwd = getpass("Please enter the API Key Secret for {} {}: ".format('API Key', user))

    client = SimpleClient(base_url=base_url, org_name=org, verify=False)



    client.set_api_key(user, pwd)

    print("*** Welcome! This script will query SOAR scripts, workflows and playbooks and report on those using Python2.")
    print("1) query scripts")
    print("2) query workflows")
    print("3) query playbooks")
    print("4) query all")
    action = str(input("enter desired action: "))
    if action == "1":
        printResults(scripts=query_scripts(client))
    elif action == "2":
        [definite_workflows, potential_workflows] = query_workflows(client)
        printResults(workflows_definite=definite_workflows, workflows_propable=potential_workflows)
    elif action == "3":
        printResults(playbooks=query_playbooks(client))
    else:
        scripts = query_scripts(client)
        [definite_workflows, potential_workflows] = query_workflows(client)
        playbooks = query_playbooks(client)

        printResults(scripts, definite_workflows, potential_workflows, playbooks)


if __name__ == "__main__":
    main(sys.argv)