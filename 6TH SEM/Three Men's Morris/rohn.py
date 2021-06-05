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
        self.winner=0

    def possible_moves(self):
        lss=["12","14","21","23","25","32","36","41","45","47","52","54","56","58","65","63","69","74","78","85","87","89","96","98"]
        if(self.nmove>6):
            ls=[]
            x=self.nplayer
            for i in lss:
                a=list(i)
                if(self.board[int(a[1])-1]==0 and self.board[int(a[0])-1]==(x)):
                    ls.append(i)
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
        ret = any([all([(self.board[c-1] == self.nopponent)for c in line])for line in [
                            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # horizontal
                            [1, 4, 7], [2, 5, 8], [3, 6, 9]  # vertical
                ]])
        return ret

    def is_over(self):
        if((self.possible_moves() == []) or self.lose()):
            self.winner=self.nopponent
        if(self.nmove>20):
            print("")
            print("\t\tMATCH DRAW\t\t")
            return 1
        return (self.possible_moves() == []) or self.lose() 

    def show(self):
        #print(self.board)
        print(" ________________________________________________________")
        print("|\t\t\t\t\t\t\t |")
        print("|\tScores:\tPlayer1=",end=" ")
        print(p1,end="") 
        print("\tPlayer2=",end=" ")
        print(p2,end="")
        print("\t\t |")
        print("|________________________________________________________|")
        entries=['-','O','x']
        print("|\t\t\t\t\t\t\t |")
        for i in range(3):
            print("|\t\t",end="\t")          # 0 1 2
            for j in range(3):      # 0 1 2
                str=(entries[self.board[3*i+j]]) 
                print(str,end=" ")
            print("\t\t\t\t |")
        print("|\t\t\t\t\t\t\t |")
        print("|________________________________________________________|")

    def scoring(self):
        return -100 if self.lose() else 0 

def askntell():
    print("Difficulty Level ?? (Easy=E Medium=M Hard=H)  :",end="")
    diff=input()
    if(diff=="E" or diff=="e"):
        print(" ________________________________________________________")
        print("|\t\t\t\t\t\t\t |")
        print("|****************   EASY MODE SELECTED  *****************|")
        print("|________________________________________________________|")
        print("")
        return 2
    if(diff=="M" or diff=="m"):
        print(" ________________________________________________________")
        print("|\t\t\t\t\t\t\t |")
        print("|****************  MEDIUM MODE SELECTED  ****************|")
        print("|________________________________________________________|")
        print("")
        return 3
    if(diff=="H" or diff=="h"):
        print(" ________________________________________________________")
        print("|\t\t\t\t\t\t\t |")
        print("|****************   HARD MODE SELECTED  *****************|")
        print("|________________________________________________________|")
        print("")
        return 4
    else:
        print("Enter a valid input!.")
        diff=askntell()
        return diff

def show_rules():
    print(" ________________________________________________________ ")
    print("|\t\t\t\t\t\t\t |")
    print("|\t\t\tRULES\t\t\t\t |")
    print("|________________________________________________________|")
    print("|\t\t\t\t\t\t\t |")
    print("|\t1. To begin: \t\t\t\t\t |")
    print("|\t   the board is empty, and each player has three |")
    print("|\t   pieces in hand. Players decide at random who  |")
    print("|\t   goes first.\t\t\t\t\t |")
    print("|\t\t\t\t\t\t\t |")
    print("|\t2. Placement & movement: \t\t\t |")
    print("|\t   Each player takes it in turn to place a piece |")
    print("|\t   on any intersection on the board. When all of |")
    print("|\t   the pieces are entered, players instead move  |")
    print("|\t   a piece on the board along a marked line to   |")
    print("|\t   the adjacent point a horizontal or vertical   |")
    print("|\t   line to win.\t\t\t\t\t |")
    print("|\t\t\t\t\t\t\t |")
    print("|\t3. To win: \t\t\t\t\t |")
    print("|\t   When one player has a straight line of three  |")
    print("|\t   of their own pieces, horizontally, vertically |")
    print("|\t   or diagonally along a marked line, that \t |")
    print("|\t   player wins the game.\t\t\t |")
    print("|\t\t\t\t\t\t\t |")
    print("|\t4. Board Layout (Numbering of Places): \t\t |")
    print("|\t   \t\t 1  2  3 \t\t\t |")
    print("|\t   \t\t 4  5  6 \t\t\t |")
    print("|\t   \t\t 7  8  9 \t\t\t |")
    print("|\t\t\t\t\t\t\t |")
    print("|\t5. To move: \t\t\t\t\t |")
    print("|\t   A peice from fourth place to fifth place, \t |")
    print("|\t   you can enter '45'. \t\t\t\t |")
    print("|\t\t\t\t\t\t\t |")
    print("|________________________________________________________|")
    print("")

def game_over_scene():
    print("")
    print("\t\tGAME OVER\t\t")
    print("\t\tPlayer ",end="")
    print(a.winner,end=" ")
    print(" WON")
    print("")
    print("Do you want to play again ?     Y/N  :",end="")

def game_exit_scene():
            print(" ________________________________________________________")
            print("|\t\t\t\t\t\t\t |")
            print("|\tScores:\tPlayer1=",end=" ")
            print(p1,end="") 
            print("\tPlayer2=",end=" ")
            print(p2,end="")
            print("\t\t |")
            print("|________________________________________________________|")
            print("")
            print("\t\t WINNER: PLAYER ",end="")
            if(p1>p2):
                print("1")
            else:
                print("2")
            print(" ________________________________________________________")
            print("|\t\t\t\t\t\t\t |")
            print("|******************   GAME EXIT  ************************|")
            print("|________________________________________________________|")
            print("")
            


if __name__ == "__main__":
    from easyAI import AI_Player, Negamax
    show_rules()
    diff=askntell()
    ai_algo = Negamax(diff)
    rest=1
    p1,p2=0,0
    while(rest):

        #starting a game
        a=MMM([Human_Player(), AI_Player(ai_algo)])
        a.play()

        # updating scores
        if(a.winner==1):
            p1+=1
        else:
            p2+=1
        
        # end UI
        game_over_scene()
        restart=(input())
        print("")
        if(restart=="N" or restart=="n"):
            game_exit_scene()
            break
            
