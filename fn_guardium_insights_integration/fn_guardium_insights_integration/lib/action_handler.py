# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

import threading

import six


class ActionHandlerThread(threading.Thread):
    """
    A Module to handle Threads
    """

    def __init__(self, function_object):
        if six.PY3:
            threading.Thread.__init__(self, daemon=False)
        elif six.PY2:
            threading.Thread.__init__(self)
        self.call_function = function_object
        self.output = None

    def run(self):
        self.output = self.call_function(self)


def spawn_single_thread_controller(call_function, *args, **kwargs):
    """
    A method create a single thread for each call
    :param call_function: Object of the function to be called by using thread.
    :param args: function argument depends on the caller function
    :param kwargs: function argument depends on the caller function
    :return: Created thread object
    """
    thread_object = ActionHandlerThread(lambda r: call_function(*args, **kwargs))
    if six.PY2:
        thread_object.setDaemon(False)
    thread_object.start()
    return thread_object


def thread_controller(function_object, data, *args, **kwargs):
    """
    :param function_object: Object of the function to be called by using thread.
    :param data: to be processed, should be list type
    :param args: function argument depends on the caller function
    :param kwargs:function argument depends on the caller function
    :return:
    """
    if not isinstance(data, list):
        raise TypeError("Process data should list type.")

    __tmp_threads_list = []
    output_holder = []

    for d_in in data:
        thread_object = ActionHandlerThread(lambda r: function_object(d_in, *args, **kwargs))
        if six.PY2:
            thread_object.setDaemon(False)
        thread_object.start()
        __tmp_threads_list.append(thread_object)

        if len(__tmp_threads_list) == 5:
            for t_obj in __tmp_threads_list:
                t_obj.join()
                if t_obj.output:
                    output_holder.append(t_obj.output)
            __tmp_threads_list = []
    if __tmp_threads_list:
        for t_obj in __tmp_threads_list:
            t_obj.join()
            if t_obj.output:
                output_holder.append(t_obj.output)
    return output_holder
