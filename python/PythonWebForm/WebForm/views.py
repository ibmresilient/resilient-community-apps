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
Flask views for the web application
"""

import logging
import hashlib

from flask import render_template, request, redirect, url_for, g, session, flash, abort
from flask.ext.login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from WebForm import app

import wtforms as wtf
import wtforms.widgets.core

#import co3 as resilient
from .build_form import build_form, CreateIncident
from .ResOrg import ResOrg
from .forms import LoginForm, TestForm
from .models import User


LOG = logging.getLogger(__name__)

# View for the login form
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    """
    FLASK route for the /index and the document root
    """
    if getattr(g, 'res_org', None) is None:
        g.res_org = ResOrg()


    # this is a bit wierd.  if I don't build the form here and then build it again, the first time
    # the page is loaded, the form is not rendered.
    form = build_form()
    if form is not None:
        form.append_field("Submit", wtf.SubmitField("Submit"))

    if request.method == 'POST':
        (incident, error) = CreateIncident(request)  #invoke function to create incident based on form
        LOG.debug("returned values from CreateIncident {}:{}".format(incident, error))
        return redirect(url_for('index'))

    form = build_form() # build the dynamic form
    if form is not None:
        form.append_field("Submit", wtf.SubmitField("Submit"))

    if form is not None:
        return render_template('index.html', title='Case Form', form=form)
    else:
        render_template('error.html', title="CaseForm Error", error="Case Form Layout def error")



@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Flask route/view for the login form
    """
    LOG.debug("Entering Login")
    error = None
    form = LoginForm()
    if getattr(g, 'res_org', None) is None:
        g.res_org = ResOrg()

    if request.method == 'POST':
        # the below could be done in one line, but this is for clarity in
        # the example
        h = hashlib.sha256()
        h.update(request.form['password'])
        hd = h.hexdigest()
        user = User.query.filter_by(username=request.form['userid'], password=hd)
        if user.count() == 0:
            flash("Invalid User Name")

            return redirect(url_for('login'))

        elif user.count() == 1:
            login_user(user.one())
            return redirect(url_for('index'))

        else:
            abort(404)


    return render_template('login.html', error=error, title='Login', form=form)
        

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route("/test", methods=['GET', 'POST'])
def tester():
    if request.method == 'POST':
        for f in request.form:
            print "{} Tester {}".format(f, request.form[f])
            if f == 'select':
                print "In MultiSelect"
                print "{}".format(request.form.getlist(f))
        redirect(url_for('tester'))
    form = TestForm()
    return render_template('test.html', form=form)




