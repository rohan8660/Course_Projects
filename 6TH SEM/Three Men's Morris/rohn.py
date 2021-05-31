# importing easyAI library components
from easyAI import TwoPlayersGame
from easyAI.Player import Human_Player

# inheriting TwoPlayersGame class


class morris3men (TwoPlayersGame):
    """
        The board positions are numbered as follows :
            7 8 9
            4 5 6
            1 2 3
    """

    def __init__(self, p):
        self.players = p
        self.board = [None for i in range(9)]
        self.nplayer = 1  # first move player(1 starts)

    def possible_moves(self):
        return [i+1 for i, e in enumerate(self.board) if e == 0]

    def make_move(self, move):
        self.board[int(move)-1] = self.nplayer

    def unmake_move(self, move):  # optional method (speeds up the AI)
        self.board[int(move)-1] = 0

    def lose(self):
        """ DID I LOSE ? LOSING CONDITIONS """
        return any(
            [
            all(
            [
            (
            self.board[c-1] == self.nopponent
                        )
                        for c in line
                    ]
                )
                for line in [
                            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # horizontal
                            [1, 4, 7], [2, 5, 8], [3, 6, 9]  # vertical
                        ]            ])

    def is_over(self):
        return(self.possible_moves() == []) or self.lose()

    #def show(self):
        #print(#current board)


    def scoring(self):
        return -100 if self.lose() else 0


if __name__ == "__main__":
    from easyAI import AI_Player, Negamax
    ai_algo = Negamax(6)
    count=0
    morris3men([Human_Player(), AI_Player(ai_algo)]).play()
