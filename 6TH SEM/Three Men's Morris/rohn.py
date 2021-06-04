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
        return (self.possible_moves() == []) or self.lose()

    def show(self):
        #print(self.board)
        print(" _______________________________________________________")
        print("|\t\t\t\t\t\t\t|")
        print("|\tScores:\tPlayer1=",end=" ")
        print(p1,end="") 
        print("\tPlayer2=",end=" ")
        print(p2,end="")
        print("\t\t|")
        print("|_______________________________________________________|")
        entries=['-','O','x']
        print("|\t\t\t\t\t\t\t|")
        for i in range(3):
            print("|\t\t",end="\t")          # 0 1 2
            for j in range(3):      # 0 1 2
                str=(entries[self.board[3*i+j]]) 
                print(str,end=" ")
            print("\t\t\t\t|")
        print("|\t\t\t\t\t\t\t|")
        print("|_______________________________________________________|")

    def scoring(self):
        return -100 if self.lose() else 0 

def askntell():
    print("Difficulty Level ?? (Easy=E Medium=M Hard=H)  :",end="")
    diff=input()
    if(diff=="E" or diff=="e"):
        print("")
        print("\t\t EASY MODE SELECTED \t\t")
        print("")
        return 2
    if(diff=="M" or diff=="m"):
        print("")
        print("\t\t MEDIUM MODE SELECTED \t\t")
        print("")
        return 3
    if(diff=="H" or diff=="h"):
        print("")
        print("\t\t HARD MODE SELECTED \t\t")
        print("")
        return 4
    else:
        print("Enter a valid input.")
        diff=askntell()
        return diff

if __name__ == "__main__":
    from easyAI import AI_Player, Negamax
    print(" _______________________________________________________ ")
    print("|\t\t\t\t\t\t\t|")
    print("|\t\t\tRULES\t\t\t\t|")
    print("|_______________________________________________________|")
    print("|\t\t\t\t\t\t\t|")
    print("|\t1. Similar to tic tac toe for first six moves.\t|")
    print("|\t2. Then u hav to move ur peices around to make  |")
    print("|\t   a horizontal or vertical line to win.\t|")
    print("|\t3. No diagonal movement or win cases. \t\t|")
    print("|_______________________________________________________|")
    print("")
    diff=askntell()
    ai_algo = Negamax(diff)
    rest=1
    p1,p2=0,0
    while(rest):
        a=MMM([Human_Player(), AI_Player(ai_algo)])
        a.play()
        if(a.winner==1):
            p1+=1
        else:
            p2+=1
        print("")
        print("\t\tGAME OVER\t\t")
        print("\t\tPlayer ",end="")
        print(a.winner,end=" ")
        print(" WON")
        print("")
        print("Do you want to play again ?     Y/N  :",end="")
        restart=(input())
        print("")
        if(restart=="N" or restart=="n"):
            print(" _______________________________________________________")
            print("|\t\t\t\t\t\t\t|")
            print("|******************   GAME EXIT  ***********************|")
            print("|_______________________________________________________|")
            break
