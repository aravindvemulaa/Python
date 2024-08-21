a=int(input("Enter a Number :"))
while a<=0:
    a=int(input("Enter a Number :"))
    continue
result=1
for i in range(1,a+1):
        result*=i
print("Factorial of", a, "is", result)