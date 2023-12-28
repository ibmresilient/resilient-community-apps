# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

"""AppFunction implementation"""
from io import BytesIO
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, write_file_attachment
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import WebDriverException

PACKAGE_NAME = "fn_snapshot_url"
FN_NAME = "snapshot_url"

def firefox_setup(options):
    """configure the options needed for firefox operation, such as headless operation

    :return: option settings
    :rtype: FirefoxOptions
    """
    firefox_options: webdriver.FirefoxOptions = webdriver.FirefoxOptions()
    firefox_options.add_argument("-headless")

    if options.get("proxy_server"):
        firefox_options.add_argument(f'--proxy-server={options.get("proxy_server")}')

    return firefox_options


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'snapshot_url'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: None
        Inputs:
            -   fn_inputs.snapshot_url
            -   fn_inputs.snapshot_incident_id
            -   fn_inputs.snapshot_timeout
            -   fn_inputs.snapshot_fullpage
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        # Example validating required fn_inputs
        validate_fields(["snapshot_url", "snapshot_incident_id"], fn_inputs)

        try:
            # setup the driver and take the snapshot
            driver: webdriver.Firefox = webdriver.Firefox(options=firefox_setup(self.options))

            if hasattr(fn_inputs, "snapshot_timeout"):
                driver.set_page_load_timeout(fn_inputs.snapshot_timeout)

            driver.get(fn_inputs.snapshot_url)
            if getattr(fn_inputs, "snapshot_fullpage", False):
                png_bytes = driver.get_full_page_screenshot_as_png()
            else:
                png_bytes = driver.get_screenshot_as_png()

            bytes_io = BytesIO(png_bytes)

            attachment_name = f"{fn_inputs.snapshot_url}.png"
            write_file_attachment(self.rest_client(),
                                  attachment_name,
                                  bytes_io,
                                  fn_inputs.snapshot_incident_id,
                                  content_type="image/png")
            result = {
                "attachment_name": attachment_name
            }
            reason = None
        except WebDriverException as err:
            result = {}
            reason = f"failed to access: {fn_inputs.snapshot_url}. Error: {str(err)}"
        except Exception as err2:
            result = {}
            reason = f"failed to process: {fn_inputs.snapshot_url}. Error: {str(err2)}"
        finally:
            if "driver" in locals():
                driver.quit()

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(result, success=True if result else False, reason=reason)
