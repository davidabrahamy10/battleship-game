class BattleshipBoard:
    """
    A class that represents the board for the game Battleship.
    """

    def __init__(self, board):
        """
        The constructor for BattleshipBoard class.
        """

        self.board = board

    def letters_and_numbers_dict(self):
        """
        A method that returns a dictionary mapping letters to numbers for use in printing the board.
        """
        return {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}

    def print_board(self):
        """
        A method that prints the board.
        """
        print("  A B C D E F")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

class Battleship:
    """
    A class that represents the game Battleship.
    """

    def __init__(self, board):
        self.board = board

    def create_ships(self):
        """
        A method that places the ships randomly on the board.
        """
        for i in range(5):
            self.number_row, self.letter_column = randint(0, 5), randint(0, 5)
            while self.board[self.number_row][self.letter_column] == "X":
                self.number_row, self.letter_column = randint(
                    0, 5), randint(0, 5)
                if all(self.board[x][y] != "X" for x in range(5) for y in range(5)):
                    break
            self.board[self.number_row][self.letter_column] = "X"

        return self.board

    def player_input(self):
        """
        A method that gets player input for the guess of a ship's location.
        """
        while True:
            number_row = input("Enter the row number of the ship (1-6): ")
            if number_row in '123456':
                break
            else:
                print('Invalid choice. Please select a valid row.')

        while True:
            letter_column = input(
                "Enter the column letter of the ship (A-F): ").upper()
            if letter_column in "ABCDEF":
                break
            else:
                print('Invalid choice. Please select a valid column.')

        letters_and_numbers_dict = BattleshipBoard.letters_and_numbers_dict(
            self)
        return int(number_row) - 1, letters_and_numbers_dict[letter_column]

    def count_hit_ships(self):
        """
        Counts the number of ships that have been hit on the game board.
        """
        return sum([row.count("X") for row in self.board])