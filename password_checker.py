# #password checker


# password = input("Please Enter your password ")

# if(password.isdigit() or password.isalpha() or password.isupper() or password.islower()):
#     print("Password isnt eligible")
# else:
#     print("Password created successfully!")


password = input("Please Enter your password ")

if(password.isdigit()):
    print("only numberic not allowed")
if(password.isalpha()):
    print("only alphabeic not allowed")
if(password.isupper()):
    print("only uppercase is not allowed")
if(password.islower()):
    print("only lowercase is not allowed")
else:
    print("Password created successfully!")
    




