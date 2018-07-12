# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
import docker
import base64
import os
import hashlib
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError

CONFIG_DATA_SECTION = 'thug'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function(s)"""

    def __init__(self, opts):
	super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})
	self.thug_dir = self.options.get("thug_dir")

    @function("thug")
    def _thug_function(self, event, *args, **kwargs):
        """Function: """
        try:
            # Get the function parameters:
            art_val = kwargs.get("thug_url")  # text

            log = logging.getLogger(__name__)

	    thug_dir = self.thug_dir
            
	    def md5(my_val):
                """ Creates an MD5 from given value"""
                m_val = hashlib.md5()
                m_val.update(my_val)
                return m_val.hexdigest()
	    
	    art_val_md5 = md5(art_val)
    
	    # Setup a connection to docker
            try:
                client = docker.from_env()
                yield StatusMessage("Testing docker connection")
                client.info()
            except docker.errors.APIError:
                yield StatusMessage("Docker is not installed or started")
        
            # Check we have our thug image 
            try: 
                client.images.get('honeynet/thug:latest')
                yield StatusMessage("Docker image found")
            # handle no image
            except docker.errors.ImageNotFound:
                yield StatusMessage("Docker image not found")
                yield StatusMessage("Getting thug image")
                # go grab image
                try: 
                        client.images.pull('honeynet/thug:latest')
                # handle download or API error
                except docker.errors.APIError:
                        yield StatusMessage("Couldn't download the image")

            # Runs the thug analysis tool in a docker
            client = docker.from_env()
            thug_logs = {thug_dir: {'bind': '/logs', 'mode': 'rw'}}
            command = "python /opt/thug/src/thug.py -FZM " + art_val
            yield StatusMessage("Running analysis on " + art_val)
            try: 
                thug_docker = client.containers.run('honeynet/thug', volumes=thug_logs, command=command, detach=True)
                thug_docker_id = thug_docker.id
                yield StatusMessage("Running in docker " + thug_docker_id)
                thug_docker.wait()
                yield StatusMessage("Thug has completed running in Docker")
                thug_docker.remove()
            except docker.errors.ContainerError: 
                yield StatusMessage("Some error happened during the analysis")

           # Can probably make the file path stuff cleaner but shrug
            site_analysis_dir = os.path.join(self.thug_dir, art_val_md5)
            all_analysis_dir = os.listdir(site_analysis_dir)
            wanted_analysis_dir = all_analysis_dir[-1]
            log.info("Using analysis in folder " + wanted_analysis_dir)
            wanted_analysis_path = os.path.join(self.thug_dir, art_val_md5, wanted_analysis_dir,'analysis')
        

            yield StatusMessage("Encoding files for transmission")
            graph_path = os.path.join(wanted_analysis_path, 'graph.svg')
	    with open(graph_path, "rb") as f:
		data = f.read()
		thug_png_b64 = base64.b64encode(data)        

            json_path = os.path.join(wanted_analysis_path, 'json', 'analysis.json')
	    with open(json_path, "rb") as f:
	   	data = f.read()
		thug_report_b64 = base64.b64encode(data)
           
	    results = {
                "png_file": thug_png_b64,
		"report_file": thug_report_b64
             }

            
	    yield StatusMessage("Response values sent")
	    # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
