
#Tuples
# A tuple is  a collection of objects that are ordered and immutable 
#Tuples are written with round bracket
# Duplicates are allowed in Tuples 

thisTuple= ('apple', 'banana','cherry','Mango')
print(thisTuple)   

# Accessing Tuples
thisTuple = ('cherry','Mango','apple', 'banana','cherry','Mango')
print(thisTuple[1])    
print(thisTuple[2:])                                 
print(thisTuple[2:5]) 
print(thisTuple[:2])  
print(thisTuple[-4])


#Update tuple
# tuples are immutable but they can be coverted into list and update and again converted into tuple
fruit_tuple = ("Apple", 'banana','cherry',"Mango")
list_tuple =list(fruit_tuple)
print(list_tuple)
list_tuple.append('guva')     # the guva is appended at last position in the list
print(list_tuple)
list_tuple.insert(3,'Grapes')   # grapes is inserted at [3] position
print(list_tuple)
New_fruit_tuple=tuple(list_tuple)   # list is converted into tuple
print(New_fruit_tuple)               # prints the  updated tuple
print(type(New_fruit_tuple))          # it will show <class 'tuple'>

#loops in tuple
fruit_tuple = ("Apple", 'banana','cherry',"Mango")
for i in range(len(fruit_tuple)):
    print(i,fruit_tuple[i])  # this will give output as index value pair
    continue
print("out of len of fruit_tuple ")


#joining tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#example 2
first_tuple=("Apple","Mango")
scnd_tuple=('banana','cherry')
thrd_tuple=first_tuple +  scnd_tuple      # we can
print(thrd_tuple)


#Multiply Tuples
first_tuple=("Apple","Mango")
new_first_tuple= first_tuple*3             
print(new_first_tuple)     

# example 2
tuple1 = ("a", "b" , "c")
print(tuple1*3)
