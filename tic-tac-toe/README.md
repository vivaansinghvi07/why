# Tic-Tac-Toe

This program generates a model that contains pretty much every tic-tac-toe board, and the "optimal" computer move(s) for that position. Obviously, there is no need to make it this complicated. It is assumed that cross always goes first.

## Versions

- Version 1: Recursively generates boards in a backtracking manner and decides where the best move is (if any team has two in a row, it is optimal to place the piece there, otherwise, continue). This method is not very good for accuracy.
- Version 2: All legal game configurations are considered, and simple logic is used to find the optimal move for each configuration.

## Usage

To use, you can do either of the following :
- Run `$ python3 use.py VERSION`, where `VERSION` is either `v1` or `v2`, and play the computer.
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
  
    ```
    >>> model[(1, 1, 0, -1, 0, 0, 0, 0, 0)]
    [2]
    ```
  - This corresponds to a board that looks like this (it is interpreted that it is O's turn):

    ```
     X | X | 
    -----------
     O |   |   
    -----------
       |   | 
    ```
