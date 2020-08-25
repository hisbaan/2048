def print_board():
    print("█████████████████████")
    print("█{:>4}█{:>4}█{:>4}█{:>4}█".format(board[0][0], board[1][0], board[2][0], board[3][0]))
    print("█████████████████████")
    print("█{:>4}█{:>4}█{:>4}█{:>4}█".format(board[0][1], board[1][1], board[2][1], board[3][1]))
    print("█████████████████████")
    print("█{:>4}█{:>4}█{:>4}█{:>4}█".format(board[0][2], board[1][2], board[2][2], board[3][2]))
    print("█████████████████████")
    print("█{:>4}█{:>4}█{:>4}█{:>4}█".format(board[0][3], board[1][3], board[2][3], board[3][3]))
    print("█████████████████████")

def up():
    for x in range(len(board)):
        for y in range(len(board)):
            move_up(x, y)

def move_up(x, y):
    if (board[x][y] != 0 and board[x][y - 1] == 0):
        board[x][y - 1] = board[x][y]
        board[x][y] = 0

        if (board[x][y - 2] == 0 and y >= 2):
            move_up(x, y - 1)

def down():
    for x in reversed(range(len(board))):
        for y in reversed(range(len(board))):
            move_down(x, y)

def move_down(x, y):
    if (board[x][y] != 0 and board[x][y + 1] == 0):
        board[x][y + 1] = board[x][y]
        board[x][y] = 0

        if (board[x][y + 2] == 0 and y <= 1):
            move_down(x, y + 1)

def left():
    for x in range(len(board)):
        for y in range(len(board)):
            move_left(x, y)
           
def move_left(x, y):
    if (board[x][y] != 0 and board[x - 1][y] == 0):
        board[x - 1][y] = board[x][y]
        board[x][y] = 0

        if (board[x - 2][y] == 0 and x >= 2):
            move_left(x - 1, y)

def right():
   for x in reversed(range(len(board))):
       for y in reversed(range(len(board))):
            move_right(x, y)

def move_right(x, y):
    if (board[x][y] != 0 and board[x + 1][y] == 0):
        board[x + 1][y] = board[x][y]
        board[x][y] = 0

        if (board[x + 2][y] == 0 and x <= 1):
            move_right(x + 1, y)

board = [[0, 0, 0, 0], [0, 0, 2, 0], [0, 0, 0, 0], [0, 0, 2, 0]]
print_board()

game_ended = False

while(game_ended != True):
    user_input = input()

    if (user_input == "w"):
        up()
        print_board()
    elif (user_input == "a"):
        left()
        print_board()
    elif (user_input == "s"):
        down()
        print_board()
    elif (user_input == "d"):
        right()
        print_board()
    else:
        print("null")
        print_board()
