from passlib.hash import pbkdf2_sha256

username_check = []
def login(username, returning_password):
    password_check = False
    sign_in_check = False
    file = open("login_details.csv", "r")
    for line in file:
        line = line.strip()
        line = line.split(",")
        print("test")
        print(username)
        if username in line:
            if username not in username_check:
                print("test2")
                correct_pass = line[1]
                if pbkdf2_sha256.verify(returning_password, correct_pass):
                    password_check = True
                    sign_in_check = True
                    print(f"\033[32mAccess Granted!\033[0m Welcome back {username}")
                    username_check.append(username)
                    return -10, username
                else:              
                    print("\033[31mWRONG PASSWORD\033[0m")
            else:
                return - 4, None
    file.close()
    
def sign_up(username, new_password, confirm_password):
    file = open("login_details.csv", "r")
    for line in file:
         line = line.strip()
         line = line.split(",")
         if username in line:
             print("Username already taken")
             return -1
    if new_password == confirm_password:
          hashed_pass = pbkdf2_sha256.hash(new_password)
          sign_in_check = True
          cheese = open("login_details.csv", "a")
          cheese.write(f"{username},{hashed_pass}\n")
          cheese.close()
    else:
        return -2