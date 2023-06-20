class Board: 
	
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

	def can_win(self, team: int) -> list[int]: 
		""" if checking if cross can win, pass 1. if checking circle, pass -1. returns a list of winning moves. """
		winning_moves = []
		for possibility in Board.WIN_INDECES:
			row = self[possibility]
			if row.count(0) == 1 and row.count(team) == 2:
				winning_moves.append(possibility[row.index(0)])
		return winning_moves

	def can_fork(self, team: int) -> list[int]:
		""" checking if the move would lead to a fork """
		chances = [] 
		for possibility in Board.WIN_INDECES:
			row = self[possibility]
			if row.count(0) == 2 and row.count(team) == 1:
				chances.append({*possibility})
		
		forks = set()
		for chance in chances:
			for other_chance in chances:
				if len(winning_moves:=(chance&other_chance)) == 1:
					if self[winning_move:=winning_moves.pop()] == 0:
						forks.add(winning_move)
		return [*forks]

	@property
	def config(self) -> tuple:
		board_config = [self[i] for i in range(9)]
		return tuple(board_config)

def test_board():
	
	board = Board([
		[1, 0, 1],
		[-1, -1, 1],
		[0, 0, -1]
	])

	assert board.config == (1, 0, 1, -1, -1, 1, 0, 0, -1)
	assert board.can_win(1) == [1]

	other_board = Board([
		[-1, 0, 1],
		[0, 1, 0],
		[0, -1, 0]
	])

	assert other_board.can_fork(-1) == [6]

if __name__ == "__main__":

	test_board()
