class Car :
    color = ""
    speed = 0
    
    
    def __init__(self, value1, value2) :
        self.color = value1
        self.speed = value2
        
    def upSpeed(self, value) :
        self.speed += value
    
    def downSpeed(self, value) :
        self.speed -= value
        
class Car2 :
    
    name = ""
    speed = 0
    
    def __init__ (self, name, speed) :
        self.name = name
        self.speed = speed
    
    def getName(self) :
        return self.name
    
    def getSpeed(self) :
        return self.speed


myCar1= Car("빨강", 60)
myCar2 = Car("파랑", 30)

car1, car2 = None, None
car1 =  Car2("아우디", 0)
car2 =  Car2("벤츠", 30)

print("자동차1의 색상은 %s 이며, 현재 속도는 %dkm입니다." % (myCar1.color, myCar1.speed))
print("자동차2의 색상은 %s 이며, 현재 속도는 %dkm입니다." % (myCar2.color, myCar2.speed))

print("%s의 현재 속도는 %d입니다." % (car1.getName(), car1.getSpeed()))
print("%s의 현재 속도는 %d입니다." % (car2.getName(), car2.getSpeed()))