def main():
    def add(x,y):
        return (x + y)
    
    def multiply(x,y):
        return (x * y)
    
    first = eval(input("Enter a number: "))
    second = eval(input("Enter a second number: "))
    
    print("Sum:", add(first,second))
    print("Product:", multiply(first,second))

main()