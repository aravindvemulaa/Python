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
