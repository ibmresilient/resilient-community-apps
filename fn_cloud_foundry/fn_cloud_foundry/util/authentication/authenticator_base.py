class AuthenticatorBase(object):
    """
    Base class, essentially an interface for writing an Authenticator class.
    authenticate and get_headers will need to be implemented by them.
    Currently supports 2 authentication types - apikey and password, which in turn simply
    specify what data should be used from app.config to authenticate.
    """
    AUTHENTICATION_TYPES = {
        "apikey":   ["apikey"],
        "password": ["username", "password"]
    }
    AUTHENTICATION_TYPE = "apikey"

    def __init__(self, options):
        self.auth = {}
        self._get_auth_data(options)

    def _get_auth_data(self, options):
        for inp in self.AUTHENTICATION_TYPES[self.AUTHENTICATION_TYPE]:
            self.auth[inp] = options.get("cf_api_"+inp, None)
            if self.auth[inp] is None:
                raise KeyError("cf_api_{} isn't specified in the config.".format(inp))

    def authenticate(self):
        """
        Abstracts out the authentication specifics.
        """
        raise NotImplementedError()

    def get_headers(self):
        raise NotImplementedError()
