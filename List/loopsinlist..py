# Loops In the List 

#for
Constructor_list = (('here', 'we', 'have', 'double', 'circle', 'bracket', 'so', 'this', 'is', 'list'))
print(Constructor_list)
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
