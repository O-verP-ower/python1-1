import math

r = float(input("원의 반지름을 입력하세요> "))
cf = 2 * math.pi * r

area = math.pi * r**2

print("반지름이", r, "인 원의 둘레는", cf)
print("반지름이", r, "인 원의 넓이는", area)