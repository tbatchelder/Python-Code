# Program builds a pyramid using only a single character

def pyramid1(s,h):
    for l in range(1, h+1):
        print(s * l, end="")
        print("")

def pyramid2(s,h):
    for l in range(1, h+1):
        maxString = h + 2
        print(" " * (h - l), end="")
        print(s * (l + (l - 1)), end="")
        print("")

# pyramid1("*", 6)
pyramid2("*",10)