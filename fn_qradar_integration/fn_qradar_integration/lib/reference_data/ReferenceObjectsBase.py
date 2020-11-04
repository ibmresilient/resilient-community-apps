import abc


class ReferenceObjectBase(abc.ABC):

    @abc.abstractmethod
    def add_ref_element(self):
        pass

    @abc.abstractmethod
    def update_ref_element(self):
        pass
     
    @abc.abstractmethod
    def delete_ref_element(self, *args, **kwargs):
        pass
