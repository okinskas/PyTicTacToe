
board = [[0,0,0],[0,0,0],[0,0,0]]
player = 1

def turn():
    print_board()
    
    if is_win():
        print("Player %s Wins! \n" % player)
        reset()
        turn()
    elif is_board_full():
        print("Draw, no one wins.")
        reset()
        turn()
    else:
        r = input("Player %s's Turn: \n" % player)
        if r == "reset":
            reset()
            turn()
        elif r == "help":
            help_me()
            turn()
        elif r == "quit":
            pass
        else:
            args = r.split()
            if len(args) == 2:
                try:
                    x = int(args[0])
                    y = int(args[1])

                    if (0 > x or x > 2 or 0 > y or y > 2):
                        print("Out of bounds, type 'help' to see all commands.\n")
                    elif is_empty(x, y):
                        draw(x, y)
                        alternate()
                    else:
                        print("Coord occupied. Enter an empty coord.\n")
                    turn()
                except ValueError:
                    print("Invalid command, type 'help' to see all commands.\n")
                    turn()
            else:
                print("Invalid command, type 'help' to see all commands.\n")
                turn()

def getSymbol(p):
    if player == 1:
        return "O"
    else:
        return "X"

def draw(x,y):
    board[x][y] = getSymbol(player)

def reset():
    global player
    global board
    player = 1
    board = [[0,0,0],[0,0,0],[0,0,0]]

def alternate():
    global player
    if player == 1:
        player = 2
    elif player == 2:
        player = 1

def is_empty(x,y):
    return board[x][y] == 0

def is_board_full():
    global board
    for row in board:
        for val in row:
            if val == 0:
                return False
    return True
def is_win():
    def row_win():
        for row in board:
            if row[0] != 0 and row[0] == row[1] == row[2]:
                return True
        return False
    def col_win():
        for x in range(2):
            col = [board[0][x], board[1][x], board[2][x]]
            if col[0] != 0 and col[0] == col[1] == col[2]:
                return True
        return False
    def diag_win():
        if board[0][0] != 0 and board[0][0] == board[1][1] == board[2][2]:
            return True
        elif board[0][2] != 0 and board[0][2] == board[1][1] == board[2][0]:
            return True
        return False

    return row_win() or col_win() or diag_win()

def help_me():
    print("Input commands:")
    print(" x y       - Take turn, draw symbol at (x,y).")
    print(" reset     - Reset the board and restart game.")
    print(" help      - Display this message.")
    print(" quit      - Quit game.\n")

def print_board():
    print(" +---+---+---+")
    for row in board:
        print(" | %s | %s | %s |" % (row[0], row[1], row[2]))
        print(" +---+---+---+")
    print("\n")

def play():
    global player
    print("Welcome! \n\n ")
    help_me()
    turn()

if __name__ == "__main__":
    play()