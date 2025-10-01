# tictactoe.py
def print_board(board):
    for r in range(3):
        print(board[3*r], '|', board[3*r+1], '|', board[3*r+2])
    print()

def check_winner(board):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    if ' ' not in board:
        return 'Draw'
    return None

def minimax(board, player):
    winner = check_winner(board)
    if winner == 'O': return (1, None)
    if winner == 'X': return (-1, None)
    if winner == 'Draw': return (0, None)

    moves = []
    for i in range(9):
        if board[i] == ' ':
            board[i] = player
            score, _ = minimax(board, 'O' if player == 'X' else 'X')
            moves.append((score, i))
            board[i] = ' '
    if player == 'O':
        return max(moves, key=lambda x: x[0])
    else:
        return min(moves, key=lambda x: x[0])

def best_move(board):
    score, move = minimax(board, 'O')
    return move

if __name__ == "__main__":
    board = [' '] * 9
    print("Tic-Tac-Toe: You are X, AI is O")
    print_board(board)

    while True:
        pos = int(input("Enter position (0-8): "))
        if board[pos] == ' ':
            board[pos] = 'X'
        else:
            print("Invalid move, try again")
            continue

        if check_winner(board): break

        ai_pos = best_move(board)
        board[ai_pos] = 'O'
        print("AI plays at", ai_pos)
        print_board(board)

        if check_winner(board): break

    result = check_winner(board)
    print("Game Over! Winner:", result)
