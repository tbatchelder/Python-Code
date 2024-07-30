def calculate_sum(n):
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += i
    return sum

result = calculate_sum(10)
print(result)

def print_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num, end=' ')

print_numbers(1, 10)

def multiply_numbers(a, b):
    return a * b

result = multiply_numbers(3, 4) + multiply_numbers(2, 5)
print(result)

def calculate_average(numbers):
    sum = 0
    count = 0
    for num in numbers:
        sum += num
        count += 1
    average = sum / count
    return average

scores = [85, 92, 78, 90, 88]
result = calculate_average(scores)

if result >= 80:
    print("Congratulations! You passed.")
else:
    print("Sorry, you failed.")