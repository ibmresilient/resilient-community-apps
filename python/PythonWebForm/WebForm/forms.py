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

# Form object definitions here.

"""
Flask web form definitions and widgets
"""
from copy import deepcopy

from flask.ext.wtf import Form
#from wtforms import StringField, BooleanField1
import wtforms as wtf
from wtforms.validators import DataRequired


# SAB Start widget playings  from Flask App Builder
from wtforms.widgets import HTMLString, html_params
#from flask.ext.wtf import fields, widgets, TextField


class DatePickerWidget(object):
    """
    Date picker
    """
    data_template = (
        '''
        <div class="container">
            <div class="row">
                <div class='col-sm-6'>
                    <div class="form-group">
                        <div class='input-group date' id=%(id)s>
                            <input type='text' class="form-control"  %(text)s />
                            <span class="input-group-addon">
                                <span class="glyphicon glyphicon-calendar"></span>
                            </span>
                        </div>
                    </div>
                </div>
                <script type="text/javascript">
                    $(function () {
                        $('#%(id)s').datepicker({format:"yyyy-mm-dd"});
                    });
                </script>
            </div>
        </div>
        '''
    )

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', 'datetimepicker1')  # field.id)
        kwargs.setdefault('name', field.name)
        if not field.data:
            field.data = ""
        template = self.data_template

        return HTMLString(template % {
            'text': html_params(type='text', value=field.data, **kwargs),
            'id': field.id
        })


class DateTimePickerWidget(object):
    """
    Date time picker widget definition
    """
    data_template = (
        '''
        <div class="container">
            <div class="row">
                <div class='col-sm-6'>
                    <div class="form-group">
                        <div class='input-group date' id=%(id)s>
                            <input type='text' class="form-control"  %(text)s />
                            <span class="input-group-addon">
                                <span class="glyphicon glyphicon-calendar"></span>
                            </span>
                        </div>
                    </div>
                </div>
                <script type="text/javascript">
                    $(function () {
                        $('#%(id)s').datetimepicker({
                             format:"YYYY-MM-DD HH:mm:ss"
                            });
                    });
                </script>
            </div>
        </div>
        '''
    )

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('name', field.name)
        if not field.data:
            field.data = ""
        template = deepcopy(self.data_template)

        return HTMLString(template % {
            'text': html_params(type='text', value=field.data, **kwargs),
            'id': field.id
        })
# SAB end widget playing


# Define the login form for authentication
class LoginForm(Form):
    """
    Form for login to the page.
    """
    userid = wtf.StringField('User:', validators=[DataRequired()])
    password = wtf.PasswordField('Password')

# Scaffold for the dynamicaly created case form


class CaseForm(Form):
    """
    Class for the case creation form.
    """
    @classmethod
    def append_field(cls, name, field):
        """
        Class method to add a field to the form as
        this form is a dynamicly built construct
        """
        setattr(cls, name, field)
        return cls


class TestForm(Form):
    """
    Test form object
    """
    dtsample = wtf.DateTimeField(
        "Date Time Sample", widget=DateTimePickerWidget())
    datesample = wtf.DateField("Date Sample", widget=DatePickerWidget())
    select = wtf.SelectMultipleField("Multi Select", choices=[('A', 'a'), ('B', 'b'), ('C', 'c')])
    check = wtf.BooleanField("Boolean")
