# Input 20 numbers and spit back the average
# myNums = []
# for i in range(21):
#     myNums.append(eval(input("Please enter a number: ")))

# print("Average:", sum(myNums) / 20)

def mangle(str):
    strMod = str.upper()
    strMod = strMod[:2] + strMod[3:]
    strMod = strMod[:-3] + strMod[-2:]
    return strMod

# We can set up a test for this by:
# def main():
#     test_input = ["hellothere", "42 degrees Celsius", "eeeeeee"]
#     test_output = ["HELOTHRE", "42DEGREES CELSUS", "EEEEE"]
#     for i in range(len(test_input)):
#         print("Mangle: ", test_input[i], mangle(test_input[i]) == test_output[i])
# therefore, if the mangle test outputs the same as test_output, it will return True so we know we passed

print(mangle("hellothere"))
print(mangle("42 degrees Celsius"))
print(mangle("eeeeeee"))

def count_e(str):
    count = 0 
    for i in str:
        count += i.count('E')
        count += i.count("e")
    return count

print(count_e(["hi", "hello", "EEK!"]))

def count_vowels(str):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in str:
        test = i.lower()
        strLen = len(i)
        for x in range(strLen):
            if test[x] in vowels:
                count += 1
    return count

print(count_vowels(["hi", "hello", "OOF!"]))