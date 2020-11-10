
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
                    if i != 0 and j != len(self.board[i]) - 1 and self.board[i - 1][j + 1] == 0:
                        possibleMoves.append(([i, j],[i - 1,j + 1]))
                    if i != 0 and self.board[i][j - 1] == 0:
                        possibleMoves.append(([i, j],[i,j - 1]))
                    if j != len(self.board[i]) - 1 and self.board[i][j + 1] == 0:
                        possibleMoves.append(([i, j],[i,j + 1]))
                    if i != len(self.board) - 1 and j != 0 and self.board[i + 1][j - 1] == 0:
                        possibleMoves.append(([i, j],[i + 1,j - 1]))
                    if i != len(self.board) - 1 and self.board[i + 1][j] == 0:
                        possibleMoves.append(([i, j],[i + 1,j]))
                    if i != len(self.board) -1 and j != len(self.board[i]) - 1 and self.board[i + 1][j + 1] == 0:
                        possibleMoves.append(([i, j],[i + 1,j + 1]))
        return possibleMoves

    def evaluate(self):
        sum = 12
        for i in range(board):
            for j in range(board[i]):
                if self.board[i][j] == 1 or self.board[i][j] == 2:
                    sum = sum - i
        return sum

    def checkWinner(self):
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
                return 0 #remiza
        return -1

    def move(self, player, old_x, old_y, new_x, new_y):
        if abs(old_x - new_x) > 1 or abs(old_y - new_y) > 1 or abs(old_x - new_x) + abs(old_y - new_y) > 1:
            return -1
        if self.board[new_x][new_y] != 0:
            return -1
        if self.board[old_x][old_y] != player:
            print("c")
            return -1

        self.board[new_x][new_y], self.board[old_x][old_y] = self.board[old_x][old_y], self.board[new_x][new_y]
        return 1

    def printBoard(self):
        print(" _________")
        for line in self.board:
            print('|',line[0], line[1],line[2],line[3],'|')
        print(" _________")



    def minmax(self, x, y, depth, wantMax, board):
        if depth == 0 or board.checkWinner() != -1:
            return board.evaluate()

        if wantMax == 1: #we want to maximize the score if the player is the AI
            maxEval = float(12)
            best_move = None
            for move in self.checkPossibleMoves(2):
                pass
        elif wantMax == 0: #minimize the score of the opposing player (the human)
            pass
        




