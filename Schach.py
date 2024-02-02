import board_layout
import play_Pieces
import piece_Move_2
import schachpruefung


white_Pieces = ["wT ", "wL ", "wS ", "wK ", "wKK", "wS ", "wL ", "wT ", "wB ", "___"]
black_Pieces = ["sT ", "sL ", "sS ", "sK ", "sKK", "sS ", "sL ", "sT ", "sB ", "___"]

def main():
    # For debugging commented out change accordingly 
    #game_Start = input("Welcome to the chess app. Do you want to play a round ? Type 'y' or 'n' !")

    game_Start = "y"
    pos1 = ""
    pos2 = ""

    if game_Start == "y":
        start = True
        turn = False
        start_game = 1
        player = 1
    else:
        print("The game will close now.")
        start = False
    print("\n White makes the first move")

    while start:
        if start_game == 1:
            state = board_layout.layout(True, play_Pieces.pieces())
            start_game = 0
        else:
            board_layout.layout(start, state)

        pos1 = input("\n Please enter coordinates to move a piece e.g. 'FROM' '1-c'")
        pos2 = input("Please enter coordinates to move a piece to a position 'TO' e.g. '3-d'")
        try:
            pos1 = [int(pos1[0]), play_Pieces.char_to_int(pos1[2]) - 1]
            pos2 = [int(pos2[0]), play_Pieces.char_to_int(pos2[2]) - 1]

            print(pos1, pos2)
        except:
            continue

        if player == 1:
            if state[pos1[0]][pos1[1]] in white_Pieces[0:9]:
                state = piece_Move_2.make_move(pos1, pos2, state, turn, player)
                print("White moves.")
                player = 2
            else:
                player = 1
                print("Tried to move wrong color, try again")
        if player == 2:
            if state[pos1[0]][pos1[1]] in black_Pieces[0:9]:
                state = piece_Move_2.make_move(pos1, pos2, state, turn, player)
                print("Black moves.")
                player = 1
            else:
                player = 2
                print("Tried to move wrong color, try again")


        king_Kill = schachpruefung.schach(state)
        if king_Kill == True:
            print("Game over!")


main()
