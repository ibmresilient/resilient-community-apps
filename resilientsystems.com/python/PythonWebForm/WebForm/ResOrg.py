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

import os
import json
#from collections import OrderedDict

import co3 as resilient
from WebForm import app

"""
resilient access utility module
"""


# Object class for dealing with the resilient organization 

class ResOrg(object):
    """
    Utility object
    """
    def __init__(self):
        self.config = app.config
        self.form_config = None

        config = self.config
        self.client = resilient.SimpleClient(org_name=config['RES_ORG'], 
                                             base_url="https://{}:{}".format(config['RES_HOST'],
                                                                             config['RES_PORT']), 
                                             verify=config['RES_CA'])
        self.client.connect(config['RES_ID'], config['RES_PW'])
        self.enums = None
        self.enums = self.get_field_enums()
        self.form_config = self.get_form_config()
        self.create_template = None
        self.create_template = self.get_template('CreateTemplate')


    # build a dictionary of just the enumerations for fields.
    def get_field_enums(self):
        """
        get a simple dictionary list of the field enumerations
        for a given type
        """
        ftype = 'incident'
        fields = self.client.get('/types/{}/fields'.format(ftype))


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



    # read the configuration for the input form
    def get_form_config(self):
        """
        Read the configuration of the form from the file
        """
        if self.form_config is None:
            aproot = os.path.dirname(os.path.abspath(__file__))
            formfile = os.path.join(aproot, 'config', 'form_layout.json')
            with open(formfile, 'rb') as ff:
                self.form_config = json.load(ff)

        return self.form_config

    def get_enums(self):
        if self.enums is None:
            self.enums = self.get_field_enums()

        return self.enums

    def get_template(self, tempname):
        """
        load the incident create template
        """
        if self.create_template is None:
            aproot = os.path.dirname(os.path.abspath(__file__))
            formfile = os.path.join(aproot, 'config', tempname+'.json')
            with open(formfile, 'rb') as ff:
               template = json.load(ff)
        return template


    def get_config(self, configelement):
        """
        Get a configuration element from the form layout
        """
        for i in self.form_config:
            if i.get('fieldname', None) == configelement:
                return i
        return None

