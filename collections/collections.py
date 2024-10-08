# A set is a collection which is unordered, unchangeable*, and unindexed.
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.
# Duplicates Not Allowed
#a set is started using curly brackets ie  " { } "


thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)  # Duplicates will be ignored

# Access set

# You cannot access items in a set by referring to an index or a key.
#But you can loop through the 'set' items using a 'for loop',
# or ask if a specified value is present in a set, by using the 'in' keyword.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)


# updating set

# Adding new elements - use the update() method
# Once a set is created, you cannot change its items, but you can add new items.

newset = {'captain','ironman', 'winter_Soilder','hulk'}
newset.add('thor')   # we can only give one item at a time in add method
print(newset)
newset.update(["black_panther","spiderman"])  
print(newset)

set1={'a','nb','r','d'}
set2={'q','h','a'}  
set1.update(set2)   # The set2  values are added into set1 
print(set1)

set3=set2.update(set1) # ''''gives an error  the update() method for sets does not return the updated set itself.
#Instead, it performs an in-place update on the set it is called on and returns None.
#Therefore, if you try to assign the result of set2.update(set1) to set3, set3 will end up being None.''''
# so, use copy

set3=set1.copy()
set2.update(set3)
print(set3)

#removing items in set

Avengers = {'captain','ironman', 'winter_Soilder','hulk',"black_panther","spiderman"}
Avengers.remove('hulk')
print(Avengers)
Avengers.discard('black_panther')
print(Avengers)
Avengers.pop()  #removes random itemm because 
print(Avengers)
# to remove multiple  items from set we need to use for loop or list comprehension

team ={'iron man','vision','the_Wasp','ant-man','vision','blackwidow'}
team_mem_to_remove={'the_Wasp','ant-man'}
for item in team_mem_to_remove:
    team.discard(item)
print(team)

#using list comphrehension
team=[x for x in team if x not in team_mem_to_remove] #x for x in team indicates team and if x not in team_mem_to_remove :the items are found in the team_mem_to_remove then and team those are not printed 
print(team) 

#join Sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)    # returns common elements between two sets by updating y
print(x)

z = x.intersection(y)       #returns common elements between two sets without updating either sets
print(z)

x.symmetric_difference_update(y)   # Returns a new Set with different elements that are in y comparing elements in x
print(x)

z = x.symmetric_difference(y)  #Returns a new set containing elements that are in  only one of the sets (X OR Y),
print(z)

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)  #Returns the elements with symmetric difference of two sets 
print(z)
