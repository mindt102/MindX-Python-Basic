while True:
    valid_pass = False
    password = input("Enter your password:")
    for i in range(10):
        if str(i) in password:
            valid_pass = True
    if valid_pass and length(password) > 8:
        print("Your password is: ",password)
        break
    else:
        print("Invalid password")