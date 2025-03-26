select = int(input("입력 진수 결정(16/10/8/2): "))

value = input("값 입력: ")

if select == 16 :
    value = int(value, 16)

if select == 10 :
    value = int(value)

if select == 8 :
    value = int(value, 8)

if select == 2 :
    value = int(value, 2)

print("16진수 ==> ", hex(value))   
print("10진수 ==> ", int(value))
print("8진수 ==> ", oct(value))
print("2진수 ==> ", bin(value))


