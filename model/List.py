class List:

    def __init__(self, id, name, cards):
        self._id = id
        self._name = name
        self._cards = cards # dict

    
    def set_id(self, id):
        self._id = id
    
    def set_name(self, name):
        self._name = name
    
    def set_card(self, cards):
        self._cards = cards

    def get_id(self):
        return self._id

    def get_cards(self):
        return self._cards

    

    

