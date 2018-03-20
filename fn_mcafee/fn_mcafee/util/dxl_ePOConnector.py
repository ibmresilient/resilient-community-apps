import json
from dxlclient import Request
import logging

# Configure Logger
logger = logging.getLogger(__name__)

dxlClientCNX = None
ePOUniqueID = "epo1"


def tagSystemsOnEPO(dxlClientCNX, sysList, tagName):
    """
    Varargs to be
    {
        "command" = "system.applyTag",
        "params" = {"names": [<systemList may be IP / hostname>],"tagName":<tagName>},
        "output_format"=OutputFormat.JSON
    }
    """

    var_args = {
        "command": "system.applyTag",
        "params": {
            "names": sysList,
            "tagName": tagName
        },
        "output": "json"
    }

    EPO_SERVICE_TOPIC = ("/mcafee/service/epo/remote/{0}").format(ePOUniqueID)

    req = Request(EPO_SERVICE_TOPIC)
    # Set the payload
    req.payload = json.dumps(var_args).encode(encoding="UTF-8")

    # Display the request that is going to be sent
    logger.info("Asynchronous Request:\n" + json.dumps(var_args, sort_keys=True, indent=4, separators=(',', ': ')))

    # Send the request and wait for a response (synchronous)
    dxlClientCNX.sync_request(req)