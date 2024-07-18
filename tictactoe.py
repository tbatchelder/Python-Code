# Determine if a player won
# player = X or O
# board is the board list

def col_check(col, player, board):
  counter = 0

  for row in range(3):
    if board[row][col] == player:
      counter += 1
  return counter


def row_check(row, player, board):
  counter = 0

  for col in range(3):
    if board[row][col] == player:
      counter += 1
  return counter


def did_I_win(player, board):
  # Initialize the variables
  win = False
  counter = 0

  # Check all 3 verticals
  for col in range(3):
    if col_check(col, player, board) == 3:
      return True
    
  # Check all 3 horizontals
  for row in range(3):
    if row_check(row, player, board) == 3:
      return True
    
  # Check the diaginals
  for row_col in range(3):
    if board[row_col][row_col] == player:
      counter += 1
  if counter == 3:
    return True
  else:
    counter = 0
  
  if board[0][2] == player:
    counter += 1
  if board[1][1] == player:
    counter += 1
  if board[2][0] == player:
    counter += 1
  if counter == 3:
    return True

  return win


print(did_I_win("X", [["O", "O", "X"], ["O", "X", "O"], ["X", "O", "O"]]))
print(did_I_win("O", [["O", "O", "X"], ["O", "X", "O"], ["X", "O", "O"]]))
print(did_I_win("X", [["O", "O", "X"], ["O", "O", "X"], ["O", "O", "X"]]))
print(did_I_win("O", [["O", "O", "X"], ["O", "O", "X"], ["O", "O", "X"]]))