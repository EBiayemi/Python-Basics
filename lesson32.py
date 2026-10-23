class MyClass:
    privateVar = 10
    def __privMeth(self):
        print("This is a private method")
    def hello(self):
        print(MyClass.privateVar)
obj = MyClass()
obj.hello()
#Activity 2
class Computer:
    def __init__(self, max_price):
        self.__max_price = max_price
    def sell(self):
        print("Selling Price:", self.__max_price)
    def setmaxprice(self, price):
        self.__max_price = price
computer1 = Computer(1000)
computer1.sell()
computer1.setmaxprice(15000)
computer1.sell()
computer1.setmaxprice(2000)
computer1.sell()
#Activity 3
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
p1 = Point(3,5)
print(p1)