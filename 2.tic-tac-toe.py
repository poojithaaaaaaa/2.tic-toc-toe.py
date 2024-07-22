import random
board = [' ' for _ in range(9)]
def draw_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()
def player_move(icon):
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2

    print("Your turn player {}".format(number))

    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == ' ':
        board[choice - 1] = icon
    else:
        print()
        print("That space is taken!")
def ai_move(icon):
    best_score = float('-inf')
    best_move = 0

    for i in range(len(board)):
        if board[i] == ' ':
            board[i] = icon
            score = minimax(board, False, icon)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = icon
def minimax(board, is_maximizing, icon):
    if check_win(icon):
        return 1
    elif check_win('O' if icon == 'X' else 'X'):
        return -1
    elif ' ' not in board:
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = icon
                score = minimax(board, False, icon)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = 'O' if icon == 'X' else 'X'
                score = minimax(board, True, icon)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score
def check_win(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False
while True:
    draw_board()
    player_move('X')
    draw_board()
    if check_win('X'):
        print("Player 1 wins! Congratulations!")
        break
    elif ' ' not in board:
        print("It's a tie!")
        break
    ai_move('O')
    if check_win('O'):
        print("AI wins!")
        break
