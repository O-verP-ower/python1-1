inFp, outFp = None, None
inStr = ""

inFp = open("C:\\windows\\win.ini", "r")
outFp = open("C:\\python1-1\\python1-1-1\\week11\\data4.txt", "w")

inList = inFp.readlines()

for inStr in inList :
    outFp.writelines(inStr)

inFp.close()
outFp.close()

print("---파일이 정상적으로 복사되었음 ---")