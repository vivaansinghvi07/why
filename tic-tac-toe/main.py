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

WIN_INDECES = [
	(0, 1, 2),
	(3, 4, 5),
	(6, 7, 8),
	(0, 3, 6),
	(1, 4, 7),
	(6, 7, 8),
	(0, 4, 8),
	(2, 4, 6)
]

class Board: 
	def __init__(self, board: list[list[int]] = None):
		if board is None:
			self.board = [[0] * 3 for _ in range(3)]
		else:
			self.board = board
		self.cross_turn = 1
	
	def __getitem__(self, index: int | tuple[int]) -> int:
		if isinstance(index, tuple):
			return tuple(self.__getitem__(i) for i in index)
		return self.board[index // 3][index % 3]

	def __setitem__(self, index: int, value: int) -> int:
		self.board[index // 3][index % 3] = value

	def moves_made(self) -> int:
		return sum([row.count(0) for row in self.board])

mappings = {}

def can_win(board: Board, team: int) -> bool: 
	""" if checking if cross can win, pass 1. if checking circle, pass -1 """
	for possibility in WIN_INDECES:
		row = board[possibility]
		if row.count(0) == 1:
			if row.count(team) == 2:
				return True
	return False

def get_board_config(board: Board) -> tuple:
	board_config = [board[i] for i in range(9)]
	return tuple(board_config)

def find_optimal_move(board: list[list[int]], cross_turn: int):
	global mappings 
	moves = []
	for move in range(9):
		if board[move] == 0:
			if can_win(board, cross_turn):
				mappings[get_board_config(board)] = move
				return True
			elif can_win(board, -cross_turn):
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
	
