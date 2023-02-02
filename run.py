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


def RunGame():
    """
    Run the game of Battleship. Initialize and reset the computer and player guess boards, 
    create ships on the computer board, and start 10 turns for the player to guess the 
    location of the computer's ships. If all ships are hit, the player wins. If the player 
    runs out of turns, the player loses.
    """
    welcome_text()
    computer_board = BattleshipBoard([[" "] * 6 for i in range(6)])
    player_guess_board = BattleshipBoard([[" "] * 6 for i in range(6)])
    Battleship.create_ships(computer_board)

    turns = 10
    while turns > 0:
        BattleshipBoard.print_board(player_guess_board)

        player_number_row, player_letter_column = Battleship.player_input(
            object)

        while player_guess_board.board[player_number_row][player_letter_column] == "-" or player_guess_board.board[player_number_row][player_letter_column] == "X":
            print("You have already guessed that position")
            player_number_row, player_letter_column = Battleship.player_input(
                object)

        if computer_board.board[player_number_row][player_letter_column] == "X":
            print("You sunk 1 of the computers battleship!")
            player_guess_board.board[player_number_row][player_letter_column] = "X"
        else:
            print("You missed the computers battleship!")
            player_guess_board.board[player_number_row][player_letter_column] = "-"

        if Battleship.count_hit_ships(player_guess_board) == 5:
            print("You hit all 5 of the computers battleships!")
            print("Well done! You won the game!")3
            restart_game()
        else:
            turns -= 1
            print(f"You have {turns} turns remaining")
            if turns == 0:
                print("*"*20)
                print("Sorry you ran out of turns")
                print("You lost the game!")
                print("*"*20)
                BattleshipBoard.print_board(player_guess_board)
                restart_game()


def restart_game():
    """
    Prompt the player to restart the game and run the RunGame function if the player inputs 
    "yes", or quit the game if the player inputs "no". If the player inputs any other string, 
    repeat the prompt.
    """
    player_input = input("Would you like to restart the game? (yes/no): ")
    if player_input.lower() == "yes":
        RunGame()
    elif player_input.lower() == "no":
        quit()
    else:
        print("Please type Yes or No")
        restart_game()def restart_game():
    """
    Prompt the player to restart the game and run the RunGame function if the player inputs 
    "yes", or quit the game if the player inputs "no". If the player inputs any other string, 
    repeat the prompt.
    """
    player_input = input("Would you like to restart the game? (yes/no): ")
    if player_input.lower() == "yes":
        RunGame()
    elif player_input.lower() == "no":
        quit()
    else:
        print("Please type Yes or No")
        restart_game()


def welcome_text():
    """
    Print a welcome text to the player to introduce the game of Battleship.
    """
    print("*"*30)
    print("Welcome to Battleship!")
    print("*" * 30)
    print("In this game, you will try to sink the computers ships.")
    print("5 ships are hidden on the board and you have 10 guesses.")
    print("Let's get started!")
    print("*" * 30)