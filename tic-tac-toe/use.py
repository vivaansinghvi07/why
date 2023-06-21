import pickle
import sys
import random
from board import Board
from pynterface import bounded_int, clear_window
from pathlib import Path
from time import sleep

GUIDE = """\
 0 | 1 | 2 
-----------
 3 | 4 | 5
-----------
 6 | 7 | 8
"""

def play_game(model: dict[tuple, list]):
	print("To play, enter a number, 0-8, according to the following guide: ")
	print(GUIDE)
	player_turn = random.random() < 0.5
	cross_turn = 1
	board = Board()
	while True:
		if board.moves_made == 9:
			break
		clear_window()
		print(board)
		if player_turn:
			move = bounded_int(0, 8, prompt="Enter your move: ")
			while board[move] != 0:
				move = bounded_int(0, 8, prompt="Invalid move. Enter a proper one: ")
		elif not player_turn:
			sleep(0.75)
			try:
				move = random.choice(model[board.config])
			except KeyError:
				print("Invalid configuration or game ended.")
				break
		board[move] = cross_turn
		cross_turn *= -1
		player_turn = not player_turn
	clear_window()
	print(board)

if __name__ == "__main__":
	model_name = sys.argv[1]
	with open(f"{Path(__file__).parent}/{model_name}", 'rb') as f:
		model = pickle.load(f)
	play_game(model)
