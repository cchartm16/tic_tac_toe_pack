#Objective: write a tic-tac-toe program

#------------------------NEED TO FIX:
###IF ONE SPACE LEFT IN ROUND, COMPUTER WILL NOT I REPEAT NOT GO TO NEXT ROUND

#Main variables
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
goal_score = int(input("What score would you like to play up to?"))
#Checks if input is accurate
while (type(goal_score) != int):
    goal_score = input("You must enter a number:")

goal_score = int(goal_score)
current_score = 0
turn = 0
round = 1
round_gone_up = bool
pieces = ["x", "o"]

user_piece = input("Which piece would you like to play as? 'x' or 'o'? ")


def InitializeGrid(board):

    for i in range(3):
        for j in range(3):
            board[i][j] = "."
    return board


def InitializeBoard():
    #initialize game
    #Initialize grid
    InitializeGrid(board)
    ComputerPiece()
    global turn
    global round_gone_up
    # Prints out user-turn
    turn = 1
    round_gone_up = False


def ContinueGame(current_score, goal_score):
    #Return false if game should end, true if game not over
    if (current_score >= goal_score):
        return False
    else:
        return True



### ----------------------USER MOVE

def IsValidPiece():
    piece = user_piece
    if len(piece) != 1:
        return False

    if piece not in pieces:
        return False

    return True

def GetPiece():
    piece = user_piece

    while not IsValidPiece:
        print("You entered:", piece)
        piece = input("Error! Please type in the single character 'x' or 'o': ")

    return piece



def IsValid(move):

    #move length
    if len(move) != 1:
        return False


    #move number
    if (int(move[0]) < 1):
        print("Start at index 1")
        return False


    #no probs, so return true
    return True



def GetMove():
    move = input("Enter move: ")

    while not IsValid(move):
        move = input("Invalid move! Enter a valid move: ")

    return move





###-------------------COMPUTER PIECE





def ComputerPiece():
    piece = GetPiece()
    for i in pieces:
        if piece != i:
            computer_piece = i
    return computer_piece




###--------------COMPUTER MOVE




#Generates a move for the computer
from random import randint
def GenerateMoveComputer():

    computer_choice = [randint(1, 9), ComputerPiece()]

    return computer_choice











def PositionBoard():

    position = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    #Indexes a board one-to-nine
    for i in range(1, 10):
        for j in range(3):
            for k in range(3):
                position[j][k] = i
                i += 1
        break
    return position


def CheckIfMoveAlreadyMade(board, move):
    space_already_taken = []
    board2 = PositionBoard()
    for i in range(3):
        for j in range(3):

            #If board-space is not blank
            if (board[i][j] != "."):

                #Store board-space in list, convert board-space to string
                space_already_taken += str(board2[i][j])


                while (str(move[0]) in space_already_taken):
                        if (len(space_already_taken) != 9):
                            if (type(move[0]) == str):
                            #While move[0] in the list of board-spaces taken
                                move = input("Space already taken! Enter a valid move: ")

                            elif (type(move[0]) == int):

                                move = GenerateMoveComputer()
                                continue
                        else:
                            CheckThree(board)
                            if (CheckThree(board) == None):
                                print("It's a tie!")
                                global round_gone_up
                                round_gone_up = True
                        break


    return move

def UpdateBoard(board, move, type_move):
    #Makes board equal to 1-9
    board1 = PositionBoard()
    #Updates position
    for i in range(3):
        for j in range(3):
            if (type(move[0]) == str):
                #Compares string to string
                if (move[0] == str(board1[i][j])):
                    board[i][j] = type_move
            elif (type(move[0]) == int):
                #Compares int to int
                if (move[0] == board1[i][j]):
                    board[i][j] = type_move


    return board



def CheckThree(board):
    #Check each row for three-in-a-row
    for i in range(2, -1, -1):
        for j in range(2, -1, -1):
            if (board[i][j] != "."):
                if (board[i][j] == board[i][j-1]) and (board[i][j] == board[i][j-2]):

                    return board[i][j]

    #Check each column
    for j in range(3):
        for i in range(3):
            if (board[i][j] != "."):
                if (board[i][j] == board[i-1][j]) and (board[i][j] == board[i-2][j]):
                    return board[i][j]

    #Check diagonally
    if (board[1][1] != "."):
        if (((board[1][1] == board[0][0]) and (board[0][0] == board[2][2])
             or (board[1][1] == board[0][2]) and (board[0][2] == board[2][0]))):

                return board[1][1]




def CheckScore():
    global round_gone_up
    if (CheckThree(board)):
        global current_score
        global round

        #Increments score
        current_score += 1
        print(CheckThree(board), " wins:", "round", round)

        #Increments round
        round += 1
        #Returns boolean round_gone_up
        round_gone_up = True


        #Prints the winner
    return round_gone_up


def DrawBoard(board):
    print("\n\n\n")
    print(" ---------------------------------")

    for i in range(3):
        #Draw each row
        linetodraw = ""
        for j in range(3):
            linetodraw += " | " + board[i][j]
        linetodraw += " |"
        print(linetodraw)
    print(" ---------------------------------")

def DoRound():
    DrawBoard(board)

    #Player's move
    move = CheckIfMoveAlreadyMade(board, GetMove())
    UpdateBoard(board, move, GetPiece())

    # Checks for three-in-a-row
    CheckThree(board)

    # Checks score
    CheckScore()

    #Computer Move
    move2 = CheckIfMoveAlreadyMade(board, GenerateMoveComputer())
    UpdateBoard(board, move2, ComputerPiece())







    #Prints out variables
    global current_score
    print("Current score:", current_score)
    print("Round:", round)




#Initialize game
InitializeBoard()

while ContinueGame(current_score, goal_score):
    # Checks if round gone up

    if (round_gone_up):
        InitializeBoard()
    DoRound()
    print("Turn: ", turn)
    turn += 1


if not ContinueGame(current_score, goal_score):
    print("\n\n\n")
    print(CheckThree(board), "wins!")
