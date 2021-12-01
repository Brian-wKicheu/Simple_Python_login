print("ENTER THE FOLLOWING DETAILS TO SIGN UP")
name = input("Enter your full name")
username = input("Enter your user name")
password = input("Enter password")
password_confirmation = input("Re-enter your password")
while password == password_confirmation:
    print("Account created successfully .Proceed to log in")
    break
else:
    print("Wrong credentials")

UserName = input("Enter your username")
Password = input("Enter your password")
while UserName == username and Password == password:
    print("Log in successfully")
    break
else:
    print("Username does not match password")

