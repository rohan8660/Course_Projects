from easyAI import TwoPlayersGame
from easyAI.Player import Human_Player

class TTT( TwoPlayersGame ):
    """ The board positions are numbered as follows:
            7 8 9
            4 5 6
            1 2 3
    """  

    def __init__(self, players):
        self.players = players
        self.board = [0 for i in range(9)]  #setting all zeroes
        self.nplayer = 1                    # player 1 starts.

    def possible_moves(self):               #returns list of empty places from board
        ls=[]
        for i in range(len(self.board)):
            if(self.board[i]==0):
                ls.append(i)
        return(ls)

    def make_move( self, move):
        return()