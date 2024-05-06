from abc import ABC,abstractmethod
from PYTHON_TRELLO_LLD.model.Board import Board
from PYTHON_TRELLO_LLD.repository.board_storage import Board
from PYTHON_TRELLO_LLD.Utilities.helpers import generate_random_number


class BoardService:
    @abstractmethod
    def create(self,name,privacy,members,lists):
        pass

    def move_card(self,board_id,list_id_from,list_id_to)
        pass

class BoardServiceImpl(BoardService):
    def create(self,name,privacy,members,lists):
        generated_id = generate_random_number()
        generated_url = URLConstants.BOARD_URL + str(generated_id)
        board = Board(name,privacy,members,lists,igenerated_id,generated_url)

        board_object = Board()
        board.put_board(generated_id,board)

        return board

    def move_card(self,board_id,list_id_from,list_id_to,card_id,list_service):
        first_list = None
        second_list = None

        board_object = Board()
        board = board_object.get_board(board_id)
        list_data = board.get_list_from_board()

        for data in list_data:
            if data.get_id() == list_id_from:
                first_list = data
            if data.get_id == list_id_to:
                second_list = data

        if second_list is None or first_list is None:
            print(f"The Movement is not possible for {board_id} from {list_id_from} to {list_id_to}")

        else:
            first_card_dict = first_list.get_cards()
            second_card_dict = second_list.get_cards()

            if first_card_dict.get(card_id,None):
                print(f"The card id {card_id} not found in list_id {list_id_from} so movement is not possible")
                return
            card = first_card_dict.get(card_id)
            del first_card_dict[card_id]

            second_card_dict[card_id] = card

            first_list.set_card(card)
            second_list.set_card(card)

            list_service.update_list(first_list)
            list_service.update_list(second_list)

          
            board_object.put_board(board_id,board)

    def delete_board(self,board_id):
        board_respository = Board()
        board_object = board_respository.get(board_id)
        lists = board_object.get_list_from_board()
        list_service = Listserviceimpl()
        
        for list_data in lists:
            list_service.remove_from_list(list_data.get_id())
            print(f"successfully deleted the list_data_id {list_data.get_id()} from the list_service")

        board_respository.delete_board(board_id)
        print(f"successfully deleted the board with id :{board_id}")


    def show_single_board(self,board_id):
        board_repository = Board()
        board_object = board_repository.display_single_board(board_id)
        board_object.display_board()
        


            



