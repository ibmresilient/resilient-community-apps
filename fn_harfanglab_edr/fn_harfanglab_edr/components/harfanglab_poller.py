import datetime
import logging
from circuits import Event, Timer
from resilient_circuits import ResilientComponent, handler
from resilient_lib import validate_fields, build_incident_url, build_resilient_url, IntegrationError
from fn_harfanglab_edr.lib.jinja_common import JinjaEnvironment
from fn_harfanglab_edr.lib.resilient_common import ResilientCommon
from fn_harfanglab_edr.lib.harfanglab_sdk import HarfangLabConnector


PACKAGE_NAME = "fn_harfanglab_edr"

DEFAULT_INCIDENT_CREATION_TEMPLATE = "data/incident_creation_template.jinja"
DEFAULT_INCIDENT_UPDATE_TEMPLATE = "data/incident_update_template.jinja"
DEFAULT_INCIDENT_CLOSE_TEMPLATE = "data/incident_close_template.jinja"
DEFAULT_AGENT_TEMPLATE = "data/agent_template.jinja"

POLLER_CHANNEL = "harfanglab_poller"

DEFAULT_POLLER_LOOKBACK_MINUTES = 120
DEFAULT_POLLER_SECONDS = 600
LOG = logging.getLogger(__name__)


class Poll(Event):
    """A Circuits event to trigger polling"""
    channels = (POLLER_CHANNEL,)


class PollCompleted(Event):
    """A Circuits event to notify that this poll event is completed"""
    channels = (POLLER_CHANNEL,)


class HarfangLabPollerComponent(ResilientComponent):
    """
    Event-driven polling for HarfangLab security events
    """

    # This doesn't listen to Action Module, only its internal channel for timer events
    # But we still inherit from ResilientComponent so we get a REST client etc
    channel = POLLER_CHANNEL

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(HarfangLabPollerComponent, self).__init__(opts)
        self.jinja_env = JinjaEnvironment()
        self.options = opts.get(PACKAGE_NAME, {})

        self._load_options(opts)
        if self.polling_interval == 0:
            LOG.info(
                u"HarfangLab poller interval is not configured.  Automated escalation is disabled.")
            return

        # Set last_poller_time to the specified polling_lookback in minutes to pick up extra threats
        # the first time polling.
        self.polling_lookback = int(self.options.get(
            "polling_lookback", DEFAULT_POLLER_LOOKBACK_MINUTES))
        self.last_poller_time = datetime.datetime.utcnow(
        ) - datetime.timedelta(minutes=self.polling_lookback)

        LOG.info(u"HarfangLab poller initiated, polling interval %s",
                 self.polling_interval)
        Timer(self.polling_interval, Poll(), persist=False).register(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self._load_options(opts)

    @handler("Poll")
    def _poll(self, event):
        """Handle the timer"""
        LOG.info(u"HarfangLab start polling.")
        self._escalate()

    @handler("PollCompleted")
    def _poll_completed(self, event):
        """Set up the next timer"""
        LOG.info(u"HarfangLab poller complete.")
        Timer(self.polling_interval, Poll(), persist=False).register(self)

    def _load_options(self, opts):
        """Read options from config"""
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

        # Validate required fields in app.config are set
        required_fields = ["api_url", "api_key", "verify"]
        validate_fields(required_fields, self.options)

        self.polling_interval = int(self.options.get("polling_interval", 0))
        if not self.polling_interval:
            return

        # Create api client
        verify = True
        if self.options.get('verify').lower() == 'false':
            verify = False
        self.harfanglab_connector = HarfangLabConnector(self.options.get('api_url'), self.options.get(
            'api_key'), verify, self.options.get('http_proxy'), self.options.get('https_proxy'))

        self.resilient_common = ResilientCommon(self.rest_client())

    def _escalate(self):
        """ This is the main logic of the poller
            Search for HarfangLab Security Events and create associated cases in Resilient SOAR
        """
        try:
            poller_start = datetime.datetime.utcnow()
            LOG.debug("Poll start = %s ", poller_start)

            # Call HarfangLab EDR Manager to get the latest security events since last poller time
            (last_fetch, incidents) = self.harfanglab_connector.fetch_security_events(
                alert_status=self.options.get('alert_status', None),
                alert_type=self.options.get('alert_type', None),
                min_severity=self.options.get('min_severity', None),
                max_fetch=self.options.get('max_fetch', None),
                first_fetch=self.options.get('first_fetch', None),
                last_fetch=datetime.datetime.timestamp(self.last_poller_time)*1000000)

            try:
                for incident in incidents:
                    self._process_security_event(incident)

            finally:
                self.last_poller_time = poller_start

        except Exception as err:
            LOG.error(str(err))
        finally:
            # We always want to reset the timer to wake up, no matter failure or success
            self.fire(PollCompleted())

    def _process_security_event(self, incident):
        """Process the security event found in HarfangLab EDR.  Use jinja templates to create, update
           or close the incident in SOAR.

        Args:
            alert ([type]): [HarfangLab alert object]
        """
        try:
            alert = incident.get("alert")
            alert_id = alert.get("id")

            alert['event_create_date'] = alert.get('@event_create_date')
            alert['timestamp'] = alert.get('@timestamp')

            resilient_incident = self.resilient_common.find_incident(alert_id)
            if resilient_incident is None:
                # create a new incident
                incident_payload = self.jinja_env.make_payload_from_template(
                    self.options.get("create_incident_template"),
                    DEFAULT_INCIDENT_CREATION_TEMPLATE,
                    alert)

                incident_payload["properties"][
                    "harfanglab_security_event_url"] = f'<a target=\'blank\' href=\'{alert.get("incident_link")}\'>HarfangLab Security Event</a>'
                resilient_incident = self.resilient_common.create_incident(
                    incident_payload)

                # Adding agent information
                agent = alert.get('agent')
                if agent:
                    agent_payload = self.jinja_env.make_payload_from_template(
                        self.options.get("agent_template"),
                        DEFAULT_AGENT_TEMPLATE,
                        agent)
                    self.resilient_common.add_agent_information(
                        resilient_incident.get('id'), agent_payload)

                LOG.info(
                    f'Created incident {resilient_incident.get("id")} from HarfanLab Security Event {alert_id}')

            else:
                resilient_incident_id = resilient_incident.get('id')

                if resilient_incident.get("plan_status") == "C" and alert.get("status") not in ['closed', 'false_positive']:
                    """Incident is closed in Resilient but not in HarfangLab"""
                    self.harfanglab_connector.change_security_event_status(
                        alert_id, 'closed')
                    LOG.info(
                        f'Changing status to "closed" for HarfangLab Security Event {alert_id} as it has been closed in Resilient')

                elif alert.get("status") == "closed" and resilient_incident.get("plan_status") != "C":
                    """Incident is closed in HarfangLab EDR but not in Resilient"""
                    incident_payload = self.jinja_env.make_payload_from_template(
                        self.options.get("close_incident_template"),
                        DEFAULT_INCIDENT_CLOSE_TEMPLATE,
                        alert)
                    updated_resilient_incident = self.resilient_common.close_incident(
                        resilient_incident_id,
                        incident_payload)
                    _ = self.resilient_common.create_incident_comment(
                        resilient_incident_id, "Close synchronized from HarfangLab")
                    LOG.info(
                        f'Closed incident {resilient_incident_id} from HarfangLab Security Event {alert_id}')
                # else:
                #    # update an incident
                #    incident_payload = self.jinja_env.make_payload_from_template(
                #        self.options.get("update_incident_template"),
                #        DEFAULT_INCIDENT_UPDATE_TEMPLATE,
                #        alert)
                #    updated_resilient_incident = self.resilient_common.update_incident(
                #        resilient_incident_id,
                #        incident_payload)
                #    _ = self.resilient_common.create_incident_comment(resilient_incident_id, "Updates synchronized from HarfangLab")
                #    LOG.info(f'Updated incident {resilient_incident_id} from HarfangLab Security Event {alert_id}')

        except Exception as err:
            LOG.error(str(err))
