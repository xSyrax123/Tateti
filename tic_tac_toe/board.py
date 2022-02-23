from fields import Fields
from itertools import chain


class Board:
    WAYS_TO_WIN = (
        # Rows.
        slice(0, 3),
        slice(3, 6),
        slice(6, 9),
        # Columns.
        slice(0, 7, 3),
        slice(1, 8, 3),
        slice(2, 9, 3),
        # Diagonals.
        slice(0, 9, 4),
        slice(2, 7, 2),
    )

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
        
    @property
    def board_full(self):
        """Return True if every space on the board
        has been taken. Otherwise return False.
        """
        return Fields.FIELD_EMPTY.value not in self.board

    def check_win(self, board, letter):
        """Given a board and a player letter
        return True if that player has won.
        """
        return any(board[s] == [letter, letter, letter] for s in self.WAYS_TO_WIN)