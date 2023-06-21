""" 

Generates a list of all possible tac-tac-toe configuations and asks
me for best possible move, and writes each scenario in a file.

It should hold true that the cross always goes first.

"""


import pickle
from board import Board
from itertools import filterfalse

mappings = {}

def find_optimal_move(board: Board, cross_turn: int = 1) -> bool:	# returns true if its a winning move 
	global mappings

	if (moves:=board.can_win(cross_turn))  or \
	   (moves:=board.can_win(-cross_turn)) or \
   	   (moves:=board.can_fork(cross_turn)) or \
	   (moves:=board.can_fork(-cross_turn)):	
		return moves
		
	good_moves = []
	bad_moves = []
	for move in filter(lambda x: board[x] == 0, range(9)):
		reverted_moves = [move]
		board[move] = cross_turn
		if moves:=board.can_win(cross_turn):	# check if the current player treatens a win
			reverted_moves.append(moves[0])	# see if defense is forced
			board[moves[0]] = -cross_turn   # simulate their defense
			if board.can_win(cross_turn) or board.can_fork(cross_turn):
				good_moves.append(move)

		for opp_move in filter(lambda x: board[x] == 0, range(9)):
			reverted_moves.append(opp_move)
			board[opp_move] = -cross_turn
			if forced_def:=board.can_win(-cross_turn):
				reverted_moves.append(forced_def[0])
				board[forced_def[0]] = cross_turn
				if board.can_win(-cross_turn) or board.can_fork(-cross_turn):
					bad_moves.append(move)
				
		for move in reverted_moves:
			board[move] = 0
		
	mappings[board.config] = good_moves if good_moves \
				            else [move for move in filter(lambda x: board[x] == 0, range(9)) if move not in bad_moves]

def simulate_every_game(board: Board, cross_turn: int = 1) -> None:
	if board.moves_made == 9:
		return
	find_optimal_move(board, cross_turn) 
	for move in filter(lambda x: board[x] == 0, range(9)):
		board[move] = cross_turn
		simulate_every_game(board, -cross_turn)
		board[move] = 0
		

if __name__ == "__main__":

	simulate_every_game(Board())
	with open('v2.pkl', 'wb') as f:
		pickle.dump(mappings, f)
	print("Model saved!")
	
