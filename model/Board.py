class Board:
    
    def __init__(self,name,privacy,members,lists,ids,url):
        self._name = name
        self._privacy = privacy
        self._members = members
        self._lists = lists #set
        
        self._id = ids
        self._url = url

    def get_list_from_board(self):
        return self._lists

    def get_memebers_from_board(self):
        return self._members
    
    def get_url_from_board(self):
        return self._url

    def display_board(self):
        print(f"The board name is {self._name}")
        print(f"The privacy is {self._privacy}")
        print("following are the list present in the board")
        for list_data in self._lists:
            print("list: data\n",list_data.display_list())

        print("following are associated members of the list\n")
        for user in self._members:
            print("user : data\n", user.display_user())



    

    
        
    
    
    
        
        