from abc import ABC, abstractmethod
from list_storage import List


class Listservice(ABC):

    def create(self, id, name, card):
        pass

    def update_list(list_id,list_data):
        pass


class Listserviceimpl(Listservice):

    def create(self, id, name, card):
        list_object = List(id, name, card)
        return list_object

    # def modify_name(self,id):
    #     pass

    def update_list(self,list_id,list_data):
        list_persistence = List()
        list_persistence.put_list(list_id,list_data)

    def remove_from_list(self,list_id):
        list_persistence = List()
        list_persistence.remove_from_list(list_id)
