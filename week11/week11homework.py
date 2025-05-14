inFp = None
inList, inStr = [], ""

number = 1

filename = input("파일명을 입력하세요 : ")
inFp = open("C:\\python1-1\\python1-1-1\\week11\\data2.txt", "r", encoding='UTF8')

inList = inFp.readlines()
for inStr in inList :
    print("%d:" % number, inStr, end="")
    number += 1

inFp.close()