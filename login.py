from passlib.hash import pbkdf2_sha256

username_check = []
def login(username, returning_password):
    password_check = False
    sign_in_check = False
    username_low = username.lower()
    file = open("login_details.csv", "r")
    for line in file:
        line = line.strip()
        line = line.split(",")
        if username_low in line:
            if username_low not in username_check:
                correct_pass = line[1]
                if pbkdf2_sha256.verify(returning_password, correct_pass):
                    password_check = True
                    sign_in_check = True
                    username_check.append(username_low)

                    print(f"\033[32mAccess Granted!\033[0m Welcome back {username}\n")
                    return -10, username
                else:             
                    print("\033[31mWRONG PASSWORD\033[0m")
            else:
                return - 4, None
            
    file.close()
    
def sign_up(username, new_password, confirm_password):
    username_low = username.lower()
    file = open("login_details.csv", "r")
    for line in file:
         line = line.strip()
         line = line.split(",")
         if username_low in line:
             print("Username already taken")
             return -1
    if new_password == confirm_password:
          hashed_pass = pbkdf2_sha256.hash(new_password)
          sign_in_check = True
          cheese = open("login_details.csv", "a")
          cheese.write(f"{username_low},{hashed_pass}\n")
          cheese.close()
          print("\033[32mSign up successful\033[0m")
    else:
        return -2