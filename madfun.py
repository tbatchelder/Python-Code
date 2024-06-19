import math

def mather(x):
    anum = abs(x)
    rnum = round(x,0)
    snum = math.sqrt(rnum)

    print(f"The absolute value is: {anum}")
    print(f"The rounded value is: {rnum}")
    print(f"The square root is: {snum}")

myNum = eval(input("Please enter a number: "))

mather(myNum)