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

board = new_board()
board[0][2] = 'X'
board[1][1] = 'O'
render(board)







