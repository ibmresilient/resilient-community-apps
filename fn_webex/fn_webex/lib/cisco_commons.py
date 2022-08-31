from resilient_lib import IntegrationError

class ResponseHandler:

    def __init__(self):
        self.msg = None
        self.default_exempt_codes = [204]
        self.exempt_codes = self.default_exempt_codes


    def clear_exempt_codes(self):
        self.exempt_codes = self.default_exempt_codes


    def add_exempt_codes(self, codes):
        if isinstance(codes, int):
            self.exempt_codes.append(codes)
        elif isinstance(codes, list):
            self.exempt_codes.extend(codes)
        else:
            raise TypeError("Unsupported type supplied for codes in add_exemp_codes. Supported type <list> or <int>, type provided was {}".type(codes))


    def monitor_status(self):
        if self.response is None:
            raise IntegrationError("API call failed! Invalid METHOD passed to rc.execute()! Response returned was None")
        elif self.response.status_code == 204:
            self.msg = "API call successful! No content returned"
        elif self.response.status_code == 401:
            self.msg = "API call failed! Security context is invalid. API returned 401! {}".format(self.response.json().get("message"))
        elif self.response.status_code == 404:
            self.msg = "API call failed! Item not found. API returned 404! {}".format(self.response.json().get("message"))
        elif self.response.status_code == 405:
            self.msg = "API call failed! Method Not Allowed. API returned 405! {}".format(self.response.json().get("message"))


    def raise_or_return_erros(self):
        if self.msg: 
            if self.response.status_code in self.exempt_codes:
                if self.response.status_code == 204:
                    res = {}
                else:
                    res = self.response.json()
                res["status_code"] = self.response.status_code
                if self.msg:
                    res["message"] = self.msg
                return res
            else:
                raise IntegrationError(self.msg)
        else:
            res = self.response.json()
            res["status_code"] = self.response.status_code
            return res


    def check_response(self, response):
        self.response = None
        self.response = response
        self.monitor_status()
        return self.raise_or_return_erros()