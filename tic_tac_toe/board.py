from constants import WAYS_TO_WIN
from itertools import chain


class Board: 
    def __init__(self):
        self._board = [" "] * 9
        
    def __str__(self):
        """Return a string with game board."""
        return "{}║{}║{}\n═╬═╬═\n{}║{}║{}\n═╬═╬═\n{}║{}║{}".format(*chain(self._board))

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board
        
    def board_full(self):
        """Return True if every space on the board
        has been taken. Otherwise return False.
        """
        return FIELD_EMPTY not in self.board

    def check_win(self, board, letter):
        """Given a board and a player letter
        return True if that player has won.
        """
        return any(board[s] == [letter, letter, letter] for s in WAYS_TO_WIN)
