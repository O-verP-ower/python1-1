import random

def getNunber() :
    return random.randint(1, 46)

lotto = []
num = 0

print("** 로또 추첨을 시작합니다 **")

while True :
    num = getNunber()
    if lotto.count(num) == 0 :
        lotto.append(num)
    
    if len(lotto) >= 6 : # test -> 함수 탈출 
        break

print("추첨된 로또 번호 ==> ", end='') # test -> end=' ' : 줄바꿈을 하지 않음
lotto.sort()
for i in range(0, 6) :
    print("%d " % lotto[i], end='') 