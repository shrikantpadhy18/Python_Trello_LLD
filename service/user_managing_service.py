from abc import ABC,abstractmethod
from PYTHON_TRELLO_LLD.model.User import *
from PYTHON_TRELLO_LLD.Utilities.helpers import generate_random_number
from PYTHON_TRELLO_LLD.Utilities.enums import ModelEnum
from PYTHON_TRELLO_LLD.repository.user_storage import User

class Userservice(ABC):
    @abstractmethod
    def create(self,name,email):
        pass

    @abstractmethod
    def delete_user(self,user_id):
        pass



class UserserviceImpl(Userservice):
    
    def create(self,name,email):
        generated_user_id = generate_random_number(ModelEnum.USER)
        
        user_builder = UserBuilder();
        user = user_builder.set_user_id(generated_user_id).set_email(email).set_name(name).build()
        user_repository = User()
        user_repository.put_user(generated_user_id, user)
        return user

    def delete_user(self,user_id):
        user_repository = User()
        user_repository.delete_user(user_id)
    
    