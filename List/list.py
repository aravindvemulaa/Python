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
