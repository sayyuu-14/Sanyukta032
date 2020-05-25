
#1

def big(no1,no2,n03):
    if no1>=no2 and no1>=no2:
        print("maximum number is :" ,no1)
    elif no2>no1 and no2>no3:
        print("maximum number is :" ,no2)
    else:
        print("maximum number is :" ,no3)

big(8,1,1)


#2


def count_local():
    a=2
    b=98
    c=97
    d=987
    f=97
    c="hello"
    print(locals())

count_local()
print("the number of local variable are :",len(locals()))



#3

# using recursive 

def add(nos):
    if nos==0:
         return nos
    else:
         return nos + add(nos-1)
print("sum of numbers from 1 to 10 =",add(10))

# without recursive

def add(nos):
    x = 0
    for i in nos:
        x = x+i
    return x
print("sum of numbers from 1 to 10 =",add(range(1,11)))



#4



def show_student(name,id1=1,college="vita"):
    print("student id :",id1,"\ncollege name :",college,"\nstudent name :",name)


name=input("enter your name :")
id1=input("enter your id :")
college=input("enter your college name:")


if id1!="" and college!="" :
    show_student(name,id1,college)

else:
     show_student(name)
     




#5

def u(u_list):
    print("sample list :",sorted(u_list))
    print("unique list :",sorted(list(set(u_list))))

u([11,22,22,33,33,33,44,55,55,66])

#6
digit =input("enter number ")
def one(digit):
    return digit[0]

def two(digit):
    return digit[-1]

    

first_digit=int(one(digit))
second_digit=int(two(digit))
print("sum of 1st and last digit :",(first_digit+second_digit))







