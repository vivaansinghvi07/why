# Tic-Tac-Toe

This program generates a model that contains pretty much every tic-tac-toe board, and the "optimal" computer move(s) for that position. Obviously, there is no need to make it this complicated. It is assumed that cross always goes first. All legal game configurations are considered, and simple logic is used to find the optimal move for each configuration.

## Usage

To use, you can do `$ python3 use.py` to play against the computer, or:
- Go into a Python session, and run the following:

  ```python3
  >>> import pickle
  >>> model = pickle.load(open('v2.pkl', 'rb'))
  ```

- Then, you can simply create a tuple, length = 9, where each index corresponds to the index on the below reference:

  ```
   0 | 1 | 2
  -----------
   3 | 4 | 5
  -----------
   6 | 7 | 8
  ``` 

- Then, you can get the optimal move by using that tuple as a key:

  ```python3
  >>> model[(1, 1, 0, -1, 0, 0, 0, 0, 0)]
  [2]
  ```
- This corresponds to a board that looks like this (`*` represents O's ideal move):

  ```
   X | X | *
  -----------
   O |   |   
  -----------
     |   | 
  ```
