from board import Board
from constants import FIELD_X, FIELD_O, SPACER
from collections import deque
from random import choice


class TicTacToe:
    def __init__(self):
        self.board = Board()
        
    def get_reply(self, prompt, choices, convert=None):
        """Given a question and the choices, returns the answer given by the user."""
        # Prepare the conversion function.
        identity = lambda x: x
        convert = convert or identity

        # Return the first valid reply.
        choices_str = "/".join(str(c) for c in choices)
        while True:
            try:
                reply = input(f"{prompt} ({choices_str}): ").upper()
                val = convert(reply)
                if val in choices:
                    return val
                else:
                    print("Invalid reply.")
            except ValueError:
                print("Invalid reply.")

    def select_letter(self):
        """Returns a tuple with the letter chosen by
        the player and the one chosen by the computer."""
        letters = [FIELD_X, FIELD_O]
        if self.get_reply("Choose your side", letters) == FIELD_O:
            letters.reverse()
        print("You will be {}.\nThe computer will be {}.".format(*letters))
        return letters

    def human_goes_first(self):
        """Returns True if human chooses "yes" else False."""
        go_first = None
        while go_first not in ("yes", "no"):
            go_first = input(("Do you require the first move? (yes/no): ")).lower()
        return go_first == "yes"

    def computer_move(self, human_letter, cpu_letter):
        spot = choice(self.board.open_spots())
        self.board.play(cpu_letter, spot)

    def player_move(self, letter):
        """The player chooses the position on the
         board and the player's letter is placed
         on the board at the entered position."""
        move = self.get_reply(
            f"It's your turn {letter}. Enter a number",
            self.board.open_spots(),
            convert=int
        )
        self.board.play(letter, move)

    def start(self):
        """The game stage."""
        print("Welcome to Tic Tac Toe!")
        counter = 0
        letters = self.select_letter()
        players = deque(zip(
            letters,
            ("Human", "Computer"),
            (self.player_move, self.computer_move),
            (letters[0], letters)
        ))

        if not self.human_goes_first():
            players.rotate()

        while True:
            letter, label, mover, move_args = players[0]
            print(f"\n{SPACER}\nNow playing: {letter} ({label})")
            mover(*move_args)
            print(f"\n{self.board}\n")
            
            if self.board.check_win():           
                print(f"{SPACER}\n\n{label} won!\nThanks for playing!")
                break

            if counter == 9:
                print("\nNobody won, it's a tie.")
                break

            players.rotate()
            counter += 1
