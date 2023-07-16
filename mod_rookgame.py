from numpy import array
from random import randint
from random import sample

_board = array([[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]])
field = _board

def biggame(flawless = True, _rook = None):
    for i in range(len(_board)):
        for j in range(len(_board)):
            if _board[i][j] == 11:
                _rook = _board[i][j]
                for k in range(len(_board)):
                    for l in range(len(_board)):
                        if (_board[k][l] == _rook and i == k and j != l 
                        or _board[k][l] == _rook and i != k and j == l
                        or _board[k][l] == _rook and i == k + 1 and j == l + 1
                        or _board[k][l] == _rook and i == k - 1 and j == l - 1):
                            flawless = False
                            return flawless
    return flawless

def setting(cols, lines):
    for i in range(len(_board)):
        _board[cols[i]][lines[i]] = 11
    print(f"{_board}\n\nВсе 8 ферзей живут дружно?\n {biggame()}")
    for i in range(len(_board)):
        _board[cols[i]][lines[i]] = 0

def rndgame():
    for s in range(4):
        c = sample(range(8), 8)
        cols = list()
        lines = list()
        i = 0
        while i < 8:
            cols.append(c[i])
            l = randint(0, 7)
            lines.append(l)
            i += 1
        setting(cols, lines)
    
# debug
col = [0, 1, 2, 3, 4, 5, 6, 7]
line = [3, 0, 4, 7, 1, 6, 2, 5]
setting(col, line)

rndgame()