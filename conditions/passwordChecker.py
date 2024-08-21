# Database of user accounts
user_accounts = {}

def create_account():
    print("Create your account:")
    username = input("Enter username: ")
    password = input("Enter password: ")
    user_accounts[username] = password
    print("Account created successfully!")

def login():
    print("Login to your existing account:")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in user_accounts and user_accounts[username] == password:
        print("Login successful! Welcome,", username)
    else:
        print("Incorrect username or password. Please try again.")

def main():
    print("Welcome!")

    while True:
        choice = input("Would you like to create an account (C) or login (L)? ").lower()

        if choice == 'c':
            create_account()
        elif choice == 'l':
            login()
        else:
            print("Invalid choice. Please enter 'C' to create an account or 'L' to login.")

        another_action = input("Would you like to perform another action? (yes/no): ").lower()
        if another_action != 'yes':
            print("Thank you for using our system!")
            break

if __name__ == "__main__":
    main()
