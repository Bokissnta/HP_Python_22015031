#program to check password.
username = "saviour"
password = "admin555"
input_username = input("Enter your username:\t ")
input_password = input("Enter your password:\t ")

if input_username == username and input_password == password:
    print("Login successful!")
else:
    if input_username != username and input_password != password:
        print("Incorrect credentials")
    elif input_username != username:
        print("Username is incorrect")
    else:
        print("Password is incorrect")
