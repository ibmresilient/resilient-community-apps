# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
from netmiko import ConnectHandler


def execute(opts, net_cmd, net_config, device_commit, use_textfsm):
    """
    This function setups up a netmiko connection and performs the different commands.
    The results are returned in a json document
    :param opts:
    :param net_cmd:
    :param net_config:
    :param device_commit: used with net_config cmds
    :param use_textfsm: used with net_cmd to specify the results should be formatted through TextFSM
    :return: json results such as:
      {
        'status': 'success'|'failure',
        'reason': xx,
        'send_command': xx,
        'send_result': xx,
        'config_command': xx,
        'config_result': xx
      }
    """
    result = {}
    connection = None
    try:
        # if secret is specified, use enable_mode
        bEnable_mode = len(opts.get('secret', '')) > 0

        connection = ConnectHandler(**opts)

        if bEnable_mode:
            connection.enable()

        # standard commands to execute
        if net_cmd:
            result['send_command'] = net_cmd
            send_result = connection.send_command(net_cmd, use_textfsm=use_textfsm)
            result['send_result'] = send_result

        # configuration commands to execute
        if net_config:
            result['config_command'] = net_config
            config_result = connection.send_config_set(net_config.split("\n"))
            result['config_result'] = config_result
            if device_commit:
                connection.commit()

        result['status'] = 'success'
    except Exception as err:
        result['status'] = 'failure'
        result['reason'] = str(err)

    finally:
        if connection:
            if bEnable_mode:
                connection.exit_enable_mode()

            connection.disconnect()

    return result
