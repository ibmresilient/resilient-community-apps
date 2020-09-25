from resilient_lib import validate_fields, RequestsCommon, str_to_bool

def validate(options):
    """
    validate API_KEY, URL, and VERIFY_CERT
    :param options: function options from app.config
    :return
    """
    validate_fields([
        {"name": "misp_key", "placeholder": "http://localhost"},
        {"name": "misp_url", "placeholder": "<your key>"},
        {"name": "verify_cert"}
    ], options)
    key = options.get('misp_key')
    url = options.get('misp_url')
    verify = str_to_bool(options.get("verify_cert"))
    return key, url, verify

def get_proxies(opts, options):
    rc = RequestsCommon(opts, options)
    proxies = rc.get_proxies()
    return proxies
