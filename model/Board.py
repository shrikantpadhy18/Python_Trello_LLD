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

    

    
        
    
    
    
        
        