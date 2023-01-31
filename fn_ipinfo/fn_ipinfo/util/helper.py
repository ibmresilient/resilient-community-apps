import ipaddress
import sys

class IpInfoHelper():
    """Helper Functions """

    def is_valid_ipv4_addr(self, ip):
        """ A custom Jinja filter function which determines if input is an IPV4 Address"""
        try:
            return isinstance(ipaddress.ip_address(ip), ipaddress.IPv4Address)
        except Exception as e:
            return False

    def is_valid_ipv6_addr(self, ip):
        """ A custom Jinja filter function which determines if input is an IPV6 Address"""
        try:
            return isinstance(ipaddress.ip_address(ip), ipaddress.IPv6Address)
        except Exception as e:
            return False

    def get_config_option(self, option_name, options, optional=False):
        """Given option_name, checks if it is in app.config. Raises ValueError if a mandatory option is missing"""
        option = options.get(option_name)

        if not option and optional is False:
            err = "'{0}' is mandatory and is not set in app.config file. You must set this value to run this function properly".format(
                option_name)
            raise ValueError(err)
        else:
            return option

    def get_ipinfo_qry_ip(self, ip):

        if sys.version_info > (3, 0):
            return ip
        else:
            return unicode(ip)
