# importing easyAI library components
from easyAI import TwoPlayersGame
from easyAI.Player import Human_Player

# inheriting TwoPlayersGame class


class MMM(TwoPlayersGame):
    """
        The board positions are numbered as follows :
            1 2 1
            2 1 2
            0 2 0
    """

    def __init__(self, p):
        self.players = p
        self.board = [0 for i in range(9)]
        self.nplayer = 1  # first move player(1 starts)


    def possible_moves(self):
        lss=["12","14","21","23","25","32","36","41","45","47","52","54","56","58","65","63","69","74","78","83","87","89","96","98"]
        if(self.nmove>6):
            ls=[]
            x=self.nplayer
            for i in lss:
                a=list(i)
                if(self.board[int(a[1])-1]==0 and self.board[int(a[0])-1]==(x)):
                    ls.append(i)
            # x=self.nplayer
            # for i, e in enumerate(self.board):
            #     if e == x :
            #         if(i+1+1==0):
            #             ls.append([i+1,i+1+1]) # move right
            #         if(i-1+1==0):
            #             ls.append([i+1,i-1+1]) # move right
            #         if(i+3+1==0):
            #             ls.append([i+1,i+3+1]) # move down
            #         if(i-3+1==0):
            #             ls.append([i+1,i-3+1]) # move up
            # for i in ls:
            #     if(i[1]<0 or i[1]>8):
            #         ls.remove(i)
            # for i in range(len(ls)):
            #     st=""
            #     for j in ls[i]:
            #         st+=str(j)                                     check if place to go is free
            #     ls[i]=st
            #     ls[i]=str(ls[i])
            # print(ls)
            return(ls)
        else:
            return [i+1 for i, e in enumerate(self.board) if e == 0]

    def make_move(self, move):
        
        if(self.nmove>6):
            mov=list(str(move)) #[1,2]
            mov[0]=int(mov[0])
            mov[1]=int(mov[1])
            self.board[int(mov[0])-1]=0                    #remove
            self.board[int(mov[1])-1]=self.nplayer      #add new place              
        else:
            self.board[int(move)-1] = self.nplayer

    def lose(self):
        """ DID I LOSE ? LOSING CONDITIONS """
        return any([all([(self.board[c-1] == self.nopponent)for c in line])for line in [
                            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # horizontal
                            [1, 4, 7], [2, 5, 8], [3, 6, 9]  # vertical
                ]])

    def is_over(self):
        return (self.possible_moves() == []) or self.lose()

    def show(self):
        #print(self.board)
        entries=['-','O','x']
        for i in range(3):          # 0 1 2
            for j in range(3):      # 0 1 2
                str=(entries[self.board[3*i+j]]) 
                print(str,end=" ")
            print("")
        print("")

    def scoring(self):
        return -100 if self.lose() else 0

if __name__ == "__main__":
    from easyAI import AI_Player, Negamax
    ai_algo = Negamax(10)
    MMM([Human_Player(), AI_Player(ai_algo)]).play()
