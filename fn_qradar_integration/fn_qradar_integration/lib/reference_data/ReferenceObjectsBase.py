# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
import sys
import abc

# There is a difference between have abstract base classes are handled in py 2 and 3
# In python 3 we can directly access abc.ABC and inherit from that
# In python 2 we must create the ABC class using abc.ABCMeta
if sys.version_info >= (3, 4):
    ABC = abc.ABC
else:
    ABC = abc.ABCMeta('ABC', (), {})

class ReferenceObjectBase(ABC):

    @abc.abstractmethod
    def add_ref_element(self):
        pass

    @abc.abstractmethod
    def update_ref_element(self):
        pass
     
    @abc.abstractmethod
    def delete_ref_element(self, *args, **kwargs):
        pass
