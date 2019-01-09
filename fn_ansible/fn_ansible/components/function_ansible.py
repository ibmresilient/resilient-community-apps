# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from subprocess import PIPE, Popen
import logging
import os
import chardet
import json
import time
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_ansible.util.selftest as selftest


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_ansible"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_ansible", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_ansible", {})

    @function("fn_ansible")
    def _fn_ansible_function(self, event, *args, **kwargs):
        """Function: Ansible is simple IT engine for automation, it is designed for manage many systems, rather than just one at a time."""
        try:
            # Get the function parameters:
            host = kwargs.get("host") # text
            playbook_name = kwargs.get("playbook_name") # text
            ansible_param1 = kwargs.get("ansible_param1")  # text
            ansible_param2 = kwargs.get("ansible_param2")  # text
            ansible_param3 = kwargs.get("ansible_param3")  # text

            log = logging.getLogger(__name__)
            log.info("host: %s", host)
            log.info("playbook_name: %s", playbook_name)
            log.info("ansible_param1: %s", ansible_param1)
            log.info("ansible_param2: %s", ansible_param2)
            log.info("ansible_param3: %s", ansible_param3)

            log.info("contents of kwargs: {}".format(kwargs)) # kwargs: {'host': '192.168.1.2', 'playbook_name': 'playbook1'}

            username = self.options["username"]
            playbook_dir = self.options["playbook_dir"]
            #prepare host(s) arg
            host_arg = "{},".format(" ".join((host.split(',')))) # If there are multiple hosts  
            
            # prepare playbook arg
            playbook_extention = playbook_name.split('.')[len(playbook_name.split('.'))-1]
            if(playbook_extention != "yml"):
                playbook_name = "{}.yml".format(playbook_name)
            # check for playbook's availability in the dir
            os.chdir(playbook_dir)
            if playbook_name in os.listdir():
                target_playbook = '/'.join((playbook_dir, playbook_name))
            else:
                raise ValueError("Target playbook not present in following path: '%s'" %playbook_dir)
            
            # preparing command to execute
            command = ['ansible-playbook', "-i", host_arg, "-u", username, target_playbook]
            if(ansible_param1 or ansible_param2 or ansible_param3):
                command.insert(len(command)-1, "-e")
                playbook_extra_vars = "ansible_param1={} ansible_param2={} ansible_param3={}"
                command.insert(len(command)-1, playbook_extra_vars.format(ansible_param1, ansible_param2, ansible_param3))

            # Set up the environment
            env = os.environ.copy()

            # executing command
            tstart = time.time()
            process = Popen(command, stdout=PIPE, stderr=PIPE, shell=False, env=env)
            stdoutdata, stderrdata = process.communicate()
            retcode = process.returncode
            tend = time.time()
            
            # logging output in console
            log.info("stdout: %s", stdoutdata)
            log.info("stderr: %s", stderrdata)

            # Processing output
            encoding = chardet.detect(stdoutdata)["encoding"] or "utf-8"
            result = stdoutdata.decode(encoding)
            result_json = None
            try:
                # Let's see if the output can be decoded as JSON
                result_json = json.loads(result)
            except:
                pass

            output = stderrdata.decode(encoding)
            output_json = None
            try:
                # Let's see if the output can be decoded as JSON
                output_json = json.loads(output)
            except:
                pass
            
            
            results = {
                "start": int(tstart * 1000.0),
                "end": int(tend * 1000.0),
                "elapsed": int((tend - tstart) * 1000.0),
                "exitcode": retcode,  # Nonzero exit code indicates error
                "stdout": result,
                "stderr": output,
                "stdout_json": result_json,  # May be null
                "stderr_json": output_json  # May be null
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()