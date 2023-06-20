""" 

Generates a list of all possible tac-tac-toe configuations and asks
me for best possible move, and writes each scenario in a file.

It should hold true that the cross always goes first.

BOARD CONFIG: 

 0 | 1 | 2
-----------
 3 | 4 | 5
-----------
 6 | 7 | 8

"""

import pickle
from board import Board
def find_optimal_move(board: list[list[int]], cross_turn: int):
	global mappings 
	moves = []
	for move in range(9):
		if board[move] == 0:
			if can_win(board, cross_turn, move):
				mappings[get_board_config(board)] = move
				return True
			elif can_win(board, -cross_turn, move):
				mappings[get_board_config(board)] = move
				return True
			else:
				if board.moves_made == 9:
					return True
				board[move] = cross_turn
				if find_optimal_move(board, -cross_turn):
					moves.append(move)
				board[move] = 0
	mappings[get_board_config(board)] = moves
	return True
	
if __name__ == "__main__":
	board = Board()
	find_optimal_move(board, 1)
	with open('model.pkl', 'wb') as f:
		pickle.dump(mappings, f)
	print("Model saved!")
	
