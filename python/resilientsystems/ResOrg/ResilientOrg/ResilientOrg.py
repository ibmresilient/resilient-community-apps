"""
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
"""

import logging
import time

import json

import co3 as resilient

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class ResilientOrg(object):
    """
    Utility class for operations against an incident and an organization
    """
    def __init__(self, client=None, opts=None):
        # when no client is passed we need to establish the connection.  However
        # to work with the circuits package the client needs to be a method/function
        # that gets called
        #self.log = logging.getLogger(__name__)
        #self.log.setLevel(logging.DEBUG)

        self.enums = None
        if client:
            self.client = client  # set to the function that is passed in
        else:
            if opts is not None:
                # make the client function be
                self.client = self.get_client

                url = "https://{}:{}".format(opts.get("host", ""), opts.get("port", 443))
                self._client = resilient.SimpleClient(org_name=opts.get("org"),
                                                      proxies=opts.get("proxy"),
                                                      base_url=url,
                                                      verify=opts.get("cafile") or True)

                userinfo = self._client.connect(opts["email"], opts["password"])

                # Validate the org, and store org_id in the opts dictionary
                if(len(userinfo["orgs"])) > 1 and opts.get("org") is None:
                    raise resilient.co3.SimpleHTTPException("""
                                    User is a member of multiple organizations; please specify one.
                                    """)
                if(len(userinfo["orgs"])) > 1:
                    for org in userinfo["orgs"]:
                        if org["name"] == opts.get("org"):
                            opts["org_id"] = org["id"]
                else:
                    opts["org_id"] = userinfo["orgs"][0]["id"]
            else:
                return None


        self.get_users()
        self.alltasks = None
        self.groups = None

    def get_client(self):
        """
        used when the object establishes the connection to resilient instead of a client
        function being passed in a function is used, since the resilient_circuits module passes a
        function to get a client connection from its pool of connections
        """
        return self._client

    def get_phases(self):
        """
        Get the phase configuration from the org
        """
        phase = self.client().get("/phases")
        return phase

    def get_field_enums_by_type(self, ftype):
        """
        get a simple dictionary list of the field enumerations
        for a given type
        """
        fields = self.client().get('/types/{}/fields'.format(ftype))


        # Re- factor
        field_enums = {}
        for majorkey in fields:
            vlist = []
            name = majorkey['name'].encode('ascii')
            if majorkey['values']:
                pass
                for values in majorkey['values']:
                    vdict = {}
                    vdict[values.get('label').encode('utf-8')] = values.get('value')
                    vlist.append(vdict)
                field_enums[name] = vlist

        return field_enums


    # build a dictionary of just the enumerations for  incident fields.
    def get_field_enums(self):
        """
        get the field enumerations as a simple json structure of
        enumeration and id value
        """
        self.enums = self.get_field_enums_by_type('incident')
        return self.enums

    def get_incident_types(self):
        """
        get the incident type enumerations
        """
        itypes = self.client().get("/incident_types")
        return itypes

    def map_phase_id(self, pid, plist):
        """
        Map a numeric phase id to its name
        """
        log.debug("Phase id {}".format(pid))
        log.debug("Phase List {}".format(plist))
        for phase in plist.get('entities'):
            log.debug(phase)
            if phase.get('id') == pid:
                return phase.get('name')
        return None

    def map_phase_name_to_id(self, pname, plist):
        """
        Map a phase name to its associated id
        """
        log.debug("map phase name to id {}".format(pname))
        for phase in plist.get('entities'):
            log.debug(phase)
            if phase.get('name') == pname:
                return phase.get('id')
        return None

    def get_table_definition(self, tablename):
        """
        get the definition of a data table object based on the tables api_name
        """
        url = "/types/{}".format(tablename)
        fields = self.client().get(url)
        return fields

    def get_incident_by_id(self, incidentid):
        """
        Obtain the full content of an incident based on its incident id
        """
        uri = "/incidents/{}".format(incidentid)
        return self.client().get(uri)

    def get_users(self):
        """
        Get the users of an organization
        Used when assigning users to an incidents membership
        """
        uri = "/users"
        try:
            self.users = self.client().get(uri)
        except resilient.co3.SimpleHTTPException as ecode:
            log.error("Failed to get users from system {}".format(ecode))
            self.users = None
            log.error("Failed to get users {}".format(ecode))
            return None
        return self.users

    def get_groups(self):
        """
        Get the groups configured in the system
        """
        uri = "/groups"
        try:
            self.groups = self.client().get(uri)
        except resilient.co3.SimpleHTTPException as ecode:
            log.error("Failed to get groups from system {}".format(ecode))
            self.groups = None
            return False
        return self.groups

    def get_all_tasks(self):
        """
        Get all of the tasks in an org
        """
        uri = "/task_order"
        try:
            self.alltasks = self.client().get(uri)
        except resilient.co3.SimpleHTTPException as ecode:
            log.error("Failed to get all tasks {}".format(ecode))
            self.alltasks = None
        return self.alltasks

    def get_task(self, taskid):
        """
        Get a specific tasks definition based on the task id
        """
        uri = "/tasks/{}".format(taskid)
        try:
            task = self.client().get(uri)
        except resilient.co3.SimpleHTTPException as ecode:
            log.error("Failed to get task {} \n {}".format(taskid, ecode))
            return None
        return task

    def put_task(self, taskid, task):
        """
        update a task's definition
        """
        uri = "/tasks/{}".format(taskid)
        try:
            ntask = self.client().put(uri, task)
        except resilient.co3.SimpleHTTPException as ecode:
            log.error("Failed to update task \n{}".format(ecode))
            return None
        return ntask

    @staticmethod
    def apiname(field):
        """The full (qualified) programmatic name of a field"""
        if field["prefix"]:
            fieldname = u"{}.{}".format(field["prefix"], field["name"])
        else:
            fieldname = field["name"]
        return fieldname

    def create_case(self, tplate):
        """
        Create a new incident in resilient based on the template provided
        Assumes that the template meets the minimum requirements for fields for a given org
        """
        log.debug(tplate)
        url = "/incidents/?want_full_data=true"
        log.debug(url)
        try:
            incident = self.client().post(url, tplate)
        except resilient.co3.SimpleHTTPException as ecode:
            return (None, ecode)

        return (incident, None)

    def get_incident_type_id(self, itypes, itstring):
        """
        convert from a label to the numeric value of the incident typ
        """
        for itype in itypes:
            itdict = itypes.get(itype)
            if itdict.get('name') == itstring:
                return itdict.get('id')
        return None

    def map_incident_type_id_to_name(self, itypes, typeid):
        """
        convert from an incident type id to the label
        """
        if itypes.get(str(typeid), None) is not None:
            return itypes.get(str(typeid)).get('name')
        return None

    def get_user_id(self, userlist, name):
        """
        get the specified user or group name in id format
        """
        log.debug("name {} >userlist {}".format(name, userlist))
        for user in userlist:
            if user.get('name') == name:
                return user.get('id')
        return None

 


class ResilientIncident(object):
    """
    Utility class for operations against an incident 
    Expects that a ResilientOrg object will be passed in
    if an Incident is passed in, then operations are against that
    if an incident id is passed in, it will get the incident
    """
    def __init__(self, reso, incident=None,incidentid=None):
        if incident is None and incidentid is None:
            raise Exception("an incident or an incident id must be passed in")

        self.reso = reso

        if incident:
            self.incident = incident
        else:
            self.incident = self.reso.get_incident_by_id(incidentid)

        self.inc_id = self.incident.get('id')

    def create_note(self, content):
        """
        Create a note in an incident
        """
        note = {
            "parent_id":None,
            "mentioned_users":[],
            "text":content,
            "inc_id":self.inc_id,
            "id":None
        }
        try:
            nnote = self.reso.client().post("/incidents/{}/comments".format(self.inc_id),
                                            note)
        except resilient.co3.SimpleHTTPException as ecode:
            log.error("Note Creation failed {}".format(ecode))
            return None
        return nnote

    def create_task(self, taskname, instructions, phasename):
        """
        Create a task in the incident
        """
        task_template = {
            "inc_id": self.inc_id,
            "name": taskname,
            "phase_id": None,
            "instr_text": instructions,
            "active": True,
            "auto_task_id": None,
            "cat_name": "",
            "custom": False,
            "creator": {},
            "description": None,
            "frozen": False,
            "fullname": "Unassigned",
            "id": None,
            "inc_name": "",
            "inc_owner_id": None,
            "inc_training": False,
            "init_date": None,
            "last_update": None,
            "owner_fname": None,
            "owner_lname": None,
            "members": None,
            "perms": {},
            "regs": None,
            "required": True,
        }

        plist = self.reso.get_phases()
        log.debug("Phasename {}".format(phasename))
        pid = self.reso.map_phase_name_to_id(phasename, plist)
        log.debug("Phase id = {}".format(pid))
        if pid:
            task_template['phase_id'] = pid
        else:
            log.error("Phase name specified does not match phases defined in the system")
            return None

        ntask = self.reso.client().post("/incidents/{}/tasks".format(self.inc_id), task_template)
        return ntask

    def create_milestone(self, title, description):
        """
        create a milestone on an incident using the current time
        """
        mtemp = {"date":int(time.time()*1000),
                 "description":description,
                 "title":title}

        try:
            nmst = self.reso.client().post("/incidents/{}/milestones".format(self.inc_id), mtemp)
        except resilient.co3.SimpleHTTPException as ecode:
            log.error("Resilient server error {}".format(ecode))
            return None

        return nmst

    def put_table_row(self, tableid, rowdata, rowid):
        """
        update an existing row of a table within an incident
        """
        log.debug(rowdata)
        log.debug(rowid)
        url = "/incidents/{}/table_data/{}/row_data/{}".format(self.inc_id, tableid, rowid)
        log.debug(url)
        try:
            tdata = self.reso.client().put(url, rowdata)
            return(tdata, None)
        except resilient.co3.SimpleHTTPException as ecode:
            return(None, ecode)

    def put_case(self, case):
        """
        update an incident and return the full data after the update
        This expects a template for the incident to be passed, which
        may not be the same as the current incident (modified)
        """
        try:
            incident = self.reso.client().put('/incidents/{}/?want_full_data=true'.format(case.get('id')), case)

            return(incident, None)
        except resilient.co3.SimpleHTTPException as ecode:
            return (None, ecode)

    def get_incident_tasks(self):
        """
        Get the task list for a given incident.  pulls only the current list of tasks
        """
        uri = "/incidents/{}/tasktree".format(self.inc_id)
        try:
            itasks = self.reso.client().get(uri)
        except resilient.co3.SimpleHTTPException as ecode:
            log.error("Failed to get incident tasks {}".format(ecode))
            return None

        return itasks

    def get_table_data(self, tableid):
        """
        Tables within an incident are updated and manipulated as separate editable objects
        They are fetched from the server in separate http GET operations
        Returns a tuple

        If a 404 is returned, this means that the table has no data in this incident,
        return 404 to indicate that any operation will have to do a POST instead of a put
        """
        url = "/incidents/{}/table_data/{}".format(self.inc_id, tableid)
        log.debug(url)
        try:
            return (self.reso.client().get(url), None)
        except resilient.co3.SimpleHTTPException as ecode:
            if ecode.response.status_code == 404:
                return (None, ecode.response.status_code)
            else:
                return (None, ecode)


    def add_table_row(self,tabletemplate,tableid):
        """
        Adds a new row to a table.  
        newtable == True indicates that the table has no content so a
        POST has to be done
        the url is /incidents/<incidentnum>/table_data/<tableid>/row_data
        {"cells":{"139":{"value":"AAAAA"},"140":{"value":"BBBBB"}}}
        """

        url = "/incidents/{}/table_data/{}/row_data".format(self.inc_id,tableid)
        log.debug(url)

        try:
            return (self.reso.client().post(url,tabletemplate),None)
        except resilient.co3.SimpleHTTPException as ecode:
            log.error("failed to add row to table {}".format(ecode))
            return (None,ecode)










