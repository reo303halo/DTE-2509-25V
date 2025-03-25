
def writeToFile(number, saveFile):
    filename = open(saveFile, "a")
    filename.write(f'{number}\n')
    filename.close()


def fromFileToLst(saveFile) -> list:
    filename = open(saveFile, "r")
    lst = filename.readlines()
    filename.close()

    return lst


def findAverage(lst) -> float: 
    summed = 0
    for number in lst:
        summed += int(number.strip())
    average = summed / len(lst)

    return average

