#Objective: write a tic-tac-toe program
def get_goal_score():
    while True:
        try:
            return int(input("What score would you like to play up to? "))
        except ValueError:
            continue


def initialize_board():
    return [["."]*3 for i in range(3)]


def continue_game(current_score, goal_score):
    return all(score < goal_score for score in current_score.values())


def valid(move):
    if len(move) != 2:
        return False
    # move number
    try:
        index = int(move[0])
    except ValueError:
        return False
    if index == 0:
        print("Indices are 1..9")
        return False
    # move must be character 'x' or 'o'
    if move[1] not in ["x", "o"]:
        print("Mark must be 'x' or 'o'")
        return False
    return True


def already_taken(board, move):
    index = int(move[0]) - 1
    return board[index//3][index%3] != "."


def get_move(board):
    move = input("Enter move: ")
    while not valid(move) or already_taken(board, move):
        move = input("Invalid move! Enter a valid move: ")
    return int(move[0]), move[1]


def check_three(board):
    # Check each row for three-in-a-row
    for row in board:
        if row[0] != "." and all(el == row[0] for el in row):
            return row[0]
    # Check each column
    for col in zip(*board):
        if col[0] != "." and all(el == col[0] for el in col):
            return col[0]
    # Check diagonally
    if board[1][1] != ".":
        if (board[1][1] == board[0][0] == board[2][2]) or (board[1][1] == board[0][2] == board[2][0]):
                return board[1][1]
    return False


def draw(board):
    print("\n\n")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i != 2:
            print("---------")


def do_turn(board):
    draw(board)
    index, mark = get_move(board)
    board[(index-1)//3][(index-1)%3] = mark


def round_winner():
    board = initialize_board()
    turn = 0
    while not check_three(board):
        print("Turn: {}".format(turn))
        do_turn(board)
        turn += 1
    draw(board)
    return check_three(board)


def main():
    goal_score = get_goal_score()
    current_score = {"x": 0, "o": 0}
    round = 1
    while continue_game(current_score, goal_score):
        print("Round: {}".format(round))
        current_score[round_winner()] += 1
        print("Current score: x: {x}, o: {o}".format(**current_score))
        round += 1
    winner = "."
    for key, val in current_score.items():
        if val == goal_score:
            winner = key
    print("Player {} wins!".format(winner))

if __name__ == "__main__":
    main()