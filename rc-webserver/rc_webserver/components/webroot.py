"""Circuits Web component for handling paths at the Web root"""

import logging
from circuits.web import Controller, expose

LOG = logging.getLogger(__name__)


class WebRoot(Controller):
    """Routes for Web root ('/') requests"""

    @expose("index", priority=1)
    def _index(self, event):
        if not event.value:
            # only need to do this if we haven't overridden elsewhere
            return "<HTML><BODY>Not Found</BODY></HTML>"
        else:
            return

    @expose("robots.txt")
    def _robots(self):
        """
        Robots will request this.
        """
        self.response.headers["Content-Type"] = "text/plain"
        return "User-agent: *\nDisallow: *"

    @expose("favicon.ico", priority=1)
    def _favicon(self, event):
        """
        Browsers will request the favicon.  Redirect to the public Resilient site.
        """
        if not event.value:
            # only need to do this if we haven't overridden elsewhere
            return self.redirect("//resilientsystems.com/favicon.ico", code=302)
        else:
            return
