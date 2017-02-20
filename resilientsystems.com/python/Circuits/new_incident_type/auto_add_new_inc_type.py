"""Action Module circuits example to define new incident types in the entry wizard"""

from __future__ import print_function
import logging
from circuits.core.handlers import handler
import co3
from resilient_circuits.actions_component import ResilientComponent

LOG = logging.getLogger(__name__)

CONFIG_DATA_SECTION = 'create_inc_type'

class NewIncComponent(ResilientComponent):
    """Circuits framework to add a new incident type via the entry wizard"""

    def __init__(self, opts):
        super(NewIncComponent, self).__init__(opts)

        self.options = opts.get(CONFIG_DATA_SECTION, {})
        LOG.debug(self.options)

        #The queue name, 'add_new_object', is specified in the app.config.fragment file
        self.channel = 'actions.' + self.options.get('queue', 'create_inc_type')

    @handler('add_new_incident_type')
    def _add_new_inc_type(self, event, *args, **kwargs):
        """Create new incident type in Resilient add to the Incident"""
        incident = event.message['incident']
        inc_id = incident['id']

        # Saves the name of the new incident type
        new_inc_type = incident['properties']['new_incident_type']

        if not new_inc_type:
            # No new incident type to create
            yield "No new incident type to create"
            return
        # New incident type JSON
        obj = {'system': False, 'parent_id': None, 'create_date': None,
               'name': new_inc_type,
               'hidden': False,
               'enabled': True,
               'id': None,
               'description': "Created via new incident wizard"}
        # Adds the entered incident types to Resilient
        LOG.info('Updating incident types with %s type', new_inc_type)
        try:
            new_type = self.rest_client().post('/incident_types', obj)
        except co3.co3.SimpleHTTPException as e:
            # Failed to create new incident type
            response = e.response.json() or {}
            LOG.error(u"Incident Type Creation Failed: %s", response.get("message", ""))
            raise

        def _update_inc(incident):
            """Function to add an incident type to an incident"""
            LOG.info('Updated incident with %s type', new_inc_type)
            incident['incident_type_ids'].append(new_inc_type)
            return incident
        # Updates the incident with the new incident type
        self.rest_client().get_put('/incidents/{}'.format(inc_id),
                                   _update_inc, co3_context_token=event.context)
        yield "Incident type created and applied to incident"
