name = input("Your full name: ")

name = name.split()

print("Updated: ",end = "")
for i in name:
    print(i.capitalize(),end = " ")