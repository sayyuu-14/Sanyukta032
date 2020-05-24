
# 3


n =int(input("enter the number of rows :"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()





# 2

list_datatypes = [1,"java",4,0.987,"python",1.1,9,"string"]
int_val=[]
float_val=[]
strng_val=[]

for val in list_datatypes:
    if type(val) == int:
        int_val.append(val)
    elif type(val) == float:
        float_val.append(val)
    elif type(val)==str:
        strng_val.append(val)



print("list of all datatypes: \n \t" ,list_datatypes ,"\n")
print("list of integer datatypes : \n \t",int_val ,"\n")
print("list of float datatypes : \n \t",float_val ,"\n")
print("list of string datatypes : \n \t",strng_val ,"\n")





# 1

num=[4,8,3,0,5,1,5,7,5]
square_list=[]
for i in num:
    square_list.append(i*i)


print("list : \n",num)
print("square of the elements in the list : \n", square_list)
    



# 4

mat=[1,2,3,4,5,6,7,8,9]
mat2=[1,2,3,4,5,6,7,8,9]
print(mat ,"\n + \n",mat2,"\n =")
for i in range(0,len(mat)):
   print(mat[i]+mat2[i], end=" ")


# 5

number=int(input("enter a number :"))

add=0

copy=number

while copy>0:
    d=copy%10
    add+=d**3
    copy//=10
if number==add:
    print(number," is narcastic")
else:
    print(number," is not narcastic")


print("Thank you!!")
    








    

