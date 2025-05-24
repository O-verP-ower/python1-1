# Homework : self-study 1, 2, 3
# class : 현실 세계의 사물을 컴퓨터 안에서 구현하려고 고안된 개념 
# Class의 인스턴스 = Object (객체)
class Car :
    color = ""
    
    def upSpeed(self, value) : # self를 쓰는 이유 : 객체 자신을 가리키기 위함
        self.speed += value
    
    def downSpeed(self, value) :
        self.speed -= value

    def printMessage() :
        print("시험 출력이다.")
        

mycar1 = Car()
mycar1.color = "빨강"
mycar1.speed = 0

mycar2 = Car()
mycar2.color = "파랑"
mycar2.speed = 0

mycar3 = Car()
mycar3.color = "노랑"
mycar3.speed = 0

mycar1.upSpeed(30)
print("자동차1의 색상은 %s 이며, 현재 속도는 %dkm입니다." % (mycar1.color, mycar1.speed))

mycar2.upSpeed(60)
print("자동차2의 색상은 %s 이며, 현재 속도는 %dkm입니다." % (mycar2.color, mycar2.speed))

mycar3.upSpeed(0)
print("자동차3의 색상은 %s 이며, 현재 속도는 %dkm입니다." % (mycar3.color, mycar3.speed))