user_log = []

def check_username_length(username):
    max_username_length = 11
    username_length = 0
    for letters in username:
        username_length += 1
    return username_length <= max_username_length

def check_password_length(password):
    max_password_length = 16
    password_length = 0
    for letters in password:
        password_length += 1
    return password_length <= max_password_length

def register(username, password):
    if not check_username_length(username):
        return "Username must up to 11 chars."
    if not check_password_length(password):
        return "Password must up to 16 chars."
    if any(user[0] == username for user in user_log):
        return "Username already exists."
    user_log.append([username, password])
    with open("user_info.txt", "a") as file:
        file.write(f"REGISTERED: Username =  {username} *** Password =  {password}\n")
    return "User registered successfully!"

def edit_username(old_username, new_username):
    for user in user_log:
        if user[0] == old_username:
            user[0] = new_username
            return "Username updated successfully."
        user_log.append([old_username, new_username])
    with open("user_info.txt", "a") as file:
        file.write(f"USERNAME CHANGED: Old_Username =  {old_username} *** New_Username =  {new_username}\n")
    return "Username Updated successfully!"

def login(username, password):
    if not any(user[0] == username for user in user_log):
        return "Username not found."
    if any(user[0] == username and user[1] == password for user in user_log):
        return "Login successful."
    else:
        return "Incorrect password."

def change_password(username, old_pass, new_pass):
    if not any(user[0] == username for user in user_log):
        return "Username not found."
    if any(user[0] == username and user[1] == old_pass for user in user_log):
        if not check_password_length(new_pass):
            return "New password must up to 16 chars."
        for user in user_log:
            if user[0] == username:
                user[1] = new_pass
        with open("user_info.txt", "a") as file:
            file.write(f"PASSWORD CHANGED: Username: {username} - - - New Password: {new_pass}\n")
        return "Changed Successfully!"
    else:
        return "Incorrect old password."

def main():
    while True:
        print("\nEnter No:")
        print("1 to Register")
        print("2 to Edit Username")
        print("3 to Log In")
        print("4 to Change Password")
        print("5 to Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username must up to 11 chars: ")
            password = input("Enter password must up to 16 chars: ")
            output = register(username, password)
            print(output)
        elif choice == '2':
            old_username = input("Enter current username: ")
            new_username = input("Enter new username: ")
            output = edit_username(old_username, new_username)
            print(output)
        elif choice == '3':
            username = input("Enter username: ")
            password = input("Enter password: ")
            output = login(username, password)
            print(output)
        elif choice == '4':
            username = input("Enter username: ")
            old_password = input("Enter old password: ")
            new_password = input("Enter new password must up to 16 chars): ")
            output = change_password(username, old_password, new_password)
            print(output)
        elif choice == '5':
            print("Thank you for using.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
