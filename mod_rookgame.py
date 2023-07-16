from numpy import array
from random import randint

_board = array([[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]])
field = _board

def bigame(flawless = True, _rook = None):
    for i in range(len(_board)):
        for j in range(len(_board)):
            if _board[i][j] == 11:
                _rook = _board[i][j]
            for k in range(len(_board)):
                for l in range(len(_board)):
                    if _board[k][l] == _rook and i == k and j != l or _board[k][l] == _rook and i != k and j == l:
                        flawless = False
                        return flawless

def setting(cols, lines):
    for i in range(len(_board)):
        _board[cols[i]][lines[i]] = 11
    print(f"{_board}\n\nВсе 8 ферзей живут дружно?\n {bigame()}")
    for i in range(len(_board)):
        _board[cols[i]][lines[i]] = 0

def rndgame():
    for s in range(4):
        cols = list()
        lines = list()
        i = 0
        while i < 8:
            c = randint(0, 7)
            cols.append(c)
            l = randint(0, 7)
            lines.append(l)
            i += 1
        setting(cols, lines)
    

# col = [5, 7, 3, 4, 5, 0, 1, 2]
# line = [2, 0, 1, 4, 5, 2, 1, 2]
# setting(col, line)