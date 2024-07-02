def hourGlassSum(array):
  # Container for 2D integer list
  arr = []

  # After searching a bit for what "6 lines of inputs contain 6 space-separated intergers", we determined that meant
  # a 1D list of 6 items.  Each item has 6 integers in it which are separated by a space.
  # However, based on the examples, the number of spaces is NOT exactly 1 all of the time, so we need to strip ALL spaces.
  # Once we get the list of separated strings, we can convert that into a list using list(map(int, array)) ... which we haven't learned yet.
  # So, we split the string first based upon the given "space-separated" criteria
  #   then we strip out all other whitespace from the array[i]
  for i in range(6):
    arr_temp = list( map( int, array[i].strip().split(' ') ) )
    arr.append(arr_temp)
  
  # Now that we have a 2D array, we can solve the problem
  # We can do this one of 2 ways - from row 0 and counting out the hourglass shape to the next 2 rows
  # Or starting at row 1 and counting the row above and below it.
  # Either way, we need to only cycle thru a 4 counts since only 4 hoursglasses are present per row and column.
  # We need to store the total value of all 16 so we can get the maximum value at the end.
  totals = []

  for i in range(4):
    for j in range(4):
      # Ok, so, much like strings, we can tell sum to sum a list of numbers using ":"
      # print(sum(arr[i][j:j+3]))
      # print(arr[i+1][j+1])
      # print(sum(arr[i+2][j:j+3]))
      total = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
      totals.append(total)
  
  # Now that we have the right example list, how do we find the max?
  return max(totals)

print(hourGlassSum(["-9 -9 -9 1 1 1","0 -9 0 4 3 2","-9 -9 -9 1 2 3","0 0 8 6 6 0","0 0 0 -2 0 0","0 0 1 2 4 0"]))