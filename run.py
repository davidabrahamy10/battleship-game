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