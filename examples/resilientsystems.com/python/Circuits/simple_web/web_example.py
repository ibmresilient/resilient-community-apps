"""Circuits Web component with example webhook and webform"""
# Example Usage for Webhook:
# curl -H "Content-Type: application/json" -X POST -d '{"text": "This is a great note"}' http://localhost:9000/example/incident/2661/note
#
# Example Usage for Webform:
# In Browser, visit http://localhost:9000/example

import json
import logging
import time
import traceback
from circuits.web import BaseController
from circuits.web.exceptions import BadRequest, MethodNotAllowed, NotImplemented, InternalServerError
from rc_webserver.web import exposeWeb
from resilient_circuits.actions_component import ResilientComponent

LOG = logging.getLogger(__name__)


class WebExample(BaseController, ResilientComponent):
    """JSON web service implementing example web hooks"""

    def __init__(self, opts):
        """ Simple Webhook and Webform Examples """
        super(WebExample, self).__init__(opts)
        self.channel = "/example"
        urls = ["%s/%s" % (self.channel, e)  for e in self.events()]
        LOG.info("Web handler for %s", ", ".join(urls))

        self.html = """
<html>
 <head>
  <title>Submit Incident</title>
 </head>
 <body>
  <h1>Submit Incident</h1>
  <p>
    Example of a simple incident creation webform</p>
  <form action="/example/submit" method="POST">
   <table border="0" rules="none">
    <tr>
     <td>Name:</td>
     <td><input type="text" name="name"></td>
    </tr>
    <tr>
     <td>Description:</td>
     <td><input type="text" name="description"></td>
    </tr>
     <tr>
      <td colspan="2" align="center">
       <input type="submit" value="Submit">
     </td>
     </tr>
   </table>
  </form>
  <div><p>{status}</p></div>
 </body>
</html>"""

    # Web endpoints

    @exposeWeb("incident")
    def _create_note(self, event, *args, **kwargs):
        """
        Webhook to post a note to an existing incident
        POST to /example/incident/<inc_id>/note
        Payload should be  JSON in the format {"text": "<note text>"}
        """
        request = event.args[0]
        response = event.args[1]

        if request.method != "POST":
            raise MethodNotAllowed(request.method)

        try:
            incident_id = int(args[0])
            action = args[1]
        except IndexError:
            raise BadRequest(description="URL format is /incident/<inc_id>/note")
        except ValueError:
            raise BadRequest(description="%s is not a valid incident id" % args[0])

        value = request.body.getvalue()
        if value is None or len(value) == 0:
            raise BadRequest(description="Empty message body")
        try:
            body = json.loads(value.decode("utf-8"))
        except:
            raise BadRequest(description="JSON decode error in message body",
                             traceback=traceback.format_exc())
        LOG.debug(json.dumps(body, indent=2))

        note_text = body.get("text")
        description = body.get("description")
        if not note_text:
            raise BadRequest(description="'text' required in message body")

        LOG.info(json.dumps(body, indent=2))
        if action != "note":
            raise NotImplemented("The action '%s' is not handled." % action)

        # Post Note
        try:
            new_note = {"text": "<div>{}</div>".format(note_text)}
            note_uri = "/incidents/{}/comments".format(incident_id)
            note = self.rest_client().post(note_uri, new_note)
        except:
            raise InternalServerError(description="Failure to post note to Resilient",
                                      traceback=traceback.format_exc())
        response.status = 200
        return {"status": "Note ID [%d] posted to incident [%d]" % (note["id"], incident_id)}

    @exposeWeb("index")
    def _webform(self, status=""):
        LOG.info("Get webform")
        return self.html.format(status=status)

    @exposeWeb("hello")
    def hello(self):
        return "Hello World"

    @exposeWeb("submit")
    def submit(self, name, description):
        """handle form submission"""
        LOG.info("Submit incident [%s]", name)
        incident = {"name": name,
                    "description": {"content": description,
                                    "format": "html"},
                    "discovered_date": int(time.time() * 1000)}
        try:
            inc = self.rest_client().post("/incidents", incident)
            status = "Submission Succesful! Incident '%d' created." % inc['id']
        except:
            status =  "Submission Failed.\r\n\r\n" + traceback.format_exc()

        return self.html.format(status=status)
