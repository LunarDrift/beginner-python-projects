def new_board():
    return [
  [None, None, None],
  [None, None, None],
  [None, None, None]
]

def render(board):
    print("    0   1   2")                                          # Print column numbers
    print("  -------------")                                        # Print top border
    for i, row in enumerate(board):                                 # Go through each row
        # Replace None or "" with a space
        symbol = [cell if cell else " " for cell in row]       # Use nested loop to iterate through each cell in the row
        # Use f string to keep spacing even
        print(f"{i} | {' | '.join(symbol)} |")

        print("  -------------")                     # Print bottom border

# board = new_board()
# board[0][2] = 'X'
# board[1][1] = 'O'
# render(board)

def get_player_move(player_symbol, board):
    """Ask the player for 2 numbers - row and column.
    Must include validation. Check if the numbers are within the valid range(0-2) and
    check if the cell is already taken. If move is invalid, ask again."""
    while True:     # Loop until a valid move is entered
        try:
            # Ask for player input. .split() gives 2 lists of strings
            row, column = input(f"'{player_symbol}' Player: Enter a 'Row,Column' pair: ").split(",")
            # Convert those strings into integers
            row = int(row)
            column = int(column)

            # Check if row/column is valid
            if 0 <= row <= 2 and 0 <= column <= 2:
                if board[row][column] is None:      # Check if cell is empty
                    board[row][column] = player_symbol
                    break       # Move was successful -> exit loop
                else:
                    print("That cell is already taken! Try again.")
            else:
                print("Row and Column must be 0, 1, or 2. Try again.")

        except ValueError:
            print("Invalid input format! Enter two numbers separated by a comma, e.g. '1,2'.")

def check_win(board, player_symbol):
    """Returns True if player has won, False otherwise.
    Break problem down into 8 possible winning lines:
     - 3 Horizontal rows: use loop to check if all 3 elements in board[0], then board[1], then
         board[2] are the same and equal to the player_symbol
     - 3 Vertical columns: Must fix the column index(0, 1, or 2) and check across all 3 rows.
        Example: check if board[0][0], board[1][0], AND board[2][0] are the same
     - 2 Diagonals: Must be checked explicitly - don't follow simple looping pattern:
                - Top-Left to Bottom-Right:
                    board[0][0], board[1][1], board[2][2]
                - Top-Right to Bottom-Left:
                    board[0][2], board[1][1], board[2][0]"""

    """Horizontal wins"""
    for row in board:
        # Check if all cells in a Row contain the player symbol
        if all(cell == player_symbol for cell in row):
            return True
        
    """Vertical wins"""
    # The Row changes, but the Column stays the same. Simple loop through Column indices
    # Checks each Column individually, if all 3 cells in a Column equal player symbol, return True
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] == player_symbol:
            return True
        
    """Diagonal wins"""
    # Top-Left to Bottom-Right
    if board[0][0] == board[1][1] == board[2][2] == player_symbol:
        return True
    
    # Top-Right to Bottom-Left
    if board[0][2] == board[1][1] == board[2][0] == player_symbol:
        return True
    
    # Default status is False - No winner yet
    return False

def main():
    # Create a new, empty board
    board = new_board()
    # Decide which player goes first
    current_player = 'X'
    # Show empty board before first move
    render(board)

    # Repeat for up to 9 turns (Max amount of turns in Tic Tac Toe)
    for turn in range(9):
        # Get the player's move
        get_player_move(current_player, board)
        # Render board again after player move
        render(board)
        # Check for a winner
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break           # Exit out of the loop
        # Switch player each turn
        current_player = 'O' if current_player == 'X' else 'X'

    else:
        print("Tie Game! There is no winner.")




if __name__ == "__main__":
    main()



