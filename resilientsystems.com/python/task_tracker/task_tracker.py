#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Resilient Systems, Inc. ("Resilient") is willing to license software
# or access to software to the company or entity that will be using or
# accessing the software and documentation and that you represent as
# an employee or authorized agent ("you" or "your") only on the condition
# that you accept all of the terms of this license agreement.
#
# The software and documentation within Resilient's Development Kit are
# copyrighted by and contain confidential information of Resilient. By
# accessing and/or using this software and documentation, you agree that
# while you may make derivative works of them, you:
#
# 1)  will not use the software and documentation or any derivative
#     works for anything but your internal business purposes in
#     conjunction your licensed used of Resilient's software, nor
# 2)  provide or disclose the software and documentation or any
#     derivative works to any third party.
#
# THIS SOFTWARE AND DOCUMENTATION IS PROVIDED "AS IS" AND ANY EXPRESS
# OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL RESILIENT BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

"""Action Module task logger, implemented via circuits""" 

from __future__ import print_function
import logging
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent

LOG = logging.getLogger(__name__)

CONFIG_DATA_SECTION = "task_tracker" 


class TaskTrackerComponent(ResilientComponent):
    """Example Circuits script to implement a data-table based task tracker"""

    def __init__(self, opts):
        super(TaskTrackerComponent, self).__init__(opts) 
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        LOG.debug(self.options)

        # The queue name can be specified in the config file,
        # or default to 'framework_default_queue'
        self.channel = "actions." + self.options.get("queue", "tasktrackerqueue")

    @handler("task_tracker")
    def _task_tracker_function(self, event, *args, **kwargs):
        """FRAMEWORK FUNCTION DOCSTRING""" # CHANGE inside """
        # CHANGE everything after the following line
        # ====================================================================
        # Get information from action
        LOG.info('Getting information from action...')
        information = kwargs['message']
        task_name = information['task']['name']
        task_init_date = information['task']['init_date']
        task_closed_date = information['task']['closed_date']
        task_id = information['task']['id']
        if task_closed_date == None:
            task_closed_date=task_init_date
        task_status = information['task']['status']
        task_inc_id = information['task']['inc_id']
        # Create task note
        LOG.info('Creating task note...')
        task_note = "Task Opened"
        if task_status == "C":
            task_note = "Task Closed"
        # Create time duration 
        LOG.info('Calculating duration...')
        task_closetime = 0
        if task_closed_date != None:
            secs = (int(task_closed_date)-int(task_init_date))/1000
            minutes = int(secs/60)
            secs = secs%60
            hours = int(minutes/60)
            minutes = minutes%60
            days = int(hours/24)
            hours = hours%24
            task_closetime = "{}d {}h {}m {}s".format(days, hours, minutes, secs)

        # Get the table ID  
        LOG.info('Organizing data...')
        table_uri = '/types/'+self.options['table_api_name']
        mytable = self.rest_client().get(table_uri)
        mytable_id = mytable['id']
        # Get table column ID's
        column_ids = {}        
        for column in mytable['fields']:
            column_ids[column]=mytable['fields'][column]['id']
        # Create values dictionary
        values = {self.options['column_one']: str(task_name),
                  self.options['column_two']: str(task_note),
                  self.options['column_three']: task_init_date,
                  self.options['column_four']: task_closed_date,
                  self.options['column_five']: str(task_closetime)
                  self.options['column_six']: str(task_id)}
        table_uri = "/incidents/{}/table_data/{}/row_data".format(task_inc_id, mytable_id)
        # Create row to add
        LOG.info('Creating row...')
        row = {}
        row['cells'] = {}
        for key in column_ids:
            row['cells'][int(column_ids[key])] = {'value': values[key]}

        # Post Row
        LOG.info('Posting row...')
        self.rest_client().post(table_uri, row)
        LOG.info('Row posted! :D')

        status = "Finished executing framework code!" 
        yield status

