board = [" " for i in range(9)]

def board_creation():
    row1 = f"|{board[0]}|{board[1]}|{board[2]}|"
    row2 = f"|{board[3]}|{board[4]}|{board[5]}|"
    row3 = f"|{board[6]}|{board[7]}|{board[8]}|"

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def players(icon):
    if icon == "X":
        num = 1
    elif icon == "O":
        num = 2
    
    print(f"Your turn Player {num}")
    choice = int(input("Enter the position of the move (1-9): ").strip())
    if choice in range(1, 10):
        if board[choice - 1] == " ":
            board[choice - 1] = icon
        else:
            print("Position already occupied. Try again.")
    else:
        print("INVALID CHOICE.")

def vic(icon):
    if ((board[0] == icon and board[1] == icon and board[2] == icon) or 
        (board[0] == icon and board[3] == icon and board[6] == icon) or 
        (board[0] == icon and board[4] == icon and board[8] == icon) or 
        (board[1] == icon and board[4] == icon and board[7] == icon) or
        (board[2] == icon and board[5] == icon and board[8] == icon) or
        (board[2] == icon and board[4] == icon and board[6] == icon) or
        (board[3] == icon and board[4] == icon and board[5] == icon) or
        (board[6] == icon and board[7] == icon and board[8] == icon)):
        return True
    else:
        return False
    
def draw():
    if " " not in board:
        return True
    else:
        return False

while True:
    board_creation()
    players("X")
    board_creation()
    if vic("X"):
        print("X WINS!!! CONGRATULATIONS")
        break
    elif draw():
        print("It's a DRAW")
        break
    players("O")
    if vic("O"):
        board_creation()
        print("O WINS!!! CONGRATULATIONS")
        break
    elif draw():
        print("It's a DRAW")
        break