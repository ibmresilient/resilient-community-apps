import re
import sys
import time
import logging
import exchangelib

from exchangelib import EWSTimeZone
from exchangelib.errors import ErrorFolderNotFound
from resilient_lib import ResultPayload

from resilient_circuits import FunctionResult

PACKAGE_NAME =  "fn_exchange"
log = logging.getLogger(__file__)


#function_parameters["recipients"]  = getattr(fn_inputs, "exchange_emails", None)
        
INPUTS_MAP = {
    "exchange_email"                   : "username",
    "exchange_num_emails"              : "num_emails",
    "exchange_email_ids"               : "email_ids",
    
    "exchange_meeting_start_time"      : "start_time",
    "exchange_meeting_end_time"        : "end_time",
    "exchange_meeting_subject"         : "meeting_subject",
    "exchange_meeting_body"            : "meeting_body",
    "exchange_required_attendees"      : "required_attendees",
    "exchange_optional_attendees"      : "optional_attendees",
    "exchange_is_online_meeting"       : "is_online_meeting",
    "exchange_meeting_location"        : "meeting_location",
    
    "exchange_sender"                  : "sender",
    "exchange_email_recipients"        : "recipients",
    "exchange_message_subject"         : "msg_subject",
    "exchange_message_body"            : "msg_body",
    "exchange_start_date"              : "start_date",
    "exchange_end_date"                : "end_date",
    
    "exchange_hard_delete"             : "hard_delete",
    "exchange_has_attachments"         : "has_attachments",
    "exchange_order_by_recency"        : "order_by_recency",
    "exchange_search_subfolders"       : "search_subfolders",
    "exchange_folder_path"             : "src_folder",
    "exchange_destination_folder_path" : "dst_folder",
    "exchange_get_email"               : "mailbox_id",
    "exchange_delete_source_folder"    : "delete_src_folder",
    "exchange_force_delete_subfolders" : "force_delete"}



class ResultsHandler(ResultPayload):
    """
    A wrapper class that modifies the results that are returned to allow for 
    backwards comparability. This function returns results as a named tuple and 
    also encloses a copy of the results as an element.
    """
    def __init__(self, package_name, fn_inputs):
        super(ResultsHandler, self).__init__(pkgname=package_name, inputs=fn_inputs._asdict())

    def success(self, content):
        results = self.done(success=True, content=content)
        results.update(content)
        return FunctionResult(results, custom_results=True)

    def fail(self, reason):
        results = self.done(success=False, reason=reason, content={})
        return FunctionResult(results, custom_results=True)


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


def get_timezone(format) -> EWSTimeZone:
    if not format:
        format = "Etc/GMT"
    else:
        format = format.strip()
    log.info(f"Setting Timezone to {format}")
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
