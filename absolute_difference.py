# Takes 2 numbers and returns the absolute difference

def main():
    def request():
        num = float(input("Enter any number: "))
        return num
    
    def absDiff(x,y):
        return abs(x - y)
    
    num1 = request()
    num2 = request()

    print("The absolute difference is:", absDiff(num1, num2) )

main()
