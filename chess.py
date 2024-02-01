from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

import shared_state
import board_layout
import play_Pieces
import piece_Move_2
import schachpruefung


class ChessButton(Button):
    button_id = StringProperty()

class ChessBoard(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 8
        self.spacing = [5, 5]  # Set spacing in pixels

        self.buffer = ["to", "", 0]
        self.buttons = {}
        self.button_list = []


        letter = ["a", "b", "c", "d", "e", "f", "g", "h"]

        # Create buttons for the chessboard
        self.white_Pieces = ["wT", "wL", "wS", "wK", "wKK", "wS", "wL", "wT", "wB"]
        self.black_Pieces = ["sT", "sL", "sS", "sK", "sKK", "sS", "sL", "sT", "sB"]
        self.blank = "__"


        for i in range(8):
            for z in range(8):
                chess_button = ChessButton(
                    text=(
                        f"{self.white_Pieces[z]}" if i <= 0 else
                        f"{self.white_Pieces[8]}" if i == 1 else
                        f"{self.blank}" if i < 6 else
                        f"{self.black_Pieces[8]}" if i == 6 else
                        f"{self.black_Pieces[z]}")
                    )

                chess_button.button_id = f"{str(i + 1) + letter[z]}"

                chess_button.bind(on_press=self.on_button_press)
                self.add_widget(chess_button)
                self.buttons[chess_button.button_id] = chess_button # Store reference
                self.button_list.append(chess_button)


    def change_specific_button_text_by_id(self, button_id, new_text):
        if button_id in self.buttons:
            self.buttons[button_id].text = new_text

    def on_button_press(self, instance):


        if self.buffer[0] == "from":
            self.buffer[0] = "to"
            
            print("\n Turn, reset, pos1,pos2", shared_state.turn, shared_state.game_info,  self.buffer[2], instance.button_id)

            ChessBoard.start_Game(self, True, shared_state.turn, shared_state.game_info,  self.buffer[2], instance.button_id)
            if shared_state.game_info == 1:
                shared_state.game_info = 0
            if shared_state.success:
                ChessBoard.change_specific_button_text_by_id(self, self.buffer[2], "___")
                instance.text = self.buffer[1]
                shared_state.success = False
        else:
            self.buffer = ["from", instance.text, instance.button_id]


    
    def reset_board(self):
        c = 0
        for i in range(8):
            for z in range(8):
                text_reset = (
                    f"{self.white_Pieces[z]}" if i == 0 else
                    f"{self.white_Pieces[8]}" if i == 1 else
                    f"{self.blank}" if 1 < i < 6 else
                    f"{self.black_Pieces[8]}" if i == 6 else
                    f"{self.black_Pieces[z]}")

                self.button_list[c].text = text_reset
                c += 1



        print(f"Button {instance.text} pressed with id: {instance.button_id}")

    def start_Game(self, start, turn, restart, pos1, pos2):

        self.white_Pieces = ["wT ", "wL ", "wS ", "wK ", "wKK", "wS ", "wL ", "wT ", "wB ", "___"]
        self.black_Pieces = ["sT ", "sL ", "sS ", "sK ", "sKK", "sS ", "sL ", "sT ", "sB ", "___"]


        if restart == 1:
            shared_state.player = 1
            shared_state.state = board_layout.layout(start, play_Pieces.pieces())
            restart = 0
        else:
            board_layout.layout(start, shared_state.state)

        try:
            pos1 = [int(pos1[0]), play_Pieces.char_to_int(pos1[1] ) - 1]
            pos2 = [int(pos2[0]), play_Pieces.char_to_int(pos2[1] ) - 1]
            print("\n Pos1,Pos2", pos1, pos2)
        except:
            print("Its not working")

        if shared_state.player == 1:
            if shared_state.state[pos1[0]][pos1[1]] in self.white_Pieces[0:9]:
                shared_state.success = True
                shared_state.state = piece_Move_2.make_move(pos1, pos2, shared_state.state, turn, shared_state.player)
                print("It's whites turn")
                if shared_state.success:
                    shared_state.player = 2

            else:
                shared_state.player = 1
                print("Moved wrong color, player 1 please move again")
        elif shared_state.player == 2:
            if shared_state.state[pos1[0]][pos1[1]] in self.black_Pieces[0:9]:
                shared_state.success = True
                shared_state.state = piece_Move_2.make_move(pos1, pos2, shared_state.state, turn, shared_state.player)
                print("Its blacks turn")
                if shared_state.success:
                    shared_state.player = 1   
            else:
                shared_state.player = 2
                print("Moved wrong color, player 2 please move again")


            king_Kill = schachpruefung.schach(shared_state.state)
            if king_Kill == True:
                print("Game over!")
        
        board_layout.layout(start, shared_state.state)


class OptionsLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spacing = 5

        options = ["Reset", "Option2", "Option3", "Option4"]

        # Create buttons for options
        for option in options:
            chess_button = ChessButton(
                text=option
                )
            chess_button.button_id = f"button_{options.index(option) + 1}"
            chess_button.bind(on_press=self.on_button_press)
            self.add_widget(chess_button)

    def on_button_press(self, instance):
        print(f"Option {instance.text} pressed")
        print(f"{instance.button_id}")

        if instance.text == "Reset":
            #game_info = [start, turn, start_game, player]
            shared_state.game_info = 1
            ChessApp.chessboard.reset_board()

class ChessApp(App):

    chessboard = None  # Class attribute to store ChessBoard instance

    def build(self):
        # Create a BoxLayout to hold both the chessboard and options layout
        root_layout = BoxLayout(orientation='vertical')

        # Add the options layout
        options_layout = OptionsLayout(size_hint_y=None, height=50)
        root_layout.add_widget(options_layout)

        # Add the chessboard
        ChessApp.chessboard = ChessBoard(size_hint_y=7)
        root_layout.add_widget(ChessApp.chessboard)

        return root_layout

if __name__ == "__main__":
    ChessApp().run()
