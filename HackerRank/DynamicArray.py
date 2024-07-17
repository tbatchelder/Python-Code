# Create the function
#
# For each sub-list:
#   1st # = the equation to use
#   2nd # = the calculation to use to determine which sub-list to put the 3rd # into
#   3rd # = the number to put in the sub-list
def dynamicArray(n, queries):
  # Initialize variables
  arr = []
  lastAnswer = 0
  returns = []

  # Use n to make the 2D array
  for i in range(n):
    arr.append([])
  
  # Figure out which formula we are using
  for i in queries:
    if len(i) != 3:
      pass
    else:
      idx = (i[1] ^ lastAnswer) % n
      if i[0] == 1:
        arr[idx].append(i[2])
      if i[0] == 2:
        lastAnswer = arr[idx][i[2] % len(arr[idx])]
        returns.append(lastAnswer)
      print(i, idx, arr, returns)
  return returns

# dynamicArray(5, [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]])
dynamicArray(2, [[2, 5], [1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]])