from board import *
from field_is_occupied import *
from invalid_input import *
from copy import deepcopy
from random import choice


class TicTacToe:
    SPACER = "-" * 50

    def __init__(self):
        self.board = Board()

    @property
    def select_letter(self):
        """Returns a tuple with the letter chosen by the player and the one chosen by the computer."""
        computer_letter = None
        player_letter = None

        while True:
            player_letter = input("Choose your side: ").upper()

            if player_letter not in Fields.FIELDS_X_O.value:
                print("You can only choose X or O.")
            else:
                break

        computer_letter = "O" if player_letter == "X" else "X"
        print(f"The computer has chosen to be {computer_letter}.")
        print(f"You will be {player_letter}.")
        return player_letter, computer_letter

    @property
    def human_goes_first(self):
        """Returns True if human chooses "yes" else False."""
        go_first = None
        while go_first not in ("yes", "no"):
            go_first = input(("Do you require the first move? (yes/no): ")).lower()
        return go_first == "yes"

    def get_random_move(self, moves):
        """Returns a valid move from the passed list on the passed board.
        Returns None if there is no valid move.
        """
        possible_moves = [i for i in moves]
        return choice(possible_moves) if len(possible_moves) != 0 else None

    def computer_move(self, player_letter, computer_letter):
        """Given a board, the player's letter and the computer's
        letter, determine where to move to and the computer's
        letter is placed on the board in the determined position.
        """
        board_copy = deepcopy(self.board.board)
        corners = (0, 2, 6, 8)
        sides = (1, 3, 5, 7)
        # First, check if we can win in the next move.
        for i in range(8):
            if board_copy[i] == Fields.FIELD_EMPTY.value:
                board_copy[i] = computer_letter
                if self.board.check_win(board_copy, computer_letter):
                    self.board.board[i] = computer_letter
                    return

        # Check if the player could win on their next move, and block them.
        for i in range(8):
            if board_copy[i] == Fields.FIELD_EMPTY.value:
                board_copy[i] = player_letter
                if self.board.check_win(board_copy, player_letter):
                    self.board.board[i] = computer_letter
                    return

        # Try to take one of the corners, if they are free.
        move = self.get_random_move(corners)
        if move:
            self.board.board[move] = computer_letter
            return

        # Try to take the center, if it's free.
        if self.board.board[4] == Fields.FIELD_EMPTY.value:
            self.board.board[4] = computer_letter
            return

        # Move on one of the sides.
        move = self.get_random_move(sides)
        self.board.board[move] = computer_letter

    def player_move(self, letter):
        """The player chooses the position on the
         board and the player's letter is placed
         on the board at the entered position.
        """
        while True:
            try:
                move = int(input(f"It's your turn {letter}. Enter a number [1-9]: ")) - 1
                if not 0 <= move <= 8:
                    raise InvalidInput("The number entered is invalid. Enter a number between 1 and 9.")
                elif self.board.board[move] != Fields.FIELD_EMPTY.value:
                    raise FieldIsOccupied("This field is already occupied.")
                else:
                    self.board.board[move] = letter
                    break
            except ValueError:
                print(f"Enter a number!\n\n{self.SPACER}\n")

    def play(self):
        """The game stage."""
        print("Welcome to Tic Tac Toe!")
        human, computer = self.select_letter
        first_player = self.human_goes_first
        print(f"\n{self.SPACER}")

        while not self.board.board_full:
            if first_player:
                print(f"\nNow playing: Human ({human})")
                self.player_move(human)
            else:
                print(f"\nNow playing: Computer ({computer})")
                self.computer_move(human, computer)
            
            print(f"\n{self.board}")
            print(f"\n{self.SPACER}")
            first_player = False if first_player else True

            if self.board.check_win(self.board.board, human):           
                print("\nYou won!")
                print("Thanks for playing!")
                break
            elif self.board.check_win(self.board.board, computer):
                print("\nComputer won!")
                print("Thanks for playing!")
                break
        else:
            print("\nNobody won, it's a tie.")


def main():
    game = TicTacToe()
    game.play()


if __name__ == '__main__':
    main()
