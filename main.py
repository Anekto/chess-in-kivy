from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button  # Import other UI elements you need
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.image import Image



#from kivy.uix.label import Label  # Import the Label class



# ... (your existing imports)
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

        # stores to/from , button text, button id
        self.buffer = ["to", "", 0, None]
        self.buttons = {}
        self.button_list = []


        letter = ["a", "b", "c", "d", "e", "f", "g", "h"]

        # Create buttons for the chessboard
        self.white_Pieces = ["wT", "wL", "wS", "wK", "wKK", "wS", "wL", "wT", "wB"]
        self.black_Pieces = ["sT", "sL", "sS", "sK", "sKK", "sS", "sL", "sT", "sB"]
        self.blank = "__"

        c = 0
        for i in range(8):
            c += 1
            for z in range(8):
                
                c += 1

                chess_button = ChessButton(
                    text=(
                        f"{self.white_Pieces[z]}" if i <= 0 else
                        f"{self.white_Pieces[8]}" if i == 1 else
                        f"{self.blank}" if i < 6 else
                        f"{self.black_Pieces[8]}" if i == 6 else
                        f"{self.black_Pieces[z]}"),
                        background_color=(0.3, 0.3, 0.3, 1 )if c % 2 == 0 else
                                        (0.6, 0.6, 0.6, 1 )
                                           
                        )

                chess_button.button_id = f"{str(i + 1) + letter[z]}"

                chess_button.bind(on_press=self.on_button_press)
                chess_button.bind(on_release=self.on_release_button)
                self.add_widget(chess_button)
                self.buttons[chess_button.button_id] = chess_button # Store reference
                self.button_list.append(chess_button)


    def change_specific_button_text_by_id(self, button_id, new_text):
        if button_id in self.buttons:
            self.buttons[button_id].text = new_text

    def change_specific_button_color_by_id(self, button_id, new_color):
        if button_id in self.buttons:
            self.buttons[button_id].color = new_color
    

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
                pass
        else:
            self.buffer = ["from", instance.text, instance.button_id]

    def on_release_button(self, instance):
        instance.color = (0, 1, 1, 1)
        print("BUTTON RELEASED")

        if self.buffer[0] == "to": # Changes color of first and 2nd button back to normal
            instance.color = (1, 1, 1, 1)
            ChessBoard.change_specific_button_color_by_id(self, self.buffer[2], (1, 1, 1, 1))


    

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
                #print("\n Pos1,Pos2", pos1, pos2)
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



class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation="vertical")
        label = Label(text="This is the Main Screen!")  # Corrected line

        button_quit = Button(text="Quit Game")
        button = Button(text="Go to Second Screen")
        button.bind(on_press=self.switch_to_second_screen)
        # BUTTON DOESNT WORK
        button_quit.bind(on_press=self.quit_game)
        
        layout.add_widget(button)
        layout.add_widget(button_quit)
        
        self.add_widget(layout)

    def switch_to_second_screen(self, instance):
        # Change screen manager's current screen to "second_screen"
        self.manager.current = "second_screen"


    def quit_game(self, instance):
        App.get_running_app().stop()





class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        # Main layout with vertical orientation
        self.main_layout = BoxLayout(orientation="vertical")

        # Top layout for buttons
        top_layout = BoxLayout(size_hint_y=0.2)  # Adjust size_hint_y as needed
        top_layout.add_widget(Button(text="Game Reset", on_press=self.reset_board, background_color=(1, 1, 0.5, 1)))  # Yellow
        top_layout.add_widget(Button(text="Go Back to Main Screen", on_press=self.switch_to_main_screen, background_color=(0.5, 0.5, 1, 1)))  # Gray

       
        # Chess board layout
        self.chess_layout = ChessBoard()

        # Add layouts to the main layout
        self.main_layout.add_widget(top_layout)
        self.main_layout.add_widget(self.chess_layout)

        self.add_widget(self.main_layout)




    def switch_to_main_screen(self, instance):
        # Change screen manager's current screen to "main_screen"
        self.manager.current = "main_screen"

    def reset_board(self, instance):
        # Clear main_layout widget for chessboard to reset the game state
        self.main_layout.remove_widget(self.chess_layout)
        shared_state.game_info = 1
        shared_state.state = None
        shared_state.player = 1
        shared_state.success = False
        shared_state.buttons_share = None
        shared_state.turn = False

        self.chess_layout = ChessBoard()
        self.main_layout.add_widget(self.chess_layout)


class ChessApp(App):
    def build(self):
        # ADDS SCREENS AS A WIDGET TO CLICK THROUGH
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name="main_screen"))
        screen_manager.add_widget(SecondScreen(name="second_screen"))
        return screen_manager
    

ChessApp().run()
