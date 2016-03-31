#!/usr/bin/env python
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

activate = "/var/www/WebForm/formvenv/bin/activate_this.py"
execfile(activate,dict(__file__=activate))

import sys
sys.path.insert(0,"/var/www/WebForm/")

import requests
requests.packages.urllib3.disable_warnings()

import logging
 
logging.getLogger("requests.packages.urllib3").setLevel(logging.WARNING)


file_handler = logging.handlers.RotatingFileHandler("app.log", maxBytes=10000000, backupCount=10)
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s:%(name)s:%(levelname)-8s:%(lineno)s:%(message)s'
                )

file_handler.setFormatter(logging.Formatter('%(asctime)s:%(name)s:%(levelname)-8s:%(lineno)s:%(message)s'))
logging.getLogger().addHandler(file_handler)

from WebForm import app as application
