from abc import ABC,abstractmethod
from PYTHON_TRELLO_LLD.model.User import *

class Userservice(ABC):
    @abstractmethod
    def create(self,user_id,name,email):
        pass



class UserserviceImpl(Userservice):
    
    def create(self,user_id,name,email):
        
        user_builder = UserBuilder();
        user = user_builder.set_user_id(user_id).set_email(email).set_name(name).build()
        
        return user
        
    
    
    