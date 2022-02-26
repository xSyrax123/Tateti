from constants import FIELD_EMPTY, WAYS_TO_WIN


class Board: 
    def __init__(self):
        self.board = [FIELD_EMPTY] * 9
        
    def __str__(self):
        """Return a string with game board."""
        return "{}║{}║{}\n═╬═╬═\n{}║{}║{}\n═╬═╬═\n{}║{}║{}".format(*self.board)

    def board_full(self):
        """Return True if every space on the board
        has been taken. Otherwise return False."""
        return FIELD_EMPTY not in self.board

    def check_win(self, board, letter):
        """Given a board and a player letter
        return True if that player has won."""
        return any(board[s] == [letter, letter, letter] for s in WAYS_TO_WIN)
