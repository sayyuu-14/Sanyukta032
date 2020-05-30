
# 1

n = int(input("enter a number :"))
sum1=0
str1=''
for i in range(1,n+1):
    sum1=sum1+i
    str1=str1+str(i)+' + '
print(str1[:-2],"=",sum1)
    





#5

n = int(input("enter rows :"))

for i in range(1,n+1):
    print((str(i)+" ")*i)



#3

n = int(input("enter number :"))
for i in range(1,11):
    print((str(n)+" x "+str(i))+" =",(n*i))


#2


series =[1,2,3,4,5,6,7,8,9,86,9,5,3,9,3]
even,odd=0,0
for i in series:
    if i % 2== 0:
        even=even+1
    else:
        odd=odd+1

print("even numbers count :",even)

print("odd numbers count :",odd)    



 
#4
#solution :

n = int(input("enter the rows :"))
num=1
for i in range(1,n+1):
    print(" "*(n-i+1),end="  ")
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+2
    print()

def sum(number):
    return (number*number*number)

number=int(input("enter the row :"))
print("the sum of consecutive odd numbers :", sum(number))
    



