import base64
import requests

# class AtdHelper():

    # def __init__(self, atd_url, resilient_url):
    #     self.atd_url = atd_url
    #     self.resilient_url = resilient_url

def getSessionATD(username, password, atd_url):
    login_string = "{}:{}".format(username, password)
    base64_login = base64.b64encode(login_string)
    session_url = atd_url + "/php/session.php"

    headers = {
        "Accept": "application/vnd.ve.v1.0+json",
        "Content-Type": "application/json",
        "VE-SDK-API": base64_login
    }
    r = requests.get(session_url, headers=headers, verify=False)

    return r
