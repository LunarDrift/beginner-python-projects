def new_board():
    return [
  [None, None, None],
  [None, None, None],
  [None, None, None]
]

def render(board):
    print("""
          0 1 2
         -------
        0|     |
        1|     |
        2|     |
         -------
""")

board = new_board()
board[0][1] = 'X'
board[1][1] = 'O'
render(board)

# Loop through turns until the game is over
#while True:

    # Print the current state of the board
    #render(board)

    # Get the move that the current player is going
    # to make.
    #move_co_ords = get_move()

    # Make the move that we calculated above
    #make_move(board, move_co_ords)

    # Work out if there's a winner
    #winner = check_win(board)

  # If there is a winner, crown them the champion
  # and exit the loop.


  # If there is no winner and the board is full,
  # exit the loop.

  # Repeat until the game is over









