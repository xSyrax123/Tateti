from board import Board
from constants import FIELD_X, FIELD_O, FIELD_EMPTY, SPACER
from collections import deque
from copy import deepcopy
from random import choice


class TicTacToe:
    def __init__(self):
        self.board = Board()

    def select_letter(self):
        """Returns a tuple with the letter chosen by the player and the one chosen by the computer."""
        cpu_letter = None
        human_letter = None

        while True:
            human_letter = input("Choose your side: ").upper()

            if human_letter not in (FIELD_X, FIELD_O):
                print("You can only choose X or O.")
            else:
                break

        cpu_letter = FIELD_O if human_letter == FIELD_X else FIELD_X
        print(f"The computer has chosen to be {cpu_letter}.")
        print(f"You will be {human_letter}.")
        return human_letter, cpu_letter

    def human_goes_first(self):
        """Returns True if human chooses "yes" else False."""
        go_first = None
        while go_first not in ("yes", "no"):
            go_first = input(("Do you require the first move? (yes/no): ")).lower()
        return go_first == "yes"

    def get_random_move(self, moves):
        """Returns a valid move from the passed list on the passed board.
        Returns None if there is no valid move."""
        return choice(moves) if len(moves) != 0 else None

    def computer_move(self, human_letter, cpu_letter):
        """Given a board, the player's letter and the computer's
        letter, determine where to move to and the computer's
        letter is placed on the board in the determined position."""
        board_copy = deepcopy(self.board.board)
        corners = (0, 2, 6, 8)
        sides = (1, 3, 5, 7)
        # First, check if we can win in the next move.
        for i in range(8):
            if board_copy[i] == FIELD_EMPTY:
                board_copy[i] = cpu_letter
                if self.board.check_win(board_copy, cpu_letter):
                    self.board.board[i] = cpu_letter
                    return

        # Check if the player could win on their next move, and block them.
        for i in range(8):
            if board_copy[i] == FIELD_EMPTY:
                board_copy[i] = human_letter
                if self.board.check_win(board_copy, human_letter):
                    self.board.board[i] = cpu_letter
                    return

        # Try to take one of the corners, if they are free.
        move = self.get_random_move(corners)
        if move:
            self.board.board[move] = cpu_letter
            return

        # Try to take the center, if it's free.
        if self.board.board[4] == FIELD_EMPTY:
            self.board.board[4] = cpu_letter
            return

        # Move on one of the sides.
        move = self.get_random_move(sides)
        self.board.board[move] = cpu_letter

    def player_move(self, letter):
        """The player chooses the position on the
         board and the player's letter is placed
         on the board at the entered position."""
        while True:
            try:
                move = int(input(f"It's your turn {letter}. Enter a number [1-9]: ")) - 1
                if not 0 <= move <= 8:
                    print(f"The number entered is invalid. Enter a number between 1 and 9.\n\n{SPACER}\n")
                elif self.board.board[move] != FIELD_EMPTY:
                    print(f"This field is already occupied.\n\n{SPACER}\n")
                else:
                    self.board.board[move] = letter
                    break
            except ValueError:
                print(f"Enter a number!\n\n{SPACER}\n")

    def play(self):
        """The game stage."""
        print("Welcome to Tic Tac Toe!")
        human_letter, cpu_letter = self.select_letter()
        first_player = self.human_goes_first()
        letters = deque((human_letter, cpu_letter) if first_player else (cpu_letter, human_letter))
        players = deque(("Human", "Computer") if first_player else ("Computer", "Human"))
        print(f"\n{SPACER}")

        while not self.board.board_full():
            current_letter = letters[0]
            current_player = players[0]
            print(f"\nNow playing: {current_player} ({current_letter})")

            if current_letter == human_letter:
                self.player_move(human_letter)
            else:
                self.computer_move(human_letter, cpu_letter) 

            print(f"\n{self.board}\n\n{SPACER}")
            
            if self.board.check_win(self.board.board, current_letter):           
                print(f"\n{current_player} won!\nThanks for playing!")
                break

            letters.rotate()
            players.rotate()
        else:
            print("\nNobody won, it's a tie.")


def main():
    game = TicTacToe()
    game.play()


if __name__ == '__main__':
    main()
