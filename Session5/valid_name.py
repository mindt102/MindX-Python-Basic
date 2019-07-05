
while True:
    valid_name = True
    name = input("Enter name: ")
    for i in "0123456789":
        if i in name:
            valid_name = False
    if valid_name:
        break
    else:
        print("Invalid name.")

print("Your name is:",name)
            
                        

            
    
