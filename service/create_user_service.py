from TRELLO.service.servicetemplates.user_service import *
from TRELLO.model.User import *


class UserserviceImpl(Userservice):
    
    def create_user(self,user_id,name,email):
        
        user_builder = UserBuilder();
        user = user_builder.set_user_id(user_id).set_email(email).set_name(name).build()
        
        return user
        
    
    
    