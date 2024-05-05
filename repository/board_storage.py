class Board:

    _object = None

    def __new__(cls):
        if cls._object == None:
            cls._object = super().__new__(cls)

        return cls._object

    def __init__(self):

        if not hasattr(self, 'board_storage'):
            self.board_storage = Board._object 
            self.board_storage.data_store = dict() # key will be id and value will be board

        
    def put_board(self,ids,board):

        if hasattr(self,"board_storage"):
            self.board_storage.data_store[ids] = board
            printf(f"The board inserted succesfully for {ids} ..")


    def get_board(self,ids):
        if hasattr(self,'board_storage'):
            return self.board_storage.data_store[ids]
        return None
            
