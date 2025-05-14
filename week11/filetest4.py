inFp = None
inList, inStr = [], ""

inFp = open("C:\\python1-1\\python1-1-1\\week11\\data.txt", "r", encoding='UTF8')

inList = inFp.readlines()
for inStr in inList :
    print(inStr, end="")

inFp.close()