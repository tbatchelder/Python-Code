letters = ["A", "B", "C", "D", "F"]
counts = {}
file = "letter-grades.txt"

for line in open(file):
    letter = line.replace("\n", "")
    # gets the count of letter if it exists, otherwise 0
    count = counts.get(letter, 0)
    # Store count
    counts[letter] = count + 1

print("Letter counts: ")
for l in letters:
    print(l + ":", counts.get(l,0))
print()

print("File grade counts:")
for item in counts.keys():
    print(item + ":", counts[item])