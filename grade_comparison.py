# How do students in a python class compare to students from a prior semester?
# Use fiel: sample_grades.csv
# Timothy Batchelder

import statistics as s

# Read and process any csv file
def readCsvFile(theFile):
    datafile = open(theFile)

    csvList = []

    for line in datafile:
        itemList = line.strip().split(",")
        csvList.append(itemList)

    datafile.close()

    return csvList

# For this project, we want to specially process some data
def specialProcess(theList):
    newList = []

    for i in range(len(theList)):
        student = theList[i][0]
        temp = theList[i][1].split()
        semester = temp[0]
        year = int(temp[1])
        grade = int(theList[i][2])

        rebuild = [student, semester, year, grade]

        newList.append(rebuild)
    return newList

def listSplitter(theList, col, str):
    newList = []

    for i in theList:
        if i[col] == str:
            newList.append(i)

    return newList

def theGrades(theList):
    newList = []
    for i in theList:
        newList.append(i[3])
    return newList

first = readCsvFile("sample_grades.csv")
second = specialProcess(first)
third = listSplitter(second, 1, "Fall")
fourth = listSplitter(second, 1, "Spring")
theFallGrades = theGrades(third)
theSpringGrades = theGrades(fourth)

print("         Fall 2016    Spring 2016")
print("Mean:     ", round(sum(theFallGrades) / len(theFallGrades),2), "       ", round(sum(theSpringGrades) / len(theSpringGrades),2))
print("Median:   ", round(s.median(theFallGrades), 2), "        ", round(s.median(theSpringGrades),2))
print("STD:      ", round(s.stdev(theFallGrades),2), "        ", round(s.stdev(theSpringGrades),2))