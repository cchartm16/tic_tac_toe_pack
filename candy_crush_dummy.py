#First "game" for Python! :D

#Initialize
#While game not over
    #Do round of game


#State main variables
score = 0
turn = 0
goalscore = 100
newlist = []

#CANNOT WORK

def DefineBoard(greater_list):
    lesser_list = []
    for i in range(8):
        for j in range(8):
            lesser_list.append(0)
            break
        greater_list.append(lesser_list)
    return greater_list




board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

board2 = DefineBoard(newlist)
check = (board == board2)

if check == True:
    print('hello')
else:
    print("not correct")








from random import choice
def InitializeGrid(board):
    #Initialize grid by reading from file

        for i in range(8):
            for j in range(8):
                board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])


def InitializeBoard():
    # Initialize game
    #Initialize grid
    InitializeGrid(board)

    #Initialize score
    global score
    score = 0

    #Initialize turn number
    global turn
    turn = 1



def ContinueGame(current_score, goal_score = 100):
    # Return false if game should end, true if game is not over
    if (current_score >= goal_score):
        return False
    else:
        return True








def DrawBoard(board):
    #Display board to screen
    linetodraw = ""
    #Draw some blank lines first
    print("\n\n\n")


    print(" ---------------------------------")

    #Draw numbering columns by letters

    letterlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in range(len(letterlist)):
        letterdrawn = ""
        for j in range(len(letterlist)):
            letterdrawn += " | " + letterlist[j]





        letterdrawn += " |"


        print(letterdrawn)
        break





#LONGHAND WAY OF DOING IT

        # letterdrawn = ""
        # for j in range(8):
        #     letterdrawn += " | " + letterlist[i]
        #     break
        #
        #
        # letterdrawn += " | " + letterlist[i+1]
        # letterdrawn += " | " + letterlist[i + 2]
        # letterdrawn += " | " + letterlist[i + 3]
        # letterdrawn += " | " + letterlist[i + 4]
        # letterdrawn += " | " + letterlist[i + 5]
        # letterdrawn += " | " + letterlist[i + 6]
        # letterdrawn += " | " + letterlist[i + 7]
        #
        # letterdrawn += " |"
        # break
    # print(letterdrawn)







    #Now draw rows from 8 to 1
    for i in range(7, -1, -1):
        #Draw each row
        linetodraw=""
        for j in range(8):


            linetodraw += " | " + board[i][j]

        #Put numbers at end of row
        #i + 1 because i starts at zero
        linetodraw += " | " + str(i+1)








        print(linetodraw)
        print(" ---------------------------------")

    global score
    print("Current score:", score)


def IsValid(move):
    #Return true if move is valid, false otherwise
    #Check length of move
    if (len(move) != 3):
        return False


    ###
    #COME BACK FOR A LOOP???

    ###

    #Check that space and direction are valid
    if not (move[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
        return False
    if not (move[1] in ['1', '2', '3', '4', '5', '6', '7', '8']):
        return False
    if not (move[2] in ['u', 'd', 'l', 'r']):
        return False

    #Check that direction is valid for given row/column

    #check that first column moves not towards left
    if (move[0] == 'a') and (move[2] == 'l'):
        return False
    #check that last-column moves not towards right
    if (move[0] == 'h') and (move[2] == 'r'):
        return False
    #check that bottom row moves not down
    if (move[1] == '1') and (move[2] == 'd'):
        return False
    #check that top-row moves not up
    if (move[1] == '8') and (move[2] == 'u'):
        return False


    #no problems, so return true
    return True



def GetMove():
    #Print instructions
    print("Enter a move by specifying the space and direction (u = up, d = down, l = left, r = right). Spaces should list column then row")
    print("For example, e3u would swap position e3 with the one above, and f7r would swap f7 to the right")


    #Get move input from user
    move = input("Enter move: ")


    #Loop until good move
    while not IsValid(move):
        move = input("Invalid move! Enter a valid one: ")

    return move



def ConvertLetterToCol(Col):
    if Col == 'a':
        return 0
    elif Col == 'b':
        return 1
    elif Col == 'c':
        return 2
    elif Col == 'd':
        return 3
    elif Col == 'e':
        return 4
    elif Col == 'f':
        return 5
    elif Col == 'g':
        return 6
    elif Col == 'h':
        return 7
    else:
        # not a valid column!
        return -1

def SwapPieces(board, move):
    # Swap pieces on board according to move
    # Get original position
    origrow = int(move[1]) - 1
    origcol = ConvertLetterToCol(move[0])
    # Get adjacent position
    if move[2] == 'u':
        newrow = origrow + 1
        newcol = origcol
    elif move[2] == 'd':
        newrow = origrow - 1
        newcol = origcol
    elif move[2] == 'l':
        newrow = origrow
        newcol = origcol - 1
    elif move[2] == 'r':
        newrow = origrow
        newcol = origcol + 1
    # Swap objects in two positions
    temp = board[origrow][origcol]
    board[origrow][origcol] = board[newrow][newcol]
    board[newrow][newcol] = temp


def RemovePieces(board):
    # Remove 3-in-a-row and 3-in-a-column pieces
    # Create board to store remove-or-not

    remove = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]


    # Go through rows
    for i in range(8):
        for j in range(6):
            if (board[i][j] == board[i][j + 1]) and (board[i][j] == board[i][j + 2]):
                # three in a row are the same!
                remove[i][j] = 1;
                remove[i][j + 1] = 1;
                remove[i][j + 2] = 1;

    #Go through columns
    for j in range(8):
        for i in range(6):
            if (board[i][j] == board[i + 1][j]) and (board[i][j] == board[i + 2][j]):
                # three in a row are the same!
                remove[i][j] = 1;
                remove[i + 1][j] = 1;
                remove[i + 2][j] = 1;

    # Eliminate those marked
    global score
    removed_any = False
    for i in range(8):
        for j in range(8):
            if(remove[i][j] == 1):
                board[i][j] = 0
                score += 1
                removed_any = True
    return removed_any


def DropPieces(board):
    # Drop pieces to fill in blanks
    for j in range(8):
        # make list of pieces in the column
        listofpieces = []
        for i in range(8):
            if board[i][j] != 0:
                listofpieces.append(board[i][j])
        # copy that list into colulmn
        for i in range(len(listofpieces)):
            board[i][j] = listofpieces[i]
        # fill in remainder of column with 0s
        for i in range(len(listofpieces), 8):
            board[i][j] = 0


def FillBlanks(board):
    # Fill blanks with random pieces
    for i in range(8):
        for j in range(8):
            if (board[i][j] == 0):
                board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])




def Update(board, move):
    #Update hte board according to move
    SwapPieces(board, move)
    pieces_eliminated = True
    while pieces_eliminated:
        pieces_eliminated = RemovePieces(board)
        DropPieces(board)
        FillBlanks(board)





def DoRound(board):
    #Perform one round of game

    #Display current board
    DrawBoard(board)

    #Get move
    move = GetMove()
    #Update board
    Update(board, move)
    #Update turn number
    global turn
    turn += 1







# Perform one round of the game
# Initialize game
InitializeBoard()
while (RemovePieces(board) == True):
    InitializeBoard()
    continue



# While game not over
while ContinueGame(0):
    DoRound(board)
