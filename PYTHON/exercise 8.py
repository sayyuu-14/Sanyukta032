
#Write a program to implement Constructor Overloading.

class demo:
    result=0
    def add(self,typeof,*args):
        if typeof == "init":
            result = 0
        if typeof == "str":
            result = ' '
        for i in args:
            result = result + i
        print(result)

d=demo()
d.add("init",35,23,64,2,6)
d.add("str","hello","bye")



#Write a program to implement multiple inheritance.


class Cal:  
    def Sum(self,a,b):  
        return a+b;  
class Cal2:  
    def Mul(self,a,b):  
        return a*b;  
class Dev(Cal,Cal2):  
    def Divide(self,a,b):  
        return a/b;  
d = Dev()  
print(d.Sum(10,20))  
print(d.Mul(10,20))  
print(d.Divide(10,20))


#Write a program to implement operator overloading in python.


class power:
    def __init__(self,x):                  
        self.x=x
    def __pow__(self,other):
        return self.x**other.x             
a=power(2)
b=power(10)
print(a**b)

#Write a Python program to square and cube every number in a given list of integers using Lambda.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst)
square = list(map(lambda x: x ** 2, lst))
print(square)
cube = list(map(lambda x: x ** 3, lst))
print(cube)




#Write a program to implement Constructor with Variable Number of Arguments.


def foo(*tupple,**dictionary): 
    print(tupple) 
    print(dictionary) 
  
foo('python','for','fun',first="python",mid="for",last="fun") 
