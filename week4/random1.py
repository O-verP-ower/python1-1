import random 

numbers = []

for num in range(0, 10) :
    numbers.append(random.randrange(0, 10))
    

print("생성된 리스트", numbers)

for num in range(0, 10) :
    if not num in numbers :
        print("숫자 %d는 리스트에 없네용" % num)
    