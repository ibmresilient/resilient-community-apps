class WorkflowStatus(object):
    """Class to handle the status of a Workflow Instance"""
    def __init__(self):
        self.instance_id = 98765432
        self.status = "running"
        self.start_date = 1648133974233
        self.end_date = None
        self.reason = None
        self.is_terminated = False

    def as_dict(self):
        return {}