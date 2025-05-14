inFp = None
inStr = ""

inFp = open("C:\\python1-1\\python1-1-1\\week11\\data.txt", "r", encoding='UTF8')

while True :

    inStr = inFp.readline()
    if inStr == "" :
        break;
    print(inStr, end="")


inFp.close()