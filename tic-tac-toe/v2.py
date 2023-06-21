""" 

Generates a list of all possible tac-tac-toe configuations and asks
me for best possible move, and writes each scenario in a file.

It should hold true that the cross always goes first.

"""


import pickle
from board import Board
from itertools import filterfalse

# stores configs -> best moves
mappings = {}

def find_optimal_move(board: Board, cross_turn: int = 1) -> None:
	global mappings

	# check for winning moves, first for the player and then for the opponent
	if (moves:=board.can_win(cross_turn))  or \
	   (moves:=board.can_win(-cross_turn)) or \
   	   (moves:=board.can_fork(cross_turn)) or \
	   (moves:=board.can_fork(-cross_turn)):	
		mappings[board.config] = moves
		return
		
	# search every square if there are no threats
	good_moves = []
	bad_moves = []
	for move in filter(lambda x: board[x] == 0, range(9)):

		# simulate the move
		reverted_moves = [move]
		board[move] = cross_turn

		# check if current player can win off that move
		if moves:=board.can_win(cross_turn): 

			# defense by opponent is forced
			board[moves[0]] = -cross_turn   

			# if player can force a fork or a win off that move, its good
			if board.can_win(cross_turn) or board.can_fork(cross_turn):
				good_moves.append(move)

			# undo simulated defense
			board[moves[0]] = 0

		# check for every opponent move off that move
		for opp_move in filter(lambda x: board[x] == 0, range(9)):

			# simulate opponent moving there
			board[opp_move] = -cross_turn
			
			# if you are forced to defend off that move
			if (forced_def:=board.can_win(-cross_turn)) and not board.can_win(cross_turn) or \
			   (forced_def:=board.can_fork(-cross_turn)) and not board.can_win(cross_turn) and not board.can_fork(cross_turn):
				
				# simulate forced defence by player
				board[forced_def[0]] = cross_turn
			
				# check if opponent can win off that - if they can its a bad move
				if board.can_win(-cross_turn) or (board.can_fork(-cross_turn) and not board.can_win(cross_turn)):
					bad_moves.append(move)

				# undo simulated defense
				board[forced_def[0]] = 0
			
			# undo the simulated opponent's move
			board[opp_move] = 0
				
		# undo simulated original move
		board[move] = 0
		
	mappings[board.config] = good_moves if good_moves \
				            else [move for move in filter(lambda x: board[x] == 0, range(9)) if move not in bad_moves]

def simulate_every_game(board: Board = None, cross_turn: int = 1) -> None:
	
	# allows calling with no args	
	if board is None:
		board = Board()

	# full board
	if board.moves_made == 9:
		return

	# detects best move and then simulates every move possible
	find_optimal_move(board, cross_turn) 
	for move in filter(lambda x: board[x] == 0, range(9)):
		board[move] = cross_turn
		simulate_every_game(board, -cross_turn)
		board[move] = 0
		

if __name__ == "__main__":

	simulate_every_game()
	with open('v2.pkl', 'wb') as f:
		pickle.dump(mappings, f)
	print("Model saved!")
	
