# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.

import resilient_lib


class ResDockerHelper:

    def __init__(self, options):
        self.options = options

    def get_function_input(inputs, input_name, optional=False):
        """Given input_name, checks if it defined. Raises ValueError if a mandatory input is None"""
        the_input = inputs.get(input_name)

        if the_input is None and optional is False:
            err = "'{0}' is a mandatory function input".format(input_name)
            raise ValueError(err)
        else:
            return the_input

    def get_config_option(self, option_name, optional=False):
        """Given option_name, checks if it is in app.config. Raises ValueError if a mandatory option is missing"""
        option = self.options.get(option_name)

        if option is None and optional is False:
            err = "'{0}' is mandatory and is not set in app.config file. You must set this value to run this function properly".format(
                option_name)
            raise ValueError(err)
        else:
            return option

    def get_image_specific_config_option(self, options, option_name, optional=False):
        """Given option_name, checks if it is in app.config. Raises ValueError if a mandatory option is missing"""
        option = options.get(option_name)

        if option is None and optional is False:
            err = "'{0}' is mandatory and is not set in app.config file. You must set this value to run this function properly".format(
                option_name)
            raise ValueError(err)
        else:
            return option

    def merge_two_dicts(self, x, y):
        z = x.copy()  # start with x's keys and values
        z.update(y)  # modifies z with y's keys and values & returns None
        return z

    def prepare_res_link(self,incident_id, host, task_id=None):
        link = "https://{0}/#incidents/{1}".format(host, incident_id)

        if task_id is not None:
            link += "?task_id={0}".format(task_id)

        return link


    def prepare_attachment_link(self,host, org_id, attachment_id, incident_id, task_id=None):
        param = ("tasks",task_id) if task_id else ("incidents",incident_id)

        link = "https://{host}/rest/orgs/{org_id}/{object}/{object_id}/attachments/{attach_id}/contents".format(
            host=host, org_id=org_id, object=param[0], object_id=param[1], attach_id=attachment_id)

        return link

