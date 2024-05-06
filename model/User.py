class User:
    """
        define user model
    """
    
    def __init__(self, user_id, email, name):
        self._user_id = user_id
        self._email = email
        self._name = name
        
    def display_user(self):
        print("following is the user information...")
        print("user-email : ",self._email)
        print("user name : ",self._name)
        print("user id : ", self._user_id)
        
    
class UserBuilder:
    
    def __init__(self):
        self._user = User("","","")
        
    
    def set_user_id(self, user_id):
        self._user.user_id = user_id
        return self
    
    def set_email(self, email):
        self._email = email
        return self
    
    def set_name(self, name):
        self.name = name
        return self
    
    def build(self):
        return self._user
    
    
        