

class Board:
    def __init__(self):
        self.size = 4
        self.board = [[2,2,2,2],
                      [0,0,0,0],
                      [0,0,0,0],
                      [1,1,1,1]]

    def cehckWinner(self):
        for i in range(4):
            if len([x for x in self.board[0] if x == 1]) == 4:
                return 1
            if len([x for x in self.board[0] if x == 2]) == 4:
                return 2
        return 0
