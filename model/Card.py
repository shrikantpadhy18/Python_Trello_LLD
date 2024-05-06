class Card:

    def __init__(self,ids,name,description,assigned_user):
        self._id = ids
        self._name = name
        self._description = description
        self._user = assigned_user


    def set_id(self,id):
        self._id = id

    def set_name(self,name):
        self._name = name

    def set_description(self,description):
        self._description = description
    
    def set_assign_user(self,user):
        self._user = user

    def unassign_user(self):
        self._user = None

    def display_card(self):
        print("following are the card information...")
        print("id : ", self._id)
        print("name : ",self._name)
        print("description : ",self._description)
        print("assigned_user_info :\n ", self._user.display_user() if self._user is not None else "No User Assigned")




