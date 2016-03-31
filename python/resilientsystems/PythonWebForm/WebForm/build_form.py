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
Module for handling the dynamic form building 
"""

# Methods and functions for building the dynamic web form and for handling the creation of an incident

import datetime
import time
import re
from copy import deepcopy
from pprint import pprint

from flask import render_template, request, redirect, url_for, g, session, flash
import wtforms as wtf
import wtforms.widgets.core

from WebForm import app
#from .forms import LoginForm, CaseForm, DatePickerWidget, DateTimePickerWidget
from .forms import CaseForm, DatePickerWidget, DateTimePickerWidget

from .ResOrg import ResOrg

# allows specifying width and height in creation
# wtforms default TextArea requires that you specify the width and height in the
# jinja 2 template
class TextArea(wtforms.widgets.core.TextArea):
    """
    Extend the textarea object to allow for specifying the height and width
    of the area
    """
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __call__(self, field, **kwargs):
        for arg in self.kwargs:
            if arg not in kwargs:
                kwargs[arg] = self.kwargs[arg]
        return super(TextArea, self).__call__(field, **kwargs)


# Simple function to create the form dynamically
# Needs to have validation etc added to the form fields
def build_form():
    """
    Simple function that builds the web form
    """
    if getattr(g, 'res_org') is None:
        g.res_org = ResOrg()

    form = CaseForm()

    # walk thgrough the form layout and build the form fields dynamically
    for f in g.res_org.form_config:
        field = None
        #print(">> f is {}\n".format(f))
        if f['fieldtype'] == 'Text':
            field = wtf.TextField(f['fieldlabel'])
        elif f['fieldtype'] == 'TextArea':
            field = wtf.TextAreaField(f['fieldlabel'], widget=TextArea(rows=f.get('rows', 20), cols=f.get('cols', 80)))
        elif f['fieldtype'] == 'Select':
            selections = get_selections(f['choosefrom'])
            field = wtf.SelectField(f['fieldlabel'], choices=selections)

        elif f['fieldtype'] == 'MultiSelect':
            selections = get_selections(f['choosefrom'])
            field = wtf.SelectMultipleField(f['fieldlabel'], choices=selections)
        elif f['fieldtype'] == "Date":
            #Need to specify a widget to allow for selecting from calendar
            field = wtf.DateField(f['fieldlabel'], widget=DatePickerWidget()) 
        elif f['fieldtype'] == "DateTime":
            #Need to specify a widget to allow for selecting from calendar
            field = wtf.DateTimeField(f['fieldlabel'], widget=DateTimePickerWidget()) 
        elif f['fieldtype'] == "Boolean":
            field = wtf.BooleanField(f['fieldlabel'])
        elif f['fieldtype'] == "Number":
            field = wtf.IntegerField(f['fieldlabel'])
        else:
            continue  # we don't know what you specified, so just skip it

        if field is not None:
            # Append the field to the object
            CaseForm.append_field(f['fieldname'], field)

    return form


# Build the list of select values from the Resilient system configuration
def get_selections(resfield):
    """
    build the select list from the resilient system configuration incident enumerations
    """
    enums = g.res_org.get_enums()

    fenum = enums.get(resfield, None)
    if fenum is not None:
        choices = []
        for e in fenum:
            for key, value in e.iteritems():
                nt = convert_selection(key, value)
                choices.append(nt)
        return choices
    else:
        raise Exception("{} not found".format(resfield))

# Swap the key and value pair to a tuple of Value, key so that it is
# represented in select and multi select fields
def convert_selection(key, value):
    """
    invert the key,value tuple for handling in the form correctly
    """
    return (value, key)


# Convert the date/time string to the time since the epoch in miliseconds
def convert_date(item):
    """
    Convert a date time string into a time sinze epoch
    The form returns a date time string of the format below
    """
    date = datetime.datetime.strptime(item, "%Y-%m-%d %H:%M:%S")
    epoch = int(time.mktime(date.timetuple())) * 1000
    return epoch


# convert multiselect returned list to a list of the integer id's for the enumerations
# the values returned are string representation of the integer
def convert_multi_select(ilist):
    values = []
    for i in ilist:
        values.append(int(i))

    return values

# Create incident based on form and  resapi
#  Does not do anyting about wether a field is required in resilient or not
def CreateIncident(request):

    res = g.res_org
    template = deepcopy(res.create_template)
    processedfields = []

    configs = res.form_config
    for f in request.form:
        # check for a null string returned
        if request.form[f] == "" or request.form[f] is None:
            continue
        ce = res.get_config(f)
        if ce is not None:
            # get mapping 
            if ce.get('fieldtype') == 'DateTime':  #re.match('DateTime', ce.get('fieldtype')):
                value = convert_date(request.form[f])
            elif ce.get('fieldtype') == 'Date':  #re.match('Date', ce.get('fieldtype')):
                # Date only fields have time of 00am
                value = convert_date(request.form[f]+" 00:00:00")
            elif re.match(ce.get('fieldtype'), "Select"):
                value = int(request.form[f])
            elif re.match(ce.get('fieldtype'), "MultiSelect"):
                value = convert_multi_select(request.form.getlist(f))
            elif 'Boolean' in ce.get('fieldtype'):
                if request.form[f] == 'y':
                    value = True
                else:
                    value = False
            elif 'Number' in ce.get('fieldtype'):
                value = int(request.form[f])
            else:
                value = request.form[f]

            if 'properties' in ce.get('resapi'):
                incidentitem = ce.get('resapi').split('.')[1]
                props = template.get('properties') 
                props[incidentitem] = value
            else:
                template[ce.get('resapi')] = value

        processedfields.append(ce)  # Save the processed fields so we can check for required fields

    # we will make the discovered date the current date/time
    template['discovered_date'] = int(time.mktime(datetime.datetime.utcnow().timetuple())) * 1000

    pprint("incident template {}".format(template))

    try:
        incident = res.client.post('/incidents/?want_full_data=true', template)
        flash("Case Created {}".format(incident.get('id')))
        return(incident, None)
    except Exception as e:
        exceptcode = e
        flash("CREATION ERROR - {}".format(e))
        return(None, exceptcode)



