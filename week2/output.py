#하나만 출력합니다.
print("# 하나만 출력합니다.")
print("Hello Python Programming...!")
print() # 줄바꿈 

#여러 개를 출력합니다.
print("# 여러 개를 출력합니다.")
print(10, 20, 30, 40, 50)
print("안녕하세요", "저의", "이름은", "윤인성입니다!")
print()

#아무 것도 출력하지 않으면 단순하게 줄바꿈합니다.
print("# 아무 것도 출력하지 않습니다.")
print("--- 확인 전용선 ---")
print()
print()
print("--- 확인 전용선 ---")

#이스케이프 문자
print("이름\t나이\t지역") # \t -> 공백 
print("윤인성\t25\t강서구")
print("윤아린\t24\t강서구")
print("구름\t3\t강서구")

#출력합니다.
print("문자 범위 선택 연산자")
print('"안녕하세요"[0:2]:', "안녕하세요"[0:2])
print('"안녕하세요"[1:3]:', "안녕하세요"[1:3])
print('"안녕하세요"[2:4]:', "안녕하세요"[2:4])
print()

print("""여
         러
         줄""")

print("연" + "결됩니다.") # 연결됩니다.

print("안녕하세요"*3) # 3번 출력합니다.
print("안녕하세요"[0]) # '안' 출력 
print(len("안녕하세요")) # 5

print('\' 아아')
input_a = float(input("첫 번째 숫자> "))
input_b = float(input("두 번째 숫자> "))

print("덧셈 결과: ", input_a+input_b)
print("뺄셈 결과: ", input_a-input_b)
print("나눗셈 결과: ", input_a/input_b)
print("곱셈 결과: ", input_a*input_b)