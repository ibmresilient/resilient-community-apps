from exchangelib import Credentials, Account, DELEGATE, Configuration, EWSDateTime, EWSTimeZone, Message
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
import time

class exchange_utils:
    def __init__(self, **kwargs):
        self.cert_verify = kwargs.get('cert_verify')
        self.server = kwargs.get('server')
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
        self.default_folder_path = kwargs.get('default_folder_path')
        self.default_timezone = kwargs.get('default_timezone')

    def connect_to_account(self, primary_smtp_address):
        """Connect to specified account and return it"""

        # Don't check certificates
        if not self.cert_verify:
            BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

        # Use credentials to get account
        credentials = Credentials(username=self.username, password=self.password)
        config = Configuration(server=self.server, credentials=credentials)
        account = Account(primary_smtp_address=primary_smtp_address, config=config,
                          autodiscover=self.cert_verify, access_type=DELEGATE)
        return account

    def go_to_folder(self, username, folder_path):
        """Navigate to specified folder path and return it"""

        account = self.connect_to_account(username)
        folder = account.root
        for dir in folder_path.split('/'):
            folder = folder / dir
        return folder

    def get_emails(self, username, folder_path=None,
                   sender=None, start_date=None, end_date=None):
        """Get queried emails"""

        folder_path = self.default_folder_path if folder_path is None else folder_path

        folder = self.go_to_folder(username, folder_path)
        filtered_emails = folder.all()

        # filter by sender
        if sender:
            filtered_emails = filtered_emails.filter(sender=sender)

        # filter by date
        if start_date:
            # get YYYY/MM/DD from epoch time in milliseconds
            start_date = str(time.strftime('%Y-%m-%d', time.gmtime(start_date/1000.0)))
            start_date = [int(i) for i in start_date.split('-')]

            tz = EWSTimeZone.timezone(self.default_timezone)
            start = tz.localize(EWSDateTime(start_date[0], start_date[1], start_date[2]))
            filtered_emails = filtered_emails.filter(datetime_received__gte=start)
        if end_date:
            # get YYYY/MM/DD from epoch time in milliseconds
            end_date = str(time.strftime('%Y-%m-%d', time.gmtime(end_date/1000.0)))
            end_date = [int(i) for i in end_date.split('-')]

            tz = EWSTimeZone.timezone(self.default_timezone)
            end = tz.localize(EWSDateTime(end_date[0], end_date[1], end_date[2]))
            filtered_emails = filtered_emails.filter(datetime_received__lte=end)

        return filtered_emails