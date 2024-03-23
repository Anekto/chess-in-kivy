
        
piece_to_fen = {
            "___": 1,  # Empty square
            "wT ": "R",
            "wL ": "B",
            "wS ": "N",
            "wK ": "K",
            "wKK": "Q",
            "wB ": "P",
            "sT ": "r",
            "sL ": "b",
            "sS ": "n",
            "sK ": "k",
            "sKK": "q",
            "sB ": "p"
        }



def convert_fen(state):
    fenstring = ""

    for row in state[1:]:
        number = 0
        for piece in row[:8]:
            if piece == "___":
                number += 1
            else:
                if number > 0:  # Add empty count if present
                    fenstring = fenstring + str(number)
                number = 0  # Reset empty count
                fenstring = fenstring + piece_to_fen[piece]

        # Add remaining empty squares at row end
        if number > 0:
            fenstring = fenstring + str(number)

        fenstring = fenstring + "/"

    return fenstring