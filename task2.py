import math

def print_board(board):
    for row in range(3):
        print(" | ".join(board[row*3:(row+1)*3]))
        if row < 2:
            print("---------------")

def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def check_draw(board):
    return all(cell != ' ' for cell in board)

def minmax(board, depth, is_maximizing):
    if check_win(board, 'O'):
        return 1
    elif check_win(board, 'X'):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minmax(board, depth+1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score

    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minmax(board, depth+1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minmax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    board = [' ' for _ in range(9)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        human_move = int(input("Enter your move (1-9): ")) - 1
        if board[human_move] != ' ':
            print("Invalid move. Try Again.")
            continue
        board[human_move] = 'X'

        if check_win(board, 'X'):
            print_board(board)
            print("Congratulations! You win!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a Draw!")
            break

        ai_move = best_move(board)
        board[ai_move] = 'O'

        if check_win(board, 'O'):
            print_board(board)
            print("AI wins!")
            break

        elif check_draw(board):
            print_board(board)
            print("It's a Draw!")
            break

        print_board(board)

if __name__ == "__main__":
    play_game()
