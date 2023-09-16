def display_board(board):
    print("-------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            symbol = " " if cell == 0 else cell
            print(symbol, end=" | ")
        print("\n-------------")


def display_board(board):
    print("-------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            symbol = " " if cell == 0 else cell
            print(symbol, end=" | ")
        print("\n-------------")


def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def get_player_move(board, player):
    while True:
        row = int(input("Qatorni kiriting (1-3): ")) - 1
        col = int(input("Ustunni kiriting (1-3): ")) - 1
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Noto'g'ri kiritish. Iltimos, qaytadan urinib ko'ring.")
        elif board[row][col] != " ":
            print("Ushbu joy allaqachon band. Iltimos, boshqa joyni tanlang.")
        else:
            board[row][col] = player
            break


def has_won(board, player):
    # Qatorlarni tekshirish
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Ustunlarni tekshirish
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Diagonalni tekshirish
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def play_game():
    board = initialize_board()
    current_player = "X"

    while True:
        display_board(board)
        print(f"oyinchi uchun {current_player} belgisining navbati.")
        get_player_move(board, current_player)

        if has_won(board, current_player):
            display_board(board)
            print(f"{current_player} g'olib bo'ldi!")
            break
        elif is_board_full(board):
            display_board(board)
            print("Durrang!")
            break

        current_player = "O" if current_player == "X" else "X"


play_game()

