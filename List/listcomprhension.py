# List Comprehension 

L = [1,2,3,4,5,6,9]

# multiply the items in 'l' with 5   
# 1. regular method
New_list = []
for i in range(0, len(L)):
    New_list.append(L[i]*5)
print(New_list)

# using list comprehension
New_list_2= [1,2,3,4,5,6,7]
New_list_2 = [x*5 for x in New_list_2 ]
print(New_list_2)

#  conditional list comprehension
Mega_list_7 =[x for x in range(10) if x < 5]
print(Mega_list_7)
