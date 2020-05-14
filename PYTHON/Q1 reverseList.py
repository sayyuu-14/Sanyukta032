my_list = []
n = int(input("enter elements"))
for i in range(0, n):
   element = int(input())
   my_list.append(element)
   new_list = my_list[::-1]
print("reversed list is:",new_list)