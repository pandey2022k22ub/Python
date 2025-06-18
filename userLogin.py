username = str(input("Enter your username: "))
password = str(input("Enter your password: "))
if(username == "admin" and password == "1234"):
    print("Login successful!");
else:
    if(username != "admin"):
        print("Invalid username");
    else:
        print("Invalid password");          