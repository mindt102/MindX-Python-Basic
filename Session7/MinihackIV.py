name = input("Enter your user name: ")

while True:
    valid_email = True
    email = input("Enter your email: ")
    loopcount = 0
    for i in email:
        loopcount += 1
        if i == "@" and loopcount < 4:
            valid_email = False
    if not valid_email:
        continue
    if ("gmail" in email or "yahoo" in email) and "@" in email and ".com" in email:
        break

while True:
    valid = False
    pw = input("Enter your password: ")
    if pw.isdigit() or len(pw) <= 8:
        continue
    for i in "0123456789":
        if i in pw:
            valid = True
    if valid:
        break
while True:
    pw2 = input("Confirm your password: ")
    if pw2 == pw:
        break
    else:
        "Error."

print("Your account has been successfully created")