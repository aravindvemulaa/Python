class a:
    def display(self):
        print("class a")

class b(a):
    def demo(self):
        print("class b")

class c(b):
    def test(self):
        print("class c")

obj=c()
obj.demo()
obj.display()
obj.test()



print(4 + 3 % 5)

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)

a = 3
b = 1 
print(a, b)
a, b = b, a 
print(a, b)


count = 0
while(True):
   if count % 3 == 0:
       print(count, end = " ")
   if(count > 15):
       break;
   count += 1


x = 'abcd'
for i in range(len(x)):
    print(i)

x = 123
for i in x:
    print(i)

X = 2+9*((3*12)-8)/10
print(X)


i = 5
while True:
    if i%0O11 == 0:
        break
    print(i)
    i += 1
    
i = 1
while False:
    if i%2 == 0:
        break
    print(i)
    i += 2
    
i = 1 
while True: 
  if i%3 == 0: 
      break
      print(i)  
      i  +=  1
