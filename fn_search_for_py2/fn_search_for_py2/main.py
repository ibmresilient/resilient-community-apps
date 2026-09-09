# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# pragma pylint: disable=line-too-long, wrong-import-order

from argparse import ArgumentParser, Namespace
from pathlib import Path
from zipfile import ZipFile, is_zipfile

import base64
import os
import json
import sys

from fn_search_for_py2.lib.common import FindPY2
from fn_search_for_py2.lib.soar_helper import SOARHelper
from fn_search_for_py2.lib.common import EXPORT_RES, RES_EXT, RESZ_EXT, IMPORT_DEFINITION, EXPORT_RES_PATH, \
    SCRIPT_TEXT, SCRIPTS_PATH, SCRIPTS_LOCAL_PATH, PLAYBOOKS_PATH, WORKFLOWS_PATH

import pkg_resources  # part of setuptools

version = pkg_resources.require("fn_search_for_py2")[0].version

def print_error(msg: str):
    print(f"Error: {msg}. Exiting.")
    sys.exit(1)

class FindPY2_APP(FindPY2):
    def __init__(self, args: Namespace):
        super().__init__(None)
        self.export_res = None

        if not os.path.exists(args.file):
            print_error(f"File does not exist: {args.file}")

        # export.res file already in json format
        _file_root, ext = os.path.splitext(args.file)
        if RES_EXT == ext:
            with open(args.file, "r", encoding="utf-8") as f:
                self.export_res = json.load(f)

        elif RESZ_EXT == ext:
            try:
                with ZipFile(args.file, 'r') as zip_ref:
                    if not EXPORT_RES in zip_ref.namelist():
                        print_error(f"{EXPORT_RES} not found in {args.file}")

                    self.export_res = json.loads(zip_ref.read(EXPORT_RES).decode('utf-8'))
            except KeyError:
                return None

        elif "customize.py" in args.file:
            # older customize.py files have embedded base64 encoded version of export.res
            with open(args.file, "r", encoding="utf-8") as f:
                export_res_customize = f.read()

            # older embedded code?
            match = IMPORT_DEFINITION.search(export_res_customize)
            if match:
                self.export_res = json.loads(base64.b64decode(match.group(1)))
            # newer logic referencing export.res file?
            elif EXPORT_RES_PATH in export_res_customize:
                # change the file_path to the export.res file for lookup
                file_path = os.path.join(os.path.dirname(args.file), EXPORT_RES_PATH)
                with open(args.file, "r", encoding="utf-8") as f:
                    self.export_res = json.load(f)
            else:
                # not clear what's needed
                print_error(f"No embedded {EXPORT_RES} data in file: {args.file}")

        else:
            print_error(f"Unrecognized file name: {args.file}")

    def get_script_content(self, _element_id, element):
        return element.get(SCRIPT_TEXT)

    def analyze_scripts(self, inputs):
        """list scripts by id, programmatic_name"""
        scripts_json = self.export_res.get(SCRIPTS_PATH) if self.export_res.get(SCRIPTS_PATH) else []
        scripts_local_json = self.get_local_scripts(self.export_res)
        return self._analyze_scripts(self.filter_on_tags(inputs.get("py2_search_tags"), None, scripts_json + scripts_local_json))

    def analyze_workflows(self, inputs):
        workflow_json = self.export_res.get(WORKFLOWS_PATH) if self.export_res.get(WORKFLOWS_PATH) else {}
        return self._analyze_workflows(self.filter_on_tags(inputs.get("py2_search_tags"), None, workflow_json))

    def analyze_playbooks(self, inputs):
        playbook_json = self.export_res.get(PLAYBOOKS_PATH) if self.export_res.get(PLAYBOOKS_PATH) else {}
        return self._analyze_playbooks(self.filter_on_tags(inputs.get("py2_search_tags"), None, playbook_json))
    
    def get_local_scripts(self, export_res):
        local_scripts = []
        for playbook in export_res.get(PLAYBOOKS_PATH, []):
            if playbook.get(SCRIPTS_LOCAL_PATH):
                local_scripts += playbook.get(SCRIPTS_LOCAL_PATH)

        return local_scripts
    def get_script_by_uuid(self, wrkflw_plybk: dict, script_uuid: str) -> dict:
        """find the script within the existing export.res file

        :param script_uuid: search for 
        :type script_uuid: str
        :return: found script or None
        :rtype: dict
        """
        # is it in "local_scripts"
        for script in wrkflw_plybk.get("local_scripts", []):
            if script.get("uuid") == script_uuid:
                return script

        for script in self.export_res.get("scripts", []):
            if script.get("uuid") == script_uuid:
                return script

        return None

#-----

def parse_args(*args):
    """parse arguments to this app such as:
        - existing export.res file
        - whether to convert the file

    :return: parsed arguments
    :rtype: arg_parser.Namespace
    """
    arg_parser = ArgumentParser()
    arg_parser.add_argument("file",
                            nargs='?',
                            help="existing customization.py, export.res or export.resz file")
    arg_parser.add_argument("-s", "--scripts",
                            action='store_true',
                            default=False,
                            required=False,
                            help="Review scripts only")
    arg_parser.add_argument("-w", "--workflows",
                            action='store_true',
                            default=False,
                            required=False,
                            help="Review workflows only")
    arg_parser.add_argument("-p", "--playbooks",
                            action='store_true',
                            default=False,
                            required=False,
                            help="Review playbooks only")
    arg_parser.add_argument("-t", "--tags",
                            help="comma separated list of app tags to filter",
                            default=None,
                            required=False)

    return arg_parser.parse_args(args)

# S T A R T
PY2_LOOKUP = {
  "PY2_UNCONVERTIBLE": "Python 2 execution found, but script complexity prevents further analysis. Please review and, in some cases, changing the setting to Python 3 is the only change needed.",
  "PY2_CONVERTIBLE": "{item_type} set to run Python 2. This {item_type} can be easily changed to use Python 3. Check function input scripts, local scripts, and scripts used in conditions. Mostly likely the only change needed is to convert all language settings to Python 3.",
  "PY2_ITERS": "Python 2 iters found. Convert to use .items(), .keys(), and .values() as appropriate",
  "PY2_JAVA_UTIL_DATE": "'import java.util.Date' found. Change to 'from datetime import datetime' and datetime functions such as 'datetime.now()'.",
  "PY2_UNICODE": "Unicode strings found ('u' string prefix). This can remain for Python 3, but it's cleaner to remove."
}

def main():
    """ parse the input parameters and kick off the tool """
    args = parse_args(*sys.argv[1:])
    find_py2 = FindPY2_APP(args)

    item_type = "all"
    if args.scripts:
        item_type = "script" 
    elif args.workflows:
        item_type = "workflow"
    elif args.playbooks:
        item_type = "playbook"
    inputs = {
        "py2_item_type": item_type,
        "py2_search_tags": args.tags
    }
    py2_results  = find_py2.start(inputs)

    first_pass = True
    for item_type in ["script", "workflow", "playbook"]:
        for item_id, item in py2_results.get(item_type).items():
            if first_pass:
                first_pass = False
                print("\nPython 2 findings\n")

            print("{hdr}{value}".format(hdr="Id:".ljust(13), value=item_id))
            print("{hdr}{value}".format(hdr="Type:".ljust(13), value=item_type))
            name = item.get("display_name") if item.get("display_name") else item.get("name")
            print("{hdr}{value}".format(hdr="Name:".ljust(13), value=name))
            print("{hdr}{value}".format(hdr="App Tags:".ljust(13), value=", ".join([str(tag.get("tag_handle"))  for tag in item.get("tags", [])])))
            print("{hdr}{value}".format(hdr="Components:".ljust(13), value=", ".join(item.get("components", []))))
            print("Notes:")
            for attr in item.get("attributes"):
                print(PY2_LOOKUP.get(attr).format(item_type=item_type.title()))
            print("-----\n")

    if first_pass:
        print("\nNo Python 2 scripting found.")

if __name__ == "__main__":
    main()
