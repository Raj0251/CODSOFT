# tictactoe.py - Tic-Tac-Toe with Minimax AI (AI plays 'O')
from typing import List, Optional, Tuple

def check_winner(board: List[str]) -> Optional[str]:
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    if ' ' not in board:
        return 'Draw'
    return None

def minimax(board: List[str], player: str) -> Tuple[int, Optional[int]]:
    winner = check_winner(board)
    if winner == 'O':
        return (1, None)
    if winner == 'X':
        return (-1, None)
    if winner == 'Draw':
        return (0, None)
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

def best_move(board: List[str]) -> int:
    score, move = minimax(board, 'O')
    return move if move is not None else -1

def print_board(board: List[str]) -> None:
    for r in range(3):
        print(board[3*r], '|', board[3*r+1], '|', board[3*r+2])
    print()

if __name__ == '__main__':
    board = [' ']*9
    board[4] = 'X'
    board[0] = 'X'
    print('Board before AI move:')
    print_board(board)
    move = best_move(board)
    print('AI chooses position:', move)
    board[move] = 'O'
    print('Board after AI move:')
    print_board(board)
