import sys

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check for a win
def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def check_draw(board):
    return all(cell != " " for row in board for cell in row)

# Function to generate possible moves
def possible_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

# Function to evaluate the board
def evaluate(board):
    if check_win(board, "X"):
        return 10
    elif check_win(board, "O"):
        return -10
    else:
        return 0

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if check_win(board, "X"):
        return 10 - depth
    elif check_win(board, "O"):
        return depth - 10
    elif check_draw(board):
        return 0

    if maximizing_player:
        max_eval = -sys.maxsize
        for move in possible_moves(board):
            board[move[0]][move[1]] = "X"
            eval = minimax(board, depth + 1, alpha, beta, False)
            board[move[0]][move[1]] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = sys.maxsize
        for move in possible_moves(board):
            board[move[0]][move[1]] = "O"
            eval = minimax(board, depth + 1, alpha, beta, True)
            board[move[0]][move[1]] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Function to find the best move for the AI
def find_best_move(board):
    best_eval = -sys.maxsize
    best_move = None
    for move in possible_moves(board):
        board[move[0]][move[1]] = "X"
        eval = minimax(board, 0, -sys.maxsize, sys.maxsize, False)
        board[move[0]][move[1]] = " "
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

# Main function to play the game
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player's move
        row, col = map(int, input("Enter row and column (1-3) for your move: ").split())
        row -= 1
        col -= 1
        if board[row][col] == " ":
            board[row][col] = "O"
        else:
            print("Invalid move! Try again.")
            continue

        # Check if player wins or game is drawn
        if check_win(board, "O"):
            print_board(board)
            print("Congratulations! You win!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI's move
        print("AI is making a move...")
        row, col = find_best_move(board)
        board[row][col] = "X"

        # Check if AI wins or game is drawn
        if check_win(board, "X"):
            print_board(board)
            print("AI wins! Better luck next time.")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Print the updated board
        print_board(board)

if __name__ == "__main__":
    main()
