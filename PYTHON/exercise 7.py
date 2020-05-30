
# 1

class bank_acc:
    def __init__(x,name,balance,number):
        x.name = name
        x.balance = balance
        x.number = number

    def deposit(x,amount):
        x.balance += amount

    def withdraw(x,amount):
        x.balance -=  amount

    def bal(x):
        return x.balance

    def exit(x):
        print(x.name, x.balance, x.number)

obj = bank_acc("sanyukta",10000,199271773)
print("total amount :",obj.balance)
obj.deposit(100)
print("after deposit of 100rs, remaining balance = ",obj.balance)
obj.withdraw(200)
print("withdraw amount 200 , remaining balance =",obj.balance)
print("Hi, ",obj.name,"your account number ",obj.number,"has balance remaining of",obj.balance)


# 5

class math:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def addition(self):
        return self.x+self.y

class math2:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.m=math(x,y)

    def addition(self):
        return self.m.addition()

m=math2(9,4)
print(m.addition())




# 4

import sys
 
class count(object):
  def a(self):
     print("A")
 
f1 = count()
f2 = f1
f3 = f2
 
print(sys.getrefcount(f1))

# 4
import sys
class math:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def addition(self):
        return self.x+self.y

class math2:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.m=math(x,y)

    def addition(self):
        return self.m.addition()

m=math2(9,4)
m.addition()
print(sys.getrefcount(m))




# 2


class Circle():  
    def __init__(self, radius):  
        self.radius = radius  
  
    def area(self):  
        return self.radius**2*3.14  
      
    def perimeter(self):  
        return 2*self.radius*3.14  
  
obj = Circle(10)  
print(obj.area())  
print(obj.perimeter())


# 3

class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

s= Square(9)
print (s.area())
