from constants import FIELD_X, FIELD_O, FIELD_EMPTY, WAYS_TO_WIN
from illegal_move import IllegalMove


class Board: 
    def __init__(self):
        self.board = [FIELD_EMPTY] * 9
        
    def __str__(self):
        """Return a string with game board."""
        return "{}║{}║{}\n═╬═╬═\n{}║{}║{}\n═╬═╬═\n{}║{}║{}".format(*self.board)

    def check_win(self):
        for letter in (FIELD_X, FIELD_O):
            victory = [letter, letter, letter]
            if any(self.board[s] == victory for s in WAYS_TO_WIN):
                return letter
        return None

    def open_spots(self):
        return [i + 1 for i, cell in enumerate(self.board) if cell == FIELD_EMPTY]

    def play(self, letter, spot):
        i = spot - 1
        if self.board[i] == FIELD_EMPTY:
            self.board[i] = letter
        else:
            raise IllegalMove(f"Spot {spot} is already occupied.")
