import board_layout
import play_Pieces
import piece_Move_2
import schachpruefung


white_Pieces = ["wT ", "wL ", "wS ", "wK ", "wKK", "wS ", "wL ", "wT ", "wB ", "___"]
black_Pieces = ["sT ", "sL ", "sS ", "sK ", "sKK", "sS ", "sL ", "sT ", "sB ", "___"]

def main():
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
    print("\n Weiß beginnt mit dem ersten Zug!")

    while start:
        if start_game == 1:
            state = board_layout.layout(True, play_Pieces.pieces())
            start_game = 0
        else:
            board_layout.layout(start, state)

        pos1 = input("\n Bitte gebe die Koordinaten für die zu bewegende Figur an z.B. '1-c'")
        pos2 = input("Bitte gebe die Koordinaten wohin die Figur ziehen soll an z.B. '3-d'")
        try:
            pos1 = [int(pos1[0]), play_Pieces.char_to_int(pos1[2]) - 1]
            pos2 = [int(pos2[0]), play_Pieces.char_to_int(pos2[2]) - 1]

            print(pos1, pos2)
        except:
            continue

        if player == 1:
            if state[pos1[0]][pos1[1]] in white_Pieces[0:9]:
                state = piece_Move_2.make_move(pos1, pos2, state, turn, player)
                print("Weiß macht seinen Zug")
                player = 2
            else:
                player = 1
                print("Falsche Farbe bewegt, Spieler 1 bitte noch einmal!")
        if player == 2:
            if state[pos1[0]][pos1[1]] in black_Pieces[0:9]:
                state = piece_Move_2.make_move(pos1, pos2, state, turn, player)
                print("Schwarz macht seinen Zug")
                player = 1
            else:
                player = 2
                print("Falsche Farbe bewegt, Spieler 2 bitte noch einmal!")


        king_Kill = schachpruefung.schach(state)
        if king_Kill == True:
            print("Game over!")


main()