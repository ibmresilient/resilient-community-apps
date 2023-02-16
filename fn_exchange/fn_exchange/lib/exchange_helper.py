import re
import sys
import time
import logging
import exchangelib

from exchangelib import EWSTimeZone
from exchangelib.errors import ErrorFolderNotFound

PACKAGE_NAME =  "fn_exchange"
log = logging.getLogger(__file__)

class NoMailboxError(Exception):
    def __init__(self, email):
        fail_msg = 'The SMTP address {} has no mailbox associated with it'.format(email)
        log.error(fail_msg)
        super(NoMailboxError, self).__init__(fail_msg)


class ServerConnectionError(Exception):
    def __init__(self, server):
        fail_msg = 'Failed to connect to server: {}'.format(server)
        log.error(fail_msg)
        super(ServerConnectionError, self).__init__(fail_msg)


class CredentialsError(Exception):
    def __init__(self):
        fail_msg = 'The username or password specified in the config file is invalid'
        log.error(fail_msg)
        super(CredentialsError, self).__init__(fail_msg)


class FolderError(Exception):
    def __init__(self, email, folder, folder_path, tree):
        fail_msg = 'Either the user {} does not have access to the folder {} from the path {} or the folder does not ' \
                   'exist. See the above tree structure above for more information.'.format(email, folder, folder_path)
        log.error(fail_msg)
        log.error(tree)
        super(FolderError, self).__init__(fail_msg)

class ImpersonationError(Exception):
    def __init__(self, impersonator, impersonation_target):
        fail_msg = '{} does not have permission to impersonate {}'.format(impersonator, impersonation_target)
        log.error(fail_msg)
        super(ImpersonationError, self).__init__(fail_msg)


def get_timezone(format="Etc/GMT") -> EWSTimeZone:
    log.info(f"Setting Timezone to {format}")
    if sys.version_info.major <= 2:
        # Support for PY 2
        return EWSTimeZone.timezone(format)
    else:
        # Support for PY 3
        return EWSTimeZone(format)


def parse_time(epoch_time) -> list:
    """Convert epoch time in milliseconds to [year, month, day, hour, minute, second]"""
    date = time.strftime('%Y-%m-%d-%H-%M-%S', time.gmtime(epoch_time/1000))
    return [int(i) for i in date.split('-')]


def get_proxy_adapter(proxy_base_adapter, proxies):
    """ Factory function to set correct base adapter for proxy adapter.

    :param proxy_base_adapter: Base http adapter.
    :param proxies: Proxies dict.
    :return: Proxy adapter class.
    """
    class ProxyAdapter(proxy_base_adapter):
        def send(self, *args, **kwargs):
            kwargs['proxies'] = proxies
            return super(ProxyAdapter, self).send(*args, **kwargs)

    return ProxyAdapter



def go_to_folder(username, account, folder_path) -> exchangelib.folders:
    """Navigate to specified folder path and return it"""
    # Split the folder path by '/' preserving paths wrapped in quotes
    split_path = [path.strip('"') for path in re.findall('(?:[^/"]|"(?:\\.|[^"])*")+', folder_path)]

    account.root.refresh()
    folder = account.root

    if folder_path is None:
        return folder

    for dir in split_path:
        try:
            folder = folder / dir
        except ErrorFolderNotFound:
            raise FolderError(username, dir, folder_path, account.root.tree().encode('utf-8'))
    return folder
