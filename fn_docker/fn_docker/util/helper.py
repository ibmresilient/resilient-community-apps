# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
import time
class ResDockerHelper:

    def __init__(self, options):
        self.options = options

    @staticmethod
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

    @staticmethod
    def get_image_specific_config_option(options, option_name, optional=False):
        """Given option_name, checks if it is in app.config. Raises ValueError if a mandatory option is missing"""
        option = options.get(option_name)

        if option is None and optional is False:
            err = "'{0}' is mandatory and is not set in app.config file. You must set this value to run this function properly".format(
                option_name)
            raise ValueError(err)
        else:
            return option

    @staticmethod
    def merge_two_dicts(x, y):
        """
        :param x:
        :param y:
        :return:
        """
        z = x.copy()  # start with x's keys and values
        z.update(y)  # modifies z with y's keys and values & returns None
        return z

    @staticmethod
    def prepare_res_link(incident_id, host, task_id=None):
        """
        :param incident_id:
        :param host:
        :param task_id:
        :return:
        """
        link = "https://{0}/#incidents/{1}".format(host, incident_id)

        if task_id is not None:
            link += "?task_id={0}".format(task_id)

        return link

    @staticmethod
    def prepare_attachment_link(host, org_id, attachment_id, incident_id, task_id=None):
        """
        :param host:
        :param org_id:
        :param attachment_id:
        :param incident_id:
        :param task_id:
        :return:
        """
        param = ("tasks", task_id) if task_id else ("incidents", incident_id)

        link = "https://{host}/rest/orgs/{org_id}/{object}/{object_id}/attachments/{attach_id}/contents".format(
            host=host, org_id=org_id, object=param[0], object_id=param[1], attach_id=attachment_id)

        return link

    @staticmethod
    def format_result_attachment_name(image_name, container_id):
        """
        Format the new attachment name
        If artfiact append the type and artifact value
        If attachment append the attachment name


        :param attachment_name
        :param docker_artifact_type
        :param docker_input
        :param image_to_use
        """

        attachment_name = u"""Docker {} output for container {}.txt""".format(image_name, container_id[:12])
        return attachment_name

    @staticmethod
    def format_output_attachment_body(container_id, docker_operation, new_attachment_name,
                                      docker_artifact_type, docker_input, container_logs,
                                      timestamp):
        """
        A function that is used to increase the amount of information returned back to resilient as an attachment
        Instead of just providing the logs/output we can include the container_id and what we used as an input

        The functions main purpose is to prepare a body text so the main operations done are string manipulation
        Keyword arguements are used on the format() function in the hopes it makes the logic more readable.

        :param container_id:
        :param docker_operation:
        :param new_attachment_name:
        :param container_logs:
        :return:
        """

        new_attachment_body = u"""Docker Logs from Container : {container_id} \n Integration Server Time {timestamp}\n{operation}{input_to_container}\nOutput from Container : \n{container_logs}""".format(
            container_id=container_id,
            timestamp=time.strftime('%Y-%m-%d %H:%M', time.localtime(timestamp/1000)),
            input_to_container=u"""Performed on Attachment : {attachment_name}""".format(
                attachment_name=new_attachment_name)
            if new_attachment_name
            else u"""Performed on {artifact_type} : {artifact_value}""".format(
                artifact_type=docker_artifact_type, artifact_value=docker_input),
            operation=u"Operation Performed : {}\n\n".format(
                docker_operation) if docker_operation else u"\n\n",
            container_logs=container_logs)

        return new_attachment_body
