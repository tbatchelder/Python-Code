# Strings, list and whiles
# Timothy Batchelder 
# Like a header for this low level stuff makes ANY difference to anyone

def average_neg_evens(list):
    sumList = []
    i = 0
    while i < len(list):
        item = list[i]
        if (item < 0) and (item % 2 == 0):
            sumList.append(item)
        i += 1
    print(sum(sumList) /  len(sumList))
    return sum(sumList) /  len(sumList)

def count_letter(list):
    count = 0
    i = 0
    while i < len(list):
        item = list[i]
        j = 0
        while j < len(item):
            if item[j].lower() == 'o':
                count +=1
            j += 1
        i += 1
    print(count)

    return count

def main():
    test_input = [0, 1, 2, -2, -3, -4, 3, 4]
    test_output = -3
    print("average_neg_evens: ", test_input, average_neg_evens(test_input) == test_output)

    print("")

    test_input = ["HELLO", "goodbye", "1234 Oooh!"]
    test_output = 6
    print("count_letter: ", test_input, count_letter(test_input) == test_output)

main()