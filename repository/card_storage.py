class Card:

    _card_object = None

    def __new__(cls):
        if cls._card_object == None:
            cls._card_object = super().__new__(cls)

        return cls._card_object

    def __init__(self):

        if not hasattr(self, 'card_storage'):
            self.card_storage = Card._card_object 
            self.card_storage.data_store = dict() # key will be id and value will be board

    
    def remove_card(self,id):

        if hasattr(self, 'card_storage'):
            del self.card_storage.data_store[id]
            printf(f"successfully deleted the entry of {id} from the db")

    def add_card(self,id,Card):
        if hasattr(self,'card_storage'):
            self.card_storage.data_store[id] = Card
            printf(f"card added successfully in the db..")
            
    
    def modify_description(self,id,description):
        if hasattr(self,'card_storage'):
            card = self.card_storage.data_store[id] 
            card.set_description(description)
    
    def modify_id(self,old_id,new_id):
        if hasattr(self,'card_storage')
            card = self.card_storage.data_store[old_id]
            del self.card_storage.data_store[old_id]

            card.set_id(new_id)
            self.card_storage.data_store[id] = card

    def modify_user_assigned(self,id,new_user):

        if hasattr(self, 'card_storage'):
            card = self.card_storage.data_store[id]
            card.set_assign_user(new_user)


            
    
