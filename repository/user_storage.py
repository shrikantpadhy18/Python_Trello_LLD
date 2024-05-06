class User:

    _user_object = None

    def __new__(cls):
        if cls._user_object == None:
            cls._user_object = super().__new__(cls)

        return cls._user_object

    def __init__(self):

        if not hasattr(self, 'user_storage'):
            self.user_storage = Board._user_object 
            self.user_storage.data_store = dict() # key will be id and value will be board

    def put_user(self, user_id, user):
        if hasattr(self,'user_storage'):
            self.user_storage.data_store[user_id] = user
            print(f"user added successfully")

    def delete_user(self, user_id):
        if hasattr(self, 'user_storage'):
            del self.user_storage.data_store[user_id]
            print(f"user id : {user_id} is successfully deleted from user storage")

