# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import re
from bs4 import BeautifulSoup
from six import string_types
import resilient
from .errors import IntegrationError
try:
    import HTMLParser as htmlparser
except:
    import html.parser as htmlparser

resilient_client = None
connection_opts = None

INCIDENT_FRAGMENT = '#incidents'

def build_incident_url(url, incidentId):
    """
    build the url to link to an resilient incident
    :param url: base url
    :param incidentId:
    :return: full url
    """
    return '/'.join([url, INCIDENT_FRAGMENT, str(incidentId)])

def build_resilient_url(host, port):
    """
    build basic url to resilient instance
    :param host: host name
    :param port: port
    :return: base url
    """
    return "https://{0}:{1}".format(host, port)

def clean_html(htmlFragment):
    """
    Resilient textarea fields return html fragments. This routine will remove the html and insert any code within <div></div>
    with a linefeed
    :param htmlFragment:
    :return: cleaned up code
    """

    if not htmlFragment or not isinstance(htmlFragment, string_types):
        return htmlFragment

    return BeautifulSoup(unescape(htmlFragment), "html.parser").text

def unescape(data):
    """ Return unescaped data such as &gt; -> >, &quot -> ', etc. """
    try:
        return htmlparser.unescape(data)
    except:
        return data

def merge_two_dicts(x, y):
    """
    merge to dictionaries
    :param x:
    :param y:
    :return: merged dict
    """
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def validateFields(fieldList, kwargs):
    """
    ensure required fields are present. Throw ValueError if not
    :param fieldList:
    :param kwargs:
    :return: no return
    """
    for field in fieldList:
        if field not in kwargs or kwargs.get(field) == '':
            raise ValueError('Required field is missing or empty: '+field)


def get_input_entity(client, incident_id, attachment_id, artifact_id):

    re_uri_match_pattern = r"""(?:(?:https?|ftp):\/\/|\b(?:[a-z\d]+\.))(?:(?:[^\s()<>]+|\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))?\))+(?:\((?:[^\s()<>]+|(?:\(?:[^\s()<>]+\)))?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))?"""
    entity = {"incident_id": incident_id, "id": None, "type": "", "meta_data": None, "data": None}

    if (attachment_id):
        entity["id"] = attachment_id
        entity["type"] = "attachment"
        entity["meta_data"] = client.get("/incidents/{0}/attachments/{1}".format(entity["incident_id"], entity["id"]))
        if entity["meta_data"].get("name"):
            entity["name"] = entity["meta_data"]["name"]
        entity["data"] = client.get_content("/incidents/{0}/attachments/{1}/contents".format(entity["incident_id"], entity["id"]))

    elif (artifact_id):
        entity["id"] = artifact_id
        entity["type"] = "artifact"
        entity["meta_data"] = client.get("/incidents/{0}/artifacts/{1}".format(entity["incident_id"], entity["id"]))

        # handle if artifact has attachment
        if (entity["meta_data"]["attachment"]):
            entity["name"] = entity["meta_data"]["attachment"]["name"]
            entity["data"] = client.get_content("/incidents/{0}/artifacts/{1}/contents".format(entity["incident_id"], entity["id"]))

        # else handle if artifact.value contains an URI using RegEx
        else:
            match = re.match(re_uri_match_pattern, entity["meta_data"]["value"])

            if (match):
                entity["uri"] = match.group()

            else:
                raise IntegrationError("Artifact has no attachment or supported URI")

    else:
        raise ValueError('attachment_id AND artifact_id both None')

    return entity


def reset_resilient_client():
    """Reset the cached client"""
    global resilient_client
    resilient_client = None

def get_resilient_client(opts):
    """Get a connected instance of SimpleClient for Resilient REST API"""
    global resilient_client
    global connection_opts

    new_opts = (opts.get("cafile"),
                opts.get("org"),
                opts.get("host"),
                opts.get("port"),
                opts.get("proxy_host"),
                opts.get("proxy_port"),
                opts.get("proxy_user"),
                opts.get("proxy_password"),
                opts.get("email"))
    if new_opts != connection_opts:
        resilient_client = None
        connection_opts = new_opts
    #if resilient_client:
    #    return resilient_client

    resilient_client = resilient.get_client(opts)
    return resilient_client