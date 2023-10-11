# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
import sys
import abc

# There is a difference between have abstract base classes are handled in py 2 and 3
# In python 3 we can directly access abc.ABC and inherit from that
# In python 2 we must create the ABC class using abc.ABCMeta
if sys.version_info >= (3, 4):
    ABC = abc.ABC
else:
    ABC = abc.ABCMeta

class RemedyAPI(ABC):

    @abc.abstractmethod
    def get_token(self, *args, **kwargs):
        raise NotImplementedError("Child classes must implement all methods of the RemedyAPI interface.")

    @abc.abstractmethod
    def build_request_headers(self, *args, **kwargs):
        raise NotImplementedError("Child classes must implement all methods of the RemedyAPI interface.")

    @abc.abstractmethod
    def release_token(self, *args, **kwargs):
        raise NotImplementedError("Child classes must implement all methods of the RemedyAPI interface.")

    @abc.abstractmethod
    def create_form_entry(self, *args, **kwargs):
        raise NotImplementedError("Child classes must implement all methods of the RemedyAPI interface.")

    @abc.abstractmethod
    def get_form_entry(self, *args, **kwargs):
        raise NotImplementedError("Child classes must implement all methods of the RemedyAPI interface.")

    @abc.abstractmethod
    def update_form_entry(self, *args, **kwargs):
        raise NotImplementedError("Child classes must implement all methods of the RemedyAPI interface.")

    @abc.abstractmethod
    def delete_form_entry(self, *args, **kwargs):
        raise NotImplementedError("Child classes must implement all methods of the RemedyAPI interface.")
    