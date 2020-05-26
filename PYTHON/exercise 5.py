
# 1 

list1 = [14,46,43,27,57,41,45,21,70]
list2=[]
print("original list :",list1)
for i in range(0,len(list1)):
    for j in range(i,len(list1)):
        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
    list2.append(list1[i])

print("sorted list : ",list2)

#2

number = int(input("enter nuber = "))
list1=[1,14,141,131,444,1,0]

trail=0
search= False

for i in range(len(list1)):
    if list1[i] == number:
        search= True
        print("found")
        

if search == False:
     print("not found")




#4

list1 =["m","na","i","sanyu"]
list2=["y","me","s","kta"]
list3=[]

for i in range(len(list1)):
    list3.append((list1[i]+list2[i]))
    
print(list1)
print(list2)
print(list3)


#5


list1 = [47,64,37,76,95,97]

dict1 = {"sanyukta":47,"hi":95,"python":64}

val= dict1.values()
add=[]
for i in val:
    for j in list1:
        if i == j:
            add.append(j)
        
print(list1)
print(dict1)
print (add)



    
