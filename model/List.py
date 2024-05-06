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


    def display_list(self):
        print("list information follows\n")
        print(f"The id of list is {self._id}")
        print(f"The name of list is {self._name}")
        print(f"card information in the list are as follows : ")
        for card in self._cards:
            card.display_card()
        

    

    

