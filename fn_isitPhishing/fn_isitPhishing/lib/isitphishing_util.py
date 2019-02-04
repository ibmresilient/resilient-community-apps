import sys
import base64

def get_license_key(name, license):

    # Compute the base64 license key. This key will be provided to you by Vade Secure,
    # and has the following format: <CUSTOMER_NAME>:<CUSTOMER_LICENSE>.
    url_key = u'{0}:{1}'.format(name, license)

    # It must be Base64-encoded. Handled different on Python 2 vs 3.
    if sys.version_info[0] == 2:
        auth_token = base64.b64encode(bytes(url_key).encode("utf-8"))
    else:
        auth_token = base64.b64encode(bytes(url_key, 'ascii')).decode('ascii')
 
    return auth_token