def para_func(*para) :
    result = 0 
    for num in para :
        result += num
    return result

hap = 0 

hap = para_func(1,2)
print("매개변수가 2개인 함수를 출력한 결과 ==> %d " % hap)
hap = para_func(1,2,3)
print("매개변수가 3개인 함수를 출력한 결과 ==> %d " % hap)

hap = para_func(1,2,3,4,5,6,7,8,9,10)
print(hap)

def dic_func(**para2) :
    for k in para2.keys() :
        print("%s -->%d 명 입니다." % (k, para2[k]))
    print(para2)

dic_func(트와이스 = 9, 소녀시대 = 7, 걸스데이 = 4, 블랙핑크 = 4)