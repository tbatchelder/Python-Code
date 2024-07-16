# Read a file and put each line into an array
# Author: Timothy Batchelder

# Assign variables
txtLines = []

# Open the file
datafile = open("turing.txt")

# Cycle thru each line and add it to the array
for line in datafile:
  txtLines.append(line)

print("The first line is:", txtLines[0])
print("The second to last line is:", txtLines[-2])
print("The last line is:", txtLines[-1])
print("The number of lines is:", len(txtLines))

# Close the file
datafile.close()