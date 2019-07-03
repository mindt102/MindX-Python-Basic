
while True:
    valid_name = True
    name = input("Enter name: ")
    for i in range(10):
        if str(i) in name:
            valid_name = False
    if valid_name:
        break
    else:
        print("Invalid name.")

print("Your name is:",name)
            
                        

            
    
