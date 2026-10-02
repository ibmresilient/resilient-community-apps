# -*- coding: utf-8 -*-
"""Helper for tests"""

PACKAGE_NAME = "fn_ansible"

def run_ansible_module_results():
    return {
        "52": {
            "summary": "successful",
            "detail": "\u001b[1;35m[WARNING]: No inventory was parsed, only implicit localhost is available\u001b[0m"
        },
        "localhost": {
            "summary": "successful",
            "detail": {
                "changed": True,
                "stdout": "Hello World!",
                "stderr": "",
                "rc": 0,
                "cmd": ["echo","Hello","World!"],
                "start": "2024-03-19 14:17:15.087091",
                "end": "2024-03-19 14:17:15.149417",
                "delta": "0:00:00.062326",
                "msg": "",
                "invocation": {
                    "module_args": {
                        "_raw_params": "echo Hello World!",
                        "_uses_shell": False,
                        "expand_argument_vars": True,
                        "stdin_add_newline": True,
                        "strip_empty_ends": True,
                        "argv": None,
                        "chdir": None,
                        "executable": None,
                        "creates": None,
                        "removes": None,
                        "stdin": None
                    }
                },
                "stdout_lines": ["Hello World!"],
                "stderr_lines": [],
                "_ansible_no_log": False
            }
        }
    }

def run_ansible_playbook_results():
    return {
        "63": {
            "summary": "successful",
            "detail": "\u001b[1;35mthe implicit localhost does not match 'all'\u001b[0m"
        },
        "127.0.0.1": {
            "summary": "successful",
            "detail": {
                "changed": True,
                "stdout": "Hello",
                "stderr": "",
                "rc": 0,
                "cmd": ["echo", "Hello"],
                "start": "2024-03-19 14:31:34.876667",
                "end": "2024-03-19 14:31:34.888730",
                "delta": "0:00:00.012063",
                "msg": "",
                "invocation": {
                    "module_args": {
                        "_raw_params": "echo Hello",
                        "_uses_shell": False,
                        "expand_argument_vars": True,
                        "stdin_add_newline": True,
                        "strip_empty_ends": True,
                        "argv": None,
                        "chdir": None,
                        "executable": None,
                        "creates": None,
                        "removes": None,
                        "stdin": None
                    }
                },
                "stdout_lines": ["Hello"],
                "stderr_lines": [],
                "_ansible_no_log": False
            }
        }
    }

