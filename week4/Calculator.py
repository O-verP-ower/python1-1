select = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계: "))
total = 0
if select == 1 : 

    Modify = input("*** 수식을 입력하세요 :")
    print(Modify + "결과는   " , format(eval(Modify)) + "입니다.")

elif select == 2:

    Start_Number = int(input("*** 첫 번째 숫자를 입력하세요. "))
    End_Number = int(input("*** 두 번째 숫자를 입력하세요. "))

    for i in range (Start_Number, End_Number+1) :
        total = total + i
    
    print(Start_Number,"+...+" ,End_Number, "는" , total, "입니다.")

else : 
    print("등록된 형식이 아닙니다. ")