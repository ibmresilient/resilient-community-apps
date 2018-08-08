class AuthenticatorBase(object):
    AUTHENTICATION_TYPES = {
        "apikey":   ["apikey"],
        "password": ["username", "password"]
    }
    AUTHENTICATION_TYPE = "apikey"

    def __init__(self, options):
        self.auth = {}
        self.get_auth_data(options)

    def get_auth_data(self, options):
        for inp in self.AUTHENTICATION_TYPES[self.AUTHENTICATION_TYPE]:
            self.auth[inp] = options.get("cf_api_"+inp, None)
            if self.auth[inp] is None:
                raise KeyError("cf_api_{} isn't specified in the config.".format(inp))

    def get_headers(self):
        raise NotImplementedError()
