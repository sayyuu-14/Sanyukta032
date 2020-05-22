
#ques 5

age = int(input("enter your age :"))

if age in range(8,13):
    print("welcome you are allowed")
else :
    print("sorry!! you are not allowed")


age = int(input("enter your age :"))

if age>=8 and age<=12:
    print("welcome you are allowed")
else :
    print("sorry!! you are not allowed")






#4 even or odd

number = int (input("enter the number :"))

if number%2==0:
    print("number is even!")
else:
    print("number is odd!")

    

# ques 3

upp = int(input("enter your string :"))
n = []
for i in range(upp):
   
    c=input()
    n.append(c)

for i in n:
    print(i.upper())


# ques 1

for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        print(i, end= ",")



list = [}
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        list.append(str(i))
        
print(",".join(list))



# ques 2
num = int(input())
n = dict()
for i in range(1,num+1):
    n[i]=(i**2)
print(n)


num = int(input())
n = dict()
for i in range(1,num+1):
    n[i]=(i*i)
print(n)




