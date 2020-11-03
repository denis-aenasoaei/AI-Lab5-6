

class Board:
    def __init__(self, turn = 1):
        self.size = 4
        self.board = [[2,2,2,2],
                      [0,0,0,0],
                      [0,0,0,0],
                      [1,1,1,1]]
        self.turn = turn

    def checkPossibleMoves(self, player):
        possibleMoves = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == player:
                    if i != 0 and j != 0 and self.board[i - 1][j - 1] == 0:
                        possibleMoves.append(([i, j],[i - 1,j - 1]))
                    if i != 0 and self.board[i - 1][j] == 0:
                        possibleMoves.append(([i, j],[i - 1,j]))
                    if i != 0 and j != len(self.board[i]) and self.board[i - 1][j + 1] == 0:
                        possibleMoves.append(([i, j],[i - 1,j + 1]))
                    if i != 0 and self.board[i][j - 1] == 0:
                        possibleMoves.append(([i, j],[i,j - 1]))
                    if j != len(self.board[i]) and self.board[i][j + 1] == 0:
                        possibleMoves.append(([i, j],[i,j + 1]))
                    if i != len(self.board) and j != 0 and self.board[i + 1][j - 1] == 0:
                        possibleMoves.append(([i, j],[i + 1,j - 1]))
                    if i != len(self.board) and self.board[i + 1][j] == 0:
                        possibleMoves.append(([i, j],[i + 1,j]))
                    if i != len(self.board) and j != len(self.board[i]) and self.board[i + 1][j + 1] == 0:
                        possibleMoves.append(([i, j],[i + 1,j + 1]))
        return possibleMoves

    def cehckWinner(self):
        for i in range(4):
            if len([x for x in self.board[0] if x == 1]) == 4:
                return 1
            if len([x for x in self.board[3] if x == 2]) == 4:
                return 2
        #check if there are no more possible moves
        if len(self.checkPossibleMoves(1)) == 0 or len(self.checkPossibleMoves(2)) == 0:
            p1 = [x for x in self.board[0] if x == 1]
            p2 = [x for x in self.board[3] if x == 2]
            if p1 > p2:
                return 1
            elif p2>p1:
                return 2
            else:
                return -1 #remiza
        return 0

    def printBoard(self):
        print("________")
        for line in self.board:
            print("|")
            for column in line:
                print(column, '')
            print('|')
        print("________")


