# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
import abc

# In python 3 we can directly access abc.ABC and inherit from that
ABC = abc.ABC
error_text = "Child classes must implement all methods of the HelixAPI interface."

class HelixAPI(ABC):

    @abc.abstractmethod
    def get_token(self, *args, **kwargs):
        raise NotImplementedError(error_text)

    @abc.abstractmethod
    def build_request_headers(self, *args, **kwargs):
        raise NotImplementedError(error_text)

    @abc.abstractmethod
    def release_token(self, *args, **kwargs):
        raise NotImplementedError(error_text)

    @abc.abstractmethod
    def create_form_entry(self, *args, **kwargs):
        raise NotImplementedError(error_text)

    @abc.abstractmethod
    def get_form_entry(self, *args, **kwargs):
        raise NotImplementedError(error_text)

    @abc.abstractmethod
    def update_form_entry(self, *args, **kwargs):
        raise NotImplementedError(error_text)

    @abc.abstractmethod
    def delete_form_entry(self, *args, **kwargs):
        raise NotImplementedError(error_text)
