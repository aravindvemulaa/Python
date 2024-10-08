mylist = ['Banana', 'apple', 'guva', 'Orange','Mango','Grapes']
print(mylist)
print(type(mylist))

# A list can be combination of strings, integers and boolean 
# Note: True and 1 are considered as same 
Combination_list = [1," Telangana", 'Kerala', 24, True]
print(Combination_list)
print(type(Combination_list))




# List constructor 

Constructor_list = (('here', 'we', 'have', 'double', 'circle', 'bracket', 'so', 'this', 'is', 'list'))
print(Constructor_list)
print(type(Combination_list))



# Access List

print(mylist[1])
print(mylist[2:])
print(mylist[:2])
print(mylist[2:5])
# if condition in list 
if 'apple' in mylist:
    print('Yes, Apple In the List')
else: 
    print('apple is not in the list')



# Changing/Updating the Items in the list

# replacing items
thislist = ['Java', 'Python', 'Sql', 'K8s', 'Docker','jenkins', 'Pega']
thislist[1]='AWS devops'                   # AWS devops is replaced in the index[1] (i.e 'Python')
thislist[2:3]=['pinapple', 'watermelon']
thislist.pop()                             # this removes last item in the list i.e 'Docker'
print(thislist)

# inserting items into list

thislist.insert(4,'lemon')         # adds item at the refferd index
thislist.append('kiwi')            # adds item at last
print(thislist )                   # prints the last updated list 

# adding items in one list to another list

first_list =['Ravi', 'suresh', 'naresh', 'tharun', 'srikanth']
second_list = ['Samantha', 'Keerthisuresh', 'anushka', 'thamanna', 'Sreelela']
second_list.extend(first_list)   # items in the first_list is added/inserted into the second_list
print(second_list)       


# remove list items

thislist.pop()   # removes last item in the list
thislist.remove('watermelon') # removs python from the list
thislist.pop(2)               # removes index[2] item in the list
del thislist[1]               #removes the index[1] item in the list
# del thislist                #deletes the entire list
thislist.clear()              #empties the list
print(thislist)



# Loops In the List 

#for
for i in range(len(Constructor_list)):
    print(Constructor_list[i])


nums =[1,2,3,4,5,6,7,8,9,7,6]
for num in nums :
    print(num)
for num in nums:
    if num%2 == 0:
        print(f'{num} is even')
        continue
    print(f'{num} is odd')


#While
current_list = ['alpha', 'bravo','charlie', 'delta']
i=0
while  i < len(current_list):
    print(current_list[i])
    i=i+1


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



#Sorting list Alpha 0r Numecrical
List_of_strings = ["apple", 'Banana', 'guve', 'cherry','orange']
List_of_numbers = [10,213,50,120,12,1, 242]
List_of_numbers.sort()
print(List_of_numbers)
List_of_strings.sort()
print(List_of_strings)
List_of_numbers.reverse()
print(List_of_numbers)

print(max(List_of_numbers)) # returns maximum number
print(min(List_of_numbers)) # returns minimum number
print(sum(List_of_numbers)) #returns sum of all numbers

for index, item in enumerate(List_of_strings):
    print(index, item)  #return index and value of a specific item

# Converting List into string
List_of_strings = ['apple', 'Banana', 'guve', 'cherry','orange']
String_from_list = ' '.join(List_of_strings)
print(String_from_list)

#converting string into list
cnvrtn_list ='gouri,janavi,remo,emo,happy'
cnvrtd_new_list = cnvrtn_list.split(',')
print(cnvrtd_new_list)
