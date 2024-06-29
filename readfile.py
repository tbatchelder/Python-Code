# datafile = open("C:\\Users\\pegac\\OneDrive\\Documents\\Joy of Coding\\Module 01\\Week 03\\add.txt")
datafile = open("add.txt")
for line in datafile:
    print(line.rstrip())
datafile.close()