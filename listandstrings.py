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