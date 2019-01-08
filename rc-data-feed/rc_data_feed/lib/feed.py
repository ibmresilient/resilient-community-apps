

class FeedContext(object):
    """This is a simple data structure used to hold things needed by the different feed destination classes."""
    def __init__(self, type_info, inc_id, rest_client, is_deleted):
        self.type_info = type_info
        self.rest_client = rest_client
        self.inc_id = inc_id
        self.is_deleted = is_deleted


class FeedDestinationBase(object):
    """Base class for all feeds."""
    def __init__(self):
        pass

    def send_data(self, context, payload):
        """Subclasses have to implement this.  It's where all the work happens (it's where the data gets written
        to the destination."""
        raise NotImplemented

