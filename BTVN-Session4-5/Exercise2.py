while True:
    n = input("Enter a number: ")
    if n.isdigit:
        n = int(n)
        if n >= 0:
            break

fac = 1
if n != 0:
    for i in range(1,n+1):
        fac *= i

print(n,"factorial is",fac)
