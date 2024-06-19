for i in range(10,26,5):
    print(i, end=" ")
print()

for i in range(-3,22,3):
    if i < 21:
        print(i, end=", ")
    else:
        print(i)
print()

total = 0
for i in range(10):
    value = float(input("Give me a number: "))
    total += value
print("The average is:", total / 10)
