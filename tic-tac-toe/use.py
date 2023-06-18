import pickle
from pynterface import two_dim_array

def get_input():
	board = two_dim_array(3, 3, item_type=int)
	output = []
	for row in board: output.extend(row)
	return tuple(output)

if __name__ == "__main__":
	with open('model.pkl', 'rb') as f:
		model = pickle.load(f)
	while True:
		inp = get_input()	
		print(model[inp])
