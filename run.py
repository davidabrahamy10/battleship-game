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