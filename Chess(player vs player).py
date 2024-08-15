from builtins import int

import numpy

# Two player chess (person vs person)

# Creating Board with pieces on their relative squares-
# w - represents the pieces of white
# b - represents the pieces of black
# P - represents Pawn
# R - represents Rook
# K - represents Knight
# B - represents Bishop
# Q - represents Queen
# O - represents King

Board = numpy.full((8, 8), "__", dtype='object')
Board[1, :] = "bP"
Board[6, :] = "wP"
Board[0, :] = ["bR", "bK", "bB", "bQ", "bO", "bB", "bK", "bR"]
Board[7, :] = ["wR", "wK", "wB", "wQ", "wO", "wB", "wK", "wR"]


def board_display():
    for indx, item in enumerate(Board):
        print("\t", 8 - indx, item,  sep="\t")
        print()
    print("              a    b    c    d    e    f    g    h")


# Coordinate system -
def index(sq_name):
    rows = [8, 7, 6, 5, 4, 3, 2, 1]
    columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
    column_index = columns.index(sq_name[0])
    row_index = rows.index(int(sq_name[1]))
    return row_index, column_index


def position(piece_name):
    row_num = 0
    column_num = 0
    for row in Board:
        for val in row:
            if val == piece_name:
                return row_num, column_num
            else:
                column_num += 1
        column_num = 0
        row_num += 1


def before_after_check(from_sq, to_sq, piece):
    r, c = index(from_sq)
    r_, c_ = index(to_sq)
    piece_to_be_taken = Board[r_, c_]
    if check(f"{piece[0]}"):
        Board[r, c], Board[r_, c_] = "__", piece
        if not check(f"{piece[0]}"):
            return

    Board[r, c], Board[r_, c_] = "__", piece
    if check(f"{piece[0]}"):
        Board[r, c], Board[r_, c_] = piece, piece_to_be_taken
        raise MoveNotPossibleError


# Checking for check -
def check(player):
    w_king_r, w_king_c = position("wO")
    b_king_r, b_king_c = position("bO")

    # For the white king -

    # By the pawn
    if player == "w":
        if w_king_c == 0:
            if Board[w_king_r - 1, w_king_c + 1] == "bP":
                return True
        elif w_king_c == 7:
            if Board[w_king_r - 1, w_king_c - 1] == "bP":
                return True
        else:
            if Board[w_king_r - 1, w_king_c + 1] == "bP" or Board[w_king_r - 1, w_king_c - 1] == "bP":
                return True

        #    For Diagonal checks
        i = 1
        while (w_king_r - i) != -1 and (w_king_c - i) != -1:
            if Board[w_king_r - i, w_king_c - i] == "__":
                i += 1
                pass
            elif Board[w_king_r - i, w_king_c - i] in ["bB", "bQ"]:
                return True
            else:
                break
        i = 1
        while (w_king_r - i) != -1 and (w_king_c + i) != 8:
            if Board[w_king_r - i, w_king_c + i] == "__":
                i += 1
                pass
            elif Board[w_king_r - i, w_king_c + i] in ["bB", "bQ"]:
                return True
            else:
                break

        i = 1
        while (w_king_r + i) != 8 and (w_king_c - i) != -1:
            if Board[w_king_r + i, w_king_c - i] == "__":
                i += 1
                pass
            elif Board[w_king_r + i, w_king_c - i] in ["bB", "bQ"]:
                return True
            else:
                break

        i = 1
        while (w_king_r + i) != 8 and (w_king_c + i) != 8:
            if Board[w_king_r + i, w_king_c + i] == "__":
                i += 1
                pass
            elif Board[w_king_r + i, w_king_c + i] in ["bB", "bQ"]:
                return True
            else:
                break

        #   Checks of same row or column -
        i = 1
        while (w_king_r - i) != -1:
            if Board[w_king_r - i, w_king_c] == "__":
                i += 1
                pass
            elif Board[w_king_r - i, w_king_c] in ["bR", "bQ"]:
                return True
            else:
                break

        i = 1
        while (w_king_r + i) != 8:
            if Board[w_king_r + i, w_king_c] == "__":
                i += 1
                pass
            elif Board[w_king_r + i, w_king_c] in ["bR", "bQ"]:
                return True
            else:
                break

        i = 1
        while (w_king_c - i) != -1:
            if Board[w_king_r, w_king_c - i] == "__":
                i += 1
                pass
            elif Board[w_king_r, w_king_c - i] in ["bR", "bQ"]:
                return True
            else:
                break

        i = 1
        while (w_king_c + i) != 8:
            if Board[w_king_r, w_king_c + i] == "__":
                i += 1
                pass
            elif Board[w_king_r, w_king_c + i] in ["bR", "bQ"]:
                return True
            else:
                break

        #   for checks by knight -
        if [w_king_r, w_king_c] == [0, 0]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r + i, w_king_c + j] == "bK":
                    return True
        if [w_king_r, w_king_c] == [0, 7]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r + i, w_king_c - j] == "bK":
                    return True
        if [w_king_r, w_king_c] == [7, 0]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r - j, w_king_c + i] == "bK":
                    return True
        if [w_king_r, w_king_c] == [7, 7]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r - i, w_king_c - j] == "bK":
                    return True

        if [w_king_r, w_king_c] == [0, 1]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r + i, w_king_c + j] == "bK":
                    return True
            if Board[w_king_r + 2, w_king_c - 1] == "bK":
                return True

        if [w_king_r, w_king_c] == [0, 6]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r + i, w_king_c - j] == "bK":
                    return True
            if Board[w_king_r + 2, w_king_c + 1] == "bK":
                return True

        if [w_king_r, w_king_c] == [1, 0]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r + i, w_king_c + j] == "bK":
                    return True
            if Board[w_king_r + 2, w_king_c + 1] == "bK":
                return True

        if [w_king_r, w_king_c] == [1, 7]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r + i, w_king_c - j] == "bK":
                    return True
            if Board[w_king_r - 1, w_king_c - 2] == "bK":
                return True

        if [w_king_r, w_king_c] == [6, 0]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r - i, w_king_c + j] == "bK":
                    return True
            if Board[w_king_r + 1, w_king_c + 2] == "bK":
                return True

        if [w_king_r, w_king_c] == [6, 7]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r - i, w_king_c - j] == "bK":
                    return True
            if Board[w_king_r + 1, w_king_c - 2] == "bK":
                return True

        if [w_king_r, w_king_c] == [7, 1]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r - i, w_king_c + j] == "bK":
                    return True
            if Board[w_king_r - 2, w_king_c - 1] == "bK":
                return True

        if [w_king_r, w_king_c] == [7, 6]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r - i, w_king_c - j] == "bK":
                    return True
            if Board[w_king_r - 2, w_king_c + 1] == "bK":
                return True

        if [w_king_r, w_king_c] == [1, 1]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r + i, w_king_c + j] == "bK":
                    return True
            if Board[w_king_r - 1, w_king_c + 2] == "bK":
                return True
            elif Board[w_king_r + 2, w_king_c - 1] == "bK":
                return True

        if [w_king_r, w_king_c] == [1, 6]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r + i, w_king_c - j] == "bK":
                    return True
            if Board[w_king_r - 1, w_king_c - 2] == "bK":
                return True
            elif Board[w_king_r + 2, w_king_c + 1] == "bK":
                return True

        if [w_king_r, w_king_c] == [6, 1]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r - i, w_king_c + j] == "bK":
                    return True
            if Board[w_king_r + 1, w_king_c + 2] == "bK":
                return True
            elif Board[w_king_r - 2, w_king_c - 1] == "bK":
                return True

        if [w_king_r, w_king_c] == [6, 6]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r - i, w_king_c - j] == "bK":
                    return True
            if Board[w_king_r + 1, w_king_c - 2] == "bK":
                return True
            elif Board[w_king_r - 2, w_king_c + 1] == "bK":
                return True

        if w_king_c == 0 and w_king_r in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r + i, w_king_c + j] == "bK" or Board[w_king_r - i, w_king_c + j] == "bK":
                    return True

        if w_king_r == 0 and w_king_c in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r + i, w_king_c + j] == "bK" or Board[w_king_r + i, w_king_c - j] == "bK":
                    return True

        if w_king_r == 7 and w_king_c in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r - i, w_king_c - j] == "bK" or Board[w_king_r - i, w_king_c + j] == "bK":
                    return True

        if w_king_c == 7 and w_king_r in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r + i, w_king_c - j] == "bK" or Board[w_king_r - i, w_king_c - j] == "bK":
                    return True

        if w_king_c == 1 and w_king_r in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r + i, w_king_c + j] == "bK":
                    return True
                elif Board[w_king_r - i, w_king_c + j] == "bK":
                    return True
            if Board[w_king_r + 2, w_king_c - 1] == "bK" or Board[w_king_r - 2, w_king_c - 1] == "bK":
                return True

        if w_king_c == 6 and w_king_r in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r - i, w_king_c - j] == "bK":
                    return True
                elif Board[w_king_r + i, w_king_c - j] == "bK":
                    return True
            if Board[w_king_r + 2, w_king_c + 1] == "bK" or Board[w_king_r - 2, w_king_c + 1] == "bk":
                return True

        if w_king_r == 1 and w_king_c in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r + i, w_king_c - j] == "bK":
                    return True
                elif Board[w_king_r + i, w_king_c + j] == "bK":
                    return True
            if Board[w_king_r - 1, w_king_c - 2] == "bk" or Board[w_king_r - 1, w_king_c + 2] == "bK":
                return True

        if w_king_r == 6 and w_king_c in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r - i, w_king_c + j] == "bK":
                    return True
                elif Board[w_king_r - i, w_king_c - j] == "bK":
                    return True
            if Board[w_king_r + 1, w_king_c + 2] == "bK" or Board[w_king_r + 1, w_king_c - 2] == "bK":
                return True

        if w_king_r in range(2, 6) and w_king_c in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r + i, w_king_c + j] == "bK":
                    return True
                elif Board[w_king_r + i, w_king_c - j] == "bK":
                    return True
                elif Board[w_king_r - i, w_king_c + j] == "bK":
                    return True
                elif Board[w_king_r - i, w_king_c - j] == "bK":
                    return True

    # For the black king

    # By the pawn
    if player == "b":
        if b_king_c == 0:
            if Board[b_king_r + 1, b_king_c + 1] == "wP":
                return True
        elif b_king_c == 7:
            if Board[b_king_r + 1, b_king_c - 1] == "wP":
                return True
        else:
            if Board[b_king_r + 1, b_king_c + 1] == "wP" or Board[b_king_r + 1, b_king_c - 1] == "wP":
                return True

            #    For Diagonal checks
        i = 1
        while (b_king_r - i) != -1 and (b_king_c - i) != -1:
            if Board[b_king_r - i, b_king_c - i] == "__":
                i += 1
                pass
            elif Board[b_king_r - i, b_king_c - i] in ["wB", "wQ"]:
                return True
            else:
                break
        i = 1
        while (b_king_r - i) != -1 and (b_king_c + i) != 8:
            if Board[b_king_r - i, b_king_c + i] == "__":
                i += 1
                pass
            elif Board[b_king_r - i, b_king_c + i] in ["wB", "wQ"]:
                return True
            else:
                break

        i = 1
        while (b_king_r + i) != 8 and (b_king_c - i) != -1:
            if Board[b_king_r + i, b_king_c - i] == "__":
                i += 1
                pass
            elif Board[b_king_r + i, b_king_c - i] in ["wB", "wQ"]:
                return True
            else:
                break

        i = 1
        while (b_king_r + i) != 8 and (b_king_c + i) != 8:
            if Board[b_king_r + i, b_king_c + i] == "__":
                i += 1
                pass
            elif Board[b_king_r + i, b_king_c + i] in ["wB", "wQ"]:
                return True
            else:
                break

        #   Checks of same row or column -
        i = 1
        while (b_king_r - i) != -1:
            if Board[b_king_r - i, b_king_c] == "__":
                i += 1
                pass
            elif Board[b_king_r - i, b_king_c] in ["wR", "wQ"]:
                return True
            else:
                break

        i = 1
        while (b_king_r + i) != 8:
            if Board[b_king_r + i, b_king_c] == "__":
                i += 1
                pass
            elif Board[b_king_r + i, b_king_c] in ["wR", "wQ"]:
                return True
            else:
                break

        i = 1
        while (b_king_c - i) != -1:
            if Board[b_king_r, b_king_c - i] == "__":
                i += 1
                pass
            elif Board[b_king_r, b_king_c - i] in ["wR", "wQ"]:
                return True
            else:
                break

        i = 1
        while (b_king_c + i) != 8:
            if Board[b_king_r, b_king_c + i] == "__":
                i += 1
                pass
            elif Board[b_king_r, b_king_c + i] in ["wR", "wQ"]:
                return True
            else:
                break

        #   for checks by knight -
        if [b_king_r, b_king_c] == [0, 0]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r + i, b_king_c + j] == "wK":
                    return True
        if [b_king_r, b_king_c] == [0, 7]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r + i, b_king_c - j] == "wK":
                    return True
        if [b_king_r, b_king_c] == [7, 0]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r - j, b_king_c + i] == "wK":
                    return True
        if [b_king_r, b_king_c] == [7, 7]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r - i, b_king_c - j] == "wK":
                    return True

        if [b_king_r, b_king_c] == [0, 1]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r + i, b_king_c + j] == "wK":
                    return True
            if Board[b_king_r + 2, b_king_c - 1] == "wK":
                return True

        if [b_king_r, b_king_c] == [0, 6]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r + i, b_king_c - j] == "wK":
                    return True
            if Board[b_king_r + 2, b_king_c + 1] == "wK":
                return True

        if [b_king_r, b_king_c] == [1, 0]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r + i, b_king_c + j] == "wK":
                    return True
            if Board[b_king_r + 2, b_king_c + 1] == "wK":
                return True

        if [b_king_r, b_king_c] == [1, 7]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r + i, b_king_c - j] == "wK":
                    return True
            if Board[b_king_r - 1, b_king_c - 2] == "wK":
                return True

        if [b_king_r, b_king_c] == [6, 0]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r - i, b_king_c + j] == "wK":
                    return True
            if Board[b_king_r + 1, b_king_c + 2] == "wK":
                return True

        if [b_king_r, b_king_c] == [6, 7]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r - i, b_king_c - j] == "wK":
                    return True
            if Board[b_king_r + 1, b_king_c - 2] == "wK":
                return True

        if [b_king_r, b_king_c] == [7, 1]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r - i, b_king_c + j] == "wK":
                    return True
            if Board[b_king_r - 2, b_king_c - 1] == "wK":
                return True

        if [b_king_r, b_king_c] == [7, 6]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r - i, b_king_c - j] == "wK":
                    return True
            if Board[b_king_r - 2, b_king_c + 1] == "wK":
                return True

        if [b_king_r, b_king_c] == [1, 1]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r + i, b_king_c + j] == "wK":
                    return True
            if Board[b_king_r - 1, b_king_c + 2] == "wK":
                return True
            elif Board[b_king_r + 2, b_king_c - 1] == "wK":
                return True

        if [b_king_r, b_king_c] == [1, 6]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r + i, b_king_c - j] == "wK":
                    return True
            if Board[b_king_r - 1, b_king_c - 2] == "wK":
                return True
            elif Board[b_king_r + 2, b_king_c + 1] == "wK":
                return True

        if [b_king_r, b_king_c] == [6, 1]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r - i, b_king_c + j] == "wK":
                    return True
            if Board[b_king_r + 1, b_king_c + 2] == "wK":
                return True
            elif Board[b_king_r - 2, b_king_c - 1] == "wK":
                return True

        if [w_king_r, w_king_c] == [6, 6]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r - i, b_king_c - j] == "wK":
                    return True
            if Board[b_king_r + 1, b_king_c - 2] == "wK":
                return True
            elif Board[b_king_r - 2, b_king_c + 1] == "wK":
                return True

        if b_king_c == 0 and b_king_r in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r + i, b_king_c + j] == "wK" or Board[b_king_r - i, b_king_c + j] == "wK":
                    return True

        if b_king_r == 0 and b_king_c in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r + i, b_king_c + j] == "wK" or Board[b_king_r + i, b_king_c - j] == "wK":
                    return True

        if b_king_r == 7 and b_king_c in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r - i, b_king_c - j] == "wK" or Board[b_king_r - i, b_king_c + j] == "wK":
                    return True

        if b_king_c == 7 and b_king_r in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r + i, b_king_c - j] == "wK" or Board[b_king_r - i, b_king_c - j] == "wK":
                    return True

        if b_king_c == 1 and b_king_r in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r + i, b_king_c + j] == "wK":
                    return True
                elif Board[b_king_r - i, b_king_c + j] == "wK":
                    return True
            if Board[b_king_r + 2, b_king_c - 1] == "wK" or Board[b_king_r - 2, b_king_c - 1] == "wK":
                return True

        if w_king_c == 6 and w_king_r in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[w_king_r - i, w_king_c - j] == "bK":
                    return True
                elif Board[w_king_r + i, w_king_c - j] == "bK":
                    return True
            if Board[w_king_r + 2, w_king_c + 1] == "bK" or Board[w_king_r - 2, w_king_c + 1] == "bk":
                return True

        if b_king_r == 1 and b_king_c in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r + i, b_king_c - j] == "wK":
                    return True
                elif Board[b_king_r + i, b_king_c + j] == "wK":
                    return True
            if Board[b_king_r - 1, b_king_c - 2] == "wk" or Board[b_king_r - 1, b_king_c + 2] == "wK":
                return True

        if b_king_r == 6 and b_king_c in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r - i, b_king_c + j] == "wK":
                    return True
                elif Board[b_king_r - i, b_king_c - j] == "wK":
                    return True
            if Board[b_king_r + 1, b_king_c + 2] == "wK" or Board[b_king_r + 1, b_king_c - 2] == "wK":
                return True

        if b_king_r in range(2, 6) and b_king_c in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if Board[b_king_r + i, b_king_c + j] == "wK":
                    return True
                elif Board[b_king_r + i, b_king_c - j] == "wK":
                    return True
                elif Board[b_king_r - i, b_king_c + j] == "wK":
                    return True
                elif Board[b_king_r - i, b_king_c - j] == "wK":
                    return True


# Actions of pieces -

# for the pawns -
def pawn_moves(player, from_sq, to_sq):
    r, c = index(from_sq)
    r_, c_ = index(to_sq)

    if player == "w":
        if Board[r, c] == "wP":
            if c == c_:
                if r == 6 and r_ == 4:
                    if Board[r - 1, c] == "__" and Board[r_, c_] == "__":
                        before_after_check(from_sq, to_sq, "wP")
                elif r_ == r - 1:
                    #   Pawn Promotion
                    if r_ == 0 and Board[r_, c_] == "__":
                        print("Your pawn has reached the last row")
                        print("Enter 1 to promote to queen.", "Enter 2 to promote to a knight",
                              "Enter 3 to promote to a rook.", "Enter 4 to promote to a bishop", sep="\n")
                        change = int(input(">>>"))

                        if change == 1:
                            Board[r, c], Board[r_, c_] = "__", "wQ"
                        elif change == 2:
                            Board[r, c], Board[r_, c_] = "__", "wK"
                        elif change == 3:
                            Board[r, c], Board[r_, c_] = "__", "wR"
                        elif change == 4:
                            Board[r, c], Board[r_, c_] = "__", "wB"
                        else:
                            raise MoveNotPossibleError

                    elif Board[r_, c_] == "__":
                        before_after_check(from_sq, to_sq, "wP")

                    else:
                        raise MoveNotPossibleError
                else:
                    raise MoveNotPossibleError

            elif c in range(7) and c_ == c + 1 and r_ == r - 1:

                # En-Passant
                if r == 3 and moves[-1][0] == "bP" and Board[r_, c_] == "__":
                    black_pawn_r, black_pawn_c = index(moves[-1][1])
                    black_pawn_r_, black_pawn_c_ = index(moves[-1][2])

                    if black_pawn_r == 1 and black_pawn_r_ == 3 and black_pawn_c_ == c + 1:
                        if [r_, c_] == [r - 1, black_pawn_c_]:

                            Board[r, c], Board[r_, c_] = "__", "wP"
                            Board[black_pawn_r_, black_pawn_c_] = "__"
                            if check(player):
                                Board[r, c], Board[r_, c_] = "wP", "__"
                                Board[black_pawn_r_, black_pawn_c_] = "bP"
                                raise MoveNotPossibleError
                            else:
                                return

                #   Pawn Promotion
                elif r_ == 0 and Board[r_, c_][0] == "b":
                    print("Your pawn has reached the last row")
                    print("Enter 1 to promote to queen.", "Enter 2 to promote to a knight",
                          "Enter 3 to promote to a rook.", "Enter 4 to promote to a bishop", sep="\n")
                    change = int(input(">>>"))

                    if change == 1:
                        Board[r, c], Board[r_, c_] = "__", "wQ"
                    elif change == 2:
                        Board[r, c], Board[r_, c_] = "__", "wK"
                    elif change == 3:
                        Board[r, c], Board[r_, c_] = "__", "wR"
                    elif change == 4:
                        Board[r, c], Board[r_, c_] = "__", "wB"
                    else:
                        raise MoveNotPossibleError

                elif Board[r_, c_][0] == "b":
                    before_after_check(from_sq, to_sq, "wP")

                else:
                    raise MoveNotPossibleError

            elif c in range(1, 8) and c_ == c - 1 and r_ == r - 1:

                # En-Passant
                if r == 3 and moves[-1][0] == "bP" and Board[r_, c_] == "__":
                    black_pawn_r, black_pawn_c = index(moves[-1][1])
                    black_pawn_r_, black_pawn_c_ = index(moves[-1][2])

                    if black_pawn_r == 1 and black_pawn_r_ == 3 and black_pawn_c_ == c - 1:
                        if [r_, c_] == [r - 1, black_pawn_c_]:

                            Board[r, c], Board[r_, c_] = "__", "wP"
                            Board[black_pawn_r_, black_pawn_c_] = "__"
                            if check(player):
                                Board[r, c], Board[r_, c_] = "wP", "__"
                                Board[black_pawn_r_, black_pawn_c_] = "bP"
                                raise MoveNotPossibleError
                            else:
                                return

                #   Pawn Promotion
                elif r_ == 0 and Board[r_, c_][0] == "b":
                    print("Your pawn has reached the last row")
                    print("Enter 1 to promote to queen.", "Enter 2 to promote to a knight",
                          "Enter 3 to promote to a rook.", "Enter 4 to promote to a bishop", sep="\n")
                    change = int(input(">>>"))

                    if change == 1:
                        Board[r, c], Board[r_, c_] = "__", "wQ"
                    elif change == 2:
                        Board[r, c], Board[r_, c_] = "__", "wK"
                    elif change == 3:
                        Board[r, c], Board[r_, c_] = "__", "wR"
                    elif change == 4:
                        Board[r, c], Board[r_, c_] = "__", "wB"
                    else:
                        raise MoveNotPossibleError

                elif Board[r_, c_][0] == "b":
                    before_after_check(from_sq, to_sq, "wP")

                else:
                    raise MoveNotPossibleError

            else:
                raise MoveNotPossibleError
        else:
            raise MoveNotPossibleError

    elif player == "b":
        if Board[r, c] == "bP":
            if c == c_:
                if r == 1 and r_ == 3:
                    if Board[r + 1, c] == "__" and Board[r_, c_] == "__":
                        before_after_check(from_sq, to_sq, "bP")
                elif r_ == r + 1:

                    #   Pawn Promotion
                    if r_ == 7 and Board[r_, c_] == "__":
                        print("Your pawn has reached the last row")
                        print("Enter 1 to promote to queen.", "Enter 2 to promote to a knight",
                              "Enter 3 to promote to a rook.", "Enter 4 to promote to a bishop", sep="\n")
                        change = int(input(">>>"))

                        if change == 1:
                            Board[r, c], Board[r_, c_] = "__", "bQ"
                        elif change == 2:
                            Board[r, c], Board[r_, c_] = "__", "bK"
                        elif change == 3:
                            Board[r, c], Board[r_, c_] = "__", "bR"
                        elif change == 4:
                            Board[r, c], Board[r_, c_] = "__", "bB"
                        else:
                            raise MoveNotPossibleError

                    elif Board[r_, c_] == "__":
                        before_after_check(from_sq, to_sq, "bP")

                    else:
                        raise MoveNotPossibleError
                else:
                    raise MoveNotPossibleError

            elif c in range(7) and c_ == c + 1 and r_ == r + 1:

                # En-Passant
                if r == 4 and moves[-1][0] == "wP" and Board[r_, c_] == "__":
                    white_pawn_r, white_pawn_c = index(moves[-1][1])
                    white_pawn_r_, white_pawn_c_ = index(moves[-1][2])

                    if white_pawn_r == 6 and white_pawn_r_ == 4 and white_pawn_c_ == c + 1:
                        if [r_, c_] == [r + 1, white_pawn_c_]:

                            Board[r, c], Board[r_, c_] = "__", "bP"
                            Board[white_pawn_r_, white_pawn_c_] = "__"
                            if check(player):
                                Board[r, c], Board[r_, c_] = "bP", "__"
                                Board[white_pawn_r_, white_pawn_c_] = "wP"
                                raise MoveNotPossibleError
                            else:
                                return

                #   Pawn Promotion
                elif r_ == 7 and Board[r_, c_][0] == "b":
                    print("Your pawn has reached the last row")
                    print("Enter 1 to promote to queen.", "Enter 2 to promote to a knight",
                          "Enter 3 to promote to a rook.", "Enter 4 to promote to a bishop", sep="\n")
                    change = int(input(">>>"))

                    if change == 1:
                        Board[r, c], Board[r_, c_] = "__", "bQ"
                    elif change == 2:
                        Board[r, c], Board[r_, c_] = "__", "bK"
                    elif change == 3:
                        Board[r, c], Board[r_, c_] = "__", "bR"
                    elif change == 4:
                        Board[r, c], Board[r_, c_] = "__", "bB"
                    else:
                        raise MoveNotPossibleError

                elif Board[r_, c_][0] == "w":
                    before_after_check(from_sq, to_sq, "bP")

                else:
                    raise MoveNotPossibleError

            elif c in range(1, 8) and c_ == c - 1 and r_ == r + 1:

                # En-Passant
                if r == 4 and moves[-1][0] == "wP" and Board[r_, c_] == "__":
                    white_pawn_r, white_pawn_c = index(moves[-1][1])
                    white_pawn_r_, white_pawn_c_ = index(moves[-1][2])

                    if white_pawn_r == 6 and white_pawn_r_ == 4 and white_pawn_c_ == c - 1:
                        if [r_, c_] == [r + 1, white_pawn_c_]:

                            Board[r, c], Board[r_, c_] = "__", "bP"
                            Board[white_pawn_r_, white_pawn_c_] = "__"
                            if check(player):
                                Board[r, c], Board[r_, c_] = "bP", "__"
                                Board[white_pawn_r_, white_pawn_c_] = "wP"
                                raise MoveNotPossibleError
                            else:
                                return

                #   Pawn Promotion
                elif r_ == 7 and Board[r_, c_][0] == "w":
                    print("Your pawn has reached the last row")
                    print("Enter 1 to promote to queen.", "Enter 2 to promote to a knight",
                          "Enter 3 to promote to a rook.", "Enter 4 to promote to a bishop", sep="\n")
                    change = int(input(">>>"))

                    if change == 1:
                        Board[r, c], Board[r_, c_] = "__", "bQ"
                    elif change == 2:
                        Board[r, c], Board[r_, c_] = "__", "bK"
                    elif change == 3:
                        Board[r, c], Board[r_, c_] = "__", "bR"
                    elif change == 4:
                        Board[r, c], Board[r_, c_] = "__", "bB"
                    else:
                        raise MoveNotPossibleError

                elif Board[r_, c_][0] == "w":
                    before_after_check(from_sq, to_sq, "bP")

                else:
                    raise MoveNotPossibleError

            else:
                raise MoveNotPossibleError
        else:
            raise MoveNotPossibleError


# for the knights -
def knight_moves(player, from_sq, to_sq):
    r, c = index(from_sq)
    r_, c_ = index(to_sq)

    if Board[r_, c_][0] == player:
        raise MoveNotPossibleError

    if Board[r, c] == player + "K":
        if [r, c] == [0, 0]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r + i, c + j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            else:
                raise MoveNotPossibleError

        elif [r, c] == [0, 7]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r + i, c - j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            else:
                raise MoveNotPossibleError

        elif [r, c] == [7, 0]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r - j, c + i] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            else:
                raise MoveNotPossibleError

        elif [r, c] == [7, 7]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r - i, r - j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            else:
                raise MoveNotPossibleError

        elif [r, c] == [0, 1]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r + i, c + j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            if [r + 2, c - 1] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            else:
                raise MoveNotPossibleError

        elif [r, c] == [0, 6]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r + i, c - j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            if [r + 2, c + 1] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            else:
                raise MoveNotPossibleError

        elif [r, c] == [1, 0]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r + i, c + j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            if [r - 2, c + 1] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            else:
                raise MoveNotPossibleError

        elif [r, c] == [1, 7]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r + i, c - j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            if [r - 1, c - 2] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            else:
                raise MoveNotPossibleError

        elif [r, c] == [6, 0]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r - i, c + j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            if [r + 1, c + 2] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            else:
                raise MoveNotPossibleError

        elif [r, c] == [6, 7]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r - i, c - j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            if [r + 1, c - 2] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            else:
                raise MoveNotPossibleError

        elif [r, c] == [7, 1]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r - i, c + j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            if [r - 2, c - 1] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            else:
                raise MoveNotPossibleError

        elif [r, c] == [7, 6]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r - i, c - j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            if [r - 2, c + 1] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            else:
                raise MoveNotPossibleError

        elif [r, c] == [1, 1]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r + i, c + j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            if [r - 1, c + 2] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            elif [r + 2, c - 1] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            else:
                raise MoveNotPossibleError

        elif [r, c] == [1, 6]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r + i, c - j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            if [r - 1, c - 2] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            elif [r + 2, c + 1] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            else:
                raise MoveNotPossibleError

        elif [r, c] == [6, 1]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r - i, c + j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            if [r + 1, c + 2] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            elif [r - 2, c - 1] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            else:
                raise MoveNotPossibleError

        elif [r, c] == [6, 6]:
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r - i, c - j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            if [r + 1, c - 2] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            elif [r - 2, c + 1] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            else:
                raise MoveNotPossibleError

        elif c == 0 and r in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r + i, c + j] == [r_, c_] or [r - i, c + j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            else:
                raise MoveNotPossibleError
        elif r == 0 and c in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r + i, c + j] == [r_, c_] or [r + i, c - j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            else:
                raise MoveNotPossibleError
        elif r == 7 and c in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r - j, c - i] == [r_, c_] or [r - j, c + i] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            else:
                raise MoveNotPossibleError
        elif c == 7 and r in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r + i, c - j] == [r_, c_] or [r - i, c - j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            else:
                raise MoveNotPossibleError
        elif c == 1 and r in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r + i, c + j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
                elif [r - i, c + j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            if [r + 2, c - 1] == [r_, c_] or [r - 2, c - 1] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            else:
                raise MoveNotPossibleError

        elif c == 6 and r in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r - i, c - j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
                elif [r + i, c - j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            if [r + 2, c + 1] == [r_, c_] or [r - 2, c + 1] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            else:
                raise MoveNotPossibleError

        elif r == 1 and c in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r + i, c - j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
                elif [r + i, c + j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            if [r - 1, c - 2] == [r_, c_] or [r - 1, c + 2] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            else:
                raise MoveNotPossibleError

        elif r == 6 and c in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r - i, c + j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
                elif [r - i, c - j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            if [r + 1, c + 2] == [r_, c_] or [r + 1, c - 2] == [r_, c_]:
                before_after_check(from_sq, to_sq, player + "K")
                return
            else:
                raise MoveNotPossibleError

        elif r in range(2, 6) and c in range(2, 6):
            for i, j in zip(range(1, 3), range(2, 0, -1)):
                if [r + i, c + j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
                elif [r + i, c - j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
                elif [r - i, c + j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
                elif [r - i, c - j] == [r_, c_]:
                    before_after_check(from_sq, to_sq, player + "K")
                    return
            else:
                raise MoveNotPossibleError

        else:
            raise MoveNotPossibleError
    else:
        raise MoveNotPossibleError


# for the rooks and moves of queen in the same row or column -
def same_file_moves(from_sq, to_sq, piece):
    r, c = index(from_sq)
    r_, c_ = index(to_sq)

    if Board[r_, c_][0] == piece[0]:
        raise MoveNotPossibleError

    if Board[r, c] == piece:

        if (r_ != r) and (c_ != c):
            raise MoveNotPossibleError

        if r_ == r and c_ > c:
            i = 1
            while c != c_ - i:
                if Board[r, c + i] != "__":
                    raise MoveNotPossibleError
                i += 1

            else:
                before_after_check(from_sq, to_sq, piece)

        if r_ == r and c_ < c:
            i = 1
            while c - i != c_:
                if Board[r, c - i] != "__":
                    raise MoveNotPossibleError
                i += 1

            else:
                before_after_check(from_sq, to_sq, piece)

        if c_ == c and r_ > r:
            i = 1
            while r != r_ - i:
                if Board[r + i, c] != "__":
                    raise MoveNotPossibleError
                i += 1

            else:
                before_after_check(from_sq, to_sq, piece)

        if c_ == c and r_ < r:
            i = 1
            while r - i != r_:
                if Board[r - i, c] != "__":
                    raise MoveNotPossibleError
                i += 1

            else:
                before_after_check(from_sq, to_sq, piece)

    else:
        raise MoveNotPossibleError


# for the bishops and diagonal moves of the queen -
def diagonal_moves(from_sq, to_sq, piece):
    r, c = index(from_sq)
    r_, c_ = index(to_sq)

    if Board[r_, c_][0] == piece[0]:
        raise MoveNotPossibleError

    if Board[r, c] == piece:

        if r_ < r and c_ < c:
            i = 1
            while [r - i, c - i] != [r_, c_]:
                if Board[r - i, c - i] != "__":
                    raise MoveNotPossibleError
                i += 1

            else:
                before_after_check(from_sq, to_sq, piece)

        elif r_ < r and c_ > c:
            i = 1
            while [r - i, c + i] != [r_, c_]:
                if Board[r - i, c + i] != "__":
                    raise MoveNotPossibleError
                i += 1

            else:
                before_after_check(from_sq, to_sq, piece)

        elif r_ > r and c_ < c:
            i = 1
            while [r + i, c - i] != [r_, c_]:
                if Board[r + i, c - i] != "__":
                    raise MoveNotPossibleError
                i += 1

            else:
                before_after_check(from_sq, to_sq, piece)

        elif r_ > r and c_ > c:
            i = 1
            while [r + i, c + i] != [r_, c_]:
                if Board[r + i, c + i] != "__":
                    raise MoveNotPossibleError
                i += 1

            else:
                before_after_check(from_sq, to_sq, piece)

        else:
            raise MoveNotPossibleError

    else:
        raise MoveNotPossibleError


# for the queens - 
def queen_moves(from_sq, to_sq, piece):
    while True:
        try:
            same_file_moves(from_sq, to_sq, piece)
            break
        except MoveNotPossibleError:
            try:
                diagonal_moves(from_sq, to_sq, piece)
                break
            except MoveNotPossibleError:
                raise MoveNotPossibleError


# for king moves -
def king_moves(player, from_sq, to_sq):
    r, c = index(from_sq)
    r_, c_ = index(to_sq)
    piece_to_be_taken = Board[r_, c_]

    if player == "w":
        if Board[r, c] != "wO":
            raise MoveNotPossibleError
        else:
            # Short side castle
            if [r, c] == [7, 4] and [r_, c_] == [7, 6]:
                if not check(player):
                    if Board[r, c + 1] == "__" and Board[r, c + 2] == "__" and Board[7, 7] == "wR":
                        Board[r, c], Board[r, c + 1] = "__", "wO"
                        if check(player):
                            Board[r, c], Board[r, c + 1] = "wO", "__"
                            raise MoveNotPossibleError
                        else:
                            Board[r, c + 1], Board[r_, c_] = "__", "wO"
                            if check(player):
                                Board[r, c], Board[r, c + 1] = "wO", "__"
                                raise MoveNotPossibleError
                            else:
                                Board[r, c + 1], Board[7, 7] = "wR", "__"
                                return

            # Long side castle
            elif [r, c] == [7, 4] and [r_, c_] == [7, 1]:
                if not check(player):
                    if Board[r, c - 1] == "__" and Board[r, c - 2] == "__" and Board[r, c - 3] == "__" \
                            and Board[7, 0] == "wR":
                        Board[r, c], Board[r, c - 1] = "__", "wO"
                        if check(player):
                            Board[r, c], Board[r, c - 1] = "wO", "__"
                            raise MoveNotPossibleError
                        else:
                            Board[r, c - 1], Board[r, c - 2] = "__", "wO"
                            if check(player):
                                Board[r, c], Board[r, c - 2] = "wO", "__"
                                raise MoveNotPossibleError
                            else:
                                Board[r, c - 2], Board[r_, c_] = "__", "wO"
                                if check(player):
                                    Board[r, c], Board[r_, c_] = "wO", "__"
                                    raise MoveNotPossibleError
                                else:
                                    Board[r_, c_ + 1], Board[7, 0] = "wR", "__"
                                    return

    elif player == "b":
        if Board[r, c] != "bO":
            raise MoveNotPossibleError
        else:
            # Short side castle
            if [r, c] == [0, 4] and [r_, c_] == [0, 6]:
                if not check(player):
                    if Board[r, c + 1] == "__" and Board[r, c + 2] == "__" and Board[0, 7] == "bR":
                        Board[r, c], Board[r, c + 1] = "__", "bO"
                        if check(player):
                            Board[r, c], Board[r, c + 1] = "bO", "__"
                            raise MoveNotPossibleError
                        else:
                            Board[r, c + 1], Board[r_, c_] = "__", "bO"
                            if check(player):
                                Board[r, c], Board[r, c + 1] = "bO", "__"
                                raise MoveNotPossibleError
                            else:
                                Board[r, c + 1], Board[0, 7] = "bR", "__"
                                return

            # Long side castle
            elif [r, c] == [0, 4] and [r_, c_] == [0, 1]:
                if not check(player):
                    if Board[r, c - 1] == "__" and Board[r, c - 2] == "__" and Board[r, c - 3] == "__" \
                            and Board[0, 0] == "bR":
                        Board[r, c], Board[r, c - 1] = "__", "bO"
                        if check(player):
                            Board[r, c], Board[r, c - 1] = "bO", "__"
                            raise MoveNotPossibleError
                        else:
                            Board[r, c - 1], Board[r, c - 2] = "__", "bO"
                            if check(player):
                                Board[r, c], Board[r, c - 2] = "bO", "__"
                                raise MoveNotPossibleError
                            else:
                                Board[r, c - 2], Board[r_, c_] = "__", "bO"
                                if check(player):
                                    Board[r, c], Board[r_, c_] = "bO", "__"
                                    raise MoveNotPossibleError
                                else:
                                    Board[r_, c_ + 1], Board[0, 0] = "bR", "__"
                                    return

    if Board[r, c] == player + "O":
        if player == "w" and Board[r_, c_] == "bO":
            raise MoveNotPossibleError
        elif player == "b" and Board[r_, c_] == "wO":
            raise MoveNotPossibleError

        if [r, c] == [0, 0]:
            if [r_, c_] in [[0, 1], [1, 1], [1, 0]]:
                Board[r, c], Board[r_, c_] = "__", player + "O"
                if check(player):
                    Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken
                    raise MoveNotPossibleError
            else:
                raise MoveNotPossibleError

        elif [r, c] == [0, 7]:
            if [r_, c_] in [[0, 6], [1, 6], [1, 7]]:
                Board[r, c], Board[r_, c_] = "__", player + "O"
                if check(player):
                    Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken
                    raise MoveNotPossibleError
            else:
                raise MoveNotPossibleError

        elif [r, c] == [7, 0]:
            if [r_, c_] in [[7, 1], [6, 0], [6, 1]]:
                Board[r, c], Board[r_, c_] = "__", player + "O"
                if check(player):
                    Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken
                    raise MoveNotPossibleError
            else:
                raise MoveNotPossibleError

        elif [r, c] == [7, 7]:
            if [r_, c_] in [[7, 6], [6, 6], [6, 7]]:
                Board[r, c], Board[r_, c_] = "__", player + "O"
                if check(player):
                    Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken
                    raise MoveNotPossibleError
            else:
                raise MoveNotPossibleError

        found = False
        if r == 0 and c in range(1, 7):
            for i in range(2):
                if found:
                    return
                for j in range(-1, 2):
                    if [r + i, c + j] == [r_, c_]:
                        found = True
                        Board[r, c], Board[r_, c_] = "__", player + "O"
                        if check(player):
                            Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken
                            raise MoveNotPossibleError
                        break

        elif r == 7 and c in range(1, 7):
            for i in range(-1, 1):
                if found:
                    return
                for j in range(-1, 2):
                    if [r + i, c + j] == [r_, c_]:
                        found = True
                        Board[r, c], Board[r_, c_] = "__", player + "O"
                        if check(player):
                            Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken
                            raise MoveNotPossibleError
                        break

        elif c == 0 and r in range(1, 7):
            for i in range(-1, 2):
                if found:
                    return
                for j in range(2):
                    if [r + i, c + j] == [r_, c_]:
                        found = True
                        Board[r, c], Board[r_, c_] = "__", player + "O"
                        if check(player):
                            Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken
                            raise MoveNotPossibleError
                        break

        elif c == 7 and r in range(1, 7):
            for i in range(-1, 2):
                if found:
                    return
                for j in range(-1, 1):
                    if [r + i, c + j] == [r_, c_]:
                        found = True
                        Board[r, c], Board[r_, c_] = "__", player + "O"
                        if check(player):
                            Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken
                            raise MoveNotPossibleError
                        break

        else:
            found = False
            for i in range(-1, 2):
                if found:
                    return
                for j in range(-1, 2):
                    if [r + i, c + j] == [r_, c_]:
                        found = True
                        Board[r, c], Board[r_, c_] = "__", player + "O"
                        if check(player):
                            Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken
                            raise MoveNotPossibleError
                        break

        if not found:
            raise MoveNotPossibleError

    else:
        raise MoveNotPossibleError


def is_checkmate_stalemate(player):
    list_of_pieces = []
    if player == "b":
        r = 0
        c = 0
        for row in Board:
            for piece in row:
                if piece[0] == "b":
                    list_of_pieces.append([piece, r, c])
                c += 1
            c = 0
            r += 1
    elif player == "w":
        r = 0
        c = 0
        for row in Board:
            for piece in row:
                if piece[0] == "w":
                    list_of_pieces.append([piece, r, c])
                c += 1
            c = 0
            r += 1
    # else:
    # some error
    found = False
    for data in list_of_pieces:

        if data[0][1] == "O":
            r, c = data[1], data[2]
            if [r, c] == [0, 0]:
                for [r_, c_] in [[0, 1], [1, 1], [1, 0]]:
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", player + "O"
                    if not check(player):
                        Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken

            elif [r, c] == [0, 7]:
                for [r_, c_] in [[0, 6], [1, 6], [1, 7]]:
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", player + "O"
                    if not check(player):
                        Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken

            elif [r, c] == [7, 0]:
                for [r_, c_] in [[7, 1], [6, 0], [6, 1]]:
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", player + "O"
                    if not check(player):
                        Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken

            elif [r, c] == [7, 7]:
                for [r_, c_] in [[7, 6], [6, 6], [6, 7]]:
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", player + "O"
                    if not check(player):
                        Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken

            elif r == 0 and c in range(1, 7):
                for i in range(2):
                    for j in range(-1, 2):
                        [r_, c_] = [r + i, c + j]
                        piece_to_be_taken = Board[r_, c_]
                        if Board[r_, c_][0] == player:
                            continue
                        Board[r, c], Board[r_, c_] = "__", player + "O"
                        if not check(player):
                            Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken
                            return
                        Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken

            elif r == 7 and c in range(1, 7):
                for i in range(-1, 1):
                    for j in range(-1, 2):
                        [r_, c_] = [r + i, c + j]
                        piece_to_be_taken = Board[r_, c_]
                        if Board[r_, c_][0] == player:
                            continue
                        Board[r, c], Board[r_, c_] = "__", player + "O"
                        if not check(player):
                            Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken
                            return
                        Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken

            elif c == 0 and r in range(1, 7):
                for i in range(-1, 2):
                    for j in range(2):
                        [r_, c_] = [r + i, c + j]
                        piece_to_be_taken = Board[r_, c_]
                        if Board[r_, c_][0] == player:
                            continue
                        Board[r, c], Board[r_, c_] = "__", player + "O"
                        if not check(player):
                            Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken
                            return
                        Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken

            elif c == 7 and r in range(1, 7):
                for i in range(-1, 2):

                    for j in range(-1, 1):
                        [r_, c_] = [r + i, c + j]
                        piece_to_be_taken = Board[r_, c_]
                        if Board[r_, c_][0] == player:
                            continue
                        Board[r, c], Board[r_, c_] = "__", player + "O"
                        if not check(player):
                            Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken
                            return
                        Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken

            else:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        [r_, c_] = [r + i, c + j]
                        piece_to_be_taken = Board[r_, c_]
                        if Board[r_, c_][0] == player:
                            continue
                        Board[r, c], Board[r_, c_] = "__", player + "O"
                        if not check(player):
                            Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken
                            return
                        Board[r, c], Board[r_, c_] = player + "O", piece_to_be_taken

            found = True

        elif data[0][1] == "P":
            r, c = data[1], data[2]
            if player == "b":
                if r == 1:
                    r_ = 3
                    if Board[r_, c] == "__":
                        Board[r, c], Board[r_, c] = "__", "bP"
                        if not check(player):
                            Board[r, c], Board[r_, c] = "bP", "__"
                            return
                        Board[r, c], Board[r_, c] = "bP", "__"

                if Board[r + 1, c] == "__":
                    Board[r, c], Board[r + 1, c] = "__", "bP"
                    if not check(player):
                        Board[r, c], Board[r + 1, c] = "bP", "__"
                        return
                    Board[r, c], Board[r + 1, c] = "bP", "__"

                if c in range(1, 8):
                    if Board[r + 1, c - 1] != "__" and Board[r + 1, c - 1][0] != "b":
                        piece_to_be_taken = Board[r + 1, c - 1]
                        Board[r, c], Board[r + 1, c - 1] = "__", "bP"
                        if not check(player):
                            Board[r, c], Board[r + 1, c - 1] = "bP", piece_to_be_taken
                            return
                        Board[r, c], Board[r + 1, c - 1] = "bP", piece_to_be_taken

                if c in range(0, 7):
                    if Board[r + 1, c + 1] != "__" and Board[r + 1, c + 1][0] != "b":
                        piece_to_be_taken = Board[r + 1, c + 1]
                        Board[r, c], Board[r + 1, c + 1] = "__", "bP"
                        if not check(player):
                            Board[r, c], Board[r + 1, c + 1] = "bP", piece_to_be_taken
                            return
                        Board[r, c], Board[r + 1, c + 1] = "bP", piece_to_be_taken

                found = True

            elif player == "w":
                if r == 6:
                    r_ = 4
                    if Board[r_, c] == "__":
                        Board[r, c], Board[r_, c] = "__", "wP"
                        if not check(player):
                            Board[r, c], Board[r_, c] = "wP", "__"
                            return
                        Board[r, c], Board[r_, c] = "wP", "__"

                if Board[r - 1, c] == "__":
                    Board[r, c], Board[r - 1, c] = "__", "wP"
                    if not check(player):
                        Board[r, c], Board[r - 1, c] = "wP", "__"
                        return
                    Board[r, c], Board[r - 1, c] = "wP", "__"

                if c in range(1, 8):
                    if Board[r - 1, c - 1] != "__" and Board[r - 1, c - 1][0] != "w":
                        piece_to_be_taken = Board[r - 1, c - 1]
                        Board[r, c], Board[r - 1, c - 1] = "__", "wP"
                        if not check(player):
                            Board[r, c], Board[r - 1, c - 1] = "wP", piece_to_be_taken
                            return
                        Board[r, c], Board[r - 1, c - 1] = "wP", piece_to_be_taken

                if c in range(0, 7):
                    if Board[r - 1, c + 1] != "__" and Board[r - 1, c + 1][0] != "w":
                        piece_to_be_taken = Board[r - 1, c + 1]
                        Board[r, c], Board[r - 1, c + 1] = "__", "wP"
                        if not check(player):
                            Board[r, c], Board[r - 1, c + 1] = "wP", piece_to_be_taken
                            return
                        Board[r, c], Board[r - 1, c + 1] = "wP", piece_to_be_taken

                found = True

        elif data[0][1] == "K":
            r, c = data[1], data[2]
            if [r, c] == [0, 0]:
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r + i, c + j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif [r, c] == [0, 7]:
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r + i, c - j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif [r, c] == [7, 0]:
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r - i, c + j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        pass
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif [r, c] == [7, 7]:
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r - i, c - j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif [r, c] == [0, 1]:
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r + i, c + j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                r_, c_ = r + 2, c - 1
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif [r, c] == [0, 6]:
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r + i, c - j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                r_, c_ = r + 2, c + 1
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif [r, c] == [1, 0]:
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r + i, c + j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                r_, c_ = r - 2, c + 1
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif [r, c] == [1, 7]:
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r + i, c - j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                r_, c_ = r - 1, c - 2
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif [r, c] == [6, 0]:
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r - i, c + j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                r_, c_ = r + 1, c + 2
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif [r, c] == [6, 7]:
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r - i, c - j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                r_, c_ = r + 1, c - 2
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif [r, c] == [7, 1]:
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r - i, c + j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                r_, c_ = r - 2, c - 1
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif [r, c] == [7, 6]:
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r - i, c - j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                r_, c_ = r - 2, c + 1
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif [r, c] == [1, 1]:
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r + i, c + j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                r_, c_ = r + 2, c - 1
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                r_, c_ = r - 1, c + 2
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif [r, c] == [1, 6]:
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r + i, c - j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                r_, c_ = r + 2, c + 1
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                r_, c_ = r - 1, c - 2
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif [r, c] == [6, 1]:
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r - i, c + j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                r_, c_ = r - 2, c - 1
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                r_, c_ = r + 1, c + 2
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif [r, c] == [6, 6]:
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r - i, c - j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                r_, c_ = r - 2, c + 1
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                r_, c_ = r + 1, c - 2
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif c == 0 and r in range(2, 6):
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r + i, c + j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    r_, c_ = r - i, c + j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif r == 0 and c in range(2, 6):
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r + i, c + j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    r_, c_ = r + i, c - j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif r == 7 and c in range(2, 6):
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r - j, c - i
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    r_, c_ = r - j, c + i
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif c == 7 and r in range(2, 6):
                for i, j in zip(range(1, 3), range(2, 0, -1)):
                    r_, c_ = r + i, c - j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    r_, c_ = r - i, c - j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif c == 1 and r in range(2, 6):
                for i, j in zip(range(1, 3), range(2, 0, -1)):

                    r_, c_ = r + i, c + j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

                    r_, c_ = r - i, c + j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

                r_, c_ = r + 2, c - 1
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

                r_, c_ = r - 2, c - 1
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif c == 6 and r in range(2, 6):
                for i, j in zip(range(1, 3), range(2, 0, -1)):

                    r_, c_ = r - i, c - j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

                    r_, c_ = r + i, c - j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

                r_, c_ = r + 2, c + 1
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

                r_, c_ = r - 2, c + 1
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif r == 1 and c in range(2, 6):
                for i, j in zip(range(1, 3), range(2, 0, -1)):

                    r_, c_ = r + i, c - j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

                    r_, c_ = r + i, c + j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

                r_, c_ = r - 1, c - 2
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

                r_, c_ = r - 1, c + 2
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif r == 6 and c in range(2, 6):
                for i, j in zip(range(1, 3), range(2, 0, -1)):

                    r_, c_ = r - i, c + j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

                    r_, c_ = r - i, c - j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

                r_, c_ = r + 1, c + 2
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                r_, c_ = r + 1, c - 2
                piece_to_be_taken = Board[r_, c_]
                if Board[r_, c_][0] == player:
                    continue
                Board[r, c], Board[r_, c_] = "__", data[0]
                if not check(player):
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                    return
                Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            elif r in range(2, 6) and c in range(2, 6):
                for i, j in zip(range(1, 3), range(2, 0, -1)):

                    r_, c_ = r + i, c + j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

                    r_, c_ = r + i, c - j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

                    r_, c_ = r - i, c + j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

                    r_, c_ = r - i, c - j
                    piece_to_be_taken = Board[r_, c_]
                    if Board[r_, c_][0] == player:
                        continue
                    Board[r, c], Board[r_, c_] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r_, c_] = data[0], piece_to_be_taken

            found = True

        elif data[0][1] == "B" or data[0][1] == "Q":
            r, c = data[1], data[2]

            if 0 < r and 0 < c:
                i = 1
                while (r - i != -1) and (c - i != -1):
                    if Board[r - i, c - i] == "__":
                        Board[r, c], Board[r - i, c - i] = "__", data[0]
                        if not check(player):
                            Board[r, c], Board[r - i, c - i] = data[0], "__"
                            return
                        Board[r, c], Board[r - i, c - i] = data[0], "__"
                    elif Board[r - i, c - i][0] != player:
                        piece_to_be_taken = Board[r - i, c - i]
                        Board[r, c], Board[r - i, c - i] = "__", data[0]
                        if not check(player):
                            Board[r, c], Board[r - i, c - i] = data[0], piece_to_be_taken
                            return
                        Board[r, c], Board[r - i, c - i] = data[0], piece_to_be_taken
                        found = True
                        break
                    else:
                        found = True
                        break
                    i += 1

            if 0 < r and 7 > c:
                i = 1
                while (r - i != -1) and (c + i != 8):
                    if Board[r - i, c + i] == "__":
                        Board[r, c], Board[r - i, c + i] = "__", data[0]
                        if not check(player):
                            Board[r, c], Board[r - i, c + i] = data[0], "__"
                            return
                        Board[r, c], Board[r - i, c + i] = data[0], "__"
                    elif Board[r - i, c + i][0] != player:
                        piece_to_be_taken = Board[r - i, c + i]
                        Board[r, c], Board[r - i, c + i] = "__", data[0]
                        if not check(player):
                            Board[r, c], Board[r - i, c + i] = data[0], piece_to_be_taken
                            return
                        Board[r, c], Board[r - i, c + i] = data[0], piece_to_be_taken
                        found = True
                        break
                    else:
                        found = True
                        break
                    i += 1

            if 7 > r and 7 > c:
                i = 1
                while (r + i != 8) and (c + i != 8):
                    if Board[r + i, c + i] == "__":
                        Board[r, c], Board[r + i, c + i] = "__", data[0]
                        if not check(player):
                            Board[r, c], Board[r + i, c + i] = data[0], "__"
                            return
                        Board[r, c], Board[r + i, c + i] = data[0], "__"
                    elif Board[r + i, c + i][0] != player:
                        piece_to_be_taken = Board[r + i, c + i]
                        Board[r, c], Board[r + i, c + i] = "__", data[0]
                        if not check(player):
                            Board[r, c], Board[r + i, c + i] = data[0], piece_to_be_taken
                            return
                        Board[r, c], Board[r + i, c + i] = data[0], piece_to_be_taken
                        found = True
                        break
                    else:
                        found = True
                        break
                    i += 1

            if 7 > r and 0 < c:
                i = 1
                while (r + i != 8) and (c - i != -1):
                    if Board[r + i, c - i] == "__":
                        Board[r, c], Board[r + i, c - i] = "__", data[0]
                        if not check(player):
                            Board[r, c], Board[r + i, c - i] = data[0], "__"
                            return
                        Board[r, c], Board[r + i, c - i] = data[0], "__"
                    elif Board[r + i, c - i][0] != player:
                        piece_to_be_taken = Board[r + i, c - i]
                        Board[r, c], Board[r + i, c - i] = "__", data[0]
                        if not check(player):
                            Board[r, c], Board[r + i, c - i] = data[0], piece_to_be_taken
                            return
                        Board[r, c], Board[r + i, c - i] = data[0], piece_to_be_taken
                        found = True
                        break
                    else:
                        found = True
                        break
                    i += 1

        if data[0][1] == "R" or data[0][1] == "Q":
            r, c = data[1], data[2]

            i = 1
            while r - i != -1:
                if Board[r - i, c] == "__":
                    Board[r, c], Board[r - i, c] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r - i, c] = data[0], "__"
                        return
                    Board[r, c], Board[r - i, c] = data[0], "__"
                elif Board[r - i, c][0] != player:
                    piece_to_be_taken = Board[r - i, c]
                    Board[r, c], Board[r - i, c] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r - i, c] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r - i, c] = data[0], piece_to_be_taken
                    found = True
                    break
                else:
                    found = True
                    break
                i += 1

            i = 1
            while r + i != 8:
                if Board[r + i, c] == "__":
                    Board[r, c], Board[r + i, c] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r + i, c] = data[0], "__"
                        return
                    Board[r, c], Board[r + i, c] = data[0], "__"
                elif Board[r + i, c][0] != player:
                    piece_to_be_taken = Board[r + i, c]
                    Board[r, c], Board[r + i, c] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r + i, c] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r + i, c] = data[0], piece_to_be_taken
                    found = True
                    break
                else:
                    found = True
                    break
                i += 1

            i = 1
            while c - i != -1:
                if Board[r, c - i] == "__":
                    Board[r, c], Board[r, c - i] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r, c - i] = data[0], "__"
                        return
                    Board[r, c], Board[r, c - i] = data[0], "__"
                elif Board[r, c - i][0] != player:
                    piece_to_be_taken = Board[r, c - i]
                    Board[r, c], Board[r, c - i] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r, c - i] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r, c - i] = data[0], piece_to_be_taken
                    found = True
                    break
                else:
                    found = True
                    break
                i += 1

            i = 1
            while c + i != 8:
                if Board[r, c + i] == "__":
                    Board[r, c], Board[r, c + i] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r, c + i] = data[0], "__"
                        return
                    Board[r, c], Board[r, c + i] = data[0], "__"
                elif Board[r, c + i][0] != player:
                    piece_to_be_taken = Board[r, c + i]
                    Board[r, c], Board[r, c + i] = "__", data[0]
                    if not check(player):
                        Board[r, c], Board[r, c + i] = data[0], piece_to_be_taken
                        return
                    Board[r, c], Board[r, c + i] = data[0], piece_to_be_taken
                    found = True
                    break
                else:
                    found = True
                    break
                i += 1

    if found:
        if check(player):
            raise CheckmateError
        else:
            raise StalemateError
    else:
        return
#


# Errors -
class MoveNotPossibleError(Exception):
    """The pieces cannot be moved to a certain square"""
    pass


class CheckmateError(Exception):
    """The game ended by checkmate"""
    pass


class StalemateError(Exception):
    """The game ended by stalemate"""
    pass


print("Welcome to the chess game:")
print("Two player chess (person vs person)", "w - represents the pieces of white", "b - represents the pieces of black",
      "P - represents Pawn", "R - represents Rook", "K - represents Knight", "B - represents Bishop",
      "Q - represents Queen", "O - represents King", sep="\n")
print()
board_display()

moves = []
game_end = False

while True:
    if game_end:
        break
    while True:
        # noinspection PyBroadException
        try:
            if game_end:
                break
            is_checkmate_stalemate("w")
            print("White's turn -")
            w_piece_to_move = input("Please enter the piece to move :")
            w_piece_from_sq = input("Please enter the square at which the piece is present :")
            w_piece_to_sq = input("Please enter the square to which you want to move the piece to :")

            if w_piece_to_move.upper() == "P":
                pawn_moves("w", w_piece_from_sq, w_piece_to_sq)
            elif w_piece_to_move.upper() == "K":
                knight_moves("w", w_piece_from_sq, w_piece_to_sq)
            elif w_piece_to_move.upper() == "B":
                diagonal_moves(w_piece_from_sq, w_piece_to_sq, "wB")
            elif w_piece_to_move.upper() == "R":
                same_file_moves(w_piece_from_sq, w_piece_to_sq, "wR")
            elif w_piece_to_move.upper() == "Q":
                queen_moves(w_piece_from_sq, w_piece_to_sq, "wQ")
            elif w_piece_to_move.upper() == "O":
                king_moves("w", w_piece_from_sq, w_piece_to_sq)
            else:
                print("Please enter a valid input")
                continue
            moves.append(["w" + w_piece_to_move.upper(), w_piece_from_sq, w_piece_to_sq])
            print()
            board_display()
            print()
            break
        except CheckmateError:
            print("Black wins by checkmate.")
            print("Thanks for playing.")
            game_end = True
            break

        except StalemateError:
            print("Stalemate.")
            print("Thanks for playing.")
            game_end = True
            break

        except:
            print("Please enter a valid input")

    while True:
        # noinspection PyBroadException
        try:
            if game_end:
                break
            is_checkmate_stalemate("b")
            print("Black's turn -")
            b_piece_to_move = input("Please enter the piece to move :")
            b_piece_from_sq = input("Please enter the square at which the piece is present :")
            b_piece_to_sq = input("Please enter the square to which you want to move the piece to :")

            if b_piece_to_move.upper() == "P":
                pawn_moves("b", b_piece_from_sq, b_piece_to_sq)
            elif b_piece_to_move.upper() == "K":
                knight_moves("b", b_piece_from_sq, b_piece_to_sq)
            elif b_piece_to_move.upper() == "B":
                diagonal_moves(b_piece_from_sq, b_piece_to_sq, "bB")
            elif b_piece_to_move.upper() == "R":
                same_file_moves(b_piece_from_sq, b_piece_to_sq, "bR")
            elif b_piece_to_move.upper() == "Q":
                queen_moves(b_piece_from_sq, b_piece_to_sq, "bQ")
            elif b_piece_to_move.upper() == "O":
                king_moves("b", b_piece_from_sq, b_piece_to_sq)
            else:
                print("Please enter a valid move")
                continue
            moves.append(["b" + b_piece_to_move.upper(), b_piece_from_sq, b_piece_to_sq])
            print()
            board_display()
            print()
            break

        except CheckmateError:
            print("White won by checkmate.")
            print("Thanks for playing.")
            game_end = True
            break

        except StalemateError:
            print("Stalemate.")
            print("Thanks for playing.")
            game_end = True
            break

        except:
            print("Please enter a valid input")
