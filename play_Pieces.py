def pieces():
    wB  = "wB "
    sB  = "sB "


    str = ""
    header = []
    layout = []
    for h in "abcdefgh":
        str = "__" + h
        header.append(str)
    header.append("#")
    white_Pieces = ["wT ", "wS ", "wL ", "wK ", "wKK", "wL ", "wS ", "wT "]
    black_Pieces = ["sT ", "sS ", "sL ", "sK ", "sKK", "sL ", "sS ", "sT "]
    white_Pawn = []
    black_Pawn = []


    blank_Lines = []
    for i in range(8):
        blank_Lines.append("___")
        white_Pawn.append(wB)
        black_Pawn.append(sB)


    layout.append(header)
    layout.append(black_Pieces)
    layout.append(black_Pawn)
    for k in range(4):
        blank_Var = blank_Lines[0:8]
        layout.append(blank_Var)
    layout.append(white_Pawn)
    layout.append(white_Pieces)
    

    for i in range(9):
        if i != 0:
            layout[i].append(i)


    return layout


def char_to_int(char):
    if char == 'a':
        return 1
    if char == 'b':
        return 2
    if char == 'c':
        return 3
    if char == 'd':
        return 4
    if char == 'e':
        return 5
    if char == 'f':
        return 6
    if char == 'g':
        return 7
    if char == 'h':
        return 8
    
'''def stockfish_notation(num):
    return 8 - num'''