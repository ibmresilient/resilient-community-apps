from resilient_lib import validate_fields, RequestsCommon

def validate(options):
    """
    validate API_KEY, URL, and VERIFY_CERT
    :param options: function options from app.config
    :return
    """
    validate_fields(['misp_key', 'misp_url', 'verify_cert'], options)
    key = options.get('misp_key')
    url = options.get('misp_url')
    verify = True if options.get('verify_cert').lower() == "true" else False
    return key, url, verify

def get_proxies(opts, options):
    rc = RequestsCommon(opts, options)
    proxies = rc.get_proxies()
    return proxies
