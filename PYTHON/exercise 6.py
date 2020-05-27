
#1
dict1={1:"python",2:"java",3:"big data"}
dict2={}
for key,val in dict1.items():
    if val in dict2:
        dict2[val].append[key]
    else:
        dict2[val]=[key]
print(dict1)
print(dict2)

#1
dict1={1:"python",2:"java",3:"big data"}

dict2=dict((val,key) for key,val in dict1.items())
print(dict1)
print(dict2)



# 4

list1=["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
print(list1,"\n")

sub_list=["h","i","j"]
for i in sub_list:
    list1[2][1][2].append(i)

    
print(list1)


# 5


dict1={"class":{"student":{"name":"sanyukta","marks":{"physics":70,"history":80}}}}

print(dict1["class"])
print(dict1["class"]["student"])
print(dict1["class"]["student"]["marks"])
print("\n marks optained in HISTORY : ",dict1["class"]["student"]["marks"]["history"])



# 2

sel_list=[5,86,23,9,2,886]

print(sel_list)

for i in range(len(sel_list)):
    min_val=min(sel_list[i:])
    ind=sel_list.index(min_val)
    sel_list[i],sel_list[ind]=sel_list[ind],sel_list[i]

print(sel_list)

# 3

in_sort=[65,86,532,99,1,3,6,99,9,0,9]
print (in_sort)
for i in range(len(in_sort)):
    val=in_sort[i]

    while in_sort[i-1] > val and i > 0:
        in_sort[i],in_sort[i-1]=in_sort[i-1],in_sort[i]
        i = i-1
print(in_sort)
        
