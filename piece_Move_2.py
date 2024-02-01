import valid_move
import shared_state

def move_Piece(layout, start_Pos, target_Pos):

    buffer_Piece = ""

    buffer_Piece = layout[start_Pos[0]][start_Pos[1]]

    layout[start_Pos[0]][start_Pos[1]] = "___"

    layout[target_Pos[0]][target_Pos[1]] = buffer_Piece

    return layout

#def collision_check(piece_pos, dest_pos, new_pos, layout):
#    move_vector = piece_pos - dest_pos
#    for n in range(8):



def make_move(piece_pos, dest_pos, layout, turn, player):

    '''Get coordinates like [1] [8] to move the piece to that position'''

    pos_V = [0, 0]
    new_Pos = [0, 0]
    valid = False


    wB  = "wB "
    wT  = "wT "
    wL  = "wL "
    wS  = "wS "
    wK  = "wK "
    wKK = "wKK"
    sB  = "sB "
    sT  = "sT "
    sL  = "sL "
    sS  = "sS "
    sK  = "sK "
    sKK = "sKK"

    white_Pieces = [wT, wL, wS, wK, wKK, wS, wL, wT, wB, "___"]
    black_Pieces = [sT, sL, sS, sK, sKK, sS, sL, sT, sB, "___"]

    for i in range(2):
        new_Pos[i] = abs(piece_pos[i] - dest_pos[i])
        pos_V[i] = dest_pos[i] - piece_pos[i]


    if layout[piece_pos[0]][piece_pos[1]] == wB or layout[piece_pos[0]][piece_pos[1]] == sB:
        valid = valid_move.pawn(new_Pos, pos_V, layout, piece_pos, dest_pos)

    if layout[piece_pos[0]][piece_pos[1]] == wT or layout[piece_pos[0]][piece_pos[1]] == sT:
        valid = valid_move.tower(new_Pos, pos_V, layout, piece_pos, dest_pos)

    if layout[piece_pos[0]][piece_pos[1]] == wL or layout[piece_pos[0]][piece_pos[1]] == sL:
        valid = valid_move.slider(new_Pos, pos_V, layout, piece_pos, dest_pos)

    if layout[piece_pos[0]][piece_pos[1]] == wS or layout[piece_pos[0]][piece_pos[1]] == sS :
        valid = valid_move.horse(new_Pos, pos_V, layout, piece_pos, dest_pos)

    if layout[piece_pos[0]][piece_pos[1]] == wK or layout[piece_pos[0]][piece_pos[1]] == sK:
        valid = valid_move.king(new_Pos, pos_V, layout, piece_pos, dest_pos)

    if layout[piece_pos[0]][piece_pos[1]] == wKK or layout[piece_pos[0]][piece_pos[1]] == sKK:
        valid = valid_move.queen(new_Pos, pos_V, layout, piece_pos, dest_pos)


    if valid:
        if turn == None:
            return True
        else:

            if player == 1:
                if layout[piece_pos[0]][piece_pos[1]] in white_Pieces[0:9]:
                    new_layout = move_Piece(layout, piece_pos, dest_pos)
                    return new_layout
                else:
                    new_layout = layout
            elif player == 2:
                if layout[piece_pos[0]][piece_pos[1]] in black_Pieces[0:9]:
                    new_layout = move_Piece(layout, piece_pos, dest_pos)
                    return new_layout
                else:
                    new_layout = layout
            else:
                 new_layout = layout

    elif turn == None:
        return False
    else:
        print("Dieser zug ist leider nicht möglich!")
        shared_state.success = False
        new_layout = layout
    
    return new_layout
