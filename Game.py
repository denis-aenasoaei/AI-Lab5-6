class Game:
    def __init__(self, board):
        self.board = board

    def startGame(self):

        while 1:
            self.board.printBoard()
            if self.board.turn == 1:
                #human move
                while 1:
                    move = input("Write your move in the format \"old_x,old_y\" \"new_x,new_y\" (e.g. 3,2 3,3)\n")
                    old_pos = move.split(" ")[0]
                    new_pos = move.split(" ")[1]
                    try:
                        if self.board.move(1, int(old_pos.split(",")[0]), int(old_pos.split(",")[1]), int(new_pos.split(",")[0]), int(new_pos.split(",")[1])) == 1:
                            print("Successful move")
                            break
                        else:
                            print("Invalid move, try again")
                    except:
                        print("Invalid move, try again")
            elif self.board.turn == 2:
                pass
                #AI move :(

            winner = self.board.checkWinner()
            if winner == 1:
                print("You won!")
            elif winner == 2:
                print("Computer won!")
            elif winner == 0:
                print("It's a tie!")

            if winner != -1:
                print("Game ended, exiting...")
                break

            self.board.turn = ((self.board.turn + 1) % 2) + 1 #turn can take only values 1 and 2