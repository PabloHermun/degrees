"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    In the initial game state, X gets the first move. 
    Subsequently, the player alternates with each additional move.
    """
    if board_sum(board)%2 == 0:
        return X
    else:
        return O

def board_sum(board):
    """
    Counts number of tiles played so far
    """
    board_sum = 0
    for row in board:
        for entry in row:
            if entry != EMPTY:
                board_sum += 1
    return board_sum

def actions(board):
    """
    Returns set of all possible actions (i, j) available (EMPTY tiles) on the board.
    """
    allowed_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                allowed_actions.add((i,j))
    return allowed_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
    # Copy the input board and add the action according to current player
    if action in actions(board):
        for i in range(3):
            for j in range(3):
                if (i,j) == action:
                    new_board[i][j] = player(board)
                else:
                    new_board[i][j] = board[i][j]
        return new_board
    else:
        raise ValueError

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # Check rows
    for i in range(3):
        symbol = board[i][0]
        if board[i][1] == symbol == board[i][2] != EMPTY:
                return symbol
    # Check columns
    for j in range(3):
        symbol = board[0][j]
        if board[1][j] == symbol == board[2][j] != EMPTY:
                return symbol

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[2][0] == board[1][2] == board[0][2] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    In order for there to be a winner there must be at least five tiles played
    """
    tiles_played = board_sum(board)
    # Check if enough tiles have been played
    if tiles_played < 5:
        return False

    # Check if all tiles have been played
    if tiles_played > 8:
        return True
    
    # Check if there is a winner
    return True if winner(board) != None else False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    numerized = {X: 1, O: -1, None: 0}

    return numerized[winner(board)]


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    Recursive?
    Minimax will never receive a terminal board directly, only recursively.
    TODO: as of now it returns the utility value of the current board at every level,
    but it ultimately musts return the optimal action
    """
    
    utilities = {}
    for action in actions(board):
        scenario = result(board,action)

        if terminal(scenario): 
            return utility(scenario)

        utilities[action] = minimax(scenario)
    
    if player(board) == X:
        return max(utilities.values())
    if player(board) == O:
        return min(utilities.values())

    raise NotImplementedError
