# Taking input for list of values
values = input('Enter the Numbers separated by spaces: ')

# Splitting the input string into a list of values
values_list = values.split()
print(values_list)

#Converting the list of strings into a list of integers
values_list = [int(z) for z in values_list]
print(values_list)

print("List of values entered:", values_list)

#summing all the values in list
for x in values_list:
    total_sum=sum(values_list)
    print(total_sum)
    break

