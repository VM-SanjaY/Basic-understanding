import re  # re is short for regular expression
import maskpass
def repascheck():
    while True:
        repass = input("Please reenter your password: ")
        if repass == password:
            break
        elif repass != password:
            print("Password does not match")

while True:
    password = maskpass.askpass("Please enter a password: ")
    if len(password)<6:
        print("Your password should contain at least 6 character")
    elif re.search(r"[!@#$%&]",password) is None:
        print("your password must contain at least a special character")
    elif re.search(r"\d",password) is None:
        print("Your password should contain at least one number")
    elif re.search(r"[A-Z]",password) is None:
        print("Your password should contain at least one Capital letter")
    elif len(password)==6:
        print("password strength is weak")
        opt = input("Do you accept the password(Y/N): ").lower()
        if opt != "n":
            repascheck()
            break
    elif len(password)<8:
        print("password strength is Moderate")
        opt = input("Do you accept the password(Y/N): ").lower()
        if opt == "y":
            repascheck()
            break
    elif len(password)<10 or len(password) >10:
        print("password strength is Strong")
        opt = input("Do you accept the password(Y/N): ").lower()
        if opt == "y":
            repascheck()
            break


print("Password Created Successful")
print(password)



















