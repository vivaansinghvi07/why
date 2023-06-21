""" 

Generates a list of all possible tac-tac-toe configuations and asks
me for best possible move, and writes each scenario in a file.

It should hold true that the cross always goes first.

"""

import pickle
from board import Board

mappings = {}

def find_optimal_move(board: Board, cross_turn: int) -> bool:
	global mappings 
	moves = []
	for move in range(9):
		if board[move] == 0:
			if move in board.can_win(cross_turn):
				mappings[board.config] = move
				return True
			elif move in board.can_win(-cross_turn):
				mappings[board.config] = move
				return True
			else:
				if board.moves_made == 9:
					return True
				board[move] = cross_turn
				if find_optimal_move(board, -cross_turn):
					moves.append(move)
				board[move] = 0

	mappings[board.config] = moves
	return True
	
if __name__ == "__main__":
	board = Board()
	find_optimal_move(board, 1)
	with open('v1.pkl', 'wb') as f:
		pickle.dump(mappings, f)
	print("Model saved!")
	
