# 1a
print("1a")
count = 1
while count < 6:
    print(count)
    count += 1

print("\n")
print("1b")

# 1b
count = 2
while count < 12:
    print(count)
    count += 3

print("\n")
print("1c")

# 1c
count = -10
while count < 1:
    print(count, end=" ")
    count += 2

print("\n")
print("1d")

# 1d
count = 1
while count < 5:
    print("****")
    count +=1

print("\n")
print("2")

# 2
str = "CSCI 150"
strLen = len(str)
count = 0 
while count < strLen:
    print(str[count])
    count += 1

print("\n")
print("3")

# 3
def main():
    list = []
    entry = -1
    while entry != 0:
        entry = float(input("Enter any non-zero number.  Enter 0 to end: "))
        if entry != 0:
            list.append(entry)
    print("The list entered, sorted numerically is:", list.sort())
    print("The sum of all numbers in the list is:", sum(list))
    print("The average of the list is:", sum(list) /  len(list))
    
main()
