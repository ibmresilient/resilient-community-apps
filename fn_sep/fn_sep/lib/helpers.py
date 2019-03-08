# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

""" Helper functions for Resilient circuits Functions supporting Symantec SEP """

from __future__ import print_function
import logging
import re
from textwrap import dedent

LOG = logging.getLogger(__name__)


def transform_kwargs(kwargs):
    """"Update kwargs dictionary.

    :param kwargs: Dictionary of Resilient Function parameters.

     """

    # Remove  "sep_" from the kwargs key names.
    for (k, v) in kwargs.copy().items():
            kwargs[re.split('_', k, 1)[1]] = kwargs.pop(k)

    # If any entry has "None" string change to None value.
    for k, v in kwargs.items():
        if type(v) == str and v.lower() == 'none':
            kwargs[k] = None

def setup_eoc_command(scan_type, file_name, sha256, description):
    eoc_xml = dedent("""\
        <?xml version="1.0" encoding="UTF-8"?>
        <EOC creator="Creator" version="1.1" id="60">
          <DataSource name="Third-Party Provider" id="23" version="1.0"/>
          <ScanType>{0}</ScanType>
          <Threat category="Suspects" type="to_investigate" severity="Medium" time="2017-01-29 4:54:01 PM">
            <Description>{}</Description>
            <Attacker>
            </Attacker>
          </Threat>
          <Activity>
            <OS id="1" name="" version="" patch="">
              <Process>
              </Process>
              <Files>
                <File name="{1}" action="write">
                  <Hash name="SHA256" value="{2}"/>
                </File>
              </Files>
              <Registry>
              </Registry>
              <Network>
              </Network>
            </OS>ß
          </Activity>
        </EOC>""").format(scan_type, file_name, sha256)

    return eoc_xml