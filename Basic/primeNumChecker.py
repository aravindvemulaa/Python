def PrimeNumChecker():
    Num=int(input("Enter any Number : "))
    is_prime=True
    if Num <=0:
        is_prime=False
    else:
        for i in range(2,Num):
            if Num%i==0:
                is_prime=False
                break
    if is_prime:
        print("Entered value is Prime Number")
    else:
        print("Entered Value is Not a prime Number")
def PrimeNumbers(): 
    for num in range(2, num+1):  # Start from 2 as 1 is not a prime number
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=',')

def main():
    Choice = input("Select an Option \n (C) To Check User Given Value is Prime or Not\n (P) to check what are the prime numbers from 1 to 100\n Option : ").lower() 
    if Choice=='c':
        PrimeNumChecker()
    elif Choice=='p':
        PrimeNumbers()
    else:
        print("Invalid Choice")
if __name__ == "__main__":
    main()
