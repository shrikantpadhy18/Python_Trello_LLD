class List:

    _list_object = None

    def __new__(cls):
        if cls._list_object == None:
            cls._list_object = super().__new__(cls)

        return cls._list_object

    def __init__(self):

        if not hasattr(self, 'list_storage'):
            self.list_storage = Board._list_object 
            self.list_storage.data_store = dict() # key will be id and value will be list


    def get_list(self,id):

        if  hasattr(self, 'list_storage'):
            return self.list_storage.data_store[id]

    def put_list(self,id,list_data):

        if hasattr(self, 'list_storage'):
            self.list_storage.data_store[id] = list_data

    def remove_from_list(self,id):
        if hasattr(self, 'list_storage'):
            del self.list_storage.data_store[id]
            print(f"successfully removed list {id} from the the list..")
            

    

