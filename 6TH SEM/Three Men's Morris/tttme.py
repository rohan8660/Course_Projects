from easyAI import TwoPlayersGame
from easyAI.Player import Human_Player


class TTT(TwoPlayersGame):
    """ The board positions are numbered as follows:
            7 8 9   0 0 1
            4 5 6   0 0 0
            1 2 3   0 0 0
    """
    # moves 123456
    # index of board 0123456

    def __init__(self, players):
        self.players = players
        self.board = [0 for i in range(9)]  # setting all zeroes
        self.nplayer = 1                    # player 1 starts.

    def possible_moves(self):  # returns list of empty places from board
        ls = []
        for i in range(len(self.board)):
            if(self.board[i] == 0):
                ls.append(i+1)
        return(ls)

    def make_move(self, move):
        self.board[int(move)-1] = self.nplayer

    def unmake_move(self, move):  # optional method (speeds up the AI)
        self.board[int(move)-1] = 0

    def lose(self):
        """ Has the opponent "three in line ?" """
        return any([all([(self.board[c-1] == self.nopponent)
                         for c in line])
                    for line in [[1, 2, 3], [4, 5, 6], [7, 8, 9],  # horiz.
                                 [1, 4, 7], [2, 5, 8], [3, 6, 9],  # vertical
                                 [1, 5, 9], [3, 5, 7]]])  # diagonal

    def lose(self):
        """ Has the opponent "three in line ?" """
        ls = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # horizontal
            [1, 4, 7], [2, 5, 8], [3, 6, 9]]  # vertical
        for i in ls:
            for j in i:
                if(self.board[j-1] == self.nopponent):
                    if(i[-1] == j):
                        return 1
                    continue
                else:
                    break
        return 0

    def is_over(self):
        return (self.possible_moves() == []) or self.lose()

    def show(self):
        entries = ['-', 'O', 'x']
        for i in range(3):          # 0 1 2
            for j in range(3):      # 0 1 2
                str = (entries[self.board[3*i+j]])
                print(str, end=" ")
            print("")

    def scoring(self):
        return -100 if self.lose() else 0


# this is main function
if __name__ == "__main__":

    from easyAI import AI_Player, Negamax
    ai_algo = Negamax(6)
    TTT([Human_Player(), AI_Player(ai_algo)]).play()
