user_accounts={}

def create_user():
    print("create your Account")
    username=input('Enter username: ')
    password=input('Enter the password: ')
    user_accounts[username]=password
    print("Account got created successfully")

def login():
    print('login to existing account')
    username=input('Enter username: ')
    password=input('Enter the password: ')
    if username in user_accounts and user_accounts[username]==password :
        print('login is successful')
        while True:
            choice=input("would you like to do transaction(T) or view account balence(VB)").lower
            if choice=='yes':
                transaction()
            
    else:
        print('Invalid credentials, please try again')

def transaction():
    e= int(input('Enter the mobile number: '))
while True:
    f = input(f"The entered mobile number {e} is This Correct (Y/N)?").lower()
    if f == 'y':
        balence()
    else:
        e=int(input('Enter the correct mobile number: '))
        continue
else:
    print('chhoose the correct option')
    amt = float(input('Enter the  amount: '))

def balence():
    print()
