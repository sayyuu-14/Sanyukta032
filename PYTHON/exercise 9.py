# 6

def Fibanocci():

    a=0
    b=1
    for x in range(1,102):
        yield a
        a,b = b, a+b

for i in Fibanocci():
    print(i)

# 5

def arithmetic(self):
    def math(a, b):
        self(a, b)
    return math
         

@arithmetic
def add_subtract(a, b):
    print(" addition ", a + b)
    print(" subtraction ", a - b)

add_subtract(8, 4)


# 1

try:
    x = int(input("Enter number: "))
    y = int(input("Enter number: "))
    print("Division: " + str(a/b))

except(ZeroDivisionError):
    print("You have divided a number by zero, which is not allowed.")
    
except(ValueError):
    print("You must enter integer value")
except:
    print("Something went wrong!")


# 2

# 3

#4
