def login():
    password_check = False
    sign_in_check = False
    username = input("Enter your username: ")
    file = open("login_details.csv", "r")
    for line in file:
        line = line.strip()
        line = line.split(",")
        if username in line:
            while password_check == False:
                returning_password = input("Enter your password: ")
                if returning_password == line[1]:
                    password_check = True
                    sign_in_check = True
                    print(f"\033[32mAccess Granted!\033[0mWelcome back {username}")
                else:
                   print("\033[31mWRONG PASSWORD\033[0m")
    while sign_in_check == False:
        new_password = input("Enter your password: ")
        confirm_password = input("For confirmation, enter your password again: ")
        if new_password == confirm_password:
            sign_in_check = True
            cheese = open("login_details.csv", "a")
            cheese.write(f"{username},{confirm_password}\n")
            cheese.close()
    file.close()
    return username