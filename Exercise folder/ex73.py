#loops
#while loop


# DATABASE 

dbuserName = "ama"
dbPassWord = "1234"

# *User Information*

username = input("Enter username: ")
password = input("Enter password: ")

counter = 0
while username != dbuserName or password != dbPassWord:
    counter = counter + 1
    if counter==3:
        print("After three wrong attempts you have been blocked! ")
        break
    else:
        username = input("Enter correct username: ")
        password = input("Enter correct password: ")
else:
    print(f"You are welcome {username}")
