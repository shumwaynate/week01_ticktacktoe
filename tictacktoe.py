#This is my tick tack toe game
#Nathan Shumway

def main():

    player = "x" #Starts with player x
    ifWin = "N" #Variable to be considered if a win has been noticed by game
    spots = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] #this is the list holding each of the nine game spaces
    turnCount = 1
    

    for turnCount in range(9):#Create a for loop that repeats 9 times

        drawTable(spots); # call function to draw the table passing in the spots list
        playSquare = int(input(player+"'s turn to choose a square (1-9): ")) #displays who's turn it is and getting the user's input

        if (spots[playSquare-1] != "x" and spots[playSquare-1] != "o" and player == "x"): # if the spot the person chose doesn't have an x or o and it is the x players turn
            spots[playSquare-1] = player #puts in the letter of the player
            ifWin = calculateWinner(spots, player) #tests if there is a winner yet given the spots and the player who just went, making ifWin ="Y" if so
            if ifWin == "Y" : break #If there is a declared winner
            else: pass
            player = "o"
            turnCount += 1
        elif (spots[playSquare-1] != "x" and spots[playSquare-1] != "o" and player == "o"): #same as previous just for if the player is o
            spots[playSquare-1] = player
            ifWin = calculateWinner(spots, player)
            if ifWin == "Y" : break
            else: pass
            player = "x"
            turnCount += 1
        else:
            print("That square is taken!!")


        turnCount += 1 #adds one to the turn counter for every turn, break out of for loop if 9 turns pass meaning all spaces are filled

    drawTable(spots)

    if(ifWin=="Y"):
        print(player+" Wins!!")
    elif(ifWin == "N"):
        print("Looks like a tie!")
        



def calculateWinner(spots, player): #takes the list with the player who just placed a letter and returns "y" If the player is a winner

    ifWin = "N"

    if(spots[0] == player and spots[1]== player and spots[2]== player): #tests rows
        ifWin = "Y"
    elif(spots[3] == player and spots[4]== player and spots[5]== player):
        ifWin = "Y"
    elif(spots[6] == player and spots[7]== player and spots[8]== player):
        ifWin = "Y"
    elif(spots[0] == player and spots[3]== player and spots[6]== player): #tests columns
        ifWin = "Y"
    elif(spots[1] == player and spots[4]== player and spots[7]== player):
        ifWin = "Y"
    elif(spots[2] == player and spots[5]== player and spots[8]== player):
        ifWin = "Y"
    elif(spots[0] == player and spots[4]== player and spots[8]== player): #tests diagonals
        ifWin = "Y"
    elif(spots[2] == player and spots[4]== player and spots[6]== player):
        ifWin = "Y"
    else:
        pass
    
    return ifWin
    


def drawTable(list): #print out the table of the game given the list


    print("\n" + list[0]+ " | "+list[1]+" | "+list[2])
    print("--+--+--")
    print(list[3]+ " | "+list[4]+" | "+list[5])
    print("--+--+--")
    print(list[6]+ " | "+list[7]+" | "+list[8] + "\n")



main()
